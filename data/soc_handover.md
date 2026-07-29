# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-29 |
| **Generated At** | 2026-07-29T21:01:44Z |
| **Shift Time** | 21:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **165** |
| Confirmed Threats | **151** |
| False Positives Filtered | **14** (8.5%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **30** |
| High Severity Cases | **81** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **58** |
| Unique Usernames | **36** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **82** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `operator` | 10 |
| `root` | 10 |
| `supervisor` | 7 |
| `unknown` | 5 |
| `admin` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `operator5` | 4 |
| `supervisor99` | 4 |
| `vpn` | 4 |
| `qwerty1234` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 5 |
| `operator` | `operator5` | 4 |
| `supervisor` | `supervisor99` | 4 |
| `vpn` | `vpn` | 4 |
| `operator` | `qwerty1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `operator` | `operator5` | `10.0.0.73` | 2026-07-29T19:02:13 |
| `support` | `support` | `10.0.0.73` | 2026-07-29T19:03:35 |
| `sshd` | `admin234567` | `218.149.228.135` | 2026-07-29T19:06:22 |
| `root` | `1234.com` | `46.253.45.10` | 2026-07-29T19:09:55 |
| `345gs5662d34` | `345gs5662d34` | `46.253.45.10` | 2026-07-29T19:09:58 |
| `root` | `3245gs5662d34` | `46.253.45.10` | 2026-07-29T19:09:58 |
| `unknown` | `unknown12345` | `106.13.181.87` | 2026-07-29T19:13:10 |
| `unknown` | `unknown12345` | `78.186.54.65` | 2026-07-29T19:13:19 |
| `operator` | `operator5` | `181.129.31.42` | 2026-07-29T19:16:57 |
| `operator` | `operator5` | `103.147.248.44` | 2026-07-29T19:17:06 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-29T19:18:03 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-29T19:18:03 |
| `root` | `44444444` | `121.202.206.119` | 2026-07-29T19:22:11 |
| `root` | `44444444` | `45.170.50.2` | 2026-07-29T19:22:20 |
| `support` | `support` | `176.53.159.196` | 2026-07-29T19:25:34 |
| `root` | `` | `91.92.40.18` | 2026-07-29T19:29:12 |
| `raspberry` | `admin` | `193.24.211.76` | 2026-07-29T19:29:55 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-29T19:36:56 |
| `supervisor` | `supervisor99` | `10.0.0.73` | 2026-07-29T19:37:10 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-29T19:38:51 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-29T19:40:50 |
| `squid` | `squid` | `183.247.171.186` | 2026-07-29T19:41:03 |
| `supervisor` | `supervisor99` | `181.233.140.250` | 2026-07-29T19:42:13 |
| `unknown` | `unknown12345` | `220.122.115.9` | 2026-07-29T19:42:31 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-29T19:42:41 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-29T19:44:27 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-29T19:46:14 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-29T19:46:27 |
| `admin` | `admin` | `147.139.136.75` | 2026-07-29T19:47:33 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-29T19:47:34 |
| `vpn` | `vpn` | `124.88.174.143` | 2026-07-29T19:47:53 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-29T19:48:06 |
| `node` | `node` | `2.57.122.238` | 2026-07-29T19:49:54 |
| `supervisor` | `supervisor99` | `111.70.38.54` | 2026-07-29T19:50:11 |
| `node` | `1234` | `2.57.122.238` | 2026-07-29T19:51:48 |
| `node` | `123456` | `2.57.122.238` | 2026-07-29T19:53:46 |
| `support` | `4444` | `10.0.0.73` | 2026-07-29T19:55:38 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-29T19:55:42 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-29T19:57:30 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-29T19:59:21 |
| `vpn` | `vpn` | `10.0.0.73` | 2026-07-29T19:59:39 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-29T20:01:13 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-29T20:03:02 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-29T20:04:53 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-29T20:04:53 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-29T20:06:51 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-29T20:08:34 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-29T20:10:10 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-29T20:11:46 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-29T20:13:22 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-29T20:14:57 |
| `default` | `qwerty12345` | `208.109.38.143` | 2026-07-29T20:15:56 |
| `default` | `qwerty12345` | `70.91.135.181` | 2026-07-29T20:16:03 |
| `default` | `qwerty12345` | `37.28.177.141` | 2026-07-29T20:16:13 |
| `supervisor` | `1qaz2wsx` | `221.8.22.14` | 2026-07-29T20:16:26 |
| `supervisor` | `1qaz2wsx` | `82.65.140.218` | 2026-07-29T20:16:38 |
| `vpn` | `vpn` | `124.239.129.2` | 2026-07-29T20:17:30 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-29T20:19:43 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-29T20:21:21 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-29T20:22:57 |
| `supervisor` | `1qaz2wsx` | `194.31.8.12` | 2026-07-29T20:24:19 |
| `sol` | `123` | `2.57.122.238` | 2026-07-29T20:24:37 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-29T20:26:15 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-29T20:27:51 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-29T20:29:24 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-07-29T20:31:00 |
| `blank` | `blank55` | `123.129.245.249` | 2026-07-29T20:32:13 |
| `bot` | `bot` | `2.57.122.238` | 2026-07-29T20:32:38 |
| `bot` | `123456` | `2.57.122.238` | 2026-07-29T20:34:12 |
| `unknown` | `unknown10` | `10.0.0.73` | 2026-07-29T20:34:40 |
| `bot` | `12345` | `2.57.122.238` | 2026-07-29T20:35:48 |
| `blank` | `blank55` | `77.106.78.215` | 2026-07-29T20:48:55 |
| `operator` | `operator4` | `125.25.183.157` | 2026-07-29T20:50:02 |
| `operator` | `operator4` | `113.193.187.154` | 2026-07-29T20:50:14 |
| `operator` | `qwerty1234` | `39.164.94.190` | 2026-07-29T20:50:38 |
| `operator` | `qwerty1234` | `183.167.217.86` | 2026-07-29T20:50:50 |
| `operator` | `qwerty1234` | `58.56.128.190` | 2026-07-29T20:50:51 |
| `operator` | `qwerty1234` | `65.20.134.97` | 2026-07-29T20:50:58 |
| `unknown` | `unknown10` | `116.228.195.251` | 2026-07-29T20:52:26 |
| `boss` | `boss@123` | `187.212.37.143` | 2026-07-29T20:54:54 |
| `345gs5662d34` | `345gs5662d34` | `187.212.37.143` | 2026-07-29T20:54:56 |
| `boss` | `3245gs5662d34` | `187.212.37.143` | 2026-07-29T20:54:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **165** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| OpenSSH | 29 |
| libssh | 19 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 35 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 29 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 35 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 29 | 29 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `187.212.37.143`, `46.253.45.10`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **56** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS46562` | Performive LLC | 3 | LOW |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (81)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c6394bf6fae6

| Field | Detail |
|---|---|
| **Source IP** | `218.149.228[.]135` |
| **First Seen** | 2026-07-29 19:06 |
| **Last Seen** | 2026-07-29 19:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:06:19` | `cowrie.session.connect` |
| `2026-07-29 19:06:20` | `cowrie.client.version` |
| `2026-07-29 19:06:20` | `cowrie.client.kex` |
| `2026-07-29 19:06:22` | `cowrie.login.success` |
| `2026-07-29 19:06:22` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.228[.]135` to AbuseIPDB if not already reported
- [ ] Block `218.149.228[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c73de715e23

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-07-29 19:09 |
| **Last Seen** | 2026-07-29 19:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:09:55` | `cowrie.session.connect` |
| `2026-07-29 19:09:55` | `cowrie.client.version` |
| `2026-07-29 19:09:55` | `cowrie.client.kex` |
| `2026-07-29 19:09:55` | `cowrie.login.success` |
| `2026-07-29 19:09:56` | `cowrie.session.params` |
| `2026-07-29 19:09:56` | `cowrie.command.input` |
| `2026-07-29 19:09:56` | `cowrie.command.failed` |
| `2026-07-29 19:09:56` | `cowrie.log.closed` |
| `2026-07-29 19:09:57` | `cowrie.session.params` |
| `2026-07-29 19:09:57` | `cowrie.command.input` |
| `2026-07-29 19:09:57` | `cowrie.session.file_download` |
| `2026-07-29 19:09:57` | `cowrie.log.closed` |
| `2026-07-29 19:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb98c6d4ef0

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-07-29 19:09 |
| **Last Seen** | 2026-07-29 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:09:57` | `cowrie.session.connect` |
| `2026-07-29 19:09:57` | `cowrie.client.version` |
| `2026-07-29 19:09:57` | `cowrie.client.kex` |
| `2026-07-29 19:09:58` | `cowrie.login.success` |
| `2026-07-29 19:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caafb655b041

| Field | Detail |
|---|---|
| **Source IP** | `46.253.45[.]10` |
| **First Seen** | 2026-07-29 19:09 |
| **Last Seen** | 2026-07-29 19:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:09:58` | `cowrie.session.connect` |
| `2026-07-29 19:09:58` | `cowrie.client.version` |
| `2026-07-29 19:09:58` | `cowrie.client.kex` |
| `2026-07-29 19:09:58` | `cowrie.login.success` |
| `2026-07-29 19:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.253.45[.]10` to AbuseIPDB if not already reported
- [ ] Block `46.253.45[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda353b7526e

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]87` |
| **First Seen** | 2026-07-29 19:13 |
| **Last Seen** | 2026-07-29 19:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:13:04` | `cowrie.session.connect` |
| `2026-07-29 19:13:06` | `cowrie.client.version` |
| `2026-07-29 19:13:06` | `cowrie.client.kex` |
| `2026-07-29 19:13:10` | `cowrie.login.success` |
| `2026-07-29 19:13:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]87` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af183df1cc33

| Field | Detail |
|---|---|
| **Source IP** | `78.186.54[.]65` |
| **First Seen** | 2026-07-29 19:13 |
| **Last Seen** | 2026-07-29 19:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:13:17` | `cowrie.session.connect` |
| `2026-07-29 19:13:18` | `cowrie.client.version` |
| `2026-07-29 19:13:18` | `cowrie.client.kex` |
| `2026-07-29 19:13:19` | `cowrie.login.success` |
| `2026-07-29 19:13:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.186.54[.]65` to AbuseIPDB if not already reported
- [ ] Block `78.186.54[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da496836c43

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-29 19:16 |
| **Last Seen** | 2026-07-29 19:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:16:54` | `cowrie.session.connect` |
| `2026-07-29 19:16:55` | `cowrie.client.version` |
| `2026-07-29 19:16:55` | `cowrie.client.kex` |
| `2026-07-29 19:16:57` | `cowrie.login.success` |
| `2026-07-29 19:16:57` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1faa440e4a49

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-07-29 19:17 |
| **Last Seen** | 2026-07-29 19:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:17:03` | `cowrie.session.connect` |
| `2026-07-29 19:17:03` | `cowrie.client.version` |
| `2026-07-29 19:17:03` | `cowrie.client.kex` |
| `2026-07-29 19:17:06` | `cowrie.login.success` |
| `2026-07-29 19:17:06` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69bc3cdde65

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 19:18 |
| **Last Seen** | 2026-07-29 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:18:02` | `cowrie.session.connect` |
| `2026-07-29 19:18:02` | `cowrie.client.version` |
| `2026-07-29 19:18:02` | `cowrie.client.kex` |
| `2026-07-29 19:18:03` | `cowrie.login.success` |
| `2026-07-29 19:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6cbe040357

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 19:18 |
| **Last Seen** | 2026-07-29 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:18:02` | `cowrie.session.connect` |
| `2026-07-29 19:18:02` | `cowrie.client.version` |
| `2026-07-29 19:18:02` | `cowrie.client.kex` |
| `2026-07-29 19:18:03` | `cowrie.login.success` |
| `2026-07-29 19:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793f5ac5cb23

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-07-29 19:22 |
| **Last Seen** | 2026-07-29 19:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:22:08` | `cowrie.session.connect` |
| `2026-07-29 19:22:09` | `cowrie.client.version` |
| `2026-07-29 19:22:09` | `cowrie.client.kex` |
| `2026-07-29 19:22:11` | `cowrie.login.success` |
| `2026-07-29 19:22:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44a08cf613c

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-07-29 19:22 |
| **Last Seen** | 2026-07-29 19:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:22:18` | `cowrie.session.connect` |
| `2026-07-29 19:22:18` | `cowrie.client.version` |
| `2026-07-29 19:22:18` | `cowrie.client.kex` |
| `2026-07-29 19:22:20` | `cowrie.login.success` |
| `2026-07-29 19:22:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ef8bf90c9f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-29 19:25 |
| **Last Seen** | 2026-07-29 19:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:25:34` | `cowrie.session.connect` |
| `2026-07-29 19:25:34` | `cowrie.client.version` |
| `2026-07-29 19:25:34` | `cowrie.client.kex` |
| `2026-07-29 19:25:34` | `cowrie.login.success` |
| `2026-07-29 19:25:34` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:25:34` | `cowrie.direct-tcpip.data` |
| `2026-07-29 19:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a377b7bcb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 19:29 |
| **Last Seen** | 2026-07-29 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:29:12` | `cowrie.session.connect` |
| `2026-07-29 19:29:12` | `cowrie.login.success` |
| `2026-07-29 19:29:13` | `cowrie.session.params` |
| `2026-07-29 19:29:13` | `cowrie.command.input` |
| `2026-07-29 19:29:14` | `cowrie.log.closed` |
| `2026-07-29 19:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a1d2435b30a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]18` |
| **First Seen** | 2026-07-29 19:29 |
| **Last Seen** | 2026-07-29 19:30 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo WRITABLE >/tmp/.testfile 2>&1, ls -l /tmp/.testfile 2>&1, rm -f /tmp/.testfile, cd /tmp, for pid in /proc/[0-9]*; do pid_num="${pid##*/}"; if [ -r "$pid/maps" ]; then suspicious=true; while IFS= read -r line; do case "$line" in *"/lib/"*|*"/lib64/"*|*".so"*) suspicious=false; break;; esac; done < "$pid/maps"; if [ "$suspicious" = true ]; then kill -9 "$pid_num" 2>/dev/null; fi; fi; done;` |
| **Download Attempts** | hxxp://91.199.133[.]133:8080/deploy.sh, hxxp://91.199.133[.]133:8080/deploy.sh, 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 |
| **Malware Analysis** | 0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1222.002 · T1489 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:29:14` | `cowrie.session.connect` |
| `2026-07-29 19:29:15` | `cowrie.login.success` |
| `2026-07-29 19:29:16` | `cowrie.session.params` |
| `2026-07-29 19:29:16` | `cowrie.command.input` |
| `2026-07-29 19:29:17` | `cowrie.command.input` |
| `2026-07-29 19:29:18` | `cowrie.command.input` |
| `2026-07-29 19:29:18` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.failed` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:19` | `cowrie.command.input` |
| `2026-07-29 19:29:20` | `cowrie.session.file_download` |
| `2026-07-29 19:29:20` | `cowrie.session.file_download.failed` |
| `2026-07-29 19:29:20` | `cowrie.session.file_download` |
| `2026-07-29 19:29:39` | `cowrie.command.input` |
| `2026-07-29 19:29:41` | `cowrie.command.input` |
| `2026-07-29 19:29:42` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.input` |
| `2026-07-29 19:29:43` | `cowrie.command.failed` |
| `2026-07-29 19:29:43` | `cowrie.command.failed` |
| `2026-07-29 19:29:43` | `cowrie.command.failed` |
| `2026-07-29 19:29:43` | `cowrie.command.failed` |
| `2026-07-29 19:30:08` | `cowrie.session.input` |
| `2026-07-29 19:30:10` | `cowrie.session.file_download` |
| `2026-07-29 19:30:10` | `cowrie.session.file_download` |
| `2026-07-29 19:30:10` | `cowrie.log.closed` |
| `2026-07-29 19:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]18` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc8b1d7adf4

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]76` |
| **First Seen** | 2026-07-29 19:29 |
| **Last Seen** | 2026-07-29 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:29:54` | `cowrie.session.connect` |
| `2026-07-29 19:29:54` | `cowrie.client.version` |
| `2026-07-29 19:29:54` | `cowrie.client.kex` |
| `2026-07-29 19:29:55` | `cowrie.login.success` |
| `2026-07-29 19:29:55` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:29:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-29 19:29:55` | `cowrie.direct-tcpip.data` |
| `2026-07-29 19:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]76` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f978860da242

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:36 |
| **Last Seen** | 2026-07-29 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:36:56` | `cowrie.session.connect` |
| `2026-07-29 19:36:56` | `cowrie.client.version` |
| `2026-07-29 19:36:56` | `cowrie.client.kex` |
| `2026-07-29 19:36:56` | `cowrie.login.success` |
| `2026-07-29 19:36:57` | `cowrie.session.params` |
| `2026-07-29 19:36:57` | `cowrie.command.input` |
| `2026-07-29 19:36:57` | `cowrie.log.closed` |
| `2026-07-29 19:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b84b87b788

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:38 |
| **Last Seen** | 2026-07-29 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:38:51` | `cowrie.session.connect` |
| `2026-07-29 19:38:51` | `cowrie.client.version` |
| `2026-07-29 19:38:51` | `cowrie.client.kex` |
| `2026-07-29 19:38:51` | `cowrie.login.success` |
| `2026-07-29 19:38:52` | `cowrie.session.params` |
| `2026-07-29 19:38:52` | `cowrie.command.input` |
| `2026-07-29 19:38:52` | `cowrie.log.closed` |
| `2026-07-29 19:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c75fd60075

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:40 |
| **Last Seen** | 2026-07-29 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:40:50` | `cowrie.session.connect` |
| `2026-07-29 19:40:50` | `cowrie.client.version` |
| `2026-07-29 19:40:50` | `cowrie.client.kex` |
| `2026-07-29 19:40:50` | `cowrie.login.success` |
| `2026-07-29 19:40:51` | `cowrie.session.params` |
| `2026-07-29 19:40:51` | `cowrie.command.input` |
| `2026-07-29 19:40:51` | `cowrie.log.closed` |
| `2026-07-29 19:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c56d25a827

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-07-29 19:40 |
| **Last Seen** | 2026-07-29 19:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:40:58` | `cowrie.session.connect` |
| `2026-07-29 19:41:00` | `cowrie.client.version` |
| `2026-07-29 19:41:00` | `cowrie.client.kex` |
| `2026-07-29 19:41:03` | `cowrie.login.success` |
| `2026-07-29 19:41:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9e7358d895

| Field | Detail |
|---|---|
| **Source IP** | `181.233.140[.]250` |
| **First Seen** | 2026-07-29 19:42 |
| **Last Seen** | 2026-07-29 19:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:42:11` | `cowrie.session.connect` |
| `2026-07-29 19:42:12` | `cowrie.client.version` |
| `2026-07-29 19:42:12` | `cowrie.client.kex` |
| `2026-07-29 19:42:13` | `cowrie.login.success` |
| `2026-07-29 19:42:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.140[.]250` to AbuseIPDB if not already reported
- [ ] Block `181.233.140[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175e7785811f

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-29 19:42 |
| **Last Seen** | 2026-07-29 19:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:42:28` | `cowrie.session.connect` |
| `2026-07-29 19:42:29` | `cowrie.client.version` |
| `2026-07-29 19:42:29` | `cowrie.client.kex` |
| `2026-07-29 19:42:31` | `cowrie.login.success` |
| `2026-07-29 19:42:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e2271ec0d7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:42 |
| **Last Seen** | 2026-07-29 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:42:40` | `cowrie.session.connect` |
| `2026-07-29 19:42:40` | `cowrie.client.version` |
| `2026-07-29 19:42:40` | `cowrie.client.kex` |
| `2026-07-29 19:42:41` | `cowrie.login.success` |
| `2026-07-29 19:42:41` | `cowrie.session.params` |
| `2026-07-29 19:42:41` | `cowrie.command.input` |
| `2026-07-29 19:42:42` | `cowrie.log.closed` |
| `2026-07-29 19:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6cc46279f0a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:44 |
| **Last Seen** | 2026-07-29 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:44:26` | `cowrie.session.connect` |
| `2026-07-29 19:44:26` | `cowrie.client.version` |
| `2026-07-29 19:44:26` | `cowrie.client.kex` |
| `2026-07-29 19:44:27` | `cowrie.login.success` |
| `2026-07-29 19:44:27` | `cowrie.session.params` |
| `2026-07-29 19:44:27` | `cowrie.command.input` |
| `2026-07-29 19:44:27` | `cowrie.log.closed` |
| `2026-07-29 19:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8f4a8b28f5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:46 |
| **Last Seen** | 2026-07-29 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:46:14` | `cowrie.session.connect` |
| `2026-07-29 19:46:14` | `cowrie.client.version` |
| `2026-07-29 19:46:14` | `cowrie.client.kex` |
| `2026-07-29 19:46:14` | `cowrie.login.success` |
| `2026-07-29 19:46:15` | `cowrie.session.params` |
| `2026-07-29 19:46:15` | `cowrie.command.input` |
| `2026-07-29 19:46:15` | `cowrie.log.closed` |
| `2026-07-29 19:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82c68b601824

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-29 19:46 |
| **Last Seen** | 2026-07-29 19:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:46:26` | `cowrie.session.connect` |
| `2026-07-29 19:46:26` | `cowrie.client.version` |
| `2026-07-29 19:46:26` | `cowrie.client.kex` |
| `2026-07-29 19:46:27` | `cowrie.login.success` |
| `2026-07-29 19:46:27` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:46:27` | `cowrie.direct-tcpip.ja4` |
| `2026-07-29 19:46:27` | `cowrie.direct-tcpip.data` |
| `2026-07-29 19:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c541017a07

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-07-29 19:47 |
| **Last Seen** | 2026-07-29 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:47:32` | `cowrie.session.connect` |
| `2026-07-29 19:47:32` | `cowrie.client.version` |
| `2026-07-29 19:47:33` | `cowrie.client.kex` |
| `2026-07-29 19:47:33` | `cowrie.login.success` |
| `2026-07-29 19:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910cbd391749

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-29 19:47 |
| **Last Seen** | 2026-07-29 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:47:34` | `cowrie.session.connect` |
| `2026-07-29 19:47:34` | `cowrie.client.version` |
| `2026-07-29 19:47:34` | `cowrie.client.kex` |
| `2026-07-29 19:47:34` | `cowrie.login.success` |
| `2026-07-29 19:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ab58ba5c038

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-29 19:47 |
| **Last Seen** | 2026-07-29 19:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:47:50` | `cowrie.session.connect` |
| `2026-07-29 19:47:51` | `cowrie.client.version` |
| `2026-07-29 19:47:51` | `cowrie.client.kex` |
| `2026-07-29 19:47:53` | `cowrie.login.success` |
| `2026-07-29 19:47:53` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba372e50be6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:48 |
| **Last Seen** | 2026-07-29 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:48:05` | `cowrie.session.connect` |
| `2026-07-29 19:48:05` | `cowrie.client.version` |
| `2026-07-29 19:48:05` | `cowrie.client.kex` |
| `2026-07-29 19:48:06` | `cowrie.login.success` |
| `2026-07-29 19:48:06` | `cowrie.session.params` |
| `2026-07-29 19:48:06` | `cowrie.command.input` |
| `2026-07-29 19:48:07` | `cowrie.log.closed` |
| `2026-07-29 19:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0e9164e3f3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:49 |
| **Last Seen** | 2026-07-29 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:49:54` | `cowrie.session.connect` |
| `2026-07-29 19:49:54` | `cowrie.client.version` |
| `2026-07-29 19:49:54` | `cowrie.client.kex` |
| `2026-07-29 19:49:54` | `cowrie.login.success` |
| `2026-07-29 19:49:55` | `cowrie.session.params` |
| `2026-07-29 19:49:55` | `cowrie.command.input` |
| `2026-07-29 19:49:55` | `cowrie.log.closed` |
| `2026-07-29 19:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24331012d0b2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.38[.]54` |
| **First Seen** | 2026-07-29 19:50 |
| **Last Seen** | 2026-07-29 19:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:50:08` | `cowrie.session.connect` |
| `2026-07-29 19:50:08` | `cowrie.client.version` |
| `2026-07-29 19:50:09` | `cowrie.client.kex` |
| `2026-07-29 19:50:11` | `cowrie.login.success` |
| `2026-07-29 19:50:12` | `cowrie.direct-tcpip.request` |
| `2026-07-29 19:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `111.70.38[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d326c7cf120

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:51 |
| **Last Seen** | 2026-07-29 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:51:48` | `cowrie.session.connect` |
| `2026-07-29 19:51:48` | `cowrie.client.version` |
| `2026-07-29 19:51:48` | `cowrie.client.kex` |
| `2026-07-29 19:51:48` | `cowrie.login.success` |
| `2026-07-29 19:51:49` | `cowrie.session.params` |
| `2026-07-29 19:51:49` | `cowrie.command.input` |
| `2026-07-29 19:51:49` | `cowrie.log.closed` |
| `2026-07-29 19:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c26e9525ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:53 |
| **Last Seen** | 2026-07-29 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:53:46` | `cowrie.session.connect` |
| `2026-07-29 19:53:46` | `cowrie.client.version` |
| `2026-07-29 19:53:46` | `cowrie.client.kex` |
| `2026-07-29 19:53:46` | `cowrie.login.success` |
| `2026-07-29 19:53:47` | `cowrie.session.params` |
| `2026-07-29 19:53:47` | `cowrie.command.input` |
| `2026-07-29 19:53:47` | `cowrie.log.closed` |
| `2026-07-29 19:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6abf3f10c59

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:55 |
| **Last Seen** | 2026-07-29 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:55:41` | `cowrie.session.connect` |
| `2026-07-29 19:55:41` | `cowrie.client.version` |
| `2026-07-29 19:55:41` | `cowrie.client.kex` |
| `2026-07-29 19:55:42` | `cowrie.login.success` |
| `2026-07-29 19:55:43` | `cowrie.session.params` |
| `2026-07-29 19:55:43` | `cowrie.command.input` |
| `2026-07-29 19:55:43` | `cowrie.log.closed` |
| `2026-07-29 19:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f080611fbf70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:57 |
| **Last Seen** | 2026-07-29 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:57:30` | `cowrie.session.connect` |
| `2026-07-29 19:57:30` | `cowrie.client.version` |
| `2026-07-29 19:57:30` | `cowrie.client.kex` |
| `2026-07-29 19:57:30` | `cowrie.login.success` |
| `2026-07-29 19:57:31` | `cowrie.session.params` |
| `2026-07-29 19:57:31` | `cowrie.command.input` |
| `2026-07-29 19:57:31` | `cowrie.log.closed` |
| `2026-07-29 19:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24bb6029d7b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 19:59 |
| **Last Seen** | 2026-07-29 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 19:59:21` | `cowrie.session.connect` |
| `2026-07-29 19:59:21` | `cowrie.client.version` |
| `2026-07-29 19:59:21` | `cowrie.client.kex` |
| `2026-07-29 19:59:21` | `cowrie.login.success` |
| `2026-07-29 19:59:22` | `cowrie.session.params` |
| `2026-07-29 19:59:22` | `cowrie.command.input` |
| `2026-07-29 19:59:22` | `cowrie.log.closed` |
| `2026-07-29 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d564f500531

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-29 20:00 |
| **Last Seen** | 2026-07-29 20:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:00:45` | `cowrie.session.connect` |
| `2026-07-29 20:00:45` | `cowrie.client.version` |
| `2026-07-29 20:00:45` | `cowrie.client.kex` |
| `2026-07-29 20:00:45` | `cowrie.login.success` |
| `2026-07-29 20:00:45` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:00:45` | `cowrie.direct-tcpip.ja4` |
| `2026-07-29 20:00:45` | `cowrie.direct-tcpip.data` |
| `2026-07-29 20:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e0fdb7feec

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:01 |
| **Last Seen** | 2026-07-29 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:01:12` | `cowrie.session.connect` |
| `2026-07-29 20:01:12` | `cowrie.client.version` |
| `2026-07-29 20:01:12` | `cowrie.client.kex` |
| `2026-07-29 20:01:13` | `cowrie.login.success` |
| `2026-07-29 20:01:14` | `cowrie.session.params` |
| `2026-07-29 20:01:14` | `cowrie.command.input` |
| `2026-07-29 20:01:14` | `cowrie.log.closed` |
| `2026-07-29 20:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db9aec00644

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:03 |
| **Last Seen** | 2026-07-29 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:03:02` | `cowrie.session.connect` |
| `2026-07-29 20:03:02` | `cowrie.client.version` |
| `2026-07-29 20:03:02` | `cowrie.client.kex` |
| `2026-07-29 20:03:02` | `cowrie.login.success` |
| `2026-07-29 20:03:03` | `cowrie.session.params` |
| `2026-07-29 20:03:03` | `cowrie.command.input` |
| `2026-07-29 20:03:03` | `cowrie.log.closed` |
| `2026-07-29 20:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7006a16560f7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:04 |
| **Last Seen** | 2026-07-29 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:04:52` | `cowrie.session.connect` |
| `2026-07-29 20:04:52` | `cowrie.client.version` |
| `2026-07-29 20:04:53` | `cowrie.client.kex` |
| `2026-07-29 20:04:53` | `cowrie.login.success` |
| `2026-07-29 20:04:54` | `cowrie.session.params` |
| `2026-07-29 20:04:54` | `cowrie.command.input` |
| `2026-07-29 20:04:54` | `cowrie.log.closed` |
| `2026-07-29 20:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc35aba7493b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:06 |
| **Last Seen** | 2026-07-29 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:06:51` | `cowrie.session.connect` |
| `2026-07-29 20:06:51` | `cowrie.client.version` |
| `2026-07-29 20:06:51` | `cowrie.client.kex` |
| `2026-07-29 20:06:51` | `cowrie.login.success` |
| `2026-07-29 20:06:52` | `cowrie.session.params` |
| `2026-07-29 20:06:52` | `cowrie.command.input` |
| `2026-07-29 20:06:52` | `cowrie.log.closed` |
| `2026-07-29 20:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc77d38dfca

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:08 |
| **Last Seen** | 2026-07-29 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:08:34` | `cowrie.session.connect` |
| `2026-07-29 20:08:34` | `cowrie.client.version` |
| `2026-07-29 20:08:34` | `cowrie.client.kex` |
| `2026-07-29 20:08:34` | `cowrie.login.success` |
| `2026-07-29 20:08:35` | `cowrie.session.params` |
| `2026-07-29 20:08:35` | `cowrie.command.input` |
| `2026-07-29 20:08:35` | `cowrie.log.closed` |
| `2026-07-29 20:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057a4c2826b6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:10 |
| **Last Seen** | 2026-07-29 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:10:10` | `cowrie.session.connect` |
| `2026-07-29 20:10:10` | `cowrie.client.version` |
| `2026-07-29 20:10:10` | `cowrie.client.kex` |
| `2026-07-29 20:10:10` | `cowrie.login.success` |
| `2026-07-29 20:10:11` | `cowrie.session.params` |
| `2026-07-29 20:10:11` | `cowrie.command.input` |
| `2026-07-29 20:10:11` | `cowrie.log.closed` |
| `2026-07-29 20:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c383d4c3dc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:11 |
| **Last Seen** | 2026-07-29 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:11:45` | `cowrie.session.connect` |
| `2026-07-29 20:11:45` | `cowrie.client.version` |
| `2026-07-29 20:11:45` | `cowrie.client.kex` |
| `2026-07-29 20:11:46` | `cowrie.login.success` |
| `2026-07-29 20:11:47` | `cowrie.session.params` |
| `2026-07-29 20:11:47` | `cowrie.command.input` |
| `2026-07-29 20:11:47` | `cowrie.log.closed` |
| `2026-07-29 20:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c072bda56f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:13 |
| **Last Seen** | 2026-07-29 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:13:22` | `cowrie.session.connect` |
| `2026-07-29 20:13:22` | `cowrie.client.version` |
| `2026-07-29 20:13:22` | `cowrie.client.kex` |
| `2026-07-29 20:13:22` | `cowrie.login.success` |
| `2026-07-29 20:13:23` | `cowrie.session.params` |
| `2026-07-29 20:13:23` | `cowrie.command.input` |
| `2026-07-29 20:13:23` | `cowrie.log.closed` |
| `2026-07-29 20:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad309461959

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:14 |
| **Last Seen** | 2026-07-29 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:14:57` | `cowrie.session.connect` |
| `2026-07-29 20:14:57` | `cowrie.client.version` |
| `2026-07-29 20:14:57` | `cowrie.client.kex` |
| `2026-07-29 20:14:57` | `cowrie.login.success` |
| `2026-07-29 20:14:58` | `cowrie.session.params` |
| `2026-07-29 20:14:58` | `cowrie.command.input` |
| `2026-07-29 20:14:58` | `cowrie.log.closed` |
| `2026-07-29 20:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382063545f64

| Field | Detail |
|---|---|
| **Source IP** | `208.109.38[.]143` |
| **First Seen** | 2026-07-29 20:15 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:15:53` | `cowrie.session.connect` |
| `2026-07-29 20:15:54` | `cowrie.client.version` |
| `2026-07-29 20:15:54` | `cowrie.client.kex` |
| `2026-07-29 20:15:56` | `cowrie.login.success` |
| `2026-07-29 20:15:56` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.109.38[.]143` to AbuseIPDB if not already reported
- [ ] Block `208.109.38[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c103f35e06a

| Field | Detail |
|---|---|
| **Source IP** | `70.91.135[.]181` |
| **First Seen** | 2026-07-29 20:16 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:16:02` | `cowrie.session.connect` |
| `2026-07-29 20:16:02` | `cowrie.client.version` |
| `2026-07-29 20:16:02` | `cowrie.client.kex` |
| `2026-07-29 20:16:03` | `cowrie.login.success` |
| `2026-07-29 20:16:04` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.91.135[.]181` to AbuseIPDB if not already reported
- [ ] Block `70.91.135[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78afedc93dfb

| Field | Detail |
|---|---|
| **Source IP** | `37.28.177[.]141` |
| **First Seen** | 2026-07-29 20:16 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:16:12` | `cowrie.session.connect` |
| `2026-07-29 20:16:12` | `cowrie.client.version` |
| `2026-07-29 20:16:12` | `cowrie.client.kex` |
| `2026-07-29 20:16:13` | `cowrie.login.success` |
| `2026-07-29 20:16:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.28.177[.]141` to AbuseIPDB if not already reported
- [ ] Block `37.28.177[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fba44f5f59

| Field | Detail |
|---|---|
| **Source IP** | `221.8.22[.]14` |
| **First Seen** | 2026-07-29 20:16 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:16:22` | `cowrie.session.connect` |
| `2026-07-29 20:16:23` | `cowrie.client.version` |
| `2026-07-29 20:16:23` | `cowrie.client.kex` |
| `2026-07-29 20:16:26` | `cowrie.login.success` |
| `2026-07-29 20:16:26` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.8.22[.]14` to AbuseIPDB if not already reported
- [ ] Block `221.8.22[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8079876ef4c3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:16 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:16:29` | `cowrie.session.connect` |
| `2026-07-29 20:16:29` | `cowrie.client.version` |
| `2026-07-29 20:16:29` | `cowrie.client.kex` |
| `2026-07-29 20:16:30` | `cowrie.login.success` |
| `2026-07-29 20:16:30` | `cowrie.session.params` |
| `2026-07-29 20:16:30` | `cowrie.command.input` |
| `2026-07-29 20:16:30` | `cowrie.log.closed` |
| `2026-07-29 20:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-714c9bfeedd1

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-29 20:16 |
| **Last Seen** | 2026-07-29 20:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:16:36` | `cowrie.session.connect` |
| `2026-07-29 20:16:36` | `cowrie.client.version` |
| `2026-07-29 20:16:36` | `cowrie.client.kex` |
| `2026-07-29 20:16:38` | `cowrie.login.success` |
| `2026-07-29 20:16:38` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5f54fab0eb

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-29 20:17 |
| **Last Seen** | 2026-07-29 20:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:17:28` | `cowrie.session.connect` |
| `2026-07-29 20:17:29` | `cowrie.client.version` |
| `2026-07-29 20:17:29` | `cowrie.client.kex` |
| `2026-07-29 20:17:30` | `cowrie.login.success` |
| `2026-07-29 20:17:31` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c66203e8c7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:18 |
| **Last Seen** | 2026-07-29 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:18:04` | `cowrie.session.connect` |
| `2026-07-29 20:18:04` | `cowrie.client.version` |
| `2026-07-29 20:18:05` | `cowrie.client.kex` |
| `2026-07-29 20:18:05` | `cowrie.login.success` |
| `2026-07-29 20:18:06` | `cowrie.session.params` |
| `2026-07-29 20:18:06` | `cowrie.command.input` |
| `2026-07-29 20:18:06` | `cowrie.log.closed` |
| `2026-07-29 20:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1011cc87f45

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:19 |
| **Last Seen** | 2026-07-29 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:19:42` | `cowrie.session.connect` |
| `2026-07-29 20:19:42` | `cowrie.client.version` |
| `2026-07-29 20:19:42` | `cowrie.client.kex` |
| `2026-07-29 20:19:43` | `cowrie.login.success` |
| `2026-07-29 20:19:44` | `cowrie.session.params` |
| `2026-07-29 20:19:44` | `cowrie.command.input` |
| `2026-07-29 20:19:44` | `cowrie.log.closed` |
| `2026-07-29 20:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a36fc34431af

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:21 |
| **Last Seen** | 2026-07-29 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:21:21` | `cowrie.session.connect` |
| `2026-07-29 20:21:21` | `cowrie.client.version` |
| `2026-07-29 20:21:21` | `cowrie.client.kex` |
| `2026-07-29 20:21:21` | `cowrie.login.success` |
| `2026-07-29 20:21:22` | `cowrie.session.params` |
| `2026-07-29 20:21:22` | `cowrie.command.input` |
| `2026-07-29 20:21:22` | `cowrie.log.closed` |
| `2026-07-29 20:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221e9b048fa7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:22 |
| **Last Seen** | 2026-07-29 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:22:57` | `cowrie.session.connect` |
| `2026-07-29 20:22:57` | `cowrie.client.version` |
| `2026-07-29 20:22:57` | `cowrie.client.kex` |
| `2026-07-29 20:22:57` | `cowrie.login.success` |
| `2026-07-29 20:22:58` | `cowrie.session.params` |
| `2026-07-29 20:22:58` | `cowrie.command.input` |
| `2026-07-29 20:22:58` | `cowrie.log.closed` |
| `2026-07-29 20:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f615a1932f

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-07-29 20:24 |
| **Last Seen** | 2026-07-29 20:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:24:17` | `cowrie.session.connect` |
| `2026-07-29 20:24:18` | `cowrie.client.version` |
| `2026-07-29 20:24:18` | `cowrie.client.kex` |
| `2026-07-29 20:24:19` | `cowrie.login.success` |
| `2026-07-29 20:24:20` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7d127ebe7a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:24 |
| **Last Seen** | 2026-07-29 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:24:37` | `cowrie.session.connect` |
| `2026-07-29 20:24:37` | `cowrie.client.version` |
| `2026-07-29 20:24:37` | `cowrie.client.kex` |
| `2026-07-29 20:24:37` | `cowrie.login.success` |
| `2026-07-29 20:24:38` | `cowrie.session.params` |
| `2026-07-29 20:24:38` | `cowrie.command.input` |
| `2026-07-29 20:24:38` | `cowrie.log.closed` |
| `2026-07-29 20:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0046504d843c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:26 |
| **Last Seen** | 2026-07-29 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:26:15` | `cowrie.session.connect` |
| `2026-07-29 20:26:15` | `cowrie.client.version` |
| `2026-07-29 20:26:15` | `cowrie.client.kex` |
| `2026-07-29 20:26:15` | `cowrie.login.success` |
| `2026-07-29 20:26:16` | `cowrie.session.params` |
| `2026-07-29 20:26:16` | `cowrie.command.input` |
| `2026-07-29 20:26:16` | `cowrie.log.closed` |
| `2026-07-29 20:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fdafc190876

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:27 |
| **Last Seen** | 2026-07-29 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:27:50` | `cowrie.session.connect` |
| `2026-07-29 20:27:50` | `cowrie.client.version` |
| `2026-07-29 20:27:50` | `cowrie.client.kex` |
| `2026-07-29 20:27:51` | `cowrie.login.success` |
| `2026-07-29 20:27:52` | `cowrie.session.params` |
| `2026-07-29 20:27:52` | `cowrie.command.input` |
| `2026-07-29 20:27:52` | `cowrie.log.closed` |
| `2026-07-29 20:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90b6c4c242ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:29 |
| **Last Seen** | 2026-07-29 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:29:23` | `cowrie.session.connect` |
| `2026-07-29 20:29:23` | `cowrie.client.version` |
| `2026-07-29 20:29:23` | `cowrie.client.kex` |
| `2026-07-29 20:29:24` | `cowrie.login.success` |
| `2026-07-29 20:29:24` | `cowrie.session.params` |
| `2026-07-29 20:29:24` | `cowrie.command.input` |
| `2026-07-29 20:29:25` | `cowrie.log.closed` |
| `2026-07-29 20:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabd254edecf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:31 |
| **Last Seen** | 2026-07-29 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:31:00` | `cowrie.session.connect` |
| `2026-07-29 20:31:00` | `cowrie.client.version` |
| `2026-07-29 20:31:00` | `cowrie.client.kex` |
| `2026-07-29 20:31:00` | `cowrie.login.success` |
| `2026-07-29 20:31:01` | `cowrie.session.params` |
| `2026-07-29 20:31:01` | `cowrie.command.input` |
| `2026-07-29 20:31:01` | `cowrie.log.closed` |
| `2026-07-29 20:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608a5b4c9ed0

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-29 20:32 |
| **Last Seen** | 2026-07-29 20:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:32:11` | `cowrie.session.connect` |
| `2026-07-29 20:32:11` | `cowrie.client.version` |
| `2026-07-29 20:32:11` | `cowrie.client.kex` |
| `2026-07-29 20:32:13` | `cowrie.login.success` |
| `2026-07-29 20:32:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb59ce3e942f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:32 |
| **Last Seen** | 2026-07-29 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:32:37` | `cowrie.session.connect` |
| `2026-07-29 20:32:37` | `cowrie.client.version` |
| `2026-07-29 20:32:38` | `cowrie.client.kex` |
| `2026-07-29 20:32:38` | `cowrie.login.success` |
| `2026-07-29 20:32:39` | `cowrie.session.params` |
| `2026-07-29 20:32:39` | `cowrie.command.input` |
| `2026-07-29 20:32:39` | `cowrie.log.closed` |
| `2026-07-29 20:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81e0e70fb4d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:34 |
| **Last Seen** | 2026-07-29 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:34:11` | `cowrie.session.connect` |
| `2026-07-29 20:34:11` | `cowrie.client.version` |
| `2026-07-29 20:34:12` | `cowrie.client.kex` |
| `2026-07-29 20:34:12` | `cowrie.login.success` |
| `2026-07-29 20:34:13` | `cowrie.session.params` |
| `2026-07-29 20:34:13` | `cowrie.command.input` |
| `2026-07-29 20:34:13` | `cowrie.log.closed` |
| `2026-07-29 20:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4722cfc4bb0e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-29 20:35 |
| **Last Seen** | 2026-07-29 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:35:47` | `cowrie.session.connect` |
| `2026-07-29 20:35:47` | `cowrie.client.version` |
| `2026-07-29 20:35:47` | `cowrie.client.kex` |
| `2026-07-29 20:35:48` | `cowrie.login.success` |
| `2026-07-29 20:35:49` | `cowrie.session.params` |
| `2026-07-29 20:35:49` | `cowrie.command.input` |
| `2026-07-29 20:35:49` | `cowrie.log.closed` |
| `2026-07-29 20:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c751ba64cac0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 20:40 |
| **Last Seen** | 2026-07-29 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:40:05` | `cowrie.session.connect` |
| `2026-07-29 20:40:05` | `cowrie.client.version` |
| `2026-07-29 20:40:05` | `cowrie.client.kex` |
| `2026-07-29 20:40:06` | `cowrie.login.success` |
| `2026-07-29 20:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036e89f8a42b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-29 20:40 |
| **Last Seen** | 2026-07-29 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:40:06` | `cowrie.session.connect` |
| `2026-07-29 20:40:06` | `cowrie.client.version` |
| `2026-07-29 20:40:06` | `cowrie.client.kex` |
| `2026-07-29 20:40:07` | `cowrie.login.success` |
| `2026-07-29 20:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6bf8e4fc0e1

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-29 20:48 |
| **Last Seen** | 2026-07-29 20:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:48:53` | `cowrie.session.connect` |
| `2026-07-29 20:48:53` | `cowrie.client.version` |
| `2026-07-29 20:48:53` | `cowrie.client.kex` |
| `2026-07-29 20:48:55` | `cowrie.login.success` |
| `2026-07-29 20:48:55` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab27c01abb4

| Field | Detail |
|---|---|
| **Source IP** | `125.25.183[.]157` |
| **First Seen** | 2026-07-29 20:49 |
| **Last Seen** | 2026-07-29 20:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:49:59` | `cowrie.session.connect` |
| `2026-07-29 20:50:00` | `cowrie.client.version` |
| `2026-07-29 20:50:00` | `cowrie.client.kex` |
| `2026-07-29 20:50:02` | `cowrie.login.success` |
| `2026-07-29 20:50:02` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.25.183[.]157` to AbuseIPDB if not already reported
- [ ] Block `125.25.183[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0706a75b4fb6

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-07-29 20:50 |
| **Last Seen** | 2026-07-29 20:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:50:12` | `cowrie.session.connect` |
| `2026-07-29 20:50:12` | `cowrie.client.version` |
| `2026-07-29 20:50:12` | `cowrie.client.kex` |
| `2026-07-29 20:50:14` | `cowrie.login.success` |
| `2026-07-29 20:50:14` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1acffac31c5

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-29 20:50 |
| **Last Seen** | 2026-07-29 20:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:50:35` | `cowrie.session.connect` |
| `2026-07-29 20:50:36` | `cowrie.client.version` |
| `2026-07-29 20:50:36` | `cowrie.client.kex` |
| `2026-07-29 20:50:38` | `cowrie.login.success` |
| `2026-07-29 20:50:38` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25a5d252fec

| Field | Detail |
|---|---|
| **Source IP** | `58.56.128[.]190` |
| **First Seen** | 2026-07-29 20:50 |
| **Last Seen** | 2026-07-29 20:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:50:48` | `cowrie.session.connect` |
| `2026-07-29 20:50:49` | `cowrie.client.version` |
| `2026-07-29 20:50:49` | `cowrie.client.kex` |
| `2026-07-29 20:50:51` | `cowrie.login.success` |
| `2026-07-29 20:50:51` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.128[.]190` to AbuseIPDB if not already reported
- [ ] Block `58.56.128[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a42d7b284ec

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-07-29 20:50 |
| **Last Seen** | 2026-07-29 20:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:50:48` | `cowrie.session.connect` |
| `2026-07-29 20:50:49` | `cowrie.client.version` |
| `2026-07-29 20:50:49` | `cowrie.client.kex` |
| `2026-07-29 20:50:50` | `cowrie.login.success` |
| `2026-07-29 20:50:51` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d300cde049e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-07-29 20:50 |
| **Last Seen** | 2026-07-29 20:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:50:56` | `cowrie.session.connect` |
| `2026-07-29 20:50:57` | `cowrie.client.version` |
| `2026-07-29 20:50:57` | `cowrie.client.kex` |
| `2026-07-29 20:50:58` | `cowrie.login.success` |
| `2026-07-29 20:50:59` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae168a37a1d

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-29 20:52 |
| **Last Seen** | 2026-07-29 20:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:52:24` | `cowrie.session.connect` |
| `2026-07-29 20:52:25` | `cowrie.client.version` |
| `2026-07-29 20:52:25` | `cowrie.client.kex` |
| `2026-07-29 20:52:26` | `cowrie.login.success` |
| `2026-07-29 20:52:27` | `cowrie.direct-tcpip.request` |
| `2026-07-29 20:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0da912ad9654

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-07-29 20:54 |
| **Last Seen** | 2026-07-29 20:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:54:54` | `cowrie.session.connect` |
| `2026-07-29 20:54:54` | `cowrie.client.version` |
| `2026-07-29 20:54:54` | `cowrie.client.kex` |
| `2026-07-29 20:54:54` | `cowrie.login.success` |
| `2026-07-29 20:54:55` | `cowrie.session.params` |
| `2026-07-29 20:54:55` | `cowrie.command.input` |
| `2026-07-29 20:54:55` | `cowrie.command.failed` |
| `2026-07-29 20:54:55` | `cowrie.log.closed` |
| `2026-07-29 20:54:55` | `cowrie.session.params` |
| `2026-07-29 20:54:55` | `cowrie.command.input` |
| `2026-07-29 20:54:56` | `cowrie.session.file_download` |
| `2026-07-29 20:54:56` | `cowrie.log.closed` |
| `2026-07-29 20:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e81e550ba9

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-07-29 20:54 |
| **Last Seen** | 2026-07-29 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:54:56` | `cowrie.session.connect` |
| `2026-07-29 20:54:56` | `cowrie.client.version` |
| `2026-07-29 20:54:56` | `cowrie.client.kex` |
| `2026-07-29 20:54:56` | `cowrie.login.success` |
| `2026-07-29 20:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b194f9a455f0

| Field | Detail |
|---|---|
| **Source IP** | `187.212.37[.]143` |
| **First Seen** | 2026-07-29 20:54 |
| **Last Seen** | 2026-07-29 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-29 20:54:56` | `cowrie.session.connect` |
| `2026-07-29 20:54:56` | `cowrie.client.version` |
| `2026-07-29 20:54:56` | `cowrie.client.kex` |
| `2026-07-29 20:54:57` | `cowrie.login.success` |
| `2026-07-29 20:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.212.37[.]143` to AbuseIPDB if not already reported
- [ ] Block `187.212.37[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **28** | 2026-07-29 19:12 | 2026-07-29 20:54 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-29 19:14 | 2026-07-29 20:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]218` | **3** | 2026-07-29 20:34 | 2026-07-29 20:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-29 20:28 | 2026-07-29 20:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-29 19:05 | 2026-07-29 19:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-29 20:10 | 2026-07-29 20:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-29 19:34 | 2026-07-29 19:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]158` | **2** | 2026-07-29 20:01 | 2026-07-29 20:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | **2** | 2026-07-29 19:42 | 2026-07-29 20:18 | 4m | 0 | `T1592` | 🟢 LOW |
| `112.31.93[.]229` | 1 | 2026-07-29 19:50 | 2026-07-29 19:51 | 39s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-07-29 20:48 | 2026-07-29 20:49 | 42s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]230` | 1 | 2026-07-29 19:23 | 2026-07-29 19:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-29 19:35 | 2026-07-29 19:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.104.97[.]66` | 1 | 2026-07-29 20:16 | 2026-07-29 20:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.178.246[.]43` | 1 | 2026-07-29 20:49 | 2026-07-29 20:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `34.122.244[.]225` | 1 | 2026-07-29 19:23 | 2026-07-29 19:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.105.212[.]205` | 1 | 2026-07-29 18:58 | 2026-07-29 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]27` | 1 | 2026-07-29 20:11 | 2026-07-29 20:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-29 20:00 | 2026-07-29 20:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-29 20:34 | 2026-07-29 20:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]17` | 1 | 2026-07-29 20:22 | 2026-07-29 20:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-29 20:42 | 2026-07-29 20:42 | 43s | 0 | `T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-07-29 20:52 | 2026-07-29 20:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-29 19:48 | 2026-07-29 19:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-29 20:24 | 2026-07-29 20:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-07-29 19:06 | 2026-07-29 19:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.225.108[.]138` | 1 | 2026-07-29 20:17 | 2026-07-29 20:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]18` | 1 | 2026-07-29 19:29 | 2026-07-29 19:29 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `218.149.228[.]135` | KR | Korea Telecom | **100** ⚠️ | 35 |
| `106.13.181[.]87` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.147.248[.]44` | IN | Softcrop It | **100** ⚠️ | 50 |
| `39.164.94[.]190` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `183.167.217[.]86` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `116.228.195[.]251` | CN | Yi Cheng Transport Service Co., Ltd. Shanghai set canning | **100** ⚠️ | 50 |
| `39.105.212[.]205` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `221.8.22[.]14` | CN | China Unicom JILIN province network | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 95 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 81 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 165 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (8.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 56 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 81 priority case(s) shown individually · 28 recon entry/entries in table (9 group(s) consolidating 51 session(s)).

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
_Report time: 2026-07-29T21:01:44Z_

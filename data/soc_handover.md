# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-03 |
| **Generated At** | 2026-08-03T14:48:17Z |
| **Shift Time** | 14:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **130** |
| Confirmed Threats | **112** |
| False Positives Filtered | **18** (13.9%) |
| Unique Attacker IPs | **65** |
| Countries of Origin | **25** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **99** |
| Unique Credential Pairs | **62** |
| Unique Usernames | **21** |
| Unique Passwords | **54** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `admin` | 11 |
| `345gs5662d34` | 7 |
| `support` | 7 |
| `lghkel	` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `root2` | 5 |
| `zpz}ld	` | 5 |
| `ubnt13` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `root2` | 5 |
| `lghkel	` | `zpz}ld	` | 5 |
| `ubnt` | `ubnt13` | 4 |
| `admin` | `121212` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `oracle` | `1q2w3e4r5t` | `112.120.171.95` | 2026-08-03T10:58:55 |
| `345gs5662d34` | `345gs5662d34` | `112.120.171.95` | 2026-08-03T10:58:59 |
| `oracle` | `3245gs5662d34` | `112.120.171.95` | 2026-08-03T10:59:00 |
| `root` | `master123` | `219.128.15.190` | 2026-08-03T11:01:02 |
| `root` | `master123` | `208.69.161.214` | 2026-08-03T11:01:10 |
| `root` | `master123` | `178.178.194.151` | 2026-08-03T11:01:19 |
| `pentaho` | `pentaho1` | `186.209.52.199` | 2026-08-03T11:02:09 |
| `user1` | `test` | `5.175.192.197` | 2026-08-03T11:02:11 |
| `345gs5662d34` | `345gs5662d34` | `186.209.52.199` | 2026-08-03T11:02:13 |
| `345gs5662d34` | `345gs5662d34` | `5.175.192.197` | 2026-08-03T11:02:14 |
| `pentaho` | `3245gs5662d34` | `186.209.52.199` | 2026-08-03T11:02:14 |
| `user1` | `3245gs5662d34` | `5.175.192.197` | 2026-08-03T11:02:14 |
| `workshop` | `workshop` | `101.47.14.46` | 2026-08-03T11:03:29 |
| `345gs5662d34` | `345gs5662d34` | `101.47.14.46` | 2026-08-03T11:03:33 |
| `workshop` | `3245gs5662d34` | `101.47.14.46` | 2026-08-03T11:03:35 |
| `root` | `root2` | `156.238.86.2` | 2026-08-03T11:04:53 |
| `root` | `screencast` | `10.0.0.73` | 2026-08-03T11:08:01 |
| `root` | `screencast` | `178.178.194.151` | 2026-08-03T11:09:45 |
| `user` | `user` | `31.77.227.120` | 2026-08-03T11:14:35 |
| `root` | `root2` | `10.0.0.73` | 2026-08-03T11:16:44 |
| `ubnt` | `ubnt13` | `10.0.0.73` | 2026-08-03T11:16:48 |
| `root` | `admin` | `34.159.18.221` | 2026-08-03T11:16:50 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-03T11:18:09 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-03T11:18:09 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-03T11:18:11 |
| `support` | `support` | `176.53.159.196` | 2026-08-03T11:20:28 |
| `root` | `Admin@123` | `94.237.111.75` | 2026-08-03T11:32:16 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8c\x8e\x8e\x86\x8e\x86\x8c\x88'` | `14.47.200.242` | 2026-08-03T11:32:39 |
| `lghkel	` | `zpz}ld	` | `14.47.200.242` | 2026-08-03T11:32:40 |
| `b'\xcc\xd1\xd1\xca'` | `b'\x8f\x8c\x8d\x8a\x8b\x88'` | `14.47.200.242` | 2026-08-03T11:33:14 |
| `mg3500` | `merlin` | `14.47.200.242` | 2026-08-03T11:33:49 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8f\x8f\x8f'` | `14.47.200.242` | 2026-08-03T11:34:23 |
| `root` | `root2` | `34.146.217.105` | 2026-08-03T11:34:23 |
| `root` | `root2` | `182.75.227.178` | 2026-08-03T11:34:32 |
| `root` | `5up` | `14.47.200.242` | 2026-08-03T11:34:57 |
| `"??$` | `$1` | `14.47.200.242` | 2026-08-03T11:35:30 |
| `ubnt` | `ubnt13` | `114.30.223.119` | 2026-08-03T11:35:53 |
| `ubnt` | `ubnt13` | `122.187.147.13` | 2026-08-03T11:36:03 |
| `b'\xdb\xc4\xda\xc8\xcc'` | `b'\xdb\xc4\xda\xc8\xcc'` | `14.47.200.242` | 2026-08-03T11:36:05 |
| `root` | `klv123` | `14.47.200.242` | 2026-08-03T11:36:39 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xca\xd2\x89\x86\x87'` | `14.47.200.242` | 2026-08-03T11:37:13 |
| `admin` | `ZmqVfoSIP` | `14.47.200.242` | 2026-08-03T11:37:47 |
| `root` | `12345` | `200.199.32.174` | 2026-08-03T11:39:44 |
| `12345` | `12345` | `10.0.0.73` | 2026-08-03T11:43:13 |
| `support` | `support` | `10.0.0.73` | 2026-08-03T11:49:48 |
| `root` | `---fuck_you----` | `180.76.239.185` | 2026-08-03T11:54:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-03T12:04:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-03T12:04:29 |
| `support` | `Password123!` | `191.210.73.33` | 2026-08-03T12:10:42 |
| `support` | `Password123!` | `36.92.35.211` | 2026-08-03T12:10:57 |
| `support` | `Password123!` | `122.170.98.139` | 2026-08-03T12:11:06 |
| `admin` | `121212` | `14.99.61.248` | 2026-08-03T12:14:41 |
| `admin` | `121212` | `61.145.181.7` | 2026-08-03T12:14:50 |
| `root` | `111111` | `80.94.92.55` | 2026-08-03T12:17:15 |
| `root` | `123` | `80.94.92.55` | 2026-08-03T12:19:45 |
| `guest` | `guest9` | `117.2.123.19` | 2026-08-03T12:19:52 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-03T12:22:18 |
| `root` | `123123` | `80.94.92.55` | 2026-08-03T12:22:22 |
| `root` | `123321` | `80.94.92.55` | 2026-08-03T12:25:00 |
| `admin` | `121212` | `10.0.0.73` | 2026-08-03T12:26:35 |
| `root` | `1234` | `80.94.92.55` | 2026-08-03T12:27:48 |
| `root` | `12345` | `80.94.92.55` | 2026-08-03T12:30:31 |
| `root` | `1234567` | `80.94.92.55` | 2026-08-03T12:35:48 |
| `root` | `12345678` | `80.94.92.55` | 2026-08-03T12:38:19 |
| `root` | `123456789` | `80.94.92.55` | 2026-08-03T12:40:54 |
| `root` | `1234abcd` | `80.94.92.55` | 2026-08-03T12:43:28 |
| `story` | `story` | `182.93.7.194` | 2026-08-03T12:43:42 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-08-03T12:43:46 |
| `story` | `3245gs5662d34` | `182.93.7.194` | 2026-08-03T12:43:48 |
| `admin` | `121212` | `222.236.155.146` | 2026-08-03T12:44:16 |
| `supervisor` | `Passw@rd` | `178.178.222.60` | 2026-08-03T12:45:20 |
| `sammy` | `sammysammy` | `182.93.7.194` | 2026-08-03T12:45:21 |
| `sammy` | `3245gs5662d34` | `182.93.7.194` | 2026-08-03T12:45:26 |
| `supervisor` | `Passw@rd` | `202.138.229.190` | 2026-08-03T12:45:31 |
| `root` | `123abc` | `80.94.92.55` | 2026-08-03T12:46:00 |
| `root` | `admin1234.` | `94.182.168.149` | 2026-08-03T12:47:31 |
| `345gs5662d34` | `345gs5662d34` | `94.182.168.149` | 2026-08-03T12:47:34 |
| `root` | `3245gs5662d34` | `94.182.168.149` | 2026-08-03T12:47:36 |
| `root` | `123qwe` | `80.94.92.55` | 2026-08-03T12:48:30 |
| `support` | `1z2x3c4v` | `118.43.236.237` | 2026-08-03T12:49:43 |
| `root` | `1q2w3e` | `80.94.92.55` | 2026-08-03T12:51:02 |
| `admin` | `8888888888` | `10.0.0.73` | 2026-08-03T12:53:05 |
| `root` | `1q2w3e4r` | `80.94.92.55` | 2026-08-03T12:53:30 |
| `admin` | `8888888888` | `188.168.86.6` | 2026-08-03T12:54:41 |
| `admin` | `8888888888` | `121.159.71.249` | 2026-08-03T12:54:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **130** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 23 |
| Go SSH scanner | 23 |
| libssh | 22 |
| Paramiko (Python) | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 23 | 22 |
| `f555226df196...` | Mirai/variant | 15 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `03a80b21afa8...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 23 | 22 | Mirai/variant |
| `f555226df196...` | libssh | 15 | 5 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 14 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.55`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `5.175.192.197`, `112.120.171.95`, `186.209.52.199`, `94.182.168.149`, `182.93.7.194`, `101.47.14.46`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **65** |
| Unique ASNs | **46** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (80)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-616d7c4ac058

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-03 10:58 |
| **Last Seen** | 2026-08-03 10:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:58:54` | `cowrie.session.connect` |
| `2026-08-03 10:58:54` | `cowrie.client.version` |
| `2026-08-03 10:58:54` | `cowrie.client.kex` |
| `2026-08-03 10:58:55` | `cowrie.login.success` |
| `2026-08-03 10:58:56` | `cowrie.session.params` |
| `2026-08-03 10:58:56` | `cowrie.command.input` |
| `2026-08-03 10:58:56` | `cowrie.command.failed` |
| `2026-08-03 10:58:56` | `cowrie.log.closed` |
| `2026-08-03 10:58:57` | `cowrie.session.params` |
| `2026-08-03 10:58:57` | `cowrie.command.input` |
| `2026-08-03 10:58:57` | `cowrie.session.file_download` |
| `2026-08-03 10:58:57` | `cowrie.log.closed` |
| `2026-08-03 10:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23809d6a00ba

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-03 10:58 |
| **Last Seen** | 2026-08-03 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:58:58` | `cowrie.session.connect` |
| `2026-08-03 10:58:58` | `cowrie.client.version` |
| `2026-08-03 10:58:58` | `cowrie.client.kex` |
| `2026-08-03 10:58:59` | `cowrie.login.success` |
| `2026-08-03 10:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9059f5007c

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-03 10:58 |
| **Last Seen** | 2026-08-03 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 10:58:59` | `cowrie.session.connect` |
| `2026-08-03 10:58:59` | `cowrie.client.version` |
| `2026-08-03 10:58:59` | `cowrie.client.kex` |
| `2026-08-03 10:59:00` | `cowrie.login.success` |
| `2026-08-03 10:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ceb4c0a0b1

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-08-03 11:00 |
| **Last Seen** | 2026-08-03 11:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:00:59` | `cowrie.session.connect` |
| `2026-08-03 11:01:00` | `cowrie.client.version` |
| `2026-08-03 11:01:00` | `cowrie.client.kex` |
| `2026-08-03 11:01:02` | `cowrie.login.success` |
| `2026-08-03 11:01:03` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b72b28d130

| Field | Detail |
|---|---|
| **Source IP** | `208.69.161[.]214` |
| **First Seen** | 2026-08-03 11:01 |
| **Last Seen** | 2026-08-03 11:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:01:08` | `cowrie.session.connect` |
| `2026-08-03 11:01:09` | `cowrie.client.version` |
| `2026-08-03 11:01:09` | `cowrie.client.kex` |
| `2026-08-03 11:01:10` | `cowrie.login.success` |
| `2026-08-03 11:01:10` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.69.161[.]214` to AbuseIPDB if not already reported
- [ ] Block `208.69.161[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0256d1042bf

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-03 11:01 |
| **Last Seen** | 2026-08-03 11:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:01:13` | `cowrie.session.connect` |
| `2026-08-03 11:01:16` | `cowrie.client.version` |
| `2026-08-03 11:01:16` | `cowrie.client.kex` |
| `2026-08-03 11:01:19` | `cowrie.login.success` |
| `2026-08-03 11:01:20` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6883b1d449

| Field | Detail |
|---|---|
| **Source IP** | `186.209.52[.]199` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:08` | `cowrie.session.connect` |
| `2026-08-03 11:02:08` | `cowrie.client.version` |
| `2026-08-03 11:02:09` | `cowrie.client.kex` |
| `2026-08-03 11:02:09` | `cowrie.login.success` |
| `2026-08-03 11:02:10` | `cowrie.session.params` |
| `2026-08-03 11:02:10` | `cowrie.command.input` |
| `2026-08-03 11:02:10` | `cowrie.command.failed` |
| `2026-08-03 11:02:10` | `cowrie.log.closed` |
| `2026-08-03 11:02:11` | `cowrie.session.params` |
| `2026-08-03 11:02:11` | `cowrie.command.input` |
| `2026-08-03 11:02:11` | `cowrie.session.file_download` |
| `2026-08-03 11:02:11` | `cowrie.log.closed` |
| `2026-08-03 11:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.209.52[.]199` to AbuseIPDB if not already reported
- [ ] Block `186.209.52[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b0aead7efd

| Field | Detail |
|---|---|
| **Source IP** | `5.175.192[.]197` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:10` | `cowrie.session.connect` |
| `2026-08-03 11:02:10` | `cowrie.client.version` |
| `2026-08-03 11:02:10` | `cowrie.client.kex` |
| `2026-08-03 11:02:11` | `cowrie.login.success` |
| `2026-08-03 11:02:12` | `cowrie.session.params` |
| `2026-08-03 11:02:12` | `cowrie.command.input` |
| `2026-08-03 11:02:12` | `cowrie.command.failed` |
| `2026-08-03 11:02:12` | `cowrie.log.closed` |
| `2026-08-03 11:02:13` | `cowrie.session.params` |
| `2026-08-03 11:02:13` | `cowrie.command.input` |
| `2026-08-03 11:02:13` | `cowrie.session.file_download` |
| `2026-08-03 11:02:13` | `cowrie.log.closed` |
| `2026-08-03 11:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.192[.]197` to AbuseIPDB if not already reported
- [ ] Block `5.175.192[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8caf7e294ea3

| Field | Detail |
|---|---|
| **Source IP** | `186.209.52[.]199` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:12` | `cowrie.session.connect` |
| `2026-08-03 11:02:12` | `cowrie.client.version` |
| `2026-08-03 11:02:12` | `cowrie.client.kex` |
| `2026-08-03 11:02:13` | `cowrie.login.success` |
| `2026-08-03 11:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.209.52[.]199` to AbuseIPDB if not already reported
- [ ] Block `186.209.52[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30e98a1c0dff

| Field | Detail |
|---|---|
| **Source IP** | `5.175.192[.]197` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:13` | `cowrie.session.connect` |
| `2026-08-03 11:02:13` | `cowrie.client.version` |
| `2026-08-03 11:02:13` | `cowrie.client.kex` |
| `2026-08-03 11:02:14` | `cowrie.login.success` |
| `2026-08-03 11:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.192[.]197` to AbuseIPDB if not already reported
- [ ] Block `5.175.192[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d1763b7485

| Field | Detail |
|---|---|
| **Source IP** | `186.209.52[.]199` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:13` | `cowrie.session.connect` |
| `2026-08-03 11:02:13` | `cowrie.client.version` |
| `2026-08-03 11:02:13` | `cowrie.client.kex` |
| `2026-08-03 11:02:14` | `cowrie.login.success` |
| `2026-08-03 11:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.209.52[.]199` to AbuseIPDB if not already reported
- [ ] Block `186.209.52[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390400125198

| Field | Detail |
|---|---|
| **Source IP** | `5.175.192[.]197` |
| **First Seen** | 2026-08-03 11:02 |
| **Last Seen** | 2026-08-03 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:02:14` | `cowrie.session.connect` |
| `2026-08-03 11:02:14` | `cowrie.client.version` |
| `2026-08-03 11:02:14` | `cowrie.client.kex` |
| `2026-08-03 11:02:14` | `cowrie.login.success` |
| `2026-08-03 11:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.192[.]197` to AbuseIPDB if not already reported
- [ ] Block `5.175.192[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0157928b65f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-03 11:03 |
| **Last Seen** | 2026-08-03 11:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:03:28` | `cowrie.session.connect` |
| `2026-08-03 11:03:28` | `cowrie.client.version` |
| `2026-08-03 11:03:28` | `cowrie.client.kex` |
| `2026-08-03 11:03:29` | `cowrie.login.success` |
| `2026-08-03 11:03:30` | `cowrie.session.params` |
| `2026-08-03 11:03:30` | `cowrie.command.input` |
| `2026-08-03 11:03:30` | `cowrie.command.failed` |
| `2026-08-03 11:03:31` | `cowrie.log.closed` |
| `2026-08-03 11:03:32` | `cowrie.session.params` |
| `2026-08-03 11:03:32` | `cowrie.command.input` |
| `2026-08-03 11:03:32` | `cowrie.session.file_download` |
| `2026-08-03 11:03:32` | `cowrie.log.closed` |
| `2026-08-03 11:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c172cd3ded40

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-03 11:03 |
| **Last Seen** | 2026-08-03 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:03:32` | `cowrie.session.connect` |
| `2026-08-03 11:03:32` | `cowrie.client.version` |
| `2026-08-03 11:03:32` | `cowrie.client.kex` |
| `2026-08-03 11:03:33` | `cowrie.login.success` |
| `2026-08-03 11:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e5d6363db3

| Field | Detail |
|---|---|
| **Source IP** | `101.47.14[.]46` |
| **First Seen** | 2026-08-03 11:03 |
| **Last Seen** | 2026-08-03 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:03:34` | `cowrie.session.connect` |
| `2026-08-03 11:03:34` | `cowrie.client.version` |
| `2026-08-03 11:03:34` | `cowrie.client.kex` |
| `2026-08-03 11:03:35` | `cowrie.login.success` |
| `2026-08-03 11:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.14[.]46` to AbuseIPDB if not already reported
- [ ] Block `101.47.14[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4702067882f0

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-08-03 11:04 |
| **Last Seen** | 2026-08-03 11:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:04:50` | `cowrie.session.connect` |
| `2026-08-03 11:04:51` | `cowrie.client.version` |
| `2026-08-03 11:04:51` | `cowrie.client.kex` |
| `2026-08-03 11:04:53` | `cowrie.login.success` |
| `2026-08-03 11:04:54` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591c70c0cef7

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-03 11:09 |
| **Last Seen** | 2026-08-03 11:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:09:43` | `cowrie.session.connect` |
| `2026-08-03 11:09:43` | `cowrie.client.version` |
| `2026-08-03 11:09:43` | `cowrie.client.kex` |
| `2026-08-03 11:09:45` | `cowrie.login.success` |
| `2026-08-03 11:09:45` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b52346e3eec

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-03 11:14 |
| **Last Seen** | 2026-08-03 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:14:34` | `cowrie.session.connect` |
| `2026-08-03 11:14:34` | `cowrie.client.version` |
| `2026-08-03 11:14:34` | `cowrie.client.kex` |
| `2026-08-03 11:14:35` | `cowrie.login.success` |
| `2026-08-03 11:14:35` | `cowrie.session.params` |
| `2026-08-03 11:14:35` | `cowrie.command.input` |
| `2026-08-03 11:14:35` | `cowrie.log.closed` |
| `2026-08-03 11:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bcc31f71156

| Field | Detail |
|---|---|
| **Source IP** | `34.159.18[.]221` |
| **First Seen** | 2026-08-03 11:16 |
| **Last Seen** | 2026-08-03 11:17 |
| **Session Duration** | 30s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:16:47` | `cowrie.session.connect` |
| `2026-08-03 11:16:48` | `cowrie.client.version` |
| `2026-08-03 11:16:48` | `cowrie.client.kex` |
| `2026-08-03 11:16:49` | `cowrie.login.failed` |
| `2026-08-03 11:16:50` | `cowrie.login.success` |
| `2026-08-03 11:16:51` | `cowrie.session.params` |
| `2026-08-03 11:16:51` | `cowrie.command.input` |
| `2026-08-03 11:16:51` | `cowrie.command.failed` |
| `2026-08-03 11:16:51` | `cowrie.log.closed` |
| `2026-08-03 11:16:52` | `cowrie.session.params` |
| `2026-08-03 11:16:52` | `cowrie.command.input` |
| `2026-08-03 11:16:53` | `cowrie.log.closed` |
| `2026-08-03 11:16:53` | `cowrie.session.params` |
| `2026-08-03 11:16:53` | `cowrie.command.input` |
| `2026-08-03 11:16:54` | `cowrie.log.closed` |
| `2026-08-03 11:16:54` | `cowrie.session.params` |
| `2026-08-03 11:16:54` | `cowrie.command.input` |
| `2026-08-03 11:16:55` | `cowrie.log.closed` |
| `2026-08-03 11:16:55` | `cowrie.session.params` |
| `2026-08-03 11:16:55` | `cowrie.command.input` |
| `2026-08-03 11:16:56` | `cowrie.log.closed` |
| `2026-08-03 11:16:56` | `cowrie.session.params` |
| `2026-08-03 11:16:56` | `cowrie.command.input` |
| `2026-08-03 11:16:56` | `cowrie.log.closed` |
| `2026-08-03 11:16:57` | `cowrie.session.params` |
| `2026-08-03 11:16:57` | `cowrie.command.input` |
| `2026-08-03 11:16:58` | `cowrie.log.closed` |
| `2026-08-03 11:16:58` | `cowrie.session.params` |
| `2026-08-03 11:16:58` | `cowrie.command.input` |
| `2026-08-03 11:16:59` | `cowrie.log.closed` |
| `2026-08-03 11:16:59` | `cowrie.session.params` |
| `2026-08-03 11:16:59` | `cowrie.command.input` |
| `2026-08-03 11:17:00` | `cowrie.log.closed` |
| `2026-08-03 11:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.159.18[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.159.18[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94e7fa6ac86

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 11:18 |
| **Last Seen** | 2026-08-03 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:18:08` | `cowrie.session.connect` |
| `2026-08-03 11:18:08` | `cowrie.client.version` |
| `2026-08-03 11:18:08` | `cowrie.client.kex` |
| `2026-08-03 11:18:09` | `cowrie.login.success` |
| `2026-08-03 11:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e0f1cd18fe

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 11:18 |
| **Last Seen** | 2026-08-03 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:18:08` | `cowrie.session.connect` |
| `2026-08-03 11:18:08` | `cowrie.client.version` |
| `2026-08-03 11:18:08` | `cowrie.client.kex` |
| `2026-08-03 11:18:09` | `cowrie.login.success` |
| `2026-08-03 11:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6df87d71ea

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 11:18 |
| **Last Seen** | 2026-08-03 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:18:11` | `cowrie.session.connect` |
| `2026-08-03 11:18:11` | `cowrie.client.version` |
| `2026-08-03 11:18:11` | `cowrie.client.kex` |
| `2026-08-03 11:18:11` | `cowrie.login.success` |
| `2026-08-03 11:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e08000cba2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-03 11:18 |
| **Last Seen** | 2026-08-03 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:18:11` | `cowrie.session.connect` |
| `2026-08-03 11:18:11` | `cowrie.client.version` |
| `2026-08-03 11:18:12` | `cowrie.client.kex` |
| `2026-08-03 11:18:12` | `cowrie.login.success` |
| `2026-08-03 11:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d14eaec10fc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 11:20 |
| **Last Seen** | 2026-08-03 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:20:27` | `cowrie.session.connect` |
| `2026-08-03 11:20:27` | `cowrie.client.version` |
| `2026-08-03 11:20:28` | `cowrie.client.kex` |
| `2026-08-03 11:20:28` | `cowrie.login.success` |
| `2026-08-03 11:20:28` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:20:28` | `cowrie.direct-tcpip.data` |
| `2026-08-03 11:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c70cdb27c75

| Field | Detail |
|---|---|
| **Source IP** | `94.237.111[.]75` |
| **First Seen** | 2026-08-03 11:32 |
| **Last Seen** | 2026-08-03 11:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:32:15` | `cowrie.session.connect` |
| `2026-08-03 11:32:15` | `cowrie.client.version` |
| `2026-08-03 11:32:15` | `cowrie.client.kex` |
| `2026-08-03 11:32:16` | `cowrie.login.success` |
| `2026-08-03 11:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.237.111[.]75` to AbuseIPDB if not already reported
- [ ] Block `94.237.111[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000f1fb0ce90

| Field | Detail |
|---|---|
| **Source IP** | `94.237.111[.]75` |
| **First Seen** | 2026-08-03 11:32 |
| **Last Seen** | 2026-08-03 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:32:16` | `cowrie.session.connect` |
| `2026-08-03 11:32:16` | `cowrie.client.version` |
| `2026-08-03 11:32:16` | `cowrie.client.kex` |
| `2026-08-03 11:32:16` | `cowrie.login.success` |
| `2026-08-03 11:32:17` | `cowrie.session.params` |
| `2026-08-03 11:32:17` | `cowrie.command.input` |
| `2026-08-03 11:32:17` | `cowrie.log.closed` |
| `2026-08-03 11:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.237.111[.]75` to AbuseIPDB if not already reported
- [ ] Block `94.237.111[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd80ade0d90e

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:32 |
| **Last Seen** | 2026-08-03 11:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:32:38` | `cowrie.session.connect` |
| `2026-08-03 11:32:39` | `cowrie.login.success` |
| `2026-08-03 11:32:40` | `cowrie.login.success` |
| `2026-08-03 11:32:41` | `cowrie.session.params` |
| `2026-08-03 11:32:41` | `cowrie.command.input` |
| `2026-08-03 11:32:41` | `cowrie.command.failed` |
| `2026-08-03 11:32:41` | `cowrie.command.input` |
| `2026-08-03 11:32:41` | `cowrie.command.failed` |
| `2026-08-03 11:32:42` | `cowrie.command.input` |
| `2026-08-03 11:32:42` | `cowrie.command.input` |
| `2026-08-03 11:32:42` | `cowrie.command.failed` |
| `2026-08-03 11:32:42` | `cowrie.command.failed` |
| `2026-08-03 11:33:13` | `cowrie.log.closed` |
| `2026-08-03 11:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f3079d0fce

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:33 |
| **Last Seen** | 2026-08-03 11:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:33:13` | `cowrie.session.connect` |
| `2026-08-03 11:33:14` | `cowrie.login.success` |
| `2026-08-03 11:33:14` | `cowrie.login.success` |
| `2026-08-03 11:33:15` | `cowrie.session.params` |
| `2026-08-03 11:33:15` | `cowrie.command.input` |
| `2026-08-03 11:33:15` | `cowrie.command.failed` |
| `2026-08-03 11:33:16` | `cowrie.command.input` |
| `2026-08-03 11:33:16` | `cowrie.command.failed` |
| `2026-08-03 11:33:16` | `cowrie.command.input` |
| `2026-08-03 11:33:16` | `cowrie.command.input` |
| `2026-08-03 11:33:16` | `cowrie.command.failed` |
| `2026-08-03 11:33:16` | `cowrie.command.failed` |
| `2026-08-03 11:33:48` | `cowrie.log.closed` |
| `2026-08-03 11:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1a9f922375

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:33 |
| **Last Seen** | 2026-08-03 11:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:33:48` | `cowrie.session.connect` |
| `2026-08-03 11:33:49` | `cowrie.login.success` |
| `2026-08-03 11:33:49` | `cowrie.session.params` |
| `2026-08-03 11:33:50` | `cowrie.command.input` |
| `2026-08-03 11:33:50` | `cowrie.command.failed` |
| `2026-08-03 11:33:50` | `cowrie.command.input` |
| `2026-08-03 11:33:50` | `cowrie.command.failed` |
| `2026-08-03 11:33:50` | `cowrie.command.input` |
| `2026-08-03 11:33:50` | `cowrie.command.failed` |
| `2026-08-03 11:33:51` | `cowrie.command.input` |
| `2026-08-03 11:33:51` | `cowrie.command.failed` |
| `2026-08-03 11:33:51` | `cowrie.command.input` |
| `2026-08-03 11:33:51` | `cowrie.command.input` |
| `2026-08-03 11:33:51` | `cowrie.command.failed` |
| `2026-08-03 11:33:51` | `cowrie.command.failed` |
| `2026-08-03 11:34:22` | `cowrie.log.closed` |
| `2026-08-03 11:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02408e9570b

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-08-03 11:34 |
| **Last Seen** | 2026-08-03 11:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:34:21` | `cowrie.session.connect` |
| `2026-08-03 11:34:21` | `cowrie.client.version` |
| `2026-08-03 11:34:21` | `cowrie.client.kex` |
| `2026-08-03 11:34:23` | `cowrie.login.success` |
| `2026-08-03 11:34:24` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82cca9086f94

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:34 |
| **Last Seen** | 2026-08-03 11:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:34:22` | `cowrie.session.connect` |
| `2026-08-03 11:34:23` | `cowrie.login.success` |
| `2026-08-03 11:34:23` | `cowrie.login.success` |
| `2026-08-03 11:34:24` | `cowrie.session.params` |
| `2026-08-03 11:34:24` | `cowrie.command.input` |
| `2026-08-03 11:34:24` | `cowrie.command.failed` |
| `2026-08-03 11:34:25` | `cowrie.command.input` |
| `2026-08-03 11:34:25` | `cowrie.command.failed` |
| `2026-08-03 11:34:25` | `cowrie.command.input` |
| `2026-08-03 11:34:25` | `cowrie.command.input` |
| `2026-08-03 11:34:25` | `cowrie.command.failed` |
| `2026-08-03 11:34:25` | `cowrie.command.failed` |
| `2026-08-03 11:34:56` | `cowrie.log.closed` |
| `2026-08-03 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faeff1444f5b

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-08-03 11:34 |
| **Last Seen** | 2026-08-03 11:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:34:29` | `cowrie.session.connect` |
| `2026-08-03 11:34:30` | `cowrie.client.version` |
| `2026-08-03 11:34:30` | `cowrie.client.kex` |
| `2026-08-03 11:34:32` | `cowrie.login.success` |
| `2026-08-03 11:34:33` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451790de6409

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:34 |
| **Last Seen** | 2026-08-03 11:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:34:56` | `cowrie.session.connect` |
| `2026-08-03 11:34:57` | `cowrie.login.success` |
| `2026-08-03 11:34:57` | `cowrie.session.params` |
| `2026-08-03 11:34:57` | `cowrie.command.input` |
| `2026-08-03 11:34:57` | `cowrie.command.failed` |
| `2026-08-03 11:34:58` | `cowrie.command.input` |
| `2026-08-03 11:34:58` | `cowrie.command.failed` |
| `2026-08-03 11:34:58` | `cowrie.command.input` |
| `2026-08-03 11:34:58` | `cowrie.command.failed` |
| `2026-08-03 11:34:59` | `cowrie.command.input` |
| `2026-08-03 11:34:59` | `cowrie.command.failed` |
| `2026-08-03 11:34:59` | `cowrie.command.input` |
| `2026-08-03 11:34:59` | `cowrie.command.input` |
| `2026-08-03 11:34:59` | `cowrie.command.failed` |
| `2026-08-03 11:34:59` | `cowrie.command.failed` |
| `2026-08-03 11:35:30` | `cowrie.log.closed` |
| `2026-08-03 11:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbff9e440702

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:35 |
| **Last Seen** | 2026-08-03 11:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:35:30` | `cowrie.session.connect` |
| `2026-08-03 11:35:30` | `cowrie.login.success` |
| `2026-08-03 11:35:31` | `cowrie.session.params` |
| `2026-08-03 11:35:31` | `cowrie.command.input` |
| `2026-08-03 11:35:31` | `cowrie.command.input` |
| `2026-08-03 11:35:31` | `cowrie.command.failed` |
| `2026-08-03 11:35:31` | `cowrie.command.input` |
| `2026-08-03 11:35:31` | `cowrie.command.failed` |
| `2026-08-03 11:35:32` | `cowrie.command.input` |
| `2026-08-03 11:35:32` | `cowrie.command.failed` |
| `2026-08-03 11:35:32` | `cowrie.command.input` |
| `2026-08-03 11:35:32` | `cowrie.command.failed` |
| `2026-08-03 11:35:33` | `cowrie.command.input` |
| `2026-08-03 11:35:33` | `cowrie.command.input` |
| `2026-08-03 11:35:33` | `cowrie.command.failed` |
| `2026-08-03 11:35:33` | `cowrie.command.failed` |
| `2026-08-03 11:36:04` | `cowrie.log.closed` |
| `2026-08-03 11:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250b0adacb38

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-03 11:35 |
| **Last Seen** | 2026-08-03 11:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:35:51` | `cowrie.session.connect` |
| `2026-08-03 11:35:51` | `cowrie.client.version` |
| `2026-08-03 11:35:51` | `cowrie.client.kex` |
| `2026-08-03 11:35:53` | `cowrie.login.success` |
| `2026-08-03 11:35:54` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a97c60bfde

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-03 11:36 |
| **Last Seen** | 2026-08-03 11:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:36:00` | `cowrie.session.connect` |
| `2026-08-03 11:36:00` | `cowrie.client.version` |
| `2026-08-03 11:36:00` | `cowrie.client.kex` |
| `2026-08-03 11:36:03` | `cowrie.login.success` |
| `2026-08-03 11:36:04` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659f13d8e30c

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:36 |
| **Last Seen** | 2026-08-03 11:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:36:04` | `cowrie.session.connect` |
| `2026-08-03 11:36:05` | `cowrie.login.success` |
| `2026-08-03 11:36:05` | `cowrie.login.success` |
| `2026-08-03 11:36:06` | `cowrie.session.params` |
| `2026-08-03 11:36:06` | `cowrie.command.input` |
| `2026-08-03 11:36:06` | `cowrie.command.failed` |
| `2026-08-03 11:36:07` | `cowrie.command.input` |
| `2026-08-03 11:36:07` | `cowrie.command.failed` |
| `2026-08-03 11:36:07` | `cowrie.command.input` |
| `2026-08-03 11:36:07` | `cowrie.command.input` |
| `2026-08-03 11:36:07` | `cowrie.command.failed` |
| `2026-08-03 11:36:07` | `cowrie.command.failed` |
| `2026-08-03 11:36:38` | `cowrie.log.closed` |
| `2026-08-03 11:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdfe1f9488e

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:36 |
| **Last Seen** | 2026-08-03 11:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:36:38` | `cowrie.session.connect` |
| `2026-08-03 11:36:39` | `cowrie.login.success` |
| `2026-08-03 11:36:39` | `cowrie.session.params` |
| `2026-08-03 11:36:40` | `cowrie.command.input` |
| `2026-08-03 11:36:40` | `cowrie.command.failed` |
| `2026-08-03 11:36:40` | `cowrie.command.input` |
| `2026-08-03 11:36:40` | `cowrie.command.failed` |
| `2026-08-03 11:36:40` | `cowrie.command.input` |
| `2026-08-03 11:36:40` | `cowrie.command.failed` |
| `2026-08-03 11:36:41` | `cowrie.command.input` |
| `2026-08-03 11:36:41` | `cowrie.command.failed` |
| `2026-08-03 11:36:41` | `cowrie.command.input` |
| `2026-08-03 11:36:41` | `cowrie.command.input` |
| `2026-08-03 11:36:41` | `cowrie.command.failed` |
| `2026-08-03 11:36:41` | `cowrie.command.failed` |
| `2026-08-03 11:37:12` | `cowrie.log.closed` |
| `2026-08-03 11:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2666da736a

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:37 |
| **Last Seen** | 2026-08-03 11:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:37:12` | `cowrie.session.connect` |
| `2026-08-03 11:37:13` | `cowrie.login.success` |
| `2026-08-03 11:37:13` | `cowrie.login.success` |
| `2026-08-03 11:37:14` | `cowrie.session.params` |
| `2026-08-03 11:37:14` | `cowrie.command.input` |
| `2026-08-03 11:37:14` | `cowrie.command.failed` |
| `2026-08-03 11:37:15` | `cowrie.command.input` |
| `2026-08-03 11:37:15` | `cowrie.command.failed` |
| `2026-08-03 11:37:15` | `cowrie.command.input` |
| `2026-08-03 11:37:15` | `cowrie.command.input` |
| `2026-08-03 11:37:15` | `cowrie.command.failed` |
| `2026-08-03 11:37:15` | `cowrie.command.failed` |
| `2026-08-03 11:37:46` | `cowrie.log.closed` |
| `2026-08-03 11:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3e09b4eb42

| Field | Detail |
|---|---|
| **Source IP** | `14.47.200[.]242` |
| **First Seen** | 2026-08-03 11:37 |
| **Last Seen** | 2026-08-03 11:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:37:46` | `cowrie.session.connect` |
| `2026-08-03 11:37:47` | `cowrie.login.success` |
| `2026-08-03 11:37:47` | `cowrie.session.params` |
| `2026-08-03 11:37:47` | `cowrie.command.input` |
| `2026-08-03 11:37:47` | `cowrie.command.failed` |
| `2026-08-03 11:37:48` | `cowrie.command.input` |
| `2026-08-03 11:37:48` | `cowrie.command.failed` |
| `2026-08-03 11:37:48` | `cowrie.command.input` |
| `2026-08-03 11:37:48` | `cowrie.command.failed` |
| `2026-08-03 11:37:49` | `cowrie.command.input` |
| `2026-08-03 11:37:49` | `cowrie.command.failed` |
| `2026-08-03 11:37:49` | `cowrie.command.input` |
| `2026-08-03 11:37:49` | `cowrie.command.input` |
| `2026-08-03 11:37:49` | `cowrie.command.failed` |
| `2026-08-03 11:37:49` | `cowrie.command.failed` |
| `2026-08-03 11:38:20` | `cowrie.log.closed` |
| `2026-08-03 11:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.47.200[.]242` to AbuseIPDB if not already reported
- [ ] Block `14.47.200[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b7da3340f0

| Field | Detail |
|---|---|
| **Source IP** | `200.199.32[.]174` |
| **First Seen** | 2026-08-03 11:39 |
| **Last Seen** | 2026-08-03 11:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:39:42` | `cowrie.session.connect` |
| `2026-08-03 11:39:43` | `cowrie.client.version` |
| `2026-08-03 11:39:43` | `cowrie.client.kex` |
| `2026-08-03 11:39:44` | `cowrie.login.success` |
| `2026-08-03 11:39:45` | `cowrie.direct-tcpip.request` |
| `2026-08-03 11:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.199.32[.]174` to AbuseIPDB if not already reported
- [ ] Block `200.199.32[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c263a77d60c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.239[.]185` |
| **First Seen** | 2026-08-03 11:53 |
| **Last Seen** | 2026-08-03 11:54 |
| **Session Duration** | 109s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 11:53:05` | `cowrie.session.connect` |
| `2026-08-03 11:53:05` | `cowrie.client.version` |
| `2026-08-03 11:54:32` | `cowrie.client.kex` |
| `2026-08-03 11:54:53` | `cowrie.login.success` |
| `2026-08-03 11:54:54` | `cowrie.session.params` |
| `2026-08-03 11:54:54` | `cowrie.command.input` |
| `2026-08-03 11:54:54` | `cowrie.log.closed` |
| `2026-08-03 11:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.239[.]185` to AbuseIPDB if not already reported
- [ ] Block `180.76.239[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71acf46a00a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 12:04 |
| **Last Seen** | 2026-08-03 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:04:28` | `cowrie.session.connect` |
| `2026-08-03 12:04:28` | `cowrie.client.version` |
| `2026-08-03 12:04:28` | `cowrie.client.kex` |
| `2026-08-03 12:04:29` | `cowrie.login.success` |
| `2026-08-03 12:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1522de398af2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-03 12:04 |
| **Last Seen** | 2026-08-03 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:04:28` | `cowrie.session.connect` |
| `2026-08-03 12:04:28` | `cowrie.client.version` |
| `2026-08-03 12:04:28` | `cowrie.client.kex` |
| `2026-08-03 12:04:29` | `cowrie.login.success` |
| `2026-08-03 12:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfda19903697

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-03 12:10 |
| **Last Seen** | 2026-08-03 12:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:10:39` | `cowrie.session.connect` |
| `2026-08-03 12:10:40` | `cowrie.client.version` |
| `2026-08-03 12:10:40` | `cowrie.client.kex` |
| `2026-08-03 12:10:42` | `cowrie.login.success` |
| `2026-08-03 12:10:42` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e6be7f419c

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-08-03 12:10 |
| **Last Seen** | 2026-08-03 12:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:10:54` | `cowrie.session.connect` |
| `2026-08-03 12:10:54` | `cowrie.client.version` |
| `2026-08-03 12:10:54` | `cowrie.client.kex` |
| `2026-08-03 12:10:57` | `cowrie.login.success` |
| `2026-08-03 12:10:59` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f2f4236bc39

| Field | Detail |
|---|---|
| **Source IP** | `122.170.98[.]139` |
| **First Seen** | 2026-08-03 12:11 |
| **Last Seen** | 2026-08-03 12:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:11:04` | `cowrie.session.connect` |
| `2026-08-03 12:11:04` | `cowrie.client.version` |
| `2026-08-03 12:11:04` | `cowrie.client.kex` |
| `2026-08-03 12:11:06` | `cowrie.login.success` |
| `2026-08-03 12:11:07` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.98[.]139` to AbuseIPDB if not already reported
- [ ] Block `122.170.98[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ced49bf5366

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-03 12:14 |
| **Last Seen** | 2026-08-03 12:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:14:39` | `cowrie.session.connect` |
| `2026-08-03 12:14:39` | `cowrie.client.version` |
| `2026-08-03 12:14:39` | `cowrie.client.kex` |
| `2026-08-03 12:14:41` | `cowrie.login.success` |
| `2026-08-03 12:14:42` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d6a173aceb

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-08-03 12:14 |
| **Last Seen** | 2026-08-03 12:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:14:47` | `cowrie.session.connect` |
| `2026-08-03 12:14:48` | `cowrie.client.version` |
| `2026-08-03 12:14:48` | `cowrie.client.kex` |
| `2026-08-03 12:14:50` | `cowrie.login.success` |
| `2026-08-03 12:14:50` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181480b179f6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:17 |
| **Last Seen** | 2026-08-03 12:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:17:11` | `cowrie.session.connect` |
| `2026-08-03 12:17:12` | `cowrie.client.version` |
| `2026-08-03 12:17:12` | `cowrie.client.kex` |
| `2026-08-03 12:17:15` | `cowrie.login.success` |
| `2026-08-03 12:17:17` | `cowrie.session.params` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.success` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:17` | `cowrie.command.input` |
| `2026-08-03 12:17:18` | `cowrie.log.closed` |
| `2026-08-03 12:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d825993256

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:19 |
| **Last Seen** | 2026-08-03 12:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:19:42` | `cowrie.session.connect` |
| `2026-08-03 12:19:43` | `cowrie.client.version` |
| `2026-08-03 12:19:43` | `cowrie.client.kex` |
| `2026-08-03 12:19:45` | `cowrie.login.success` |
| `2026-08-03 12:19:47` | `cowrie.session.params` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.success` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:47` | `cowrie.command.input` |
| `2026-08-03 12:19:48` | `cowrie.log.closed` |
| `2026-08-03 12:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186877356835

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-08-03 12:19 |
| **Last Seen** | 2026-08-03 12:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:19:48` | `cowrie.session.connect` |
| `2026-08-03 12:19:49` | `cowrie.client.version` |
| `2026-08-03 12:19:49` | `cowrie.client.kex` |
| `2026-08-03 12:19:52` | `cowrie.login.success` |
| `2026-08-03 12:19:52` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c27a4c57bb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:22 |
| **Last Seen** | 2026-08-03 12:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:22:21` | `cowrie.session.connect` |
| `2026-08-03 12:22:21` | `cowrie.client.version` |
| `2026-08-03 12:22:22` | `cowrie.client.kex` |
| `2026-08-03 12:22:22` | `cowrie.login.success` |
| `2026-08-03 12:22:24` | `cowrie.session.params` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.success` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:24` | `cowrie.command.input` |
| `2026-08-03 12:22:26` | `cowrie.log.closed` |
| `2026-08-03 12:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562ad757df43

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:24 |
| **Last Seen** | 2026-08-03 12:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:24:59` | `cowrie.session.connect` |
| `2026-08-03 12:24:59` | `cowrie.client.version` |
| `2026-08-03 12:24:59` | `cowrie.client.kex` |
| `2026-08-03 12:25:00` | `cowrie.login.success` |
| `2026-08-03 12:25:02` | `cowrie.session.params` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.success` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.command.input` |
| `2026-08-03 12:25:02` | `cowrie.log.closed` |
| `2026-08-03 12:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d914c5e4d2c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:27 |
| **Last Seen** | 2026-08-03 12:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:27:47` | `cowrie.session.connect` |
| `2026-08-03 12:27:47` | `cowrie.client.version` |
| `2026-08-03 12:27:47` | `cowrie.client.kex` |
| `2026-08-03 12:27:48` | `cowrie.login.success` |
| `2026-08-03 12:27:49` | `cowrie.session.params` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.success` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.command.input` |
| `2026-08-03 12:27:49` | `cowrie.log.closed` |
| `2026-08-03 12:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4910af8460da

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:30 |
| **Last Seen** | 2026-08-03 12:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:30:30` | `cowrie.session.connect` |
| `2026-08-03 12:30:30` | `cowrie.client.version` |
| `2026-08-03 12:30:30` | `cowrie.client.kex` |
| `2026-08-03 12:30:31` | `cowrie.login.success` |
| `2026-08-03 12:30:32` | `cowrie.session.params` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.success` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.command.input` |
| `2026-08-03 12:30:32` | `cowrie.log.closed` |
| `2026-08-03 12:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feab621c6e00

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-03 12:31 |
| **Last Seen** | 2026-08-03 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:31:48` | `cowrie.session.connect` |
| `2026-08-03 12:31:48` | `cowrie.client.version` |
| `2026-08-03 12:31:48` | `cowrie.client.kex` |
| `2026-08-03 12:31:48` | `cowrie.login.success` |
| `2026-08-03 12:31:48` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:31:48` | `cowrie.direct-tcpip.data` |
| `2026-08-03 12:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26db8b98c281

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:35 |
| **Last Seen** | 2026-08-03 12:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:35:45` | `cowrie.session.connect` |
| `2026-08-03 12:35:46` | `cowrie.client.version` |
| `2026-08-03 12:35:46` | `cowrie.client.kex` |
| `2026-08-03 12:35:48` | `cowrie.login.success` |
| `2026-08-03 12:35:49` | `cowrie.session.params` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.success` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:49` | `cowrie.command.input` |
| `2026-08-03 12:35:50` | `cowrie.log.closed` |
| `2026-08-03 12:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf8941a0c12

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:38 |
| **Last Seen** | 2026-08-03 12:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:38:17` | `cowrie.session.connect` |
| `2026-08-03 12:38:17` | `cowrie.client.version` |
| `2026-08-03 12:38:17` | `cowrie.client.kex` |
| `2026-08-03 12:38:19` | `cowrie.login.success` |
| `2026-08-03 12:38:20` | `cowrie.session.params` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.success` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.command.input` |
| `2026-08-03 12:38:20` | `cowrie.log.closed` |
| `2026-08-03 12:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695b8f88d7c5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:40 |
| **Last Seen** | 2026-08-03 12:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:40:53` | `cowrie.session.connect` |
| `2026-08-03 12:40:53` | `cowrie.client.version` |
| `2026-08-03 12:40:53` | `cowrie.client.kex` |
| `2026-08-03 12:40:54` | `cowrie.login.success` |
| `2026-08-03 12:40:55` | `cowrie.session.params` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.success` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.command.input` |
| `2026-08-03 12:40:55` | `cowrie.log.closed` |
| `2026-08-03 12:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b777bf68ff4f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:43 |
| **Last Seen** | 2026-08-03 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:43:26` | `cowrie.session.connect` |
| `2026-08-03 12:43:26` | `cowrie.client.version` |
| `2026-08-03 12:43:26` | `cowrie.client.kex` |
| `2026-08-03 12:43:28` | `cowrie.login.success` |
| `2026-08-03 12:43:29` | `cowrie.session.params` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.success` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.command.input` |
| `2026-08-03 12:43:29` | `cowrie.log.closed` |
| `2026-08-03 12:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937b69b3135d

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:43 |
| **Last Seen** | 2026-08-03 12:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:43:41` | `cowrie.session.connect` |
| `2026-08-03 12:43:41` | `cowrie.client.version` |
| `2026-08-03 12:43:41` | `cowrie.client.kex` |
| `2026-08-03 12:43:42` | `cowrie.login.success` |
| `2026-08-03 12:43:43` | `cowrie.session.params` |
| `2026-08-03 12:43:43` | `cowrie.command.input` |
| `2026-08-03 12:43:43` | `cowrie.command.failed` |
| `2026-08-03 12:43:44` | `cowrie.log.closed` |
| `2026-08-03 12:43:45` | `cowrie.session.params` |
| `2026-08-03 12:43:45` | `cowrie.command.input` |
| `2026-08-03 12:43:45` | `cowrie.session.file_download` |
| `2026-08-03 12:43:45` | `cowrie.log.closed` |
| `2026-08-03 12:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b961d9424c69

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:43 |
| **Last Seen** | 2026-08-03 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:43:45` | `cowrie.session.connect` |
| `2026-08-03 12:43:45` | `cowrie.client.version` |
| `2026-08-03 12:43:45` | `cowrie.client.kex` |
| `2026-08-03 12:43:46` | `cowrie.login.success` |
| `2026-08-03 12:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7615e9926d14

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:43 |
| **Last Seen** | 2026-08-03 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:43:47` | `cowrie.session.connect` |
| `2026-08-03 12:43:47` | `cowrie.client.version` |
| `2026-08-03 12:43:47` | `cowrie.client.kex` |
| `2026-08-03 12:43:48` | `cowrie.login.success` |
| `2026-08-03 12:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72ca1762f4a3

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-08-03 12:44 |
| **Last Seen** | 2026-08-03 12:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:44:13` | `cowrie.session.connect` |
| `2026-08-03 12:44:14` | `cowrie.client.version` |
| `2026-08-03 12:44:14` | `cowrie.client.kex` |
| `2026-08-03 12:44:16` | `cowrie.login.success` |
| `2026-08-03 12:44:16` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217f1e93cb82

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:18` | `cowrie.session.connect` |
| `2026-08-03 12:45:18` | `cowrie.client.version` |
| `2026-08-03 12:45:18` | `cowrie.client.kex` |
| `2026-08-03 12:45:20` | `cowrie.login.success` |
| `2026-08-03 12:45:21` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de03d6532f2d

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:20` | `cowrie.session.connect` |
| `2026-08-03 12:45:20` | `cowrie.client.version` |
| `2026-08-03 12:45:20` | `cowrie.client.kex` |
| `2026-08-03 12:45:21` | `cowrie.login.success` |
| `2026-08-03 12:45:22` | `cowrie.session.params` |
| `2026-08-03 12:45:22` | `cowrie.command.input` |
| `2026-08-03 12:45:22` | `cowrie.command.failed` |
| `2026-08-03 12:45:22` | `cowrie.log.closed` |
| `2026-08-03 12:45:23` | `cowrie.session.params` |
| `2026-08-03 12:45:23` | `cowrie.command.input` |
| `2026-08-03 12:45:23` | `cowrie.session.file_download` |
| `2026-08-03 12:45:23` | `cowrie.log.closed` |
| `2026-08-03 12:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fd0ee4a7e8

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:24` | `cowrie.session.connect` |
| `2026-08-03 12:45:24` | `cowrie.client.version` |
| `2026-08-03 12:45:24` | `cowrie.client.kex` |
| `2026-08-03 12:45:25` | `cowrie.login.success` |
| `2026-08-03 12:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0208a87b790d

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:25` | `cowrie.session.connect` |
| `2026-08-03 12:45:25` | `cowrie.client.version` |
| `2026-08-03 12:45:25` | `cowrie.client.kex` |
| `2026-08-03 12:45:26` | `cowrie.login.success` |
| `2026-08-03 12:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3a816adce9

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:28` | `cowrie.session.connect` |
| `2026-08-03 12:45:29` | `cowrie.client.version` |
| `2026-08-03 12:45:29` | `cowrie.client.kex` |
| `2026-08-03 12:45:31` | `cowrie.login.success` |
| `2026-08-03 12:45:31` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3f2def6638

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:45 |
| **Last Seen** | 2026-08-03 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:45:59` | `cowrie.session.connect` |
| `2026-08-03 12:45:59` | `cowrie.client.version` |
| `2026-08-03 12:45:59` | `cowrie.client.kex` |
| `2026-08-03 12:46:00` | `cowrie.login.success` |
| `2026-08-03 12:46:01` | `cowrie.session.params` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.success` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.command.input` |
| `2026-08-03 12:46:01` | `cowrie.log.closed` |
| `2026-08-03 12:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34841f04f312

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]149` |
| **First Seen** | 2026-08-03 12:47 |
| **Last Seen** | 2026-08-03 12:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:47:30` | `cowrie.session.connect` |
| `2026-08-03 12:47:30` | `cowrie.client.version` |
| `2026-08-03 12:47:30` | `cowrie.client.kex` |
| `2026-08-03 12:47:31` | `cowrie.login.success` |
| `2026-08-03 12:47:32` | `cowrie.session.params` |
| `2026-08-03 12:47:32` | `cowrie.command.input` |
| `2026-08-03 12:47:32` | `cowrie.command.failed` |
| `2026-08-03 12:47:32` | `cowrie.log.closed` |
| `2026-08-03 12:47:33` | `cowrie.session.params` |
| `2026-08-03 12:47:33` | `cowrie.command.input` |
| `2026-08-03 12:47:33` | `cowrie.session.file_download` |
| `2026-08-03 12:47:33` | `cowrie.log.closed` |
| `2026-08-03 12:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760fcb514118

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]149` |
| **First Seen** | 2026-08-03 12:47 |
| **Last Seen** | 2026-08-03 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:47:33` | `cowrie.session.connect` |
| `2026-08-03 12:47:33` | `cowrie.client.version` |
| `2026-08-03 12:47:34` | `cowrie.client.kex` |
| `2026-08-03 12:47:34` | `cowrie.login.success` |
| `2026-08-03 12:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1acac13715cb

| Field | Detail |
|---|---|
| **Source IP** | `94.182.168[.]149` |
| **First Seen** | 2026-08-03 12:47 |
| **Last Seen** | 2026-08-03 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:47:35` | `cowrie.session.connect` |
| `2026-08-03 12:47:35` | `cowrie.client.version` |
| `2026-08-03 12:47:35` | `cowrie.client.kex` |
| `2026-08-03 12:47:36` | `cowrie.login.success` |
| `2026-08-03 12:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.182.168[.]149` to AbuseIPDB if not already reported
- [ ] Block `94.182.168[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb2c97d88c5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:48 |
| **Last Seen** | 2026-08-03 12:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:48:29` | `cowrie.session.connect` |
| `2026-08-03 12:48:29` | `cowrie.client.version` |
| `2026-08-03 12:48:30` | `cowrie.client.kex` |
| `2026-08-03 12:48:30` | `cowrie.login.success` |
| `2026-08-03 12:48:31` | `cowrie.session.params` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.success` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:31` | `cowrie.command.input` |
| `2026-08-03 12:48:32` | `cowrie.log.closed` |
| `2026-08-03 12:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e11a1a18040

| Field | Detail |
|---|---|
| **Source IP** | `118.43.236[.]237` |
| **First Seen** | 2026-08-03 12:49 |
| **Last Seen** | 2026-08-03 12:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:49:40` | `cowrie.session.connect` |
| `2026-08-03 12:49:41` | `cowrie.client.version` |
| `2026-08-03 12:49:41` | `cowrie.client.kex` |
| `2026-08-03 12:49:43` | `cowrie.login.success` |
| `2026-08-03 12:49:44` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.43.236[.]237` to AbuseIPDB if not already reported
- [ ] Block `118.43.236[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da9f17be7bc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:51 |
| **Last Seen** | 2026-08-03 12:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:51:02` | `cowrie.session.connect` |
| `2026-08-03 12:51:02` | `cowrie.client.version` |
| `2026-08-03 12:51:02` | `cowrie.client.kex` |
| `2026-08-03 12:51:02` | `cowrie.login.success` |
| `2026-08-03 12:51:04` | `cowrie.session.params` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.success` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.command.input` |
| `2026-08-03 12:51:04` | `cowrie.log.closed` |
| `2026-08-03 12:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b58b50b66c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]55` |
| **First Seen** | 2026-08-03 12:53 |
| **Last Seen** | 2026-08-03 12:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:53:28` | `cowrie.session.connect` |
| `2026-08-03 12:53:29` | `cowrie.client.version` |
| `2026-08-03 12:53:29` | `cowrie.client.kex` |
| `2026-08-03 12:53:30` | `cowrie.login.success` |
| `2026-08-03 12:53:32` | `cowrie.session.params` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.success` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.command.input` |
| `2026-08-03 12:53:32` | `cowrie.log.closed` |
| `2026-08-03 12:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]55` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fc785bbedf

| Field | Detail |
|---|---|
| **Source IP** | `188.168.86[.]6` |
| **First Seen** | 2026-08-03 12:54 |
| **Last Seen** | 2026-08-03 12:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:54:39` | `cowrie.session.connect` |
| `2026-08-03 12:54:40` | `cowrie.client.version` |
| `2026-08-03 12:54:40` | `cowrie.client.kex` |
| `2026-08-03 12:54:41` | `cowrie.login.success` |
| `2026-08-03 12:54:42` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.168.86[.]6` to AbuseIPDB if not already reported
- [ ] Block `188.168.86[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471ca2f9dec8

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-08-03 12:54 |
| **Last Seen** | 2026-08-03 12:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-03 12:54:47` | `cowrie.session.connect` |
| `2026-08-03 12:54:48` | `cowrie.client.version` |
| `2026-08-03 12:54:48` | `cowrie.client.kex` |
| `2026-08-03 12:54:50` | `cowrie.login.success` |
| `2026-08-03 12:54:51` | `cowrie.direct-tcpip.request` |
| `2026-08-03 12:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.227.254[.]154` | **6** | 2026-08-03 11:22 | 2026-08-03 12:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-03 11:05 | 2026-08-03 12:34 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.219.32[.]239` | **3** | 2026-08-03 11:14 | 2026-08-03 11:33 | 6m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-03 11:52 | 2026-08-03 11:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.226.38[.]71` | **3** | 2026-08-03 12:54 | 2026-08-03 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | **2** | 2026-08-03 12:08 | 2026-08-03 12:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]23` | **2** | 2026-08-03 12:24 | 2026-08-03 12:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]81` | **2** | 2026-08-03 11:50 | 2026-08-03 11:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.170.141[.]170` | 1 | 2026-08-03 12:26 | 2026-08-03 12:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.228.224[.]203` | 1 | 2026-08-03 12:45 | 2026-08-03 12:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.239[.]185` | 1 | 2026-08-03 11:53 | 2026-08-03 11:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.94.219[.]39` | 1 | 2026-08-03 12:44 | 2026-08-03 12:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | 1 | 2026-08-03 11:14 | 2026-08-03 11:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-08-03 12:35 | 2026-08-03 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]36` | 1 | 2026-08-03 11:01 | 2026-08-03 11:01 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `182.75.227[.]178` | IN | SANT SANDESH MEDIA &COMMU | **100** ⚠️ | 50 |
| `194.165.16[.]163` | PL | Flyservers S.A. | **100** ⚠️ | 50 |
| `178.178.222[.]60` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `191.210.73[.]33` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `188.168.86[.]6` | RU | TTK-Chita/BRAS in Chita | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `185.94.219[.]39` | UA | Laboratory of Information Technologies | **100** ⚠️ | 0 |
| `200.199.32[.]174` | BR | V tal | **100** ⚠️ | 50 |
| `5.175.192[.]197` | NL | MagicHosting | **100** ⚠️ | 5 |
| `219.128.15[.]190` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 78 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 15 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 14 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 14 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 130 cases |
| Tool 34  | Credential Extractor        | ✅ 99 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 65 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (13.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 80 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 25 session(s)).

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
_Report time: 2026-08-03T14:48:17Z_

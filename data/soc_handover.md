# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T19:06:56Z |
| **Shift Time** | 19:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **121** |
| Confirmed Threats | **94** |
| False Positives Filtered | **27** (22.3%) |
| Unique Attacker IPs | **68** |
| Countries of Origin | **25** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **81** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **153** |
| Unique Credential Pairs | **130** |
| Unique Usernames | **86** |
| Unique Passwords | **121** |
| Successful Auth Pairs | **145** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `nobody` | 7 |
| `ethereum` | 7 |
| `support` | 6 |
| `solana` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin123` | 6 |
| `support` | 4 |
| `112233` | 4 |
| `66666` | 3 |
| `1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `admin123` | 6 |
| `support` | `support` | 4 |
| `test` | `112233` | 4 |
| `ubnt` | `66666` | 3 |
| `root` | `﻿------fuck------` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubnt` | `66666` | `103.67.152.201` | 2026-08-11T16:59:31 |
| `ubnt` | `66666` | `122.187.147.13` | 2026-08-11T16:59:40 |
| `ubnt` | `66666` | `116.113.241.82` | 2026-08-11T16:59:45 |
| `support` | `support` | `176.53.159.196` | 2026-08-11T17:09:29 |
| `mark` | `mark` | `61.145.181.7` | 2026-08-11T17:09:58 |
| `test` | `112233` | `210.177.143.61` | 2026-08-11T17:16:23 |
| `test` | `112233` | `117.248.201.39` | 2026-08-11T17:16:35 |
| `root` | `﻿------fuck------` | `43.103.49.116` | 2026-08-11T17:17:40 |
| `test` | `112233` | `14.54.22.11` | 2026-08-11T17:32:42 |
| `test` | `112233` | `211.253.10.61` | 2026-08-11T17:32:52 |
| `support` | `support` | `10.0.0.73` | 2026-08-11T17:32:59 |
| `centos` | `2222` | `178.178.194.123` | 2026-08-11T17:33:51 |
| `root` | `zFNVcaCBbu` | `10.0.0.73` | 2026-08-11T17:42:03 |
| `admin` | `123abc` | `10.0.0.73` | 2026-08-11T17:49:22 |
| `nobody` | `admin123` | `10.0.0.73` | 2026-08-11T17:49:30 |
| `root` | `﻿------fuck------` | `121.229.38.239` | 2026-08-11T17:55:32 |
| `sol` | `sol` | `10.0.0.73` | 2026-08-11T17:58:37 |
| `solana` | `solana` | `10.0.0.73` | 2026-08-11T17:58:54 |
| `hyperliquid` | `hyperliquid` | `10.0.0.73` | 2026-08-11T17:59:12 |
| `hummingbot` | `hummingbot` | `10.0.0.73` | 2026-08-11T17:59:30 |
| `Ethereum` | `Ethereum` | `10.0.0.73` | 2026-08-11T17:59:47 |
| `eth` | `eth` | `10.0.0.73` | 2026-08-11T18:00:05 |
| `validator` | `validator` | `10.0.0.73` | 2026-08-11T18:00:23 |
| `trader` | `trader` | `10.0.0.73` | 2026-08-11T18:00:41 |
| `osmc` | `osmc` | `165.245.181.178` | 2026-08-11T18:00:54 |
| `freqtrade` | `freqtrade` | `10.0.0.73` | 2026-08-11T18:01:17 |
| `node` | `node` | `10.0.0.73` | 2026-08-11T18:01:35 |
| `passivbot` | `passivbot` | `10.0.0.73` | 2026-08-11T18:01:52 |
| `jesse` | `jesse` | `10.0.0.73` | 2026-08-11T18:02:10 |
| `octobot` | `octobot` | `10.0.0.73` | 2026-08-11T18:02:28 |
| `superalgos` | `superalgos` | `10.0.0.73` | 2026-08-11T18:02:45 |
| `gocryptotrader` | `gocryptotrader` | `10.0.0.73` | 2026-08-11T18:03:02 |
| `krypto-trading-bot` | `krypto-trading-bot` | `10.0.0.73` | 2026-08-11T18:03:20 |
| `tribeca` | `tribeca` | `10.0.0.73` | 2026-08-11T18:03:37 |
| `vyos` | `vyos` | `165.245.181.178` | 2026-08-11T18:03:38 |
| `kelp` | `kelp` | `10.0.0.73` | 2026-08-11T18:03:54 |
| `zenbot` | `zenbot` | `10.0.0.73` | 2026-08-11T18:04:11 |
| `gekko` | `gekko` | `10.0.0.73` | 2026-08-11T18:04:28 |
| `catalyst` | `catalyst` | `10.0.0.73` | 2026-08-11T18:04:45 |
| `blankly` | `blankly` | `10.0.0.73` | 2026-08-11T18:05:02 |
| `lumibot` | `lumibot` | `10.0.0.73` | 2026-08-11T18:05:19 |
| `binance-trade-bot` | `binance-trade-bot` | `10.0.0.73` | 2026-08-11T18:05:37 |
| `gunbot` | `gunbot` | `10.0.0.73` | 2026-08-11T18:05:55 |
| `nautilus-trader` | `nautilus-trader` | `10.0.0.73` | 2026-08-11T18:06:13 |
| `lean` | `lean` | `10.0.0.73` | 2026-08-11T18:06:31 |
| `backtrader` | `backtrader` | `10.0.0.73` | 2026-08-11T18:06:49 |
| `backtesting` | `backtesting` | `10.0.0.73` | 2026-08-11T18:07:07 |
| `vectorbt` | `vectorbt` | `10.0.0.73` | 2026-08-11T18:07:25 |
| `zipline` | `zipline` | `10.0.0.73` | 2026-08-11T18:07:43 |
| `pyalgotrade` | `pyalgotrade` | `10.0.0.73` | 2026-08-11T18:08:01 |
| `nobody` | `admin123` | `223.82.86.2` | 2026-08-11T18:08:02 |
| `nobody` | `admin123` | `114.30.223.119` | 2026-08-11T18:08:09 |
| `nobody` | `admin123` | `179.189.85.66` | 2026-08-11T18:08:11 |
| `qstrader` | `qstrader` | `10.0.0.73` | 2026-08-11T18:08:19 |
| `nobody` | `admin123` | `202.129.35.8` | 2026-08-11T18:08:22 |
| `bt` | `bt` | `10.0.0.73` | 2026-08-11T18:08:37 |
| `hftbacktest` | `hftbacktest` | `10.0.0.73` | 2026-08-11T18:08:54 |
| `barter` | `barter` | `10.0.0.73` | 2026-08-11T18:09:12 |
| `roboquant` | `roboquant` | `10.0.0.73` | 2026-08-11T18:09:30 |
| `stocksharp` | `stocksharp` | `10.0.0.73` | 2026-08-11T18:09:48 |
| `vnpy` | `vnpy` | `10.0.0.73` | 2026-08-11T18:10:05 |
| `wondertrader` | `wondertrader` | `10.0.0.73` | 2026-08-11T18:10:23 |
| `ethdocker` | `ethdocker` | `10.0.0.73` | 2026-08-11T18:10:40 |
| `ethereum` | `ethereum2025` | `10.0.0.73` | 2026-08-11T18:10:58 |
| `ethereum` | `ethereum2026` | `10.0.0.73` | 2026-08-11T18:11:16 |
| `ethereum` | `ethereum!2024` | `10.0.0.73` | 2026-08-11T18:11:33 |
| `ethereum` | `ethereum@2026` | `10.0.0.73` | 2026-08-11T18:11:51 |
| `solana` | `solana2026` | `10.0.0.73` | 2026-08-11T18:12:09 |
| `solana` | `solana!2026` | `10.0.0.73` | 2026-08-11T18:12:27 |
| `solana` | `sol!@#$` | `10.0.0.73` | 2026-08-11T18:12:45 |
| `solana` | `solana!@#$` | `10.0.0.73` | 2026-08-11T18:13:04 |
| `config` | `techsupport` | `203.252.10.3` | 2026-08-11T18:13:05 |
| `config` | `techsupport` | `95.79.57.221` | 2026-08-11T18:13:14 |
| `solana` | `solana1234` | `10.0.0.73` | 2026-08-11T18:13:22 |
| `firedancer` | `firedancer` | `10.0.0.73` | 2026-08-11T18:13:40 |
| `firedancer` | `solana` | `10.0.0.73` | 2026-08-11T18:13:59 |
| `firedancer` | `firedancer1234` | `10.0.0.73` | 2026-08-11T18:14:17 |
| `solv` | `solv` | `10.0.0.73` | 2026-08-11T18:14:35 |
| `solv` | `123456` | `10.0.0.73` | 2026-08-11T18:14:53 |
| `solv` | `1234` | `10.0.0.73` | 2026-08-11T18:15:11 |
| `eth.docker` | `eth.docker` | `10.0.0.73` | 2026-08-11T18:15:29 |
| `eth-docker` | `eth-docker` | `10.0.0.73` | 2026-08-11T18:15:46 |
| `ethdocker` | `docker@123` | `10.0.0.73` | 2026-08-11T18:16:04 |
| `eth` | `docker` | `10.0.0.73` | 2026-08-11T18:16:21 |
| `eth@docker` | `eth@docker` | `10.0.0.73` | 2026-08-11T18:16:39 |
| `ethdocker` | `eth@docker` | `10.0.0.73` | 2026-08-11T18:16:56 |
| `ethereum` | `ethereum` | `10.0.0.73` | 2026-08-11T18:17:14 |
| `eth` | `ethereum` | `10.0.0.73` | 2026-08-11T18:17:49 |
| `ether` | `ether` | `10.0.0.73` | 2026-08-11T18:18:07 |
| `ethereum` | `12345678` | `10.0.0.73` | 2026-08-11T18:18:26 |
| `ethereum` | `123456` | `10.0.0.73` | 2026-08-11T18:18:44 |
| `eth` | `1234` | `10.0.0.73` | 2026-08-11T18:19:02 |
| `eth` | `123` | `10.0.0.73` | 2026-08-11T18:19:21 |
| `geth` | `geth` | `10.0.0.73` | 2026-08-11T18:19:40 |
| `nethermind` | `nethermind` | `10.0.0.73` | 2026-08-11T18:19:59 |
| `besu` | `besu` | `10.0.0.73` | 2026-08-11T18:20:18 |
| `erigon` | `erigon` | `10.0.0.73` | 2026-08-11T18:20:37 |
| `reth` | `reth` | `10.0.0.73` | 2026-08-11T18:20:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-11T18:21:06 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-11T18:21:06 |
| `ethereumjs` | `ethereumjs` | `10.0.0.73` | 2026-08-11T18:21:15 |
| `silkworm` | `silkworm` | `10.0.0.73` | 2026-08-11T18:21:33 |
| `nimbus-eth1` | `nimbus-eth1` | `10.0.0.73` | 2026-08-11T18:21:51 |
| `ress` | `ress` | `10.0.0.73` | 2026-08-11T18:22:09 |
| `openethereum` | `openethereum` | `10.0.0.73` | 2026-08-11T18:22:28 |
| `blank` | `webadmin` | `10.0.0.73` | 2026-08-11T18:23:45 |
| `test` | `Passw@rd` | `10.0.0.73` | 2026-08-11T18:30:06 |
| `root` | `000000` | `2.57.122.209` | 2026-08-11T18:36:32 |
| `user01` | `user01!` | `165.154.235.9` | 2026-08-11T18:37:04 |
| `345gs5662d34` | `345gs5662d34` | `165.154.235.9` | 2026-08-11T18:37:06 |
| `user01` | `3245gs5662d34` | `165.154.235.9` | 2026-08-11T18:37:06 |
| `mongo` | `1qaz@WSX` | `103.210.22.17` | 2026-08-11T18:37:49 |
| `345gs5662d34` | `345gs5662d34` | `103.210.22.17` | 2026-08-11T18:37:53 |
| `mongo` | `3245gs5662d34` | `103.210.22.17` | 2026-08-11T18:37:54 |
| `root` | `111111` | `2.57.122.209` | 2026-08-11T18:39:33 |
| `blank` | `webadmin` | `122.160.50.155` | 2026-08-11T18:41:48 |
| `nobody` | `password321` | `179.189.85.66` | 2026-08-11T18:42:16 |
| `root` | `123` | `2.57.122.209` | 2026-08-11T18:42:36 |
| `ncts` | `ncts` | `10.0.0.73` | 2026-08-11T18:43:32 |
| `osmc` | `osmc` | `10.0.0.73` | 2026-08-11T18:43:54 |
| `trading` | `trading` | `10.0.0.73` | 2026-08-11T18:44:16 |
| `freight` | `freight` | `10.0.0.73` | 2026-08-11T18:44:37 |
| `tms` | `tms` | `10.0.0.73` | 2026-08-11T18:44:57 |
| `onroute` | `onroute` | `10.0.0.73` | 2026-08-11T18:45:18 |
| `root` | `123123` | `2.57.122.209` | 2026-08-11T18:45:37 |
| `logistics` | `logistics` | `10.0.0.73` | 2026-08-11T18:45:37 |
| `logic` | `logic` | `10.0.0.73` | 2026-08-11T18:45:58 |
| `root` | `logisticsadmin` | `10.0.0.73` | 2026-08-11T18:46:38 |
| `root` | `logistics@123` | `10.0.0.73` | 2026-08-11T18:46:57 |
| `logistaas` | `logistaas` | `10.0.0.73` | 2026-08-11T18:47:17 |
| `root` | `logistaaS` | `10.0.0.73` | 2026-08-11T18:47:36 |
| `root` | `logistaaS2026` | `10.0.0.73` | 2026-08-11T18:47:56 |
| `dispatcher` | `dispatcher` | `10.0.0.73` | 2026-08-11T18:48:14 |
| `root` | `123321` | `2.57.122.209` | 2026-08-11T18:48:27 |
| `ncts` | `ncts@1234` | `10.0.0.73` | 2026-08-11T18:48:34 |
| `ncts` | `admin1234` | `10.0.0.73` | 2026-08-11T18:48:53 |
| `ncts` | `admin` | `10.0.0.73` | 2026-08-11T18:49:12 |
| `billing` | `billing` | `10.0.0.73` | 2026-08-11T18:49:31 |
| `scanner` | `scanner` | `10.0.0.73` | 2026-08-11T18:49:51 |
| `server` | `server` | `10.0.0.73` | 2026-08-11T18:50:10 |
| `user` | `1` | `10.0.0.73` | 2026-08-11T18:50:30 |
| `root` | `admin` | `10.0.0.73` | 2026-08-11T18:50:50 |
| `root` | `1234` | `2.57.122.209` | 2026-08-11T18:51:16 |
| `support` | `qwerty123456` | `103.68.52.210` | 2026-08-11T18:52:32 |
| `root` | `12345` | `2.57.122.209` | 2026-08-11T18:54:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **121** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 19 |
| Go SSH scanner | 17 |
| libssh | 12 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 19 | 17 |
| `2ec37a7cc8da...` | Mirai/variant | 7 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 19 | 17 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 7 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.210.22.17`, `165.154.235.9`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **68** |
| Unique ASNs | **54** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 6 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS10396` | DATACOM CARIBE, INC. | 2 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS56045` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cb2dfdf02243

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-08-11 16:59 |
| **Last Seen** | 2026-08-11 16:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:59:28` | `cowrie.session.connect` |
| `2026-08-11 16:59:29` | `cowrie.client.version` |
| `2026-08-11 16:59:29` | `cowrie.client.kex` |
| `2026-08-11 16:59:31` | `cowrie.login.success` |
| `2026-08-11 16:59:32` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5abf41300059

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-08-11 16:59 |
| **Last Seen** | 2026-08-11 16:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:59:37` | `cowrie.session.connect` |
| `2026-08-11 16:59:38` | `cowrie.client.version` |
| `2026-08-11 16:59:38` | `cowrie.client.kex` |
| `2026-08-11 16:59:40` | `cowrie.login.success` |
| `2026-08-11 16:59:41` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6615fff98bfd

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-08-11 16:59 |
| **Last Seen** | 2026-08-11 16:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 16:59:42` | `cowrie.session.connect` |
| `2026-08-11 16:59:43` | `cowrie.client.version` |
| `2026-08-11 16:59:43` | `cowrie.client.kex` |
| `2026-08-11 16:59:45` | `cowrie.login.success` |
| `2026-08-11 16:59:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 16:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6fdd1faa08

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 17:09 |
| **Last Seen** | 2026-08-11 17:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:09:29` | `cowrie.session.connect` |
| `2026-08-11 17:09:29` | `cowrie.client.version` |
| `2026-08-11 17:09:29` | `cowrie.client.kex` |
| `2026-08-11 17:09:29` | `cowrie.login.success` |
| `2026-08-11 17:09:29` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:09:30` | `cowrie.direct-tcpip.data` |
| `2026-08-11 17:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce8d46744c5

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-08-11 17:09 |
| **Last Seen** | 2026-08-11 17:10 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:09:53` | `cowrie.session.connect` |
| `2026-08-11 17:09:54` | `cowrie.client.version` |
| `2026-08-11 17:09:54` | `cowrie.client.kex` |
| `2026-08-11 17:09:58` | `cowrie.login.success` |
| `2026-08-11 17:09:59` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a6468859d3

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-11 17:16 |
| **Last Seen** | 2026-08-11 17:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:16:20` | `cowrie.session.connect` |
| `2026-08-11 17:16:21` | `cowrie.client.version` |
| `2026-08-11 17:16:21` | `cowrie.client.kex` |
| `2026-08-11 17:16:23` | `cowrie.login.success` |
| `2026-08-11 17:16:24` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ba1da74b40

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-11 17:16 |
| **Last Seen** | 2026-08-11 17:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:16:33` | `cowrie.session.connect` |
| `2026-08-11 17:16:34` | `cowrie.client.version` |
| `2026-08-11 17:16:34` | `cowrie.client.kex` |
| `2026-08-11 17:16:35` | `cowrie.login.success` |
| `2026-08-11 17:16:35` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071be5037e64

| Field | Detail |
|---|---|
| **Source IP** | `43.103.49[.]116` |
| **First Seen** | 2026-08-11 17:17 |
| **Last Seen** | 2026-08-11 17:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:17:39` | `cowrie.session.connect` |
| `2026-08-11 17:17:39` | `cowrie.client.version` |
| `2026-08-11 17:17:40` | `cowrie.client.kex` |
| `2026-08-11 17:17:40` | `cowrie.login.success` |
| `2026-08-11 17:17:41` | `cowrie.session.params` |
| `2026-08-11 17:17:41` | `cowrie.command.input` |
| `2026-08-11 17:17:42` | `cowrie.log.closed` |
| `2026-08-11 17:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.103.49[.]116` to AbuseIPDB if not already reported
- [ ] Block `43.103.49[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c496ee96689f

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-11 17:32 |
| **Last Seen** | 2026-08-11 17:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:32:39` | `cowrie.session.connect` |
| `2026-08-11 17:32:40` | `cowrie.client.version` |
| `2026-08-11 17:32:40` | `cowrie.client.kex` |
| `2026-08-11 17:32:42` | `cowrie.login.success` |
| `2026-08-11 17:32:43` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64da327c9625

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-08-11 17:32 |
| **Last Seen** | 2026-08-11 17:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:32:48` | `cowrie.session.connect` |
| `2026-08-11 17:32:49` | `cowrie.client.version` |
| `2026-08-11 17:32:49` | `cowrie.client.kex` |
| `2026-08-11 17:32:52` | `cowrie.login.success` |
| `2026-08-11 17:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd6eeba0fa1

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-08-11 17:33 |
| **Last Seen** | 2026-08-11 17:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:33:50` | `cowrie.session.connect` |
| `2026-08-11 17:33:50` | `cowrie.client.version` |
| `2026-08-11 17:33:50` | `cowrie.client.kex` |
| `2026-08-11 17:33:51` | `cowrie.login.success` |
| `2026-08-11 17:33:52` | `cowrie.direct-tcpip.request` |
| `2026-08-11 17:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-597c4711f385

| Field | Detail |
|---|---|
| **Source IP** | `121.229.38[.]239` |
| **First Seen** | 2026-08-11 17:55 |
| **Last Seen** | 2026-08-11 17:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 17:55:32` | `cowrie.session.connect` |
| `2026-08-11 17:55:32` | `cowrie.client.version` |
| `2026-08-11 17:55:32` | `cowrie.client.kex` |
| `2026-08-11 17:55:32` | `cowrie.login.success` |
| `2026-08-11 17:55:34` | `cowrie.session.params` |
| `2026-08-11 17:55:34` | `cowrie.command.input` |
| `2026-08-11 17:55:34` | `cowrie.log.closed` |
| `2026-08-11 17:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.38[.]239` to AbuseIPDB if not already reported
- [ ] Block `121.229.38[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90543f8e5ef4

| Field | Detail |
|---|---|
| **Source IP** | `165.245.181[.]178` |
| **First Seen** | 2026-08-11 18:00 |
| **Last Seen** | 2026-08-11 18:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:00:53` | `cowrie.session.connect` |
| `2026-08-11 18:00:53` | `cowrie.client.version` |
| `2026-08-11 18:00:53` | `cowrie.client.kex` |
| `2026-08-11 18:00:54` | `cowrie.login.success` |
| `2026-08-11 18:00:55` | `cowrie.session.params` |
| `2026-08-11 18:00:55` | `cowrie.command.input` |
| `2026-08-11 18:00:56` | `cowrie.log.closed` |
| `2026-08-11 18:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.181[.]178` to AbuseIPDB if not already reported
- [ ] Block `165.245.181[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d247f64e20

| Field | Detail |
|---|---|
| **Source IP** | `165.245.181[.]178` |
| **First Seen** | 2026-08-11 18:03 |
| **Last Seen** | 2026-08-11 18:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:03:36` | `cowrie.session.connect` |
| `2026-08-11 18:03:36` | `cowrie.client.version` |
| `2026-08-11 18:03:36` | `cowrie.client.kex` |
| `2026-08-11 18:03:38` | `cowrie.login.success` |
| `2026-08-11 18:03:39` | `cowrie.session.params` |
| `2026-08-11 18:03:39` | `cowrie.command.input` |
| `2026-08-11 18:03:39` | `cowrie.log.closed` |
| `2026-08-11 18:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.245.181[.]178` to AbuseIPDB if not already reported
- [ ] Block `165.245.181[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342e1f5a4d17

| Field | Detail |
|---|---|
| **Source IP** | `223.82.86[.]2` |
| **First Seen** | 2026-08-11 18:07 |
| **Last Seen** | 2026-08-11 18:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:07:58` | `cowrie.session.connect` |
| `2026-08-11 18:07:59` | `cowrie.client.version` |
| `2026-08-11 18:07:59` | `cowrie.client.kex` |
| `2026-08-11 18:08:02` | `cowrie.login.success` |
| `2026-08-11 18:08:03` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `223.82.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cedcd8ff4b

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-11 18:08 |
| **Last Seen** | 2026-08-11 18:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:08:06` | `cowrie.session.connect` |
| `2026-08-11 18:08:07` | `cowrie.client.version` |
| `2026-08-11 18:08:07` | `cowrie.client.kex` |
| `2026-08-11 18:08:09` | `cowrie.login.success` |
| `2026-08-11 18:08:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb42dce7be9

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-11 18:08 |
| **Last Seen** | 2026-08-11 18:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:08:09` | `cowrie.session.connect` |
| `2026-08-11 18:08:09` | `cowrie.client.version` |
| `2026-08-11 18:08:09` | `cowrie.client.kex` |
| `2026-08-11 18:08:11` | `cowrie.login.success` |
| `2026-08-11 18:08:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16913c7690a9

| Field | Detail |
|---|---|
| **Source IP** | `202.129.35[.]8` |
| **First Seen** | 2026-08-11 18:08 |
| **Last Seen** | 2026-08-11 18:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:08:20` | `cowrie.session.connect` |
| `2026-08-11 18:08:20` | `cowrie.client.version` |
| `2026-08-11 18:08:20` | `cowrie.client.kex` |
| `2026-08-11 18:08:22` | `cowrie.login.success` |
| `2026-08-11 18:08:23` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.129.35[.]8` to AbuseIPDB if not already reported
- [ ] Block `202.129.35[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8c3aecc8ec

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-08-11 18:13 |
| **Last Seen** | 2026-08-11 18:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:13:02` | `cowrie.session.connect` |
| `2026-08-11 18:13:03` | `cowrie.client.version` |
| `2026-08-11 18:13:03` | `cowrie.client.kex` |
| `2026-08-11 18:13:05` | `cowrie.login.success` |
| `2026-08-11 18:13:06` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb84e872452

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-11 18:13 |
| **Last Seen** | 2026-08-11 18:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:13:12` | `cowrie.session.connect` |
| `2026-08-11 18:13:13` | `cowrie.client.version` |
| `2026-08-11 18:13:13` | `cowrie.client.kex` |
| `2026-08-11 18:13:14` | `cowrie.login.success` |
| `2026-08-11 18:13:14` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c1e7f70f0d8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 18:21 |
| **Last Seen** | 2026-08-11 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:21:05` | `cowrie.session.connect` |
| `2026-08-11 18:21:05` | `cowrie.client.version` |
| `2026-08-11 18:21:05` | `cowrie.client.kex` |
| `2026-08-11 18:21:06` | `cowrie.login.success` |
| `2026-08-11 18:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477b451989b9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 18:21 |
| **Last Seen** | 2026-08-11 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:21:05` | `cowrie.session.connect` |
| `2026-08-11 18:21:05` | `cowrie.client.version` |
| `2026-08-11 18:21:05` | `cowrie.client.kex` |
| `2026-08-11 18:21:06` | `cowrie.login.success` |
| `2026-08-11 18:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92640281bb00

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:36 |
| **Last Seen** | 2026-08-11 18:36 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:36:24` | `cowrie.session.connect` |
| `2026-08-11 18:36:25` | `cowrie.client.version` |
| `2026-08-11 18:36:25` | `cowrie.client.kex` |
| `2026-08-11 18:36:32` | `cowrie.login.success` |
| `2026-08-11 18:36:35` | `cowrie.session.params` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.success` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:35` | `cowrie.command.input` |
| `2026-08-11 18:36:36` | `cowrie.log.closed` |
| `2026-08-11 18:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d93296724e0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:03` | `cowrie.session.connect` |
| `2026-08-11 18:37:03` | `cowrie.client.version` |
| `2026-08-11 18:37:03` | `cowrie.client.kex` |
| `2026-08-11 18:37:04` | `cowrie.login.success` |
| `2026-08-11 18:37:04` | `cowrie.session.params` |
| `2026-08-11 18:37:04` | `cowrie.command.input` |
| `2026-08-11 18:37:04` | `cowrie.command.failed` |
| `2026-08-11 18:37:04` | `cowrie.log.closed` |
| `2026-08-11 18:37:05` | `cowrie.session.params` |
| `2026-08-11 18:37:05` | `cowrie.command.input` |
| `2026-08-11 18:37:05` | `cowrie.session.file_download` |
| `2026-08-11 18:37:05` | `cowrie.log.closed` |
| `2026-08-11 18:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34a7283dbe6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:05` | `cowrie.session.connect` |
| `2026-08-11 18:37:05` | `cowrie.client.version` |
| `2026-08-11 18:37:05` | `cowrie.client.kex` |
| `2026-08-11 18:37:06` | `cowrie.login.success` |
| `2026-08-11 18:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f7387f4325

| Field | Detail |
|---|---|
| **Source IP** | `165.154.235[.]9` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:06` | `cowrie.session.connect` |
| `2026-08-11 18:37:06` | `cowrie.client.version` |
| `2026-08-11 18:37:06` | `cowrie.client.kex` |
| `2026-08-11 18:37:06` | `cowrie.login.success` |
| `2026-08-11 18:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.235[.]9` to AbuseIPDB if not already reported
- [ ] Block `165.154.235[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-546de0a92d7d

| Field | Detail |
|---|---|
| **Source IP** | `103.210.22[.]17` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:47` | `cowrie.session.connect` |
| `2026-08-11 18:37:47` | `cowrie.client.version` |
| `2026-08-11 18:37:48` | `cowrie.client.kex` |
| `2026-08-11 18:37:49` | `cowrie.login.success` |
| `2026-08-11 18:37:50` | `cowrie.session.params` |
| `2026-08-11 18:37:50` | `cowrie.command.input` |
| `2026-08-11 18:37:50` | `cowrie.command.failed` |
| `2026-08-11 18:37:50` | `cowrie.log.closed` |
| `2026-08-11 18:37:51` | `cowrie.session.params` |
| `2026-08-11 18:37:51` | `cowrie.command.input` |
| `2026-08-11 18:37:51` | `cowrie.session.file_download` |
| `2026-08-11 18:37:51` | `cowrie.log.closed` |
| `2026-08-11 18:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.22[.]17` to AbuseIPDB if not already reported
- [ ] Block `103.210.22[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a88cd812f06

| Field | Detail |
|---|---|
| **Source IP** | `103.210.22[.]17` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:51` | `cowrie.session.connect` |
| `2026-08-11 18:37:51` | `cowrie.client.version` |
| `2026-08-11 18:37:52` | `cowrie.client.kex` |
| `2026-08-11 18:37:53` | `cowrie.login.success` |
| `2026-08-11 18:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.22[.]17` to AbuseIPDB if not already reported
- [ ] Block `103.210.22[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a9ed9dc273

| Field | Detail |
|---|---|
| **Source IP** | `103.210.22[.]17` |
| **First Seen** | 2026-08-11 18:37 |
| **Last Seen** | 2026-08-11 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:37:53` | `cowrie.session.connect` |
| `2026-08-11 18:37:53` | `cowrie.client.version` |
| `2026-08-11 18:37:53` | `cowrie.client.kex` |
| `2026-08-11 18:37:54` | `cowrie.login.success` |
| `2026-08-11 18:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.22[.]17` to AbuseIPDB if not already reported
- [ ] Block `103.210.22[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc372f158daa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:39 |
| **Last Seen** | 2026-08-11 18:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:39:27` | `cowrie.session.connect` |
| `2026-08-11 18:39:28` | `cowrie.client.version` |
| `2026-08-11 18:39:28` | `cowrie.client.kex` |
| `2026-08-11 18:39:33` | `cowrie.login.success` |
| `2026-08-11 18:39:37` | `cowrie.session.params` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.success` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:37` | `cowrie.command.input` |
| `2026-08-11 18:39:39` | `cowrie.log.closed` |
| `2026-08-11 18:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10a7d52bf2c

| Field | Detail |
|---|---|
| **Source IP** | `122.160.50[.]155` |
| **First Seen** | 2026-08-11 18:41 |
| **Last Seen** | 2026-08-11 18:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:41:46` | `cowrie.session.connect` |
| `2026-08-11 18:41:46` | `cowrie.client.version` |
| `2026-08-11 18:41:46` | `cowrie.client.kex` |
| `2026-08-11 18:41:48` | `cowrie.login.success` |
| `2026-08-11 18:41:49` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.50[.]155` to AbuseIPDB if not already reported
- [ ] Block `122.160.50[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9008563de080

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-11 18:42 |
| **Last Seen** | 2026-08-11 18:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:42:14` | `cowrie.session.connect` |
| `2026-08-11 18:42:14` | `cowrie.client.version` |
| `2026-08-11 18:42:14` | `cowrie.client.kex` |
| `2026-08-11 18:42:16` | `cowrie.login.success` |
| `2026-08-11 18:42:17` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4e4e206f16

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:42 |
| **Last Seen** | 2026-08-11 18:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:42:33` | `cowrie.session.connect` |
| `2026-08-11 18:42:34` | `cowrie.client.version` |
| `2026-08-11 18:42:34` | `cowrie.client.kex` |
| `2026-08-11 18:42:36` | `cowrie.login.success` |
| `2026-08-11 18:42:37` | `cowrie.session.params` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.success` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:37` | `cowrie.command.input` |
| `2026-08-11 18:42:40` | `cowrie.log.closed` |
| `2026-08-11 18:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed7a3ec7be1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:45 |
| **Last Seen** | 2026-08-11 18:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:45:31` | `cowrie.session.connect` |
| `2026-08-11 18:45:32` | `cowrie.client.version` |
| `2026-08-11 18:45:32` | `cowrie.client.kex` |
| `2026-08-11 18:45:37` | `cowrie.login.success` |
| `2026-08-11 18:45:40` | `cowrie.session.params` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.success` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:40` | `cowrie.command.input` |
| `2026-08-11 18:45:41` | `cowrie.log.closed` |
| `2026-08-11 18:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b96a33cd606

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:48 |
| **Last Seen** | 2026-08-11 18:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:48:20` | `cowrie.session.connect` |
| `2026-08-11 18:48:21` | `cowrie.client.version` |
| `2026-08-11 18:48:21` | `cowrie.client.kex` |
| `2026-08-11 18:48:27` | `cowrie.login.success` |
| `2026-08-11 18:48:29` | `cowrie.session.params` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.success` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:29` | `cowrie.command.input` |
| `2026-08-11 18:48:30` | `cowrie.log.closed` |
| `2026-08-11 18:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8cad48c9db6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:51 |
| **Last Seen** | 2026-08-11 18:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:51:09` | `cowrie.session.connect` |
| `2026-08-11 18:51:10` | `cowrie.client.version` |
| `2026-08-11 18:51:10` | `cowrie.client.kex` |
| `2026-08-11 18:51:16` | `cowrie.login.success` |
| `2026-08-11 18:51:20` | `cowrie.session.params` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.success` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.command.input` |
| `2026-08-11 18:51:20` | `cowrie.log.closed` |
| `2026-08-11 18:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ace1c5668bf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 18:52 |
| **Last Seen** | 2026-08-11 18:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:52:21` | `cowrie.session.connect` |
| `2026-08-11 18:52:21` | `cowrie.client.version` |
| `2026-08-11 18:52:21` | `cowrie.client.kex` |
| `2026-08-11 18:52:22` | `cowrie.login.success` |
| `2026-08-11 18:52:22` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:52:22` | `cowrie.direct-tcpip.data` |
| `2026-08-11 18:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8b0c762c0b

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-08-11 18:52 |
| **Last Seen** | 2026-08-11 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:52:29` | `cowrie.session.connect` |
| `2026-08-11 18:52:30` | `cowrie.client.version` |
| `2026-08-11 18:52:30` | `cowrie.client.kex` |
| `2026-08-11 18:52:32` | `cowrie.login.success` |
| `2026-08-11 18:52:32` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d958f47dc5

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-08-11 18:52 |
| **Last Seen** | 2026-08-11 18:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:52:38` | `cowrie.session.connect` |
| `2026-08-11 18:52:39` | `cowrie.client.version` |
| `2026-08-11 18:52:39` | `cowrie.client.kex` |
| `2026-08-11 18:52:41` | `cowrie.login.success` |
| `2026-08-11 18:52:42` | `cowrie.direct-tcpip.request` |
| `2026-08-11 18:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e1534165d7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-08-11 18:53 |
| **Last Seen** | 2026-08-11 18:54 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 18:53:58` | `cowrie.session.connect` |
| `2026-08-11 18:53:59` | `cowrie.client.version` |
| `2026-08-11 18:53:59` | `cowrie.client.kex` |
| `2026-08-11 18:54:07` | `cowrie.login.success` |
| `2026-08-11 18:54:10` | `cowrie.session.params` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.success` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:10` | `cowrie.command.input` |
| `2026-08-11 18:54:12` | `cowrie.log.closed` |
| `2026-08-11 18:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **18** | 2026-08-11 17:11 | 2026-08-11 18:38 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-11 17:10 | 2026-08-11 18:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `196.251.121[.]142` | **4** | 2026-08-11 17:02 | 2026-08-11 17:10 | 3m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]91` | **3** | 2026-08-11 18:16 | 2026-08-11 18:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **3** | 2026-08-11 16:56 | 2026-08-11 18:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-11 17:59 | 2026-08-11 17:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-11 17:42 | 2026-08-11 17:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-11 17:25 | 2026-08-11 18:26 | 2m | 0 | `T1592` | 🟢 LOW |
| `121.229.38[.]239` | 1 | 2026-08-11 17:55 | 2026-08-11 17:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.239.169[.]52` | 1 | 2026-08-11 18:48 | 2026-08-11 18:49 | 94s | 0 | `T1592` | 🟢 LOW |
| `14.103.45[.]20` | 1 | 2026-08-11 18:08 | 2026-08-11 18:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.245.181[.]178` | 1 | 2026-08-11 17:56 | 2026-08-11 17:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | 1 | 2026-08-11 17:49 | 2026-08-11 17:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `197.232.36[.]140` | 1 | 2026-08-11 17:20 | 2026-08-11 17:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-08-11 18:16 | 2026-08-11 18:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-08-11 18:18 | 2026-08-11 18:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `38.172.184[.]129` | 1 | 2026-08-11 17:23 | 2026-08-11 17:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]186` | 1 | 2026-08-11 17:52 | 2026-08-11 17:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | 1 | 2026-08-11 18:03 | 2026-08-11 18:03 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.164.37[.]170` | 1 | 2026-08-11 18:07 | 2026-08-11 18:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `84.244.58[.]222` | 1 | 2026-08-11 18:13 | 2026-08-11 18:13 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]6` | 1 | 2026-08-11 18:33 | 2026-08-11 18:33 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `121.229.38[.]239` | CN | CHINANET jiangsu province network | **100** ⚠️ | 3 |
| `117.248.201[.]39` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 7 |
| `202.129.35[.]8` | TH | National Telecom Public Company Limited | **100** ⚠️ | 50 |
| `122.187.147[.]13` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `103.67.152[.]201` | IN | Netfirre Communications Pvt Ltd | **100** ⚠️ | 50 |
| `122.160.50[.]155` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |
| `114.30.223[.]119` | KR | HVHonam | **100** ⚠️ | 50 |
| `66.132.195[.]35` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 7 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 7 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 7 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 121 cases |
| Tool 34  | Credential Extractor        | ✅ 153 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 68 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (22.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 40 session(s)).

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
_Report time: 2026-08-11T19:06:56Z_

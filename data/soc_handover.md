# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-27 |
| **Generated At** | 2026-07-27T17:47:19Z |
| **Shift Time** | 17:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **307** |
| Confirmed Threats | **278** |
| False Positives Filtered | **29** (9.4%) |
| Unique Attacker IPs | **143** |
| Countries of Origin | **38** |
| High Severity Cases | **144** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **163** |
| Malware Samples Analyzed | **3** HIGH · **31** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **256** |
| Unique Credential Pairs | **176** |
| Unique Usernames | **19** |
| Unique Passwords | **150** |
| Successful Auth Pairs | **236** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 85 |
| `ubuntu` | 41 |
| `user` | 24 |
| `admin` | 22 |
| `support` | 15 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r` | 9 |
| `admin` | 8 |
| `3245gs5662d34` | 6 |
| `555` | 6 |
| `smo@@kkklss` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 7 |
| `administrator` | `1q2w3e4r` | 6 |
| `config` | `555` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `@dmin@123456` | `10.0.0.73` | 2026-07-27T12:56:27 |
| `root` | `ssh-probe-3493C641B8BC0C6A4A914443D8E2D2A8193B596558B1676D` | `10.0.0.73` | 2026-07-27T12:56:28 |
| `root` | `1234!abcd` | `10.0.0.73` | 2026-07-27T13:01:42 |
| `root` | `ssh-probe-292FD5AE160651B7DCE9362589EC593BE86DF9253BCDDB6B` | `10.0.0.73` | 2026-07-27T13:01:42 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-27T13:03:50 |
| `erpnext` | `1234` | `189.204.230.91` | 2026-07-27T13:05:07 |
| `345gs5662d34` | `345gs5662d34` | `189.204.230.91` | 2026-07-27T13:05:15 |
| `erpnext` | `3245gs5662d34` | `189.204.230.91` | 2026-07-27T13:05:23 |
| `postgres` | `Passw0rd` | `96.56.228.149` | 2026-07-27T13:08:33 |
| `postgres` | `Passw0rd` | `103.158.138.179` | 2026-07-27T13:08:45 |
| `test` | `777` | `103.174.145.35` | 2026-07-27T13:11:15 |
| `test` | `777` | `10.0.0.73` | 2026-07-27T13:11:41 |
| `root` | `adm!n111` | `10.0.0.73` | 2026-07-27T13:11:44 |
| `root` | `ssh-probe-05A0AFE8DC2E0D6440471E1764400CA3143DFBC23313BFA9` | `10.0.0.73` | 2026-07-27T13:11:45 |
| `user` | `user555` | `78.187.230.168` | 2026-07-27T13:15:34 |
| `root` | `Qaz12345` | `10.0.0.73` | 2026-07-27T13:16:45 |
| `root` | `ssh-probe-D8E15AFF7BA5056B96F4F327E411F015DF9908EAE1E6928A` | `10.0.0.73` | 2026-07-27T13:16:47 |
| `user` | `user555` | `103.147.248.23` | 2026-07-27T13:18:52 |
| `user` | `user555` | `222.99.52.202` | 2026-07-27T13:19:01 |
| `user` | `user555` | `10.0.0.73` | 2026-07-27T13:19:19 |
| `ubuntu` | `P@ssw0rd2024` | `115.191.23.138` | 2026-07-27T13:20:23 |
| `root` | `q1` | `10.0.0.73` | 2026-07-27T13:21:51 |
| `root` | `ssh-probe-F052BDDA90EC108A45ACED58F4A24300FEE3E41866573020` | `10.0.0.73` | 2026-07-27T13:21:52 |
| `root` | `reset@123` | `157.10.182.14` | 2026-07-27T13:24:51 |
| `345gs5662d34` | `345gs5662d34` | `157.10.182.14` | 2026-07-27T13:24:55 |
| `root` | `3245gs5662d34` | `157.10.182.14` | 2026-07-27T13:24:57 |
| `root` | `P45$word@2026` | `10.0.0.73` | 2026-07-27T13:26:48 |
| `root` | `ssh-probe-237A64F6FDB9894761431257FA14B538F92D4FFB11757DE1` | `10.0.0.73` | 2026-07-27T13:26:49 |
| `root` | `abc123456!` | `10.0.0.73` | 2026-07-27T13:31:56 |
| `root` | `ssh-probe-BBB6ACAD923AE893F98CECE634A5E9AFD0FD3EC1CD9C212F` | `10.0.0.73` | 2026-07-27T13:31:59 |
| `root` | `1q2w3e4r` | `164.92.140.160` | 2026-07-27T13:35:33 |
| `345gs5662d34` | `345gs5662d34` | `164.92.140.160` | 2026-07-27T13:35:35 |
| `root` | `3245gs5662d34` | `164.92.140.160` | 2026-07-27T13:35:36 |
| `unknown` | `unknown555` | `175.206.113.91` | 2026-07-27T13:35:52 |
| `unknown` | `unknown555` | `10.0.0.73` | 2026-07-27T13:36:19 |
| `user` | `777` | `76.132.238.43` | 2026-07-27T13:36:34 |
| `user` | `777` | `14.153.226.88` | 2026-07-27T13:36:47 |
| `root` | `P4s5word@1234` | `10.0.0.73` | 2026-07-27T13:36:57 |
| `root` | `ssh-probe-5B4A35B500D9C9329EC890865F7DFD92714691A49B5768A1` | `10.0.0.73` | 2026-07-27T13:36:58 |
| `nobody` | `44444` | `201.63.52.54` | 2026-07-27T13:40:17 |
| `root` | `adm1n123456` | `10.0.0.73` | 2026-07-27T13:42:11 |
| `root` | `ssh-probe-DD7C695CB4188ED10530B3D34EF7F7D8D5DA4A50941EFA0E` | `10.0.0.73` | 2026-07-27T13:42:13 |
| `nobody` | `44444` | `10.0.0.73` | 2026-07-27T13:44:05 |
| `micro` | `123` | `92.205.177.212` | 2026-07-27T13:45:43 |
| `345gs5662d34` | `345gs5662d34` | `92.205.177.212` | 2026-07-27T13:45:46 |
| `micro` | `3245gs5662d34` | `92.205.177.212` | 2026-07-27T13:45:46 |
| `root` | `Janautthan2019` | `10.0.0.73` | 2026-07-27T13:47:20 |
| `root` | `ssh-probe-6DCF017F8F2A96722AC13F7EC91C805582D5C7D9DCF41B73` | `10.0.0.73` | 2026-07-27T13:47:26 |
| `root` | `p4$sword2026` | `10.0.0.73` | 2026-07-27T13:52:24 |
| `root` | `ssh-probe-850EAD13B2DAD3C8C53C6B220A226943A1CE7D17EA78F0CD` | `10.0.0.73` | 2026-07-27T13:52:25 |
| `administrator` | `uploader` | `102.90.34.90` | 2026-07-27T13:57:16 |
| `root` | `Admin@321` | `10.0.0.73` | 2026-07-27T13:57:28 |
| `root` | `ssh-probe-098FA0D3FBB3479E007F589AE67ED230C0EFA12E8C2CB468` | `10.0.0.73` | 2026-07-27T13:57:29 |
| `administrator` | `1q2w3e4r` | `175.43.184.200` | 2026-07-27T13:57:56 |
| `administrator` | `1q2w3e4r` | `81.195.152.14` | 2026-07-27T13:58:08 |
| `administrator` | `uploader` | `103.103.53.44` | 2026-07-27T14:00:39 |
| `administrator` | `1q2w3e4r` | `117.226.48.35` | 2026-07-27T14:01:27 |
| `administrator` | `1q2w3e4r` | `111.39.167.59` | 2026-07-27T14:01:39 |
| `administrator` | `1q2w3e4r` | `10.0.0.73` | 2026-07-27T14:01:45 |
| `root` | `P4$sw0rd@1234` | `10.0.0.73` | 2026-07-27T14:02:34 |
| `root` | `ssh-probe-7D98CE85EBFBCD34D18AAFD4129C3A6825A5EB3C8082EC0D` | `10.0.0.73` | 2026-07-27T14:02:36 |
| `config` | `555` | `190.223.36.108` | 2026-07-27T14:04:56 |
| `config` | `555` | `213.230.65.53` | 2026-07-27T14:05:08 |
| `root` | `qwer-1234` | `10.0.0.73` | 2026-07-27T14:07:35 |
| `root` | `ssh-probe-0AE20FA081C6BE1E899B27EA003B2B2BE7F4980F15B0CA38` | `10.0.0.73` | 2026-07-27T14:07:36 |
| `config` | `555` | `23.30.11.253` | 2026-07-27T14:08:13 |
| `config` | `555` | `182.76.36.62` | 2026-07-27T14:08:25 |
| `config` | `555` | `10.0.0.73` | 2026-07-27T14:08:38 |
| `root` | `Aurora123` | `10.0.0.73` | 2026-07-27T14:12:38 |
| `root` | `ssh-probe-C3BD43FBF4E68E6C582D0A1B7431631C8B1B314D3AEBBB03` | `10.0.0.73` | 2026-07-27T14:12:39 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-27T14:16:29 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-27T14:16:31 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-27T14:16:37 |
| `root` | `@dm!n11` | `10.0.0.73` | 2026-07-27T14:22:49 |
| `root` | `ssh-probe-F610E0350E9CD471B977A2CA148477C1B4706B7953DB591D` | `10.0.0.73` | 2026-07-27T14:22:50 |
| `administrator` | `logon` | `94.205.250.78` | 2026-07-27T14:25:09 |
| `administrator` | `logon` | `10.0.0.73` | 2026-07-27T14:25:34 |
| `postgres` | `1q2w3e4r` | `10.0.0.73` | 2026-07-27T14:26:12 |
| `root` | `pa$$w0rd@2026` | `10.0.0.73` | 2026-07-27T14:27:56 |
| `root` | `ssh-probe-4FFD6C104E3C02F9B9BC2962CD49C1CC4E2DD33C2E5701BE` | `10.0.0.73` | 2026-07-27T14:27:57 |
| `blank` | `blank111` | `111.53.131.79` | 2026-07-27T14:29:32 |
| `blank` | `blank111` | `118.122.196.230` | 2026-07-27T14:29:49 |
| `root` | `4dmin12345678!` | `10.0.0.73` | 2026-07-27T14:33:03 |
| `root` | `ssh-probe-5343EE0F7D419CE6D44BFF9DA0F74737F50696BEBDC24E37` | `10.0.0.73` | 2026-07-27T14:33:03 |
| `blank` | `blank111` | `222.120.176.6` | 2026-07-27T14:33:06 |
| `blank` | `blank111` | `10.0.0.73` | 2026-07-27T14:33:21 |
| `root` | `@dmin11!` | `10.0.0.73` | 2026-07-27T14:38:10 |
| `root` | `ssh-probe-902F60A51CA38CE7A76D8C7FE4058D974329BBED96098945` | `10.0.0.73` | 2026-07-27T14:38:11 |
| `admin` | `CalVxePV1!` | `94.154.43.210` | 2026-07-27T14:43:35 |
| `root` | `123qwe123` | `193.24.211.76` | 2026-07-27T14:45:42 |
| `support` | `support111` | `1.212.225.99` | 2026-07-27T14:46:31 |
| `support` | `support111` | `211.238.237.254` | 2026-07-27T14:46:44 |
| `user` | `6666666` | `102.90.34.90` | 2026-07-27T14:47:09 |
| `user` | `6666666` | `82.193.122.91` | 2026-07-27T14:47:20 |
| `support` | `support111` | `34.146.217.105` | 2026-07-27T14:49:54 |
| `user` | `6666666` | `10.0.0.73` | 2026-07-27T14:51:01 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-27T14:53:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-27T14:53:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-27T14:53:43 |
| `postgres` | `asdfgh` | `223.107.72.234` | 2026-07-27T14:54:21 |
| `postgres` | `asdfgh` | `10.0.0.73` | 2026-07-27T14:58:03 |
| `ubuntu` | `Local123` | `10.0.0.73` | 2026-07-27T15:04:33 |
| `ubuntu` | `ssh-probe-88D78D75C688CF6EA61314486C5F0E7C81D590ABF05CB157` | `10.0.0.73` | 2026-07-27T15:04:34 |
| `root` | `` | `176.65.148.93` | 2026-07-27T15:07:32 |
| `ubuntu` | `Ff123456` | `10.0.0.73` | 2026-07-27T15:09:25 |
| `ubuntu` | `ssh-probe-62B9B8251711FC2D7006EBFC82AF34CFBF75D8E5C01647F7` | `10.0.0.73` | 2026-07-27T15:09:29 |
| `debian` | `999` | `31.41.84.98` | 2026-07-27T15:11:55 |
| `ubuntu` | `4dm1n1234567!` | `10.0.0.73` | 2026-07-27T15:14:18 |
| `ubuntu` | `ssh-probe-748891B9F7FE0EB4D8E8D73865235941846CF5A8D414A545` | `10.0.0.73` | 2026-07-27T15:14:22 |
| `postgres` | `112233` | `179.185.227.77` | 2026-07-27T15:14:32 |
| `debian` | `999` | `10.0.0.73` | 2026-07-27T15:15:43 |
| `guest` | `4` | `113.200.216.246` | 2026-07-27T15:18:57 |
| `guest` | `4` | `195.222.57.190` | 2026-07-27T15:19:04 |
| `ubuntu` | `P@s$word@12345` | `10.0.0.73` | 2026-07-27T15:19:13 |
| `ubuntu` | `ssh-probe-36355CF8D9DC2D25C390009D881BC3E1CD4EB9CBEE8A2224` | `10.0.0.73` | 2026-07-27T15:19:15 |
| `guest` | `4` | `10.0.0.73` | 2026-07-27T15:22:43 |
| `ubuntu` | `India123` | `10.0.0.73` | 2026-07-27T15:24:09 |
| `ubuntu` | `ssh-probe-484AED6502E63851728CC7C3F30570925856DB2EA9373A2B` | `10.0.0.73` | 2026-07-27T15:24:10 |
| `ubuntu` | `P@$5word@12345` | `10.0.0.73` | 2026-07-27T15:29:03 |
| `ubuntu` | `ssh-probe-9A5C11AF52DAE1C489661120E31CE71E40475D827536BD02` | `10.0.0.73` | 2026-07-27T15:29:04 |
| `ubuntu` | `qwertyuiop@123` | `10.0.0.73` | 2026-07-27T15:33:53 |
| `ubuntu` | `ssh-probe-E36479ACC9A2B1FE9ABCD75A8262BF854554F6A8AE3FC29A` | `10.0.0.73` | 2026-07-27T15:33:54 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-27T15:35:57 |
| `operator` | `operator888` | `208.96.233.67` | 2026-07-27T15:39:45 |
| `operator` | `operator888` | `61.2.228.177` | 2026-07-27T15:39:54 |
| `operator` | `operator888` | `10.0.0.73` | 2026-07-27T15:40:17 |
| `ubuntu` | `Lm123456` | `10.0.0.73` | 2026-07-27T15:43:39 |
| `ubuntu` | `ssh-probe-48FB5D6FBC70D67B71791D39F429DD4465371FF2ED05631E` | `10.0.0.73` | 2026-07-27T15:43:39 |
| `support` | `66` | `222.236.155.146` | 2026-07-27T15:43:55 |
| `support` | `66` | `222.86.168.224` | 2026-07-27T15:47:10 |
| `support` | `66` | `187.126.105.42` | 2026-07-27T15:47:20 |
| `ubuntu` | `P@$sword@123456` | `10.0.0.73` | 2026-07-27T15:48:29 |
| `ubuntu` | `ssh-probe-28B3FD1FD4A7AD13C4266BCEBE085B1D806B32E48F92C67A` | `10.0.0.73` | 2026-07-27T15:48:31 |
| `ubuntu` | `root@123` | `10.0.0.73` | 2026-07-27T15:53:23 |
| `ubuntu` | `ssh-probe-C589C5A7A9F67F71F8962155B2012D0A738F0300D1778360` | `10.0.0.73` | 2026-07-27T15:53:25 |
| `root` | `admin` | `193.32.162.34` | 2026-07-27T15:54:59 |
| `root` | `password` | `193.32.162.34` | 2026-07-27T15:56:12 |
| `root` | `toor` | `193.32.162.34` | 2026-07-27T15:58:35 |
| `ubuntu` | `@dm1n11!` | `10.0.0.73` | 2026-07-27T15:58:54 |
| `ubuntu` | `ssh-probe-49F60085CBFE23FD46B9BB70F814452BBA3C286477721E89` | `10.0.0.73` | 2026-07-27T15:58:54 |
| `root` | `qwerty` | `193.32.162.34` | 2026-07-27T15:59:45 |
| `operator` | `operator2015` | `178.216.165.187` | 2026-07-27T16:00:27 |
| `operator` | `operator2015` | `183.104.220.84` | 2026-07-27T16:00:35 |
| `root` | `12345` | `193.32.162.34` | 2026-07-27T16:00:53 |
| `ubuntu` | `asdfgh` | `112.25.140.211` | 2026-07-27T16:01:03 |
| `ubuntu` | `asdfgh` | `60.172.41.103` | 2026-07-27T16:01:18 |
| `root` | `letmein` | `193.32.162.34` | 2026-07-27T16:02:01 |
| `root` | `123456789` | `193.32.162.34` | 2026-07-27T16:03:11 |
| `root` | `admin123` | `193.32.162.34` | 2026-07-27T16:04:16 |
| `operator` | `operator2015` | `10.0.0.73` | 2026-07-27T16:04:19 |
| `support` | `support` | `176.53.159.196` | 2026-07-27T16:04:30 |
| `root` | `welcome` | `193.32.162.34` | 2026-07-27T16:05:18 |
| `root` | `Default123` | `14.103.115.213` | 2026-07-27T16:05:23 |
| `root` | `3245gs5662d34` | `14.103.115.213` | 2026-07-27T16:05:56 |
| `root` | `P@ssw0rd` | `193.32.162.34` | 2026-07-27T16:06:20 |
| `root` | `passw0rd` | `193.32.162.34` | 2026-07-27T16:07:25 |
| `ubuntu` | `Xs123456` | `10.0.0.73` | 2026-07-27T16:08:10 |
| `ubuntu` | `ssh-probe-C852FA5AF12C3B6DA774CD22F39210410A34595C70F676D3` | `10.0.0.73` | 2026-07-27T16:08:10 |
| `admin` | `admin` | `213.141.130.251` | 2026-07-27T16:08:22 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-27T16:08:27 |
| `root` | `root123` | `193.32.162.34` | 2026-07-27T16:08:30 |
| `root` | `Qwer@12345` | `14.103.115.117` | 2026-07-27T16:08:43 |
| `345gs5662d34` | `345gs5662d34` | `14.103.115.117` | 2026-07-27T16:08:48 |
| `root` | `3245gs5662d34` | `14.103.115.117` | 2026-07-27T16:08:52 |
| `root` | `alpine` | `193.32.162.34` | 2026-07-27T16:09:38 |
| `root` | `changeme` | `193.32.162.34` | 2026-07-27T16:10:46 |
| `administrator` | `test` | `10.0.0.73` | 2026-07-27T16:11:55 |
| `root` | `default` | `193.32.162.34` | 2026-07-27T16:11:56 |
| `root` | `r00t` | `193.32.162.34` | 2026-07-27T16:13:04 |
| `ubuntu` | `Admin123123` | `10.0.0.73` | 2026-07-27T16:13:15 |
| `ubuntu` | `ssh-probe-0DD9AEE8E61F323A06BD5B3ACFF3FAEA3BE1A81248C670EA` | `10.0.0.73` | 2026-07-27T16:13:16 |
| `root` | `root@123` | `193.32.162.34` | 2026-07-27T16:14:10 |
| `root` | `Root123` | `193.32.162.34` | 2026-07-27T16:15:17 |
| `root` | `!root` | `193.32.162.34` | 2026-07-27T16:16:24 |
| `root` | `rootme` | `193.32.162.34` | 2026-07-27T16:17:33 |
| `ubuntu` | `Password99` | `10.0.0.73` | 2026-07-27T16:17:50 |
| `ubuntu` | `ssh-probe-BE72490FD55243D0BABA5D672F8156410DED4A9CB07D8354` | `10.0.0.73` | 2026-07-27T16:17:50 |
| `admin` | `admin` | `193.32.162.34` | 2026-07-27T16:18:43 |
| `admin` | `password` | `193.32.162.34` | 2026-07-27T16:19:56 |
| `admin` | `123456` | `193.32.162.34` | 2026-07-27T16:21:21 |
| `admin` | `admin123` | `193.32.162.34` | 2026-07-27T16:22:47 |
| `admin` | `letmein` | `193.32.162.34` | 2026-07-27T16:24:06 |
| `support` | `7777` | `49.124.153.12` | 2026-07-27T16:24:58 |
| `support` | `7777` | `218.149.235.152` | 2026-07-27T16:25:11 |
| `admin` | `qwerty` | `193.32.162.34` | 2026-07-27T16:25:16 |
| `config` | `5555555` | `34.146.248.7` | 2026-07-27T16:25:36 |
| `config` | `5555555` | `222.139.245.137` | 2026-07-27T16:25:45 |
| `admin` | `12345` | `193.32.162.34` | 2026-07-27T16:26:27 |
| `ubuntu` | `qwert123` | `10.0.0.73` | 2026-07-27T16:27:20 |
| `ubuntu` | `ssh-probe-57CC1BCED781B18DA3BDB0F45F8CC82AF84BAD6CC01DCFFA` | `10.0.0.73` | 2026-07-27T16:27:21 |
| `admin` | `admin@123` | `193.32.162.34` | 2026-07-27T16:27:38 |
| `support` | `7777` | `183.233.85.194` | 2026-07-27T16:28:24 |
| `support` | `7777` | `10.0.0.73` | 2026-07-27T16:28:42 |
| `admin` | `Admin123` | `193.32.162.34` | 2026-07-27T16:28:44 |
| `config` | `5555555` | `14.194.128.158` | 2026-07-27T16:28:51 |
| `config` | `5555555` | `113.28.86.1` | 2026-07-27T16:29:00 |
| `config` | `5555555` | `10.0.0.73` | 2026-07-27T16:29:16 |
| `admin` | `P@ssw0rd` | `193.32.162.34` | 2026-07-27T16:29:51 |
| `support` | `support` | `10.0.0.73` | 2026-07-27T16:29:56 |
| `admin` | `welcome` | `193.32.162.34` | 2026-07-27T16:30:56 |
| `admin` | `passw0rd` | `193.32.162.34` | 2026-07-27T16:32:03 |
| `ubuntu` | `password123$` | `10.0.0.73` | 2026-07-27T16:32:12 |
| `ubuntu` | `ssh-probe-46B2B0BD427EC8AF0C56DB855E751A784AF975D9FCA5FC48` | `10.0.0.73` | 2026-07-27T16:32:13 |
| `nobody` | `2` | `14.54.22.11` | 2026-07-27T16:32:49 |
| `nobody` | `2` | `110.14.192.20` | 2026-07-27T16:32:59 |
| `admin` | `administrator` | `193.32.162.34` | 2026-07-27T16:33:15 |
| `admin` | `adminroot` | `193.32.162.34` | 2026-07-27T16:34:32 |
| `admin` | `adminadmin` | `193.32.162.34` | 2026-07-27T16:35:54 |
| `nobody` | `2` | `10.0.0.73` | 2026-07-27T16:36:41 |
| `ubuntu` | `P@$$w0rd@123` | `10.0.0.73` | 2026-07-27T16:37:02 |
| `ubuntu` | `ssh-probe-8BFC7421D8C4BB3E7D9825B26A5501CF7A7B6988F81A0494` | `10.0.0.73` | 2026-07-27T16:37:03 |
| `user` | `user` | `193.32.162.34` | 2026-07-27T16:37:05 |
| `user` | `password` | `193.32.162.34` | 2026-07-27T16:38:12 |
| `user` | `123456` | `193.32.162.34` | 2026-07-27T16:39:19 |
| `user` | `qwerty` | `193.32.162.34` | 2026-07-27T16:40:28 |
| `user` | `12345` | `193.32.162.34` | 2026-07-27T16:41:38 |
| `ubuntu` | `1Qaz` | `10.0.0.73` | 2026-07-27T16:41:50 |
| `ubuntu` | `ssh-probe-1E74A3F2EB68E3446E052F130448D4C2D6693695C313914B` | `10.0.0.73` | 2026-07-27T16:41:51 |
| `user` | `letmein` | `193.32.162.34` | 2026-07-27T16:42:48 |
| `user` | `welcome` | `193.32.162.34` | 2026-07-27T16:43:59 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-27T16:44:43 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-27T16:44:44 |
| `user` | `passw0rd` | `193.32.162.34` | 2026-07-27T16:45:12 |
| `user` | `user123` | `193.32.162.34` | 2026-07-27T16:46:30 |
| `user` | `user1` | `193.32.162.34` | 2026-07-27T16:47:41 |
| `user` | `userpass` | `193.32.162.34` | 2026-07-27T16:48:46 |
| `user` | `user@123` | `193.32.162.34` | 2026-07-27T16:49:52 |
| `user` | `User123` | `193.32.162.34` | 2026-07-27T16:51:04 |
| `ubuntu` | `pas$w0rd12345` | `10.0.0.73` | 2026-07-27T16:51:35 |
| `ubuntu` | `ssh-probe-DA3E6DF42F6BCC33FFA022D49D34199E05AB209869E4630C` | `10.0.0.73` | 2026-07-27T16:51:35 |
| `user` | `guest` | `193.32.162.34` | 2026-07-27T16:52:21 |
| `supervisor` | `supervisor2011` | `178.178.222.59` | 2026-07-27T16:52:54 |
| `support` | `555555` | `82.193.122.91` | 2026-07-27T16:53:18 |
| `support` | `555555` | `35.130.111.98` | 2026-07-27T16:53:25 |
| `test` | `test` | `193.32.162.34` | 2026-07-27T16:53:45 |
| `test` | `password` | `193.32.162.34` | 2026-07-27T16:55:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **307** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 65 |
| OpenSSH | 57 |
| libssh | 36 |
| Paramiko (Python) | 14 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 57 | 55 |
| `2ec37a7cc8da...` | Mirai/variant | 53 | 1 |
| `f555226df196...` | Mirai/variant | 16 | 7 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 57 | 55 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 53 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 16 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 50 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
Source IPs: `193.32.162.34`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
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
Source IPs: `164.92.140.160`, `14.103.115.117`, `92.205.177.212`, `157.10.182.14`, `14.103.115.213`, `189.204.230.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **143** |
| Unique ASNs | **92** |
| High-Risk ASNs | **72** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS4766` | Korea Telecom | 6 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS46562` | Performive LLC | 4 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (144)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-129d2cbc2256

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-27 13:05 |
| **Last Seen** | 2026-07-27 13:05 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:05:07` | `cowrie.session.connect` |
| `2026-07-27 13:05:07` | `cowrie.client.version` |
| `2026-07-27 13:05:07` | `cowrie.client.kex` |
| `2026-07-27 13:05:07` | `cowrie.login.success` |
| `2026-07-27 13:05:08` | `cowrie.session.params` |
| `2026-07-27 13:05:08` | `cowrie.command.input` |
| `2026-07-27 13:05:08` | `cowrie.command.failed` |
| `2026-07-27 13:05:08` | `cowrie.log.closed` |
| `2026-07-27 13:05:09` | `cowrie.session.params` |
| `2026-07-27 13:05:09` | `cowrie.command.input` |
| `2026-07-27 13:05:09` | `cowrie.session.file_download` |
| `2026-07-27 13:05:09` | `cowrie.log.closed` |
| `2026-07-27 13:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c194fb8a1fb3

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-27 13:05 |
| **Last Seen** | 2026-07-27 13:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:05:09` | `cowrie.session.connect` |
| `2026-07-27 13:05:09` | `cowrie.client.version` |
| `2026-07-27 13:05:09` | `cowrie.client.kex` |
| `2026-07-27 13:05:15` | `cowrie.login.success` |
| `2026-07-27 13:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dda18af4041

| Field | Detail |
|---|---|
| **Source IP** | `189.204.230[.]91` |
| **First Seen** | 2026-07-27 13:05 |
| **Last Seen** | 2026-07-27 13:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:05:16` | `cowrie.session.connect` |
| `2026-07-27 13:05:16` | `cowrie.client.version` |
| `2026-07-27 13:05:16` | `cowrie.client.kex` |
| `2026-07-27 13:05:23` | `cowrie.login.success` |
| `2026-07-27 13:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.204.230[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.204.230[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e42421a138

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-07-27 13:08 |
| **Last Seen** | 2026-07-27 13:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:08:31` | `cowrie.session.connect` |
| `2026-07-27 13:08:32` | `cowrie.client.version` |
| `2026-07-27 13:08:32` | `cowrie.client.kex` |
| `2026-07-27 13:08:33` | `cowrie.login.success` |
| `2026-07-27 13:08:33` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e098c65495

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-07-27 13:08 |
| **Last Seen** | 2026-07-27 13:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:08:43` | `cowrie.session.connect` |
| `2026-07-27 13:08:43` | `cowrie.client.version` |
| `2026-07-27 13:08:43` | `cowrie.client.kex` |
| `2026-07-27 13:08:45` | `cowrie.login.success` |
| `2026-07-27 13:08:46` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f229b4ff18c9

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-27 13:11 |
| **Last Seen** | 2026-07-27 13:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:11:13` | `cowrie.session.connect` |
| `2026-07-27 13:11:14` | `cowrie.client.version` |
| `2026-07-27 13:11:14` | `cowrie.client.kex` |
| `2026-07-27 13:11:15` | `cowrie.login.success` |
| `2026-07-27 13:11:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff54479cdb2

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-27 13:15 |
| **Last Seen** | 2026-07-27 13:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:15:33` | `cowrie.session.connect` |
| `2026-07-27 13:15:33` | `cowrie.client.version` |
| `2026-07-27 13:15:33` | `cowrie.client.kex` |
| `2026-07-27 13:15:34` | `cowrie.login.success` |
| `2026-07-27 13:15:35` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa38b5dbca84

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-07-27 13:18 |
| **Last Seen** | 2026-07-27 13:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:18:49` | `cowrie.session.connect` |
| `2026-07-27 13:18:50` | `cowrie.client.version` |
| `2026-07-27 13:18:50` | `cowrie.client.kex` |
| `2026-07-27 13:18:52` | `cowrie.login.success` |
| `2026-07-27 13:18:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5e5009983d

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-07-27 13:18 |
| **Last Seen** | 2026-07-27 13:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:18:58` | `cowrie.session.connect` |
| `2026-07-27 13:18:59` | `cowrie.client.version` |
| `2026-07-27 13:18:59` | `cowrie.client.kex` |
| `2026-07-27 13:19:01` | `cowrie.login.success` |
| `2026-07-27 13:19:02` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af57ed684e4

| Field | Detail |
|---|---|
| **Source IP** | `115.191.23[.]138` |
| **First Seen** | 2026-07-27 13:20 |
| **Last Seen** | 2026-07-27 13:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:20:22` | `cowrie.session.connect` |
| `2026-07-27 13:20:22` | `cowrie.client.version` |
| `2026-07-27 13:20:22` | `cowrie.client.kex` |
| `2026-07-27 13:20:23` | `cowrie.login.success` |
| `2026-07-27 13:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.23[.]138` to AbuseIPDB if not already reported
- [ ] Block `115.191.23[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adafb8ec6f39

| Field | Detail |
|---|---|
| **Source IP** | `157.10.182[.]14` |
| **First Seen** | 2026-07-27 13:24 |
| **Last Seen** | 2026-07-27 13:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:24:50` | `cowrie.session.connect` |
| `2026-07-27 13:24:50` | `cowrie.client.version` |
| `2026-07-27 13:24:50` | `cowrie.client.kex` |
| `2026-07-27 13:24:51` | `cowrie.login.success` |
| `2026-07-27 13:24:52` | `cowrie.session.params` |
| `2026-07-27 13:24:52` | `cowrie.command.input` |
| `2026-07-27 13:24:52` | `cowrie.command.failed` |
| `2026-07-27 13:24:53` | `cowrie.log.closed` |
| `2026-07-27 13:24:53` | `cowrie.session.params` |
| `2026-07-27 13:24:53` | `cowrie.command.input` |
| `2026-07-27 13:24:54` | `cowrie.session.file_download` |
| `2026-07-27 13:24:54` | `cowrie.log.closed` |
| `2026-07-27 13:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.182[.]14` to AbuseIPDB if not already reported
- [ ] Block `157.10.182[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e706eab48d13

| Field | Detail |
|---|---|
| **Source IP** | `157.10.182[.]14` |
| **First Seen** | 2026-07-27 13:24 |
| **Last Seen** | 2026-07-27 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:24:54` | `cowrie.session.connect` |
| `2026-07-27 13:24:54` | `cowrie.client.version` |
| `2026-07-27 13:24:54` | `cowrie.client.kex` |
| `2026-07-27 13:24:55` | `cowrie.login.success` |
| `2026-07-27 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.182[.]14` to AbuseIPDB if not already reported
- [ ] Block `157.10.182[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d619dcb14a92

| Field | Detail |
|---|---|
| **Source IP** | `157.10.182[.]14` |
| **First Seen** | 2026-07-27 13:24 |
| **Last Seen** | 2026-07-27 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:24:56` | `cowrie.session.connect` |
| `2026-07-27 13:24:56` | `cowrie.client.version` |
| `2026-07-27 13:24:56` | `cowrie.client.kex` |
| `2026-07-27 13:24:57` | `cowrie.login.success` |
| `2026-07-27 13:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.182[.]14` to AbuseIPDB if not already reported
- [ ] Block `157.10.182[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521b15637031

| Field | Detail |
|---|---|
| **Source IP** | `164.92.140[.]160` |
| **First Seen** | 2026-07-27 13:35 |
| **Last Seen** | 2026-07-27 13:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:35:32` | `cowrie.session.connect` |
| `2026-07-27 13:35:32` | `cowrie.client.version` |
| `2026-07-27 13:35:32` | `cowrie.client.kex` |
| `2026-07-27 13:35:33` | `cowrie.login.success` |
| `2026-07-27 13:35:33` | `cowrie.session.params` |
| `2026-07-27 13:35:33` | `cowrie.command.input` |
| `2026-07-27 13:35:33` | `cowrie.command.failed` |
| `2026-07-27 13:35:34` | `cowrie.log.closed` |
| `2026-07-27 13:35:34` | `cowrie.session.params` |
| `2026-07-27 13:35:34` | `cowrie.command.input` |
| `2026-07-27 13:35:35` | `cowrie.session.file_download` |
| `2026-07-27 13:35:35` | `cowrie.log.closed` |
| `2026-07-27 13:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.140[.]160` to AbuseIPDB if not already reported
- [ ] Block `164.92.140[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11a4f447d24

| Field | Detail |
|---|---|
| **Source IP** | `164.92.140[.]160` |
| **First Seen** | 2026-07-27 13:35 |
| **Last Seen** | 2026-07-27 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:35:35` | `cowrie.session.connect` |
| `2026-07-27 13:35:35` | `cowrie.client.version` |
| `2026-07-27 13:35:35` | `cowrie.client.kex` |
| `2026-07-27 13:35:35` | `cowrie.login.success` |
| `2026-07-27 13:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.140[.]160` to AbuseIPDB if not already reported
- [ ] Block `164.92.140[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474dc81da94e

| Field | Detail |
|---|---|
| **Source IP** | `164.92.140[.]160` |
| **First Seen** | 2026-07-27 13:35 |
| **Last Seen** | 2026-07-27 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:35:35` | `cowrie.session.connect` |
| `2026-07-27 13:35:35` | `cowrie.client.version` |
| `2026-07-27 13:35:35` | `cowrie.client.kex` |
| `2026-07-27 13:35:36` | `cowrie.login.success` |
| `2026-07-27 13:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.140[.]160` to AbuseIPDB if not already reported
- [ ] Block `164.92.140[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f2e3c2252a

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-07-27 13:35 |
| **Last Seen** | 2026-07-27 13:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:35:49` | `cowrie.session.connect` |
| `2026-07-27 13:35:50` | `cowrie.client.version` |
| `2026-07-27 13:35:50` | `cowrie.client.kex` |
| `2026-07-27 13:35:52` | `cowrie.login.success` |
| `2026-07-27 13:35:53` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:35:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd169fa14b6

| Field | Detail |
|---|---|
| **Source IP** | `76.132.238[.]43` |
| **First Seen** | 2026-07-27 13:36 |
| **Last Seen** | 2026-07-27 13:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:36:33` | `cowrie.session.connect` |
| `2026-07-27 13:36:33` | `cowrie.client.version` |
| `2026-07-27 13:36:33` | `cowrie.client.kex` |
| `2026-07-27 13:36:34` | `cowrie.login.success` |
| `2026-07-27 13:36:35` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.132.238[.]43` to AbuseIPDB if not already reported
- [ ] Block `76.132.238[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1f5e3c7851

| Field | Detail |
|---|---|
| **Source IP** | `14.153.226[.]88` |
| **First Seen** | 2026-07-27 13:36 |
| **Last Seen** | 2026-07-27 13:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:36:44` | `cowrie.session.connect` |
| `2026-07-27 13:36:45` | `cowrie.client.version` |
| `2026-07-27 13:36:45` | `cowrie.client.kex` |
| `2026-07-27 13:36:47` | `cowrie.login.success` |
| `2026-07-27 13:36:48` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.226[.]88` to AbuseIPDB if not already reported
- [ ] Block `14.153.226[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99fbe0dc440f

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-27 13:40 |
| **Last Seen** | 2026-07-27 13:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:40:14` | `cowrie.session.connect` |
| `2026-07-27 13:40:15` | `cowrie.client.version` |
| `2026-07-27 13:40:15` | `cowrie.client.kex` |
| `2026-07-27 13:40:17` | `cowrie.login.success` |
| `2026-07-27 13:40:17` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd8c27d641c

| Field | Detail |
|---|---|
| **Source IP** | `92.205.177[.]212` |
| **First Seen** | 2026-07-27 13:45 |
| **Last Seen** | 2026-07-27 13:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:45:43` | `cowrie.session.connect` |
| `2026-07-27 13:45:43` | `cowrie.client.version` |
| `2026-07-27 13:45:43` | `cowrie.client.kex` |
| `2026-07-27 13:45:43` | `cowrie.login.success` |
| `2026-07-27 13:45:44` | `cowrie.session.params` |
| `2026-07-27 13:45:44` | `cowrie.command.input` |
| `2026-07-27 13:45:44` | `cowrie.command.failed` |
| `2026-07-27 13:45:44` | `cowrie.log.closed` |
| `2026-07-27 13:45:45` | `cowrie.session.params` |
| `2026-07-27 13:45:45` | `cowrie.command.input` |
| `2026-07-27 13:45:45` | `cowrie.session.file_download` |
| `2026-07-27 13:45:45` | `cowrie.log.closed` |
| `2026-07-27 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.177[.]212` to AbuseIPDB if not already reported
- [ ] Block `92.205.177[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221cf6d87693

| Field | Detail |
|---|---|
| **Source IP** | `92.205.177[.]212` |
| **First Seen** | 2026-07-27 13:45 |
| **Last Seen** | 2026-07-27 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:45:45` | `cowrie.session.connect` |
| `2026-07-27 13:45:45` | `cowrie.client.version` |
| `2026-07-27 13:45:45` | `cowrie.client.kex` |
| `2026-07-27 13:45:46` | `cowrie.login.success` |
| `2026-07-27 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.177[.]212` to AbuseIPDB if not already reported
- [ ] Block `92.205.177[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0720bdf4094

| Field | Detail |
|---|---|
| **Source IP** | `92.205.177[.]212` |
| **First Seen** | 2026-07-27 13:45 |
| **Last Seen** | 2026-07-27 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:45:46` | `cowrie.session.connect` |
| `2026-07-27 13:45:46` | `cowrie.client.version` |
| `2026-07-27 13:45:46` | `cowrie.client.kex` |
| `2026-07-27 13:45:46` | `cowrie.login.success` |
| `2026-07-27 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.177[.]212` to AbuseIPDB if not already reported
- [ ] Block `92.205.177[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a86244e6dce0

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-27 13:57 |
| **Last Seen** | 2026-07-27 14:02 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:57:14` | `cowrie.session.connect` |
| `2026-07-27 13:57:14` | `cowrie.client.version` |
| `2026-07-27 13:57:14` | `cowrie.client.kex` |
| `2026-07-27 13:57:16` | `cowrie.login.success` |
| `2026-07-27 13:57:16` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7c0f3856a5

| Field | Detail |
|---|---|
| **Source IP** | `175.43.184[.]200` |
| **First Seen** | 2026-07-27 13:57 |
| **Last Seen** | 2026-07-27 13:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:57:53` | `cowrie.session.connect` |
| `2026-07-27 13:57:54` | `cowrie.client.version` |
| `2026-07-27 13:57:54` | `cowrie.client.kex` |
| `2026-07-27 13:57:56` | `cowrie.login.success` |
| `2026-07-27 13:57:56` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.184[.]200` to AbuseIPDB if not already reported
- [ ] Block `175.43.184[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16364a768e25

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-07-27 13:58 |
| **Last Seen** | 2026-07-27 13:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 13:58:06` | `cowrie.session.connect` |
| `2026-07-27 13:58:06` | `cowrie.client.version` |
| `2026-07-27 13:58:06` | `cowrie.client.kex` |
| `2026-07-27 13:58:08` | `cowrie.login.success` |
| `2026-07-27 13:58:08` | `cowrie.direct-tcpip.request` |
| `2026-07-27 13:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76fadfa48f6e

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-07-27 14:00 |
| **Last Seen** | 2026-07-27 14:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:00:36` | `cowrie.session.connect` |
| `2026-07-27 14:00:37` | `cowrie.client.version` |
| `2026-07-27 14:00:37` | `cowrie.client.kex` |
| `2026-07-27 14:00:39` | `cowrie.login.success` |
| `2026-07-27 14:00:40` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305c7c759fef

| Field | Detail |
|---|---|
| **Source IP** | `117.226.48[.]35` |
| **First Seen** | 2026-07-27 14:01 |
| **Last Seen** | 2026-07-27 14:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:01:24` | `cowrie.session.connect` |
| `2026-07-27 14:01:24` | `cowrie.client.version` |
| `2026-07-27 14:01:25` | `cowrie.client.kex` |
| `2026-07-27 14:01:27` | `cowrie.login.success` |
| `2026-07-27 14:01:28` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.226.48[.]35` to AbuseIPDB if not already reported
- [ ] Block `117.226.48[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c18e52a2fcd

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-07-27 14:01 |
| **Last Seen** | 2026-07-27 14:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:01:34` | `cowrie.session.connect` |
| `2026-07-27 14:01:35` | `cowrie.client.version` |
| `2026-07-27 14:01:35` | `cowrie.client.kex` |
| `2026-07-27 14:01:39` | `cowrie.login.success` |
| `2026-07-27 14:01:40` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639809cf7d72

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-07-27 14:04 |
| **Last Seen** | 2026-07-27 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:04:55` | `cowrie.session.connect` |
| `2026-07-27 14:04:55` | `cowrie.client.version` |
| `2026-07-27 14:04:55` | `cowrie.client.kex` |
| `2026-07-27 14:04:56` | `cowrie.login.success` |
| `2026-07-27 14:04:57` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461e06b8e6fc

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-27 14:05 |
| **Last Seen** | 2026-07-27 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:05:06` | `cowrie.session.connect` |
| `2026-07-27 14:05:07` | `cowrie.client.version` |
| `2026-07-27 14:05:07` | `cowrie.client.kex` |
| `2026-07-27 14:05:08` | `cowrie.login.success` |
| `2026-07-27 14:05:08` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c198732f018

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-07-27 14:08 |
| **Last Seen** | 2026-07-27 14:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:08:12` | `cowrie.session.connect` |
| `2026-07-27 14:08:12` | `cowrie.client.version` |
| `2026-07-27 14:08:12` | `cowrie.client.kex` |
| `2026-07-27 14:08:13` | `cowrie.login.success` |
| `2026-07-27 14:08:13` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c069e5b0fd

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-27 14:08 |
| **Last Seen** | 2026-07-27 14:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:08:23` | `cowrie.session.connect` |
| `2026-07-27 14:08:23` | `cowrie.client.version` |
| `2026-07-27 14:08:23` | `cowrie.client.kex` |
| `2026-07-27 14:08:25` | `cowrie.login.success` |
| `2026-07-27 14:08:26` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76178aa7663

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 14:16 |
| **Last Seen** | 2026-07-27 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:16:28` | `cowrie.session.connect` |
| `2026-07-27 14:16:28` | `cowrie.client.version` |
| `2026-07-27 14:16:28` | `cowrie.client.kex` |
| `2026-07-27 14:16:29` | `cowrie.login.success` |
| `2026-07-27 14:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa4b396a0dd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 14:16 |
| **Last Seen** | 2026-07-27 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:16:30` | `cowrie.session.connect` |
| `2026-07-27 14:16:30` | `cowrie.client.version` |
| `2026-07-27 14:16:30` | `cowrie.client.kex` |
| `2026-07-27 14:16:31` | `cowrie.login.success` |
| `2026-07-27 14:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0e3a4e0327

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 14:16 |
| **Last Seen** | 2026-07-27 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:16:37` | `cowrie.session.connect` |
| `2026-07-27 14:16:37` | `cowrie.client.version` |
| `2026-07-27 14:16:37` | `cowrie.client.kex` |
| `2026-07-27 14:16:37` | `cowrie.login.success` |
| `2026-07-27 14:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f0dd871ca5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 14:16 |
| **Last Seen** | 2026-07-27 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:16:38` | `cowrie.session.connect` |
| `2026-07-27 14:16:38` | `cowrie.client.version` |
| `2026-07-27 14:16:38` | `cowrie.client.kex` |
| `2026-07-27 14:16:38` | `cowrie.login.success` |
| `2026-07-27 14:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51df573f877

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-07-27 14:25 |
| **Last Seen** | 2026-07-27 14:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:25:07` | `cowrie.session.connect` |
| `2026-07-27 14:25:08` | `cowrie.client.version` |
| `2026-07-27 14:25:08` | `cowrie.client.kex` |
| `2026-07-27 14:25:09` | `cowrie.login.success` |
| `2026-07-27 14:25:10` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc790ba4234d

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-07-27 14:29 |
| **Last Seen** | 2026-07-27 14:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:29:29` | `cowrie.session.connect` |
| `2026-07-27 14:29:30` | `cowrie.client.version` |
| `2026-07-27 14:29:30` | `cowrie.client.kex` |
| `2026-07-27 14:29:32` | `cowrie.login.success` |
| `2026-07-27 14:29:33` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433d7d1552f3

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-27 14:29 |
| **Last Seen** | 2026-07-27 14:29 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:29:43` | `cowrie.session.connect` |
| `2026-07-27 14:29:44` | `cowrie.client.version` |
| `2026-07-27 14:29:44` | `cowrie.client.kex` |
| `2026-07-27 14:29:49` | `cowrie.login.success` |
| `2026-07-27 14:29:50` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da8efa07c1a

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-07-27 14:33 |
| **Last Seen** | 2026-07-27 14:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:33:03` | `cowrie.session.connect` |
| `2026-07-27 14:33:04` | `cowrie.client.version` |
| `2026-07-27 14:33:04` | `cowrie.client.kex` |
| `2026-07-27 14:33:06` | `cowrie.login.success` |
| `2026-07-27 14:33:07` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2aba96dae27

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-27 14:43 |
| **Last Seen** | 2026-07-27 14:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:43:34` | `cowrie.session.connect` |
| `2026-07-27 14:43:35` | `cowrie.login.success` |
| `2026-07-27 14:43:36` | `cowrie.session.params` |
| `2026-07-27 14:43:36` | `cowrie.command.input` |
| `2026-07-27 14:43:36` | `cowrie.command.input` |
| `2026-07-27 14:43:37` | `cowrie.command.input` |
| `2026-07-27 14:43:38` | `cowrie.command.input` |
| `2026-07-27 14:43:38` | `cowrie.command.failed` |
| `2026-07-27 14:43:39` | `cowrie.log.closed` |
| `2026-07-27 14:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d434c68386

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]76` |
| **First Seen** | 2026-07-27 14:45 |
| **Last Seen** | 2026-07-27 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:45:41` | `cowrie.session.connect` |
| `2026-07-27 14:45:41` | `cowrie.client.version` |
| `2026-07-27 14:45:42` | `cowrie.client.kex` |
| `2026-07-27 14:45:42` | `cowrie.login.success` |
| `2026-07-27 14:45:42` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:45:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-27 14:45:42` | `cowrie.direct-tcpip.data` |
| `2026-07-27 14:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]76` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb289e2d7fff

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-07-27 14:46 |
| **Last Seen** | 2026-07-27 14:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:46:28` | `cowrie.session.connect` |
| `2026-07-27 14:46:29` | `cowrie.client.version` |
| `2026-07-27 14:46:29` | `cowrie.client.kex` |
| `2026-07-27 14:46:31` | `cowrie.login.success` |
| `2026-07-27 14:46:31` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6696fc5125

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-27 14:46 |
| **Last Seen** | 2026-07-27 14:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:46:41` | `cowrie.session.connect` |
| `2026-07-27 14:46:42` | `cowrie.client.version` |
| `2026-07-27 14:46:42` | `cowrie.client.kex` |
| `2026-07-27 14:46:44` | `cowrie.login.success` |
| `2026-07-27 14:46:45` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c3e4f5b97c

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-07-27 14:47 |
| **Last Seen** | 2026-07-27 14:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:47:08` | `cowrie.session.connect` |
| `2026-07-27 14:47:08` | `cowrie.client.version` |
| `2026-07-27 14:47:08` | `cowrie.client.kex` |
| `2026-07-27 14:47:09` | `cowrie.login.success` |
| `2026-07-27 14:47:10` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b933da2ca29

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-27 14:47 |
| **Last Seen** | 2026-07-27 14:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:47:19` | `cowrie.session.connect` |
| `2026-07-27 14:47:19` | `cowrie.client.version` |
| `2026-07-27 14:47:19` | `cowrie.client.kex` |
| `2026-07-27 14:47:20` | `cowrie.login.success` |
| `2026-07-27 14:47:20` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f773a39014

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-27 14:49 |
| **Last Seen** | 2026-07-27 14:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:49:51` | `cowrie.session.connect` |
| `2026-07-27 14:49:52` | `cowrie.client.version` |
| `2026-07-27 14:49:52` | `cowrie.client.kex` |
| `2026-07-27 14:49:54` | `cowrie.login.success` |
| `2026-07-27 14:49:54` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb54c2df4d85

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 14:53 |
| **Last Seen** | 2026-07-27 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:53:40` | `cowrie.session.connect` |
| `2026-07-27 14:53:40` | `cowrie.client.version` |
| `2026-07-27 14:53:40` | `cowrie.client.kex` |
| `2026-07-27 14:53:40` | `cowrie.login.success` |
| `2026-07-27 14:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9cf9b31ec8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 14:53 |
| **Last Seen** | 2026-07-27 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:53:40` | `cowrie.session.connect` |
| `2026-07-27 14:53:40` | `cowrie.client.version` |
| `2026-07-27 14:53:40` | `cowrie.client.kex` |
| `2026-07-27 14:53:40` | `cowrie.login.success` |
| `2026-07-27 14:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ec4b2b06e2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 14:53 |
| **Last Seen** | 2026-07-27 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:53:43` | `cowrie.session.connect` |
| `2026-07-27 14:53:43` | `cowrie.client.version` |
| `2026-07-27 14:53:43` | `cowrie.client.kex` |
| `2026-07-27 14:53:43` | `cowrie.login.success` |
| `2026-07-27 14:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a7cb9e37c9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-27 14:53 |
| **Last Seen** | 2026-07-27 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:53:43` | `cowrie.session.connect` |
| `2026-07-27 14:53:43` | `cowrie.client.version` |
| `2026-07-27 14:53:43` | `cowrie.client.kex` |
| `2026-07-27 14:53:44` | `cowrie.login.success` |
| `2026-07-27 14:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70f7b4633d4c

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-27 14:54 |
| **Last Seen** | 2026-07-27 14:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 14:54:18` | `cowrie.session.connect` |
| `2026-07-27 14:54:19` | `cowrie.client.version` |
| `2026-07-27 14:54:19` | `cowrie.client.kex` |
| `2026-07-27 14:54:21` | `cowrie.login.success` |
| `2026-07-27 14:54:22` | `cowrie.direct-tcpip.request` |
| `2026-07-27 14:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c1319de8f0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]93` |
| **First Seen** | 2026-07-27 15:07 |
| **Last Seen** | 2026-07-27 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_OK` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:07:32` | `cowrie.session.connect` |
| `2026-07-27 15:07:32` | `cowrie.login.success` |
| `2026-07-27 15:07:33` | `cowrie.session.params` |
| `2026-07-27 15:07:33` | `cowrie.command.input` |
| `2026-07-27 15:07:34` | `cowrie.log.closed` |
| `2026-07-27 15:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]93` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0128f9d2d0

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-07-27 15:11 |
| **Last Seen** | 2026-07-27 15:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:11:53` | `cowrie.session.connect` |
| `2026-07-27 15:11:54` | `cowrie.client.version` |
| `2026-07-27 15:11:54` | `cowrie.client.kex` |
| `2026-07-27 15:11:55` | `cowrie.login.success` |
| `2026-07-27 15:11:55` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb395690bfb

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-07-27 15:14 |
| **Last Seen** | 2026-07-27 15:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:14:29` | `cowrie.session.connect` |
| `2026-07-27 15:14:29` | `cowrie.client.version` |
| `2026-07-27 15:14:29` | `cowrie.client.kex` |
| `2026-07-27 15:14:32` | `cowrie.login.success` |
| `2026-07-27 15:14:32` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80725e6d1e8d

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-07-27 15:18 |
| **Last Seen** | 2026-07-27 15:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:18:53` | `cowrie.session.connect` |
| `2026-07-27 15:18:54` | `cowrie.client.version` |
| `2026-07-27 15:18:54` | `cowrie.client.kex` |
| `2026-07-27 15:18:57` | `cowrie.login.success` |
| `2026-07-27 15:18:57` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e62728a0ff

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-27 15:19 |
| **Last Seen** | 2026-07-27 15:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:19:03` | `cowrie.session.connect` |
| `2026-07-27 15:19:04` | `cowrie.client.version` |
| `2026-07-27 15:19:04` | `cowrie.client.kex` |
| `2026-07-27 15:19:04` | `cowrie.login.success` |
| `2026-07-27 15:19:05` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07408aaf0b13

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-27 15:39 |
| **Last Seen** | 2026-07-27 15:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:39:44` | `cowrie.session.connect` |
| `2026-07-27 15:39:44` | `cowrie.client.version` |
| `2026-07-27 15:39:44` | `cowrie.client.kex` |
| `2026-07-27 15:39:45` | `cowrie.login.success` |
| `2026-07-27 15:39:46` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb25e2b25f9c

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-27 15:39 |
| **Last Seen** | 2026-07-27 15:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:39:51` | `cowrie.session.connect` |
| `2026-07-27 15:39:52` | `cowrie.client.version` |
| `2026-07-27 15:39:52` | `cowrie.client.kex` |
| `2026-07-27 15:39:54` | `cowrie.login.success` |
| `2026-07-27 15:39:55` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f591bd261cba

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-07-27 15:43 |
| **Last Seen** | 2026-07-27 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:43:51` | `cowrie.session.connect` |
| `2026-07-27 15:43:52` | `cowrie.client.version` |
| `2026-07-27 15:43:52` | `cowrie.client.kex` |
| `2026-07-27 15:43:55` | `cowrie.login.success` |
| `2026-07-27 15:43:55` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d34c2e85b3

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-27 15:47 |
| **Last Seen** | 2026-07-27 15:47 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:47:03` | `cowrie.session.connect` |
| `2026-07-27 15:47:05` | `cowrie.client.version` |
| `2026-07-27 15:47:05` | `cowrie.client.kex` |
| `2026-07-27 15:47:10` | `cowrie.login.success` |
| `2026-07-27 15:47:11` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ad839eecbe

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-27 15:47 |
| **Last Seen** | 2026-07-27 15:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:47:16` | `cowrie.session.connect` |
| `2026-07-27 15:47:17` | `cowrie.client.version` |
| `2026-07-27 15:47:17` | `cowrie.client.kex` |
| `2026-07-27 15:47:20` | `cowrie.login.success` |
| `2026-07-27 15:47:20` | `cowrie.direct-tcpip.request` |
| `2026-07-27 15:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ddb71b25faa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 15:54 |
| **Last Seen** | 2026-07-27 15:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:54:57` | `cowrie.session.connect` |
| `2026-07-27 15:54:57` | `cowrie.client.version` |
| `2026-07-27 15:54:57` | `cowrie.client.kex` |
| `2026-07-27 15:54:59` | `cowrie.login.success` |
| `2026-07-27 15:55:01` | `cowrie.session.params` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.success` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:01` | `cowrie.command.input` |
| `2026-07-27 15:55:02` | `cowrie.log.closed` |
| `2026-07-27 15:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9d84d14cc8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 15:56 |
| **Last Seen** | 2026-07-27 15:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:56:09` | `cowrie.session.connect` |
| `2026-07-27 15:56:10` | `cowrie.client.version` |
| `2026-07-27 15:56:10` | `cowrie.client.kex` |
| `2026-07-27 15:56:12` | `cowrie.login.success` |
| `2026-07-27 15:56:14` | `cowrie.session.params` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.success` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:14` | `cowrie.command.input` |
| `2026-07-27 15:56:15` | `cowrie.log.closed` |
| `2026-07-27 15:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4befbe9c5969

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 15:58 |
| **Last Seen** | 2026-07-27 15:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:58:32` | `cowrie.session.connect` |
| `2026-07-27 15:58:33` | `cowrie.client.version` |
| `2026-07-27 15:58:33` | `cowrie.client.kex` |
| `2026-07-27 15:58:35` | `cowrie.login.success` |
| `2026-07-27 15:58:37` | `cowrie.session.params` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.success` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:37` | `cowrie.command.input` |
| `2026-07-27 15:58:38` | `cowrie.log.closed` |
| `2026-07-27 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecb6a5ea7eb9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 15:59 |
| **Last Seen** | 2026-07-27 15:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 15:59:42` | `cowrie.session.connect` |
| `2026-07-27 15:59:43` | `cowrie.client.version` |
| `2026-07-27 15:59:43` | `cowrie.client.kex` |
| `2026-07-27 15:59:45` | `cowrie.login.success` |
| `2026-07-27 15:59:47` | `cowrie.session.params` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.success` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.command.input` |
| `2026-07-27 15:59:47` | `cowrie.log.closed` |
| `2026-07-27 15:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6731f3fceb

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-07-27 16:00 |
| **Last Seen** | 2026-07-27 16:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:00:25` | `cowrie.session.connect` |
| `2026-07-27 16:00:26` | `cowrie.client.version` |
| `2026-07-27 16:00:26` | `cowrie.client.kex` |
| `2026-07-27 16:00:27` | `cowrie.login.success` |
| `2026-07-27 16:00:27` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac34e21e38f0

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-07-27 16:00 |
| **Last Seen** | 2026-07-27 16:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:00:32` | `cowrie.session.connect` |
| `2026-07-27 16:00:33` | `cowrie.client.version` |
| `2026-07-27 16:00:33` | `cowrie.client.kex` |
| `2026-07-27 16:00:35` | `cowrie.login.success` |
| `2026-07-27 16:00:36` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92939185cfd2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:00 |
| **Last Seen** | 2026-07-27 16:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:00:51` | `cowrie.session.connect` |
| `2026-07-27 16:00:51` | `cowrie.client.version` |
| `2026-07-27 16:00:51` | `cowrie.client.kex` |
| `2026-07-27 16:00:53` | `cowrie.login.success` |
| `2026-07-27 16:00:54` | `cowrie.session.params` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.success` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:54` | `cowrie.command.input` |
| `2026-07-27 16:00:55` | `cowrie.log.closed` |
| `2026-07-27 16:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566396f486ed

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-07-27 16:01 |
| **Last Seen** | 2026-07-27 16:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:01:00` | `cowrie.session.connect` |
| `2026-07-27 16:01:01` | `cowrie.client.version` |
| `2026-07-27 16:01:01` | `cowrie.client.kex` |
| `2026-07-27 16:01:03` | `cowrie.login.success` |
| `2026-07-27 16:01:05` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-843902a8c137

| Field | Detail |
|---|---|
| **Source IP** | `60.172.41[.]103` |
| **First Seen** | 2026-07-27 16:01 |
| **Last Seen** | 2026-07-27 16:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:01:14` | `cowrie.session.connect` |
| `2026-07-27 16:01:16` | `cowrie.client.version` |
| `2026-07-27 16:01:16` | `cowrie.client.kex` |
| `2026-07-27 16:01:18` | `cowrie.login.success` |
| `2026-07-27 16:01:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.41[.]103` to AbuseIPDB if not already reported
- [ ] Block `60.172.41[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65541eb56aab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:01 |
| **Last Seen** | 2026-07-27 16:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:01:59` | `cowrie.session.connect` |
| `2026-07-27 16:01:59` | `cowrie.client.version` |
| `2026-07-27 16:01:59` | `cowrie.client.kex` |
| `2026-07-27 16:02:01` | `cowrie.login.success` |
| `2026-07-27 16:02:03` | `cowrie.session.params` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.success` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:03` | `cowrie.command.input` |
| `2026-07-27 16:02:04` | `cowrie.log.closed` |
| `2026-07-27 16:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31de0efe5991

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:03 |
| **Last Seen** | 2026-07-27 16:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:03:09` | `cowrie.session.connect` |
| `2026-07-27 16:03:09` | `cowrie.client.version` |
| `2026-07-27 16:03:09` | `cowrie.client.kex` |
| `2026-07-27 16:03:11` | `cowrie.login.success` |
| `2026-07-27 16:03:13` | `cowrie.session.params` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.success` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:13` | `cowrie.command.input` |
| `2026-07-27 16:03:14` | `cowrie.log.closed` |
| `2026-07-27 16:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e994e22386f4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:04 |
| **Last Seen** | 2026-07-27 16:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:04:15` | `cowrie.session.connect` |
| `2026-07-27 16:04:15` | `cowrie.client.version` |
| `2026-07-27 16:04:15` | `cowrie.client.kex` |
| `2026-07-27 16:04:16` | `cowrie.login.success` |
| `2026-07-27 16:04:18` | `cowrie.session.params` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.success` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.command.input` |
| `2026-07-27 16:04:18` | `cowrie.log.closed` |
| `2026-07-27 16:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ac972dceae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-27 16:04 |
| **Last Seen** | 2026-07-27 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:04:30` | `cowrie.session.connect` |
| `2026-07-27 16:04:30` | `cowrie.client.version` |
| `2026-07-27 16:04:30` | `cowrie.client.kex` |
| `2026-07-27 16:04:30` | `cowrie.login.success` |
| `2026-07-27 16:04:30` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:04:30` | `cowrie.direct-tcpip.data` |
| `2026-07-27 16:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02995b42979d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:05 |
| **Last Seen** | 2026-07-27 16:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:05:16` | `cowrie.session.connect` |
| `2026-07-27 16:05:17` | `cowrie.client.version` |
| `2026-07-27 16:05:17` | `cowrie.client.kex` |
| `2026-07-27 16:05:18` | `cowrie.login.success` |
| `2026-07-27 16:05:19` | `cowrie.session.params` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.success` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.command.input` |
| `2026-07-27 16:05:19` | `cowrie.log.closed` |
| `2026-07-27 16:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3474957bdbb6

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]213` |
| **First Seen** | 2026-07-27 16:05 |
| **Last Seen** | 2026-07-27 16:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:05:21` | `cowrie.session.connect` |
| `2026-07-27 16:05:21` | `cowrie.client.version` |
| `2026-07-27 16:05:22` | `cowrie.client.kex` |
| `2026-07-27 16:05:23` | `cowrie.login.success` |
| `2026-07-27 16:05:24` | `cowrie.session.params` |
| `2026-07-27 16:05:24` | `cowrie.command.input` |
| `2026-07-27 16:05:24` | `cowrie.command.failed` |
| `2026-07-27 16:05:24` | `cowrie.log.closed` |
| `2026-07-27 16:05:25` | `cowrie.session.params` |
| `2026-07-27 16:05:25` | `cowrie.command.input` |
| `2026-07-27 16:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]213` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3429ed4e273b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]213` |
| **First Seen** | 2026-07-27 16:05 |
| **Last Seen** | 2026-07-27 16:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:05:54` | `cowrie.session.connect` |
| `2026-07-27 16:05:54` | `cowrie.client.version` |
| `2026-07-27 16:05:54` | `cowrie.client.kex` |
| `2026-07-27 16:05:56` | `cowrie.login.success` |
| `2026-07-27 16:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]213` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236801954388

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:06 |
| **Last Seen** | 2026-07-27 16:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:06:19` | `cowrie.session.connect` |
| `2026-07-27 16:06:19` | `cowrie.client.version` |
| `2026-07-27 16:06:19` | `cowrie.client.kex` |
| `2026-07-27 16:06:20` | `cowrie.login.success` |
| `2026-07-27 16:06:21` | `cowrie.session.params` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.success` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:21` | `cowrie.command.input` |
| `2026-07-27 16:06:22` | `cowrie.log.closed` |
| `2026-07-27 16:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50b5214d498

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:07 |
| **Last Seen** | 2026-07-27 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:07:23` | `cowrie.session.connect` |
| `2026-07-27 16:07:24` | `cowrie.client.version` |
| `2026-07-27 16:07:24` | `cowrie.client.kex` |
| `2026-07-27 16:07:25` | `cowrie.login.success` |
| `2026-07-27 16:07:26` | `cowrie.session.params` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.success` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.command.input` |
| `2026-07-27 16:07:26` | `cowrie.log.closed` |
| `2026-07-27 16:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea660e4bf4d9

| Field | Detail |
|---|---|
| **Source IP** | `213.141.130[.]251` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:09` | `cowrie.session.connect` |
| `2026-07-27 16:08:12` | `cowrie.client.version` |
| `2026-07-27 16:08:12` | `cowrie.client.kex` |
| `2026-07-27 16:08:22` | `cowrie.login.success` |
| `2026-07-27 16:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.141.130[.]251` to AbuseIPDB if not already reported
- [ ] Block `213.141.130[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68931020b91c

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:27` | `cowrie.session.connect` |
| `2026-07-27 16:08:27` | `cowrie.client.version` |
| `2026-07-27 16:08:27` | `cowrie.client.kex` |
| `2026-07-27 16:08:27` | `cowrie.login.success` |
| `2026-07-27 16:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39e519f5274

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:29` | `cowrie.session.connect` |
| `2026-07-27 16:08:29` | `cowrie.client.version` |
| `2026-07-27 16:08:29` | `cowrie.client.kex` |
| `2026-07-27 16:08:30` | `cowrie.login.success` |
| `2026-07-27 16:08:31` | `cowrie.session.params` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.success` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.command.input` |
| `2026-07-27 16:08:31` | `cowrie.log.closed` |
| `2026-07-27 16:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8344b1fccb85

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]117` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:41` | `cowrie.session.connect` |
| `2026-07-27 16:08:41` | `cowrie.client.version` |
| `2026-07-27 16:08:42` | `cowrie.client.kex` |
| `2026-07-27 16:08:43` | `cowrie.login.success` |
| `2026-07-27 16:08:45` | `cowrie.session.params` |
| `2026-07-27 16:08:45` | `cowrie.command.input` |
| `2026-07-27 16:08:45` | `cowrie.command.failed` |
| `2026-07-27 16:08:45` | `cowrie.log.closed` |
| `2026-07-27 16:08:46` | `cowrie.session.params` |
| `2026-07-27 16:08:46` | `cowrie.command.input` |
| `2026-07-27 16:08:46` | `cowrie.session.file_download` |
| `2026-07-27 16:08:46` | `cowrie.log.closed` |
| `2026-07-27 16:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]117` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d64c9076d52

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]117` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:46` | `cowrie.session.connect` |
| `2026-07-27 16:08:46` | `cowrie.client.version` |
| `2026-07-27 16:08:47` | `cowrie.client.kex` |
| `2026-07-27 16:08:48` | `cowrie.login.success` |
| `2026-07-27 16:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]117` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257197c8c5c0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.115[.]117` |
| **First Seen** | 2026-07-27 16:08 |
| **Last Seen** | 2026-07-27 16:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:08:50` | `cowrie.session.connect` |
| `2026-07-27 16:08:50` | `cowrie.client.version` |
| `2026-07-27 16:08:50` | `cowrie.client.kex` |
| `2026-07-27 16:08:52` | `cowrie.login.success` |
| `2026-07-27 16:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.115[.]117` to AbuseIPDB if not already reported
- [ ] Block `14.103.115[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b6b4b3e437

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:09 |
| **Last Seen** | 2026-07-27 16:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:09:36` | `cowrie.session.connect` |
| `2026-07-27 16:09:36` | `cowrie.client.version` |
| `2026-07-27 16:09:37` | `cowrie.client.kex` |
| `2026-07-27 16:09:38` | `cowrie.login.success` |
| `2026-07-27 16:09:39` | `cowrie.session.params` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.success` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.command.input` |
| `2026-07-27 16:09:39` | `cowrie.log.closed` |
| `2026-07-27 16:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8017eab9bb3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:10 |
| **Last Seen** | 2026-07-27 16:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:10:45` | `cowrie.session.connect` |
| `2026-07-27 16:10:45` | `cowrie.client.version` |
| `2026-07-27 16:10:45` | `cowrie.client.kex` |
| `2026-07-27 16:10:46` | `cowrie.login.success` |
| `2026-07-27 16:10:47` | `cowrie.session.params` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.success` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.command.input` |
| `2026-07-27 16:10:47` | `cowrie.log.closed` |
| `2026-07-27 16:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2a4e1b75d9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:11 |
| **Last Seen** | 2026-07-27 16:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:11:55` | `cowrie.session.connect` |
| `2026-07-27 16:11:55` | `cowrie.client.version` |
| `2026-07-27 16:11:55` | `cowrie.client.kex` |
| `2026-07-27 16:11:56` | `cowrie.login.success` |
| `2026-07-27 16:11:57` | `cowrie.session.params` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.success` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.command.input` |
| `2026-07-27 16:11:57` | `cowrie.log.closed` |
| `2026-07-27 16:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcaf2c0600f2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:13 |
| **Last Seen** | 2026-07-27 16:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:13:03` | `cowrie.session.connect` |
| `2026-07-27 16:13:03` | `cowrie.client.version` |
| `2026-07-27 16:13:03` | `cowrie.client.kex` |
| `2026-07-27 16:13:04` | `cowrie.login.success` |
| `2026-07-27 16:13:05` | `cowrie.session.params` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.success` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.command.input` |
| `2026-07-27 16:13:05` | `cowrie.log.closed` |
| `2026-07-27 16:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c73b01b5bbb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:14 |
| **Last Seen** | 2026-07-27 16:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:14:09` | `cowrie.session.connect` |
| `2026-07-27 16:14:09` | `cowrie.client.version` |
| `2026-07-27 16:14:10` | `cowrie.client.kex` |
| `2026-07-27 16:14:10` | `cowrie.login.success` |
| `2026-07-27 16:14:11` | `cowrie.session.params` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.success` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:11` | `cowrie.command.input` |
| `2026-07-27 16:14:12` | `cowrie.log.closed` |
| `2026-07-27 16:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8edb2e4da38f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:15 |
| **Last Seen** | 2026-07-27 16:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:15:16` | `cowrie.session.connect` |
| `2026-07-27 16:15:16` | `cowrie.client.version` |
| `2026-07-27 16:15:17` | `cowrie.client.kex` |
| `2026-07-27 16:15:17` | `cowrie.login.success` |
| `2026-07-27 16:15:18` | `cowrie.session.params` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.success` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:18` | `cowrie.command.input` |
| `2026-07-27 16:15:19` | `cowrie.log.closed` |
| `2026-07-27 16:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b32be901a7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:16 |
| **Last Seen** | 2026-07-27 16:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:16:23` | `cowrie.session.connect` |
| `2026-07-27 16:16:23` | `cowrie.client.version` |
| `2026-07-27 16:16:24` | `cowrie.client.kex` |
| `2026-07-27 16:16:24` | `cowrie.login.success` |
| `2026-07-27 16:16:25` | `cowrie.session.params` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.success` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:25` | `cowrie.command.input` |
| `2026-07-27 16:16:26` | `cowrie.log.closed` |
| `2026-07-27 16:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c5a43e9993

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:17 |
| **Last Seen** | 2026-07-27 16:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:17:32` | `cowrie.session.connect` |
| `2026-07-27 16:17:32` | `cowrie.client.version` |
| `2026-07-27 16:17:32` | `cowrie.client.kex` |
| `2026-07-27 16:17:33` | `cowrie.login.success` |
| `2026-07-27 16:17:34` | `cowrie.session.params` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.success` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:34` | `cowrie.command.input` |
| `2026-07-27 16:17:35` | `cowrie.log.closed` |
| `2026-07-27 16:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a99d73a6580

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:18 |
| **Last Seen** | 2026-07-27 16:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:18:42` | `cowrie.session.connect` |
| `2026-07-27 16:18:42` | `cowrie.client.version` |
| `2026-07-27 16:18:42` | `cowrie.client.kex` |
| `2026-07-27 16:18:43` | `cowrie.login.success` |
| `2026-07-27 16:18:44` | `cowrie.session.params` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.success` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:44` | `cowrie.command.input` |
| `2026-07-27 16:18:45` | `cowrie.log.closed` |
| `2026-07-27 16:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c88dcba4e354

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:19 |
| **Last Seen** | 2026-07-27 16:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:19:55` | `cowrie.session.connect` |
| `2026-07-27 16:19:56` | `cowrie.client.version` |
| `2026-07-27 16:19:56` | `cowrie.client.kex` |
| `2026-07-27 16:19:56` | `cowrie.login.success` |
| `2026-07-27 16:19:58` | `cowrie.session.params` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.success` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.command.input` |
| `2026-07-27 16:19:58` | `cowrie.log.closed` |
| `2026-07-27 16:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651cc1518edd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:21 |
| **Last Seen** | 2026-07-27 16:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:21:19` | `cowrie.session.connect` |
| `2026-07-27 16:21:19` | `cowrie.client.version` |
| `2026-07-27 16:21:19` | `cowrie.client.kex` |
| `2026-07-27 16:21:21` | `cowrie.login.success` |
| `2026-07-27 16:21:22` | `cowrie.session.params` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.success` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.command.input` |
| `2026-07-27 16:21:22` | `cowrie.log.closed` |
| `2026-07-27 16:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2486a49d3a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:22 |
| **Last Seen** | 2026-07-27 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:22:46` | `cowrie.session.connect` |
| `2026-07-27 16:22:46` | `cowrie.client.version` |
| `2026-07-27 16:22:46` | `cowrie.client.kex` |
| `2026-07-27 16:22:47` | `cowrie.login.success` |
| `2026-07-27 16:22:48` | `cowrie.session.params` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.success` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.command.input` |
| `2026-07-27 16:22:48` | `cowrie.log.closed` |
| `2026-07-27 16:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a733b7a96c02

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:05` | `cowrie.session.connect` |
| `2026-07-27 16:24:05` | `cowrie.client.version` |
| `2026-07-27 16:24:05` | `cowrie.client.kex` |
| `2026-07-27 16:24:06` | `cowrie.login.success` |
| `2026-07-27 16:24:07` | `cowrie.session.params` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.success` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:07` | `cowrie.command.input` |
| `2026-07-27 16:24:08` | `cowrie.log.closed` |
| `2026-07-27 16:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4c4d1a8a3f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:51` | `cowrie.session.connect` |
| `2026-07-27 16:24:51` | `cowrie.client.version` |
| `2026-07-27 16:24:51` | `cowrie.client.kex` |
| `2026-07-27 16:24:51` | `cowrie.login.success` |
| `2026-07-27 16:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5654f28ab9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:51` | `cowrie.session.connect` |
| `2026-07-27 16:24:51` | `cowrie.client.version` |
| `2026-07-27 16:24:51` | `cowrie.client.kex` |
| `2026-07-27 16:24:51` | `cowrie.login.success` |
| `2026-07-27 16:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b717b1cb6f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:54` | `cowrie.session.connect` |
| `2026-07-27 16:24:54` | `cowrie.client.version` |
| `2026-07-27 16:24:54` | `cowrie.client.kex` |
| `2026-07-27 16:24:55` | `cowrie.login.success` |
| `2026-07-27 16:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-644e4888a2b6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:55` | `cowrie.session.connect` |
| `2026-07-27 16:24:55` | `cowrie.client.version` |
| `2026-07-27 16:24:55` | `cowrie.client.kex` |
| `2026-07-27 16:24:56` | `cowrie.login.success` |
| `2026-07-27 16:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226f01d4337c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]12` |
| **First Seen** | 2026-07-27 16:24 |
| **Last Seen** | 2026-07-27 16:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:24:55` | `cowrie.session.connect` |
| `2026-07-27 16:24:56` | `cowrie.client.version` |
| `2026-07-27 16:24:56` | `cowrie.client.kex` |
| `2026-07-27 16:24:58` | `cowrie.login.success` |
| `2026-07-27 16:24:59` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]12` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2155411254

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-27 16:25 |
| **Last Seen** | 2026-07-27 16:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:25:08` | `cowrie.session.connect` |
| `2026-07-27 16:25:09` | `cowrie.client.version` |
| `2026-07-27 16:25:09` | `cowrie.client.kex` |
| `2026-07-27 16:25:11` | `cowrie.login.success` |
| `2026-07-27 16:25:12` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cfef513153f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:25 |
| **Last Seen** | 2026-07-27 16:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:25:15` | `cowrie.session.connect` |
| `2026-07-27 16:25:15` | `cowrie.client.version` |
| `2026-07-27 16:25:15` | `cowrie.client.kex` |
| `2026-07-27 16:25:16` | `cowrie.login.success` |
| `2026-07-27 16:25:17` | `cowrie.session.params` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.success` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.command.input` |
| `2026-07-27 16:25:17` | `cowrie.log.closed` |
| `2026-07-27 16:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506a30e51201

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-07-27 16:25 |
| **Last Seen** | 2026-07-27 16:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:25:33` | `cowrie.session.connect` |
| `2026-07-27 16:25:34` | `cowrie.client.version` |
| `2026-07-27 16:25:34` | `cowrie.client.kex` |
| `2026-07-27 16:25:36` | `cowrie.login.success` |
| `2026-07-27 16:25:37` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7897db6878

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-07-27 16:25 |
| **Last Seen** | 2026-07-27 16:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:25:42` | `cowrie.session.connect` |
| `2026-07-27 16:25:43` | `cowrie.client.version` |
| `2026-07-27 16:25:43` | `cowrie.client.kex` |
| `2026-07-27 16:25:45` | `cowrie.login.success` |
| `2026-07-27 16:25:45` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ca3284afad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:26 |
| **Last Seen** | 2026-07-27 16:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:26:25` | `cowrie.session.connect` |
| `2026-07-27 16:26:26` | `cowrie.client.version` |
| `2026-07-27 16:26:26` | `cowrie.client.kex` |
| `2026-07-27 16:26:27` | `cowrie.login.success` |
| `2026-07-27 16:26:28` | `cowrie.session.params` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.success` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.command.input` |
| `2026-07-27 16:26:28` | `cowrie.log.closed` |
| `2026-07-27 16:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136314b48711

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:27 |
| **Last Seen** | 2026-07-27 16:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:27:36` | `cowrie.session.connect` |
| `2026-07-27 16:27:37` | `cowrie.client.version` |
| `2026-07-27 16:27:37` | `cowrie.client.kex` |
| `2026-07-27 16:27:38` | `cowrie.login.success` |
| `2026-07-27 16:27:39` | `cowrie.session.params` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.success` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.command.input` |
| `2026-07-27 16:27:39` | `cowrie.log.closed` |
| `2026-07-27 16:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c340f514185c

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-27 16:28 |
| **Last Seen** | 2026-07-27 16:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:28:21` | `cowrie.session.connect` |
| `2026-07-27 16:28:22` | `cowrie.client.version` |
| `2026-07-27 16:28:22` | `cowrie.client.kex` |
| `2026-07-27 16:28:24` | `cowrie.login.success` |
| `2026-07-27 16:28:24` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85045781aa4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:28 |
| **Last Seen** | 2026-07-27 16:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:28:43` | `cowrie.session.connect` |
| `2026-07-27 16:28:43` | `cowrie.client.version` |
| `2026-07-27 16:28:43` | `cowrie.client.kex` |
| `2026-07-27 16:28:44` | `cowrie.login.success` |
| `2026-07-27 16:28:45` | `cowrie.session.params` |
| `2026-07-27 16:28:45` | `cowrie.command.input` |
| `2026-07-27 16:28:45` | `cowrie.command.input` |
| `2026-07-27 16:28:45` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.success` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.command.input` |
| `2026-07-27 16:28:46` | `cowrie.log.closed` |
| `2026-07-27 16:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f13ae196b1

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-27 16:28 |
| **Last Seen** | 2026-07-27 16:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:28:48` | `cowrie.session.connect` |
| `2026-07-27 16:28:49` | `cowrie.client.version` |
| `2026-07-27 16:28:49` | `cowrie.client.kex` |
| `2026-07-27 16:28:51` | `cowrie.login.success` |
| `2026-07-27 16:28:51` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cbda25440e

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-07-27 16:28 |
| **Last Seen** | 2026-07-27 16:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:28:57` | `cowrie.session.connect` |
| `2026-07-27 16:28:57` | `cowrie.client.version` |
| `2026-07-27 16:28:57` | `cowrie.client.kex` |
| `2026-07-27 16:29:00` | `cowrie.login.success` |
| `2026-07-27 16:29:00` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464808d7a7a6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:29 |
| **Last Seen** | 2026-07-27 16:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:29:49` | `cowrie.session.connect` |
| `2026-07-27 16:29:50` | `cowrie.client.version` |
| `2026-07-27 16:29:50` | `cowrie.client.kex` |
| `2026-07-27 16:29:51` | `cowrie.login.success` |
| `2026-07-27 16:29:52` | `cowrie.session.params` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.success` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:52` | `cowrie.command.input` |
| `2026-07-27 16:29:53` | `cowrie.log.closed` |
| `2026-07-27 16:29:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7f65b1b14f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:30 |
| **Last Seen** | 2026-07-27 16:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:30:55` | `cowrie.session.connect` |
| `2026-07-27 16:30:55` | `cowrie.client.version` |
| `2026-07-27 16:30:55` | `cowrie.client.kex` |
| `2026-07-27 16:30:56` | `cowrie.login.success` |
| `2026-07-27 16:30:57` | `cowrie.session.params` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.success` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.command.input` |
| `2026-07-27 16:30:57` | `cowrie.log.closed` |
| `2026-07-27 16:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba427ac2d494

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:32 |
| **Last Seen** | 2026-07-27 16:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:32:02` | `cowrie.session.connect` |
| `2026-07-27 16:32:02` | `cowrie.client.version` |
| `2026-07-27 16:32:02` | `cowrie.client.kex` |
| `2026-07-27 16:32:03` | `cowrie.login.success` |
| `2026-07-27 16:32:04` | `cowrie.session.params` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.success` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:04` | `cowrie.command.input` |
| `2026-07-27 16:32:05` | `cowrie.log.closed` |
| `2026-07-27 16:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87fad289e5d

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-27 16:32 |
| **Last Seen** | 2026-07-27 16:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:32:46` | `cowrie.session.connect` |
| `2026-07-27 16:32:47` | `cowrie.client.version` |
| `2026-07-27 16:32:47` | `cowrie.client.kex` |
| `2026-07-27 16:32:49` | `cowrie.login.success` |
| `2026-07-27 16:32:49` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f5274ea716

| Field | Detail |
|---|---|
| **Source IP** | `110.14.192[.]20` |
| **First Seen** | 2026-07-27 16:32 |
| **Last Seen** | 2026-07-27 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:32:55` | `cowrie.session.connect` |
| `2026-07-27 16:32:56` | `cowrie.client.version` |
| `2026-07-27 16:32:56` | `cowrie.client.kex` |
| `2026-07-27 16:32:59` | `cowrie.login.success` |
| `2026-07-27 16:33:00` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.14.192[.]20` to AbuseIPDB if not already reported
- [ ] Block `110.14.192[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7798667a4f13

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:33 |
| **Last Seen** | 2026-07-27 16:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:33:14` | `cowrie.session.connect` |
| `2026-07-27 16:33:14` | `cowrie.client.version` |
| `2026-07-27 16:33:14` | `cowrie.client.kex` |
| `2026-07-27 16:33:15` | `cowrie.login.success` |
| `2026-07-27 16:33:16` | `cowrie.session.params` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.success` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.command.input` |
| `2026-07-27 16:33:16` | `cowrie.log.closed` |
| `2026-07-27 16:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45f96f8e02e5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:34 |
| **Last Seen** | 2026-07-27 16:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:34:31` | `cowrie.session.connect` |
| `2026-07-27 16:34:31` | `cowrie.client.version` |
| `2026-07-27 16:34:32` | `cowrie.client.kex` |
| `2026-07-27 16:34:32` | `cowrie.login.success` |
| `2026-07-27 16:34:33` | `cowrie.session.params` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.success` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:33` | `cowrie.command.input` |
| `2026-07-27 16:34:34` | `cowrie.log.closed` |
| `2026-07-27 16:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdecb2f4af08

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:35 |
| **Last Seen** | 2026-07-27 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:35:54` | `cowrie.session.connect` |
| `2026-07-27 16:35:54` | `cowrie.client.version` |
| `2026-07-27 16:35:54` | `cowrie.client.kex` |
| `2026-07-27 16:35:54` | `cowrie.login.success` |
| `2026-07-27 16:35:56` | `cowrie.session.params` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.success` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.command.input` |
| `2026-07-27 16:35:56` | `cowrie.log.closed` |
| `2026-07-27 16:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782850d2f9d2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:37 |
| **Last Seen** | 2026-07-27 16:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:37:04` | `cowrie.session.connect` |
| `2026-07-27 16:37:04` | `cowrie.client.version` |
| `2026-07-27 16:37:04` | `cowrie.client.kex` |
| `2026-07-27 16:37:05` | `cowrie.login.success` |
| `2026-07-27 16:37:07` | `cowrie.session.params` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.success` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.command.input` |
| `2026-07-27 16:37:07` | `cowrie.log.closed` |
| `2026-07-27 16:37:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745452854017

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:38 |
| **Last Seen** | 2026-07-27 16:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:38:10` | `cowrie.session.connect` |
| `2026-07-27 16:38:10` | `cowrie.client.version` |
| `2026-07-27 16:38:10` | `cowrie.client.kex` |
| `2026-07-27 16:38:12` | `cowrie.login.success` |
| `2026-07-27 16:38:13` | `cowrie.session.params` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.success` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:13` | `cowrie.command.input` |
| `2026-07-27 16:38:14` | `cowrie.log.closed` |
| `2026-07-27 16:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab89afc1c66f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:39 |
| **Last Seen** | 2026-07-27 16:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:39:18` | `cowrie.session.connect` |
| `2026-07-27 16:39:18` | `cowrie.client.version` |
| `2026-07-27 16:39:18` | `cowrie.client.kex` |
| `2026-07-27 16:39:19` | `cowrie.login.success` |
| `2026-07-27 16:39:20` | `cowrie.session.params` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.success` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:20` | `cowrie.command.input` |
| `2026-07-27 16:39:21` | `cowrie.log.closed` |
| `2026-07-27 16:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862f0c8d549d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:40 |
| **Last Seen** | 2026-07-27 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:40:27` | `cowrie.session.connect` |
| `2026-07-27 16:40:27` | `cowrie.client.version` |
| `2026-07-27 16:40:27` | `cowrie.client.kex` |
| `2026-07-27 16:40:28` | `cowrie.login.success` |
| `2026-07-27 16:40:29` | `cowrie.session.params` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.success` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.command.input` |
| `2026-07-27 16:40:29` | `cowrie.log.closed` |
| `2026-07-27 16:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c70a592359

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:41 |
| **Last Seen** | 2026-07-27 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:41:37` | `cowrie.session.connect` |
| `2026-07-27 16:41:37` | `cowrie.client.version` |
| `2026-07-27 16:41:37` | `cowrie.client.kex` |
| `2026-07-27 16:41:38` | `cowrie.login.success` |
| `2026-07-27 16:41:39` | `cowrie.session.params` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.success` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.command.input` |
| `2026-07-27 16:41:39` | `cowrie.log.closed` |
| `2026-07-27 16:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5592d1edff5e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:42 |
| **Last Seen** | 2026-07-27 16:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:42:47` | `cowrie.session.connect` |
| `2026-07-27 16:42:47` | `cowrie.client.version` |
| `2026-07-27 16:42:47` | `cowrie.client.kex` |
| `2026-07-27 16:42:48` | `cowrie.login.success` |
| `2026-07-27 16:42:49` | `cowrie.session.params` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.success` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.command.input` |
| `2026-07-27 16:42:49` | `cowrie.log.closed` |
| `2026-07-27 16:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64298953b394

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:43 |
| **Last Seen** | 2026-07-27 16:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:43:58` | `cowrie.session.connect` |
| `2026-07-27 16:43:58` | `cowrie.client.version` |
| `2026-07-27 16:43:58` | `cowrie.client.kex` |
| `2026-07-27 16:43:59` | `cowrie.login.success` |
| `2026-07-27 16:44:00` | `cowrie.session.params` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.success` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.command.input` |
| `2026-07-27 16:44:00` | `cowrie.log.closed` |
| `2026-07-27 16:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2804dd884d2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 16:44 |
| **Last Seen** | 2026-07-27 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:44:42` | `cowrie.session.connect` |
| `2026-07-27 16:44:42` | `cowrie.client.version` |
| `2026-07-27 16:44:42` | `cowrie.client.kex` |
| `2026-07-27 16:44:43` | `cowrie.login.success` |
| `2026-07-27 16:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9a42fbded5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-27 16:44 |
| **Last Seen** | 2026-07-27 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:44:43` | `cowrie.session.connect` |
| `2026-07-27 16:44:43` | `cowrie.client.version` |
| `2026-07-27 16:44:43` | `cowrie.client.kex` |
| `2026-07-27 16:44:44` | `cowrie.login.success` |
| `2026-07-27 16:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103c27c739dd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:45 |
| **Last Seen** | 2026-07-27 16:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:45:11` | `cowrie.session.connect` |
| `2026-07-27 16:45:11` | `cowrie.client.version` |
| `2026-07-27 16:45:11` | `cowrie.client.kex` |
| `2026-07-27 16:45:12` | `cowrie.login.success` |
| `2026-07-27 16:45:13` | `cowrie.session.params` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.success` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:13` | `cowrie.command.input` |
| `2026-07-27 16:45:14` | `cowrie.log.closed` |
| `2026-07-27 16:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de178d49f60

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:46 |
| **Last Seen** | 2026-07-27 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:46:30` | `cowrie.session.connect` |
| `2026-07-27 16:46:30` | `cowrie.client.version` |
| `2026-07-27 16:46:30` | `cowrie.client.kex` |
| `2026-07-27 16:46:30` | `cowrie.login.success` |
| `2026-07-27 16:46:31` | `cowrie.session.params` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.success` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:31` | `cowrie.command.input` |
| `2026-07-27 16:46:32` | `cowrie.log.closed` |
| `2026-07-27 16:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda68262508c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:47 |
| **Last Seen** | 2026-07-27 16:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:47:40` | `cowrie.session.connect` |
| `2026-07-27 16:47:40` | `cowrie.client.version` |
| `2026-07-27 16:47:40` | `cowrie.client.kex` |
| `2026-07-27 16:47:41` | `cowrie.login.success` |
| `2026-07-27 16:47:42` | `cowrie.session.params` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.success` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:42` | `cowrie.command.input` |
| `2026-07-27 16:47:43` | `cowrie.log.closed` |
| `2026-07-27 16:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7150ad27a12

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:48 |
| **Last Seen** | 2026-07-27 16:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:48:45` | `cowrie.session.connect` |
| `2026-07-27 16:48:45` | `cowrie.client.version` |
| `2026-07-27 16:48:45` | `cowrie.client.kex` |
| `2026-07-27 16:48:46` | `cowrie.login.success` |
| `2026-07-27 16:48:47` | `cowrie.session.params` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.success` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:47` | `cowrie.command.input` |
| `2026-07-27 16:48:48` | `cowrie.log.closed` |
| `2026-07-27 16:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0dd97737ad6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:49 |
| **Last Seen** | 2026-07-27 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:49:51` | `cowrie.session.connect` |
| `2026-07-27 16:49:51` | `cowrie.client.version` |
| `2026-07-27 16:49:51` | `cowrie.client.kex` |
| `2026-07-27 16:49:52` | `cowrie.login.success` |
| `2026-07-27 16:49:53` | `cowrie.session.params` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.success` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.command.input` |
| `2026-07-27 16:49:53` | `cowrie.log.closed` |
| `2026-07-27 16:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641f3b418a13

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:51 |
| **Last Seen** | 2026-07-27 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:51:03` | `cowrie.session.connect` |
| `2026-07-27 16:51:03` | `cowrie.client.version` |
| `2026-07-27 16:51:03` | `cowrie.client.kex` |
| `2026-07-27 16:51:04` | `cowrie.login.success` |
| `2026-07-27 16:51:05` | `cowrie.session.params` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.success` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.command.input` |
| `2026-07-27 16:51:05` | `cowrie.log.closed` |
| `2026-07-27 16:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c452d9a467

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:52 |
| **Last Seen** | 2026-07-27 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:52:20` | `cowrie.session.connect` |
| `2026-07-27 16:52:20` | `cowrie.client.version` |
| `2026-07-27 16:52:20` | `cowrie.client.kex` |
| `2026-07-27 16:52:21` | `cowrie.login.success` |
| `2026-07-27 16:52:22` | `cowrie.session.params` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.success` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.command.input` |
| `2026-07-27 16:52:22` | `cowrie.log.closed` |
| `2026-07-27 16:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6319e639f392

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-27 16:52 |
| **Last Seen** | 2026-07-27 16:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:52:52` | `cowrie.session.connect` |
| `2026-07-27 16:52:53` | `cowrie.client.version` |
| `2026-07-27 16:52:53` | `cowrie.client.kex` |
| `2026-07-27 16:52:54` | `cowrie.login.success` |
| `2026-07-27 16:52:54` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e7fc484038

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-27 16:53 |
| **Last Seen** | 2026-07-27 16:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:53:17` | `cowrie.session.connect` |
| `2026-07-27 16:53:17` | `cowrie.client.version` |
| `2026-07-27 16:53:17` | `cowrie.client.kex` |
| `2026-07-27 16:53:18` | `cowrie.login.success` |
| `2026-07-27 16:53:19` | `cowrie.direct-tcpip.request` |
| `2026-07-27 16:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2415beda34

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-07-27 16:53 |
| **Last Seen** | 2026-07-27 16:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:53:24` | `cowrie.session.connect` |
| `2026-07-27 16:53:24` | `cowrie.client.version` |
| `2026-07-27 16:53:24` | `cowrie.client.kex` |
| `2026-07-27 16:53:25` | `cowrie.login.success` |
| `2026-07-27 16:53:25` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd2d14987ab

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:53 |
| **Last Seen** | 2026-07-27 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:53:44` | `cowrie.session.connect` |
| `2026-07-27 16:53:45` | `cowrie.client.version` |
| `2026-07-27 16:53:45` | `cowrie.client.kex` |
| `2026-07-27 16:53:45` | `cowrie.login.success` |
| `2026-07-27 16:53:46` | `cowrie.session.params` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.success` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.command.input` |
| `2026-07-27 16:53:46` | `cowrie.log.closed` |
| `2026-07-27 16:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8eba26f3b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]34` |
| **First Seen** | 2026-07-27 16:55 |
| **Last Seen** | 2026-07-27 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-27 16:55:01` | `cowrie.session.connect` |
| `2026-07-27 16:55:02` | `cowrie.client.version` |
| `2026-07-27 16:55:02` | `cowrie.client.kex` |
| `2026-07-27 16:55:03` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]34` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **25** | 2026-07-27 13:00 | 2026-07-27 16:43 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `94.154.43[.]210` | **12** | 2026-07-27 14:43 | 2026-07-27 16:22 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `150.95.66[.]172` | **10** | 2026-07-27 13:11 | 2026-07-27 16:37 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-27 13:11 | 2026-07-27 16:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **6** | 2026-07-27 14:57 | 2026-07-27 15:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.201.104[.]216` | **5** | 2026-07-27 12:58 | 2026-07-27 13:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.167[.]142` | **4** | 2026-07-27 16:08 | 2026-07-27 16:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **3** | 2026-07-27 15:22 | 2026-07-27 16:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]34` | **3** | 2026-07-27 15:48 | 2026-07-27 15:57 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-27 16:16 | 2026-07-27 16:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-27 13:44 | 2026-07-27 13:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-27 13:43 | 2026-07-27 13:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **3** | 2026-07-27 13:35 | 2026-07-27 13:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | **3** | 2026-07-27 13:46 | 2026-07-27 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]107` | **3** | 2026-07-27 13:46 | 2026-07-27 13:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]233` | **3** | 2026-07-27 13:47 | 2026-07-27 13:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.20.160[.]34` | **2** | 2026-07-27 16:00 | 2026-07-27 16:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `111.228.5[.]238` | **2** | 2026-07-27 14:21 | 2026-07-27 14:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `118.145.231[.]144` | **2** | 2026-07-27 16:29 | 2026-07-27 16:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-27 15:59 | 2026-07-27 16:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]36` | 1 | 2026-07-27 14:20 | 2026-07-27 14:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-07-27 14:57 | 2026-07-27 14:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-07-27 13:12 | 2026-07-27 13:12 | 7s | 0 | `T1592` | 🟢 LOW |
| `125.227.240[.]43` | 1 | 2026-07-27 14:32 | 2026-07-27 14:33 | 7s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-27 14:06 | 2026-07-27 14:07 | 36s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-07-27 14:34 | 2026-07-27 14:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]93` | 1 | 2026-07-27 15:07 | 2026-07-27 15:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-07-27 13:12 | 2026-07-27 13:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.193.147[.]75` | 1 | 2026-07-27 13:15 | 2026-07-27 13:15 | 4s | 0 | `T1592` | 🟢 LOW |
| `218.13.157[.]209` | 1 | 2026-07-27 13:52 | 2026-07-27 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-27 16:07 | 2026-07-27 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-27 15:35 | 2026-07-27 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.7.197[.]30` | 1 | 2026-07-27 13:17 | 2026-07-27 13:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-07-27 13:34 | 2026-07-27 13:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-27 13:34 | 2026-07-27 13:34 | 1s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-27 15:15 | 2026-07-27 15:15 | 40s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-07-27 15:11 | 2026-07-27 15:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-27 16:47 | 2026-07-27 16:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]162` | 1 | 2026-07-27 13:32 | 2026-07-27 13:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-27 14:35 | 2026-07-27 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.28.66[.]63` | 1 | 2026-07-27 13:22 | 2026-07-27 13:22 | 12s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-07-27 15:43 | 2026-07-27 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-07-27 13:33 | 2026-07-27 13:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-07-27 12:56 | 2026-07-27 12:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.43.232[.]42` | 1 | 2026-07-27 15:22 | 2026-07-27 15:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]105` | 1 | 2026-07-27 13:41 | 2026-07-27 13:41 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]3` | 1 | 2026-07-27 13:43 | 2026-07-27 13:43 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]35` | 1 | 2026-07-27 13:41 | 2026-07-27 13:41 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 40/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `44fcd7a6a61dd418b64fd2fa3e0048d139740bf74a77d261a6900e24609e83f6` | ELF Binary (Linux executable) (x86 32-bit) | `44fcd7a6a61dd418...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |

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
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 7 |
| `14.153.226[.]88` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `213.141.130[.]251` | RU | Meridian-net Network | **100** ⚠️ | 6 |
| `222.139.245[.]137` | CN | China Unicom Henan province network | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `150.95.66[.]172` | TH | ZCOM THAI EP | **100** ⚠️ | 6 |
| `111.228.5[.]238` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 17 |
| `121.66.63[.]186` | KR | LG Uplus | **100** ⚠️ | 50 |
| `66.132.224[.]233` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 176 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 144 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 51 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 50 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 50 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 3 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 307 cases |
| Tool 34  | Credential Extractor        | ✅ 256 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 143 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 92 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 144 priority case(s) shown individually · 48 recon entry/entries in table (20 group(s) consolidating 106 session(s)).

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
_Report time: 2026-07-27T17:47:19Z_

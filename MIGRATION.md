# THIR Migration — thir-live → thir-ha

## What this repository is
thir-ha is the Oracle Cloud HA continuation of THIR (Threat Hunter Intelligence Range).
It was forked from thir-live and restructured for a two-node Oracle Always Free deployment.

## Architecture change
- **thir-live:** Single AWS EC2 t2.micro — GitHub Actions SSHed directly to EC2
- **thir-ha:** Two Oracle VM.Standard.E2.1.Micro — VM1 sensor, VM2 brain
  - GitHub Actions SSHes to VM2 only
  - VM2 rsync pulls logs from VM1 via Oracle VCN private network (10.0.0.x)
  - VM1 never directly accessed by pipeline

## Branch
Default branch is `oracle-ha` — not `main`.
This intentionally breaks GitHub fork sync with thir-live.

## Key differences from thir-live
| Item | thir-live | thir-ha |
|------|-----------|---------|
| Platform | AWS EC2 t2.micro | Oracle Cloud 2x E2.1.Micro |
| Node count | 1 | 2 (sensor + brain) |
| Pipeline SSH target | AWS EC2 direct | VM2 only |
| Log path (pipeline reads) | `/home/cowrie/.../cowrie.json` | `/opt/thir/logs/cowrie.json` |
| Load balancer | None | HAProxy on VM2 |
| DNS failover | None | Cloudflare health checks |
| Raw log archive | None | Cloudflare R2 |

## Legacy reference
thir-live: [link to thir-live repo] — archived after Oracle pipeline confirmed stable 72h+

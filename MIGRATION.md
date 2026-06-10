# THIR Migration — thir-live → thir-ha

*Documents what changed, what was preserved, and why — for anyone reviewing the repository history.*

---

## What This Repository Is

thir-ha is the Oracle Cloud HA continuation of THIR (Threat Hunter Intelligence Range). It was forked from thir-live in May 2026 and restructured for a two-node Oracle Always Free deployment. The fork preserves the full git history of thir-live, showing the architecture evolution from single-node AWS to two-node Oracle HA.

thir-live operated from March 7 2026 to [retirement date] on AWS EC2 t2.micro (free tier). Oracle takes over as primary after a 72-hour parallel validation run. thir-live is archived on GitHub after Oracle is confirmed stable — archiving stops GitHub Actions but GitHub Pages remains live.

---

## Why Oracle Cloud

| Factor | AWS EC2 t2.micro | Oracle E2.1.Micro |
|---|---|---|
| Free tier duration | 12 months (expiring ~Sep 2026) | Always Free — no expiry |
| vCPU | Burstable (shared core) | Full AMD core |
| VM count | 1 free | 2 free simultaneously |
| Cost after free tier | Billable | Never billable |
| Migration urgency | ~4 months runway at fork time | Eliminates deadline |

The two-VM Always Free allowance is the deciding factor. One VM for sensor exposure, one VM for pipeline processing — a separation that wasn't possible on AWS without cost.

---

## Architecture Change

| Property | thir-live (AWS) | thir-ha (Oracle) |
|---|---|---|
| Platform | AWS EC2 t2.micro | 2x Oracle VM.Standard.E2.1.Micro |
| Node count | 1 | 2 (sensor + brain) |
| Pipeline SSH target | AWS EC2 direct | VM2 only (150.230.174.199) |
| Log source path | `/home/cowrie/.../cowrie.json` | `/opt/thir/logs/cowrie.json` |
| Log delivery | SCP from EC2 in pipeline | rsync VM2←VM1 pre-pipeline |
| Load balancer | None | HAProxy on VM2 |
| DNS failover | None | Cloudflare health checks |
| Raw log archive | None | Cloudflare R2 (`thirha-raw-archive` — Oracle corpus, June 2026+) |
| Admin port | 22222 (single VM) | 22222 (both VMs) |

---

## Branch

Default branch is `oracle-ha` — not `main`. This intentionally prevents automatic GitHub fork sync with thir-live and makes the architectural break explicit.

---

## Key Pipeline Change

The single most important workflow change: the log fetch step.

**thir-live** — GitHub Actions SSHed directly to the EC2 and ran `tail -n +N` on the live Cowrie log file:

```yaml
ssh ubuntu@${{ secrets.ORACLE_VPS_IP }} \
  "tail -n +$LINE /home/cowrie/cowrie/var/log/cowrie/cowrie.json"
```

**thir-ha** — VM2 rsync pulls logs from VM1 via private VCN before the pipeline runs. GitHub Actions reads from VM2's local copy:

```yaml
ssh -p 22222 ubuntu@${{ secrets.ORACLE_VPS_IP }} \
  "tail -n +$LINE /opt/thir/logs/cowrie.json"
```

`ORACLE_VPS_IP` now points to VM2 (150.230.174.199). VM1 (129.80.119.236) is never in any GitHub secret. VM1 is public-facing attack surface and must never be a direct pipeline target.

---

## Tools Carried Unchanged

All 15 core pipeline tools (05, 07, 26–37) are carried from thir-live without modification. They read and write the same file formats. The only change affecting them is the log source path — they still consume `/tmp/cowrie.json` which the pipeline places there after fetching from VM2's local copy.

| Tool | Change |
|---|---|
| 05 `network_monitor_live.go` | Now checks VM2 HAProxy port 2222 — not EC2 direct. Functionally equivalent: confirms full honeypot path is working. |
| All others (07, 26–37) | No changes. |

---

## New Tools Required

These tools do not exist in thir-live. They are built specifically for the HA architecture.

| Tool | Purpose | Replaces | Priority |
|---|---|---|---|
| 00 `historical_processor.py` | Batch re-process 59-day AWS log corpus → `historical_data/` | Nothing — new capability | High — before AWS retires |
| 38 `rsync_collector.py` | Structured log pull VM1→VM2 with verification and logging | Shell cron script `/home/ubuntu/rsync_from_vm1.sh` | High — at launch |
| 39 `node_healthcheck.go` | Direct VM1 health checks via private VCN → `data/node_health.json` | Nothing — Tool 05 checks VM2/HAProxy only | High — at launch |
| 40 `failover_notifier.py` | Alerts when HAProxy shifts traffic between backends | Nothing — new capability | Medium |
| 41 `http_honeypot.py` | Flask HTTP attack surface on VM1 port 8080 | Nothing — new sensor type | Medium — after SSH stable |
| 42 `http_parser_live.py` | Parses HTTP honeypot logs → ir_cases format | Nothing — new parser | Medium — after Tool 41 |

---

## New Data Files

These `data/` files do not exist in thir-live:

| File | Written By | Purpose |
|---|---|---|
| `data/node_health.json` | Tool 39 | VM1 direct health status — separate from Tool 05's HAProxy check |

`historical_data/` directory is also new — created by Tool 00 and committed to the repo as a permanent baseline from the 59-day AWS corpus.

---

## Files Retired or Superseded

| File | Status | Reason |
|---|---|---|
| `docs/runbook_rc_rp_1.md` | Superseded | AWS single-node recovery procedure. Oracle HA recovery is covered by `docs/THIR_HA_Runbooks_v2.docx` RB-02 through RB-06. Retained for historical reference only. |
| `SETUP.md` (thir-live version) | Replaced | Described AWS EC2 setup. Replaced with Oracle HA deployment guide. |

---

## Raw Log Preservation — Two Corpora

Two separate Cloudflare R2 buckets archive two distinct corpora. They must not be conflated.

**AWS corpus — `thir-raw-archive`**

59 days of raw Cowrie logs (March 7 – May 5 2026, ~540MB NDJSON) from the AWS deployment. Archived before AWS EC2 retires (~Sep 2026). Three individual log files exceed GitHub's 100MB limit — GitHub storage was never an option for this data.

The Apr 19-22 2026 anomaly (3 days, 250MB, 46% of the AWS corpus) is the most intelligence-rich period in the AWS data — an identified multi-day campaign. Tool 00 processes the full AWS corpus and commits results to `historical_data/` — recovering intelligence that the rolling pipeline retention deleted.

**Oracle corpus — `thirha-raw-archive`**

Oracle VM1 production logs from June 2026 onwards. Active ongoing archive — `sync_to_r2.sh` runs daily at 01:00 UTC on VM2, compressing and uploading the previous day's logs. This bucket grows continuously for the life of the Oracle deployment.

---

## Migration Sequence — At a Glance

| Step | Action | Status |
|---|---|---|
| 1 | Set up Cloudflare R2, compress and upload 59-day AWS log corpus | ✓ Complete |
| 2 | Provision Oracle VM2 (brain), VM1 (sensor) | ✓ Complete |
| 3 | Install HAProxy on VM2, Cowrie on both VMs | ✓ Complete |
| 4 | Configure rsync VM2←VM1 via private VCN | ✓ Complete — shell script |
| 5 | Fork thir-live → thir-ha, update pipeline.yml | ✓ Complete |
| 6 | Update GitHub secrets — ORACLE_VPS_IP → VM2 | ✓ Complete |
| 7 | Parallel run + 72h stability check | In progress |
| 8 | Cutover — Oracle confirmed as primary | ✓ Complete |
| 9 | Run Tool 00 — process full 59-day AWS history | Pending |
| 10 | Archive thir-live on GitHub | Pending — after Oracle stable |
| 11 | Terminate AWS EC2 before billing resumes | Pending — ~Sep 2026 |

---

## Legacy Reference

- **thir-live repo:** [https://github.com/nikhilsalunkemumbai/thir-live] — archived after Oracle pipeline confirmed stable 72h+
- **AWS corpus archive:** Cloudflare R2 `thir-raw-archive` — March–September 2026 raw logs
- **Oracle corpus archive:** Cloudflare R2 `thirha-raw-archive` — June 2026 onwards, active ongoing sync
- **Original recovery runbook:** `docs/runbook_rc_rp_1.md` — AWS single-node, superseded by HA runbooks

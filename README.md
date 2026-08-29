# THIR.HA — Threat Hunter Intelligence Range HAProxy

A live honeypot threat intelligence platform. Two Oracle Cloud Always Free VMs — one sensor, one brain — capture real-world attacks continuously. A GitHub Actions pipeline runs every two hours: parsing sessions, enriching attacker IPs, clustering campaigns, analysing malware, and publishing to a live dashboard with automated SOC reporting.

**Live:** [thirha.aegispub.com](https://thirha.aegispub.com)

---

## Architecture

```
                         Internet
                            │
                   Cloudflare (free tier)
              DNS health checks · DDoS protection
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
     VM1 — Sensor Node              VM2 — Brain Node
     ─────────────────              ────────────────
     Cowrie SSH    :2222            HAProxy TCP LB  :2222
     Cowrie Telnet :2223            HAProxy Telnet  :2223
     cloudflared tunnel             pipeline tools
     Public IP: 129.80.119.236      rsync collector
     Private IP: 10.0.0.53          cloudflared tunnel
                                    Public IP: 150.230.174.199
                                    Private IP: 10.0.0.73
            │                               │
            └──────── Oracle VCN ───────────┘
                       10.0.0.0/24
                    (internal · 10Gbps)
                            │
                     GitHub Actions
                  (SSHes to VM2 only —
                   VM1 never touched)
                            │
               thirha.aegispub.com
                 (GitHub Pages)
```

### Data Flow

```
VM1 Cowrie writes → /home/cowrie/cowrie/var/log/cowrie/cowrie.json
        │
        │  rsync over Oracle VCN private IP (10.0.0.x)
        │  VM2 cron pulls at :55 — before GitHub Actions at :00
        ▼
VM2 local copy  → /opt/thir/logs/cowrie.json
        │
        │  GitHub Actions SSHes to VM2 public IP (port 22222)
        │  reads /opt/thir/logs/cowrie.json (watermark-incremental)
        ▼
┌──────────────────────────────────────────────────────────────┐
│                   GitHub Actions Pipeline                     │
│                                                              │
│  ── Every 2 hours ─────────────────────────────────────── │
│  Tool 05  → Honeypot liveness (HAProxy:2222)→posture.json   │
│           →                              → data/assets.json  │
│  [rsync]  → Incremental log fetch        → /tmp/cowrie.json  │
│  Tool 26  → Parse Cowrie sessions        → data/ir_cases.json│
│  Tool 34  → Credential extraction        → data/credentials.json│
│  Tool 35  → SSH fingerprint aggregation  → data/ssh_fingerprints.json│
│  Tool 36  → Command clustering           → data/command_clusters.json│
│  Tool 27  → Enrich attacker IPs          → data/threat_ips.json│
│  Tool 29  → FP filter                    → data/fp_filter.json│
│  Tool 30  → Aggregate metrics            → data/stats.json   │
│  Tool 30b → ASN clustering               → data/asn_clusters.json│
│  [cond]   → Fetch downloads (if any)     → /tmp/cowrie-downloads/│
│  Tool 31  → Malware analysis (cond.)     → data/malware_report.json│
│  Tool 33  → YARA classifier (cond.)      → data/yara_matches.json│
│  Tool 28  → SOC handover report          → data/soc_handover.md│
│  Tool 37  → Alert engine                 → data/alert_history.json│
│  Tool 32  → Save daily + peak stats      → reports/daily/    │
│  Tool 07  → Data integrity check         → (exit code)       │
│                                                              │
│  ── Monday (sentinel-triggered) ──────────────────────────── │
│  Tool 32 --rollup weekly                 → reports/weekly/   │
│                                                              │
│  ── 1st of month (sentinel, deferred until prior month's   │
│     final ISO week is rolled up) ─────────────────────────  │
│  Tool 32 --rollup monthly                → reports/monthly/  │
│                                                              │
│  ── April 1 (fixed fiscal-year boundary) ─────────────────  │
│  Tool 32 --rollup monthly (yearly step)  → reports/yearly/   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
        │  git push data/ + reports/
        ▼
GitHub Pages → thirha.aegispub.com
```

```
┌──────────────────────────────────────────────────────────────┐
│         GitHub Actions — Enriched Corpus Workflow             │
│         (.github/workflows/enriched_corpus.yml)                │
│         Independent workflow — offset +15min from pipeline    │
│                                                              │
│  ── Every 2 hours (15 */2) ─────────────────────────────── │
│  Tool 43 → Actor Corpus          → data/enriched_corpus.json │
│  Tool 44 → Campaign Corpus       → data/campaign_corpus.json │
│  Tool 47 → Credential Corpus     → data/credential_corpus.json│
│  Tool 48 → Fingerprint Corpus    → data/fingerprint_corpus.json│
│  Tool 49 → Malware Corpus        → data/malware_corpus.json  │
│  Tool 50 → Infrastructure Corpus → data/infrastructure_corpus.json│
│                                                              │
│  ── 1st of month (once, via persisted marker) ──────────── │
│  R2 archive (all six, via r2_archive_helper.py)               │
│  Prune entries >180 days (all except Tool 49 — permanent)     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
        │  git push data/*_corpus.json (never touches pipeline.yml's files)
        ▼
Read by Tool 27 (AbuseIPDB/OTX cache) and Tool 31 (VirusTotal cache)
on their NEXT run — see docs/enriched_corpus_schema_reconciliation.md
```

### HA Stack

| Layer | Technology | Scope | Failover Time |
|---|---|---|---|
| DNS | Cloudflare health checks | Full VM failover | 60–120 seconds |
| TCP | HAProxy on VM2 | Service-level (Cowrie crash) | 30–60 seconds |
| Tunnel | cloudflared on both VMs | Network blip recovery | 10–30 seconds |
| Data | Rsync over VCN 10.0.0.x | Log continuity | No real-time gap |

---

## Pipeline Tools

### Core Tools (carried from thir-live, Oracle-adapted)

| # | Tool | Language | Role |
|---|---|---|---|
| 05 | `05_network_monitor_live.go` | Go | TCP liveness check on VM2 HAProxy:2222; writes `posture.json` + `assets.json` |
| 07 | `07_file_integrity_live.go` | Go | SHA-256 baseline verification of `data/` files |
| 26 | `26_incident_timeline_live.py` | Python | Parses Cowrie NDJSON → IR cases with MITRE ATT&CK TTPs |
| 27 | `27_threat_intel_feeder_live.go` | Go | Concurrent IP enrichment via AbuseIPDB + OTX |
| 28 | `28_soc_handover_live.py` | Python | Generates structured SOC handover report per run |
| 29 | `29_false_positive_live.py` | Python | 3-signal FP filter (score, ISP, behaviour) |
| 30 | `30_metric_exporter_live.go` | Go | Aggregates all pipeline outputs → dashboard stats |
| 30b | `30b_asn_clustering_live.go` | Go | Groups attacker IPs by ASN; tags Tor/VPN/proxy infrastructure |
| 31 | `31_malware_analyzer_live.py` | Python | Magic bytes, hashes, suspicious strings, optional VirusTotal |
| 32 | `32_report_lifecycle.py` | Python | Daily save, weekly/monthly/yearly (fiscal Apr-Mar) rollup, peak stats, consumption-pruned at every tier |
| 33 | `33_yara_classifier_live.py` | Python | YARA rule matching on downloaded malware; heuristic fallback |
| 34 | `34_credential_extractor_live.py` | Python | Extracts attacker username/password pairs; top credentials analysis |
| 35 | `35_ssh_fingerprint_live.py` | Python | HASSH fingerprints, client family mapping, botnet KEX detection |
| 36 | `36_command_clustering_live.py` | Python | Groups sessions by Jaccard similarity; detects campaigns |
| 37 | `37_alerts_live.py` | Python | Alert engine — HIGH/CRITICAL findings via Slack/email/dry-run |

### HA Tools (planned — thir-ha only)

| # | Tool | Language | Role |
|---|---|---|---|
| 00 | `00_historical_processor.py` | Python | Batch re-process full 59-day AWS log corpus → `historical_data/` |
| 38 | `38_rsync_collector.py` | Python | Structured log pull VM1→VM2 via private VCN; replaces shell cron script |
| 39 | `39_node_healthcheck.go` | Go | Direct VM1 health checks (10.0.0.53); writes `data/node_health.json` |
| 40 | `40_failover_notifier.py` | Python | Alerts when HAProxy shifts traffic between backends |

### Enriched Corpus Tools (thir-ha only — cross-run accumulation)

Six tools that accumulate permanent, cross-run state from the live pipeline's outputs, running in a separate workflow (`.github/workflows/enriched_corpus.yml`) offset 15 minutes after the main pipeline. Unlike the tools above, which each produce output scoped to a single 2h run, these six read that per-run output and merge it into a growing vault — see `docs/enriched_corpus_schema_reconciliation.md` for the full field-level design and `docs/enriched_corpus_build_plan.md` for build rationale.

| # | Tool | Language | Role |
|---|---|---|---|
| 43 | `43_enriched_corpus.py` | Python | Actor Corpus — per-IP cross-run memory (first/last seen, session count, TTP union); also the TTL cache Tool 27 reads to skip redundant AbuseIPDB/OTX calls |
| 44 | `44_campaign_corpus.py` | Python | Campaign Corpus — cross-run campaign tracking keyed by `sequence_hash`, with active/ended status |
| 47 | `47_credential_corpus.py` | Python | Credential Corpus — cross-run credential pair accumulation, keyed by SHA256(username\|password) |
| 48 | `48_fingerprint_corpus.py` | Python | Fingerprint Corpus — cross-run HASSH tracking, exact session dedup via `sessions[]` |
| 49 | `49_malware_corpus.py` | Python | Malware Corpus — permanent SHA256 sample vault; never pruned by design; also the cache Tool 31 reads to skip redundant VirusTotal calls |
| 50 | `50_infrastructure_corpus.py` | Python | Infrastructure Corpus — cross-run ASN tracking; cross-references Tool 43's output for Tor/VPN/proxy confirmation |
| — | `r2_archive_helper.py` | Python | Shared module (not a numbered pipeline tool) — gzip + verified R2 upload, reused by all six corpus tools above |

**Retention:** each corpus vault (`data/*_corpus.json`) is permanent in git — never wholesale overwritten. On the 1st of each calendar month (once, via a persisted `last-archived-month` marker rather than a same-day repeat trigger), each corpus is snapshotted to Cloudflare R2 (`thirha-raw-archive`, same bucket and `r2-oracle` remote as the historical corpus above) and entries older than 180 days are pruned from the git vault — except Tool 49's malware corpus, which is permanent-retention by design (a SHA256 hash vault has no useful "too old" concept for future cross-referencing).

**API cost reduction:** Tools 27 and 31 were both modified to check these corpora before making external API calls — Tool 27 against Tool 43's output (AbuseIPDB, ipinfo.io, and OTX, all skipped on a TTL-fresh cache hit), Tool 31 against Tool 49's output (VirusTotal, skipped permanently once a SHA256 has a cached result). Both changes are backward compatible: with no corpus file present, both tools behave exactly as before.

### HTTP Honeypot Tools (planned — pending Tool 41 deployment)

| # | Tool | Language | Role |
|---|---|---|---|
| 41 | `41_http_honeypot.py` | Python/Flask | HTTP attack surface on port 8080; NDJSON output |
| 42 | `42_http_parser_live.py` | Python | Parses HTTP honeypot logs → `ir_cases.json` format |

---

## Incremental Log Fetching

The pipeline uses watermark-based incremental fetching. After each successful run, the total line count of VM2's `cowrie.json` is saved to `data/cowrie_watermark.json`. On the next run, only new lines since the watermark are fetched via `tail -n +N`. Each run processes only the delta — typically 50–200 lines per 2-hour window.

**Fallback:** If the watermark file is missing, or VM2 line count is less than the stored watermark (log rotation on VM1), the pipeline falls back to a full fetch automatically.

---

## Report Lifecycle (Tool 32)

| Tier | Trigger | Output | Retention |
|---|---|---|---|
| Daily | Every pipeline run | `reports/daily/soc_YYYY-MM-DD.md` | 5–7 days |
| Weekly | Monday (sentinel-triggered, no fixed hour) | `reports/weekly/soc_week_YYYY-WNN.md` | 3–4 weeks (consumption-pruned by Monthly) |
| Monthly | 1st of month — deferred until the previous month's final ISO week has itself been rolled up (see below) | `reports/monthly/soc_YYYY-MM.md` | Consumption-pruned by Yearly, not age-pruned |
| Yearly | April 1 (fixed fiscal-year boundary, no jurisdiction-specific meaning) | `reports/yearly/soc_FY<start>-<end>.md` | Permanent |

Monthly rollup will not run before its actual prerequisite exists: if the previous month's last few days fall in an ISO week extending into the following month (true for December every year), monthly rollup defers automatically and retries on the next scheduled run rather than producing a short month or racing weekly's own rollup of that same week. The original 6-month monthly retention cap was an AWS free-tier credit-expiry workaround; since the Oracle HA migration there is no equivalent time constraint, so monthly reports are retained until rolled into a yearly summary instead of being deleted outright.

Peak stats (peak sessions, unique IPs, confirmed threats) are tracked as high-water marks in `data/stats.json` — only updated when the current run beats the existing peak, never reset by a quieter run.

---

## Malware Analysis (Tool 31)

Runs only when downloads are detected in `ir_cases.json`. Runs before Tool 28 so SOC handover always contains current-run malware findings.

- File type detection via magic byte signatures (ELF, PE, shell scripts, archives)
- Hash computation — MD5, SHA1, SHA256 per sample
- ELF architecture detection — x86, x86-64, ARM, AArch64, MIPS, RISC-V
- Suspicious string scanning — 30+ patterns across persistence, C2, crypto miners, destructive commands
- VirusTotal lookup (optional, free tier) — hash-based, reports detection ratios
- Threat scoring — 0–100 score mapping to LOW / MEDIUM / HIGH severity

Output: `data/malware_report.json`

---

## Alert Engine (Tool 37)

Alert conditions: HIGH/CRITICAL malware samples, new successful-authentication IPs, new ASN clusters, TCP tunnel attempts, active campaigns from Tool 36 clustering.

Channels controlled by `ALERT_CHANNEL` secret: `slack`, `email`, `both`, or `dry-run` (default if not set — safe on first deploy). Deduplication state in `data/alert_history.json` prevents repeat alerts on the same finding.

---

## Quick Start

See **[SETUP.md](SETUP.md)** for the complete step-by-step Oracle HA deployment guide.

### Required GitHub Secrets

| Secret | Purpose |
|---|---|
| `ORACLE_VPS_SSH_KEY` | SSH private key for Oracle VM2 (ubuntu user, port 22222) |
| `ORACLE_VPS_IP` | Oracle VM2 public IP — pipeline brain node |
| `ABUSEIPDB_API_KEY` | [abuseipdb.com](https://www.abuseipdb.com) free key |
| `OTX_API_KEY` | [otx.alienvault.com](https://otx.alienvault.com) free key |

### Optional GitHub Secrets

| Secret | Purpose |
|---|---|
| `VIRUSTOTAL_API_KEY` | VirusTotal free key — enables Tool 31 hash lookups |
| `ALERT_CHANNEL` | `slack` \| `email` \| `both` \| `dry-run` (default: `dry-run`) |
| `SLACK_WEBHOOK_URL` | Required if `ALERT_CHANNEL` includes `slack` |
| `SMTP_HOST` / `SMTP_USER` / `SMTP_PASS` | Required if `ALERT_CHANNEL` includes `email` |
| `ALERT_EMAIL_FROM` / `ALERT_EMAIL_TO` | Sender/recipient for email alerts |

---

## Repository Structure

```
thir-ha/
├── .github/workflows/
│   └── pipeline.yml              ← 3 schedules: every 2h + weekly + monthly
├── tools/
│   ├── core/                     ← Tools 05, 07, 26–37 (Oracle-adapted)
│   ├── ha/                       ← Tools 00, 38, 39, 40 (HA-specific)
│   └── http_honeypot/            ← Tools 41, 42 (planned)
├── config/
│   ├── haproxy.cfg               ← HAProxy reference config (VM2)
│   ├── vcn_rules.md              ← Oracle VCN ingress rules
│   └── cloudflare.md             ← DNS failover + tunnel setup
├── data/                         ← Written by pipeline every 2 hours
│   ├── ir_cases.json             ← IR cases from Cowrie sessions (Tool 26)
│   ├── threat_ips.json           ← Enriched attacker IPs (Tool 27)
│   ├── fp_filter.json            ← False positive decisions (Tool 29)
│   ├── stats.json                ← Aggregated metrics + peak stats (Tool 30)
│   ├── node_health.json          ← VM1 direct health checks (Tool 39)
│   ├── posture.json              ← HAProxy liveness + CIS controls (Tool 05)
│   ├── assets.json               ← Live asset inventory (Tool 05)
│   ├── soc_handover.md           ← Current SOC shift report (Tool 28)
│   ├── malware_report.json       ← Malware analysis results (Tool 31)
│   ├── yara_matches.json         ← YARA classification results (Tool 33)
│   ├── credentials.json          ← Attacker credential pairs (Tool 34)
│   ├── ssh_fingerprints.json     ← HASSH fingerprints (Tool 35)
│   ├── command_clusters.json     ← Session clusters + campaigns (Tool 36)
│   ├── asn_clusters.json         ← ASN groupings (Tool 30b)
│   ├── alert_history.json        ← Alert dedup state (Tool 37)
│   ├── cowrie_watermark.json     ← Incremental fetch watermark
│   └── integrity_baseline.json  ← SHA-256 baseline (Tool 07)
├── historical_data/              ← Tool 00 output — 59-day AWS corpus baseline
│   │                               Source: thir-raw-archive (AWS R2 bucket)
│   ├── historical_ir_cases.json
│   ├── historical_stats.json
│   └── historical_credentials.json
├── reports/                      ← SOC report archive (Tool 32)
│   ├── daily/
│   ├── weekly/
│   └── monthly/
├── docs/
│   └── THIR_HA_Runbooks_v2.docx ← 6 recovery runbooks (RB-01 to RB-06)
├── css/thir.css                  ← Dashboard stylesheet
├── js/                           ← Dashboard modules
│   ├── data.js
│   ├── pipeline.js
│   ├── render.js
│   ├── map.js
│   └── main.js
├── index.html                    ← Live dashboard
├── CNAME                         ← thirha.aegispub.com
├── README.md
├── SETUP.md                      ← Oracle HA deployment guide
├── ARCHITECTURE.md               ← Two-node design reference
├── MIGRATION.md                  ← What changed from thir-live and why
├── CONTRIBUTING.md
├── SECURITY.md
├── DISCLAIMER.md
└── LICENSE
```

---

## Planned Roadmap

| Priority | Item | Tool |
|---|---|---|
| High | Tool 38 — structured rsync collector replacing shell cron | `tools/ha/` |
| High | Tool 39 — VM1 direct node health checker | `tools/ha/` |
| Medium | Tool 40 — HAProxy failover notifier | `tools/ha/` |
| Medium | Tool 00 — 59-day historical processor (before AWS retires) | `tools/ha/` |
| Medium | Tool 41 — HTTP honeypot Flask app on VM1:8080 | `tools/http_honeypot/` |
| Medium | Tool 42 — HTTP log parser → ir_cases format | `tools/http_honeypot/` |
| Low | cloudflared tunnel deployment on both VMs | Infrastructure |

---

## License

MIT — see [LICENSE](LICENSE)

## Disclaimer

Defensive security research only. See [DISCLAIMER.md](DISCLAIMER.md).

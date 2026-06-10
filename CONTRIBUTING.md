# Contributing to THIR-HA

Thanks for your interest in contributing to THIR-HA (Threat Hunter Intelligence Range-HAProxy).

## What We Welcome

- Bug fixes in pipeline tools (`tools/`)
- Dashboard (`index.html`) improvements — visualisation, accessibility, performance
- New TTP detection rules in `26_incident_timeline_live.py`
- False positive signal improvements in `29_false_positive_live.py`
- New YARA rules in `tools/yara_rules/` for Tool 33
- Improvements to credential analysis in `34_credential_extractor_live.py`
- Documentation improvements

## What We Don't Accept

- Changes that add offensive capabilities
- Hardcoded credentials or API keys of any kind
- Dependencies that require a paid license
- Changes that break the `go run` (no `go.mod`) design decision for Go tools
- External Python dependencies — all Python tools use stdlib only

## How to Contribute

1. **Fork** the repository
2. **Create a branch** from `oracle-ha` — `git checkout -b fix/your-fix-name`
3. **Make your changes** — keep commits focused and descriptive
4. **Test locally** if possible — run tools against a sample `cowrie.json`
5. **Open a Pull Request** targeting `oracle-ha` — describe what you changed and why

## Code Style

- **Go tools:** standard `gofmt` formatting, stdlib only (no external dependencies, no `go.mod`)
- **Python tools:** PEP 8, type hints where practical, no external dependencies beyond stdlib
- **pipeline.yml:** keep steps self-documenting with inline comments

## Testing Locally

Most pipeline tools can be tested without a live VM by pointing them at a sample Cowrie log:

```bash
# Tool 26 — parse a sample cowrie.json
python tools/26_incident_timeline_live.py \
  --input-glob "/path/to/sample_cowrie.json" \
  --output /tmp/ir_cases_test.json \
  --verbose

# Tool 27 — enrich a list of IPs (requires API keys)
go run tools/27_threat_intel_feeder_live.go \
  --input /tmp/test_ips.txt \
  --output /tmp/threat_ips_test.json \
  -v
```

## Port Note

The admin SSH port on both Oracle VMs is **22222** — not 22.

- **VM1 (sensor):** Port 22 on VM1 redirects to Cowrie port 2222 via iptables. Always use port 22222 for admin access to VM1.
- **VM2 (brain):** Port 22 on VM2 is unused. Admin access is port 22222 only.
- **GitHub Actions** SSHes to VM2 port 22222 only — VM1 is never directly accessed by the pipeline.

If you're testing SSH access or SCP commands locally, always specify `-p 22222`.

## Reporting Issues

Open a GitHub Issue with:
- What you expected to happen
- What actually happened
- Relevant log output from GitHub Actions (redact any sensitive data, especially IP addresses and API keys)

## Security Issues

Do **not** open a public issue for security vulnerabilities. Contact the repository owner directly via GitHub or open a Security Advisory (Repository → Security → Advisories).

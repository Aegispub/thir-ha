#!/usr/bin/env python3
"""
Static checks on .github/workflows/historical_processor.yml and its test
workflow. These guard the invariants that make a failed run safe to re-run
and keep secrets/side effects where they belong. They parse the YAML; they do
not execute it.

Needs PyYAML (installed by test_historical_processor.yml). If PyYAML is not
available the test SKIPs (exit 0) so it never breaks a bare-Python run.
"""
import os, re, subprocess, sys

try:
    import yaml
except ImportError:
    print("SKIP  PyYAML not installed")
    sys.exit(0)

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
WF = os.path.join(ROOT, ".github", "workflows")
FAILS = []


def check(cond, label):
    print(f"{'PASS' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILS.append(label)


def load(name):
    with open(os.path.join(WF, name), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def steps_of(job):
    return job.get("steps", [])


def idx(steps, name):
    for i, s in enumerate(steps):
        if s.get("name") == name:
            return i
    return -1


def main():
    wf = load("historical_processor.yml")
    on = wf.get(True, wf.get("on"))          # PyYAML parses bare `on:` as boolean True
    proc = wf["jobs"]["process"]
    st = steps_of(proc)
    by = {s.get("name"): s for s in st}

    # --- triggers / safety envelope
    check("schedule" in on and "workflow_dispatch" in on, "has schedule + manual dispatch")
    check(wf.get("permissions", {}).get("contents") == "write", "contents: write (only permission)")
    check(set(wf.get("permissions", {})) == {"contents"}, "no other permissions granted")
    check(bool(wf.get("concurrency", {}).get("group")) and wf["concurrency"].get("cancel-in-progress") is False,
          "own concurrency group, never cancels a running job")
    check(isinstance(proc.get("timeout-minutes"), int), "process job has timeout-minutes")
    check(proc["strategy"].get("max-parallel") == 1, "corpora run one after the other (no git push race)")
    check("fromJSON" in str(proc["strategy"]["matrix"]), "matrix comes from the plan job")
    check(proc["strategy"].get("fail-fast") is False, "one corpus failing does not cancel the other")

    # --- Tool 00 invocation
    tool = by.get("Run Tool 00", {})
    run = tool.get("run", "")
    for flag in ("--incremental", "--state-dir", "--spill-dir", "--full-records-out",
                 "--current-listing", "--corpus-name", "--output-dir", "--log-dir"):
        check(flag in run, f"Tool 00 invoked with {flag}")
    check(isinstance(tool.get("timeout-minutes"), int), "Tool 00 step has its own timeout")
    check("--check-eof" not in run, "no .EOF-based skipping (per-file manifest is the watermark)")
    check(".EOF" not in yaml.dump(wf), "workflow does not depend on .EOF markers")

    # --- order of side effects
    a = idx(st, "Upload full-record archive to R2")
    c = idx(st, "Commit and push historical_data")
    s = idx(st, "Upload state to R2")
    check(-1 not in (a, c, s) and a < c < s, "order: archive upload < git push < state upload")
    for nm in ("Upload full-record archive to R2", "Commit and push historical_data", "Upload state to R2"):
        check("inputs.dry_run != true" in str(by[nm].get("if", "")), f"'{nm}' honours dry_run")

    # --- state upload: manifest last
    su = by["Upload state to R2"]["run"]
    first = su.find('--exclude "manifest.json"')
    last = su.rfind("manifest.json")
    check(first != -1 and last > first and su.count("manifest.json") >= 2,
          "state upload copies manifest.json last (it is the watermark)")
    check('--exclude "spill/**"' in su, "spill directory is never uploaded")

    # --- archive upload verifies name AND size
    au = by["Upload full-record archive to R2"]["run"]
    check("stat -c %s" in au and "--format" in au, "archive upload verifies remote size, not just exit code")

    # --- push retry
    cp = by["Commit and push historical_data"]["run"]
    check("git rebase" in cp and "for i in" in cp, "git push rebases and retries")

    # --- listing / download hygiene
    check("--files-only" in by["List raw logs in R2"]["run"], "bucket listing uses --files-only")
    check("--files-from" in by["Download needed raw logs"]["run"], "downloads only the planned files")
    check(by["Download needed raw logs"]["run"].count("-ne") >= 1, "download count is verified")

    # --- secrets only at job env level
    for sname, step in by.items():
        body = yaml.dump({k: v for k, v in step.items() if k != "name"})
        check("secrets." not in body, f"no secrets referenced in step '{sname}'")
    check("secrets." in yaml.dump(proc.get("env", {})), "secrets are mapped in job env only")
    check("echo ${R2_SECRET_KEY}" not in str(wf) and "echo \"${R2_SECRET_KEY}" not in str(wf),
          "secret values are never echoed")

    # --- every run block is valid bash
    ok = True
    for job in wf["jobs"].values():
        for step in steps_of(job):
            if "run" in step:
                txt = re.sub(r"\$\{\{[^}]*\}\}", "0", step["run"])
                if subprocess.run(["bash", "-n"], input=txt, text=True, capture_output=True).returncode:
                    ok = False
                    print("   bad bash in:", step.get("name") or step.get("id"))
    check(ok, "all run blocks pass bash -n")

    # --- the test workflow covers what this one relies on
    tw = load("test_historical_processor.yml")
    twt = yaml.dump(tw)
    for needle in ("tests/historical", "test_tool00_incremental.py", "test_tool00_spill.py",
                   "test_workflow_historical.py"):
        check(needle in twt, f"test workflow runs {needle}")
    check(not any("rclone" in str(s.get("run", "")) for j in tw["jobs"].values() for s in steps_of(j)),
          "test workflow needs no R2/rclone")
    check(tw.get("permissions") == {"contents": "read"}, "test workflow is read-only")

    if FAILS:
        print(f"\n{len(FAILS)} FAILED"); sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()

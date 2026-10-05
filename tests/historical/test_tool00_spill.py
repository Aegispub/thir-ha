#!/usr/bin/env python3
"""
Tool 00 --spill-dir regression test.

  1. In-memory and spill runs over the same synthetic corpus must produce
     byte-identical outputs (full-record archive, corpus_highlights,
     historical_stats, corpus_metadata) after normalising timestamps/paths.
  2. The spill run's peak memory (child ru_maxrss) must be well below the
     in-memory run's: the point of spilling.
  3. The spill file must be removed when the run ends.

Standard library only. Temp dir only. No network. Exit 0 = pass.
"""
import os, resource, re, shutil, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from test_tool00_incremental import make_corpus, TOOL, OUTS   # noqa: E402

MAX_RATIO = 0.70      # spill peak must be < 70% of in-memory peak
FAILS = []


def check(cond, label):
    print(f"{'PASS' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILS.append(label)


def run(logdir, out, extra=()):
    os.makedirs(out, exist_ok=True)
    t = time.time()
    r = subprocess.run([sys.executable, TOOL, "--log-dir", logdir, "--output-dir", out,
                        "--corpus-name", "sp", "--full-records-out", os.path.join(out, "full.json"), *extra],
                       capture_output=True, text=True)
    return r, time.time() - t


def norm(b, out):
    b = re.sub(rb'("(?:generated_at|processed_at)": )"[^"]*"', rb'\1"X"', b)
    return b.replace(out.encode(), b"OUT")


def main():
    tmp = tempfile.mkdtemp(prefix="tool00_spill_")
    try:
        src = os.path.join(tmp, "logs"); os.makedirs(src)
        make_corpus(src, days=7, sessions=25000, seed=5)
        spill_dir = os.path.join(tmp, "spill")
        o_s, o_m = os.path.join(tmp, "o_spill"), os.path.join(tmp, "o_mem")

        r_s, t_s = run(src, o_s, ("--spill-dir", spill_dir))
        peak_s = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024
        r_m, t_m = run(src, o_m)
        peak_m = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024   # max over both
        check(r_s.returncode == 0 and r_m.returncode == 0, "both runs exit 0")
        for n in OUTS:
            same = norm(open(os.path.join(o_s, n), "rb").read(), o_s) == \
                   norm(open(os.path.join(o_m, n), "rb").read(), o_m)
            check(same, f"spill == in-memory: {n}")
        print(f"      peak memory: spill {peak_s:.0f} MB, in-memory {peak_m:.0f} MB "
              f"({t_s:.1f}s vs {t_m:.1f}s)")
        check(peak_s < MAX_RATIO * peak_m, f"spill peak < {int(MAX_RATIO*100)}% of in-memory peak")
        left = [f for f in os.listdir(spill_dir)] if os.path.isdir(spill_dir) else []
        check(not left, "spill file removed after the run")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if FAILS:
        print(f"\n{len(FAILS)} FAILED"); sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()

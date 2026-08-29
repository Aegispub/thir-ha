#!/usr/bin/env python3
"""
Shared R2 monthly-archival helper for the enriched corpus tool set
(Tools 43, 44, 47, 48, and the Fingerprint/Infrastructure corpora).

Not a pipeline tool in its own right -- imported by each corpus builder,
or invoked standalone with --corpus-file / --r2-remote / --r2-bucket-path
from the pipeline.yml monthly step.

Reuses the exact pattern already proven working in
.github/workflows/historical_processor.yml (Oracle corpus upload block):
  1. gzip -k the corpus file (keep the original, compress a copy)
  2. rclone copyto with --retries 5 --low-level-retries 10
  3. Verify via `rclone lsf <dest-dir> | grep -Fxq <filename>` -- rclone's
     exit code alone is not treated as sufficient proof of a landed upload,
     matching the existing Oracle corpus upload discipline exactly.
  4. Hard-fail (non-zero exit) if verification fails, so the calling
     pipeline step fails cleanly rather than silently proceeding as if
     the archive succeeded.

Uses the SAME r2-oracle rclone remote and thirha-raw-archive bucket
already configured in historical_processor.yml -- no new remote, no new
bucket, no new secrets. Per the original design doc (Section 6): all
seven corpus R2 paths reuse the existing ORACLE_R2_* secrets and
r2-oracle rclone remote.
"""

import gzip
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


class R2UploadError(Exception):
    pass


def gzip_file(src_path: Path) -> Path:
    """gzip -k equivalent -- keeps the original, writes src_path + '.gz'"""
    gz_path = Path(str(src_path) + ".gz")
    with open(src_path, "rb") as f_in, gzip.open(gz_path, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    return gz_path


def upload_and_verify(
    local_gz_path: Path,
    remote: str,
    bucket_path: str,
    filename: str,
    retries: int = 5,
    low_level_retries: int = 10,
) -> None:
    """
    Uploads local_gz_path to {remote}:{bucket_path}/{filename}, then
    verifies via `rclone lsf` -- same two-step discipline as the existing
    Oracle historical corpus upload. Raises R2UploadError on any failure,
    including a "successful" copyto whose file cannot subsequently be
    listed at the destination.
    """
    dest = f"{remote}:{bucket_path}"

    copy_cmd = [
        "rclone", "copyto", str(local_gz_path),
        f"{dest}/{filename}",
        "--retries", str(retries),
        "--low-level-retries", str(low_level_retries),
    ]
    try:
        result = subprocess.run(copy_cmd, capture_output=True, text=True)
    except FileNotFoundError:
        raise R2UploadError(
            "rclone binary not found on PATH -- cannot archive to R2. "
            "This is expected in local/sandbox environments without rclone "
            "installed; the production runner (per historical_processor.yml's "
            "'Install rclone' step) installs it before this code path runs."
        )
    if result.returncode != 0:
        raise R2UploadError(
            f"rclone copyto failed (exit {result.returncode}): {result.stderr.strip()}"
        )

    list_cmd = ["rclone", "lsf", dest]
    try:
        list_result = subprocess.run(list_cmd, capture_output=True, text=True)
    except FileNotFoundError:
        raise R2UploadError("rclone binary not found on PATH -- cannot verify upload.")
    if list_result.returncode != 0:
        raise R2UploadError(
            f"rclone lsf verification failed (exit {list_result.returncode}): "
            f"{list_result.stderr.strip()}"
        )

    listed_files = set(line.strip() for line in list_result.stdout.splitlines())
    if filename not in listed_files:
        raise R2UploadError(
            f"{filename} not found in {dest} after upload — upload did not verify. "
            f"rclone copyto exit 0 is not treated as sufficient proof (matches "
            f"historical_processor.yml's Oracle corpus upload discipline)."
        )


def archive_corpus_to_r2(
    corpus_json_path: Path,
    corpus_name: str,
    remote: str = "r2-oracle",
    bucket: str = "thirha-raw-archive",
    now: datetime = None,
) -> str:
    """
    High-level entry point for a single corpus's monthly archival step.

    corpus_name is used both for the R2 subfolder (e.g. "actor-corpus")
    and the filename prefix (e.g. "actor_corpus_2026-08.json.gz"),
    matching the naming convention in the design doc's Section 6 R2
    structure table exactly.

    Returns the filename on success. Raises R2UploadError on failure --
    callers should let this propagate so the pipeline step fails loudly,
    consistent with the "abort the entire monthly prune" behaviour
    specified in the original design doc's Section 5.1 Step 3.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    if not corpus_json_path.exists():
        raise R2UploadError(f"{corpus_json_path} does not exist -- nothing to archive")

    gz_path = gzip_file(corpus_json_path)
    year_month = now.strftime("%Y-%m")
    filename = f"{corpus_name}_{year_month}.json.gz"
    bucket_path = f"{bucket}/{corpus_name}"

    upload_and_verify(gz_path, remote, bucket_path, filename)

    return filename


def main():
    """
    Standalone CLI use from a pipeline.yml monthly step, e.g.:

      python3 tools/r2_archive_helper.py \\
        data/enriched_corpus.json actor-corpus

    Mirrors the pattern already used for the Oracle historical corpus
    upload step, just parameterised per-corpus instead of hardcoded.
    """
    if len(sys.argv) < 3:
        print("Usage: r2_archive_helper.py <corpus_json_path> <corpus_name> [remote] [bucket]")
        sys.exit(2)

    corpus_path = Path(sys.argv[1])
    corpus_name = sys.argv[2]
    remote = sys.argv[3] if len(sys.argv) > 3 else "r2-oracle"
    bucket = sys.argv[4] if len(sys.argv) > 4 else "thirha-raw-archive"

    try:
        filename = archive_corpus_to_r2(corpus_path, corpus_name, remote, bucket)
        print(f"Verified {corpus_name} archive uploaded: {filename}")
    except R2UploadError as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

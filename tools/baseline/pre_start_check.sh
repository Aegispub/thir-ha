#!/bin/bash
# THIR — Cowrie Pre-Start Integrity Check
# /home/cowrie/cowrie/tools/pre_start_check.sh
#
# Run before any bin/cowrie restart to confirm the source tree
# matches the locked baseline. Exits non-zero on any failure.
#
# Usage:
#   bash /home/cowrie/cowrie/tools/pre_start_check.sh
#   bash /home/cowrie/cowrie/tools/pre_start_check.sh --vm2
#
# Revised per validation review June 29 2026:
#   - Uses sha256sum --check against baseline manifest file
#     instead of hardcoded hashes in the script itself
#   - Checks file ownership and permissions alongside hashes
#   - Handles missing files explicitly before attempting hash
#   - Uses git status to verify expected modification state
#   - Drops twistd hash (low value per validation)
#   - Adds requirements.txt hash (better virtualenv integrity signal)

set -uo pipefail

COWRIE_DIR="/home/cowrie/cowrie"
ERRORS=0
VM="vm1"

if [[ "${1:-}" == "--vm2" ]]; then
    VM="vm2"
fi

BASELINE_FILE="$(dirname "$0")/baseline_${VM}.sha256"

# ── Colour output ─────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
ok()   { echo -e "${GREEN}OK${NC}    $*"; }
fail() { echo -e "${RED}FAIL${NC}  $*"; ERRORS=$((ERRORS + 1)); }
warn() { echo -e "${YELLOW}WARN${NC}  $*"; }

echo "THIR Pre-Start Integrity Check — ${VM^^}"
echo "Baseline: $BASELINE_FILE"
echo "Time:     $(date -u)"
echo "──────────────────────────────────────────────"

# ── 1. Baseline file exists ───────────────────────────────────────────────
if [[ ! -f "$BASELINE_FILE" ]]; then
    fail "Baseline file not found: $BASELINE_FILE"
    echo "Cannot continue without baseline. Exiting."
    exit 1
fi

# Check for unfilled placeholders
PENDING=$(grep -c "LOCKED_AFTER_DEPLOY" "$BASELINE_FILE" | tr -d '[:space:]')
if [[ "$PENDING" -gt 0 ]]; then
    warn "$PENDING placeholder(s) not yet filled in baseline — run after July 8 deployment"
fi

# ── 2. File existence check (before hashing) ──────────────────────────────
echo ""
echo "── File existence ───────────────────────────────"
# Extract paths from non-comment, non-placeholder lines
while IFS= read -r line; do
    [[ "$line" =~ ^#   ]] && continue
    [[ -z "$line"       ]] && continue
    filepath=$(echo "$line" | awk '{print $2}')
    if [[ ! -f "$filepath" ]]; then
        fail "MISSING: $filepath"
    else
        ok "EXISTS:  $filepath"
    fi
done < "$BASELINE_FILE"

# ── 3. SHA256 hash verification ───────────────────────────────────────────
echo ""
echo "── SHA256 hashes ────────────────────────────────"
# Use sha256sum --check, suppressing OK lines, capturing failures
HASH_OUTPUT=$(sha256sum --check --ignore-missing "$BASELINE_FILE" 2>&1)
HASH_FAILS=$(echo "$HASH_OUTPUT" | grep -E "FAILED|WARNING|No such" || true)

if [[ -z "$HASH_FAILS" ]]; then
    ok "All hashes match baseline"
else
    while IFS= read -r line; do
        fail "$line"
    done <<< "$HASH_FAILS"
fi

# ── 4. Ownership and permissions check ───────────────────────────────────
echo ""
echo "── Ownership and permissions ────────────────────"

check_perms() {
    local filepath="$1"
    local expected_mode="$2"
    local expected_owner="$3"

    if [[ ! -f "$filepath" ]]; then
        warn "SKIP (missing): $filepath"
        return
    fi

    actual_mode=$(stat -c "%a" "$filepath")
    actual_owner=$(stat -c "%U:%G" "$filepath")

    if [[ "$actual_mode" != "$expected_mode" ]]; then
        fail "MODE $filepath — expected $expected_mode got $actual_mode"
    elif [[ "$actual_owner" != "$expected_owner" ]]; then
        fail "OWNER $filepath — expected $expected_owner got $actual_owner"
    else
        ok "$actual_mode $actual_owner $filepath"
    fi
}

# Plugin files — must be readable by cowrie user
check_perms "$COWRIE_DIR/src/cowrie/http/__init__.py"                     "644" "cowrie:cowrie"
check_perms "$COWRIE_DIR/src/cowrie/http/factory.py"                      "644" "cowrie:cowrie"
check_perms "$COWRIE_DIR/src/cowrie/http/honeypot.py"                     "644" "cowrie:cowrie"
check_perms "$COWRIE_DIR/src/twisted/plugins/cowrie_plugin.py"            "644" "cowrie:cowrie"
check_perms "$COWRIE_DIR/src/cowrie/core/output.py"                       "644" "cowrie:cowrie"
check_perms "$COWRIE_DIR/etc/cowrie.cfg"                                   "644" "cowrie:cowrie"

if [[ "$VM" == "vm2" ]]; then
    check_perms "/etc/haproxy/haproxy.cfg"                                 "644" "root:root"
    check_perms "/home/ubuntu/sync_to_r2.sh"                              "755" "ubuntu:ubuntu"
    check_perms "/home/ubuntu/rsync_from_vm1.sh"                          "755" "ubuntu:ubuntu"
fi

# ── 5. git status — expected modification state ───────────────────────────
echo ""
echo "── git status (source tree state) ──────────────"

cd "$COWRIE_DIR"

GIT_STATUS=$(sudo -u cowrie git status --short 2>/dev/null || git status --short 2>/dev/null)

# Before deployment: should be clean
# After deployment:  exactly two M lines and one ?? line
MODIFIED=$(echo "$GIT_STATUS" | grep -c "^ M" || true)
UNTRACKED=$(echo "$GIT_STATUS" | grep -c "^??" || true)
UNEXPECTED=$(echo "$GIT_STATUS" | grep -v "^ M\|^??" | grep -v "^$" || true)

if [[ -n "$UNEXPECTED" ]]; then
    fail "Unexpected git status entries:"
    while read -r l; do fail "  $l"; done < <(echo "$UNEXPECTED")
fi

# Check that cowrie_plugin.py and output.py are the M entries if plugin is deployed
PLUGIN_FILES_EXIST=false
if [[ -f "$COWRIE_DIR/src/cowrie/http/honeypot.py" ]]; then
    PLUGIN_FILES_EXIST=true
fi

if $PLUGIN_FILES_EXIST; then
    if echo "$GIT_STATUS" | grep -q "src/twisted/plugins/cowrie_plugin.py"; then
        ok "M  src/twisted/plugins/cowrie_plugin.py (expected — patched for HTTP plugin)"
    else
        warn "cowrie_plugin.py not showing as modified — patch may not have been applied"
    fi
    if echo "$GIT_STATUS" | grep -q "src/cowrie/core/output.py"; then
        ok "M  src/cowrie/core/output.py (expected — patched for HTTP protocol prefix)"
    else
        warn "output.py not showing as modified — patch may not have been applied"
    fi
    if echo "$GIT_STATUS" | grep -q "src/cowrie/http"; then
        ok "?? src/cowrie/http/ (expected — new untracked plugin directory)"
    else
        warn "src/cowrie/http/ not present in git status — plugin files may not be copied"
    fi
else
    if [[ "$GIT_STATUS" == "" ]]; then
        ok "Clean working tree (pre-deployment state — expected)"
    else
        echo "$GIT_STATUS" | while IFS= read -r line; do
            warn "Unexpected change: $line"
        done
    fi
fi

# ── 6. Port binding verification (post-Cowrie-start only) ─────────────────
echo ""
echo "── Port bindings ────────────────────────────────"

check_port() {
    local port="$1"
    local expected_bind="$2"
    local description="$3"
    if ss -tlnp | grep -q ":${port}"; then
        actual_bind=$(ss -tlnp | grep ":${port}" | awk '{print $4}' | head -1)
        if echo "$actual_bind" | grep -q "$expected_bind"; then
            ok "PORT $port ($description) — bound to $actual_bind"
        else
            fail "PORT $port ($description) — expected $expected_bind got $actual_bind"
        fi
    else
        warn "PORT $port ($description) — not listening (Cowrie may be stopped)"
    fi
}

if [[ "$VM" == "vm1" ]]; then
    check_port "2222"  "0.0.0.0" "Cowrie SSH — must be public"
    check_port "2323"  "0.0.0.0" "Cowrie telnet — must be public"
    check_port "22222" "0.0.0.0" "Admin SSH — must be public"
    check_port "8080"  "0.0.0.0" "HTTP honeypot — must be public after plugin deployment"
else
    check_port "2222"  "0.0.0.0"   "HAProxy SSH frontend — must be public"
    check_port "2223"  "0.0.0.0"   "HAProxy telnet frontend — must be public"
    check_port "22222" "0.0.0.0"   "Admin SSH — must be public"
    check_port "4222"  "127.0.0.1" "Cowrie SSH backup — must be localhost only"
    check_port "4223"  "127.0.0.1" "Cowrie telnet backup — must be localhost only"
    check_port "4323"  "127.0.0.1" "Cowrie telnet alt backup — must be localhost only"
    check_port "6415"  "127.0.0.1" "Cowrie pool port — must be localhost only"
    check_port "81"    "127.0.0.1" "HTTP honeypot standby — must be localhost only (post-July 8)"
fi

# ── 7. Summary ────────────────────────────────────────────────────────────
echo ""
echo "──────────────────────────────────────────────"
if [[ $ERRORS -eq 0 ]]; then
    echo -e "${GREEN}PRE-START CHECK PASSED — $VM is clear to restart Cowrie${NC}"
    exit 0
else
    echo -e "${RED}PRE-START CHECK FAILED — $ERRORS error(s) found${NC}"
    echo "Do not restart Cowrie until all failures are investigated."
    exit 1
fi

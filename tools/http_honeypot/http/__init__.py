# THIR — HTTP Honeypot Cowrie Plugin
# cowrie/http/__init__.py
#
# Version:      v3.2 — finalised June 29 2026
# Whitepaper:   THIR_HTTP_Honeypot_Cowrie_Plugin_Whitepaper_v3.2.md
# Gate:         July 8 2026
# Build status: FINAL — no stubs
#
# Module registration for the HTTP protocol plugin.
#
# Cowrie discovers output plugins dynamically (any [output_*] section).
# Protocol plugins (SSH, Telnet) are NOT dynamically discovered — they are
# wired explicitly in src/twisted/plugins/cowrie_plugin.py inside
# pool_ready(). Confirmed from VM1 source read June 29 2026.
# This module provides getFactory() which the pool_ready() wiring block
# calls. The [http] section in cowrie.cfg enables the plugin and specifies
# listen_endpoints; pool_ready() does the actual binding.
#
# Wiring location confirmed: pool_ready() — NOT create_endpoint_services().
# Server reference confirmed: factory.tac = self — NOT factory.server.
#
# Deploy path: copy this entire http/ directory to
#   /home/cowrie/cowrie/src/cowrie/http/
# Then apply the three manual edits in cowrie_plugin.py.patch to wire
# it into pool_ready() in src/twisted/plugins/cowrie_plugin.py.

from __future__ import annotations

from cowrie.http.factory import HTTPHoneypotFactory


def getFactory() -> HTTPHoneypotFactory:
    """Return the Twisted protocol factory for the HTTP honeypot.

    Called by the HTTP wiring block in cowrie_plugin.py when
    [http] enabled = true in cowrie.cfg. The factory is then
    bound to the listen_endpoints defined in that section.

    Returns a fresh factory instance each time — Cowrie's service
    loader holds the reference and injects the server object before
    the first connection arrives.
    """
    return HTTPHoneypotFactory()

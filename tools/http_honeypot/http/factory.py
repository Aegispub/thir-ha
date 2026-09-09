# THIR — HTTP Honeypot Cowrie Plugin
# cowrie/http/factory.py
#
# Version:      v3.1 — finalised June 29 2026
# Whitepaper:   Section 4.1, 4.2
# Gate:         July 8 2026
# Build status: FINAL — zero stubs remaining
#
# Source read: src/twisted/plugins/cowrie_plugin.py (VM1 June 29 2026)
# Confirmed:   server reference attribute is 'tac', not 'server'.
#              SSH:    factory.tac = self
#              Telnet: f.tac = self
#              HTTP:   factory.tac = self  ← matches this file
#
# Source read: src/cowrie/core/output.py (VM1 June 29 2026)
# Confirmed:   logDispatch() calls self.emit(ev) directly.
#              No factory attribute used by output.py — only the events
#              fired via logDispatch matter, not the factory attribute name.
#              The 'tac' attribute is only used by cowrie_plugin.py to
#              call pool_ready() and other lifecycle methods on the service
#              maker. HTTP plugin does not need those callbacks.
#
# The guard in honeypot.py uses:
#   channel.factory is None or channel.factory.tac is None
# Updated from 'server' to 'tac' to match confirmed source.

from __future__ import annotations

from typing import Any

from twisted.web import http

from cowrie.http.honeypot import HTTPHoneypotChannel


class HTTPHoneypotFactory(http.HTTPFactory):
    """Twisted protocol factory — one instance shared across all connections.

    Twisted calls buildProtocol() for each new TCP connection, producing
    one HTTPHoneypotChannel per connection.

    Attributes
    ----------
    tac : Any
        Reference to the CowrieServiceMaker instance injected by the HTTP
        wiring block in pool_ready(). Provides logDispatch() for event bus
        access via output plugin observers.
        Confirmed from cowrie_plugin.py: SSH uses factory.tac = self,
        Telnet uses f.tac = self. HTTP uses factory.tac = self.

    noisy : bool
        Suppresses Twisted's default per-connection log noise.
    """

    noisy = False

    def __init__(self) -> None:
        super().__init__()
        # Confirmed attribute name: 'tac' — matches SSH and Telnet factories.
        # Set by the pool_ready() wiring block in cowrie_plugin.py:
        #   factory.tac = self
        self.tac: Any = None

    def buildProtocol(self, addr: Any) -> HTTPHoneypotChannel:
        """Build and return a new protocol instance for each TCP connection.

        Explicitly sets channel.factory = self. Twisted's base
        http.HTTPFactory.buildProtocol() already does this, so the
        override is documentary — confirmed safe by external review.
        """
        channel = HTTPHoneypotChannel()
        channel.factory = self
        return channel

    def startFactory(self) -> None:
        """Called once when the factory begins accepting connections."""
        super().startFactory()

    def stopFactory(self) -> None:
        """Called once when the factory stops accepting connections."""
        super().stopFactory()

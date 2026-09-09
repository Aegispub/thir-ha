# ── INSERT AT END OF pool_ready() in cowrie_plugin.py ─────────────────────
#
# Paste this block at the very end of pool_ready(), after the Telnet block.
# Indentation is 8 spaces — matches the existing SSH and Telnet blocks.
#
# Prerequisites in cowrie_plugin.py (see cowrie_plugin.py.patch):
#   - import cowrie.http.factory           added at top of file
#   - self.enableHTTP = CowrieConfig...    added in __init__()
#   - get_endpoints_from_section           already imported from cowrie.core.utils
#   - create_endpoint_services             already imported from cowrie.core.utils
#   - reactor                              already imported from twisted.internet

        if self.enableHTTP:
            f = cowrie.http.factory.HTTPHoneypotFactory()
            f.tac = self
            listen_endpoints = get_endpoints_from_section(CowrieConfig, "http", 8080)
            create_endpoint_services(reactor, self.topService, listen_endpoints, f)

# THIR — HTTP Honeypot Cowrie Plugin
# cowrie/http/honeypot.py
#
# Version:      v3.1 — finalised June 29 2026
# Whitepaper:   Sections 4.2, 4.3, 4.4, 4.8, 4.9
# Gate:         July 8 2026
# Build status: FINAL — zero stubs remaining
#
# ── Source reads confirmed June 29 2026 ───────────────────────────────────
#
# src/twisted/plugins/cowrie_plugin.py
#   - Server reference attribute: 'tac' (not 'server')
#     SSH:    factory.tac = self
#     Telnet: f.tac = self
#     HTTP:   factory.tac = self  ← all guards updated below
#   - Wiring goes in pool_ready(), not create_endpoint_services()
#   - Helpers: get_endpoints_from_section(CowrieConfig, "http", 8080)
#              create_endpoint_services(reactor, self.topService, endpoints, factory)
#
# src/cowrie/core/output.py — emit() session tracking confirmed:
#
#   emit() has three branches for resolving sessionno:
#     1. "sessionno" in ev  → use it directly, register session on connect
#     2. "session"   in ev  → reverse-lookup in self.sessions (fails silently
#                              via StopIteration if not yet registered)
#     3. "system"    in ev  → extract S<n>/T<n> from Twisted log prefix
#
#   logDispatch() calls emit() directly with only the kwargs passed in.
#   No "system" key is added by logDispatch — so HTTP events via logDispatch
#   can only use branch 1 (explicit sessionno) or branch 2 (session lookup).
#
#   CRITICAL: cowrie.session.connect MUST use branch 1 (explicit sessionno)
#   because self.sessions is empty at connect time — branch 2 would hit
#   StopIteration and return silently, dropping the event and all subsequent
#   events for that session.
#
#   FIX: pass sessionno="H<counter>" explicitly in cowrie.session.connect.
#   Subsequent events pass only session=session_id and use branch 2, which
#   succeeds because the session is now registered in self.sessions.
#
#   output.py also sets ev["protocol"] based on sessionno prefix:
#     S → "ssh", T → "telnet", else → "unknown"
#   HTTP sessions use prefix "H" — output.py needs one line added to handle it.
#   See output.py.patch for that change.
#
# ── Session model ──────────────────────────────────────────────────────────
# Per-TCP-connection. One HTTPHoneypotChannel = one session UUID.
# Session numeric counter (_http_session_counter) is module-level so session
# numbers are globally unique across all concurrent HTTP connections,
# consistent with how SSH numbers its sessions.
#
# ── Event types fired ──────────────────────────────────────────────────────
#   cowrie.session.connect  — on connectionMade(), with explicit sessionno
#   http.request            — on every GET/POST, with session= for lookup
#   cowrie.login.failed     — on POST with credential fields
#   cowrie.session.closed   — on connectionLost(), with session= for lookup
#
# ── Extended header fields (v3.1, Section 4.9) ────────────────────────────
#   http_version, host, x_forwarded_for, referer,
#   authorization_present (bool), cookie_present (bool)
#
# ── Rate limiting ──────────────────────────────────────────────────────────
# None here. Scanner noise handled by per-IP deduplication in Tool 26
# (Section 5.5, threshold = 20 sessions/window).
#
# ── cowrie.session.file_download not fired ────────────────────────────────
# The HTTP plugin serves fake credential files (/.env, /config.json etc.)
# as response bodies. It does NOT fire cowrie.session.file_download because
# no files are downloaded TO the honeypot — they are served FROM it.
# Tool 31 (malware analyser) is triggered by file_download events in
# ir_cases.json. HTTP sessions will never trigger Tool 31.
# Tool 26's HTTP handler must not expect file_download events from HTTP
# sessions. This is correct behaviour, not a missing feature.

from __future__ import annotations

import itertools
import time
import uuid
from urllib.parse import parse_qs

from twisted.web import http

# ── Module-level session counter ─────────────────────────────────────────────
# Globally unique HTTP session numbers. Prefix "H" distinguishes HTTP
# sessions from SSH ("S") and Telnet ("T") in output.py's session map.
_http_counter = itertools.count(1)


def _next_sessionno() -> str:
    """Return the next HTTP session number string: H1, H2, H3 ..."""
    return f"H{next(_http_counter)}"


# ── Constants ────────────────────────────────────────────────────────────────

FAKE_SERVER: bytes = b"Apache/2.4.41 (Ubuntu)"

# TTP mapping: normalised path → MITRE ATT&CK technique ID.
# Catch-all maps to T1595.003. POST with credentials additionally maps to
# T1078 — handled in _handle_post via cowrie.login.failed eventid.
TTP_MAP: dict[str, str] = {
    # Credential file probing — T1552.001
    "/.env":                                        "T1552.001",
    "/config.json":                                 "T1552.001",
    "/.git/config":                                 "T1552.001",
    "/actuator/env":                                "T1552.001",
    # Cloud instance metadata — T1552.005
    "/latest/meta-data/":                           "T1552.005",
    "/latest/meta-data/iam/security-credentials/":  "T1552.005",
    "/opc/v1/instance/":                            "T1552.005",
    # Exploit public-facing application — T1190
    "/actuator/health":                             "T1190",
    "/admin":                                       "T1190",
    "/login":                                       "T1190",
    "/wp-admin/":                                   "T1190",
    "/wp-login.php":                                "T1190",
    "/phpmyadmin/":                                 "T1190",
    "/manager/html":                                "T1190",
    # File and directory discovery — T1083
    "/actuator/mappings":                           "T1083",
    "/api/v1/":                                     "T1083",
    "/api/v1/users":                                "T1083",
    "/backup.zip":                                  "T1083",
    "/dump.sql":                                    "T1083",
    # Scanner / liveness probes — T1595.003
    "/health":                                      "T1595.003",
    "/status":                                      "T1595.003",
    "/robots.txt":                                  "T1595.003",
}

# Route table: normalised path → (status_code, content_type, body_string).
FAKE_RESPONSES: dict[str, tuple[int, str, str]] = {

    # ── Credential files (T1552.001) ─────────────────────────────────────

    "/.env": (200, "text/plain", (
        "APP_ENV=production\n"
        "APP_KEY=base64:kJ7sP2mXnQ4rT8vY1wZ0uI3oL6hE9dF5gA2bC\n"
        "DB_CONNECTION=mysql\n"
        "DB_HOST=127.0.0.1\n"
        "DB_PORT=3306\n"
        "DB_DATABASE=app_production\n"
        "DB_USERNAME=app_user\n"
        "DB_PASSWORD=Xk9#mP2$vL7nQ4rT\n"
        "AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE\n"
        "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\n"
        "AWS_DEFAULT_REGION=us-east-1\n"
        "REDIS_PASSWORD=rP8kM3nX7qT2vY5w\n"
        "MAIL_PASSWORD=smtp_secret_2026\n"
    )),

    "/config.json": (200, "application/json", (
        '{"database":{"host":"127.0.0.1","port":3306,"name":"app_db",'
        '"user":"admin","password":"Db#P4ssw0rd!2026"},'
        '"api":{"key":"sk_live_4xK9mP2vL7nQ3rT8wY1z","secret":"api_secret_Xk9mP2vL"},'
        '"redis":{"host":"127.0.0.1","port":6379,"password":"rP8kM3nX"},'
        '"s3":{"bucket":"app-assets-prod","region":"us-east-1",'
        '"access_key":"AKIAIOSFODNN7EXAMPLE",'
        '"secret_key":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}}'
    )),

    "/.git/config": (200, "text/plain", (
        "[core]\n"
        "\trepositoryformatversion = 0\n"
        "\tfilemode = true\n"
        "\tbare = false\n"
        "[remote \"origin\"]\n"
        "\turl = https://deploy:ghp_Xk9mP2vL7nQ4rT8wY1zI3oL6hE9dF5"
        "@github.com/internal/app.git\n"
        "\tfetch = +refs/heads/*:refs/remotes/origin/*\n"
        "[branch \"main\"]\n"
        "\tremote = origin\n"
        "\tmerge = refs/heads/main\n"
    )),

    "/actuator/env": (200, "application/json", (
        '{"activeProfiles":["production"],'
        '"propertySources":[{"name":"applicationConfig",'
        '"properties":{"spring.datasource.password":{"value":"Sp$R1ngP4ss!"},'
        '"spring.datasource.username":{"value":"root"},'
        '"spring.datasource.url":{"value":"jdbc:mysql://127.0.0.1:3306/spring_db"},'
        '"management.security.enabled":{"value":"false"}}}]}'
    )),

    # ── Cloud metadata (T1552.005) ────────────────────────────────────────

    "/latest/meta-data/": (200, "text/plain", (
        "ami-id\nami-launch-index\nami-manifest-path\n"
        "hostname\niam/\ninstance-action\ninstance-id\n"
        "instance-type\nlocal-hostname\nlocal-ipv4\n"
        "mac\nnetwork/\nplacement/\npublic-hostname\n"
        "public-ipv4\npublic-keys/\nreservation-id\nsecurity-groups\n"
    )),

    "/latest/meta-data/iam/security-credentials/": (200, "text/plain",
        "app-ec2-role\n"
    ),

    "/opc/v1/instance/": (200, "application/json", (
        '{"availabilityDomain":"AD-1",'
        '"compartmentId":"ocid1.compartment.oc1..aaaaaaaafake",'
        '"displayName":"production-server-01",'
        '"id":"ocid1.instance.oc1.ap-sydney-1.fake",'
        '"image":"Oracle-Linux-8.9",'
        '"region":"ap-sydney-1",'
        '"shape":"VM.Standard.E4.Flex"}'
    )),

    # ── Spring Boot actuator (T1190) ──────────────────────────────────────

    "/actuator/health":   (200, "application/json", '{"status":"UP"}'),

    "/actuator/mappings": (200, "application/json", (
        '{"contexts":{"application":{"mappings":{"dispatcherServlets":{'
        '"dispatcherServlet":[{"handler":"GET /api/v1/users",'
        '"predicate":"/api/v1/users"},'
        '{"handler":"POST /api/v1/auth","predicate":"/api/v1/auth"},'
        '{"handler":"GET /admin/dashboard","predicate":"/admin/dashboard"},'
        '{"handler":"DELETE /api/v1/users/{id}",'
        '"predicate":"/api/v1/users/{id}"}]}}}}}'
    )),

    # ── API discovery (T1083) ─────────────────────────────────────────────

    "/api/v1/": (200, "application/json", (
        '{"version":"1.0","endpoints":['
        '"/api/v1/users","/api/v1/auth","/api/v1/products",'
        '"/api/v1/orders","/api/v1/admin/config"]}'
    )),

    "/api/v1/users": (200, "application/json", (
        '{"users":['
        '{"id":1,"email":"admin@internal.local","role":"admin"},'
        '{"id":2,"email":"deploy@internal.local","role":"deployer"},'
        '{"id":3,"email":"monitor@internal.local","role":"readonly"}]}'
    )),

    # ── Admin / login panels (T1190 / T1078) ─────────────────────────────

    "/admin": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>Admin Login</title></head><body>"
        "<h2>Administration Panel</h2>"
        "<form method='POST' action='/admin'>"
        "<input name='username' placeholder='Username'><br>"
        "<input name='password' type='password' placeholder='Password'><br>"
        "<button type='submit'>Login</button>"
        "</form></body></html>"
    )),

    "/login": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>Login</title></head><body>"
        "<form method='POST' action='/login'>"
        "<input name='username' placeholder='Username'><br>"
        "<input name='password' type='password' placeholder='Password'><br>"
        "<button type='submit'>Sign In</button>"
        "</form></body></html>"
    )),

    "/wp-admin/": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>WordPress &#8250; Log In</title></head><body>"
        "<div id='login'>"
        "<form name='loginform' method='post' action='/wp-login.php'>"
        "<p><label>Username<br>"
        "<input type='text' name='log' size='20'></label></p>"
        "<p><label>Password<br>"
        "<input type='password' name='pwd' size='20'></label></p>"
        "<p><input type='submit' value='Log In'></p>"
        "</form></div></body></html>"
    )),

    "/wp-login.php": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>WordPress &#8250; Log In</title></head><body>"
        "<div id='login'>"
        "<form name='loginform' method='post' action='/wp-login.php'>"
        "<p><label>Username or Email Address<br>"
        "<input type='text' name='log' size='20'></label></p>"
        "<p><label>Password<br>"
        "<input type='password' name='pwd' size='20'></label></p>"
        "<p><input type='submit' name='wp-submit' value='Log In'></p>"
        "</form></div></body></html>"
    )),

    "/phpmyadmin/": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>phpMyAdmin</title></head><body>"
        "<div class='login_form'>"
        "<form method='POST' action='/phpmyadmin/index.php'>"
        "<input name='pma_username' placeholder='Username'><br>"
        "<input name='pma_password' type='password' placeholder='Password'><br>"
        "<select name='server'><option value='1'>127.0.0.1</option></select><br>"
        "<button type='submit'>Go</button>"
        "</form></div></body></html>"
    )),

    "/manager/html": (200, "text/html", (
        "<!DOCTYPE html><html><head><title>Tomcat Web Application Manager</title></head><body>"
        "<h3>Tomcat Web Application Manager</h3>"
        "<p>Please sign in to manage applications.</p>"
        "<form method='POST' action='/manager/html'>"
        "<input name='username' placeholder='Username'><br>"
        "<input name='password' type='password' placeholder='Password'><br>"
        "<input type='submit' value='Login'>"
        "</form></body></html>"
    )),

    # ── High-signal 404s (T1083) ─────────────────────────────────────────

    "/backup.zip": (404, "text/plain", "Not Found"),
    "/dump.sql":   (404, "text/plain", "Not Found"),

    # ── Scanner / health probes (T1595.003) ──────────────────────────────

    "/health":  (200, "application/json", '{"status":"ok"}'),
    "/status":  (200, "application/json", '{"status":"running"}'),

    "/robots.txt": (200, "text/plain", (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Disallow: /config/\n"
        "Disallow: /backup/\n"
        "Disallow: /.env\n"
        "Disallow: /api/internal/\n"
        "Disallow: /wp-admin/\n"
        "Disallow: /phpmyadmin/\n"
    )),
}

# POST credential field names by route.
# cowrie.login.failed is reused — Tool 34 captures HTTP credential spray
# with zero code changes.
POST_CREDENTIAL_FIELDS: dict[str, tuple[str, str]] = {
    "/admin":        ("username",    "password"),
    "/login":        ("username",    "password"),
    "/wp-login.php": ("log",         "pwd"),
    "/phpmyadmin/":  ("pma_username","pma_password"),
    "/manager/html": ("username",    "password"),
}


# ── Protocol classes ─────────────────────────────────────────────────────────

class HTTPHoneypotRequest(http.Request):
    """One instance per HTTP request.

    Twisted parses all headers before calling process(). By the time
    process() runs, self.method, self.path, self.clientproto, and all
    request headers are fully available.
    """

    def process(self) -> None:
        """Handle one HTTP request end-to-end.

        finish() is always in a finally block — without it, TCP sockets
        stay open until client timeout, exhausting file descriptors under
        sustained scanner load.
        """
        try:
            raw_path: str = self.path.decode("utf-8", errors="ignore")
            path: str = raw_path.split("?")[0]  # strip query string for route lookup

            self._fire_request_event(path, raw_path)

            if self.method == b"POST":
                self._handle_post(path)

            status, ctype, body = FAKE_RESPONSES.get(
                path, (404, "text/plain", "Not Found")
            )
            self.setResponseCode(status)
            self.setHeader(b"Content-Type", ctype.encode())
            self.setHeader(b"Server", FAKE_SERVER)
            self.write(body.encode("utf-8"))

        except Exception:
            self.setResponseCode(500)
            self.write(b"")

        finally:
            self.finish()

    # ── Event helpers ────────────────────────────────────────────────────

    def _fire_request_event(self, path: str, raw_path: str) -> None:
        """Fire http.request with extended header schema (Section 4.9).

        Uses session= (not sessionno=) so output.py uses branch 2 (reverse
        lookup). This works because cowrie.session.connect already registered
        this session_id in self.sessions via branch 1 (explicit sessionno).

        Authorization and Cookie VALUES are never logged — boolean presence only.
        """
        channel: HTTPHoneypotChannel = self.channel
        if channel.factory is None or channel.factory.tac is None:
            return

        def _hdr(name: bytes) -> str:
            val = self.getHeader(name)
            if val is None:
                return ""
            return val.decode("utf-8", errors="ignore") if isinstance(val, bytes) else str(val)

        for output in channel.factory.tac.output_plugins:
            output.logDispatch(
                eventid="http.request",
                # Connection context
                src_ip=channel.peer_addr[0],
                src_port=channel.peer_addr[1],
                dst_port=channel.dst_port,
                session=channel.session_id,
                protocol="http",
                # HTTP metadata
                http_version=self.clientproto.decode("utf-8", errors="ignore"),
                method=self.method.decode("utf-8", errors="ignore"),
                path=path,
                raw_path=raw_path,
                # Extended headers (v3.1 Section 4.9)
                user_agent=_hdr(b"user-agent"),
                host=_hdr(b"host"),
                x_forwarded_for=_hdr(b"x-forwarded-for"),
                referer=_hdr(b"referer"),
                authorization_present=self.getHeader(b"authorization") is not None,
                cookie_present=self.getHeader(b"cookie") is not None,
                # TTP
                ttp=TTP_MAP.get(path, "T1595.003"),
                # Required by output.py emit() — without one of these the event is dropped
                format="HTTP %(method)s %(path)s from %(src_ip)s",
            )

    def _handle_post(self, path: str) -> None:
        """Parse POST body and fire cowrie.login.failed for credential routes.

        Only fires when both username and password fields are non-empty.
        Empty-field POSTs (scanner probes without real credentials) are skipped.
        """
        channel: HTTPHoneypotChannel = self.channel
        if channel.factory is None or channel.factory.tac is None:
            return
        if path not in POST_CREDENTIAL_FIELDS:
            return

        username_field, password_field = POST_CREDENTIAL_FIELDS[path]

        try:
            self.content.seek(0)
            body_bytes = self.content.read()
            params = parse_qs(body_bytes.decode("utf-8", errors="ignore"))
        except Exception:
            return

        username = params.get(username_field, [""])[0].strip()
        password = params.get(password_field, [""])[0]

        if not username and not password:
            return

        for output in channel.factory.tac.output_plugins:
            output.logDispatch(
                eventid="cowrie.login.failed",
                username=username,
                password=password,
                src_ip=channel.peer_addr[0],
                session=channel.session_id,
                protocol="http",
                format="HTTP login attempt %(username)s/%(password)s from %(src_ip)s",
            )


class HTTPHoneypotChannel(http.HTTPChannel):
    """One instance per TCP connection.

    Owns session-level state: session_id (UUID hex), sessionno (H<n>),
    peer_addr, dst_port, start_time.

    Session model: per-TCP-connection (Section 4.8).
    """

    requestFactory = HTTPHoneypotRequest

    def __init__(self) -> None:
        super().__init__()
        self.session_id: str = ""
        self.sessionno: str = ""       # "H<n>" — used in cowrie.session.connect
        self.peer_addr: tuple[str, int] = ("", 0)
        self.dst_port: int = 80
        self._start_time: float = 0.0

    def connectionMade(self) -> None:
        """Assign session state and fire cowrie.session.connect.

        MUST pass sessionno= explicitly. output.py emit() registers the
        session in self.sessions only when processing cowrie.session.connect
        via the 'sessionno in ev' branch (branch 1). Without an explicit
        sessionno, emit() hits branch 2 (reverse lookup), finds nothing,
        raises StopIteration, and silently drops the event — along with
        every subsequent event for this session.
        """
        super().connectionMade()

        self.session_id = uuid.uuid4().hex
        self.sessionno  = _next_sessionno()        # "H1", "H2", ...
        self._start_time = time.time()

        peer = self.transport.getPeer()
        self.peer_addr = (peer.host, peer.port)

        host = self.transport.getHost()
        if hasattr(host, "port"):
            self.dst_port = host.port

        self._fire_connect()

    def connectionLost(self, reason) -> None:
        """Fire cowrie.session.closed and release session state."""
        self._fire_closed()
        super().connectionLost(reason)

    # ── Session event helpers ─────────────────────────────────────────────

    def _fire_connect(self) -> None:
        """Fire cowrie.session.connect with explicit sessionno.

        Branch 1 in output.py emit():
          'sessionno' in ev → use directly, register in self.sessions
        After this call, self.sessions[self.sessionno] == self.session_id
        and subsequent events can use session= for reverse lookup.
        """
        if self.factory is None or self.factory.tac is None:
            return

        for output in self.factory.tac.output_plugins:
            output.logDispatch(
                eventid="cowrie.session.connect",
                sessionno=self.sessionno,    # explicit — triggers branch 1
                session=self.session_id,
                src_ip=self.peer_addr[0],
                src_port=self.peer_addr[1],
                dst_port=self.dst_port,
                protocol="http",
                format="New HTTP connection from %(src_ip)s",
            )

    def _fire_closed(self) -> None:
        """Fire cowrie.session.closed.

        Uses session= (branch 2) — safe here because connect already
        registered the session. output.py cleans up self.sessions and
        self.ips after processing cowrie.session.closed.
        """
        if self.factory is None or self.factory.tac is None:
            return

        duration = round(time.time() - self._start_time, 3)

        for output in self.factory.tac.output_plugins:
            output.logDispatch(
                eventid="cowrie.session.closed",
                session=self.session_id,
                duration=duration,
                protocol="http",
                format="HTTP session closed after %(duration)ss",
            )

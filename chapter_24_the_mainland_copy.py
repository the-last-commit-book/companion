# chapter_24_the_mainland_copy.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 24: The Mainland Copy

import json
import threading
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import ThreadingHTTPServer

# Marcus's cloud audit log lives on the mainland, off the island, beyond the
# reach of anyone at Raven House. To keep this chapter runnable on one machine,
# we start that mainland service locally, in the background, and then talk to it
# over HTTP exactly the way you would talk to a real cloud API.
from audit_api_server import AuditHandler, READ_TOKEN

server = ThreadingHTTPServer(("127.0.0.1", 0), AuditHandler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()

BASE_URL = f"http://127.0.0.1:{port}"
DEATH_UTC = datetime(2025, 10, 14, 4, 17, tzinfo=timezone.utc)  # 00:17 Maine local


def get(path, token):
    request = urllib.request.Request(BASE_URL + path)
    request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return response.status, json.loads(response.read().decode("utf-8"))


print("Querying the Glasshouse cloud audit API")
print()

# A real API refuses strangers. Prove it, so the evidence is trusted.
try:
    get("/audit", "WRONG-TOKEN")
except urllib.error.HTTPError as error:
    print("Request with a bad token ->", error.code, error.reason)

status, audit = get("/audit", READ_TOKEN)
print("Request with the evidence token ->", status, "OK")
print()

status, registry = get("/tokens", READ_TOKEN)
tokens = registry["tokens"]

events = audit["events"]
print("Audit events retrieved:", len(events))
print("Time of death (UTC):", DEATH_UTC.strftime("%Y-%m-%d %H:%M %Z"))
print()

impossible = []
for event in events:
    when = datetime.fromisoformat(event["timestamp_utc"].replace("Z", "+00:00"))
    token = tokens.get(event["actor_token"], {})
    claimed_marcus = event["principal_claimed"].startswith("marcus.thorne")
    is_service = token.get("type") == "service"

    if when > DEATH_UTC and claimed_marcus and is_service:
        impossible.append((event, token))

print("Events acting as Marcus Thorne after his death:")
for event, token in impossible:
    print(" ", event["timestamp_utc"], event["action"])
    print("     token:", event["actor_token"], "owned by", token["owner"], "(" + token["type"] + ")")
    print("     source IP:", event["source_ip"], "(Raven Island subnet)")

print()
print("Impossible-actor events:", len(impossible))
print("Clue: after Marcus died, a security service token impersonated him")
print("from the island and pushed a rewritten repository history to the cloud.")
print("The cloud log is off the island. No one at Raven House could edit it.")

server.shutdown()

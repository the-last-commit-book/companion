# Exercise Solutions

Worked answers for the **Your Turn** exercises at the end of each chapter of *The Last Commit: Learn Python by Solving a Murder Mystery*.

Solutions are intentionally brief. If your code differs but the output agrees, your code is correct — there is more than one honest way to ask a file a question.

---

Solutions are intentionally brief. If your code differs but the output agrees, your code is correct; there is more than one honest way to ask a file a question.

### Chapter 1

1. `total_devices = registered_devices + staff_devices` then `print("All devices seen:", total_devices)` -- prints 11.
2. `unexplained_devices` becomes 0. The clue was never the seven; it was the disagreement between two counts.
Stretch: `print("Expected", invited_guests, "devices but found", registered_devices)`.

### Chapter 2

1. `registered_devices[-1]` -- negative indexes count from the end.
2. `i = registered_devices.index("VOLKOV-SECURE")` then `print(device_owners[i], device_locations[i])`.
Stretch: the *last* device changes to `UNKNOWN-WATCH`; index 6 still returns `HARTLEY-PRIVATE`. Position and meaning are different things.

### Chapter 3

1. `vendor_message[1:17]` gives `2025-10-12 18:44`.
2. `pos = whitmore_message_body.find("vendor")` then `print(whitmore_message_body[pos:])`.
Stretch: lowercase before searching -- `.lower()` -- because `find()` is case-sensitive and witnesses are not.

### Chapter 4

1. `print(motive_categories["Daniel Thorne"], "|", declared_alibis["Daniel Thorne"])`.
2. Build the dictionary, then loop: `for name in interviewed:` / `if not interviewed[name]: print(name)`.
Stretch: the bare lookup raises `KeyError: 'Eleanor'`; `.get()` returns your fallback instead of crashing.

### Chapter 5

1. `if event == "closed" and side == "inside": print("Door closed normally")`.
2. The two lines that depend on `reentry_event_found` being `False` disappear, including the contradiction line.
Stretch: identical output; `not reentry_event_found` reads like English, which is what code is for.

### Chapter 6

1. Loop over `claimed_locations.values()` counting `location.startswith("W")` -- the answer is 2: West Gallery and Wine Cellar.
2. `if sensor_status[suspect] != "local_sensor_match": print(suspect)` -- prints only Eleanor Hartley.
Stretch: keep a counter you increment inside the loop, or loop with `enumerate(suspects, start=1)`.

### Chapter 7

1. 00:09 through 00:17 exclusive is nine minutes.
2. `for minute in range(0, 60, 5): print(minute)` -- 0, 5, 10, ... 55.
Stretch: the counter finishes at the same value as the subtraction; if it does not, the loop and the arithmetic disagree, and one of them is lying.

### Chapter 8

1. `03:17Z` is 23:17 the previous evening in Maine -- around the time Marcus was messaging Whitmore.
2. In January, Maine is UTC-5 (EST), so `00:17Z` becomes 19:17, not 20:17. Offsets are seasonal; that is exactly why you convert with `ZoneInfo` instead of subtracting a constant.
Stretch:

```python
def to_local(timestamp_text):
    ts = datetime.fromisoformat(timestamp_text.replace("Z", "+00:00"))
    return ts.astimezone(ZoneInfo("America/New_York"))
```

### Chapter 9

1. `len(active_keycards.union(retired_keycards))` -- 8.
2. Unused active cards mostly mean people who stayed put; the retired card is interesting because it should not have been usable at all.
Stretch: loop over `known_to.items()` and print keys where `len(people) == 1` -- only `MV-014`.

### Chapter 10

1. Accumulate `int(row["amount_usd"])` over every row without the vendor filter.
2. Zero payments are at or over threshold. A rule that is never triggered is not evidence of compliance; it is evidence that everyone knows exactly where the line is.
Stretch: add each `row["vendor"]` to a set, then print the set.

### Chapter 11

1. `for event in calendar_data["events"]: print(event["title"], "-", event["status"])`.
2. Count `event["status"] != "deleted"` -- 2.
Stretch: test `"Study" in event["location"]` -- the private meeting is the only one.

### Chapter 12

1. Same loop as the chapter with `re.compile(r"northstar", re.IGNORECASE)` -- 2 matches.
2. `re.compile(r"\d{2}:\d{2}")` finds every clock time in the file.
Stretch: `exit` also matches inside words like `exits`; `\bexit\b` requires word boundaries. Precision in patterns is precision in accusations.

### Chapter 13

1. `fragment_parts[9]` raises `IndexError`; catch it with `except IndexError:` and its own message.
2. `else:` after `except` runs only when the `try` block succeeded -- a clean-read receipt.
Stretch: a bare `except:` would also swallow typos like `NameError`, hiding your own bugs inside the evidence's damage. Catch what you expect; be surprised by the rest.

### Chapter 14

1. `def is_financial(name): return name in {"Eleanor Hartley", "Julian Cross"}`.
2. `def has_northstar_motive(suspect_name, vendor_name="Northstar Consulting"):` -- calling with one argument uses the default.
Stretch: returning lets the caller decide what the answer is *for*; printing decides for them.

### Chapter 15

1. `def has_findings(self): return len(self.findings) > 0`.
2. `aruna = Suspect("Aruna Patel", "Digital forensics", "Evidence table")` -- `aruna.score` is 0.
Stretch: track a best-so-far pair `(points, label)` inside `add_finding` and update it when a higher-point finding arrives.

### Chapter 16

1. `self.assertEqual(len(load_guests()), 6)` -- or read `guests.csv` inside the test.
2. `self.assertFalse(library_alibi_fails_for("Priya Anand"))`-style, or assert the phrase is absent with `assertNotIn("clean exit", whitmore_message)`.
Stretch: London is UTC+1 in October, so the conversion lands at a different local hour and two tests fail, telling you exactly which assumptions the case leans on.

### Chapter 17

1. In the interactive prompt: `from case_solver import build_case_report`, then `report = build_case_report()`, then `report.keys()`.
2. It lets a file behave as both script and module: run directly, the block executes; imported, it stays quiet.
Stretch: nothing changes in the output -- which is the whole point of a refactor.

### Chapter 18

1. Group on `row["date"][:7]` (the `YYYY-MM` prefix) and accumulate.
2. `146750 / 3` -- about $48,916 per transfer, each politely under the review threshold it was laundered past.
Stretch: `totals[name] = totals.get(name, 0) + amount`.

### Chapter 19

1. `sorted(commit_checks, key=lambda c: c["authored"])` -- or a named key function if you prefer the book's house style.
2. The door commit reaches 34 minutes into its future; the alibi-loop commit reaches 28. Bold is a good word for a forger.
Stretch: `def is_impossible(record): return datetime.fromisoformat(record["authored"]) < datetime.fromisoformat(record["refers_to"])`.

### Chapter 20

1. `machine_counts.most_common(1)` -- `[('RAVENHOUSE-SEC01', 14)]`.
2. Count `committer_text[11:13]` -- the 01:00 hour is the forger's most productive; five commits.
Stretch: keep `largest = None` and replace it whenever a bigger gap appears; print at the end.

### Chapter 21

1. Parse each timestamp, subtract consecutive pairs, print `.total_seconds()`.
2. The median barely moves when one human takes 90 seconds; the mean lurches. Baselines built on medians are harder to poison.
Stretch: `return gap_seconds < min(baseline) / 10` -- `True` for 0.38, `False` for 4.2.

### Chapter 22

1. Widest spread belongs to IMOGEN-TABLET (25 dBm) -- a device that wandered, which is what innocence usually looks like.
2. `statistics.mean(device_readings[name])` per device.
Stretch: named constants turn a magic number into a reviewable decision. `STATIONARY_SPREAD_DBM = 4` invites the question "why 4?" -- which is exactly the question a threshold should have to answer.

### Chapter 23

1. Totals do not move; a zero-weight source can be recorded without being believed. Keeping it in the file preserves honesty about what you chose to ignore.
2. Eleanor's murder total drops slightly; rankings do not change. Weights should change conclusions only when the evidence was actually load-bearing.
Stretch: Volkov rests on four provenance types; Eleanor's murder findings rest mostly on systems his session touched. Narrow bases deserve narrow confidence.

### Chapter 24

1. Loop the audit events, look each `actor_token` up in the `/tokens` map, and print `token["owner"]`. Volkov's service token appears most among the post-death events; Marcus's own user token owns the genuine evening pushes.
2. Keep events where `event["source_ip"].startswith("10.20.")`. The only off-island action is Priya's public registry export from a mainland IP -- press, not the house.
Stretch: `get("/secrets", TOKEN)` raises `HTTPError` with `.code == 404`. An API that describes what it refuses hands attackers a map; silence is a security feature, not rudeness.

### Chapter 25

1. The traceback names the misspelled variable and the exact line; bottom-up reading takes you from diagnosis to address.
2. The missing colon raises `SyntaxError: expected ':'` -- blunter and more honest than the unclosed parenthesis, which Python can only report from where it noticed, not where it happened.
Stretch:

```python
try:
    log_file = open("data/commit_log_fuller.txt", encoding="utf-8")
except FileNotFoundError:
    print("Run this from the murder_by_python folder, next to data/.")
```

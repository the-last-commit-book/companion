# chapter_19_the_commit_that_couldnt_exist.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 19: The Commit That Couldn't Exist

from datetime import datetime

# Each entry: commit, author time, and the earliest event its files describe.
commit_checks = [
    {"commit": "4c19a02", "message": "count guests before trusting house",
     "authored": "2025-10-13T22:31:00-04:00", "refers_to": "2025-10-13T19:30:00-04:00"},
    {"commit": "e03a7bf", "message": "northstar is not a constellation",
     "authored": "2025-10-13T23:43:00-04:00", "refers_to": "2025-10-13T23:42:00-04:00"},
    {"commit": "7d4f0e9", "message": "if i die run this",
     "authored": "2025-10-13T23:47:00-04:00", "refers_to": "2025-10-13T23:47:00-04:00"},
    {"commit": "8a19fc2", "message": "door opened after no return",
     "authored": "2025-10-13T23:41:00-04:00", "refers_to": "2025-10-14T00:15:00-04:00"},
    {"commit": "91c4d0b", "message": "alibis should repeat cleanly",
     "authored": "2025-10-13T23:49:00-04:00", "refers_to": "2025-10-14T00:17:31-04:00"},
    {"commit": "c04f7aa", "message": "count the blind minutes",
     "authored": "2025-10-13T23:56:00-04:00", "refers_to": "2025-10-14T00:10:00-04:00"},
    {"commit": "f18d2c9", "message": "library time is not local",
     "authored": "2025-10-14T00:02:00-04:00", "refers_to": "2025-10-14T00:17:00-04:00"},
    {"commit": "a62b19e", "message": "old admin card still opens doors",
     "authored": "2025-10-14T00:04:00-04:00", "refers_to": "2025-10-14T00:15:00-04:00"},
    {"commit": "d77f4e1", "message": "northstar stays under review limit",
     "authored": "2025-10-14T00:07:00-04:00", "refers_to": "2025-09-28T00:00:00-04:00"},
    {"commit": "e3c6a04", "message": "deleted does not mean gone",
     "authored": "2025-10-14T00:09:00-04:00", "refers_to": "2025-10-14T00:05:00-04:00"},
    {"commit": "6f2c1bd", "message": "broken record still says manual",
     "authored": "2025-10-14T00:13:00-04:00", "refers_to": "2025-10-14T00:10:00-04:00"},
    {"commit": "f49b72e", "message": "let the program say who remains",
     "authored": "2025-10-14T00:17:00-04:00", "refers_to": "2025-10-14T00:17:00-04:00"},
]

impossible_count = 0

print("Commit timeline check")
print("Rule: a commit cannot describe an event that has not happened yet.")
print()

for check in commit_checks:
    authored = datetime.fromisoformat(check["authored"])
    refers_to = datetime.fromisoformat(check["refers_to"])

    if authored < refers_to:
        impossible_count = impossible_count + 1
        verdict = "IMPOSSIBLE: describes the future"
    else:
        verdict = "consistent"

    print(check["commit"], check["authored"][11:16], "->", check["message"])
    print("   earliest event referenced:", check["refers_to"][11:16], "|", verdict)

print()
print("Impossible commits found:", impossible_count)
print("Clue: several commits were written before the events they describe.")
print("Files do not foreshadow. Someone backdated history.")

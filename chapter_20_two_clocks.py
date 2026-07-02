# chapter_20_two_clocks.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 20: Two Clocks in One Repository

from collections import Counter
from datetime import datetime

commits = [
    ("4c19a02", "2025-10-13T22:31:00-04:00", "2025-10-13T22:31:00-04:00", "THORNE-STUDY"),
    ("e03a7bf", "2025-10-13T23:43:00-04:00", "2025-10-13T23:43:00-04:00", "THORNE-STUDY"),
    ("7d4f0e9", "2025-10-13T23:47:00-04:00", "2025-10-13T23:47:00-04:00", "THORNE-STUDY"),
    ("8a19fc2", "2025-10-13T23:41:00-04:00", "2025-10-14T00:41:22-04:00", "RAVENHOUSE-SEC01"),
    ("b6117aa", "2025-10-13T23:49:00-04:00", "2025-10-14T00:52:07-04:00", "RAVENHOUSE-SEC01"),
    ("91c4d0b", "2025-10-13T23:49:00-04:00", "2025-10-14T00:58:41-04:00", "RAVENHOUSE-SEC01"),
    ("c04f7aa", "2025-10-13T23:56:00-04:00", "2025-10-14T01:05:33-04:00", "RAVENHOUSE-SEC01"),
    ("f18d2c9", "2025-10-14T00:02:00-04:00", "2025-10-14T01:12:19-04:00", "RAVENHOUSE-SEC01"),
    ("a62b19e", "2025-10-14T00:04:00-04:00", "2025-10-14T01:19:48-04:00", "RAVENHOUSE-SEC01"),
    ("d77f4e1", "2025-10-14T00:07:00-04:00", "2025-10-14T01:27:02-04:00", "RAVENHOUSE-SEC01"),
    ("e3c6a04", "2025-10-14T00:09:00-04:00", "2025-10-14T01:33:56-04:00", "RAVENHOUSE-SEC01"),
    ("b4a90df", "2025-10-14T00:11:00-04:00", "2025-10-14T01:40:11-04:00", "RAVENHOUSE-SEC01"),
    ("6f2c1bd", "2025-10-14T00:13:00-04:00", "2025-10-14T01:47:29-04:00", "RAVENHOUSE-SEC01"),
    ("0d8c4be", "2025-10-14T00:14:00-04:00", "2025-10-14T01:53:37-04:00", "RAVENHOUSE-SEC01"),
    ("9ce71a3", "2025-10-14T00:15:00-04:00", "2025-10-14T01:58:50-04:00", "RAVENHOUSE-SEC01"),
    ("3a6e0dc", "2025-10-14T00:16:00-04:00", "2025-10-14T02:03:24-04:00", "RAVENHOUSE-SEC01"),
    ("f49b72e", "2025-10-14T00:17:00-04:00", "2025-10-14T02:09:14-04:00", "RAVENHOUSE-SEC01"),
]

machine_counts = Counter()
forged_count = 0

print("Two-clock review")
print("Rule: author date is a claim. Committer date is a fact.")
print()

for commit_hash, author_text, committer_text, machine in commits:
    author_time = datetime.fromisoformat(author_text)
    committer_time = datetime.fromisoformat(committer_text)
    machine_counts[machine] += 1

    if author_time == committer_time:
        print(commit_hash, machine, "clocks agree")
    else:
        forged_count = forged_count + 1
        gap = committer_time - author_time
        print(commit_hash, machine, "clocks disagree by", gap)

print()
print("Commits per machine:", dict(machine_counts))
print("Backdated commits:", forged_count)
print()
print("Every genuine commit came from THORNE-STUDY with agreeing clocks.")
print("Every backdated commit was made on RAVENHOUSE-SEC01 between 00:41 and 02:09,")
print("while Marcus Thorne was dead and the island was cut off.")
print("Clue: the last commit was authored at the minute Marcus died")
print("and created almost two hours after it. The dead do not push code.")

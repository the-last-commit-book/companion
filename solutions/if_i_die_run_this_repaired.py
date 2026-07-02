# if_i_die_run_this.py
# Marcus Thorne -- committed 2025-10-13 23:47, repaired by the analyst.

from datetime import datetime

GENUINE_MACHINE = "THORNE-STUDY"

commit_records = []

with open("data/commit_log_fuller.txt", encoding="utf-8") as log_file:
    block = {}
    for line in log_file:
        line = line.strip()
        if line.startswith("commit "):
            block = {"commit": line.split()[1]}
        if line.startswith("AuthorDate:"):
            block["author"] = line.replace("AuthorDate:", "").strip()
        if line.startswith("CommitDate:"):
            block["committer"] = line.replace("CommitDate:", "").strip()
        if line.startswith("Machine:"):
            block["machine"] = line.replace("Machine:", "").strip()
            commit_records.append(block)

print("Verifying repository history...")
print()

genuine_count = 0
tampered_count = 0

for record in commit_records:
    author_time = datetime.fromisoformat(record["author"])
    committer_time = datetime.fromisoformat(record["committer"])

    if record["machine"] == GENUINE_MACHINE and author_time == committer_time:
        genuine_count = genuine_count + 1
        print(record["commit"], "GENUINE")
    else:
        tampered_count = tampered_count + 1
        print(record["commit"], "TAMPERED -- dates disagree or wrong machine")

print()
print("Genuine commits:", genuine_count)
print("Tampered commits:", tampered_count)
print()
print("If tampered commits exist, read this aloud to whoever is investigating:")
print()
print("  Someone has been inside my repository. My chapters change on nights")
print("  I do not write. I do not yet know which of them it is, so I am")
print("  telling the only witness I still trust: the graph.")
print()
print("  Copies of what matters are with my attorney in Rockland:")
print("  the vendor ledger, the original 2019 board metrics, and a list of")
print("  every person who can touch this house's logs.")
print()
print("  Do not trust any commit whose two dates disagree.")
print("  Trust the graph, not the dates.")
print("  Whoever edits history is the one who needs it edited.")
print()
print("  -- M.T.")

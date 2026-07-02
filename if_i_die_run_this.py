# if_i_die_run_this.py
# If you are reading this, check the dates.

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

print("Verifying repository history..."

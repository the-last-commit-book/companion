# chapter_18_the_announcement.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 18: The Announcement He Never Made

import csv

transfers_file_path = "data/bank_transfers.csv"

outbound_totals = {}
outbound_counts = {}

print("Northstar outbound transfer review")
print("File:", transfers_file_path)
print()

with open(transfers_file_path, newline="", encoding="utf-8") as transfers_file:
    reader = csv.DictReader(transfers_file)

    for row in reader:
        recipient = row["to_name"]
        amount = int(row["amount_usd"])

        if recipient not in outbound_totals:
            outbound_totals[recipient] = 0
            outbound_counts[recipient] = 0

        outbound_totals[recipient] = outbound_totals[recipient] + amount
        outbound_counts[recipient] = outbound_counts[recipient] + 1

        print(row["transfer_id"], "->", recipient, "$" + str(amount), "on", row["date"])

print()
for recipient in outbound_totals:
    print("Recipient:", recipient)
    print("  Transfers:", outbound_counts[recipient])
    print("  Total: $" + str(outbound_totals[recipient]))

print()
print("Northstar received $199120 in under-threshold payments approved by Eleanor Hartley.")
print("Clue: almost all of it left again, three transfers to Seahook Holdings LLC.")
print("Open question: who is Seahook Holdings?")

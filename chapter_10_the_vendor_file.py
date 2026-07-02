# chapter_10_the_vendor_file.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 10: The Vendor File

import csv

vendor_file_path = "data/vendors.csv"

northstar_payment_count = 0
northstar_payment_total = 0

print("Vendor file review")
print("File:", vendor_file_path)
print()
print("Northstar payments under approval threshold:")

with open(vendor_file_path, newline="", encoding="utf-8") as vendor_file:
    reader = csv.DictReader(vendor_file)

    for row in reader:
        vendor = row["vendor"]
        amount = int(row["amount_usd"])
        threshold = int(row["approval_threshold_usd"])
        approver = row["approver"]

        if vendor == "Northstar Consulting" and amount < threshold:
            northstar_payment_count = northstar_payment_count + 1
            northstar_payment_total = northstar_payment_total + amount

            print(row["payment_id"], vendor, "$" + str(amount), "approved by", approver)

print()
print("Northstar under-threshold payment count:", northstar_payment_count)
print("Northstar under-threshold payment total: $" + str(northstar_payment_total))
print("Approval threshold: $50000")
print("Clue: Northstar received repeated payments just under the approval threshold, all approved by Eleanor Hartley.")

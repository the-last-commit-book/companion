# chapter_22_too_obvious.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 22: Too Obvious

import csv

signal_file_path = "data/wifi_signal_log.csv"

device_readings = {}

with open(signal_file_path, newline="", encoding="utf-8") as signal_file:
    reader = csv.DictReader(signal_file)

    for row in reader:
        device_name = row["device_name"]
        signal_dbm = int(row["signal_dbm"])

        if device_name not in device_readings:
            device_readings[device_name] = []

        device_readings[device_name].append(signal_dbm)

print("Signal spread review")
print("Rule: carried devices vary; installed devices hold still.")
print()

stationary_devices = []

for device_name in device_readings:
    readings = device_readings[device_name]
    strongest = max(readings)
    weakest = min(readings)
    spread = strongest - weakest

    print("Device:", device_name)
    print("  readings:", len(readings), " strongest:", strongest, " weakest:", weakest, " spread:", spread)

    if spread < 4:
        stationary_devices.append(device_name)
        print("  Finding: effectively stationary all night.")

print()
print("Stationary devices:", stationary_devices)
print("Clue: HARTLEY-PRIVATE never moved. It was not carried near the east wing.")
print("It was placed there, and left to testify.")

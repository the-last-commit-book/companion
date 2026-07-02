# chapter_21_the_alibi_that_answered_itself.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 21: The Alibi That Answered Itself

import statistics
from datetime import datetime

alert_time = datetime.fromisoformat("2025-10-14T00:17:03.200000-04:00")
acknowledged_time = datetime.fromisoformat("2025-10-14T00:17:03.580000-04:00")

night_ack_gap = (acknowledged_time - alert_time).total_seconds()

# Volkov's acknowledgment latencies from the previous week, in seconds.
baseline_gaps = [4.2, 6.8, 11.3, 5.5, 7.9, 4.8]
baseline_average = statistics.mean(baseline_gaps)
baseline_fastest = min(baseline_gaps)

svc_kiosk_events = [
    ("00:10:00.41", "camera_manual_disable", "CAM-EAST-02"),
    ("00:16:58.77", "camera_enable", "CAM-EAST-02"),
    ("00:17:03.58", "alert_acknowledge", "STORM-EAST"),
    ("02:09:14.02", "repo_sync_push", "marcus-thorne/last-commit"),
]

print("Acknowledgment latency review")
print("Storm alert raised:      00:17:03.20")
print("Storm alert acknowledged: 00:17:03.58")
print("Latency this night:", night_ack_gap, "seconds")
print()
print("Baseline latencies:", baseline_gaps)
print("Baseline average:", round(baseline_average, 1), "seconds")
print("Baseline fastest:", baseline_fastest, "seconds")
print()

if night_ack_gap < baseline_fastest / 10:
    print("Finding: the acknowledgment is faster than human. It was scripted.")

print()
print("Events in service session SVC-KIOSK:")
for event_time, event_name, target in svc_kiosk_events:
    print(" ", event_time, event_name, target)

print()
print("Clue: the session that acknowledged the alert also blinded the camera")
print("and pushed the forged history. The alibi answered itself.")

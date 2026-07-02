# chapter_08_the_library_alibi.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 8: The Library Alibi

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

raven_house_time_zone = ZoneInfo("America/New_York")

library_timestamp_from_report = "2025-10-14T00:17:00Z"
actual_murder_time_local_text = "2025-10-14T00:17:00-04:00"

# The naive report looked only at the clock part of the UTC timestamp.
naive_report_time = library_timestamp_from_report[11:16]

# Convert the smart-light timestamp from UTC into Raven House local time in Maine.
library_time_utc = datetime.fromisoformat(
    library_timestamp_from_report.replace("Z", "+00:00")
)
library_time_local = library_time_utc.astimezone(raven_house_time_zone)

# Convert the known murder time into UTC so both times can be compared cleanly.
actual_murder_time_local = datetime.fromisoformat(actual_murder_time_local_text)
actual_murder_time_utc = actual_murder_time_local.astimezone(timezone.utc)

time_gap = actual_murder_time_utc - library_time_utc

library_event_from_naive_report = "occupancy_confirmed"
library_event_at_actual_murder_time = "no_occupancy"

print("Library alibi review")
print("Smart-light timestamp in report:", library_timestamp_from_report)
print("Naive report read the clock as:", naive_report_time)
print("Converted Raven House local time in Maine:", library_time_local.strftime("%Y-%m-%d %H:%M %Z"))
print("Actual murder time, local:", actual_murder_time_local.strftime("%Y-%m-%d %H:%M %z"))
print("Actual murder time, UTC:", actual_murder_time_utc.strftime("%Y-%m-%d %H:%M %Z"))
print("Gap between library confirmation and murder:", time_gap)
print()
print("Library event from naive report:", library_event_from_naive_report)
print("Library event at actual murder time:", library_event_at_actual_murder_time)

if library_time_utc == actual_murder_time_utc:
    print("Result: the library timestamp matches the murder time.")

if library_time_utc != actual_murder_time_utc:
    print("Result: the library timestamp does not match the murder time.")
    print("Clue: Eleanor's library alibi is four hours too early when UTC is converted correctly.")

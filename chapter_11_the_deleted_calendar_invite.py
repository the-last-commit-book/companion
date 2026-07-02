# chapter_11_the_deleted_calendar_invite.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 11: The Deleted Calendar Invite

import json

calendar_file_path = "data/calendar.json"

print("Calendar review")
print("File:", calendar_file_path)
print()

with open(calendar_file_path, encoding="utf-8") as calendar_file:
    calendar_data = json.load(calendar_file)

raven_house_timezone = calendar_data["timezone"]
events = calendar_data["events"]

target_person_one = "Marcus Thorne"
target_person_two = "Eleanor Hartley"

deleted_meeting_count = 0

print("Calendar timezone:", raven_house_timezone)
print("Recovered events:", len(events))
print()
print("Deleted Marcus-Eleanor meetings:")

for event in events:
    status = event["status"]
    attendees = event["attendees"]

    if status == "deleted" and target_person_one in attendees and target_person_two in attendees:
        deleted_meeting_count = deleted_meeting_count + 1

        print("Event ID:", event["event_id"])
        print("Title:", event["title"])
        print("Start:", event["start_local"])
        print("End:", event["end_local"])
        print("Location:", event["location"])
        print("Deleted by:", event["deleted_by"])
        print("Notes:", event["notes"])
        print()

print("Deleted Marcus-Eleanor meeting count:", deleted_meeting_count)
print("Clue: a deleted calendar invite places Marcus and Eleanor in a private study meeting before the murder.")

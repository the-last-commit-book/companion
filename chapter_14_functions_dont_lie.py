# chapter_14_functions_dont_lie.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 14: Functions Don't Lie

import csv
import json
import re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def has_northstar_motive(suspect_name):
    northstar_payment_count = 0

    with open("data/vendors.csv", newline="", encoding="utf-8") as vendor_file:
        reader = csv.DictReader(vendor_file)

        for row in reader:
            vendor = row["vendor"]
            amount = int(row["amount_usd"])
            threshold = int(row["approval_threshold_usd"])
            approver = row["approver"]

            if vendor == "Northstar Consulting" and amount < threshold and approver == suspect_name:
                northstar_payment_count = northstar_payment_count + 1

    return northstar_payment_count > 0


def lied_about_library_alibi(suspect_name):
    if suspect_name != "Eleanor Hartley":
        return False

    raven_house_time_zone = ZoneInfo("America/New_York")
    actual_murder_time_local = datetime.fromisoformat("2025-10-14T00:17:00-04:00")
    actual_murder_time_utc = actual_murder_time_local.astimezone(timezone.utc)

    library_confirmation_utc = None
    library_event_at_murder = None

    with open("data/smart_light_log.csv", newline="", encoding="utf-8") as light_file:
        reader = csv.DictReader(light_file)

        for row in reader:
            timestamp_utc = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))

            if row["room"] == "Library" and row["actor_hint"] == suspect_name and row["event"] == "occupancy_confirmed":
                library_confirmation_utc = timestamp_utc

            if row["room"] == "Library" and timestamp_utc == actual_murder_time_utc:
                library_event_at_murder = row["event"]

    if library_confirmation_utc is None:
        return False

    library_confirmation_local = library_confirmation_utc.astimezone(raven_house_time_zone)
    library_confirmation_is_early = library_confirmation_local != actual_murder_time_local
    library_empty_at_murder = library_event_at_murder == "no_occupancy"

    return library_confirmation_is_early and library_empty_at_murder


def knew_old_admin_card(suspect_name):
    with open("data/keycard_assignments.csv", newline="", encoding="utf-8") as keycard_file:
        reader = csv.DictReader(keycard_file)

        for row in reader:
            if row["keycard_id"] == "OLD-ADMIN-000":
                people_who_knew = row["known_to"].split(";")
                return suspect_name in people_who_knew

    return False


def had_deleted_meeting_with_marcus(suspect_name):
    with open("data/calendar.json", encoding="utf-8") as calendar_file:
        calendar_data = json.load(calendar_file)

    for event in calendar_data["events"]:
        attendees = event["attendees"]

        if event["status"] == "deleted" and "Marcus Thorne" in attendees and suspect_name in attendees:
            return True

    return False


def used_clean_exit_phrase(suspect_name):
    phrase_pattern = re.compile(r"clean exit", re.IGNORECASE)

    with open("data/messages.txt", encoding="utf-8") as messages_file:
        for line in messages_file:
            if suspect_name in line and phrase_pattern.search(line):
                return True

    return False


def has_private_device_near_east_wing(suspect_name):
    surname = suspect_name.split()[-1].upper()

    with open("data/wifi_log.csv", newline="", encoding="utf-8") as wifi_file:
        reader = csv.DictReader(wifi_file)

        for row in reader:
            device_name = row["device_name"]
            access_point = row["access_point"]
            owner = row["owner"]

            if surname in device_name and owner == "Unknown" and access_point == "EAST_WING_AP":
                return True

    return False


def manual_camera_disable_used_old_admin():
    with open("data/camera_metadata.json", encoding="utf-8") as camera_file:
        camera_data = json.load(camera_file)

    for record in camera_data["metadata_records"]:
        if record["camera_id"] == "CAM-EAST-02":
            try:
                if record["last_command"] == "manual_disable" and record["keycard_id"] == "OLD-ADMIN-000":
                    return True
            except KeyError:
                raw_fragment = record["raw_fragment"]
                fragment_parts = raw_fragment.split("|")
                fragment_command = fragment_parts[2]
                fragment_keycard = fragment_parts[4]

                if fragment_command == "manual_disable" and fragment_keycard == "OLD-ADMIN-000":
                    return True

    return False


def calculate_convergence_score(suspect_name):
    score = 0

    if has_northstar_motive(suspect_name):
        score = score + 1

    if lied_about_library_alibi(suspect_name):
        score = score + 1

    if knew_old_admin_card(suspect_name):
        score = score + 1

    if had_deleted_meeting_with_marcus(suspect_name):
        score = score + 1

    if used_clean_exit_phrase(suspect_name):
        score = score + 1

    if has_private_device_near_east_wing(suspect_name):
        score = score + 1

    if manual_camera_disable_used_old_admin() and knew_old_admin_card(suspect_name):
        score = score + 1

    return score


suspects_to_review = [
    "Eleanor Hartley",
    "Mikhail Volkov",
    "Julian Cross",
]

print("Function review")
print("Each function checks one repeated question against the evidence files.")
print()

for suspect in suspects_to_review:
    print("Suspect:", suspect)
    print("has_northstar_motive:", has_northstar_motive(suspect))
    print("lied_about_library_alibi:", lied_about_library_alibi(suspect))
    print("knew_old_admin_card:", knew_old_admin_card(suspect))
    print("had_deleted_meeting_with_marcus:", had_deleted_meeting_with_marcus(suspect))
    print("used_clean_exit_phrase:", used_clean_exit_phrase(suspect))
    print("has_private_device_near_east_wing:", has_private_device_near_east_wing(suspect))
    print("old_admin_connected_to_manual_camera_disable:", manual_camera_disable_used_old_admin() and knew_old_admin_card(suspect))
    print("convergence_score:", calculate_convergence_score(suspect))
    print()

print("Clue: the same reusable checks converge most strongly on Eleanor Hartley.")
print("Reminder: a convergence score organizes evidence. It is not a verdict.")

# chapter_16_test_the_alibis.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 16: Test the Alibis

import csv
import unittest
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


RAVEN_HOUSE_TIME_ZONE = ZoneInfo("America/New_York")
SMART_LIGHT_FILE = "data/smart_light_log.csv"
ACTUAL_MURDER_TIME_LOCAL = datetime.fromisoformat("2025-10-14T00:17:00-04:00")
ACTUAL_MURDER_TIME_UTC = ACTUAL_MURDER_TIME_LOCAL.astimezone(timezone.utc)


def parse_utc_timestamp(timestamp_text):
    return datetime.fromisoformat(timestamp_text.replace("Z", "+00:00"))


def convert_utc_text_to_raven_local(timestamp_text):
    timestamp_utc = parse_utc_timestamp(timestamp_text)
    return timestamp_utc.astimezone(RAVEN_HOUSE_TIME_ZONE)


def find_library_confirmation_for(actor_name):
    with open(SMART_LIGHT_FILE, newline="", encoding="utf-8") as light_file:
        reader = csv.DictReader(light_file)

        for row in reader:
            if row["room"] == "Library" and row["event"] == "occupancy_confirmed" and row["actor_hint"] == actor_name:
                return row["timestamp_utc"]

    return None


def find_library_event_at(timestamp_utc):
    with open(SMART_LIGHT_FILE, newline="", encoding="utf-8") as light_file:
        reader = csv.DictReader(light_file)

        for row in reader:
            row_timestamp_utc = parse_utc_timestamp(row["timestamp_utc"])

            if row["room"] == "Library" and row_timestamp_utc == timestamp_utc:
                return row["event"]

    return None


def library_alibi_fails_for(actor_name):
    confirmation_timestamp_text = find_library_confirmation_for(actor_name)

    if confirmation_timestamp_text is None:
        return False

    confirmation_time_local = convert_utc_text_to_raven_local(confirmation_timestamp_text)
    event_at_murder = find_library_event_at(ACTUAL_MURDER_TIME_UTC)

    confirmation_is_not_murder_time = confirmation_time_local != ACTUAL_MURDER_TIME_LOCAL
    library_empty_at_murder = event_at_murder == "no_occupancy"

    return confirmation_is_not_murder_time and library_empty_at_murder


class TestLibraryAlibi(unittest.TestCase):
    def test_naive_clock_reading_looks_like_murder_time(self):
        timestamp_text = "2025-10-14T00:17:00Z"
        naive_clock_reading = timestamp_text[11:16]
        self.assertEqual(naive_clock_reading, "00:17")

    def test_utc_library_confirmation_converts_one_hour_early(self):
        timestamp_text = "2025-10-14T00:17:00Z"
        converted_local = convert_utc_text_to_raven_local(timestamp_text)
        self.assertEqual(converted_local.strftime("%Y-%m-%d %H:%M %z"), "2025-10-13 20:17 -0400")

    def test_actual_murder_time_is_one_hour_later_in_utc(self):
        self.assertEqual(ACTUAL_MURDER_TIME_UTC.strftime("%Y-%m-%d %H:%M %Z"), "2025-10-14 04:17 UTC")

    def test_library_is_empty_at_actual_murder_time(self):
        event_at_murder = find_library_event_at(ACTUAL_MURDER_TIME_UTC)
        self.assertEqual(event_at_murder, "no_occupancy")

    def test_eleanor_library_alibi_fails(self):
        self.assertTrue(library_alibi_fails_for("Eleanor Hartley"))

    def test_other_suspects_do_not_have_eleanor_library_failure(self):
        self.assertFalse(library_alibi_fails_for("Mikhail Volkov"))
        self.assertFalse(library_alibi_fails_for("Julian Cross"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

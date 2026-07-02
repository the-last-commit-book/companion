from pathlib import Path
import csv
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

BASE = Path(__file__).parent
DATA = BASE / "data"
LOCAL_ZONE = ZoneInfo("America/New_York")
UTC_ZONE = ZoneInfo("UTC")


def read_csv(filename):
    with open(DATA / filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def parse_local(timestamp_text):
    return datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S").replace(tzinfo=LOCAL_ZONE)


def parse_utc(timestamp_text):
    clean = timestamp_text.replace("Z", "+00:00")
    return datetime.fromisoformat(clean).astimezone(UTC_ZONE)


def main():
    guests = read_csv("guests.csv")
    wifi = read_csv("wifi_log.csv")
    door_log = read_csv("door_log.csv")
    lights = read_csv("smart_light_log.csv")
    keycards = read_csv("keycard_assignments.csv")
    vendors = read_csv("vendors.csv")
    messages = (DATA / "messages.txt").read_text(encoding="utf-8")
    calendar = json.loads((DATA / "calendar.json").read_text(encoding="utf-8"))
    camera = json.loads((DATA / "camera_metadata.json").read_text(encoding="utf-8"))

    incident_text = (DATA / "incident_report.txt").read_text(encoding="utf-8")
    assert "Marcus Thorne used a wheelchair" in incident_text
    assert "brake engaged" in incident_text

    # 1. Six guests, seven unique devices.
    unique_devices = {row["device_name"] for row in wifi if row["timestamp_local"] <= "2025-10-14 00:12:00"}
    assert len(guests) == 6
    assert len(unique_devices) == 7
    assert "HARTLEY-PRIVATE" in unique_devices

    # 2. Door contradiction: Marcus is logged opening the east balcony from inside twice,
    # but there is no re-entry between the first exit and second opening.
    east_events = [row for row in door_log if row["door"] == "EAST_BALCONY_DOOR"]
    marcus_inside_opens = [
        row for row in east_events
        if row["user"] == "Marcus Thorne" and row["event"] == "opened" and row["side"] == "inside"
    ]
    assert [row["timestamp_local"] for row in marcus_inside_opens] == [
        "2025-10-14 00:08:00",
        "2025-10-14 00:15:00",
    ]
    re_entries = [
        row for row in east_events
        if "2025-10-14 00:09:00" < row["timestamp_local"] < "2025-10-14 00:15:00"
        and row["side"] == "outside"
        and row["event"] == "opened"
    ]
    assert re_entries == []

    # 3. Timezone twist: Eleanor's 00:17 UTC library log is 20:17 local, not 00:17 local.
    eleanor_light = next(
        row for row in lights
        if row["actor_hint"] == "Eleanor Hartley" and row["event"] == "occupancy_confirmed"
    )
    naive_time_seen_by_report = eleanor_light["timestamp_utc"].replace("T", " ")[11:16]
    actual_local = parse_utc(eleanor_light["timestamp_utc"]).astimezone(LOCAL_ZONE)
    assert naive_time_seen_by_report == "00:17"
    assert actual_local.strftime("%Y-%m-%d %H:%M") == "2025-10-13 20:17"

    actual_murder_local = datetime(2025, 10, 14, 0, 17, tzinfo=LOCAL_ZONE)
    actual_murder_utc = actual_murder_local.astimezone(UTC_ZONE)
    library_at_murder = [
        row for row in lights
        if row["room"] == "Library" and parse_utc(row["timestamp_utc"]) == actual_murder_utc
    ]
    assert library_at_murder[0]["event"] == "no_occupancy"

    # 4. Old admin keycard is used and retired.
    used_keycards = {row["keycard_id"] for row in door_log if row["keycard_id"]}
    active_keycards = {row["keycard_id"] for row in keycards if row["status"] == "active"}
    retired_used = used_keycards - active_keycards
    assert retired_used == {"OLD-ADMIN-000"}
    old_admin = next(row for row in keycards if row["keycard_id"] == "OLD-ADMIN-000")
    assert "Eleanor Hartley" in old_admin["known_to"]
    assert "Mikhail Volkov" in old_admin["known_to"]

    # 5. Northstar pattern: repeated payments under the approval threshold, approved by Eleanor.
    northstar_payments = [
        row for row in vendors
        if row["vendor"] == "Northstar Consulting"
        and int(row["amount_usd"]) < int(row["approval_threshold_usd"])
        and row["approver"] == "Eleanor Hartley"
    ]
    assert len(northstar_payments) == 4

    # 6. The phrase "clean exit" appears in Eleanor's message and Marcus's recovered note.
    clean_exit_matches = re.findall(r"clean exit", messages, flags=re.IGNORECASE)
    assert len(clean_exit_matches) == 2

    # 7. Deleted calendar meeting between Marcus and Eleanor exists.
    deleted_meetings = [
        event for event in calendar["events"]
        if event["status"] == "deleted"
        and "Marcus Thorne" in event["attendees"]
        and "Eleanor Hartley" in event["attendees"]
    ]
    assert len(deleted_meetings) == 1
    assert deleted_meetings[0]["start_local"] == "2025-10-13T23:50:00-04:00"

    # 8. East camera outage is exactly seven minutes and manually disabled.
    east_camera = next(
        record for record in camera["metadata_records"]
        if record.get("camera_id") == "CAM-EAST-02" and record.get("status") == "offline"
    )
    start = datetime.fromisoformat(east_camera["offline_start_local"])
    end = datetime.fromisoformat(east_camera["offline_end_local"])
    outage_minutes = int((end - start).total_seconds() // 60)
    assert outage_minutes == 7
    assert east_camera["last_command"] == "manual_disable"
    assert east_camera["keycard_id"] == "OLD-ADMIN-000"

    # ---- v21 additions: the twist arc ----

    # 9. Northstar outbound: three transfers to Seahook totaling 146750.
    transfers = read_csv("bank_transfers.csv")
    seahook = [row for row in transfers if row["to_name"] == "Seahook Holdings LLC"]
    assert len(seahook) == 3
    assert sum(int(row["amount_usd"]) for row in seahook) == 146750

    # 10. Two clocks: 3 genuine commits, 14 tampered, last commit pushed at 02:09.
    fuller = (DATA / "commit_log_fuller.txt").read_text(encoding="utf-8")
    blocks = [b for b in fuller.strip().split("\n\n") if b.strip()]
    genuine = 0
    tampered = 0
    for block in blocks:
        fields = dict(line.split(": ", 1) for line in block.splitlines()[1:])
        agree = fields["AuthorDate"] == fields["CommitDate"]
        if agree and fields["Machine"] == "THORNE-STUDY":
            genuine += 1
        else:
            tampered += 1
    assert genuine == 3
    assert tampered == 14

    # 11. Scripted alibi: storm-alert acknowledgment latency is 0.38 seconds.
    sessions = read_csv("console_sessions.csv")
    storm = [row for row in sessions if row["target"] == "STORM-EAST"]
    raised = datetime.fromisoformat(next(r for r in storm if r["event"] == "alert_raise")["timestamp"])
    acked = datetime.fromisoformat(next(r for r in storm if r["event"] == "alert_acknowledge")["timestamp"])
    assert abs((acked - raised).total_seconds() - 0.38) < 0.001

    # 12. Planted device: HARTLEY-PRIVATE signal spread is 2 dBm; every carried device exceeds 15.
    signals = read_csv("wifi_signal_log.csv")
    readings = {}
    for row in signals:
        readings.setdefault(row["device_name"], []).append(int(row["signal_dbm"]))
    spread = {name: max(vals) - min(vals) for name, vals in readings.items()}
    assert spread["HARTLEY-PRIVATE"] == 2
    assert all(value > 15 for name, value in spread.items() if name != "HARTLEY-PRIVATE")

    # 13. Lockbox custody: H-77 left the lockbox with M. Volkov before the retreat.
    lockbox = read_csv("lockbox_inventory.csv")
    h77 = next(row for row in lockbox if row["item_id"] == "H-77")
    assert "M. Volkov" in h77["custody_note"]

    # 14. Daniel's east-wing hop: out at 00:10:52, back at 00:12:31.
    hops = read_csv("wifi_assoc_log.csv")
    daniel = [row for row in hops if row["device_name"] == "DANIEL-PHONE" and row["from_ap"] != "NONE"]
    assert [row["to_ap"] for row in daniel] == ["EAST_WING_AP", "BILLIARD_AP"]

    # 15. Registry: Seahook's manager of record is Volkov; announcement audits security too.
    registry = (DATA / "registry_extract.txt").read_text(encoding="utf-8")
    assert "MIKHAIL VOLKOV" in registry
    announcement = (DATA / "announcement_draft.txt").read_text(encoding="utf-8")
    assert "including security" in announcement

    # 16. Cloud audit: a service token impersonated Marcus after death (04:17 UTC).
    audit = json.loads((DATA / "cloud_audit_log.json").read_text(encoding="utf-8"))
    tokens = json.loads((DATA / "token_registry.json").read_text(encoding="utf-8"))["tokens"]
    death_utc = datetime(2025, 10, 14, 4, 17, tzinfo=UTC_ZONE)
    impossible = [
        e for e in audit["events"]
        if parse_utc(e["timestamp_utc"]) > death_utc
        and e["principal_claimed"].startswith("marcus.thorne")
        and tokens.get(e["actor_token"], {}).get("type") == "service"
    ]
    assert len(impossible) == 2
    assert all(tokens[e["actor_token"]]["owner"] == "Mikhail Volkov" for e in impossible)
    assert all(e["source_ip"].startswith("10.20.") for e in impossible)

    print("Dataset self-test passed.")
    print(f"Python version: {'.'.join(map(str, __import__('sys').version_info[:3]))}")
    print("Guests:", len(guests))
    print("Unique devices by 00:12:", len(unique_devices), sorted(unique_devices))
    print("Eleanor naive library time:", naive_time_seen_by_report)
    print("Eleanor actual local library time:", actual_local.strftime("%Y-%m-%d %H:%M %Z"))
    print("Actual murder UTC:", actual_murder_utc.strftime("%Y-%m-%d %H:%M %Z"))
    print("Library event at actual murder time:", library_at_murder[0]["event"])
    print("Retired keycards used:", sorted(retired_used))
    print("Northstar under-threshold payments approved by Eleanor:", len(northstar_payments))
    print('"clean exit" matches:', len(clean_exit_matches))
    print("East camera outage minutes:", outage_minutes)
    print("Accessibility note: Marcus used a wheelchair; chair brake engaged inside east balcony door.")


if __name__ == "__main__":
    main()

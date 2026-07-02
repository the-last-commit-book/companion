# chapter_06_every_alibi_has_a_loop.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 6: Every Alibi Has a Loop

suspects = [
    "Eleanor Hartley",
    "Julian Cross",
    "Imogen Wells",
    "Mikhail Volkov",
    "Priya Anand",
    "Daniel Thorne",
]

claimed_locations = {
    "Eleanor Hartley": "Library",
    "Julian Cross": "Wine Cellar",
    "Imogen Wells": "West Gallery",
    "Mikhail Volkov": "Security Office",
    "Priya Anand": "Conservatory",
    "Daniel Thorne": "Billiard Room",
}

sensor_notes = {
    "Eleanor Hartley": "Imported from smart-light report; timezone not checked yet.",
    "Julian Cross": "Wine cellar humidity panel touched at 00:16:20 local.",
    "Imogen Wells": "West gallery voice note saved at 00:16:45 local.",
    "Mikhail Volkov": "Security console storm alert acknowledged at 00:17:05 local.",
    "Priya Anand": "Conservatory keyboard activity at 00:17:12 local.",
    "Daniel Thorne": "Billiard table ball return triggered at 00:17:31 local.",
}

sensor_status = {
    "Eleanor Hartley": "imported_report",
    "Julian Cross": "local_sensor_match",
    "Imogen Wells": "local_sensor_match",
    "Mikhail Volkov": "local_sensor_match",
    "Priya Anand": "local_sensor_match",
    "Daniel Thorne": "local_sensor_match",
}

local_matches = 0
needs_time_review = 0

print("Alibi sensor review")
print()

for suspect in suspects:
    print("Suspect:", suspect)
    print("Claimed location:", claimed_locations[suspect])
    print("Sensor note:", sensor_notes[suspect])

    if sensor_status[suspect] == "local_sensor_match":
        local_matches = local_matches + 1
        print("Status: local sensor support found")

    if sensor_status[suspect] == "imported_report":
        needs_time_review = needs_time_review + 1
        print("Status: imported report; timezone review required")

    print()

print("Local sensor matches:", local_matches)
print("Alibis needing timezone review:", needs_time_review)
print("Clue: five alibis have local sensor support; Eleanor's library alibi is the one imported from a time-sensitive report.")

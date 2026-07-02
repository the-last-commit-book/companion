# chapter_07_the_impossible_minute.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 7: The Impossible Minute

camera_id = "CAM-EAST-02"
camera_location = "East Balcony"

camera_offline_start = 10
camera_offline_end = 17

minute_labels = {
    10: "00:10",
    11: "00:11",
    12: "00:12",
    13: "00:13",
    14: "00:14",
    15: "00:15",
    16: "00:16",
    17: "00:17",
}

smart_light_status = "still recording"
smart_light_room = "Library"

print("Camera timeline review")
print("Camera:", camera_id)
print("Location:", camera_location)
print("Offline start:", minute_labels[camera_offline_start])
print("Offline end:", minute_labels[camera_offline_end])
print()

minute = camera_offline_start
offline_minutes = 0

while minute < camera_offline_end:
    print(minute_labels[minute], "camera offline")
    offline_minutes = offline_minutes + 1
    minute = minute + 1

print()
print("Offline minutes counted:", offline_minutes)
print("Smart-light system:", smart_light_status)
print("Smart-light room checked:", smart_light_room)
print("Clue: the east camera was blind for exactly seven minutes, but the house kept recording elsewhere.")

print()
print("Range check:")
for minute in range(camera_offline_start, camera_offline_end):
    print("range minute:", minute_labels[minute])

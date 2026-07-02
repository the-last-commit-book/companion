# chapter_13_exceptions_in_the_evidence.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 13: Exceptions in the Evidence

import json

camera_file_path = "data/camera_metadata.json"
target_camera = "CAM-EAST-02"

manual_disable_count = 0
recovered_fragment_count = 0
storm_failure_count = 0

print("Camera metadata recovery")
print("File:", camera_file_path)
print("Target camera:", target_camera)
print()

with open(camera_file_path, encoding="utf-8") as camera_file:
    camera_data = json.load(camera_file)

records = camera_data["metadata_records"]

for record in records:
    if record["camera_id"] == target_camera:
        print("Reviewing record for:", record["camera_id"])
        print("Record status:", record["status"])

        try:
            command = record["last_command"]
            source = record["command_source"]
            keycard_id = record["keycard_id"]

            print("Command:", command)
            print("Source:", source)
            print("Keycard:", keycard_id)

            if command == "manual_disable":
                manual_disable_count = manual_disable_count + 1
                print("Finding: complete metadata says the camera was manually disabled.")

            if command == "storm_failure":
                storm_failure_count = storm_failure_count + 1
                print("Finding: metadata says storm failure.")

        except KeyError:
            recovered_fragment_count = recovered_fragment_count + 1
            print("Incomplete record found. Recovering from raw fragment.")

            raw_fragment = record["raw_fragment"]
            fragment_parts = raw_fragment.split("|")

            fragment_camera_id = fragment_parts[0]
            fragment_timestamp = fragment_parts[1]
            fragment_command = fragment_parts[2]
            fragment_source = fragment_parts[3]
            fragment_keycard = fragment_parts[4]

            print("Recovered camera:", fragment_camera_id)
            print("Recovered timestamp:", fragment_timestamp)
            print("Recovered command:", fragment_command)
            print("Recovered source:", fragment_source)
            print("Recovered keycard:", fragment_keycard)

            if fragment_command == "manual_disable":
                manual_disable_count = manual_disable_count + 1
                print("Finding: recovered fragment also says manual disable.")

        print()

print("Manual disable findings:", manual_disable_count)
print("Recovered corrupt fragments:", recovered_fragment_count)
print("Storm failure findings:", storm_failure_count)

if manual_disable_count > 0 and storm_failure_count == 0:
    print("Clue: CAM-EAST-02 was manually disabled by admin override, not knocked out by the storm.")

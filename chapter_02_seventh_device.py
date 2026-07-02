# chapter_02_seventh_device.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 2: The Seventh Device

registered_devices = [
    "HARTLEY-PHONE",
    "CROSS-PHONE",
    "IMOGEN-TABLET",
    "VOLKOV-SECURE",
    "PRIYA-NOTES",
    "DANIEL-PHONE",
    "HARTLEY-PRIVATE",
]

device_owners = [
    "Eleanor Hartley",
    "Julian Cross",
    "Imogen Wells",
    "Mikhail Volkov",
    "Priya Anand",
    "Daniel Thorne",
    "Unknown",
]

device_locations = [
    "LIBRARY_AP",
    "NORTH_HALL_AP",
    "WEST_GALLERY_AP",
    "SECURITY_AP",
    "CONSERVATORY_AP",
    "BILLIARD_AP",
    "EAST_WING_AP",
]

# Python starts counting list positions at 0.
# The seventh item is therefore at index 6.
seventh_device_index = 6

seventh_device = registered_devices[seventh_device_index]
seventh_owner = device_owners[seventh_device_index]
seventh_location = device_locations[seventh_device_index]

print("Seventh registered device:", seventh_device)
print("Listed owner:", seventh_owner)
print("Access point:", seventh_location)
print("Case consequence: a Hartley-named private device appears near the east wing.")

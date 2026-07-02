# chapter_01_guest_list.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 1: Guest List

victim = "Marcus Thorne"
location = "Raven House"

invited_guests = 6
registered_devices = 7

unexplained_devices = registered_devices - invited_guests

case_label = "Raven House device check"
expected_device_rule = "one registered device per invited guest"

print("Case:", victim, "at", location)
print("Check:", case_label)
print("Rule:", expected_device_rule)
print("Invited guests:", invited_guests)
print("Registered devices:", registered_devices)
print("Unexplained devices:", unexplained_devices)
print("First clue: there is one more device than invited guest.")

# chapter_09_the_duplicate_keycard.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 9: The Duplicate Keycard

active_keycards = {
    "EH-216",
    "JC-088",
    "IW-401",
    "MV-014",
    "PA-330",
    "DT-077",
    "MT-001",
}

retired_keycards = {
    "OLD-ADMIN-000",
}

used_keycards = {
    "EH-216",
    "MV-014",
    "MT-001",
    "OLD-ADMIN-000",
}

known_to = {
    "EH-216": {"Eleanor Hartley", "Mikhail Volkov"},
    "MV-014": {"Mikhail Volkov"},
    "MT-001": {"Marcus Thorne", "Mikhail Volkov"},
    "OLD-ADMIN-000": {"Eleanor Hartley", "Mikhail Volkov"},
}

old_admin_uses = [
    "00:06 SERVICE_STAIR_EAST opened by Unassigned legacy admin",
    "00:15 EAST_BALCONY_DOOR opened under Marcus Thorne's identity",
]

used_retired_keycards = used_keycards.intersection(retired_keycards)
used_keycards_not_active = used_keycards.difference(active_keycards)
people_who_knew_old_admin = known_to["OLD-ADMIN-000"]

print("Keycard review")
print("Active keycards:", active_keycards)
print("Retired keycards:", retired_keycards)
print("Used keycards:", used_keycards)
print()
print("Used retired keycards:", used_retired_keycards)
print("Used keycards not in active assignments:", used_keycards_not_active)
print()

for old_admin_use in old_admin_uses:
    print("OLD-ADMIN-000 use:", old_admin_use)

print()
print("People who knew OLD-ADMIN-000 still worked:", people_who_knew_old_admin)

if "OLD-ADMIN-000" in used_retired_keycards:
    print("Clue: the retired admin keycard was used during the critical window.")

if people_who_knew_old_admin == {"Eleanor Hartley", "Mikhail Volkov"}:
    print("Clue: only Eleanor Hartley and Mikhail Volkov are recorded as knowing the old admin card still worked.")
